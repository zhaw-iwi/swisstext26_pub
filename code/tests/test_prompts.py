from swisstext_eval.io.scenarios import PredefinedTask
from swisstext_eval.prompts.builders import build_prompt_payload


def test_prompt_builder_includes_processing_metadata() -> None:
    payload = build_prompt_payload(
        system_prompt="sys",
        user_template=(
            "Structure condition: {structure_condition}\\n"
            "Processing mode: {processing_mode}\\n"
            "Prefix index: {prefix_index}\\n"
            "Tasks: {predefined_task_list}\\n"
            "Transcript: {transcript}\\n"
            "Schema: {output_schema}"
        ),
        scenario_id="S1",
        structure_condition="structured_dialogue",
        processing_mode="incremental",
        prefix_index=2,
        transcript="abc",
        predefined_tasks=[PredefinedTask(task_id="T1", task_name="Task A")],
        output_schema="{}",
    )

    assert payload["system"] == "sys"
    assert "Prefix index: 2" in payload["user"]
    assert '"task_id": "T1"' in payload["user"]
