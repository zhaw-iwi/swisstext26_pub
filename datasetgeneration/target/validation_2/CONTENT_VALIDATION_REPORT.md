# Content Validation Report

Dataset: `data/scenarios/synthetic_firefighter_radio_controlled_v1`

Scope: operational plausibility and task-content validity only. Protocol/format validation was not assessed here.

Grounding sources:
- `./.agents/datasetgeneration/dataset_validation_content.md`
- `./.agents/datasetgeneration/source_notes_einsatzfuehrung.md`
- `./.agents/datasetgeneration/source_notes_real_transcript.md`

## Scenario S1: Kuechenbrand Mehrfamilienhaus

### Criteria
| Criterion | Rating | Notes |
|---|---|---|
| Task Realism | PASS | `T1` water supply, `T2` search, and `T3` smoke control are all valid radio-task families. |
| Scenario Plausibility | PASS | Progression is plausible: alarm (`m1`) -> arrival/assessment (`m4`) -> tasking (`m5`, `m7`, `m9`) -> execution/progress (`m11`, `m12`, `m15`). |
| Role and Assignment Correctness | PASS | Einsatzleitung assigns; Angriffstrupp, Wassertrupp, and Lueftungstrupp act within plausible capability. |
| Task Sequencing and Dependencies | PASS | Search precedes ventilation release; ventilation is explicitly held until attack/search feedback (`m9`, `m13`). |
| Completion Signal Validity | PASS | `T1` is completed by observable effect in `m11`; `T2` by search result in `m12`; `T3` correctly remains incomplete based on `m15`. |
| Traceability of Gold Task States | PASS | All three gold states are supported by clear messages. |
| Consistency Across Scenario | PARTIAL | The operational picture includes an active kitchen fire (`m4`, `m12`), but no suppression task exists in `predefined_tasks`. The task layer captures support actions but omits the main fire attack thread. |

### Issues
- Moderate: Missing core suppression task. Messages `m4` and `m12` establish a real fire problem, but there is no predefined task or gold state for extinguishment/containment. This weakens coherence between `messages` and the task layer.

### Verdict
- Overall verdict: PASS
- Pass/fail gate: PASS

## Scenario S2: Tiefgaragenbrand Wohnblock

### Criteria
| Criterion | Rating | Notes |
|---|---|---|
| Task Realism | PASS | Electrical isolation, suppression, and CO measurement are all realistic radio tasks. |
| Scenario Plausibility | PASS | Incident develops plausibly from smoke report (`m1`) to safety setup (`m3`, `m7`), fire attack (`m4`, `m8`, `m11`, `m14`), then atmospheric follow-up (`m9`, `m13`). |
| Role and Assignment Correctness | PASS | Safety, attack, and measurement tasks are assigned to functionally plausible units. |
| Task Sequencing and Dependencies | PASS | Safety control is initiated before interior progress is reported; CO measurement waits for release and still reports the area not free (`m9`, `m12`, `m13`). |
| Completion Signal Validity | PASS | `T1` and `T2` have observable completion evidence; `T3` is correctly incomplete because `m13` reports residual hazard. |
| Traceability of Gold Task States | PARTIAL | `T3` is named as a full "CO-Nachkontrolle Tiefgarage", but the actual order and evidence are limited to Vorraum and Rampe (`m9`, `m12`, `m13`). The gold state is directionally correct but broader than the message evidence. |
| Consistency Across Scenario | PASS | No internal contradictions in assignment or completion. |

### Issues
- Moderate: Scope mismatch on `T3`. The task name says "CO-Nachkontrolle Tiefgarage", but the actual operational scope is "im Vorraum und in der Rampe" in `m9`, confirmed by measurement in `m13`.

### Verdict
- Overall verdict: PASS
- Pass/fail gate: PASS

## Scenario S3: Kellerbrand Schulhaus

### Criteria
| Criterion | Rating | Notes |
|---|---|---|
| Task Realism | PASS | Access control, hose line setup, and basement fire attack are realistic. |
| Scenario Plausibility | PASS | Alarm -> access control/water setup (`m2`-`m6`) -> fire attack (`m7`-`m10`) -> control check (`m11`-`m13`) is coherent. |
| Role and Assignment Correctness | PASS | Units operate within plausible responsibilities. |
| Task Sequencing and Dependencies | PASS | Water supply is established before interior attack progress is reported (`m9` before `m10`). Control of possible spread follows extinguishment (`m11`-`m13`). |
| Completion Signal Validity | PARTIAL | `T3` is marked complete using `m11`, but that message still says "Kontrolle im Installationsschacht laeuft noch". Stronger completion evidence exists later in `m13`. |
| Traceability of Gold Task States | PARTIAL | The assignment for `T3` is clear, but the selected `completion_outcome` is premature. `m13` better supports final completion than `m11`. |
| Consistency Across Scenario | PASS | Scenario logic remains coherent despite the premature gold completion pointer. |

### Issues
- Moderate: `T3` completion evidence is weakly chosen. `m11` shows the seat of fire extinguished, but also states an unresolved follow-up check. If `T3` is intended as full completion of "Brandraum Keller West abloeschen", `m13` is the safer gold evidence.

### Verdict
- Overall verdict: PASS
- Pass/fail gate: PASS

## Scenario S4: Werkstattbrand mit Gasflaschen

