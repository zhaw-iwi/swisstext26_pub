from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


FULL_PREFIX_INDEX = -1


@dataclass(frozen=True)
class WorkItem:
    run_index: int
    run_id: str
    scenario_id: str
    structure_condition: str
    processing_mode: str
    prefix_index: int

    @property
    def prefix_label(self) -> str:
        return "full" if self.prefix_index == FULL_PREFIX_INDEX else f"{self.prefix_index:03d}"


@dataclass(frozen=True)
class WorkKey:
    run_id: str
    scenario_id: str
    structure_condition: str
    processing_mode: str
    prefix_index: int

    @classmethod
    def from_item(cls, item: WorkItem) -> "WorkKey":
        return cls(
            run_id=item.run_id,
            scenario_id=item.scenario_id,
            structure_condition=item.structure_condition,
            processing_mode=item.processing_mode,
            prefix_index=item.prefix_index,
        )

    def as_dict(self) -> dict[str, str | int]:
        return {
            "run_id": self.run_id,
            "scenario_id": self.scenario_id,
            "structure_condition": self.structure_condition,
            "processing_mode": self.processing_mode,
            "prefix_index": self.prefix_index,
        }


def request_artifact_path(requests_root: Path, key: WorkKey) -> Path:
    prefix = "full" if key.prefix_index == FULL_PREFIX_INDEX else f"prefix_{key.prefix_index:03d}"
    return (
        requests_root
        / key.scenario_id
        / key.structure_condition
        / key.processing_mode
        / f"{prefix}.json"
    )
