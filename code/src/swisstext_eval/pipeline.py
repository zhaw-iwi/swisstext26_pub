from __future__ import annotations

import json
from dataclasses import asdict
from pathlib import Path
from typing import Any, Callable, TypeVar

from swisstext_eval.config import NotebookConfig, ensure_run_directories, run_dir, run_id_for_index
from swisstext_eval.eval.gold import derive_prefix_gold_states, derive_task_transitions
from swisstext_eval.eval.metrics import (
    FullMetricsRow,
    IncrementalMetricsRow,
    IncrementalPrefixRow,
    compute_full_metrics,
    compute_incremental_metrics,
)
from swisstext_eval.eval.prefixes import prefix_indices_for_scenario
from swisstext_eval.eval.work import FULL_PREFIX_INDEX, WorkItem, WorkKey
from swisstext_eval.io.artifacts import (
    init_request_artifact,
    is_completed_artifact,
    load_request_artifact,
    save_request_artifact,
    utc_now_iso,
)
from swisstext_eval.io.scenarios import Scenario, load_scenarios
from swisstext_eval.llm.client import LLMClient
from swisstext_eval.parsing.predictions import ParsedPrediction, parse_prediction, parse_prediction_object
from swisstext_eval.prompts.builders import build_prompt_payload, load_prompt
from swisstext_eval.reporting.figures import export_figures
from swisstext_eval.reporting.tables import export_run_tables
from swisstext_eval.transforms.transcript_conditions import render_transcript, render_transcript_prefix
from swisstext_eval.utils.io import write_json, write_text


OUTPUT_SCHEMA = (
    '{"task_states":[{"task_id":"string","assigned":"boolean",'
    '"assigned_unit":"string|null","completed":"boolean",'
    '"completion_outcome":"string|null"}]}'
)

OUTPUT_JSON_SCHEMA = {
    "type": "object",
    "additionalProperties": False,
    "required": ["task_states"],
    "properties": {
        "task_states": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "required": [
                    "task_id",
                    "assigned",
                    "assigned_unit",
                    "completed",
                    "completion_outcome",
                ],
                "properties": {
                    "task_id": {"type": "string"},
                    "assigned": {"type": "boolean"},
                    "assigned_unit": {"type": ["string", "null"]},
                    "completed": {"type": "boolean"},
                    "completion_outcome": {"type": ["string", "null"]},
                },
            },
        }
    },
}


def _output_stem(item: WorkItem) -> str:
    suffix = "full" if item.prefix_index == FULL_PREFIX_INDEX else f"prefix_{item.prefix_index:03d}"
    return f"{item.scenario_id}__{item.structure_condition}__{item.processing_mode}__{suffix}"


def _build_work_items(config: NotebookConfig, run_index: int, scenarios: list[Scenario]) -> list[WorkItem]:
    run_id = run_id_for_index(config, run_index)
    items: list[WorkItem] = []

    for scenario in scenarios:
        for structure_condition in config.experiment.selected_structure_conditions:
            for processing_mode in config.experiment.selected_processing_modes:
                if processing_mode == "full_transcript":
                    items.append(
                        WorkItem(
                            run_index=run_index,
                            run_id=run_id,
                            scenario_id=scenario.scenario_id,
                            structure_condition=structure_condition,
                            processing_mode=processing_mode,
                            prefix_index=FULL_PREFIX_INDEX,
                        )
                    )
                    continue

                if processing_mode != "incremental":
                    raise ValueError(f"Unsupported processing mode: {processing_mode}")

                for prefix_index in prefix_indices_for_scenario(scenario, config.experiment.incremental_prefix_policy):
                    items.append(
                        WorkItem(
                            run_index=run_index,
                            run_id=run_id,
                            scenario_id=scenario.scenario_id,
                            structure_condition=structure_condition,
                            processing_mode=processing_mode,
                            prefix_index=prefix_index,
                        )
                    )

    if config.debug.limit_work_items is not None:
        return items[: config.debug.limit_work_items]
    return items


def count_work_items_for_run(config: NotebookConfig, run_index: int) -> int:
    scenarios = load_scenarios(config.paths.input_data_dir, config.experiment.selected_scenarios)
    if config.debug.limit_scenarios is not None:
        scenarios = scenarios[: config.debug.limit_scenarios]
    return len(_build_work_items(config, run_index, scenarios))


