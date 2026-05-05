# Content Validation Report

Dataset: `data/scenarios/synthetic_firefighter_radio_controlled_v1`

Scope of this review:
- operational plausibility only
- task-content validity only
- no evaluation of communication protocol structure except where it affects task interpretation

Judgment basis:
- `./.agents/datasetgeneration/dataset_validation_content.md`
- `./.agents/datasetgeneration/source_notes_einsatzfuehrung.md`
- `./.agents/datasetgeneration/source_notes_real_transcript.md`

Pass threshold used here:
- Scenario `PASS` only if the framework verdict is `PASS`
- Scenario `FAIL` if the framework verdict is `PARTIAL` or `FAIL`
- Dataset `PASS` only if all scenarios pass

## Per-Scenario Assessment

### S1 `Kuechenbrand Mehrfamilienhaus`

Criterion scores:

| Criterion | Score | Notes |
| --- | --- | --- |
| Task Realism | PASS | `T1` (`7` to `11`), `T2` (`5` to `12`), and `T3` (`9` to `16`) are actionable radio tasks within doctrine task families. |
| Scenario Plausibility | PASS | The incident evolves plausibly from alarm picture (`1`) to arrival report (`4`), rescue/search (`5` to `12`), suppression (`13`), then smoke control (`14` to `16`). |
| Role and Assignment Correctness | PASS | Einsatzleitung assigns; Angriffstrupp searches and attacks; Wassertrupp supplies water; Lueftungstrupp ventilates. |
| Task Sequencing and Dependencies | PASS | Search precedes ventilation release; water supply is established before interior suppression develops; smoke control is delayed until after attack-team release. |
| Completion Signal Validity | PASS | `T1` completion in `11` and `T2` completion in `12` are operationally observable. `T3` is correctly left open because `16` explicitly says it is not finished. |
| Traceability of Gold Task States | PASS | All three gold states map cleanly to message evidence. |
| Consistency Across Scenario | PASS | Messages, tasks, and gold labels stay aligned throughout. |

Critical issues:
- None.

Moderate issues:
- None.

Minor issues:
- `T2` completion evidence in message `12` also includes a containment update ("Brand auf Kuechenbereich begrenzt"). This is plausible field compression, but it blends search completion with a separate fire-development assessment.

Framework verdict: `PASS`

Explicit scenario pass/fail judgment: `PASS`

### S2 `Tiefgaragenbrand Wohnblock`

Criterion scores:

| Criterion | Score | Notes |
| --- | --- | --- |
| Task Realism | PASS | Electrical isolation (`T1`), suppression (`T2`), and CO follow-up measurement (`T3`) are realistic task families for this setting. |
| Scenario Plausibility | PASS | Alarm (`1`), first size-up (`2`), hazard control (`3` to `8`), interior attack (`9` to `14`), then measurement (`12`, `15` to `17`) form a coherent progression. |
| Role and Assignment Correctness | PASS | Sicherheitstrupp handles hazard isolation, Wassertrupp supports access/supply, Angriffstrupp suppresses, Messgruppe measures. |
| Task Sequencing and Dependencies | PARTIAL | `T3` is activated in `15` immediately after `14` reports open fire out but while Nachloescharbeiten are still ongoing and the garage remains heavily smoke affected. A first check in the access zones is possible, but the sequence is only partially convincing as an operational milestone. |
| Completion Signal Validity | PASS | `T1` completion in `7`, `T2` completion in `18`, and open-state evidence for `T3` in `17` are all observable and role-appropriate. |
| Traceability of Gold Task States | PASS | Gold labels are supported by specific messages. |
| Consistency Across Scenario | PASS | No contradiction between messages, predefined tasks, and gold states. |

Critical issues:
- None.

Moderate issues:
- `T3` in messages `12`, `15`, and `17` is operationally plausible, but its timing is somewhat synthetic: the task is staged for traceability before the fire scene is meaningfully cleared of smoke. That weakens dependency realism without making the scenario impossible.

Minor issues:
- `T2` task wording is narrower than the actual assignment. Message `9` orders the Angriffstrupp to localize and extinguish the fire, while predefined task `T2` keeps only the extinguishment part.

