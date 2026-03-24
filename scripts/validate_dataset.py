from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def _load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8-sig") as handle:
        return json.load(handle)


def _is_non_empty_string(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def validate_scenario(path: Path) -> list[str]:
    errors: list[str] = []
    data = _load_json(path)

    for field in ("scenario_id", "scenario_name", "messages", "predefined_tasks", "gold_task_states"):
        if field not in data:
            errors.append(f"{path.name}: missing required field '{field}'")

    messages = data.get("messages")
    tasks = data.get("predefined_tasks")
    gold = data.get("gold_task_states")

    if not isinstance(messages, list) or not messages:
        errors.append(f"{path.name}: messages must be a non-empty list")
        return errors
    if not isinstance(tasks, list) or not tasks:
        errors.append(f"{path.name}: predefined_tasks must be a non-empty list")
        return errors
    if not isinstance(gold, list) or not gold:
        errors.append(f"{path.name}: gold_task_states must be a non-empty list")
        return errors

    message_ids: list[int] = []
    for idx, message in enumerate(messages, start=1):
        if not isinstance(message, dict):
            errors.append(f"{path.name}: messages[{idx}] must be an object")
            continue
        msg_id = message.get("id")
        if not isinstance(msg_id, int):
            errors.append(f"{path.name}: messages[{idx}].id must be int")
        else:
            message_ids.append(msg_id)
        if message.get("speaker") is not None and not _is_non_empty_string(message.get("speaker")):
            errors.append(f"{path.name}: messages[{idx}].speaker must be string or null")
        if not _is_non_empty_string(message.get("text")):
            errors.append(f"{path.name}: messages[{idx}].text must be non-empty string")

    if message_ids and message_ids != list(range(1, len(message_ids) + 1)):
        errors.append(f"{path.name}: message ids must be sequential starting from 1")

    task_ids: set[str] = set()
    for idx, task in enumerate(tasks, start=1):
        if not isinstance(task, dict):
            errors.append(f"{path.name}: predefined_tasks[{idx}] must be an object")
            continue
        task_id = task.get("task_id")
        task_name = task.get("task_name")
        if not _is_non_empty_string(task_id):
            errors.append(f"{path.name}: predefined_tasks[{idx}].task_id must be non-empty string")
        else:
            if task_id in task_ids:
                errors.append(f"{path.name}: duplicate predefined task_id '{task_id}'")
            task_ids.add(task_id)
        if not _is_non_empty_string(task_name):
            errors.append(f"{path.name}: predefined_tasks[{idx}].task_name must be non-empty string")

    gold_ids: set[str] = set()
    for idx, state in enumerate(gold, start=1):
        if not isinstance(state, dict):
            errors.append(f"{path.name}: gold_task_states[{idx}] must be an object")
            continue

        task_id = state.get("task_id")
        if not _is_non_empty_string(task_id):
            errors.append(f"{path.name}: gold_task_states[{idx}].task_id must be non-empty string")
        else:
            if task_id in gold_ids:
                errors.append(f"{path.name}: duplicate gold task_id '{task_id}'")
            gold_ids.add(task_id)

        assigned = state.get("assigned")
        completed = state.get("completed")
        assigned_unit = state.get("assigned_unit")
        completion_outcome = state.get("completion_outcome")
        assignment_message_id = state.get("assignment_message_id")
        completion_message_id = state.get("completion_message_id")

        if not isinstance(assigned, bool):
            errors.append(f"{path.name}: gold_task_states[{idx}].assigned must be boolean")
        if not isinstance(completed, bool):
            errors.append(f"{path.name}: gold_task_states[{idx}].completed must be boolean")
        if assigned_unit is not None and not _is_non_empty_string(assigned_unit):
            errors.append(f"{path.name}: gold_task_states[{idx}].assigned_unit must be string or null")
        if completion_outcome is not None and not _is_non_empty_string(completion_outcome):
            errors.append(f"{path.name}: gold_task_states[{idx}].completion_outcome must be string or null")
        if assignment_message_id is not None and not isinstance(assignment_message_id, int):
            errors.append(f"{path.name}: gold_task_states[{idx}].assignment_message_id must be int or null")
        if completion_message_id is not None and not isinstance(completion_message_id, int):
            errors.append(f"{path.name}: gold_task_states[{idx}].completion_message_id must be int or null")

        if isinstance(assigned, bool) and not assigned and assigned_unit is not None:
            errors.append(f"{path.name}: task {task_id!r} has assigned=false but assigned_unit is not null")
        if isinstance(completed, bool) and completed and isinstance(assigned, bool) and not assigned:
            errors.append(f"{path.name}: task {task_id!r} has completed=true but assigned=false")
        if isinstance(assigned, bool) and not assigned and assignment_message_id is not None:
            errors.append(f"{path.name}: task {task_id!r} has assigned=false but assignment_message_id is not null")
        if isinstance(completed, bool) and not completed and completion_message_id is not None:
            errors.append(f"{path.name}: task {task_id!r} has completed=false but completion_message_id is not null")
        if (
            isinstance(assignment_message_id, int)
            and isinstance(completion_message_id, int)
            and assignment_message_id > completion_message_id
        ):
            errors.append(
                f"{path.name}: task {task_id!r} has assignment_message_id > completion_message_id"
            )

    if task_ids != gold_ids:
        missing_gold = sorted(task_ids - gold_ids)
        extra_gold = sorted(gold_ids - task_ids)
        if missing_gold:
            errors.append(f"{path.name}: missing gold_task_states for task_ids {missing_gold}")
        if extra_gold:
            errors.append(f"{path.name}: gold_task_states references unknown task_ids {extra_gold}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate closed-world firefighter scenario dataset")
    parser.add_argument("--data-dir", type=Path, default=Path("data/scenarios"))
    args = parser.parse_args()

    files = sorted(args.data_dir.glob("*.json"))
    if not files:
        print(f"ERROR: no scenario JSON files found in {args.data_dir}")
        return 1

    all_errors: list[str] = []
    for path in files:
        all_errors.extend(validate_scenario(path))

    if all_errors:
        print("DATASET VALIDATION FAILED")
        for err in all_errors:
            print(f"- {err}")
        return 1

    print("DATASET VALIDATION PASSED")
    for path in files:
        print(f"- OK: {path.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