T = TypeVar("T")


def _chunked(items: list[T], chunk_size: int) -> list[list[T]]:
    if chunk_size < 1:
        raise ValueError("api_batch_size must be >= 1")
    return [items[i : i + chunk_size] for i in range(0, len(items), chunk_size)]


def _transcript_for_item(scenario: Scenario, item: WorkItem) -> str:
    if item.processing_mode == "full_transcript":
        return render_transcript(scenario, item.structure_condition)
    return render_transcript_prefix(scenario, item.structure_condition, item.prefix_index)


def _prediction_from_artifact(artifact: dict[str, Any]) -> ParsedPrediction:
    parsed_payload = artifact.get("parsed_output")
    if isinstance(parsed_payload, dict):
        return parse_prediction_object(parsed_payload)
    raw = artifact.get("response_raw_text")
    if isinstance(raw, str):
        return parse_prediction(raw)
    return ParsedPrediction(task_states=[])


def _eval_work_item(
    *,
    config: NotebookConfig,
    item: WorkItem,
    scenario: Scenario,
    dirs: dict[str, Path],
    client: LLMClient,
    system_prompt: str,
    user_template: str,
) -> tuple[ParsedPrediction, int]:
    key = WorkKey.from_item(item)
    existing = load_request_artifact(dirs["requests"], key)

    if config.experiment.resume_behavior == "skip_completed" and is_completed_artifact(existing):
        return _prediction_from_artifact(existing), 0

    transcript = _transcript_for_item(scenario, item)
    if config.debug.save_transformed_inputs:
        write_text(dirs["inputs_transformed"] / f"{_output_stem(item)}.txt", transcript)

    prompt_payload = build_prompt_payload(
        system_prompt=system_prompt,
        user_template=user_template,
        scenario_id=scenario.scenario_id,
        structure_condition=item.structure_condition,
        processing_mode=item.processing_mode,
        prefix_index=item.prefix_index,
        transcript=transcript,
        predefined_tasks=scenario.predefined_tasks,
        output_schema=OUTPUT_SCHEMA,
    )

    model_settings = {
        "model_name": config.provider.model_name,
        "temperature": config.provider.temperature,
        "max_tokens": config.provider.max_tokens,
        "timeout_seconds": config.provider.timeout_seconds,
        "retry_count": config.provider.retry_count,
        "provider_mode": config.provider.mode,
        "prompt_version_tag": config.experiment.prompt_version_tag,
    }

    artifact = init_request_artifact(item, prompt_payload, model_settings)

    try:
        response = client.run(prompt_payload["system"], prompt_payload["user"], json_schema=OUTPUT_JSON_SCHEMA)
        artifact["response_timestamp"] = utc_now_iso()
        artifact["response_raw_text"] = response.content

        parsed = parse_prediction(response.content)
        artifact["parsed_output"] = asdict(parsed)
        artifact["status"] = "completed"
        save_request_artifact(dirs["requests"], key, artifact)

        stem = _output_stem(item)
        write_text(dirs["raw_responses"] / f"{stem}.json", response.content)
        write_json(dirs["parsed_predictions"] / f"{stem}.json", asdict(parsed))
        return parsed, 1
    except Exception as exc:  # noqa: BLE001
        artifact["response_timestamp"] = utc_now_iso()
        artifact["status"] = "failed"
        artifact["error"] = {
            "type": exc.__class__.__name__,
            "message": str(exc),
        }
        save_request_artifact(dirs["requests"], key, artifact)
        return ParsedPrediction(task_states=[]), 1


