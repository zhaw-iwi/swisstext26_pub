# SwissText 2026 Paper Specification

## Paper Claim

This project studies a bounded coordination-support capability for firefighter incident command: monitoring the state of predefined operational tasks from multi-party radio transcripts for a command-support dashboard.

The paper does not study open-ended task discovery, autonomous command assistance, or a generic incident copilot.

## Research Question

How much transcript structure is required for reliable closed-world task-state monitoring in firefighter incident command?

Concretely, the comparison varies:

- `structured_dialogue`
- `no_speaker`
- `continuous_transcript`

and asks whether speaker identities and explicit utterance boundaries materially affect monitoring quality.

## System Framing

- The dashboard task list is available before transcript analysis.
- Tasks originate from procedures and incident context.
- The model proposes conservative state updates under human oversight.
- The system supports shared coordination; it does not make operational decisions.

Preferred wording:

- "bounded coordination-support capability"
- "command-support dashboard"
- "closed-world task-state monitoring"
- "predefined operational tasks"

Avoid shorthand such as:

- "digital scribe"
- "task extraction"
- "ontology matching"
- "open-ended assistance"

## Task Formulation

Input:

- predefined task list for the scenario
- transcript evidence under one of the three structure conditions

Output for each predefined task:

- `assigned` (`bool`)
- `assigned_unit` (`str | null`)
- `completed` (`bool`)
- `completion_outcome` (`str | null`)

Conservative interpretation rule:

- when evidence is insufficient, keep values at `false` / `null`

## Dataset Facts

- 5 German-language synthetic firefighter scenarios
- 102 ordered radio messages in total
- 15 predefined tasks in total
- 15 assigned tasks
- 12 completed tasks
- 3 tasks still assigned but incomplete at scenario end

Construction facts that should remain aligned with the paper:

- source-grounded synthetic dataset
- grounded in radio-procedure material, a real firefighter transcript, and procedural regulations
- generation and validation conducted with `gpt-5.4`
- two rubric-guided validation streams: structural and content
- the generation-validation-revision loop ran for 12 rounds

Repository nuance:

- the repository also retains `datasetgeneration/target/validation_13/` as an additional audit snapshot; do not let that overwrite the paper's reported 12-round loop

## Evaluation Contract

Experimental design:

- 3 transcript structures x 2 processing modes
- processing modes:
  - `incremental`
  - `full_transcript`

Interpretation priority:

1. incremental monitoring accuracy
2. incremental detection responsiveness
3. terminal convergence to the offline full-transcript reference
4. full-transcript reference results

Primary metrics:

- assignment accuracy
- unit assignment accuracy
- completion accuracy
- state accuracy
- assignment detection latency
- completion detection latency
- assignment detection miss rate
- completion detection miss rate
- terminal assignment gap
- terminal unit-assignment gap
- terminal completion gap
- terminal state gap

`completion_outcome` handling:

- exact match remains zero in the reported results
- paper interpretation uses a ROUGE-L reanalysis on gold-completed tasks only
- do not present exact-match `completion_outcome_accuracy` as a substantive result

## Gold Transition Principle

- task-command linkage is annotation-grounded
- do not derive task linkage primarily from lexical overlap
- assignment timing uses the first operative assignment to the responsible unit
- later refinements to the same unit do not reset the assignment point
- ambiguous timing should be resolved through explicit scenario metadata, not heuristics

## Contribution Scope

- bounded operational formulation for shared coordination support
- controlled transcript-structure comparison with fixed scenario content
- reproducible evaluation pipeline with auditable artifacts and deterministic tests
