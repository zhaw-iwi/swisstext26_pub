from conftest import SCENARIO_DATA_DIR
from swisstext_eval.io.scenarios import load_scenarios
from swisstext_eval.transforms.transcript_conditions import render_transcript, render_transcript_prefix


def test_render_transcript_conditions() -> None:
    scenario = load_scenarios(SCENARIO_DATA_DIR)[0]

    structured = render_transcript(scenario, "structured_dialogue")
    no_speaker = render_transcript(scenario, "no_speaker")
    continuous = render_transcript(scenario, "continuous_transcript")

    assert structured.count("\n") == len(scenario.messages) - 1
    assert no_speaker.count("\n") == len(scenario.messages) - 1
    assert all(
        line.startswith(f"{message.speaker or 'UNKNOWN'}: ")
        for line, message in zip(structured.splitlines(), scenario.messages, strict=True)
    )
    assert "\n" not in continuous
    assert continuous


def test_render_transcript_prefix() -> None:
    scenario = load_scenarios(SCENARIO_DATA_DIR)[0]
    prefix_index = min(2, len(scenario.messages))
    prefix = render_transcript_prefix(scenario, "structured_dialogue", prefix_index)
    assert prefix.count("\n") == prefix_index - 1
