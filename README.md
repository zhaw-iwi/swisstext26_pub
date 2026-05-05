# SwissText 2026: Task-State Monitoring for Firefighter Incident Command

This repository contains the paper, dataset, and evaluation pipeline for a bounded coordination-support capability: monitoring the state of predefined firefighter tasks from multi-party radio transcripts for a command-support dashboard.

The central paper question is:

> How much transcript structure is required for reliable closed-world task-state monitoring?

## Paper Framing

The paper studies a narrow monitoring problem.

- Tasks are predefined before transcript analysis.
- The model updates task state from transcript evidence.
- The target system is a dashboard for shared coordination under human oversight.
- The work does not study open-ended task discovery or autonomous command decisions.

## Repository Contents

- `main.tex` and the section `.tex` files: paper source
- `data/scenarios/synthetic_firefighter_radio_controlled_v1/`: scenario dataset
- `code/src/swisstext_eval/`: evaluation pipeline
- `code/tests/`: deterministic local tests
- `code/evaluation_notebook.ipynb`: main experiment notebook
- `code/completion_outcome_reanalysis.ipynb`: ROUGE-L analysis for `completion_outcome`
- `datasetgeneration/`: source-grounded dataset construction and validation materials; see `README_DATASET_GENERATION.md` for the LLM-as-judge workflow, repository layout, and dataset-generation instructions

## Dataset Summary

The dataset used in the paper contains:

- 5 German-language firefighter scenarios
- 102 ordered radio messages
- 15 predefined tasks
- 15 assigned tasks
- 12 completed tasks
- 3 tasks that remain assigned but incomplete at scenario end

The dataset is synthetic but source-grounded. It is grounded in radio-procedure material, a real firefighter transcript, and procedural regulations. Scenario generation and validation were carried out with `gpt-5.4` under constrained, rubric-guided prompts. The paper reports a 12-round generation-validation-revision loop; the repository keeps the iterative validation trail under `datasetgeneration/target/validation_1/` through `datasetgeneration/target/validation_13/` as audit material.

## Experiment Design

The evaluation uses a `3 x 2` design.

Transcript structures:

- `structured_dialogue`
- `no_speaker`
- `continuous_transcript`

Processing modes:

- `incremental`
- `full_transcript`

Incremental evaluation is the primary application-facing condition. Full-transcript evaluation is a secondary offline reference.

## Task Formulation

Given a predefined task list and transcript evidence, the model predicts for each task:

- `assigned`
- `assigned_unit`
- `completed`
- `completion_outcome`

The prompt is conservative: if the evidence is insufficient, fields remain `false` or `null`.

## Main Evaluation Facts

- evaluation model: `gpt-5.2`
- temperature: `0.0`
- repeated runs: `12`
- primary metrics:
  - assignment accuracy
  - unit assignment accuracy
  - completion accuracy
  - state accuracy
  - assignment / completion detection latency
  - assignment / completion miss rate
  - terminal convergence gaps

For `completion_outcome`, the exact-match metric remained uninformative in the evaluation. The paper therefore also reports a similarity-based re-analysis on gold-completed tasks only, using ROUGE-L. That re-analysis is documented in:

- `code/completion_outcome_reanalysis.ipynb`

The paper's main conclusion is that transcript simplification has only small effects in this controlled setup. The most persistent weakness is grounding the responsible unit, not detecting assignment or completion itself.

## Run

Install dependencies:

```powershell
python -m pip install -r code/requirements.txt
```

Set the API key for live evaluation:

```powershell
$env:OPENAI_API_KEY='YOUR_KEY'
```

Run tests:

```powershell
python -m pytest -q
```

Validate the dataset:

```powershell
python scripts/validate_dataset.py
```

Execute the main experiment in:

- `code/evaluation_notebook.ipynb`

## Outputs

Per-run artifacts are stored under:

- `code/outputs/<run_id>/`

Repeated-run summaries are stored under:

- `code/outputs/<run_tag>__batch/`

Key exported tables include:

- `full_transcript_summary.csv`
- `incremental_summary.csv`
- `combined_condition_summary.csv`
- `all_condition_rows.csv`
- `terminal_convergence_per_scenario.csv`
- `terminal_convergence_summary.csv`

## Dataset Construction Materials

Dataset-generation provenance and validation materials are documented in:

- `README_DATASET_GENERATION.md`

## Completion-Outcome Reanalysis

The completion-outcome reanalysis materials are documented in:

- `code/completion_outcome_reanalysis.ipynb`
