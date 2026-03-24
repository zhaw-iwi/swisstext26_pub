# SwissText 2026 Paper Specification

## Paper Positioning

This paper studies whether a large language model can reliably monitor the execution state of predefined firefighter operational tasks from radio communication transcripts under different transcript-structure conditions.

## Research Question

What transcript structure is required for reliable known-task state monitoring in firefighter incident command support?

## Task Formulation

Input:
- predefined task list for a scenario
- transcript under one of three conditions:
  - `structured_dialogue`
  - `no_speaker`
  - `continuous_transcript`

Output (for each predefined task):
- `assigned` (boolean)
- `assigned_unit` (nullable string)
- `completed` (boolean)
- `completion_outcome` (nullable string)

## System Framing

The system is a digital scribe for incident command.
Tasks are already present on the operational dashboard.
The model does not discover new tasks; it monitors state changes of known tasks from communication evidence.

## Evaluation Focus

Primary reporting order:
- incremental monitoring accuracy
- incremental detection responsiveness
- full-transcript reference evaluation

Primary metrics:
- assignment accuracy
- unit assignment accuracy
- completion accuracy
- current-state accuracy (`NOT_ASSIGNED`, `ASSIGNED`, `COMPLETED`) for incremental evaluation
- assignment detection latency
- completion detection latency
- assignment detection miss rate
- completion detection miss rate
- final state accuracy (`NOT_ASSIGNED`, `ASSIGNED`, `COMPLETED`) for full-transcript reference evaluation
- optional completion outcome accuracy
- terminal assignment gap
- terminal unit-assignment gap
- terminal completion gap
- terminal state gap

Primary comparison axis:
- transcript condition robustness

Latency interpretation:
- latency is measured in prefix steps, not wall-clock time
- latency is conditional on successful correct detection
- assignment detection requires `assigned=true` with the correct unit
- completion detection requires `completed=true` while preserving coherent assigned state and correct unit
- miss rate must be reported alongside latency so responsiveness is interpretable on its own

Full-transcript interpretation:
- full-transcript evaluation is an offline reference, not the application condition
- use terminal convergence gaps to justify the reference by checking whether the last incremental prefix approaches the full-transcript results

## Transition Annotation Principle

Gold transition timing must remain conservative and annotation-grounded.

- Do not derive task-command linkage primarily from lexical overlap between `task_name` and command wording.
- Assignment timing is anchored to the first operative command that hands responsibility for the predefined task to the assigned unit.
- Later refinements, clarifications, or continuation instructions to the same unit do not create a new assignment event.
- When assignment or completion timing is ambiguous from the transcript alone, prefer explicit scenario metadata rather than heuristic matching.
- Failing on ambiguous transition derivation is preferable to silently guessing.

## Contribution Scope

- operationally aligned closed-world monitoring formulation
- controlled transcript-structure comparison
- reproducible pipeline with auditable artifacts and deterministic tests
