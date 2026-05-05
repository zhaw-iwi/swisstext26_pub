from __future__ import annotations

from pathlib import Path

import pandas as pd

from swisstext_eval.eval.metrics import FullMetricsRow, IncrementalMetricsRow, IncrementalPrefixRow


def _ci95(series: pd.Series) -> float:
    n = int(series.count())
    if n <= 1:
        return 0.0
    return float(1.96 * series.std(ddof=1) / (n**0.5))


def _mean_std_ci(df: pd.DataFrame, group_cols: list[str], metric_cols: list[str]) -> pd.DataFrame:
    grouped = df.groupby(group_cols, as_index=False)
    rows: list[dict[str, object]] = []
    for keys, subset in grouped:
        if not isinstance(keys, tuple):
            keys = (keys,)
        row: dict[str, object] = {col: value for col, value in zip(group_cols, keys)}
        row["n_runs"] = int(subset["run_id"].nunique()) if "run_id" in subset.columns else len(subset)
        for metric in metric_cols:
            row[f"{metric}_mean"] = float(subset[metric].mean())
            row[f"{metric}_std"] = float(subset[metric].std(ddof=1)) if len(subset) > 1 else 0.0
            row[f"{metric}_ci95"] = _ci95(subset[metric])
        rows.append(row)
    return pd.DataFrame(rows)