Framework verdict: `PASS`

Explicit scenario pass/fail judgment: `PASS`

### S3 `Kellerbrand Schulhaus`

Criterion scores:

| Criterion | Score | Notes |
| --- | --- | --- |
| Task Realism | PASS | Access control (`T1`), hose line deployment (`T2`), and reconnaissance/suppression/void check (`T3`) are realistic and radio-trackable. |
| Scenario Plausibility | PASS | The sequence follows alarm picture (`1`), perimeter control (`2` to `6`), supply (`4` to `9`), attack (`7` to `11`), then a control step for possible spread (`12` to `15`). |
| Role and Assignment Correctness | PASS | Tasks match unit capability and reporting perspective throughout. |
| Task Sequencing and Dependencies | PASS | Site security and water supply come before interior action; the shaft check follows initial knockdown and is explicitly requested after the first fire report. |
| Completion Signal Validity | PASS | `6`, `9`, and `15` all provide concrete, observable task outcomes. |
| Traceability of Gold Task States | PASS | Every gold state is directly grounded in message evidence. |
| Consistency Across Scenario | PASS | The operational picture remains coherent from start to finish. |

Critical issues:
- None.

Moderate issues:
- None.

Minor issues:
- The scenario stops at "unter Kontrolle" (`15`, `16`) without a later demobilization or handover phase. That is acceptable for a mid-incident dataset item, but it shortens the canonical closure sequence from the doctrine notes.

Framework verdict: `PASS`

Explicit scenario pass/fail judgment: `PASS`

### S4 `Werkstattbrand mit Gasflaschen`

Criterion scores:

| Criterion | Score | Notes |
| --- | --- | --- |
| Task Realism | PASS | Perimeter/traffic control (`T1`), foam attack on the workbench fire (`T2`), and protected cooling of gas cylinders (`T3`) are realistic task families. |
| Scenario Plausibility | PASS | The scenario builds from hazard recognition (`1`, `2`) to isolation (`3`, `12`), protected cooling (`5` to `13`), then delayed interior attack only after cooling is established (`10`, `14` to `20`). |
| Role and Assignment Correctness | PASS | Verkehrstrupp, Wassertrupp, and Angriffstrupp all operate within plausible domains. |
| Task Sequencing and Dependencies | PASS | Cooling and stand-off protection precede the foam attack, which fits the reported gas-cylinder hazard. |
| Completion Signal Validity | PASS | `T1` completion in `12` and `T2` completion in `20` are strong. `T3` is correctly labeled incomplete because `19` states one cylinder remains warm and `21` to `22` continue the task. |
| Traceability of Gold Task States | PASS | Gold labels are well supported by the message sequence. |
| Consistency Across Scenario | PASS | The scenario stays internally coherent and the open gas-cylinder hazard is carried through correctly. |

Critical issues:
- None.

Moderate issues:
- None.

Minor issues:
- `T3` completion evidence is intentionally an incomplete-state message (`19`). That is valid for the gold label, but it leaves the scenario ending on an unresolved hazard without a later control or handover step.

Framework verdict: `PASS`

Explicit scenario pass/fail judgment: `PASS`

### S5 `Dachstockbrand Reihenhaus`

Criterion scores:

| Criterion | Score | Notes |
| --- | --- | --- |
| Task Realism | PASS | Ladder readiness (`T1`), opening/search/extinguishment in the roof void (`T2`), and independent final control (`T3`) all fit the doctrine notes. |
| Scenario Plausibility | PASS | The progression from initial report (`1`), ladder and water preparation (`4` to `11`), roof opening and hotspot search (`9` to `17`), then final thermal control and handover (`15` to `22`) is coherent. |
| Role and Assignment Correctness | PASS | Drehleiter prepares access, Angriffstrupp performs tactical opening and extinguishment, Kontrolltrupp performs the final check, Polizei receives the scene. |
| Task Sequencing and Dependencies | PASS | Access readiness precedes roof work; extinguishment precedes final control; handover follows a negative control result. |
| Completion Signal Validity | PASS | `11`, `17`, and `20` all provide concrete observable completion evidence. |
| Traceability of Gold Task States | PASS | Gold task states are directly supported by the cited messages. |
| Consistency Across Scenario | PASS | No task-state contradiction is visible. |

