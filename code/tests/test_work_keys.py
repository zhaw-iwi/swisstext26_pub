from pathlib import Path

from swisstext_eval.eval.work import WorkItem, WorkKey, request_artifact_path


def test_work_key_and_path() -> None:
    item = WorkItem(
        run_index=1,
        run_id="tag__r01",
        scenario_id="S1",
        structure_condition="structured_dialogue",
        processing_mode="incremental",
        prefix_index=3,
    )
    key = WorkKey.from_item(item)
    path = request_artifact_path(Path("requests"), key)
    assert key.as_dict()["prefix_index"] == 3
    assert str(path).endswith("S1\\structured_dialogue\\incremental\\prefix_003.json")
