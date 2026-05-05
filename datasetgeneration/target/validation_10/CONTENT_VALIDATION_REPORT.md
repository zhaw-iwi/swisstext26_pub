# Content Validation Report

Validation basis:
- `./.agents/datasetgeneration/dataset_validation_content.md`
- `./.agents/datasetgeneration/source_notes_einsatzfuehrung.md`
- `./.agents/datasetgeneration/source_notes_real_transcript.md`

Scope:
- Evaluated only operational plausibility and task-content validity.
- Did not evaluate protocol formatting except where it affects task interpretation.

Release gate used in this report:
- `PASS` if the scenario-level guidance verdict is `PASS`
- `FAIL` if the scenario-level guidance verdict is `PARTIAL` or `FAIL`

## Per-Scenario Assessment

### S1 - Kuechenbrand Mehrfamilienhaus

Criterion ratings:

| Criterion | Rating | Justification |
|---|---|---|
| Task Realism | PASS | `T1` water supply, `T2` person search, and `T3` smoke control are all valid fireground task families and are radio-actionable. |
| Scenario Plausibility | PASS | Message flow follows realistic progression: alarm picture (`m1`), local assessment (`m4`), tasking (`m5`, `m7`, `m9`), execution and updates (`m11`-`m16`). |
| Role and Assignment Correctness | PASS | Einsatzleitung assigns; Angriffstrupp searches and suppresses; Wassertrupp builds supply; Lueftungstrupp waits for release before ventilation. |
| Task Sequencing and Dependencies | PASS | Ventilation is explicitly delayed until after attack progress (`m9`, `m14`), which matches the source-note dependency logic. |
| Completion Signal Validity | PASS | `T1` is completed by an observable setup result in `m11`; `T2` by a search result in `m12`; `T3` is correctly left incomplete with evidence in `m16`. |
| Traceability of Gold Task States | PASS | All three gold states map cleanly to explicit assignment and report messages. |
| Consistency Across Scenario | PASS | No contradictions between messages, predefined tasks, and gold states. |

Issues:
- Minor: None material for content validity.

Guidance verdict: `PASS`

Pass/fail judgment: `PASS`

### S2 - Tiefgaragenbrand Wohnblock

Criterion ratings:

| Criterion | Rating | Justification |
|---|---|---|
| Task Realism | PASS | Power isolation (`T1`), vehicle-fire suppression (`T2`), and post-fire CO control (`T3`) are realistic and observable tasks. |
| Scenario Plausibility | PASS | The sequence from smoke report (`m1`-`m2`) to hazard control (`m3`, `m7`), hose deployment (`m4`, `m8`), attack (`m9`-`m18`), and measurement (`m12`-`m19`) is coherent. |
| Role and Assignment Correctness | PASS | Sicherheitstrupp handles electrical/access safety; Wassertrupp supports attack route; Angriffstrupp performs interior suppression; Messgruppe performs atmosphere checks. |
| Task Sequencing and Dependencies | PASS | Power and hose line are established before the offensive order in `m9`; measurement is delayed until attack progress is reported in `m14`-`m15`. |
| Completion Signal Validity | PASS | `T1` completion in `m7` and `T2` completion in `m18` are supported by direct operational evidence; `T3` is correctly incomplete in `m17`. |
| Traceability of Gold Task States | PASS | Assignments and final labels are all message-supported. |
| Consistency Across Scenario | PASS | The scenario maintains one clear operational picture without contradictory state changes. |

Issues:
- Minor: `T3` is scoped only to `Vorraum` and `Rampe`. For a vehicle fire in a deep garage, that is a narrow control scope, but the scenario does not falsely present it as a final release or handover, so it remains acceptable.

Guidance verdict: `PASS`

Pass/fail judgment: `PASS`

### S3 - Kellerbrand Schulhaus

Criterion ratings:

