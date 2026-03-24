# Dataset Revision Log

Dataset folder: `data/scenarios/synthetic_firefighter_radio_controlled_v1`

## Changed Files

- `s1.json`
- `s2.json`
- `s3.json`
- `s4.json`
- `s5.json`

## Fixes Applied

### `s1.json`

- Type: local revision
- Fixed unclosed turn allocation by changing message `12` from a report ending in `antworten` to a closed report ending in `Schluss`.
- Tightened message `10` wording so the acknowledgement names the staged ventilation resource explicitly.
- Updated `gold_task_states.T2.completion_outcome` to match the revised message text exactly.

### `s2.json`

- Type: local revision
- Fixed repeated unacknowledged turn-allocation issues by changing messages `7`, `8`, and `11` from status reports ending in `antworten` to closed reports ending in `Schluss`.
- Strengthened closure discipline in acknowledgement messages `5` and `10`.
- Relabeled message `12` from `Meldung` to `Befehl` because it directs the Messgruppe to start work.
- Narrowed predefined task `T3` from `CO-Nachkontrolle Tiefgarage` to `CO-Nachkontrolle Vorraum und Rampe` so task scope matches assignment and evidence.
- Updated `gold_task_states.T1.completion_outcome` to match the revised message text exactly.

### `s3.json`

- Type: local revision
- Fixed repeated unacknowledged turn-allocation issues by changing messages `9`, `10`, and `11` from progress reports ending in `antworten` to closed reports ending in `Schluss`.
- Strengthened closure discipline in acknowledgement messages `4` and `8`.
- Relabeled message `12` from `Meldung` to `Befehl` because it assigns follow-up control work to the Angriffstrupp.
- Corrected `gold_task_states.T3.completion_outcome` to the actual completion-style message `13` instead of the earlier still-ongoing message `11`.
- Updated `gold_task_states.T2.completion_outcome` to match the revised message text exactly.

### `s4.json`

- Type: local revision
- Fixed repeated unacknowledged turn-allocation issues by changing messages `8`, `9`, and `10` from reports ending in `antworten` to closed reports ending in `Schluss`.
- Strengthened closure discipline in acknowledgement messages `3` and `5`.
- Relabeled message `11` from `Meldung` to `Befehl` because it orders continued cooling.
- Added new message `13` to provide explicit, observable completion evidence for foam suppression after the earlier progress-only report in `9`.
- Corrected `gold_task_states.T2.completion_outcome` to point to the new explicit completion message instead of the still-ongoing `Nachschaeumen laeuft` report.
- Updated `gold_task_states.T1` and `T3` completion text to match the revised message wording exactly.

### `s5.json`

- Type: local revision
- Fixed repeated unacknowledged turn-allocation issues by changing messages `9` and `12` from reports ending in `antworten` to closed reports ending in `Schluss`.
- Strengthened closure discipline in short acknowledgement/status messages `2`, `3`, `5`, `7`, and `11`.
- Updated `gold_task_states.T2.completion_outcome` to match the revised message text exactly.

## Remaining Limitations

- `s1.json` still compresses the operational picture around support tasks (water, search, ventilation) more than around explicit suppression-task tracking. This is internally coherent enough to keep, but it remains a mildly abstracted task layer compared with the message stream.
- The dataset is now more consistent about `Schluss` and about reserving `antworten` for turns that actually expect a reply, but some realistic protocol looseness is intentionally preserved.
- Scenario structures remain comparable across the dataset because all five files were designed for the same closed-world monitoring setup; the revision improved variation in protocol tightness but did not redesign scenario archetypes from scratch.

## Revision Summary

- All fixes were local revisions.
- No full-scenario regeneration was required.
- The main improvements were:
  - gold-label evidence now points to actual completion messages,
  - task scope better matches assignment/evidence where flagged,
  - command/report labeling is more consistent,
  - turn-taking markers are less often left hanging without a reply.
