# Dataset Revision Log

Dataset: `synthetic_firefighter_radio_controlled_v1`  
Revision date: 2026-03-21

## Revision Summary

The dataset was revised against both validation reports with a conservative policy:

- fixed local structural and content-alignment issues where possible
- preserved the fixed JSON schema
- preserved the closed-world predefined-task setup
- preserved scenario diversity and overall task difficulty
- avoided full-scenario regeneration because no scenario was reported as systematically broken

## Changed Files

- `s1.json`
- `s2.json`
- `s3.json`
- `s4.json`
- `s5.json`

## File-Level Changes

### `s1.json`

Fix type: local revision

Issues fixed:

- softened the overly compressed acknowledgement at message `10` so it now reads as readiness confirmation rather than immediate execution-plus-completion
- added a local suppression progress report from `Angriffstrupp` before ventilation release to improve operational continuity and reduce the impression of an abrupt transition from search result to smoke control

Result:

- clearer separation between acknowledgement, ongoing suppression, and later ventilation
- stronger scenario plausibility without changing the monitored task inventory

### `s2.json`

Fix type: local revision

Issues fixed:

- strengthened message `2` with explicit sender, receiver, message type, and closure so it no longer drops all structural anchors at once
- added an explicit acknowledgement after the directed `Befehl` to `Messgruppe` before the later measurement report

Result:

- improved protocol adherence and acknowledgement pattern traceability
- preserved the incomplete `CO-Nachkontrolle` task while making the command chain structurally cleaner

### `s3.json`

Fix type: local revision

Issues fixed:

- tightened the `Sicherungstrupp` order and readback so the monitored task and its later evidence align more directly
- removed the earlier mismatch where the order contained a narrower untracked sub-requirement (`Hauswart`) while the evidence referred more broadly to holding people at the assembly point

Result:

- cleaner traceability between assignment, readback, completion evidence, and predefined task `T1`

### `s4.json`

Fix type: local revision

Issues fixed:

- replaced the looser phrase `wir bleiben drauf` with a more radio-typical progress report while keeping realistic field compression
- added the missing acknowledgement after the directed cooling order in message `11`

Result:

- improved protocol adherence for a previously flagged command
- kept `T3` correctly incomplete with explicit progress evidence

### `s5.json`

Fix type: local revision

Issues fixed:

- strengthened the early `Drehleiter` status line with explicit addressing
- added a short police acknowledgement to the handover-readiness message

Result:

- improved structural anchoring of a self-initiated status message
- made the handover close more like a realistic radio exchange

## Full-Scenario Regenerations

- None.

Rationale:

- both validation reports rated all scenarios as overall `PASS`
- the remaining issues were local and repairable without replacing otherwise good scenario material

## Remaining Limitations

- the dataset still intentionally models incident slices rather than full end-to-end incident closure in every scenario
- several scenarios remain somewhat tidier than highly noisy real radio traffic; this was kept deliberately to preserve label traceability
- the monitored task inventory remains intentionally narrow and closed-world, so some tactically relevant follow-on work still appears only in messages and not as separate predefined tasks

## Verification Performed

- all modified JSON files parse successfully
- message ids remain strictly increasing within each scenario
- each `gold_task_states.completion_outcome` still matches an existing message text exactly
