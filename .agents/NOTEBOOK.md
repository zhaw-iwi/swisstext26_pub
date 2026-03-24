# NOTEBOOK.md

Execution contract for the final SwissText 2026 notebook.

## Notebook Purpose

Run the final 3x2 experiment end-to-end with repeated resumable evaluation.

Axes:

- structure: `structured_dialogue`, `no_speaker`, `continuous_transcript`
- processing: `full_transcript`, `incremental`

Primary reporting priority:

1. incremental monitoring accuracy
2. incremental detection latency together with miss rate
3. terminal convergence to the offline reference
4. full-transcript reference evaluation

## Required Notebook Flow

1. Experiment purpose and design overview.
2. Single configuration object (`NotebookConfig`).
3. Imports and environment setup.
4. Scenario loading and validation.
5. Transcript condition generation.
6. Prompt loading/building.
7. Resume-aware request execution.
8. Parsing / artifact inspection.
9. Metric computation.
10. Aggregation across scenarios/conditions.
11. Table export.
12. Figure export.
13. Final run summary.

## Notebook Design Rules

- Keep orchestration in notebook; core logic in `code/src/swisstext_eval`.
- No open-ended task extraction.
- No ontology/category matching.
- Use a concrete dataset directory containing scenario JSON files, not only the parent `data/scenarios` folder when datasets are organized in subdirectories.
- Keep conservative state prediction semantics.
- Treat incremental evaluation as the main application-facing result.
- Report latency only as correct-detection latency and always pair it with miss rate.
- Treat full-transcript results as a secondary offline reference point rather than the main outcome.
- Report terminal convergence gaps to justify the offline reference.

## Mandatory Artifact Behavior

Every request must persist prompt/response/parse/error with deterministic key:

`(run_id, scenario_id, structure_condition, processing_mode, prefix_index)`

Resume default: skip already completed request artifacts.

## Repeated Runs

Default target is 12 runs (`experiment.run_count=12`), configurable.

Batch outputs live under `code/outputs/<run_tag>__batch/`.

## Testing Requirement

Stable logic in `code/src/swisstext_eval` must be covered by deterministic local tests.
No automated test depends on live API calls.

## Incremental Detection Metrics

Required incremental reporting:
- assignment accuracy
- unit assignment accuracy
- completion accuracy
- current-state accuracy
- assignment detection latency
- completion detection latency
- assignment detection miss rate
- completion detection miss rate

Required reference reporting:
- terminal assignment gap
- terminal unit-assignment gap
- terminal completion gap
- terminal state gap

Detection semantics:
- latency is measured in prefix steps after the gold transition point
- latency is conditional on successful correct detection
- assignment detection requires a correct positive assignment prediction including the correct unit
- completion detection requires a correct positive completion prediction while preserving coherent assigned state and correct unit
- miss rate is the share of gold transitions never correctly detected before the scenario ended
- task-command linkage for gold transitions is annotation-grounded, not based primarily on token overlap
- assignment timing is anchored to the first operative command for the predefined task
- later refinements to the same unit do not reset assignment timing
- ambiguous transition timing should be resolved through explicit scenario metadata such as `assignment_message_id` and `completion_message_id`

Reference semantics:
- full-transcript evaluation is not motivated by the live dashboard workflow itself
- it serves as an offline reference for the performance ceiling once all evidence is available
- terminal convergence gaps compare the last incremental prefix with the corresponding full-transcript result
