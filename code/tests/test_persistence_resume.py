from pathlib import Path

from swisstext_eval.eval.work import WorkKey
from swisstext_eval.io.artifacts import init_request_artifact, is_completed_artifact, load_request_artifact, save_request_artifact


class DummyItem:
    run_id = "tag__r01"
    scenario_id = "S1"
    structure_condition = "structured_dialogue"
    processing_mode = "full_transcript"
    prefix_index = -1


def test_persistence_resume_logic(tmp_path: Path) -> None:
    item = DummyItem()
    key = WorkKey(
        run_id=item.run_id,
        scenario_id=item.scenario_id,
        structure_condition=item.structure_condition,
        processing_mode=item.processing_mode,
        prefix_index=item.prefix_index,
    )

    artifact = init_request_artifact(item, {"system": "s", "user": "u"}, {"model_name": "m"})
    assert is_completed_artifact(artifact) is False

    artifact["status"] = "completed"
    artifact["parsed_output"] = {"task_states": []}
    save_request_artifact(tmp_path, key, artifact)

    loaded = load_request_artifact(tmp_path, key)
    assert loaded is not None
    assert is_completed_artifact(loaded) is True
