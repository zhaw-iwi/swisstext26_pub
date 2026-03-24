from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any


@dataclass
class PathsConfig:
    repo_root: Path
    input_data_dir: Path
    output_root: Path
    cache_dir: Path


@dataclass
class ProviderConfig:
    model_name: str = "gpt-5.2"
    api_key_env: str = "OPENAI_API_KEY"
    temperature: float = 0.0
    max_tokens: int = 1200
    timeout_seconds: int = 60
    retry_count: int = 2
    mode: str = "mock"


@dataclass
class ExperimentConfig:
    run_count: int = 12
    selected_scenarios: list[str] = field(default_factory=list)
    selected_structure_conditions: list[str] = field(
        default_factory=lambda: ["structured_dialogue", "no_speaker", "continuous_transcript"]
    )
    selected_processing_modes: list[str] = field(default_factory=lambda: ["full_transcript", "incremental"])
    incremental_prefix_policy: str = "every_message"
    api_batch_size: int = 8
    resume_behavior: str = "skip_completed"
    output_run_tag: str = field(default_factory=lambda: datetime.now().strftime("%Y%m%d_%H%M%S"))
    prompt_version_tag: str = "v3_known_task_monitoring"


@dataclass
class PromptConfig:
    system_prompt_path: Path
    user_prompt_template_path: Path


@dataclass
class EvalConfig:
    export_tables: bool = True
    export_figures: bool = True
    export_prefix_level_metrics: bool = True
    export_detailed_condition_rows: bool = True


@dataclass
class DebugConfig:
    verbose: bool = True
    limit_scenarios: int | None = None
    limit_work_items: int | None = None
    save_transformed_inputs: bool = True


@dataclass
class NotebookConfig:
    paths: PathsConfig
    provider: ProviderConfig
    experiment: ExperimentConfig
    prompts: PromptConfig
    evaluation: EvalConfig
    debug: DebugConfig

    def to_dict(self) -> dict[str, Any]:
        raw = asdict(self)
        raw["paths"]["repo_root"] = str(self.paths.repo_root)
        raw["paths"]["input_data_dir"] = str(self.paths.input_data_dir)
        raw["paths"]["output_root"] = str(self.paths.output_root)
        raw["paths"]["cache_dir"] = str(self.paths.cache_dir)
        raw["prompts"]["system_prompt_path"] = str(self.prompts.system_prompt_path)
        raw["prompts"]["user_prompt_template_path"] = str(self.prompts.user_prompt_template_path)
        return raw


def run_id_for_index(config: NotebookConfig, run_index: int) -> str:
    return f"{config.experiment.output_run_tag}__r{run_index:02d}"


def batch_id(config: NotebookConfig) -> str:
    return f"{config.experiment.output_run_tag}__batch"


def run_dir(config: NotebookConfig, run_index: int) -> Path:
    return config.paths.output_root / run_id_for_index(config, run_index)


def ensure_run_directories(config: NotebookConfig, run_index: int) -> dict[str, Path]:
    root = run_dir(config, run_index)
    directories = {
        "root": root,
        "config": root / "config",
        "logs": root / "logs",
        "inputs_transformed": root / "inputs_transformed",
        "requests": root / "requests",
        "raw_responses": root / "raw_responses",
        "parsed_predictions": root / "parsed_predictions",
        "metrics": root / "metrics",
        "tables": root / "tables",
        "figures": root / "figures",
        "inspection": root / "inspection",
    }
    for path in directories.values():
        path.mkdir(parents=True, exist_ok=True)
    return directories


def ensure_batch_directories(config: NotebookConfig) -> dict[str, Path]:
    root = config.paths.output_root / batch_id(config)
    tables = root / "tables"
    figures = root / "figures"
    tables.mkdir(parents=True, exist_ok=True)
    figures.mkdir(parents=True, exist_ok=True)
    return {"root": root, "tables": tables, "figures": figures}