def export_run_tables(
    *,
    output_dir: Path,
    full_rows: list[FullMetricsRow],
    incremental_rows: list[IncrementalMetricsRow],
    prefix_rows: list[IncrementalPrefixRow],
    export_prefix_level: bool,
) -> dict[str, Path]:
    output_dir.mkdir(parents=True, exist_ok=True)

    outputs: dict[str, Path] = {}
    full_df = pd.DataFrame([row.to_row() for row in full_rows])
    inc_df = pd.DataFrame([row.to_row() for row in incremental_rows])

    if not full_df.empty:
        full_per_scenario = output_dir / "full_transcript_per_scenario.csv"
        full_df.to_csv(full_per_scenario, index=False)
        outputs["full_transcript_per_scenario_csv"] = full_per_scenario

        full_summary = (
            full_df.groupby("structure_condition", as_index=False)[
                [
                    "assignment_accuracy",
                    "unit_assignment_accuracy",
                    "completion_accuracy",
                    "final_state_accuracy",
                    "completion_outcome_accuracy",
                ]
            ]
            .mean()
            .sort_values("structure_condition")
            .reset_index(drop=True)
        )
        full_summary_path = output_dir / "full_transcript_summary.csv"
        full_summary.to_csv(full_summary_path, index=False)
        outputs["full_transcript_summary_csv"] = full_summary_path

    prefix_df = pd.DataFrame([row.to_row() for row in prefix_rows]) if prefix_rows else pd.DataFrame()

    if not inc_df.empty:
        inc_per_scenario = output_dir / "incremental_per_scenario.csv"
        inc_df.to_csv(inc_per_scenario, index=False)
        outputs["incremental_per_scenario_csv"] = inc_per_scenario

        inc_summary = (
            inc_df.groupby("structure_condition", as_index=False)[
                [
                    "assignment_accuracy",
                    "unit_assignment_accuracy",
                    "completion_accuracy",
                    "current_state_accuracy",
                    "assignment_detection_latency",
                    "completion_detection_latency",
                    "assignment_detection_miss_rate",
                    "completion_detection_miss_rate",
                ]
            ]
            .mean()
            .sort_values("structure_condition")
            .reset_index(drop=True)
        )
        inc_summary_path = output_dir / "incremental_summary.csv"
        inc_summary.to_csv(inc_summary_path, index=False)
        outputs["incremental_summary_csv"] = inc_summary_path

    all_rows_frames = []
    if not full_df.empty:
        all_rows_frames.append(full_df)
    if not inc_df.empty:
        all_rows_frames.append(inc_df)
    all_rows_df = pd.concat(all_rows_frames, ignore_index=True) if all_rows_frames else pd.DataFrame()

    if not all_rows_df.empty:
        all_rows_path = output_dir / "all_condition_rows.csv"
        all_rows_df.to_csv(all_rows_path, index=False)
        outputs["all_condition_rows_csv"] = all_rows_path

        metric_cols = [
            col
            for col in all_rows_df.columns
            if col not in {"run_id", "run_index", "scenario_id", "structure_condition", "processing_mode"}
        ]
        long_df = all_rows_df.melt(
            id_vars=["run_id", "run_index", "scenario_id", "structure_condition", "processing_mode"],
            value_vars=metric_cols,
            var_name="metric_name",
            value_name="metric_value",
        )
        combined = (
            long_df.groupby(["structure_condition", "processing_mode", "metric_name"], as_index=False)["metric_value"]
            .agg(mean="mean", std="std", n="count")
            .reset_index(drop=True)
        )
        combined["std"] = combined["std"].fillna(0.0)
        combined["ci95"] = combined.apply(
            lambda r: 0.0 if r["n"] <= 1 else float(1.96 * r["std"] / (r["n"] ** 0.5)),
            axis=1,
        )
        combined = combined[["structure_condition", "processing_mode", "metric_name", "mean", "std", "ci95"]]
        combined_path = output_dir / "combined_condition_summary.csv"
        combined.to_csv(combined_path, index=False)
        outputs["combined_condition_summary_csv"] = combined_path

    if export_prefix_level and not prefix_df.empty:
        prefix_path = output_dir / "prefix_level_metrics.csv"
        prefix_df.to_csv(prefix_path, index=False)
        outputs["prefix_level_metrics_csv"] = prefix_path

    if not full_df.empty and not prefix_df.empty:
        last_prefix_df = (
            prefix_df.sort_values("prefix_index")
            .groupby(["run_id", "run_index", "scenario_id", "structure_condition"], as_index=False)
            .tail(1)
            .reset_index(drop=True)
        )
        terminal_gap_df = last_prefix_df.merge(
            full_df,
            on=["run_id", "run_index", "scenario_id", "structure_condition"],
            suffixes=("_incremental", "_full"),
        )
        terminal_gap_df = pd.DataFrame(
            {
                "run_id": terminal_gap_df["run_id"],
                "run_index": terminal_gap_df["run_index"],
                "scenario_id": terminal_gap_df["scenario_id"],
                "structure_condition": terminal_gap_df["structure_condition"],
                "assignment_terminal_gap": (
                    terminal_gap_df["assignment_accuracy_incremental"] - terminal_gap_df["assignment_accuracy_full"]
                ).abs(),
                "unit_assignment_terminal_gap": (
                    terminal_gap_df["unit_assignment_accuracy_incremental"]
                    - terminal_gap_df["unit_assignment_accuracy_full"]
                ).abs(),
                "completion_terminal_gap": (
                    terminal_gap_df["completion_accuracy_incremental"] - terminal_gap_df["completion_accuracy_full"]
                ).abs(),
                "state_terminal_gap": (
                    terminal_gap_df["current_state_accuracy"] - terminal_gap_df["final_state_accuracy"]
                ).abs(),
            }
        )
        terminal_gap_path = output_dir / "terminal_convergence_per_scenario.csv"
        terminal_gap_df.to_csv(terminal_gap_path, index=False)
        outputs["terminal_convergence_per_scenario_csv"] = terminal_gap_path

    return outputs


