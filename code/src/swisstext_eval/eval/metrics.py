from __future__ import annotations

from dataclasses import dataclass
from statistics import mean

from swisstext_eval.eval.gold import TaskTransition
from swisstext_eval.io.scenarios import Scenario, TaskStateLabel
from swisstext_eval.parsing.predictions import ParsedPrediction, PredictedTaskState


@dataclass(frozen=True)
class FullMetricsRow:
    run_id: str
    run_index: int
    scenario_id: str
    structure_condition: str
    processing_mode: str
    assignment_accuracy: float
    unit_assignment_accuracy: float
    completion_accuracy: float
    final_state_accuracy: float
    completion_outcome_accuracy: float

    def to_row(self) -> dict[str, str | int | float]:
        return {
            "run_id": self.run_id,
            "run_index": self.run_index,
            "scenario_id": self.scenario_id,
            "structure_condition": self.structure_condition,
            "processing_mode": self.processing_mode,
            "assignment_accuracy": self.assignment_accuracy,
            "unit_assignment_accuracy": self.unit_assignment_accuracy,
            "completion_accuracy": self.completion_accuracy,
            "final_state_accuracy": self.final_state_accuracy,
            "completion_outcome_accuracy": self.completion_outcome_accuracy,
        }


@dataclass(frozen=True)
class IncrementalPrefixRow:
    run_id: str
    run_index: int
    scenario_id: str
    structure_condition: str
    processing_mode: str
    prefix_index: int
    assignment_accuracy: float
    unit_assignment_accuracy: float
    completion_accuracy: float
    current_state_accuracy: float

    def to_row(self) -> dict[str, str | int | float]:
        return {
            "run_id": self.run_id,
            "run_index": self.run_index,
            "scenario_id": self.scenario_id,
            "structure_condition": self.structure_condition,
            "processing_mode": self.processing_mode,
            "prefix_index": self.prefix_index,
            "assignment_accuracy": self.assignment_accuracy,
            "unit_assignment_accuracy": self.unit_assignment_accuracy,
            "completion_accuracy": self.completion_accuracy,
            "current_state_accuracy": self.current_state_accuracy,
        }


@dataclass(frozen=True)
class IncrementalMetricsRow:
    run_id: str
    run_index: int
    scenario_id: str
    structure_condition: str
    processing_mode: str
    assignment_accuracy: float
    unit_assignment_accuracy: float
    completion_accuracy: float
    current_state_accuracy: float
    assignment_detection_latency: float
    completion_detection_latency: float
    assignment_detection_miss_rate: float
    completion_detection_miss_rate: float

    def to_row(self) -> dict[str, str | int | float]:
        return {
            "run_id": self.run_id,
            "run_index": self.run_index,
            "scenario_id": self.scenario_id,
            "structure_condition": self.structure_condition,
            "processing_mode": self.processing_mode,
            "assignment_accuracy": self.assignment_accuracy,
            "unit_assignment_accuracy": self.unit_assignment_accuracy,
            "completion_accuracy": self.completion_accuracy,
            "current_state_accuracy": self.current_state_accuracy,
            "assignment_detection_latency": self.assignment_detection_latency,
            "completion_detection_latency": self.completion_detection_latency,
            "assignment_detection_miss_rate": self.assignment_detection_miss_rate,
            "completion_detection_miss_rate": self.completion_detection_miss_rate,
        }


def _normalize_text(value: str | None) -> str | None:
    if value is None:
        return None
    normalized = " ".join(value.strip().lower().split())
    return normalized if normalized else None


def _state(assigned: bool, completed: bool) -> str:
    if completed:
        return "COMPLETED"
    if assigned:
        return "ASSIGNED"
    return "NOT_ASSIGNED"


def _safe_ratio(correct: int, support: int) -> float:
    if support == 0:
        return 0.0
    return correct / support


def _prediction_by_task_id(prediction: ParsedPrediction) -> dict[str, PredictedTaskState]:
    return {item.task_id: item for item in prediction.task_states}


def _compute_state_metrics(gold_states: list[TaskStateLabel], prediction: ParsedPrediction) -> tuple[float, float, float, float, float]:
    gold_by_id = {item.task_id: item for item in gold_states}
    pred_by_id = _prediction_by_task_id(prediction)

    assignment_correct = 0
    completion_correct = 0
    state_correct = 0

    unit_correct = 0
    unit_support = 0

    outcome_correct = 0
    outcome_support = 0

    for task_id, gold in gold_by_id.items():
        pred = pred_by_id.get(task_id)

        pred_assigned = pred.assigned if pred is not None else False
        pred_completed = pred.completed if pred is not None else False
        pred_unit = _normalize_text(pred.assigned_unit) if pred is not None else None
        pred_outcome = _normalize_text(pred.completion_outcome) if pred is not None else None

        gold_unit = _normalize_text(gold.assigned_unit)
        gold_outcome = _normalize_text(gold.completion_outcome)

        if pred_assigned == gold.assigned:
            assignment_correct += 1
        if pred_completed == gold.completed:
            completion_correct += 1
        if _state(pred_assigned, pred_completed) == _state(gold.assigned, gold.completed):
            state_correct += 1

        if gold.assigned or pred_assigned:
            unit_support += 1
            if pred_unit == gold_unit:
                unit_correct += 1

        if gold_outcome is not None or pred_outcome is not None:
            outcome_support += 1
            if pred_outcome == gold_outcome:
                outcome_correct += 1

    support = len(gold_by_id)
    return (
        _safe_ratio(assignment_correct, support),
        _safe_ratio(unit_correct, unit_support),
        _safe_ratio(completion_correct, support),
        _safe_ratio(state_correct, support),
        _safe_ratio(outcome_correct, outcome_support),
    )


