from __future__ import annotations

from swisstext_eval.io.scenarios import Message, Scenario

STRUCTURE_CONDITIONS = ("structured_dialogue", "no_speaker", "continuous_transcript")


def _normalize_text(text: str) -> str:
    return " ".join(text.strip().split())


def render_messages(messages: list[Message], structure_condition: str) -> str:
    if structure_condition not in STRUCTURE_CONDITIONS:
        raise ValueError(f"Unknown transcript condition: {structure_condition}")

    if structure_condition == "structured_dialogue":
        lines = []
        for message in messages:
            speaker = message.speaker or "UNKNOWN"
            lines.append(f"{speaker}: {_normalize_text(message.text)}")
        return "\n".join(lines)

    if structure_condition == "no_speaker":
        return "\n".join(_normalize_text(message.text) for message in messages)

    # continuous_transcript
    return " ".join(_normalize_text(message.text) for message in messages)


def render_transcript(scenario: Scenario, structure_condition: str) -> str:
    return render_messages(scenario.messages, structure_condition)


def render_transcript_prefix(scenario: Scenario, structure_condition: str, prefix_index: int) -> str:
    if prefix_index < 1 or prefix_index > len(scenario.messages):
        raise ValueError(f"prefix_index must be in [1, {len(scenario.messages)}]")
    return render_messages(scenario.messages[:prefix_index], structure_condition)
