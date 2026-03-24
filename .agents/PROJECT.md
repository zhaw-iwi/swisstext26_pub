# swisstext26

## Project Summary

Final evaluation pipeline for closed-world firefighter task monitoring.

System objective:

Given predefined tasks and transcript evidence, predict per-task state:
- assigned
- assigned_unit
- completed
- completion_outcome (optional)

Primary reporting priority:
1. incremental monitoring quality for the application setting
2. incremental detection responsiveness via conditional latency plus miss rate
3. terminal convergence to the offline reference
4. full-transcript reference evaluation

## Benchmark Semantics

Task-command linkage is annotation-grounded.

- A command is linked to a predefined task when it is unambiguously intended as that task under the dataset annotation rules and scenario meaning.
- Wording differences between command text and `task_name` are allowed.
- Lexical overlap is not the benchmark semantics for linking commands to tasks.

Assignment timing uses the first operative assignment.

- A task becomes assigned at the first message that operationally hands responsibility for that predefined dashboard task to a unit.
- Later refinement, narrowing, or operationalization of the same task to the same unit does not create a new assignment event.
- Status requests, clarifications, or completion-check instructions do not reset assignment timing.
- Reassignment should remain out of scope unless explicitly represented in the dataset.

Dataset contract for transition timing:
- prefer explicit `assignment_message_id` and `completion_message_id` annotations in `gold_task_states`
- if transcript-only derivation is ambiguous, the pipeline should fail conservatively rather than guess

## Final Experiment Design

- Primary axis (structure):
  - `structured_dialogue`
  - `no_speaker`
  - `continuous_transcript`
- Secondary axis (processing):
  - `full_transcript`
  - `incremental`

The full experiment evaluates all 6 cells for each scenario and each run.

Interpretation guidance:
- incremental results are the main paper outcome because they match the live dashboard setting
- latency metrics describe responsiveness of correct state updates, not model runtime
- latency must be reported together with miss rate
- full-transcript metrics are useful only as a secondary offline end-of-scenario reference
- terminal convergence gaps justify the full-transcript reference by checking whether the last incremental prefix approaches it

## Core Guarantees

- configurable repeated runs (default 12)
- deterministic work keys per request
- request/response artifact persistence
- resume-safe execution (`skip_completed`)
- full and incremental metrics
- cross-run mean/std/CI95 exports for paper tables

## Canonical Commands

- Validate dataset:
  - `python scripts/validate_dataset.py`
- Run tests:
  - `python -m pytest -q`
- Execute notebook:
  - `code/evaluation_notebook.ipynb`

## Output Contract

Per run (`code/outputs/<run_id>/tables/`):
- `full_transcript_summary.csv`
- `incremental_summary.csv`
- `combined_condition_summary.csv`
- `all_condition_rows.csv`
- `terminal_convergence_per_scenario.csv`

Batch (`code/outputs/<run_tag>__batch/tables/`):
- `full_transcript_summary.csv`
- `incremental_summary.csv`
- `combined_condition_summary.csv`
- `all_condition_rows.csv`
- `per_scenario_summary.csv`
- `overall_summary.csv`
- `terminal_convergence_per_scenario.csv`
- `terminal_convergence_summary.csv`
