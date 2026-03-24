# swisstext26

## Project Summary

This repository contains the paper, dataset, and evaluation pipeline for a bounded coordination-support capability in firefighter incident command: monitoring the state of predefined operational tasks from transcript evidence for a command-support dashboard.

## Canonical Scope

What this project is:

- closed-world task-state monitoring
- transcript-structure sensitivity analysis
- reproducible repeated-run evaluation with persisted artifacts

What this project is not:

- open-ended task discovery
- a generic incident copilot
- automated decision support
- a speech pipeline from raw audio

## Paper-Aligned Framing

- application setting: firefighter incident command
- support surface: dashboard for shared coordination
- predefined tasks come from procedures and incident context
- model role: propose conservative task-state updates under human oversight

Preferred phrasing:

- "command-support dashboard"
- "bounded coordination-support capability"
- "closed-world monitoring"

## Dataset Contract

Canonical scenario directory:

- `data/scenarios/synthetic_firefighter_radio_controlled_v1/`

Dataset facts used by the paper:

- 5 scenarios
- 102 messages
- 15 predefined tasks
- 15 assigned tasks
- 12 completed tasks
- 3 incomplete assigned tasks at scenario end

Transition timing semantics:

- prefer explicit `assignment_message_id` and `completion_message_id`
- linkage is annotation-grounded, not lexical-overlap-based
- first operative assignment anchors assignment timing
- later refinements to the same unit do not reset timing

## Evaluation Design

Structure conditions:

- `structured_dialogue`
- `no_speaker`
- `continuous_transcript`

Processing modes:

- `incremental`
- `full_transcript`

Interpretation rules:

- incremental results are the primary application-facing outcome
- latency is measured in prefix steps, not runtime
- latency must always be interpreted together with miss rate
- full-transcript results are a secondary offline reference
- terminal convergence gaps compare the last incremental prefix with the corresponding full-transcript result

## Core Guarantees

- configurable repeated runs with default `run_count=12`
- deterministic work keys
- persisted request / response / parse artifacts
- resume-safe execution via `skip_completed`
- deterministic local tests for stable logic
- exported tables and figures for paper reporting

## Canonical Commands

- install dependencies:
  - `python -m pip install -r code/requirements.txt`
- validate dataset:
  - `python scripts/validate_dataset.py`
- run tests:
  - `python -m pytest -q`
- execute the main evaluation workflow:
  - `code/evaluation_notebook.ipynb`

## Output Contract

Per run:

- `code/outputs/<run_id>/tables/full_transcript_per_scenario.csv`
- `code/outputs/<run_id>/tables/incremental_per_scenario.csv`
- `code/outputs/<run_id>/tables/full_transcript_summary.csv`
- `code/outputs/<run_id>/tables/incremental_summary.csv`
- `code/outputs/<run_id>/tables/combined_condition_summary.csv`
- `code/outputs/<run_id>/tables/all_condition_rows.csv`
- `code/outputs/<run_id>/tables/prefix_level_metrics.csv`
- `code/outputs/<run_id>/tables/terminal_convergence_per_scenario.csv`

Batch:

- `code/outputs/<run_tag>__batch/tables/full_transcript_summary.csv`
- `code/outputs/<run_tag>__batch/tables/incremental_summary.csv`
- `code/outputs/<run_tag>__batch/tables/combined_condition_summary.csv`
- `code/outputs/<run_tag>__batch/tables/all_condition_rows.csv`
- `code/outputs/<run_tag>__batch/tables/per_scenario_summary.csv`
- `code/outputs/<run_tag>__batch/tables/overall_summary.csv`
- `code/outputs/<run_tag>__batch/tables/terminal_convergence_per_scenario.csv`
- `code/outputs/<run_tag>__batch/tables/terminal_convergence_summary.csv`