Critical issues:
- None.

Moderate issues:
- `T2` bundles opening, search, and extinguishment into one predefined task. The evidence is still traceable across `12` and `17`, but the task definition is broader than the single completion message used in the gold state.

Minor issues:
- For a roof-space fire in a row house, the scenario does not explicitly mention checks of adjacent sections before handover. The existing evidence is still sufficient for this dataset item, but closure realism would be stronger with one explicit neighboring-spread check.

Framework verdict: `PASS`

Explicit scenario pass/fail judgment: `PASS`

## Dataset-Level Assessment

### Overall result

Framework-level scenario outcomes:
- `S1`: `PASS`
- `S2`: `PASS`
- `S3`: `PASS`
- `S4`: `PASS`
- `S5`: `PASS`

Explicit overall pass/fail judgment: `PASS`

Reason:
- No scenario reaches the framework `PARTIAL` or `FAIL` threshold.
- The dataset is operationally coherent and the gold task states are generally well supported by message evidence.

### Cross-Dataset Strengths

- All five scenarios stay inside the task families permitted by the doctrine notes: command/coordination, hazard control, rescue/search, suppression, ventilation or smoke-related control, scene organization, and final checks.
- Task assignments usually follow a sound dependency chain: first assessment, then hazard control or access preparation, then attack, then verification.
- Open tasks are usually labeled correctly rather than being forced into unsupported completions. This is especially clear in `S1-T3`, `S2-T3`, and `S4-T3`.
- Role-task alignment is consistently strong. Units report from positions they could plausibly observe.
- Gold task states are mostly traceable with little ambiguity.

### Cross-Dataset Patterns That Reduce Content Realism

Moderate patterns:
- Several scenarios compress multiple operational subgoals into one predefined task or one completion message. This appears in:
  - `S1-T2`
  - `S3-T3`
  - `S5-T2`
- Canonical closure phases are underrepresented. Only `S5` reaches a clear handover step; `S1`, `S3`, and `S4` stop at control or ongoing operations, and `S2` stops before smoke or gas safety is resolved.
- The dataset tends to present very clear task-state evidence with little uncertainty after assignment. Real incidents often require one more reassessment cycle before a stable completion claim.

Minor patterns:
- Early size-up is sometimes compressed into the initial command picture instead of being developed through a distinct field reassessment cycle.
- Some scenarios end as soon as the target task states are machine-checkable, rather than at the most natural operational stopping point.

Critical patterns:
- None found.

## Concrete Revision List

1. Keep all five scenarios as content-valid baselines, but strengthen dependency realism in `S2` by revising the `Messgruppe` sequence around messages `12`, `15`, and `17`.
2. Split over-bundled predefined tasks where one label currently covers multiple tactical steps:
   - `S1-T2`
   - `S3-T3`
   - `S5-T2`
3. Where a scenario is intended to represent an incomplete incident, add one explicit framing message that makes the open operational state natural rather than abrupt:
   - `S1` after `16`
   - `S2` after `17` or `18`
   - `S4` after `22`
4. Increase the number of explicit control-check transitions before final completion in at least `S1` and `S2`, so that completions follow a clearer `Handeln` to `Kontrollieren` cycle from the doctrine notes.
5. Add one concise closure or handover step in at least two of `S1`, `S3`, and `S4` to better cover the doctrine requirement that incident completion includes checks and transition of responsibility.
6. In future generations, prefer predefined task names that match the actual ordered scope exactly, rather than collapsing reconnaissance, attack, and verification into one label unless the scenario truly tracks them as one unit of work.

## Bottom Line

The dataset passes a strict content-only validation. The scenarios are operationally plausible, the task assignments are realistic, and the gold task states are generally supported by specific radio evidence. The main weakness is not invalidity, but compression: several scenarios package multiple tactical substeps into one tracked task and stop before a fuller closure phase.
