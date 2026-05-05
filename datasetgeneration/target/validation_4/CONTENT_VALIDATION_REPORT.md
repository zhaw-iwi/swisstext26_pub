# Content Validation Report

Dataset: `data/scenarios/synthetic_firefighter_radio_controlled_v1`
Scope: operational plausibility and task-content validity only
Grounding: `./.agents/datasetgeneration/dataset_validation_content.md`, `./.agents/datasetgeneration/source_notes_einsatzfuehrung.md`, `./.agents/datasetgeneration/source_notes_real_transcript.md`

## Per-Scenario Assessment

### S1 - Kuechenbrand Mehrfamilienhaus

**Criteria**

| Criterion | Rating | Justification |
| --- | --- | --- |
| Task Realism | PASS | `T1` water supply, `T2` person search, and `T3` smoke control are all valid fireground task families and are communicable and observable in messages `7-16`. |
| Scenario Plausibility | PASS | The sequence follows alarm (`1`) -> arrival/assessment (`4`) -> tasking (`5,7,9`) -> execution (`11-16`). Smoke conditions and phased ventilation are operationally coherent. |
| Role and Assignment Correctness | PASS | Einsatzleitung assigns tasks; `Angriffstrupp`, `Wassertrupp`, and `Lueftungstrupp` execute within plausible roles (`5,7,9`). |
| Task Sequencing and Dependencies | PASS | Rescue/search is prioritized before ventilation (`5` before `14`), and ventilation is explicitly delayed until release by interior operations (`9`). |
| Completion Signal Validity | PASS | `T1` is evidenced by water supply standing (`11`), `T2` by search result (`12`), and `T3` is correctly left incomplete because `16` reports only partial smoke improvement. |
| Traceability of Gold Task States | PASS | All gold labels map cleanly to the cited messages. `T3` correctly remains `completed=false`. |
| Consistency Across Scenario | PASS | No contradiction between messages, tasks, or gold states. |

**Issues**

- Critical issues: none.
- Moderate issues: none.
- Minor issues:
  - `message 13` reports fire knockdown while the predefined task set has no explicit suppression task. This does not break the three labeled tasks, but it means the operational picture is slightly broader than the gold task inventory.

**Overall verdict:** PASS

**Pass/fail judgment:** PASS

---

### S2 - Tiefgaragenbrand Wohnblock

**Criteria**

| Criterion | Rating | Justification |
| --- | --- | --- |
| Task Realism | PASS | Power isolation (`T1`), suppression (`T2`), and CO follow-up measurement (`T3`) are valid task families. |
| Scenario Plausibility | PARTIAL | The incident evolves plausibly overall, but deep garage suppression is ordered immediately in heavy smoke (`1-4`) without any explicit water supply, attack-path preparation, or staging step. |
| Role and Assignment Correctness | PASS | Tasks are assigned by command to plausible roles: `Sicherheitstrupp` (`3`), `Angriffstrupp` (`4`), `Messgruppe` (`9,12`). |
| Task Sequencing and Dependencies | FAIL | `message 4` orders interior suppression with a `C-Rohr` before any message establishes water availability or access feasibility, despite the source note dependency that suppression depends on access and water. |
| Completion Signal Validity | PASS | `T1` completion is observable in `7`; `T2` completion is evidenced by `15`; `T3` is correctly incomplete because `14` reports `60 ppm CO` and `Tiefgarage nicht frei`. |
| Traceability of Gold Task States | PASS | Gold states are traceable to messages and assigned units. |
| Consistency Across Scenario | PARTIAL | `message 8` reports an adjacent vehicle is heat-exposed, but no containment/protection task or follow-up appears afterward. The scenario stays interpretable, but the tactical picture is under-resolved. |

**Issues**

- Critical issues:
  - `T2`, `message 4`: suppression is ordered in a smoke-filled underground environment before any explicit water/access readiness is established. This violates the source-note dependency that suppression must depend on feasible access and water.
