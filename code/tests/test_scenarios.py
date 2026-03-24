import pytest

from conftest import SCENARIO_DATA_DIR
from swisstext_eval.io.scenarios import load_scenarios, parse_scenario


def test_load_scenario_dataset() -> None:
    scenarios = load_scenarios(SCENARIO_DATA_DIR)
    assert scenarios
    scenario_ids = [scenario.scenario_id for scenario in scenarios]
    assert len(set(scenario_ids)) == len(scenario_ids)

    scenario = load_scenarios(SCENARIO_DATA_DIR, [scenario_ids[0]])[0]
    assert scenario.scenario_id == scenario_ids[0]
    assert scenario.messages
    assert scenario.predefined_tasks
    assert scenario.gold_task_states


def test_parse_requires_new_fields() -> None:
    raw = {
        "scenario_id": "X",
        "scenario_name": "Missing fields",
        "messages": [{"id": 1, "speaker": "IC", "text": "x"}],
    }
    with pytest.raises(ValueError):
        parse_scenario(raw)


def test_parse_rejects_non_sequential_ids() -> None:
    raw = {
        "scenario_id": "X",
        "scenario_name": "Bad ids",
        "messages": [
            {"id": 1, "speaker": "IC", "text": "x"},
            {"id": 3, "speaker": "IC", "text": "y"},
        ],
        "predefined_tasks": [{"task_id": "T1", "task_name": "Task A"}],
        "gold_task_states": [
            {"task_id": "T1", "assigned": False, "assigned_unit": None, "completed": False, "completion_outcome": None}
        ],
    }
    with pytest.raises(ValueError):
        parse_scenario(raw)


def test_parse_accepts_explicit_transition_annotations() -> None:
    raw = {
        "scenario_id": "X",
        "scenario_name": "Annotated transitions",
        "messages": [
            {"id": 1, "speaker": "IC", "text": "An UnitA von Einsatzleitung, Befehl: Task A, antworten"},
            {"id": 2, "speaker": "UnitA", "text": "An Einsatzleitung von UnitA, Meldung: Task A erledigt, Schluss"},
        ],
        "predefined_tasks": [{"task_id": "T1", "task_name": "Task A"}],
        "gold_task_states": [
            {
                "task_id": "T1",
                "assigned": True,
                "assigned_unit": "UnitA",
                "completed": True,
                "completion_outcome": "An Einsatzleitung von UnitA, Meldung: Task A erledigt, Schluss",
                "assignment_message_id": 1,
                "completion_message_id": 2,
            }
        ],
    }
    scenario = parse_scenario(raw)
    gold = scenario.gold_task_states[0]
    assert gold.assignment_message_id == 1
    assert gold.completion_message_id == 2
