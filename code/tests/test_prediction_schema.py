from swisstext_eval.parsing.predictions import parse_prediction


def test_parse_task_state_prediction() -> None:
    raw = '''
    {
      "task_states": [
        {
          "task_id": "T1",
          "assigned": true,
          "assigned_unit": "Wassertrupp",
          "completed": false,
          "completion_outcome": null
        }
      ]
    }
    '''
    parsed = parse_prediction(raw)
    assert len(parsed.task_states) == 1
    assert parsed.task_states[0].task_id == "T1"
    assert parsed.task_states[0].assigned is True


def test_parse_embedded_json() -> None:
    raw = '''Result:\n```json\n{"task_states":[{"task_id":"T1","assigned":false,"assigned_unit":null,"completed":false,"completion_outcome":null}]}\n```'''
    parsed = parse_prediction(raw)
    assert parsed.task_states[0].task_id == "T1"
    assert parsed.task_states[0].assigned is False
