# Dataset Generation and Validation Pipeline

## Overview

This repository contains a controlled synthetic dataset for firefighter radio communication, constructed as part of a research project on LLM-based monitoring of predefined operational tasks.

Beyond the dataset itself, this repository contributes a **reproducible, source-grounded dataset construction methodology**. The goal is not only to provide data, but to demonstrate how synthetic datasets can be systematically grounded in real-world sources while remaining controllable and auditable.

The approach combines:

- explicit grounding in external domain sources  
- structured prompt-based dataset generation  
- independent validation passes  
- iterative refinement under predefined acceptance criteria  

This process is designed to balance **realism, control, and reproducibility**, and is aligned with the broader goal of reproducible NLP research.

---

## Methodological Framing

The dataset was constructed using a controlled synthetic generation process grounded in three external sources:

1. Official radio communication protocols (BABS Sprechregeln)  
2. A real-world firefighter communication transcript  
3. Operational doctrine (FKS Einsatzführung)  

From these sources, structured **source note documents** were created and used to guide both generation and validation.

Two independent validation passes were applied:

- **Structural validation**: protocol adherence, communication structure, and realism of radio interaction  
- **Content validation**: operational plausibility, task validity, and consistency of task-state representations  

The dataset was iteratively refined until it satisfied predefined acceptance criteria. The goal was not perfect realism, but a **stable and defensible design point** suitable for evaluating closed-world task monitoring.

---

## Bootstrap Procedure

The entire pipeline is reproducible from a single meta-prompt.

### Step 1 — Meta-Prompt Initialization

A bootstrap prompt is provided at:
`.bootstrap/metaprompt.txt`

This prompt is designed to be inserted into a new ChatGPT session. It guides the creation of:

- three grounded source note files  
- one dataset generation specification  
- two validation specifications  

These documents form the `.agents/datasetgeneration/` folder and act as the **formal specification layer** for the dataset.

---

### Step 2 — Codex Prompt Generation

Using the bootstrap process, four Codex prompts were derived and stored in:
`.bootstrap/`

- `codex_1_generate-the-dataset.txt`
- `codex_2_structural-validation.txt`
- `codex_3_content-validation.txt`
- `codex_4_revision-pass-after-validation.txt`

These prompts implement the operational pipeline for dataset construction and refinement.

---

## Iterative Dataset Construction Process

The dataset was created through iterative application of the four Codex prompts:

### Step 1 — Dataset Generation

- Run: `codex_1_generate-the-dataset.txt`
- Output: initial synthetic dataset (5 scenarios) + construction log

### Step 2 — Structural Validation

- Run: `codex_2_structural-validation.txt`
- Evaluates:
  - radio protocol adherence  
  - message structure  
  - turn-taking plausibility  
  - communication realism  

### Step 3 — Content Validation

- Run: `codex_3_content-validation.txt`
- Evaluates:
  - operational plausibility  
  - task realism  
  - role-task alignment  
  - sequencing and dependencies  
  - gold-state traceability  

### Step 4 — Revision Pass

- Run: `codex_4_revision-pass-after-validation.txt`
- Applies targeted fixes based on validation reports:
  - local corrections where possible  
  - scenario regeneration only when necessary  

### Step 5 — Re-Validation

- Re-run:
  - structural validation  
  - content validation  
- Continue iteration if needed

---

## Iteration Summary

The process was executed for **13 full runs** of:

- generation → validation → revision → re-validation  

The iteration was stopped once both validation passes produced:

- no critical issues  
- only minor or limited moderate issues  
- stable dataset-level behavior  
- full schema and gold-label consistency  

Importantly, the stopping criterion was **fitness for purpose**, not perfect validation scores.

---

## Stopping Rule

The iteration process was guided by the following relaxed stopping criteria:

- no critical issues in either validation report  
- at most a small number of moderate issues per scenario  
- no repeated dataset-level issue patterns across consecutive rounds  
- sufficient diversity across the 5 scenarios  
- full consistency of schema and gold task states  

Once these conditions were satisfied, the process was terminated.

---

## Design Rationale

This pipeline reflects several design decisions:

### 1. Separation of Concerns

- generation, validation, and revision are handled independently  
- prevents circular bias between generation and evaluation  

### 2. Source Grounding

- all rules are derived from curated source notes  
- ensures traceability to real-world material  

### 3. Controlled Variability

- dataset includes realistic imperfections (e.g. partial updates, delayed confirmations)  
- avoids overly clean, artificial scenarios  

### 4. Reproducibility

- all steps are prompt-driven and documented  
- no hidden manual adjustments  

### 5. Bounded Realism

- the goal is not perfect simulation of reality  
- but a controlled, representative testbed for task-state monitoring  

---

## Outcome

The final dataset represents a **stable and validated synthetic benchmark** for:

- monitoring predefined tasks in multi-party communication  
- evaluating robustness to transcript structure variation  
- studying incremental inference behavior  

At the same time, the pipeline itself constitutes a reusable approach for:

- grounded synthetic dataset construction  
- LLM-assisted validation workflows  
- reproducible experimental setup design  

---

## Repository Structure (Relevant Parts)

`.bootstrap/`

- `metaprompt.txt`
- `codex_1_generate-the-dataset.txt`
- `codex_2_structural-validation.txt`
- `codex_3_content-validation.txt`
- `codex_4_revision-pass-after-validation.txt`

`.agents/datasetgeneration/`

- `dataset_generation.md`
- `dataset_validation_structure.md`
- `dataset_validation_content.md`
- `source_notes_sprechregeln.md`
- `source_notes_real_transcript.md`
- `source_notes_einsatzfuehrung.md`
- `validation_X/` for X in {1, 2, ..., 13}, each containing the validation reports and revision logs


---

## Reproducibility

To reproduce the dataset:

1. Start a new ChatGPT session  
2. paste `.bootstrap/metaprompt.txt`  
3. generate the specification documents  
4. run the Codex prompts in sequence  
5. iterate until stopping criteria are met  

---

## Final Note

This dataset should be understood as:

- **synthetic but grounded**  
- **controlled but realistic**  
- **validated but not overfitted to validation criteria**  

The pipeline intentionally stops at a point where remaining imperfections reflect **real-world ambiguity**, not construction errors.