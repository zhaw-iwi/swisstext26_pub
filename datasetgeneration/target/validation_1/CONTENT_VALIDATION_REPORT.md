# Content Validation Report

Dataset: `synthetic_firefighter_radio_controlled_v1`  
Scope: operational plausibility and task-content validity only. Communication protocol structure was not evaluated.

Binary judgment rule used for this report:
- `PASS`: scenario receives overall rubric verdict `PASS`
- `FAIL`: scenario receives overall rubric verdict `PARTIAL` or `FAIL`

## Per-Scenario Assessment

### S1 - Kuechenbrand Mehrfamilienhaus

Criterion ratings:

| Criterion | Rating | Justification |
| --- | --- | --- |
| Task Realism | PARTIAL | `T2` is modeled as only person search, but message `5` assigns a combined order: person search and first interior attack. The interior attack is a major operational task but is absent from `predefined_tasks` and `gold_task_states`. |
| Scenario Plausibility | PASS | Incident progression is plausible: initial alarm (`1`), arrival/report (`4`), tasking (`5`, `7`, `8`), supply setup (`10`), search result (`11`), delayed ventilation release (`12`-`14`). |
| Role and Assignment Correctness | PASS | Einsatzleitung assigns; Angriffstrupp searches/attacks; Wassertrupp establishes supply; Lueftungstrupp ventilates. These align with role capability. |
| Task Sequencing and Dependencies | PASS | Ventilation is explicitly held until attack crew release in `8`, then started only after the search/update in `11` via `12`. |
| Completion Signal Validity | PASS | `T1` completion is observable in `10`; `T2` completion is supported by `11`; `T3` is correctly left incomplete because `14` still reports smoke on the fire floor. |
| Traceability of Gold Task States | PARTIAL | `T1` and `T2` are traceable, but the scenario contains an additional assigned operational task in `5` (interior attack) that is not traceable through the task schema at all. |
| Consistency Across Scenario | PARTIAL | Messages describe a larger task set than the task model captures. This creates a coherence gap between `messages` and `predefined_tasks`/`gold_task_states`. |

Issues:

- Moderate: `T2` under-models the actual assignment in message `5`. `m5` gives Angriffstrupp both person search and interior attack, but only the search task exists in the labeled task inventory.
- Moderate: Because the interior attack from `m5` is missing from the task inventory, the scenario is not fully coherent across `messages`, `predefined_tasks`, and `gold_task_states`.

Rubric verdict: `PARTIAL`  
Binary judgment: `FAIL`

### S2 - Tiefgaragenbrand Wohnblock

Criterion ratings:

| Criterion | Rating | Justification |
| --- | --- | --- |
| Task Realism | PASS | Isolation, suppression, and CO follow-up are all realistic task families for a garage fire. |
| Scenario Plausibility | PASS | Progression is plausible: smoke conditions (`1`-`2`), hazard control (`3`, `7`), attack order (`4`-`5`), location confirmation and active suppression (`8`), post-fire measurement (`9`-`13`). |
| Role and Assignment Correctness | PASS | Sicherheitstrupp handles isolation, Angriffstrupp suppression, Messgruppe gas measurement. |
| Task Sequencing and Dependencies | PASS | Measuring is correctly delayed until release in `9` and partially enabled in `12` after the fire report in `11`. |
| Completion Signal Validity | FAIL | `T2` is marked completed, but the cited evidence in `11` says only "offenes Feuer ... aus" while "Nachloescharbeiten laufen". That is not a strong completion signal for a task named "Brandherd ... abloeschen". |
| Traceability of Gold Task States | FAIL | `gold_task_states` for `T2` overclaims completion. Message `11` supports progress and partial success, not clean task completion. |
| Consistency Across Scenario | PARTIAL | The labeled state says `T2` completed, while the message evidence still describes continuing suppression work. |

Issues:

- Critical: `T2` is mislabeled as completed. Message `11` explicitly says overhaul is still ongoing. The task state should not be `completed: true` on that evidence.
- Moderate: `T3` is well-modeled as incomplete, but this makes the over-optimistic completion of `T2` stand out even more because the scene is still unsafe in `13` (`60 ppm CO`, "Tiefgarage nicht frei").

Rubric verdict: `PARTIAL`  
Binary judgment: `FAIL`

### S3 - Kellerbrand Schulhaus

Criterion ratings:

| Criterion | Rating | Justification |
| --- | --- | --- |
| Task Realism | PASS | Access control, hose lay, and cellar fire attack are realistic and actionable. |
| Scenario Plausibility | PASS | Alarm (`1`), scene control (`2`, `6`), water supply (`3`, `9`), reconnaissance/attack (`7`, `10`), extinguishment/control checks (`11`, `12`) form a plausible sequence. |
| Role and Assignment Correctness | PASS | Sicherungstrupp, Wassertrupp, and Angriffstrupp each stay within plausible functional roles. |
| Task Sequencing and Dependencies | PASS | Access control and water supply are established before the interior attack develops. The attack crew then reports fire location and containment before final control. |
| Completion Signal Validity | PARTIAL | The scenario contains enough evidence for `T3` completion across `11` and `12`, but the cited `completion_outcome` in gold uses only `12`, which says "unter Kontrolle" rather than explicitly "abgeloescht". |
| Traceability of Gold Task States | PARTIAL | `T1` and `T2` are clean. `T3` is only fully supported if `11` and `12` are read together; the single quoted gold outcome is weaker than the actual evidentiary chain. |
| Consistency Across Scenario | PASS | Operational picture is coherent and no contradictions appear. |

Issues:

