# NOTEBOOK.md

Execution contract for the SwissText 2026 evaluation notebook and its companion analysis notebooks.

## Notebook Purpose

Run the paper experiment end to end on the controlled firefighter dataset.

Primary experiment:

- structures: `structured_dialogue`, `no_speaker`, `continuous_transcript`
- processing modes: `incremental`, `full_transcript`
- repeated live evaluation runs with resume-safe artifacts

Primary notebook:

- `code/evaluation_notebook.ipynb`

Companion analysis:

- `code/completion_outcome_reanalysis.ipynb` for the ROUGE-L analysis of `completion_outcome`

## Reporting Priority

1. incremental monitoring accuracy
2. incremental detection latency together with miss rate
3. terminal convergence to the offline full-transcript reference
4. full-transcript reference evaluation

The full-transcript condition is a secondary offline reference, not the deployment-facing condition.

## Required Flow

1. State the bounded system framing and experiment design.
2. Build one explicit `NotebookConfig`.
3. Load and validate scenarios from `data/scenarios/synthetic_firefighter_radio_controlled_v1/`.
4. Render the three transcript-structure conditions.
5. Load prompts from `code/prompts/`.
6. Execute resume-safe requests.
7. Parse and persist predictions and errors.
8. Compute per-run metrics.
9. Export run-level tables and figures.
10. Aggregate repeated runs into batch summaries.
11. Run the separate `completion_outcome` reanalysis if needed for paper reporting.

## Design Rules

- Keep orchestration in the notebook; keep stable logic in `code/src/swisstext_eval/`.
- Preserve the closed-world formulation.
- No open-ended task discovery.
- No ontology matching or lexical-overlap-based linking semantics.
- Use conservative state prediction semantics.
- Treat incremental monitoring as the main application-facing result.
- Report latency only as correct-detection latency and always alongside miss rate.
- Use terminal convergence gaps to justify the offline reference.

## Runtime Configuration

The notebook uses `NotebookConfig` from `code/src/swisstext_eval/config.py`.

Important defaults:

- provider model: `gpt-5.2`
- temperature: `0.0`
- repeated runs: `12`
- prefix policy: `every_message`
- resume behavior: `skip_completed`

## Artifact Contract

Each request is keyed by:

`(run_id, scenario_id, structure_condition, processing_mode, prefix_index)`

Per-run artifacts live under:

`code/outputs/<run_id>/`

Key subdirectories:

- `config/`
- `requests/`
- `raw_responses/`
- `parsed_predictions/`
- `inputs_transformed/`
- `metrics/`
- `tables/`
- `figures/`
- `inspection/`

Batch outputs live under:

`code/outputs/<run_tag>__batch/`

## Required Tables

Per run:

- `full_transcript_per_scenario.csv`
- `incremental_per_scenario.csv`
- `full_transcript_summary.csv`
- `incremental_summary.csv`
- `combined_condition_summary.csv`
- `all_condition_rows.csv`
- `prefix_level_metrics.csv`
- `terminal_convergence_per_scenario.csv`

Batch:

- `full_transcript_summary.csv`
- `incremental_summary.csv`
- `combined_condition_summary.csv`
- `all_condition_rows.csv`
- `per_scenario_summary.csv`
- `overall_summary.csv`
- `terminal_convergence_per_scenario.csv`
- `terminal_convergence_summary.csv`

## Interpretation Constraints

- Assignment detection counts as correct only with the correct responsible unit.
- Completion detection counts as correct only when completion is predicted while preserving coherent assigned state and the correct unit.
- `completion_outcome_accuracy` remains an exported artifact but is not a meaningful headline result for the paper.
- Paper-level discussion of completion outcome should rely on the similarity-based reanalysis instead.
