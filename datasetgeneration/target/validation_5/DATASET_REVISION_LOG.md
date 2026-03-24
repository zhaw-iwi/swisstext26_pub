# DATASET_REVISION_LOG

Dataset folder: `data/scenarios/synthetic_firefighter_radio_controlled_v1`

## Changed files

- `s1.json`
- `s2.json`
- `s3.json`
- `s4.json`

## Fix log

### `s1.json`

- Fix type: local
- Issues fixed:
  - Clarified that the ventilation task remains in progress rather than looking like a weak completion statement.
  - Added acknowledgement wording variety with `korrekt`.
- Revision:
  - Updated the final ventilation report to state `Entrauchung noch nicht abgeschlossen`.
  - Aligned `gold_task_states.T3.completion_outcome` to that explicit non-completion evidence.

### `s2.json`

- Fix type: local
- Issues fixed:
  - Removed a non-task-related observation that could be over-read as rescue evidence.
  - Clarified that the CO follow-up task is still ongoing rather than ambiguously stored as a completion outcome.
- Revision:
  - Simplified message `14` by removing `keine Person aufgefunden`.
  - Updated message `17` to state `CO-Nachkontrolle noch nicht abgeschlossen`.
  - Aligned `gold_task_states.T3.completion_outcome` to that explicit progress/blocking message.

### `s3.json`

- Fix type: local
- Issues fixed:
  - Strengthened traceability for the extinguishment task by selecting the strongest direct completion evidence.
- Revision:
  - Updated `gold_task_states.T3.completion_outcome` from the later spread-control confirmation to the direct extinguishment message `Brand am Trockner abgeloescht`.

### `s4.json`

- Fix type: local
- Issues fixed:
  - Added explicit early on-scene assessment before major tactical commitments.
  - Made the gas-bottle hazard chain more explicit by confirming visibility and access before assigning cooling.
  - Reduced task-boundary blur in the later traffic-control thread.
  - Closed the last active communication loop more cleanly while keeping the cooling task incomplete.
  - Clarified the incomplete-task evidence in the gold labels.
- Revision:
  - Inserted an early reconnaissance report from `Angriffstrupp` after the initial incident broadcast.
  - Shifted subsequent message ids to preserve strict chronological order.
  - Reframed the later traffic-control communication as maintaining the existing perimeter instead of a new substantive task.
  - Updated the last cooling report to state `Abschluss noch nicht erreicht`.
  - Added an explicit command acknowledgement/continuation message from `Einsatzleitung` after the final cooling update.
  - Aligned `gold_task_states.T3.completion_outcome` to the explicit non-completion evidence.

## Full-scenario regenerations

- None. All fixes were handled locally to preserve scenario diversity and the existing closed-world task inventories.

## Remaining limitations

- The dataset still intentionally includes some cleaner-than-field protocol sequences; variability improved slightly, but the set remains more orderly than noisy real radio traffic.
- `completion_outcome` remains a fixed schema field, so incomplete tasks still store the strongest available progress or blocking evidence rather than a true completion statement.
- Multi-recipient ordered acknowledgement patterns remain lightly represented across the dataset.