### Criteria
| Criterion | Rating | Notes |
|---|---|---|
| Task Realism | PASS | Perimeter control, foam attack, and protected cooling of gas cylinders are realistic task families. |
| Scenario Plausibility | PASS | Initial hazard report (`m1`) leads to scene organization (`m2`, `m8`), suppression (`m4`, `m9`), and hazard cooling (`m6`, `m10`, `m11`). |
| Role and Assignment Correctness | PASS | Traffic, attack, and cooling roles are plausible. |
| Task Sequencing and Dependencies | PASS | Safety perimeter is established early; cooling and suppression run in parallel, which is justified by the dual hazard. |
| Completion Signal Validity | FAIL | `T2` is marked complete, but the cited evidence `m9` still says "Nachschaeumen laeuft". That is ongoing work, not a clean completion signal. |
| Traceability of Gold Task States | FAIL | `gold_task_states.T2.completed=true` is not fully supported by `m9`. The message supports major progress, not finished suppression. |
| Consistency Across Scenario | PARTIAL | The gold label for `T2` says complete while the scenario text keeps suppression activity active. |

### Issues
- Critical: `T2` is mislabeled as completed. Message `m9` explicitly says follow-up foam application is still ongoing, so the task "Werkbankbrand mit Schaum abloeschen" should not be closed there.
- Moderate: The scenario ends with `T3` still active (`m10`, `m11`) and no later control message. That is acceptable for an incomplete task, but it leaves the scenario without a stabilization checkpoint.

### Verdict
- Overall verdict: PARTIAL
- Pass/fail gate: FAIL

## Scenario S5: Dachstockbrand Reihenhaus

### Criteria
| Criterion | Rating | Notes |
|---|---|---|
| Task Realism | PASS | Ladder readiness, opening/searching for hotspots, and final thermal check are realistic. |
| Scenario Plausibility | PASS | Alarm (`m1`) -> positioning (`m2`, `m3`) -> ladder task and attack task (`m4`-`m7`) -> progress (`m8`, `m9`) -> final check (`m10`-`m13`) -> handover readiness (`m14`). |
| Role and Assignment Correctness | PASS | All units act within plausible roles as represented by the source notes. |
| Task Sequencing and Dependencies | PASS | Final control is explicitly delayed until attack completion (`m10`, `m11`), and handover follows the negative final check (`m13`, `m14`). |
| Completion Signal Validity | PASS | `T1`, `T2`, and `T3` all have concrete, observable completion evidence. |
| Traceability of Gold Task States | PASS | All gold labels are directly traceable to messages. |
| Consistency Across Scenario | PASS | Operational picture, tasks, and gold states align well. |

### Issues
- Minor: `m4` assigns both anleiterbereitschaft and lighting, while `T1` only tracks the ladder-readiness portion. This simplification does not break validity but slightly compresses the task scope.

### Verdict
- Overall verdict: PASS
- Pass/fail gate: PASS

## Dataset-Level Assessment

### Strengths
- Incident evolution is generally realistic and incremental.
- Role-task alignment is consistently strong.
- Most incomplete tasks are correctly left incomplete rather than falsely closed.
- Radio phrasing stays operational and task-oriented without needing strict protocol regularity.

### Cross-Dataset Issues
- Moderate: Task-layer compression sometimes drops a tactically central thread. Most visible in `S1`, where a real kitchen fire is described in messages but no explicit suppression task exists in `predefined_tasks`.
- Moderate: Gold completion evidence sometimes points to progress messages instead of terminal completion messages. This occurs in `S3/T3` and critically in `S4/T2`.
- Moderate: Some task names are broader than the actual assigned/evidenced scope, especially `S2/T3` ("Tiefgarage") versus the concrete message scope ("Vorraum und Rampe").

### Scenario Gates
| Scenario | Verdict | Pass/Fail Gate |
|---|---|---|
| S1 | PASS | PASS |
| S2 | PASS | PASS |
| S3 | PASS | PASS |
| S4 | PARTIAL | FAIL |
| S5 | PASS | PASS |

### Overall Judgment
- Overall dataset verdict: PARTIAL
- Overall pass/fail gate: FAIL

Reason: the dataset is mostly operationally plausible, but `S4` contains a content-labeling error in `gold_task_states` severe enough to fail independent validation. Additional moderate task-layer abstraction issues appear in `S1`, `S2`, and `S3`.

## Concrete Revision List

1. `S4/T2`: change `completed` from `true` to `false`, or add a later message that explicitly closes the foam attack with observable evidence and then keep `completed=true`.
2. `S4/T2`: if keeping the task complete, replace the current `completion_outcome` (`m9`) with a later message that states finished suppression rather than ongoing "Nachschaeumen laeuft".
3. `S3/T3`: keep the task complete if desired, but change the `completion_outcome` reference from the message equivalent of `m11` to the stronger final control message equivalent of `m13`.
4. `S2/T3`: either narrow the task name to match the actual assignment ("CO-Nachkontrolle Vorraum und Rampe") or expand the message evidence so the whole Tiefgarage is actually checked.
5. `S1`: add an explicit suppression/containment task to `predefined_tasks` and `gold_task_states`, or remove fire-suppression implications from the message stream if the scenario is intentionally limited to search/water/ventilation.
6. Re-run content validation after revisions with special attention to whether every `completed=true` label is backed by a message that describes a finished effect, not merely ongoing work.
