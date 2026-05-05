from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class PredictedTaskState:
    task_id: str
    assigned: bool
    assigned_unit: str | None
    completed: bool
    completion_outcome: str | None


@dataclass(frozen=True)
class ParsedPrediction:
    task_states: list[PredictedTaskState]


def _require_non_empty_str(value: Any, field_name: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field_name} must be a non-empty string")
    return value.strip()


def _extract_first_json_object(raw_response: str) -> str | None:
    start = raw_response.find("{")
    if start < 0:
        return None

    depth = 0
    in_string = False
    escaped = False
    for idx in range(start, len(raw_response)):
        ch = raw_response[idx]
        if in_string:
            if escaped:
                escaped = False
            elif ch == "\\":
                escaped = True
            elif ch == '"':
                in_string = False
            continue

        if ch == '"':
            in_string = True
            continue
        if ch == "{":
            depth += 1
            continue
        if ch == "}":
            depth -= 1
            if depth == 0:
                return raw_response[start : idx + 1]
            continue

    return None


def _parse_task_states(task_states_raw: Any) -> list[PredictedTaskState]:
    if not isinstance(task_states_raw, list):
        raise ValueError("'task_states' must be a list")

    parsed: list[PredictedTaskState] = []
    for idx, item in enumerate(task_states_raw, start=1):
        if not isinstance(item, dict):
            raise ValueError(f"task_states[{idx}] must be an object")

        task_id = _require_non_empty_str(item.get("task_id"), f"task_states[{idx}].task_id")
        assigned = item.get("assigned")
        assigned_unit = item.get("assigned_unit")
        completed = item.get("completed")
        completion_outcome = item.get("completion_outcome")

        if not isinstance(assigned, bool):
            raise ValueError(f"task_states[{idx}].assigned must be boolean")
        if not isinstance(completed, bool):
            raise ValueError(f"task_states[{idx}].completed must be boolean")
        if assigned_unit is not None and not isinstance(assigned_unit, str):
            raise ValueError(f"task_states[{idx}].assigned_unit must be string or null")
        if completion_outcome is not None and not isinstance(completion_outcome, str):
            raise ValueError(f"task_states[{idx}].completion_outcome must be string or null")

        assigned_unit_value = assigned_unit.strip() if isinstance(assigned_unit, str) and assigned_unit.strip() else None
        completion_outcome_value = (
            completion_outcome.strip() if isinstance(completion_outcome, str) and completion_outcome.strip() else None
        )

        if not assigned and assigned_unit_value is not None:
            raise ValueError(f"task_states[{idx}] has assigned=false but assigned_unit is not null")
        if completed and not assigned:
            raise ValueError(f"task_states[{idx}] has completed=true but assigned=false")

        parsed.append(
            PredictedTaskState(
                task_id=task_id,
                assigned=assigned,
                assigned_unit=assigned_unit_value,
                completed=completed,
                completion_outcome=completion_outcome_value,
            )
        )

    return parsed


def parse_prediction(raw_response: str) -> ParsedPrediction:
    try:
        data = json.loads(raw_response)
    except json.JSONDecodeError as exc:
        candidate = _extract_first_json_object(raw_response)
        if candidate is None:
            raise ValueError(f"Invalid JSON response: {exc}") from exc
        try:
            data = json.loads(candidate)
        except json.JSONDecodeError as inner_exc:
            raise ValueError(f"Invalid JSON response: {inner_exc}") from inner_exc

    return parse_prediction_object(data)


def parse_prediction_object(data: Any) -> ParsedPrediction:
    if not isinstance(data, dict):
        raise ValueError("Response must be a JSON object")
    if "task_states" not in data:
        raise ValueError("Response must include 'task_states'")

    task_states = _parse_task_states(data["task_states"])
    return ParsedPrediction(task_states=task_states)
