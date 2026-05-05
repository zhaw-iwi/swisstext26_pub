from swisstext_eval.eval.gold import TaskTransition
from swisstext_eval.eval.metrics import compute_full_metrics, compute_incremental_metrics
from swisstext_eval.io.scenarios import Message, PredefinedTask, Scenario, TaskStateLabel
from swisstext_eval.parsing.predictions import ParsedPrediction, PredictedTaskState


def _scenario() -> Scenario:
    return Scenario(
        scenario_id="Sx",
        scenario_name="toy",
        metadata={},
        messages=[
            Message(message_id=1, speaker="IC", text="assign"),
            Message(message_id=2, speaker="UnitA", text="done"),
        ],
        predefined_tasks=[
            PredefinedTask(task_id="T1", task_name="Task A"),
            PredefinedTask(task_id="T2", task_name="Task B"),
        ],
        gold_task_states=[
            TaskStateLabel(task_id="T1", assigned=True, assigned_unit="UnitA", completed=False, completion_outcome=None),
            TaskStateLabel(task_id="T2", assigned=True, assigned_unit="UnitB", completed=True, completion_outcome="Done"),
        ],
    )


def test_full_assignment_accuracy() -> None:
    scenario = _scenario()
    prediction = ParsedPrediction(
        task_states=[
            PredictedTaskState(task_id="T1", assigned=True, assigned_unit="UnitA", completed=False, completion_outcome=None),
            PredictedTaskState(task_id="T2", assigned=False, assigned_unit=None, completed=False, completion_outcome=None),
        ]
    )
    metrics = compute_full_metrics(
        run_id="r1",
        run_index=1,
        scenario=scenario,
        structure_condition="structured_dialogue",
        prediction=prediction,
    )
    assert metrics.assignment_accuracy == 0.5


def test_incremental_metrics_and_latency() -> None:
    scenario = _scenario()
    predictions = {
        1: ParsedPrediction(
            task_states=[
                PredictedTaskState(task_id="T1", assigned=True, assigned_unit="UnitA", completed=False, completion_outcome=None),
                PredictedTaskState(task_id="T2", assigned=False, assigned_unit=None, completed=False, completion_outcome=None),
            ]
        ),
        2: ParsedPrediction(
            task_states=[
                PredictedTaskState(task_id="T1", assigned=True, assigned_unit="UnitA", completed=False, completion_outcome=None),
                PredictedTaskState(task_id="T2", assigned=True, assigned_unit="UnitB", completed=True, completion_outcome="Done"),
            ]
        ),
    }
    gold = {
        1: [
            TaskStateLabel(task_id="T1", assigned=True, assigned_unit="UnitA", completed=False, completion_outcome=None),
            TaskStateLabel(task_id="T2", assigned=True, assigned_unit="UnitB", completed=False, completion_outcome=None),
        ],
        2: [
            TaskStateLabel(task_id="T1", assigned=True, assigned_unit="UnitA", completed=False, completion_outcome=None),
            TaskStateLabel(task_id="T2", assigned=True, assigned_unit="UnitB", completed=True, completion_outcome="Done"),
        ],
    }
    transitions = {
        "T1": TaskTransition(task_id="T1", assignment_prefix=1, completion_prefix=None),
        "T2": TaskTransition(task_id="T2", assignment_prefix=1, completion_prefix=2),
    }

    row, prefix_rows = compute_incremental_metrics(
        run_id="r1",
        run_index=1,
        scenario=scenario,
        structure_condition="structured_dialogue",
        predictions_by_prefix=predictions,
        gold_by_prefix=gold,
        transitions=transitions,
    )

    assert len(prefix_rows) == 2
    assert row.assignment_detection_latency == 0.5
    assert row.completion_detection_latency == 0.0
    assert row.assignment_detection_miss_rate == 0.0
    assert row.completion_detection_miss_rate == 0.0