def run_single_run(
    config: NotebookConfig,
    run_index: int,
    progress_callback: Callable[[int, int, WorkItem], None] | None = None,
    progress_start: int = 0,
    progress_total: int | None = None,
) -> dict[str, Any]:
    dirs = ensure_run_directories(config, run_index)
    run_id = run_id_for_index(config, run_index)

    write_json(dirs["config"] / "run_config.json", config.to_dict())
    write_json(dirs["config"] / "run_metadata.json", {"run_id": run_id, "run_index": run_index})

    scenarios = load_scenarios(config.paths.input_data_dir, config.experiment.selected_scenarios)
    if config.debug.limit_scenarios is not None:
        scenarios = scenarios[: config.debug.limit_scenarios]

    scenario_by_id = {scenario.scenario_id: scenario for scenario in scenarios}
    work_items = _build_work_items(config, run_index, scenarios)

    system_prompt = load_prompt(config.prompts.system_prompt_path)
    user_template = load_prompt(config.prompts.user_prompt_template_path)

    client = LLMClient(
        model_name=config.provider.model_name,
        mode=config.provider.mode,
        api_key_env=config.provider.api_key_env,
        temperature=config.provider.temperature,
        max_tokens=config.provider.max_tokens,
        timeout_seconds=config.provider.timeout_seconds,
        retry_count=config.provider.retry_count,
    )

    full_predictions: dict[tuple[str, str], ParsedPrediction] = {}
    incremental_predictions: dict[tuple[str, str], dict[int, ParsedPrediction]] = {}
    provider_calls = 0
    processed_count = 0
    total_count = progress_total if progress_total is not None else len(work_items)

    for batch in _chunked(work_items, config.experiment.api_batch_size):
        for item in batch:
            scenario = scenario_by_id[item.scenario_id]
            parsed, call_cost = _eval_work_item(
                config=config,
                item=item,
                scenario=scenario,
                dirs=dirs,
                client=client,
                system_prompt=system_prompt,
                user_template=user_template,
            )
            provider_calls += call_cost

            if item.processing_mode == "full_transcript":
                full_predictions[(item.scenario_id, item.structure_condition)] = parsed
            else:
                bucket = incremental_predictions.setdefault((item.scenario_id, item.structure_condition), {})
                bucket[item.prefix_index] = parsed

            processed_count += 1
            if progress_callback is not None:
                progress_callback(progress_start + processed_count, total_count, item)

    full_rows: list[FullMetricsRow] = []
    incremental_rows: list[IncrementalMetricsRow] = []
    prefix_rows: list[IncrementalPrefixRow] = []

    for scenario in scenarios:
        transitions = derive_task_transitions(scenario)
        for structure_condition in config.experiment.selected_structure_conditions:
            if "full_transcript" in config.experiment.selected_processing_modes:
                full_pred = full_predictions[(scenario.scenario_id, structure_condition)]
                full_rows.append(
                    compute_full_metrics(
                        run_id=run_id,
                        run_index=run_index,
                        scenario=scenario,
                        structure_condition=structure_condition,
                        prediction=full_pred,
                    )
                )

            if "incremental" in config.experiment.selected_processing_modes:
                pred_by_prefix = incremental_predictions[(scenario.scenario_id, structure_condition)]
                gold_by_prefix = {
                    prefix: derive_prefix_gold_states(scenario, prefix)
                    for prefix in sorted(pred_by_prefix)
                }
                inc_row, per_prefix_rows = compute_incremental_metrics(
                    run_id=run_id,
                    run_index=run_index,
                    scenario=scenario,
                    structure_condition=structure_condition,
                    predictions_by_prefix=pred_by_prefix,
                    gold_by_prefix=gold_by_prefix,
                    transitions=transitions,
                )
                incremental_rows.append(inc_row)
                prefix_rows.extend(per_prefix_rows)

    outputs = export_run_tables(
        output_dir=dirs["tables"],
        full_rows=full_rows,
        incremental_rows=incremental_rows,
        prefix_rows=prefix_rows,
        export_prefix_level=config.evaluation.export_prefix_level_metrics,
    )

    figure_outputs: dict[str, str] = {}
    if config.evaluation.export_figures:
        figure_outputs = export_figures(outputs, dirs["figures"])

    manifest = {
        "run_id": run_id,
        "run_index": run_index,
        "run_dir": str(run_dir(config, run_index)),
        "num_work_items": len(work_items),
        "num_provider_calls": provider_calls,
        "table_outputs": {k: str(v) for k, v in outputs.items()},
        "figure_outputs": figure_outputs,
    }
    write_json(dirs["config"] / "run_manifest.json", manifest)

    response = {
        "run_id": run_id,
        "run_index": run_index,
        "run_dir": str(run_dir(config, run_index)),
        "num_work_items": len(work_items),
        "num_calls": provider_calls,
    }
    response.update({k: str(v) for k, v in outputs.items()})
    response.update(figure_outputs)
    return response


def run_evaluation(config: NotebookConfig) -> dict[str, Any]:
    return run_single_run(config, run_index=1)