def export_batch_tables(
    *,
    output_dir: Path,
    all_condition_rows: pd.DataFrame,
    terminal_convergence_rows: pd.DataFrame | None = None,
) -> dict[str, Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    outputs: dict[str, Path] = {}

    all_rows_path = output_dir / "all_condition_rows.csv"
    all_condition_rows.to_csv(all_rows_path, index=False)
    outputs["all_condition_rows_csv"] = all_rows_path

    full = all_condition_rows[all_condition_rows["processing_mode"] == "full_transcript"].copy()
    if not full.empty:
        full_metrics = [
            "assignment_accuracy",
            "unit_assignment_accuracy",
            "completion_accuracy",
            "final_state_accuracy",
            "completion_outcome_accuracy",
        ]
        full_summary = _mean_std_ci(full, ["structure_condition"], full_metrics).sort_values("structure_condition")
        full_path = output_dir / "full_transcript_summary.csv"
        full_summary.to_csv(full_path, index=False)
        outputs["full_transcript_summary_csv"] = full_path

    inc = all_condition_rows[all_condition_rows["processing_mode"] == "incremental"].copy()
    if not inc.empty:
        inc_metrics = [
            "assignment_accuracy",
            "unit_assignment_accuracy",
            "completion_accuracy",
            "current_state_accuracy",
            "assignment_detection_latency",
            "completion_detection_latency",
            "assignment_detection_miss_rate",
            "completion_detection_miss_rate",
        ]
        inc_summary = _mean_std_ci(inc, ["structure_condition"], inc_metrics).sort_values("structure_condition")
        inc_path = output_dir / "incremental_summary.csv"
        inc_summary.to_csv(inc_path, index=False)
        outputs["incremental_summary_csv"] = inc_path

    metric_cols = [
        col
        for col in all_condition_rows.columns
        if col not in {"run_id", "run_index", "scenario_id", "structure_condition", "processing_mode"}
    ]
    long_df = all_condition_rows.melt(
        id_vars=["run_id", "run_index", "scenario_id", "structure_condition", "processing_mode"],
        value_vars=metric_cols,
        var_name="metric_name",
        value_name="metric_value",
    )
    grouped = (
        long_df.groupby(["structure_condition", "processing_mode", "metric_name"], as_index=False)["metric_value"]
        .agg(mean="mean", std="std", n="count")
        .reset_index(drop=True)
    )
    grouped["std"] = grouped["std"].fillna(0.0)
    grouped["ci95"] = grouped.apply(
        lambda r: 0.0 if r["n"] <= 1 else float(1.96 * r["std"] / (r["n"] ** 0.5)),
        axis=1,
    )
    combined = grouped[["structure_condition", "processing_mode", "metric_name", "mean", "std", "ci95"]]
    combined_path = output_dir / "combined_condition_summary.csv"
    combined.to_csv(combined_path, index=False)
    outputs["combined_condition_summary_csv"] = combined_path

    per_scenario = (
        all_condition_rows.groupby(["scenario_id", "structure_condition", "processing_mode"], as_index=False)
        .mean(numeric_only=True)
        .sort_values(["scenario_id", "structure_condition", "processing_mode"])
    )
    per_scenario_path = output_dir / "per_scenario_summary.csv"
    per_scenario.to_csv(per_scenario_path, index=False)
    outputs["per_scenario_summary_csv"] = per_scenario_path

    overall = all_condition_rows.mean(numeric_only=True).to_dict()
    overall_row = pd.DataFrame([overall])
    overall_path = output_dir / "overall_summary.csv"
    overall_row.to_csv(overall_path, index=False)
    outputs["overall_summary_csv"] = overall_path

    if terminal_convergence_rows is not None and not terminal_convergence_rows.empty:
        terminal_rows_path = output_dir / "terminal_convergence_per_scenario.csv"
        terminal_convergence_rows.to_csv(terminal_rows_path, index=False)
        outputs["terminal_convergence_per_scenario_csv"] = terminal_rows_path

        terminal_metrics = [
            "assignment_terminal_gap",
            "unit_assignment_terminal_gap",
            "completion_terminal_gap",
            "state_terminal_gap",
        ]
        terminal_summary = _mean_std_ci(
            terminal_convergence_rows,
            ["structure_condition"],
            terminal_metrics,
        ).sort_values("structure_condition")
        terminal_summary_path = output_dir / "terminal_convergence_summary.csv"
        terminal_summary.to_csv(terminal_summary_path, index=False)
        outputs["terminal_convergence_summary_csv"] = terminal_summary_path

    return outputs
