from __future__ import annotations

from typing import Any, Callable

import pandas as pd

from swisstext_eval.config import NotebookConfig, ensure_batch_directories
from swisstext_eval.pipeline import count_work_items_for_run, run_single_run
from swisstext_eval.reporting.figures import export_figures
from swisstext_eval.reporting.tables import export_batch_tables
from swisstext_eval.utils.io import write_json


def count_total_work_items(config: NotebookConfig, n_runs: int | None = None) -> int:
    run_count = n_runs if n_runs is not None else config.experiment.run_count
    return sum(count_work_items_for_run(config, run_index) for run_index in range(1, run_count + 1))


def run_repeated_evaluation(
    config: NotebookConfig,
    n_runs: int | None = None,
    progress_callback: Callable[[int, int, dict[str, Any]], None] | None = None,
) -> dict[str, Any]:
    run_count = n_runs if n_runs is not None else config.experiment.run_count
    if run_count < 1:
        raise ValueError("run_count must be >= 1")

    batch_dirs = ensure_batch_directories(config)

    run_records: list[dict[str, Any]] = []
    all_condition_rows: list[pd.DataFrame] = []
    terminal_convergence_rows: list[pd.DataFrame] = []

    total_work_items = count_total_work_items(config, run_count)
    progress_offset = 0

    for run_index in range(1, run_count + 1):
        run_work_items = count_work_items_for_run(config, run_index)

        def _progress(current: int, total: int, item) -> None:
            if progress_callback is None:
                return
            payload = {
                "run_index": run_index,
                "run_count": run_count,
                "scenario_id": item.scenario_id,
                "structure_condition": item.structure_condition,
                "processing_mode": item.processing_mode,
                "prefix_index": item.prefix_index,
            }
            progress_callback(current, total, payload)

        run_result = run_single_run(
            config,
            run_index,
            progress_callback=_progress if progress_callback is not None else None,
            progress_start=progress_offset,
            progress_total=total_work_items,
        )
        run_records.append(run_result)
        progress_offset += run_work_items

        run_rows_path = run_result.get("all_condition_rows_csv")
        if run_rows_path:
            all_condition_rows.append(pd.read_csv(run_rows_path))
        terminal_rows_path = run_result.get("terminal_convergence_per_scenario_csv")
        if terminal_rows_path:
            terminal_convergence_rows.append(pd.read_csv(terminal_rows_path))

    if not all_condition_rows:
        raise RuntimeError("No per-run condition rows were produced")

    combined_rows = pd.concat(all_condition_rows, ignore_index=True)
    combined_terminal_rows = (
        pd.concat(terminal_convergence_rows, ignore_index=True) if terminal_convergence_rows else pd.DataFrame()
    )
    table_outputs = export_batch_tables(
        output_dir=batch_dirs["tables"],
        all_condition_rows=combined_rows,
        terminal_convergence_rows=combined_terminal_rows,
    )

    figure_outputs = {}
    if config.evaluation.export_figures:
        figure_outputs = export_figures(table_outputs, batch_dirs["figures"])

    manifest = {
        "batch_id": batch_dirs["root"].name,
        "batch_dir": str(batch_dirs["root"]),
        "run_count": run_count,
        "runs": run_records,
        "table_outputs": {k: str(v) for k, v in table_outputs.items()},
        "figure_outputs": figure_outputs,
    }
    write_json(batch_dirs["root"] / "batch_manifest.json", manifest)

    result = {
        "batch_id": batch_dirs["root"].name,
        "batch_dir": str(batch_dirs["root"]),
        "run_count": run_count,
        "manifest": str(batch_dirs["root"] / "batch_manifest.json"),
    }
    result.update({k: str(v) for k, v in table_outputs.items()})
    result.update(figure_outputs)
    return result