- Moderate issues:
  - `message 8`: the attack crew reports `ein Fahrzeug daneben waermebeaufschlagt`, but no follow-up task or command decision addresses exposure protection. This weakens containment logic after new information.
- Minor issues:
  - `message 2` only reports `keine Personen sichtbar`; there is no explicit reassessment of whether additional search beyond the attack path is required. This is acceptable compression, but it leaves rescue logic thin for a garage occupancy environment.

**Overall verdict:** PARTIAL

**Pass/fail judgment:** FAIL

---

### S3 - Kellerbrand Schulhaus

**Criteria**

| Criterion | Rating | Justification |
| --- | --- | --- |
| Task Realism | PASS | Access control (`T1`), water supply (`T2`), and basement fire attack (`T3`) are operationally valid and observable. |
| Scenario Plausibility | PASS | The sequence is coherent: incident report (`1`), safety/access control (`2`), water supply (`3`), attack assignment (`7`), local findings (`10`), extinguishment and spread check (`11-13`). |
| Role and Assignment Correctness | PASS | `Sicherungstrupp`, `Wassertrupp`, and `Angriffstrupp` receive role-appropriate tasks. |
| Task Sequencing and Dependencies | PASS | Access control and hose line are established before interior extinguishment (`2-4`, `9` before `10-13`). The closed door to the adjacent room in `10` also supports containment logic. |
| Completion Signal Validity | PASS | `T1` and `T2` have direct effect-based completion signals (`6`, `9`). `T3` completion is valid only after the shaft check result in `13`, which the gold label correctly uses. |
| Traceability of Gold Task States | PASS | Gold assignments and completions are fully supported by messages. |
| Consistency Across Scenario | PASS | The scenario maintains one coherent tactical picture with no contradictory states. |

**Issues**

- Critical issues: none.
- Moderate issues: none.
- Minor issues:
  - `message 1` states the school wing is evacuated, but there is no later control message confirming no remaining persons in the building. This is not required by the labeled tasks, but it slightly reduces closure completeness.

**Overall verdict:** PASS

**Pass/fail judgment:** PASS

---

### S4 - Werkstattbrand mit Gasflaschen

**Criteria**

| Criterion | Rating | Justification |
| --- | --- | --- |
| Task Realism | PASS | Traffic control (`T1`), foam attack on a workbench fire (`T2`), and cooling gas cylinders (`T3`) are all valid fireground tasks. |
| Scenario Plausibility | PASS | The scenario reflects realistic uncertainty around gas cylinders and narrow access, then splits work into hazard-zone control, suppression, and cooling (`1-14`). |
| Role and Assignment Correctness | PASS | `Verkehrstrupp`, `Angriffstrupp`, and `Wassertrupp` are used in plausible functional roles (`2,4,6`). |
| Task Sequencing and Dependencies | PASS | Scene organization and exclusion zone are established early (`2-3`, `8`), suppression and cylinder cooling run in parallel, and command keeps cooling active after the fire is largely controlled (`11-12`). |
| Completion Signal Validity | PASS | `T1` is completed by `8`; `T2` is completed by `14`; `T3` is correctly incomplete because `10` states one cylinder is still warm and `11-12` continue the task. |
| Traceability of Gold Task States | PASS | Gold task states are supported by the cited messages. |
| Consistency Across Scenario | PASS | No contradiction between tasking, updates, and incompletion of cylinder cooling. |

**Issues**

- Critical issues: none.
- Moderate issues: none.
- Minor issues:
  - `message 13` gives a broadcast traffic restriction to `Alle` even though `Verkehrstrupp` already owns access control. This does not break the scenario, but a direct role-targeted update would improve responsibility traceability.

**Overall verdict:** PASS

**Pass/fail judgment:** PASS

---

### S5 - Dachstockbrand Reihenhaus

**Criteria**

