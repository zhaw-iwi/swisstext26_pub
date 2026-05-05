# DATASET_REVISION_LOG

Dataset folder: `data/scenarios/synthetic_firefighter_radio_controlled_v1`

## Revision Summary

This revision pass applied targeted local fixes to improve compliance with both validation frameworks while preserving:

- the fixed JSON schema
- the closed-world predefined-task setup
- scenario diversity
- internal consistency
- realistic variability and controlled protocol noise

No full-scenario regenerations were required.

## Changed Files

- `s1.json`
- `s2.json`
- `s3.json`
- `s4.json`
- `s5.json`

## Issue-by-Issue Log

### `s1.json`

Fix type: `local`

Issues fixed:

- Reworked opening broadcast to a one-sided incident announcement without dangling `antworten`.
- Revised message `5` so the assignment matches the modeled task inventory and no longer introduces an unlabeled interior-attack obligation.
- Strengthened readback quality in message `6`.
- Added an explicit immediate acknowledgement from `Wassertrupp` after the directed order for water supply.
- Strengthened `Lueftungstrupp` acknowledgement by including the unit name directly in the message text.
- Removed the structurally open ending from the final ventilation status report.
- Updated completion evidence text for the unfinished ventilation task so it matches the revised message content exactly.

Validation impact:

- Improves protocol adherence, acknowledgement quality, and speaker-stripped transcript coherence.
- Removes the content-level mismatch between assignment content and the closed task inventory.

### `s2.json`

Fix type: `local`

Issues fixed:

- Reworked opening broadcast to a one-sided incident announcement without dangling `antworten`.
- Added a later explicit completion report from `Angriffstrupp` stating that overhaul is finished and no open hotspots remain.
- Updated `T2` completion evidence to use the new explicit completion message instead of the earlier work-in-progress report.

Validation impact:

- Resolves the critical over-optimistic gold labeling for `T2`.
- Keeps the garage fire scenario operationally realistic by separating "open fire out" from "extinguishment completed".

### `s3.json`

Fix type: `local`

Issues fixed:

- Reworked opening broadcast to a one-sided incident announcement without dangling `antworten`.
- Strengthened the reduced acknowledgement from `Sicherungstrupp` so it contains the assignment core and closure.
- Added one command-side coordination turn near the end to reduce the single-threaded finish and improve flow realism.
- Updated `T3` completion evidence to cite the explicit extinguishment report instead of the weaker later control-status message.

Validation impact:

- Improves communication-flow realism while preserving the scenario structure.
- Makes gold completion evidence for `T3` more directly traceable.

### `s4.json`

Fix type: `local`

Issues fixed:

- Reworked opening broadcast to a one-sided incident announcement without dangling `antworten`.
- Broadened `T1` task name so it matches the actual operational order: access closure plus safety-perimeter setup.
- Added a brief command-side coordination message after the cooling update to make the late-stage interaction less schematic.

Validation impact:

- Improves task/message coherence for the traffic-control assignment.
- Adds modest interleaving without changing the scenario's task set or hazard picture.

### `s5.json`

Fix type: `local`

Issues fixed:

- Reworked opening broadcast to a one-sided incident announcement without dangling `antworten`.

Validation impact:

- Removes the repeated dataset-level broadcast misuse pattern while preserving the scenario's otherwise strong structure.

## Remaining Limitations

- Some acknowledgements remain intentionally compressed to preserve realistic field-radio variability; the dataset is cleaner, but not uniformly formal.
- Broadcast openings now avoid the strongest protocol issue, but the dataset still models practical shorthand rather than strict textbook radio procedure in every turn.
- This pass did not rewrite the validation reports themselves; they should be rerun against the revised dataset.

## Regeneration Status

- Full-scenario regenerations: `none`
- Local revisions only: `s1.json`, `s2.json`, `s3.json`, `s4.json`, `s5.json`
