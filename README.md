# SwissText 2026: Final Closed-World Task Monitoring Experiment

This repository runs the final paper experiment for known-task monitoring from firefighter communication.

Research question:

> What transcript structure is required for reliable LLM-based monitoring of known operational tasks?

## Final Experimental Design

Two axes are evaluated as a Cartesian product (3 x 2):

- Transcript structure:
  - `structured_dialogue`
  - `no_speaker`
  - `continuous_transcript`
- Processing mode:
  - `full_transcript`
  - `incremental`

For every scenario and run, all 6 cells are executed.

## Task Formulation

Given:

- predefined scenario task list
- communication transcript

Predict per task:

- `assigned`
- `assigned_unit`
- `completed`
- optional `completion_outcome`

## Configuration Surface

The notebook and runner use one explicit config object (`NotebookConfig`):

- `experiment.run_count` (default `12`)
- `experiment.selected_scenarios`
- `experiment.selected_structure_conditions`
- `experiment.selected_processing_modes`
- `experiment.incremental_prefix_policy` (default `every_message`)
- `experiment.api_batch_size`
- `experiment.resume_behavior` (default `skip_completed`)
- `experiment.output_run_tag`
- `provider.model_name`, `temperature`, `max_tokens`, `timeout_seconds`, `retry_count`
- `experiment.prompt_version_tag`
- `evaluation.export_tables`, `evaluation.export_figures`

## Resume-Safe Request Persistence

Each LLM request is persisted with deterministic work identity:

`(run_id, scenario_id, structure_condition, processing_mode, prefix_index)`

Per-request JSON artifact path:

`code/outputs/<run_id>/requests/<scenario_id>/<structure_condition>/<processing_mode>/prefix_<idx|full>.json`

Artifacts include:

- run/scenario/condition metadata
- prompt payload
- model settings
- timestamps
- raw response
- parsed output
- error metadata
- status

With `resume_behavior="skip_completed"`, reruns continue unfinished work only.

## Metrics

### Full Transcript

- `assignment_accuracy`
- `unit_assignment_accuracy`
- `completion_accuracy`
- `final_state_accuracy`
- `completion_outcome_accuracy` (optional)

### Incremental

Per-prefix and aggregated:

- `assignment_accuracy`
- `unit_assignment_accuracy`
- `completion_accuracy`
- `current_state_accuracy`
- `assignment_detection_latency`
- `completion_detection_latency`

## Outputs

Per run (`code/outputs/<run_id>/tables/`):

- `full_transcript_per_scenario.csv`
- `incremental_per_scenario.csv`
- `full_transcript_summary.csv`
- `incremental_summary.csv`
- `combined_condition_summary.csv`
- `all_condition_rows.csv`
- `prefix_level_metrics.csv` (if enabled)

Batch (repeated runs) (`code/outputs/<run_tag>__batch/tables/`):

- `full_transcript_summary.csv` (mean/std/ci95)
- `incremental_summary.csv` (mean/std/ci95)
- `combined_condition_summary.csv`
- `all_condition_rows.csv`
- `per_scenario_summary.csv`
- `overall_summary.csv`

## Run

1. Install dependencies:

```powershell
python -m pip install -r code/requirements.txt
```

2. Set API key for live mode:

```powershell
$env:OPENAI_API_KEY='YOUR_KEY'
```

3. Run notebook:

- `code/evaluation_notebook.ipynb`

4. Run tests:

```powershell
python -m pytest -q
```

5. Optional dataset validation:

```powershell
python scripts/validate_dataset.py
```
