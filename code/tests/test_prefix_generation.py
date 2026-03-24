from conftest import SCENARIO_DATA_DIR
from swisstext_eval.eval.prefixes import prefix_indices_for_scenario
from swisstext_eval.io.scenarios import load_scenarios


def test_prefix_generation_every_message() -> None:
    for scenario in load_scenarios(SCENARIO_DATA_DIR):
        indices = prefix_indices_for_scenario(scenario, "every_message")
        assert indices == list(range(1, len(scenario.messages) + 1))
