# Dataset Generation and Validation

This repository includes the source-grounded synthetic dataset used in the paper and the materials used to construct and validate it.

The role of these materials is provenance and auditability. The paper's empirical contribution is the transcript-structure evaluation on the dataset, not the dataset-generation workflow by itself.

## Dataset Role

The dataset exists to support a controlled comparison of transcript-structure conditions while keeping underlying operational content fixed.

That is why the dataset is:

- synthetic
- source-grounded
- closed-world
- small and intentionally controlled

It is not meant as a realism corpus, a raw-audio dataset, or a dataset for open-ended task discovery.

## Paper-Aligned Construction Summary

The paper describes the dataset as follows:

- grounded in three source types:
  - Swiss radio-procedure material
  - a real firefighter communication transcript
  - canonical procedural regulations
- generated as fixed-schema scenario JSON files
- validated in two rubric-guided streams:
  - structural validation
  - content validation
- generated and validated with `gpt-5.4`
- accepted after a 12-round generation-validation-revision loop

The repository preserves the full validation trail under `datasetgeneration/target/validation_1/` through `datasetgeneration/target/validation_13/`. These folders document the iterative construction history and audit trail. The paper reports the accepted dataset in terms of a 12-round generation-validation-revision loop; the extra retained validation folder is part of the repository history, not a separate paper claim.

## Dataset Contents

The dataset used in the paper is located at:

- `data/scenarios/synthetic_firefighter_radio_controlled_v1/`

Paper-level dataset facts:

- 5 German-language scenarios
- 102 ordered messages
- 15 predefined tasks
- 15 task-state traces
- 12 completed tasks
- 3 assigned but incomplete tasks at scenario end

Each scenario stores:

- ordered radio messages
- predefined monitored tasks
- gold task states
- transition annotations for assignment and completion timing

## Repository Layout

Dataset-construction materials live under:

- `datasetgeneration/boostrap/`
- `datasetgeneration/target/`

Important note:

- the directory name is `boostrap/` in the repository

Key materials:

- `datasetgeneration/boostrap/metaprompt.txt`
- `datasetgeneration/boostrap/codex_1_generate-the-dataset.txt`
- `datasetgeneration/boostrap/codex_2_structural-validation.txt`
- `datasetgeneration/boostrap/codex_3_content-validation.txt`
- `datasetgeneration/boostrap/codex_4_revision-pass-after-validation.txt`
- `datasetgeneration/target/dataset_generation.md`
- `datasetgeneration/target/dataset_validation_structure.md`
- `datasetgeneration/target/dataset_validation_content.md`
- `datasetgeneration/target/source_notes_sprechregeln.md`
- `datasetgeneration/target/source_notes_real_transcript.md`
- `datasetgeneration/target/source_notes_einsatzfuehrung.md`
- `datasetgeneration/target/validation_*/`

The repository keeps these materials in `datasetgeneration/target/`.

## How To Generate The Dataset From These Materials

If you want to reconstruct the dataset-generation workflow from the materials in `datasetgeneration/`, use the folders in this order.

1. Read the bootstrap prompt in `datasetgeneration/boostrap/metaprompt.txt`.
2. Use that prompt to initialize a fresh chat session that recreates the dataset-specification layer.
3. Treat the specification documents in `datasetgeneration/target/` as the canonical target documents for that process:
   - `dataset_generation.md`
   - `dataset_validation_structure.md`
   - `dataset_validation_content.md`
   - `source_notes_sprechregeln.md`
   - `source_notes_real_transcript.md`
   - `source_notes_einsatzfuehrung.md`
4. Run the operational prompts from `datasetgeneration/boostrap/` in sequence:
   - `codex_1_generate-the-dataset.txt`
   - `codex_2_structural-validation.txt`
   - `codex_3_content-validation.txt`
   - `codex_4_revision-pass-after-validation.txt`
5. After each pass, write the resulting artifacts into `datasetgeneration/target/`:
   - update the top-level construction documents when the specification changes
   - write round-specific reports into the next `validation_<n>/` folder
6. Repeat the structural validation, content validation, and revision cycle until the dataset satisfies the intended stopping rule.
7. Compare the resulting scenario files against `data/scenarios/synthetic_firefighter_radio_controlled_v1/`, which contains the dataset used by the paper.

In practical terms, `datasetgeneration/boostrap/` contains the executable prompt materials and `datasetgeneration/target/` contains the specification, source notes, and validation history that those prompts operate against.

## Validation Logic

The two validation streams serve different purposes.

Structural validation checks:

- radio style and protocol coherence
- acknowledgement structure
- turn-taking plausibility
- transcript realism under the intended communication style

Content validation checks:

- operational plausibility
- role-task alignment
- sequencing and dependencies
- traceability of gold states to explicit message evidence

## Gold-State Semantics

The paper relies on annotation-grounded transition timing.

- Task-command linkage is not defined by lexical overlap with the task name.
- Assignment timing is anchored to the first operative assignment to the responsible unit.
- Later refinements to the same unit do not reset the assignment point.
- Completion timing is tied to explicit completion evidence or explicit scenario metadata.

This is the reason the scenario JSON files include transition annotations rather than forcing the evaluation pipeline to infer them heuristically from wording.

## How To Use These Materials

Use the dataset-generation materials to understand:

- how the dataset was grounded
- what was validated during construction
- how the scenarios evolved across revisions
- how to reconstruct the prompt-driven generation workflow

Do not treat them as the main entry point for running the paper experiment. For that, start with:

- `README.md`
- `main.tex`
- `code/evaluation_notebook.ipynb`

## Reproducibility Caveat

The repository preserves the prompt-driven workflow and its audit trail, but the paper's main reproducibility claim is narrower:

- the dataset files are versioned
- the evaluation code is deterministic outside live API calls
- repeated runs and persisted artifacts make the reported evaluation traceable

Synthetic dataset construction with live LLMs should be understood as controlled and documented, not as bit-for-bit replayable in perpetuity.
