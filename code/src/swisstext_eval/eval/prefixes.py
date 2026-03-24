from __future__ import annotations

from swisstext_eval.io.scenarios import Scenario


def prefix_indices_for_scenario(scenario: Scenario, policy: str) -> list[int]:
    if policy != "every_message":
        raise ValueError(f"Unsupported incremental prefix policy: {policy}")
    return list(range(1, len(scenario.messages) + 1))