def compute_full_metrics(
    *,
    run_id: str,
    run_index: int,
    scenario: Scenario,
    structure_condition: str,
    prediction: ParsedPrediction,
) -> FullMetricsRow:
    assignment_acc, unit_acc, completion_acc, final_state_acc, outcome_acc = _compute_state_metrics(
        scenario.gold_task_states,
        prediction,
    )
    return FullMetricsRow(
        run_id=run_id,
        run_index=run_index,
        scenario_id=scenario.scenario_id,
        structure_condition=structure_condition,
        processing_mode="full_transcript",
        assignment_accuracy=assignment_acc,
        unit_assignment_accuracy=unit_acc,
        completion_accuracy=completion_acc,
        final_state_accuracy=final_state_acc,
        completion_outcome_accuracy=outcome_acc,
    )


def _mean_or_zero(values: list[float]) -> float:
    return mean(values) if values else 0.0


def _first_correct_detection_prefix(
    task_id: str,
    threshold_prefix: int,
    predictions_by_prefix: dict[int, ParsedPrediction],
    matcher,
) -> int | None:
    for prefix in sorted(predictions_by_prefix):
        if prefix < threshold_prefix:
            continue
        pred = predictions_by_prefix[prefix]
        pred_by_id = _prediction_by_task_id(pred)
        candidate = pred_by_id.get(task_id)
        if candidate is not None and matcher(candidate):
            return prefix
    return None


def _has_correct_assigned_unit(pred: PredictedTaskState, gold: TaskStateLabel) -> bool:
    gold_unit = _normalize_text(gold.assigned_unit)
    if gold_unit is None:
        return True
    return _normalize_text(pred.assigned_unit) == gold_unit


def _detection_latencies(
    *,
    gold_states: list[TaskStateLabel],
    transitions: dict[str, TaskTransition],
    predictions_by_prefix: dict[int, ParsedPrediction],
) -> tuple[float, float, float, float]:
    gold_by_task = {item.task_id: item for item in gold_states}
    assignment_latencies: list[float] = []
    completion_latencies: list[float] = []
    assignment_total = 0
    assignment_missed = 0
    completion_total = 0
    completion_missed = 0

    for task_id, transition in transitions.items():
        gold = gold_by_task[task_id]
        if transition.assignment_prefix is not None:
            assignment_total += 1
            detected = _first_correct_detection_prefix(
                task_id,
                transition.assignment_prefix,
                predictions_by_prefix,
                lambda p, gold=gold: p.assigned and _has_correct_assigned_unit(p, gold),
            )
            if detected is not None:
                assignment_latencies.append(float(detected - transition.assignment_prefix))
            else:
                assignment_missed += 1

        if transition.completion_prefix is not None:
            completion_total += 1
            detected = _first_correct_detection_prefix(
                task_id,
                transition.completion_prefix,
                predictions_by_prefix,
                lambda p, gold=gold: p.assigned and p.completed and _has_correct_assigned_unit(p, gold),
            )
            if detected is not None:
                completion_latencies.append(float(detected - transition.completion_prefix))
            else:
                completion_missed += 1

    return (
        _mean_or_zero(assignment_latencies),
        _mean_or_zero(completion_latencies),
        _safe_ratio(assignment_missed, assignment_total),
        _safe_ratio(completion_missed, completion_total),
    )


def compute_incremental_metrics(
    *,
    run_id: str,
    run_index: int,
    scenario: Scenario,
    structure_condition: str,
    predictions_by_prefix: dict[int, ParsedPrediction],
    gold_by_prefix: dict[int, list[TaskStateLabel]],
    transitions: dict[str, TaskTransition],
) -> tuple[IncrementalMetricsRow, list[IncrementalPrefixRow]]:
    prefix_rows: list[IncrementalPrefixRow] = []

    for prefix in sorted(gold_by_prefix):
        prediction = predictions_by_prefix[prefix]
        assignment_acc, unit_acc, completion_acc, state_acc, _outcome_acc = _compute_state_metrics(
            gold_by_prefix[prefix],
            prediction,
        )
        prefix_rows.append(
            IncrementalPrefixRow(
                run_id=run_id,
                run_index=run_index,
                scenario_id=scenario.scenario_id,
                structure_condition=structure_condition,
                processing_mode="incremental",
                prefix_index=prefix,
                assignment_accuracy=assignment_acc,
                unit_assignment_accuracy=unit_acc,
                completion_accuracy=completion_acc,
                current_state_accuracy=state_acc,
            )
        )

    (
        assignment_latency,
        completion_latency,
        assignment_miss_rate,
        completion_miss_rate,
    ) = _detection_latencies(
        gold_states=scenario.gold_task_states,
        transitions=transitions,
        predictions_by_prefix=predictions_by_prefix,
    )

    metrics_row = IncrementalMetricsRow(
        run_id=run_id,
        run_index=run_index,
        scenario_id=scenario.scenario_id,
        structure_condition=structure_condition,
        processing_mode="incremental",
        assignment_accuracy=_mean_or_zero([row.assignment_accuracy for row in prefix_rows]),
        unit_assignment_accuracy=_mean_or_zero([row.unit_assignment_accuracy for row in prefix_rows]),
        completion_accuracy=_mean_or_zero([row.completion_accuracy for row in prefix_rows]),
        current_state_accuracy=_mean_or_zero([row.current_state_accuracy for row in prefix_rows]),
        assignment_detection_latency=assignment_latency,
        completion_detection_latency=completion_latency,
        assignment_detection_miss_rate=assignment_miss_rate,
        completion_detection_miss_rate=completion_miss_rate,
    )

    return metrics_row, prefix_rows
