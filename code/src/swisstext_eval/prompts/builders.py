from __future__ import annotations

import json
from pathlib import Path

from swisstext_eval.io.scenarios import PredefinedTask


def load_prompt(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(f"Prompt file not found: {path}")
    return path.read_text(encoding="utf-8")


def build_prompt_payload(
    system_prompt: str,
    user_template: str,
    scenario_id: str,
    structure_condition: str,
    processing_mode: str,
    prefix_index: int,
    transcript: str,
    predefined_tasks: list[PredefinedTask],
    output_schema: str,
) -> dict[str, str]:
    task_list = [{"task_id": task.task_id, "task_name": task.task_name} for task in predefined_tasks]
    prefix_label = "full" if prefix_index == -1 else str(prefix_index)
    user_prompt = user_template.format(
        scenario_id=scenario_id,
        structure_condition=structure_condition,
        processing_mode=processing_mode,
        prefix_index=prefix_label,
        transcript=transcript,
        predefined_task_list=json.dumps(task_list, ensure_ascii=True, indent=2),
        output_schema=output_schema,
    )
    return {"system": system_prompt, "user": user_prompt}