| Criterion | Rating | Justification |
|---|---|---|
| Task Realism | PASS | Access control (`T1`), hose deployment (`T2`), and recon/extinguishment/shaft control (`T3`) fit the source-note task families. |
| Scenario Plausibility | PASS | The scenario starts with a partially known picture (`m1`), secures the perimeter (`m2`, `m6`), builds water supply (`m3`, `m9`), then conducts cellar attack and follow-up control (`m7`, `m10`-`m15`). |
| Role and Assignment Correctness | PASS | The assigned units act within plausible capabilities. |
| Task Sequencing and Dependencies | PASS | People are kept out of the building before the interior task; water supply is reported ready before the attack update in `m10`; spread check follows extinguishment. |
| Completion Signal Validity | PASS | `T1` and `T2` have clear observable completion reports; `T3` is completed with extinguishment plus no shaft spread in `m15`. |
| Traceability of Gold Task States | PASS | Gold labels are directly supported by assignments and subsequent reports. |
| Consistency Across Scenario | PASS | Messages and task states are coherent throughout. |

Issues:
- Minor: `T3` bundles reconnaissance, extinguishment, and spread-control into one tracked task. It is still traceable here, but the task granularity is denser than in the other scenarios.

Guidance verdict: `PASS`

Pass/fail judgment: `PASS`

### S4 - Werkstattbrand mit Gasflaschen

Criterion ratings:

| Criterion | Rating | Justification |
|---|---|---|
| Task Realism | PASS | Scene security (`T1`), suppression (`T2`), and cooling of heated cylinders (`T3`) are realistic fireground tasks. |
| Scenario Plausibility | PARTIAL | The overall incident picture is plausible, but the known gas-cylinder hazard from `m1`-`m2` is not fully integrated into the initial tactical sequence. |
| Role and Assignment Correctness | PASS | Verkehrstrupp, Angriffstrupp, and Wassertrupp all receive plausible task domains. |
| Task Sequencing and Dependencies | PARTIAL | `T2` is assigned in `m8` before dedicated cooling of the gas cylinders (`T3`) is ordered in `m10`. Given the already reported presence of two cylinders in the fire compartment (`m1`-`m2`), the safety dependency is weakly handled. A more defensible sequence would establish cooling or a clearer hazard-control condition before the offensive suppression order. |
| Completion Signal Validity | PASS | `T1` completion in `m12` and `T2` completion in `m19` are well evidenced; `T3` is correctly left incomplete with `m20`. |
| Traceability of Gold Task States | PASS | The gold labels are message-supported. |
| Consistency Across Scenario | PASS | No direct contradictions, but the tactical logic is cleaner than the hazard logic. |

Issues:
- Moderate: `T2` / `m8` is launched before `T3` / `m10` despite the hazardous-cylinder condition already being known in `m1`-`m2`. This weakens the required safety-before-deep-action dependency from the guidance.
- Minor: `T3` completion criteria are good, but the scenario never adds a later control action such as final temperature verification after cooling. That is acceptable for an in-progress scenario, but it limits realism depth.

Guidance verdict: `PARTIAL`

Pass/fail judgment: `FAIL`

### S5 - Dachstockbrand Reihenhaus

Criterion ratings:

| Criterion | Rating | Justification |
|---|---|---|
| Task Realism | PASS | Ladder standby (`T1`), opening/search/extinguishment in the roof space (`T2`), and thermal final check (`T3`) are all realistic and radio-trackable. |
| Scenario Plausibility | PASS | The sequence from initial exterior smoke picture (`m1`, `m3`) to access setup (`m4`-`m11`), roof-space intervention (`m9`-`m17`), control check (`m15`-`m20`), and handover readiness (`m21`-`m22`) is coherent. |
| Role and Assignment Correctness | PASS | Drehleiter provides access readiness, Angriffstrupp performs roof-space work, Kontrolltrupp performs final verification. |
| Task Sequencing and Dependencies | PASS | Attack is explicitly delayed until ladder readiness is reported (`m9`, `m11`); control check is delayed until Angriffstrupp completion (`m15`, `m18`). |
| Completion Signal Validity | PASS | `T1`, `T2`, and `T3` each have observable completion evidence. |
| Traceability of Gold Task States | PASS | The gold labels are well supported. |
| Consistency Across Scenario | PASS | Messages, tasks, and gold labels remain aligned. |

