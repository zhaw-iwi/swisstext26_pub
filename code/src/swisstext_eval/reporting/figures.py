from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def _bar_plot(df: pd.DataFrame, x_col: str, metric_cols: list[str], title: str, output_path: Path) -> None:
    long_df = df.melt(id_vars=[x_col], value_vars=metric_cols, var_name="metric", value_name="value")
    pivot = long_df.pivot(index=x_col, columns="metric", values="value")

    fig, ax = plt.subplots(figsize=(10, 5))
    pivot.plot(kind="bar", ax=ax)
    ax.set_title(title)
    ax.set_ylim(0, 1)
    ax.set_ylabel("Score")
    ax.legend(loc="lower right")
    fig.tight_layout()
    fig.savefig(output_path, dpi=200)
    plt.close(fig)


def export_figures(table_outputs: dict[str, Path], output_dir: Path) -> dict[str, str]:
    output_dir.mkdir(parents=True, exist_ok=True)
    outputs: dict[str, str] = {}

    full_summary_path = table_outputs.get("full_transcript_summary_csv")
    if full_summary_path and Path(full_summary_path).exists():
        full_df = pd.read_csv(full_summary_path)
        metric_cols = [
            col
            for col in full_df.columns
            if col.endswith("_mean") and "latency" not in col and "n_runs" not in col
        ]
        if not metric_cols:
            metric_cols = [
                col
                for col in full_df.columns
                if col
                in {
                    "assignment_accuracy",
                    "unit_assignment_accuracy",
                    "completion_accuracy",
                    "final_state_accuracy",
                }
            ]
        if metric_cols:
            path = output_dir / "full_transcript_metrics_by_structure.png"
            _bar_plot(full_df, "structure_condition", metric_cols, "Full Transcript Metrics by Structure", path)
            outputs["figure_full_transcript"] = str(path)

    inc_summary_path = table_outputs.get("incremental_summary_csv")
    if inc_summary_path and Path(inc_summary_path).exists():
        inc_df = pd.read_csv(inc_summary_path)
        metric_cols = [
            col
            for col in inc_df.columns
            if col.endswith("_mean") and "latency" not in col and "n_runs" not in col
        ]
        if not metric_cols:
            metric_cols = [
                col
                for col in inc_df.columns
                if col in {"assignment_accuracy", "unit_assignment_accuracy", "completion_accuracy", "current_state_accuracy"}
            ]
        if metric_cols:
            path = output_dir / "incremental_metrics_by_structure.png"
            _bar_plot(inc_df, "structure_condition", metric_cols, "Incremental Metrics by Structure", path)
            outputs["figure_incremental"] = str(path)

        latency_cols = [col for col in inc_df.columns if "latency" in col and (col.endswith("_mean") or col.endswith("latency"))]
        if latency_cols:
            long_df = inc_df.melt(
                id_vars=["structure_condition"],
                value_vars=latency_cols,
                var_name="metric",
                value_name="value",
            )
            fig, ax = plt.subplots(figsize=(8, 5))
            for metric_name, sub in long_df.groupby("metric"):
                ax.plot(sub["structure_condition"], sub["value"], marker="o", label=metric_name)
            ax.set_title("Incremental Detection Latency by Structure")
            ax.set_ylabel("Latency (prefix steps)")
            ax.legend(loc="best")
            fig.tight_layout()
            path = output_dir / "incremental_latency_by_structure.png"
            fig.savefig(path, dpi=200)
            plt.close(fig)
            outputs["figure_latency"] = str(path)

    combined_path = table_outputs.get("combined_condition_summary_csv")
    if combined_path and Path(combined_path).exists():
        combined = pd.read_csv(combined_path)
        comparison = combined[combined["metric_name"].isin(["assignment_accuracy", "current_state_accuracy", "final_state_accuracy"])]
        if not comparison.empty:
            fig, ax = plt.subplots(figsize=(10, 5))
            labels = [f"{r.structure_condition}\n{r.processing_mode}" for r in comparison.itertuples()]
            ax.bar(labels, comparison["mean"])
            ax.set_ylim(0, 1)
            ax.set_title("Condition Comparison (Structure x Processing)")
            ax.set_ylabel("Mean score")
            plt.xticks(rotation=20, ha="right")
            fig.tight_layout()
            path = output_dir / "structure_processing_comparison.png"
            fig.savefig(path, dpi=200)
            plt.close(fig)
            outputs["figure_structure_processing_comparison"] = str(path)

    return outputs
