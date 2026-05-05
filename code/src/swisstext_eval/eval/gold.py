from __future__ import annotations

import re
from dataclasses import dataclass

from swisstext_eval.io.scenarios import Scenario, TaskStateLabel


_COMMAND_RE = re.compile(
    r"^an\s+(?P<unit>.+?)\s+von\s+einsatzleitung\b[,:]?\s+befehl:\s*(?P<task>.+?)\s*,?\s*antworten$",
    flags=re.IGNORECASE,
)


@dataclass(frozen=True)
class TaskTransition:
    task_id: str
    assignment_prefix: int | None
    completion_prefix: int | None


def _normalize(text: str | None) -> str:
    if text is None:
        return ""
    return " ".join(text.lower().split())

def _extract_commands(scenario: Scenario) -> list[tuple[int, str, str]]:
    commands: list[tuple[int, str, str]] = []
    for message in scenario.messages:
        match = _COMMAND_RE.match(_normalize(message.text))
        if not match:
            continue
        unit = match.group("unit").strip()
        task_phrase = match.group("task").strip()
        commands.append((message.message_id, unit, task_phrase))
    return commands


def _find_completion_prefix(scenario: Scenario, gold: TaskStateLabel) -> int | None:
    if gold.completion_message_id is not None:
        return gold.completion_message_id
    if not gold.completed:
        return None
    if not gold.completion_outcome:
        raise ValueError(
            f"Scenario {scenario.scenario_id} task {gold.task_id} is completed but has no completion annotation"
        )

    target = _normalize(gold.completion_outcome)
    for message in scenario.messages:
        if _normalize(message.text) == target:
            return message.message_id
    raise ValueError(
        f"Scenario {scenario.scenario_id} task {gold.task_id} completion_outcome did not match any message; "
        "add completion_message_id"
    )


def _find_assignment_prefix(
    scenario: Scenario,
    gold: TaskStateLabel,
    completion_prefix: int | None,
) -> int | None:
    if gold.assignment_message_id is not None:
        return gold.assignment_message_id
    if not gold.assigned:
        return None
    if not gold.assigned_unit:
        return None

    unit_norm = _normalize(gold.assigned_unit)
    commands = _extract_commands(scenario)
    relevant: list[int] = []
    for idx, unit, _phrase in commands:
        if completion_prefix is not None and idx > completion_prefix:
            continue
        if unit_norm in _normalize(unit):
            relevant.append(idx)

    if not relevant:
        raise ValueError(
            f"Scenario {scenario.scenario_id} task {gold.task_id} has no command to assigned unit {gold.assigned_unit!r}; "
            "add assignment_message_id"
        )
    if len(relevant) == 1:
        return relevant[0]

    raise ValueError(
        f"Scenario {scenario.scenario_id} task {gold.task_id} has multiple candidate assignment commands for unit "
        f"{gold.assigned_unit!r}: {relevant}; add assignment_message_id"
    )


def derive_task_transitions(scenario: Scenario) -> dict[str, TaskTransition]:
    transitions: dict[str, TaskTransition] = {}

    for gold in scenario.gold_task_states:
        completion_prefix = _find_completion_prefix(scenario, gold)
        assignment_prefix = (
            _find_assignment_prefix(
                scenario,
                gold=gold,
                completion_prefix=completion_prefix,
            )
            if gold.assigned
            else None
        )

        if assignment_prefix is not None and completion_prefix is not None and assignment_prefix > completion_prefix:
            assignment_prefix = completion_prefix

        transitions[gold.task_id] = TaskTransition(
            task_id=gold.task_id,
            assignment_prefix=assignment_prefix,
            completion_prefix=completion_prefix,
        )

    return transitions


def derive_prefix_gold_states(scenario: Scenario, prefix_index: int) -> list[TaskStateLabel]:
    if prefix_index < 1 or prefix_index > len(scenario.messages):
        raise ValueError(f"prefix_index must be in [1, {len(scenario.messages)}]")

    transitions = derive_task_transitions(scenario)
    gold_by_task = {item.task_id: item for item in scenario.gold_task_states}

    prefix_states: list[TaskStateLabel] = []
    for task in scenario.predefined_tasks:
        gold_final = gold_by_task[task.task_id]
        transition = transitions[task.task_id]

        assigned = (
            transition.assignment_prefix is not None and prefix_index >= transition.assignment_prefix and gold_final.assigned
        )
        completed = (
            transition.completion_prefix is not None and prefix_index >= transition.completion_prefix and gold_final.completed
        )

        assigned_unit = gold_final.assigned_unit if assigned else None
        completion_outcome = gold_final.completion_outcome if completed else None

        prefix_states.append(
            TaskStateLabel(
                task_id=task.task_id,
                assigned=assigned,
                assigned_unit=assigned_unit,
                completed=completed,
                completion_outcome=completion_outcome,
            )
        )

    return prefix_states