Issues:
- Minor: `T2` is a composite task. Its completion evidence is distributed across `m12` and `m17`, even though the gold completion outcome cites only `m17`. This is still acceptable, but future scenarios should keep task bundles slightly narrower.

Guidance verdict: `PASS`

Pass/fail judgment: `PASS`

## Dataset-Level Assessment

Summary:
- Scenario guidance verdicts: `S1 PASS`, `S2 PASS`, `S3 PASS`, `S4 PARTIAL`, `S5 PASS`
- Binary release gate: `4 PASS`, `1 FAIL`

Cross-dataset strengths:
- Task families stay inside plausible firefighter-radio scope.
- Assignments are almost always attributable to Einsatzleitung and executed by plausible units.
- Gold task states are generally traceable to explicit assignment and completion messages.
- Incomplete tasks are usually labeled conservatively rather than overclaimed.

Cross-dataset issues:
- Moderate: Hazard-control dependencies are sometimes under-modeled when a serious risk is already known. The clearest case is `S4`, where the gas-cylinder hazard is recognized before the suppression push but is not handled as the stronger sequencing constraint.
- Moderate: Several scenarios use composite predefined tasks that merge multiple operational steps into one label (`S3/T3`, `S5/T2`). They remain interpretable, but this reduces clean one-to-one traceability between task label, execution phase, and completion evidence.
- Minor: Most scenarios are tactically clean and low-friction. They contain less reassessment, obstruction, or conflicting field information than the source notes suggest is common in real incidents.
- Minor: Some scenarios stop before a fuller control or demobilization phase (`S1`, `S2`, `S4`). That is acceptable for partial incidents, but it reduces realism breadth across the dataset.

Guidance-level overall verdict:
- `PARTIAL`

Overall pass/fail judgment:
- `FAIL`

Reason for overall fail:
- The set is close to usable, but at least one scenario (`S4`) has a material operational sequencing weakness tied to a known hazard, so the dataset should not be treated as fully content-validated without revision.

## Concrete Revision List

1. Revise `S4` so the gas-cylinder hazard controls the tactical sequence more clearly.
   - Either move the cooling task (`T3`) before the offensive suppression order (`m8`), or add an explicit safety condition in the suppression order that makes the attack contingent on established cooling/cover.

2. Tighten task granularity in scenarios with bundled predefined tasks.
   - Split `S3/T3` into separate tasks for `erkunden/Brand lokalisieren`, `abloeschen`, and `Installationsschacht kontrollieren` if those steps need to be tracked independently.
   - Split `S5/T2` into `Dachstock oeffnen und Glutnester suchen` and `Glutnester abloeschen` if single-message completion traceability is desired.

3. Where a scenario ends with an incomplete hazard-control task, add one more control-oriented update when possible.
   - For `S1/T3`, consider a later smoke-control effectiveness report or explicit reason the task remains open.
   - For `S2/T3`, consider whether the measurement task should remain intentionally narrow or whether a broader post-fire control check is operationally intended.
   - For `S4/T3`, add a later temperature-based or status-based control report if the scenario is meant to approach stabilization.

4. Add slightly more realistic reassessment in at least some scenarios.
   - Examples: changed smoke conditions, access restriction, delayed resource effect, or a command re-prioritization triggered by a field update.

5. Keep completion evidence tied to the exact tracked task outcome.
   - If a gold task state is `completed=true`, the cited completion outcome should ideally describe the end-state of the whole predefined task, not only the final sub-step.
