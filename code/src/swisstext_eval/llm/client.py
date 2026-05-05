from __future__ import annotations

import json
import os
import re
import time
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class LLMResponse:
    content: str
    model: str


class LLMClient:
    """Provider client with deterministic local mock mode."""

    def __init__(
        self,
        model_name: str,
        mode: str = "mock",
        api_key_env: str = "OPENAI_API_KEY",
        temperature: float = 0.0,
        max_tokens: int = 1200,
        timeout_seconds: int = 60,
        retry_count: int = 2,
    ) -> None:
        self.model_name = model_name
        self.mode = mode
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.retry_count = retry_count

        self._client = None
        if self.mode == "live":
            try:
                from openai import OpenAI
            except ImportError as exc:
                raise RuntimeError(
                    "openai package is required for live mode. Install dependencies from code/requirements.txt"
                ) from exc

            api_key = os.getenv(api_key_env)
            if not api_key:
                raise RuntimeError(f"Environment variable {api_key_env} is not set")
            self._client = OpenAI(api_key=api_key, timeout=timeout_seconds)

    def run(
        self,
        system_prompt: str,
        user_prompt: str,
        json_schema: dict[str, Any] | None = None,
    ) -> LLMResponse:
        if self.mode == "mock":
            return LLMResponse(content=self._mock_predict(user_prompt), model=self.model_name)
        if self.mode == "live":
            return self._live_predict(system_prompt, user_prompt, json_schema)
        raise ValueError(f"Unsupported provider mode: {self.mode}")

    def _live_predict(
        self,
        system_prompt: str,
        user_prompt: str,
        json_schema: dict[str, Any] | None = None,
    ) -> LLMResponse:
        assert self._client is not None

        last_error: Exception | None = None
        for attempt in range(self.retry_count + 1):
            try:
                payload: dict[str, Any] = {
                    "model": self.model_name,
                    "input": [
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt},
                    ],
                    "temperature": self.temperature,
                    "max_output_tokens": self.max_tokens,
                }
                if json_schema is not None:
                    payload["text"] = {
                        "format": {
                            "type": "json_schema",
                            "name": "swisstext_task_state_monitoring",
                            "schema": json_schema,
                            "strict": True,
                        }
                    }

                response = self._client.responses.create(**payload)
                output_text = getattr(response, "output_text", None)
                if isinstance(output_text, str) and output_text.strip():
                    return LLMResponse(content=output_text, model=self.model_name)

                dumped = response.model_dump()
                chunks: list[str] = []
                for item in dumped.get("output", []):
                    if item.get("type") != "message":
                        continue
                    for content_item in item.get("content", []):
                        if content_item.get("type") == "output_text":
                            text = content_item.get("text")
                            if isinstance(text, str) and text.strip():
                                chunks.append(text)
                if chunks:
                    return LLMResponse(content="\n".join(chunks), model=self.model_name)
                raise RuntimeError("OpenAI response did not contain output text")
            except Exception as exc:  # noqa: BLE001
                last_error = exc
                if attempt < self.retry_count:
                    time.sleep(1.5 * (attempt + 1))
                    continue
                break

        raise RuntimeError(f"OpenAI live request failed after retries: {last_error}")

    @staticmethod
    def _normalize_text(text: str) -> str:
        return " ".join(text.lower().split())

    def _extract_tasks(self, user_prompt: str) -> list[dict[str, str]]:
        marker = "Predefined task list (JSON):"
        start = user_prompt.find(marker)
        if start < 0:
            return []
        start = user_prompt.find("[", start)
        if start < 0:
            return []

        depth = 0
        in_string = False
        escaped = False
        end = -1
        for idx in range(start, len(user_prompt)):
            ch = user_prompt[idx]
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
            elif ch == "[":
                depth += 1
            elif ch == "]":
                depth -= 1
                if depth == 0:
                    end = idx + 1
                    break

        if end < 0:
            return []

        try:
            payload = json.loads(user_prompt[start:end])
            if isinstance(payload, list):
                return [item for item in payload if isinstance(item, dict)]
        except json.JSONDecodeError:
            return []
        return []

    def _extract_transcript(self, user_prompt: str) -> str:
        match = re.search(r"Transcript:\s*(.*?)\s*Output schema:", user_prompt, flags=re.DOTALL)
        if not match:
            return ""
        return match.group(1).strip()

    def _mock_predict(self, user_prompt: str) -> str:
        tasks = self._extract_tasks(user_prompt)
        transcript = self._normalize_text(self._extract_transcript(user_prompt))

        completion_markers = (
            "abgeschlossen",
            "steht",
            "brand aus",
            "rauchfrei",
            "raucharm",
            "keine glutnester",
            "kalt",
            "erledigt",
        )

        units = [
            "einsatzleitung",
            "angriffstrupp",
            "wassertrupp",
            "atemschutztrupp",
            "lueftungstrupp",
            "rettungstrupp",
            "sicherungstrupp",
        ]

        task_states: list[dict[str, object]] = []
        for task in tasks:
            task_id = str(task.get("task_id", "")).strip()
            task_name = str(task.get("task_name", "")).strip()
            task_name_norm = self._normalize_text(task_name)

            assigned = bool(task_name_norm) and task_name_norm in transcript
            assigned_unit: str | None = None
            if assigned:
                for unit in units:
                    if unit in transcript:
                        assigned_unit = unit
                        break

            completed = assigned and any(marker in transcript for marker in completion_markers)
            completion_outcome = "completion reported" if completed else None

            task_states.append(
                {
                    "task_id": task_id,
                    "assigned": assigned,
                    "assigned_unit": assigned_unit,
                    "completed": completed,
                    "completion_outcome": completion_outcome,
                }
            )

        return json.dumps({"task_states": task_states})
