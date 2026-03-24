from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from swisstext_eval.eval.work import WorkItem, WorkKey, request_artifact_path
from swisstext_eval.utils.io import read_json, write_json


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def load_request_artifact(requests_root: Path, key: WorkKey) -> dict[str, Any] | None:
    path = request_artifact_path(requests_root, key)
    if not path.exists():
        return None
    return read_json(path)


def is_completed_artifact(artifact: dict[str, Any] | None) -> bool:
    if not artifact:
        return False
    if artifact.get("status") != "completed":
        return False
    parsed = artifact.get("parsed_output")
    return isinstance(parsed, dict) and "task_states" in parsed


def init_request_artifact(item: WorkItem, prompt_payload: dict[str, str], model_settings: dict[str, Any]) -> dict[str, Any]:
    key = WorkKey.from_item(item)
    return {
        "work_key": key.as_dict(),
        "run_id": item.run_id,
        "scenario_id": item.scenario_id,
        "structure_condition": item.structure_condition,
        "processing_mode": item.processing_mode,
        "prefix_index": item.prefix_index,
        "prompt_payload": prompt_payload,
        "model_settings": model_settings,
        "request_timestamp": utc_now_iso(),
        "response_timestamp": None,
        "response_raw_text": None,
        "parsed_output": None,
        "error": None,
        "status": "requested",
    }


def save_request_artifact(requests_root: Path, key: WorkKey, payload: dict[str, Any]) -> Path:
    path = request_artifact_path(requests_root, key)
    write_json(path, payload)
    return path
