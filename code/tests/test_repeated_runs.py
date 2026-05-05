from pathlib import Path

import pandas as pd

from conftest import SCENARIO_DATA_DIR
from swisstext_eval.config import DebugConfig, EvalConfig, ExperimentConfig, NotebookConfig, PathsConfig, PromptConfig, ProviderConfig
from swisstext_eval.eval.repeated import run_repeated_evaluation
from swisstext_eval.io.scenarios import load_scenarios


def test_repeated_run_aggregation(tmp_path: Path) -> None:
    repo = Path(".").resolve()
    scenario_id = load_scenarios(SCENARIO_DATA_DIR)[0].scenario_id
    cfg = NotebookConfig(
        paths=PathsConfig(
            repo_root=repo,
            input_data_dir=SCENARIO_DATA_DIR,
            output_root=tmp_path,
            cache_dir=tmp_path / ".cache",
        ),
        provider=ProviderConfig(mode="mock"),
        experiment=ExperimentConfig(
            run_count=2,
            selected_scenarios=[scenario_id],
            selected_structure_conditions=["structured_dialogue"],
            selected_processing_modes=["full_transcript"],
            output_run_tag="testrun",
        ),
        prompts=PromptConfig(
            system_prompt_path=repo / "code" / "prompts" / "system_prompt.txt",
            user_prompt_template_path=repo / "code" / "prompts" / "user_prompt_template.txt",
        ),
        evaluation=EvalConfig(export_figures=False),
        debug=DebugConfig(verbose=False),
    )

    result = run_repeated_evaluation(cfg)
    assert Path(result["full_transcript_summary_csv"]).exists()
    summary = pd.read_csv(result["full_transcript_summary_csv"])
    assert "assignment_accuracy_mean" in summary.columns
    assert summary.iloc[0]["n_runs"] == 2
