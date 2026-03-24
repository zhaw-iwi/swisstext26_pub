# DATASET_REVISION_LOG

Dataset folder: `data/scenarios/synthetic_firefighter_radio_controlled_v1`

## Changed Files

- `s1.json`
- `s2.json`
- `s3.json`
- `s4.json`
- `s5.json`

## Revision Details

### `s1.json`

- Fix type: Local revision
- Issues fixed:
  - Added an explicit command-side closure state after the incomplete ventilation report.
  - Reduced the structural "open loop" problem at scenario end without falsely marking the task as completed.
- Change made:
  - Added message `17` from `Einsatzleitung` instructing continued entrainment and maintaining staircase restriction until release.

### `s2.json`

- Fix type: Local revision
- Issues fixed:
  - Added an explicit command-side continuation/containment state after the incomplete CO measurement report.
  - Reduced the structural "open loop" problem at scenario end while preserving the incomplete task label.
- Change made:
  - Added message `19` from `Einsatzleitung` keeping the area closed and ordering continued follow-up measurement when visibility permits.

### `s3.json`

- Fix type: Local revision
- Issues fixed:
  - Resolved the main content-validation traceability defect for `T3`.
  - Aligned the predefined task wording with the broader operational order in message `7`.
  - Moved `T3` completion evidence to the stronger final control message.
- Changes made:
  - Renamed `T3` from `Brandraum Keller West abloeschen` to `Brandraum Keller West erkunden und abloeschen`.
  - Updated `T3.completion_outcome` to message `13`: `keine Ausbreitung in den Installationsschacht, Brandraum Keller West unter Kontrolle`.

### `s4.json`

- Fix type: Local revision
- Issues fixed:
  - Corrected protocol-function mismatch in message `14` by changing it from `Meldung` to `Befehl`.
  - Restored explicit address and order framing for message `18`.
  - Closed the final active command loop with a clear acknowledgement while keeping the gas-cylinder cooling task incomplete.
- Changes made:
  - Revised message `14` to a directed `Befehl` with `antworten`.
  - Revised message `18` to `An Wassertrupp von Einsatzleitung, Befehl: ...`.
  - Added message `19` as the Wassertrupp acknowledgement/continuation report.

### `s5.json`

- Fix type: Local revision
- Issues fixed:
  - Improved dataset-level role consistency by replacing the overloaded `Sicherungstrupp` label in the final-control thread.
  - Preserved the scenario logic while making the assigned unit more semantically stable for inspection work.
- Changes made:
  - Renamed the final-control unit from `Sicherungstrupp` to `Kontrolltrupp` in messages `12`, `13`, `15`, `16`, `17`.
  - Updated `gold_task_states.T3.assigned_unit` and `completion_outcome` accordingly.

## Full-Scenario Regeneration

- None.
- All fixes were handled as local revisions because the reported problems were traceable and repairable without replacing an entire scenario.

## Remaining Limitations

- The dataset still intentionally contains controlled shorthand and imperfect protocol adherence; it is not meant to be fully textbook-clean radio traffic.
- `An Alle` opening broadcasts remain one-way informational openings rather than strict sequential acknowledgement sequences.
- Some task labels remain narrower than the full operational richness of the radio order, but the revisions removed the validator-identified case where this caused a material gold-label traceability defect.
- Structural realism would benefit from another validation pass to confirm that the new closure-state messages are sufficient under the stricter framework.

## Summary of Improvement

- Structural closure was improved in scenarios that previously ended on unresolved active threads.
- The main gold-label traceability defect in `S3` was corrected.
- Protocol labeling in `S4` is now more internally consistent.
- Cross-scenario role semantics are more stable after the `S5` unit rename.