- Minor: `T3` completion evidence is slightly under-specified. Message `12` alone is weaker than message `11` plus `12` together for proving the extinguishment task is complete.

Rubric verdict: `PASS`  
Binary judgment: `PASS`

### S4 - Werkstattbrand mit Gasflaschen

Criterion ratings:

| Criterion | Rating | Justification |
| --- | --- | --- |
| Task Realism | PASS | Traffic control, foam attack, and covered cooling of gas cylinders are realistic tasks for this hazard picture. |
| Scenario Plausibility | PASS | The scenario reflects hazard recognition (`1`), zone control (`2`, `8`), suppression (`4`, `9`), and continuing cooling due to residual heat (`6`, `10`). |
| Role and Assignment Correctness | PASS | Verkehrstrupp handles perimeter/access, Angriffstrupp suppresses the fire, Wassertrupp cools cylinders. |
| Task Sequencing and Dependencies | PASS | Safety perimeter is established before later broad traffic restriction in `11`; gas-cylinder cooling remains active while the fire is already down, which is operationally plausible. |
| Completion Signal Validity | PASS | `T1` has clear physical completion in `8`; `T2` has good evidence in `9`; `T3` is correctly left incomplete because `10` reports one cylinder still warm. |
| Traceability of Gold Task States | PARTIAL | `T1` is traceable, but the actual order in `2` includes both road closure and a 50 m safety area. The task schema only preserves the closure half of the assignment. |
| Consistency Across Scenario | PARTIAL | The task model again compresses a materially broader order into a narrower task label, reducing coherence between assignment content and labeled task set. |

Issues:

- Moderate: `T1` is narrower than the assignment in message `2`. The safety perimeter is operationally significant but is not represented as its own task or in the `T1` task name.

Rubric verdict: `PASS`  
Binary judgment: `PASS`

### S5 - Dachstockbrand Reihenhaus

Criterion ratings:

| Criterion | Rating | Justification |
| --- | --- | --- |
| Task Realism | PASS | Ladder readiness, opening the roof area, extinguishing embers, and final thermal control are all realistic for a concealed roof-space fire. |
| Scenario Plausibility | PASS | The scenario progresses plausibly from exterior smoke report (`1`, `3`) to access setup (`4`, `8`), opening/search (`6`, `9`), extinguishment (`12`), control check (`10`, `13`), and handover readiness (`14`). |
| Role and Assignment Correctness | PASS | Drehleiter supports access and lighting, Angriffstrupp opens and extinguishes, Sicherungstrupp performs the final check after release. |
| Task Sequencing and Dependencies | PASS | Final control is explicitly delayed until attack completion in `10`-`13`, and handover readiness follows only after that control check in `14`. |
| Completion Signal Validity | PASS | Each task has direct observable completion evidence: `8`, `12`, `13`. |
| Traceability of Gold Task States | PASS | All three task states are directly supported by the cited messages. |
| Consistency Across Scenario | PASS | Messages, task list, and gold labels are coherent. |

Issues:

- None material.

Rubric verdict: `PASS`  
Binary judgment: `PASS`

## Dataset-Level Assessment

### Cross-Dataset Patterns

Critical patterns:

- Gold completion labeling is too optimistic in some scenarios. The clearest case is `S2/T2`, where `m11` still reports ongoing overhaul but the gold state is `completed: true`.

Moderate patterns:

- Several scenarios compress multi-part operational orders into a narrower task inventory. This appears in `S1/m5` (`T2` captures person search but not the simultaneous interior attack) and `S4/m2` (`T1` captures road closure but not the 50 m safety perimeter).
- The dataset tends to model only the "headline" task from a radio order, even when the message contains two distinct operationally relevant obligations.

Minor patterns:

- Some `completion_outcome` fields point to a weaker single message than the full evidentiary chain available in the scenario. `S3/T3` is the clearest example.

### Overall Judgment

Rubric-level overall verdict: `PARTIAL`  
Binary overall judgment: `FAIL`

Reason:
- The dataset contains one critical gold-labeling error (`S2/T2`).
- It also shows repeated coherence loss between operational messages and the task schema in multiple scenarios (`S1`, `S4`).
- Two scenarios are clean enough to pass (`S3`, `S5`), but the dataset is not yet reliable enough for content-valid evaluation use without revision.

## Concrete Revision List

Apply these revisions in a follow-up fix pass:

1. `S2/T2`: change `completed` to `false` unless a new message is added that explicitly reports extinguishment completed rather than only "open flames out" with overhaul still running.
2. `S2/T2`: if kept as completed, add a later message from `Angriffstrupp` with explicit completion evidence such as completed extinguishment and no remaining fire spread risk.
3. `S1`: split the combined assignment in `m5` into two labeled tasks, or revise the task inventory so the interior attack component is represented in `predefined_tasks` and `gold_task_states`.
4. `S1`: if the task inventory intentionally stays minimal, rewrite `m5` so it only assigns the single modeled task (`T2`) and move interior attack wording out of the assignment.
5. `S4`: either broaden `T1` to include both access closure and safety perimeter establishment, or add a separate task for the 50 m exclusion zone from `m2`.
6. `S3/T3`: strengthen `completion_outcome` by citing the message with explicit extinguishment (`m11`) or by using wording that reflects the combined evidence from `m11` and `m12`.
7. Run a consistency sweep across all scenarios for this rule: every distinct operational obligation in an order should either exist as a task or be intentionally removed from the message.
8. Run a second consistency sweep for this rule: `completed: true` must require explicit observable completion evidence, not only partial success, work-in-progress, or "under control" wording.
