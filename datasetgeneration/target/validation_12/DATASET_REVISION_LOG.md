# DATASET_REVISION_LOG

## Scope

Revision target: `synthetic_firefighter_radio_controlled_v1`

Revision policy applied:

- Fixed minor and moderate issues locally where possible.
- No full-scenario regeneration was required.
- Preserved the fixed JSON schema, closed-world task setup, scenario diversity, and internal scenario logic.

## Changed Files

- `s1.json`
- `s2.json`
- `s3.json`
- `s4.json`
- `s5.json`

## Per-File Revision Notes

### `s1.json`

Fix type: local

Issues fixed:

- Added a small amount of controlled transcript-style variation by shortening two acknowledgement turns.
- Reduced over-polished closure usage without affecting task traceability or message interpretability.

What changed:

- Message `2`: removed closing formula to make the acknowledgement slightly less uniform.
- Message `15`: shortened acknowledgement style while preserving clear task-state progression.

### `s2.json`

Fix type: local

Issues fixed:

- Corrected semantically loose protocol labeling where directives had been framed as `Meldung`.
- Improved task granularity alignment for `T3` so the monitored task better matches the explicit measurement phase rather than the earlier standby phase.
- Added a small amount of surface realism variation by shortening one acknowledgement.

What changed:

- Message `12`: changed from `Meldung` to `Befehl` for the standby instruction to `Messgruppe`.
- Message `19`: changed from `Meldung` to `Befehl` for the directed area-control instruction.
- Message `13`: shortened acknowledgement style.
- `T3` task name revised from broad follow-up control wording to a more atomic first-measurement task.

### `s3.json`

Fix type: local

Issues fixed:

- Repaired the structural routing defect where one message implicitly instructed two units but directly addressed only one.
- Restored clean acknowledgement logic by giving the reserve order directly to `Wassertrupp`.
- Improved gold-state traceability for `T3` by aligning the combined task wording to the initial explicit assignment.

What changed:

- Message `7`: expanded the initial `Angriffstrupp` assignment so it explicitly includes both extinguishment and shaft control.
- Message `8`: updated readback to match the revised assignment.
- Message `12`: reassigned as a direct reserve order to `Wassertrupp`.
- Message `13`: converted into the corresponding `Wassertrupp` acknowledgement.

### `s4.json`

Fix type: local

Issues fixed:

- Replaced one synthetic-sounding closing broadcast phrase with more natural compressed radio wording.

What changed:

- Message `24`: changed `Einsatzstelle bleibt in laufender Phase` to `Einsatzstelle noch nicht frei`.

### `s5.json`

Fix type: local

Issues fixed:

- Improved `T2` traceability by moving the full monitored task into the first explicit assignment instead of splitting core task content across separate command turns.
- Reduced message-type looseness in the police handover exchange by making the final request an actual question.
- Kept realistic phased execution while making the gold label cleaner under the content-validation framework.

What changed:

- Message `9`: expanded the initial `Angriffstrupp` order so search and extinguishment are part of the same explicit assignment.
- Message `10`: updated readback to match the revised task wording.
- Message `13`: converted from a second core task order into a status-style follow-up requesting completion feedback after extinguishment.
- Message `21`: revised to a clearer handover question to `Polizei`.

## Full-Scenario Regeneration

- None.

Reason:

- All flagged issues were minor to moderate and could be corrected through targeted message/task revisions without replacing entire scenarios.

## Remaining Limitations

- The dataset is still intentionally more controlled than a raw transcript corpus. It now includes slightly more protocol variation, but it is not meant to model heavy noise.
- Some scenarios remain fairly serialized in their command-response rhythm. This was preserved to avoid damaging label reliability.
- Incomplete tasks still use the fixed `completion_outcome` field as state evidence because the schema is fixed.
- End-phase demobilization remains selective rather than universal across the dataset, which is acceptable for clipped scenario scope but still narrower than full incident closure modeling.

## Summary Of Improvements

- Structural routing is now clean in `S3`.
- Task-to-assignment traceability is improved in `S2`, `S3`, and `S5`.
- Semantically loose message-type labels were tightened where they affected validation.
- The dataset now shows slightly more transcript-style variability without losing clarity or schema stability.
