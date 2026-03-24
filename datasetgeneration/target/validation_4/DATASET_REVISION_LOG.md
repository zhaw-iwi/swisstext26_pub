# DATASET_REVISION_LOG

Dataset folder: `data/scenarios/synthetic_firefighter_radio_controlled_v1`

## Changed files

- `s1.json`
- `s2.json`
- `s4.json`
- `s5.json`

## Revision summary by file

### `s1.json`

- Revision type: local fix
- Issues fixed:
  - Removed an unresolved `antworten` control loop from message 13.
  - Softened the unlabeled suppression update in message 13 so it no longer reads like a fully completed extra task outside the monitored task inventory.
- Result:
  - Structural protocol symmetry improved.
  - The scenario remains a task-focused subset without changing the predefined task list.

### `s2.json`

- Revision type: local fix
- Issues fixed:
  - Added explicit prerequisite water/access readiness before interior suppression is assigned.
  - Added a concrete water-supply readiness report before the attack order.
  - Resolved the exposed adjacent-vehicle issue by adding shielding/containment information in attack progress reports.
  - Kept the deferred CO measurement task explicit with later release/start messages.
- Result:
  - Task sequencing now better reflects operational dependencies from the content framework.
  - The tactical picture is more complete without changing the monitored task inventory.

### `s4.json`

- Revision type: local fix
- Issues fixed:
  - Restored command-response symmetry by adding `antworten` to the renewed cooling order.
  - Replaced a broad broadcast traffic restriction with a role-targeted order to `Verkehrstrupp`.
  - Added a later cooling progress update so the still-open gas-cylinder thread has explicit closure state before scenario end.
- Result:
  - Structural traceability improved.
  - The incomplete cooling task remains incomplete, but now ends on a clearer in-progress status.

### `s5.json`

- Revision type: local fix
- Issues fixed:
  - Split the dense attack assignment into a reconnaissance/search step and a later explicit extinguishment order.
  - Added an explicit release/start command before the final-check completion report.
  - Tightened the handoff between `Angriffstrupp` completion and `Sicherungstrupp` final control.
- Result:
  - The task sequence is cleaner under both structure and content validation.
  - Assignment and completion evidence are more explicit in flattened transcript views.

## Unchanged files

- `s3.json`
  - No revision was needed. The scenario already aligned well with both validation reports.

## Remaining limitations

- The dataset still contains some unlabeled but operationally plausible side actions outside the predefined monitored task inventory. This is intentional and preserves the closed-world task setup without turning the scenarios into toy examples.
- Scenarios with `completed=false` still use the fixed `completion_outcome` field for the best available status evidence. This is a schema-level limitation, not a scenario inconsistency.
- Broadcast discipline is somewhat varied across scenarios by design to preserve realism; however, the most obvious unresolved response and release gaps identified by validation have been repaired.

## Verification notes

- All five JSON files were parsed successfully after revision.
- Top-level schema shape, unique increasing message IDs, and one-to-one task/gold-state mapping were checked.

## Overall assessment

- All revisions were local. No full-scenario regeneration was necessary.
- The dataset now has better protocol closure, clearer task-release transitions, and stronger operational dependency handling while preserving diversity and internal consistency.
