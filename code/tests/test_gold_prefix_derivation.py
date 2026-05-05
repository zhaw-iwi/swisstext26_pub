import pytest

from conftest import SCENARIO_DATA_DIR
from swisstext_eval.eval.gold import derive_prefix_gold_states, derive_task_transitions
from swisstext_eval.io.scenarios import Scenario, Message, PredefinedTask, TaskStateLabel, load_scenarios


EXPECTED_TRANSITIONS = {
    "S1": {"T1": (7, 11), "T2": (5, 12), "T3": (9, None)},
    "S2": {"T1": (3, 7), "T2": (9, 18), "T3": (12, None)},
    "S3": {"T1": (2, 6), "T2": (4, 9), "T3": (7, 15)},
    "S4": {"T1": (3, 12), "T2": (10, 21), "T3": (8, None)},
    "S5": {"T1": (4, 11), "T2": (9, 17), "T3": (15, 20)},
}


def test_gold_transition_and_prefix_derivation() -> None:
    scenarios = load_scenarios(SCENARIO_DATA_DIR)
    for scenario in scenarios:
        transitions = derive_task_transitions(scenario)
        task_ids = {task.task_id for task in scenario.predefined_tasks}
        assert set(transitions) == task_ids
        assert {task_id: (item.assignment_prefix, item.completion_prefix) for task_id, item in transitions.items()} == (
            EXPECTED_TRANSITIONS[scenario.scenario_id]
        )

        final_states = {state.task_id: state for state in derive_prefix_gold_states(scenario, len(scenario.messages))}
        gold_final = {state.task_id: state for state in scenario.gold_task_states}
        for task_id, final_state in final_states.items():
            gold = gold_final[task_id]
            assert final_state.assigned is gold.assigned
            assert final_state.assigned_unit == (gold.assigned_unit if gold.assigned else None)
            assert final_state.completed is gold.completed
            assert final_state.completion_outcome == (gold.completion_outcome if gold.completed else None)

        for task_id, transition in transitions.items():
            gold = gold_final[task_id]

            if transition.assignment_prefix is None:
                assert not gold.assigned
            else:
                assert 1 <= transition.assignment_prefix <= len(scenario.messages)
                if transition.assignment_prefix > 1:
                    previous = {state.task_id: state for state in derive_prefix_gold_states(scenario, transition.assignment_prefix - 1)}
                    assert previous[task_id].assigned is False
                current = {state.task_id: state for state in derive_prefix_gold_states(scenario, transition.assignment_prefix)}
                assert current[task_id].assigned is gold.assigned
                if gold.assigned:
                    assert current[task_id].assigned_unit == gold.assigned_unit

            if transition.completion_prefix is None:
                assert not gold.completed
            else:
                assert 1 <= transition.completion_prefix <= len(scenario.messages)
                assert transition.assignment_prefix is not None
                assert transition.assignment_prefix <= transition.completion_prefix
                if transition.completion_prefix > 1:
                    previous = {state.task_id: state for state in derive_prefix_gold_states(scenario, transition.completion_prefix - 1)}
                    assert previous[task_id].completed is False
                current = {state.task_id: state for state in derive_prefix_gold_states(scenario, transition.completion_prefix)}
                assert current[task_id].completed is gold.completed
                if gold.completed:
                    assert current[task_id].completion_outcome == gold.completion_outcome


def test_assignment_derivation_requires_explicit_metadata_for_ambiguous_same_unit_commands() -> None:
    scenario = Scenario(
        scenario_id="SX",
        scenario_name="ambiguous",
        metadata={},
        messages=[
            Message(message_id=1, speaker="Einsatzleitung", text="An Wassertrupp von Einsatzleitung, Befehl: Aufbau X, antworten"),
            Message(message_id=2, speaker="Einsatzleitung", text="An Wassertrupp von Einsatzleitung, Befehl: Aufgabe Y, antworten"),
        ],
        predefined_tasks=[PredefinedTask(task_id="T1", task_name="Aufgabe Y")],
        gold_task_states=[
            TaskStateLabel(
                task_id="T1",
                assigned=True,
                assigned_unit="Wassertrupp",
                completed=False,
                completion_outcome=None,
            )
        ],
    )

    with pytest.raises(ValueError, match="add assignment_message_id"):
        derive_task_transitions(scenario)
