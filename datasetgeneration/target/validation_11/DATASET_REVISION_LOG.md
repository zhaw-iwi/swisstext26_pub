# DATASET_REVISION_LOG

Dataset folder: `data/scenarios/synthetic_firefighter_radio_controlled_v1`

## Changed files

- `s1.json`
- `s2.json`
- `s3.json`
- `s4.json`
- `s5.json`

## Revision details

### `s1.json`

- Fix type: local revision
- Issues fixed:
  - Reclassified message `17` from a plain report-style transmission to an explicit directed `Befehl`, matching its actual function.
  - Added acknowledgement in message `18` so the directed order is answered according to the structural framework.
  - Added message `19` to make the open entrainment/ventilation phase end on a natural operational framing instead of an abrupt cutoff.
  - Corrected `T1` `completion_outcome` so it exactly matches the underlying message text.

### `s2.json`

- Fix type: local revision
- Issues fixed:
  - Corrected message `5` `speaker` from `Wassertrupp` to `Einsatzleitung`.
  - Added missing closure marker to message `6`.
  - Reworked the `Messgruppe` sequence (`12` to `21`) so it reads as staged readiness, interleaved support, formal release, acknowledgement, first measurement, and command-level freeze of the area instead of a synthetic two-step marker chain.
  - Added missing closure marker to the first `Messgruppe` acknowledgement (`13`).
  - Introduced additional interleaving via the `Wassertrupp` status message in `15`.
  - Added explicit end framing in `21` so the still-open CO control phase ends naturally.
  - Tightened task wording for `T2` from only `abloeschen` to `lokalisieren und abloeschen`, aligning the predefined task with the actual assignment scope.
  - Corrected message `19` sender/receiver phrasing after the sequence rewrite.

### `s3.json`

- Fix type: local revision
- Issues fixed:
  - Corrected message `4` `speaker` from `Wassertrupp` to `Einsatzleitung`.
  - Narrowed `T3` wording to better match the tracked assignment/completion scope and reduce task bundling.

### `s4.json`

- Fix type: local revision
- Issues fixed:
  - Reclassified message `18` from `Meldung` to an explicit `Befehl`.
  - Added acknowledgement in message `19` so the directed traffic-control order is answered.
  - Shifted the late-scene sequence to preserve chronological clarity after the new acknowledgement.
  - Added message `24` to frame the unresolved gas-cylinder cooling task as an intentional ongoing phase rather than an abrupt transcript stop.

### `s5.json`

- Fix type: local revision
- Issues fixed:
  - Added missing closure marker to message `5`.
  - Reclassified message `21` from `Meldung` to `Anfrage`, matching its reply-seeking handover function.
  - Strengthened message `20` with one explicit adjacent-section control result (`Nachbartrennwand ohne Auffaelligkeit`) to improve closure realism.
  - Updated `T3` `completion_outcome` so it exactly matches the strengthened message `20`.

## Full-scenario regeneration

- None.
- All reported issues were repairable through local revisions while preserving scenario identity, task inventory style, and dataset diversity.

## Remaining limitations

- The dataset still remains somewhat more protocol-explicit and cleaner than a raw real-world radio transcript. That is deliberate to preserve label traceability.
- Open-task scenarios (`s1.json`, `s2.json`, `s4.json`) now end more naturally, but they still represent mid-incident slices rather than full incident closure.
- Some scenarios still favor highly legible command chains over heavily noisy or conflict-repair traffic. This preserves annotation reliability but may still appear slightly authored under a strict realism lens.

## Local validation performed after revision

- Parsed all revised JSON files successfully.
- Verified message IDs remain strictly increasing.
- Verified every `predefined_tasks.task_id` still maps one-to-one to `gold_task_states.task_id`.
- Verified every `completion_outcome` string appears verbatim in the corresponding scenario message list.
