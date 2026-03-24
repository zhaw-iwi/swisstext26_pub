from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class Message:
    message_id: int
    speaker: str | None
    text: str


@dataclass(frozen=True)
class PredefinedTask:
    task_id: str
    task_name: str


@dataclass(frozen=True)
class TaskStateLabel:
    task_id: str
    assigned: bool
    assigned_unit: str | None
    completed: bool
    completion_outcome: str | None
    assignment_message_id: int | None = None
    completion_message_id: int | None = None


@dataclass(frozen=True)
class Scenario:
    scenario_id: str
    scenario_name: str
    metadata: dict[str, Any]
    messages: list[Message]
    predefined_tasks: list[PredefinedTask]
    gold_task_states: list[TaskStateLabel]


def _require(value: Any, field_name: str) -> Any:
    if value is None:
        raise ValueError(f"Missing required field: {field_name}")
    return value


def _non_empty_string(value: Any, field_name: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field_name} must be a non-empty string")
    return value.strip()


def _parse_message(raw: dict[str, Any]) -> Message:
    message_id = _require(raw.get("id"), "messages[].id")
    if not isinstance(message_id, int):
        raise ValueError("messages[].id must be integer")

    speaker = raw.get("speaker")
    text = _non_empty_string(raw.get("text"), "messages[].text")

    if speaker is not None and (not isinstance(speaker, str) or not speaker.strip()):
        raise ValueError("messages[].speaker must be string or null")

    return Message(message_id=message_id, speaker=speaker.strip() if isinstance(speaker, str) else None, text=text)


def _parse_predefined_task(raw: dict[str, Any]) -> PredefinedTask:
    task_id = _non_empty_string(raw.get("task_id"), "predefined_tasks[].task_id")
    task_name = _non_empty_string(raw.get("task_name"), "predefined_tasks[].task_name")
    return PredefinedTask(task_id=task_id, task_name=task_name)


def _parse_gold_task_state(raw: dict[str, Any]) -> TaskStateLabel:
    task_id = _non_empty_string(raw.get("task_id"), "gold_task_states[].task_id")
    assigned = raw.get("assigned")
    completed = raw.get("completed")
    assigned_unit = raw.get("assigned_unit")
    completion_outcome = raw.get("completion_outcome")
    assignment_message_id = raw.get("assignment_message_id")
    completion_message_id = raw.get("completion_message_id")

    if not isinstance(assigned, bool):
        raise ValueError("gold_task_states[].assigned must be boolean")
    if not isinstance(completed, bool):
        raise ValueError("gold_task_states[].completed must be boolean")
    if assigned_unit is not None and (not isinstance(assigned_unit, str) or not assigned_unit.strip()):
        raise ValueError("gold_task_states[].assigned_unit must be string or null")
    if completion_outcome is not None and (not isinstance(completion_outcome, str) or not completion_outcome.strip()):
        raise ValueError("gold_task_states[].completion_outcome must be string or null")
    if assignment_message_id is not None and not isinstance(assignment_message_id, int):
        raise ValueError("gold_task_states[].assignment_message_id must be integer or null")
    if completion_message_id is not None and not isinstance(completion_message_id, int):
        raise ValueError("gold_task_states[].completion_message_id must be integer or null")

    if not assigned and assigned_unit is not None:
        raise ValueError("gold_task_states[] has assigned=false but assigned_unit is not null")
    if completed and not assigned:
        raise ValueError("gold_task_states[] has completed=true but assigned=false")
    if not assigned and assignment_message_id is not None:
        raise ValueError("gold_task_states[] has assigned=false but assignment_message_id is not null")
    if assigned and assignment_message_id is None:
        assignment_message_id = None
    if not completed and completion_message_id is not None:
        raise ValueError("gold_task_states[] has completed=false but completion_message_id is not null")
    if completed and completion_message_id is None and completion_outcome is None:
        raise ValueError("gold_task_states[] has completed=true but neither completion_message_id nor completion_outcome is set")

    return TaskStateLabel(
        task_id=task_id,
        assigned=assigned,
        assigned_unit=assigned_unit.strip() if isinstance(assigned_unit, str) else None,
        completed=completed,
        completion_outcome=completion_outcome.strip() if isinstance(completion_outcome, str) else None,
        assignment_message_id=assignment_message_id,
        completion_message_id=completion_message_id,
    )