| Criterion | Rating | Justification |
| --- | --- | --- |
| Task Realism | PASS | Ladder standby (`T1`), ember search/extinguishment (`T2`), and final thermal check (`T3`) are valid tasks for a localized roof-space fire. |
| Scenario Plausibility | PASS | The sequence is coherent: initial roof smoke report (`1,3`), ladder setup (`4-5,8`), roof-space opening and control (`6-7,9,12`), final check (`10-13`), then handover (`14-15`). |
| Role and Assignment Correctness | PASS | `Drehleiter` supports access/readiness, `Angriffstrupp` handles opening/extinguishment, and `Sicherungstrupp` performs the final control check as explicitly assigned. |
| Task Sequencing and Dependencies | PASS | Final control is explicitly delayed until attack completion (`10-13`), and handover only occurs after the negative final check (`14`). |
| Completion Signal Validity | PASS | `T1`, `T2`, and `T3` each have direct operational evidence in `8`, `12`, and `13`. |
| Traceability of Gold Task States | PASS | Gold labels map directly to the messages. |
| Consistency Across Scenario | PASS | The task picture remains coherent through handover. |

**Issues**

- Critical issues: none.
- Moderate issues: none.
- Minor issues:
  - `message 6` combines opening, search, extinguishment, and thermal-camera use into one assignment to one unit. It is still interpretable, but it is denser than the source-note preference for one task at a time per recipient.

**Overall verdict:** PASS

**Pass/fail judgment:** PASS

## Dataset-Level Assessment

### Overall result

- Scenario verdicts:
  - `S1`: PASS
  - `S2`: PARTIAL
  - `S3`: PASS
  - `S4`: PASS
  - `S5`: PASS
- Dataset overall verdict: PARTIAL
- Dataset overall pass/fail judgment: FAIL

### Cross-dataset strengths

- Most scenarios follow the expected fireground progression from initial report to tasking and operational feedback.
- Task families are well chosen and mostly grounded in the source-note domains: safety, rescue/search, suppression, ventilation, traffic control, logistics, and final checks.
- Gold task states are generally traceable and usually use valid effect-based completion evidence rather than empty acknowledgements.

### Cross-dataset patterns needing correction

- Prerequisite steps before suppression are sometimes under-specified.
  - Most visible in `S2`, where interior garage suppression is ordered without explicit water/access readiness.
- Follow-up decisions after new hazard information are sometimes missing.
  - `S2`, `message 8` introduces an exposed adjacent vehicle without any containment task or command update.
- Some scenarios include operationally relevant actions outside the predefined task inventory.
  - `S1` includes actual fire knockdown in `message 13`, but suppression is not represented as a predefined task.
- Handover and demobilization logic is sparse across the set.
  - Only `S5` reaches explicit handover; the others stop earlier, which is acceptable for partial snapshots but reduces full-incident completeness.
- Incomplete tasks still populate `completion_outcome`.
  - This is traceable in `S1`, `S2`, and `S4`, but the field name is semantically awkward when `completed=false` because the text is really an in-progress outcome, not a completion.

## Concrete Revision List

1. Revise `S2` so `T2` has an explicit prerequisite step before `message 4`.
   - Add a water/access readiness message or task before ordering interior suppression.
   - The added evidence should show feasible attack path and water availability.
2. Revise `S2` after `message 8` to address the heat-exposed adjacent vehicle.
   - Add either a containment/protection assignment or a command decision explaining why no further action is needed.
3. Decide whether `S1` should remain a task-focused subset or a fuller incident model.
   - If fuller, add a predefined suppression task aligned to `message 13`.
   - If task-focused, remove or soften `message 13` so the unlabeled suppression action does not overshadow the selected task set.
4. Review all scenarios with `completed=false` tasks (`S1:T3`, `S2:T3`, `S4:T3`).
   - Keep the evidence message, but consider renaming or documenting `completion_outcome` usage so downstream validators do not read it as completed-state evidence.
5. Where one order bundles multiple actions into a single assignment, split if the task boundary matters for labeling.
   - Highest-value cleanup candidate: `S5`, `message 6`.

## Final Judgment

The dataset is close to operationally plausible overall, but it does **not** fully pass strict content validation because `S2` contains a dependency violation in the suppression sequence and an under-resolved tactical development after a new exposure report.