def test_assignment_latency_waits_for_correct_unit() -> None:
    scenario = _scenario()
    predictions = {
        1: ParsedPrediction(
            task_states=[
                PredictedTaskState(task_id="T1", assigned=True, assigned_unit="WrongUnit", completed=False, completion_outcome=None),
                PredictedTaskState(task_id="T2", assigned=True, assigned_unit="UnitB", completed=False, completion_outcome=None),
            ]
        ),
        2: ParsedPrediction(
            task_states=[
                PredictedTaskState(task_id="T1", assigned=True, assigned_unit="UnitA", completed=False, completion_outcome=None),
                PredictedTaskState(task_id="T2", assigned=True, assigned_unit="UnitB", completed=True, completion_outcome="Done"),
            ]
        ),
    }
    gold = {
        1: [
            TaskStateLabel(task_id="T1", assigned=True, assigned_unit="UnitA", completed=False, completion_outcome=None),
            TaskStateLabel(task_id="T2", assigned=True, assigned_unit="UnitB", completed=False, completion_outcome=None),
        ],
        2: [
            TaskStateLabel(task_id="T1", assigned=True, assigned_unit="UnitA", completed=False, completion_outcome=None),
            TaskStateLabel(task_id="T2", assigned=True, assigned_unit="UnitB", completed=True, completion_outcome="Done"),
        ],
    }
    transitions = {
        "T1": TaskTransition(task_id="T1", assignment_prefix=1, completion_prefix=None),
        "T2": TaskTransition(task_id="T2", assignment_prefix=1, completion_prefix=2),
    }

    row, _prefix_rows = compute_incremental_metrics(
        run_id="r1",
        run_index=1,
        scenario=scenario,
        structure_condition="structured_dialogue",
        predictions_by_prefix=predictions,
        gold_by_prefix=gold,
        transitions=transitions,
    )

    assert row.assignment_detection_latency == 0.5
    assert row.assignment_detection_miss_rate == 0.0


def test_detection_miss_rates_count_missed_detections() -> None:
    scenario = _scenario()
    predictions = {
        1: ParsedPrediction(
            task_states=[
                PredictedTaskState(task_id="T1", assigned=False, assigned_unit=None, completed=False, completion_outcome=None),
                PredictedTaskState(task_id="T2", assigned=True, assigned_unit="UnitB", completed=False, completion_outcome=None),
            ]
        ),
        2: ParsedPrediction(
            task_states=[
                PredictedTaskState(task_id="T1", assigned=False, assigned_unit=None, completed=False, completion_outcome=None),
                PredictedTaskState(task_id="T2", assigned=True, assigned_unit="UnitB", completed=False, completion_outcome=None),
            ]
        ),
    }
    gold = {
        1: [
            TaskStateLabel(task_id="T1", assigned=True, assigned_unit="UnitA", completed=False, completion_outcome=None),
            TaskStateLabel(task_id="T2", assigned=True, assigned_unit="UnitB", completed=False, completion_outcome=None),
        ],
        2: [
            TaskStateLabel(task_id="T1", assigned=True, assigned_unit="UnitA", completed=False, completion_outcome=None),
            TaskStateLabel(task_id="T2", assigned=True, assigned_unit="UnitB", completed=True, completion_outcome="Done"),
        ],
    }
    transitions = {
        "T1": TaskTransition(task_id="T1", assignment_prefix=1, completion_prefix=None),
        "T2": TaskTransition(task_id="T2", assignment_prefix=1, completion_prefix=2),
    }

    row, _prefix_rows = compute_incremental_metrics(
        run_id="r1",
        run_index=1,
        scenario=scenario,
        structure_condition="structured_dialogue",
        predictions_by_prefix=predictions,
        gold_by_prefix=gold,
        transitions=transitions,
    )

    assert row.assignment_detection_latency == 0.0
    assert row.assignment_detection_miss_rate == 0.5
    assert row.completion_detection_latency == 0.0
    assert row.completion_detection_miss_rate == 1.0