def parse_scenario(raw: dict[str, Any]) -> Scenario:
    scenario_id = _non_empty_string(raw.get("scenario_id"), "scenario_id")
    scenario_name = _non_empty_string(raw.get("scenario_name"), "scenario_name")

    messages_raw = _require(raw.get("messages"), "messages")
    tasks_raw = _require(raw.get("predefined_tasks"), "predefined_tasks")
    gold_raw = _require(raw.get("gold_task_states"), "gold_task_states")

    if not isinstance(messages_raw, list) or not messages_raw:
        raise ValueError("messages must be a non-empty list")
    if not isinstance(tasks_raw, list) or not tasks_raw:
        raise ValueError("predefined_tasks must be a non-empty list")
    if not isinstance(gold_raw, list) or not gold_raw:
        raise ValueError("gold_task_states must be a non-empty list")

    messages = [_parse_message(item) for item in messages_raw]
    predefined_tasks = [_parse_predefined_task(item) for item in tasks_raw]
    gold_task_states = [_parse_gold_task_state(item) for item in gold_raw]

    message_ids = [m.message_id for m in messages]
    expected = list(range(1, len(messages) + 1))
    if message_ids != expected:
        raise ValueError("messages[].id values must be sequential integers starting at 1")
    message_id_set = set(message_ids)

    task_ids = [task.task_id for task in predefined_tasks]
    if len(set(task_ids)) != len(task_ids):
        raise ValueError("predefined_tasks contains duplicate task_id values")

    gold_ids = [state.task_id for state in gold_task_states]
    if len(set(gold_ids)) != len(gold_ids):
        raise ValueError("gold_task_states contains duplicate task_id values")

    if set(task_ids) != set(gold_ids):
        missing = sorted(set(task_ids) - set(gold_ids))
        extra = sorted(set(gold_ids) - set(task_ids))
        raise ValueError(f"Task/gold task_id mismatch: missing={missing}, extra={extra}")

    for state in gold_task_states:
        if state.assignment_message_id is not None and state.assignment_message_id not in message_id_set:
            raise ValueError(
                f"gold_task_states[] assignment_message_id {state.assignment_message_id} is not a valid message id"
            )
        if state.completion_message_id is not None and state.completion_message_id not in message_id_set:
            raise ValueError(
                f"gold_task_states[] completion_message_id {state.completion_message_id} is not a valid message id"
            )
        if (
            state.assignment_message_id is not None
            and state.completion_message_id is not None
            and state.assignment_message_id > state.completion_message_id
        ):
            raise ValueError("gold_task_states[] assignment_message_id must be <= completion_message_id")

    return Scenario(
        scenario_id=scenario_id,
        scenario_name=scenario_name,
        metadata=raw.get("metadata", {}),
        messages=messages,
        predefined_tasks=predefined_tasks,
        gold_task_states=gold_task_states,
    )


def load_scenarios(data_dir: Path, selected_scenarios: list[str] | None = None) -> list[Scenario]:
    selected = set(selected_scenarios or [])
    scenario_files = sorted(data_dir.glob("*.json"))
    if not scenario_files:
        raise FileNotFoundError(f"No scenario files found in {data_dir}")

    scenarios: list[Scenario] = []
    for path in scenario_files:
        with path.open("r", encoding="utf-8-sig") as handle:
            raw = json.load(handle)
        scenario = parse_scenario(raw)
        if selected and scenario.scenario_id not in selected:
            continue
        scenarios.append(scenario)

    if selected and not scenarios:
        raise ValueError("Selected scenarios were requested but none were found")

    return scenarios
