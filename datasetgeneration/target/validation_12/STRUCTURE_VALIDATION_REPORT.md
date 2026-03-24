# STRUCTURE_VALIDATION_REPORT

## Scope and Method

This review evaluates only structural validity and communication realism, grounded strictly in:

- `./.agents/datasetgeneration/dataset_validation_structure.md`
- `./.agents/datasetgeneration/source_notes_sprechregeln.md`
- `./.agents/datasetgeneration/source_notes_real_transcript.md`

Operational correctness was not evaluated.

Binary gate used in this report:

- `PASS` only if scenario rubric verdict is `PASS`
- `FAIL` if scenario rubric verdict is `PARTIAL` or `FAIL`

---

## Per-Scenario Assessment

### S1 - Kuechenbrand Mehrfamilienhaus

#### Criteria

| Criterion | Rating | Notes |
|---|---|---|
| Message Structure Validity | PASS | Clear sender/receiver structure in most messages. `1`, `5`, `7`, `9`, `14`, `17` use recognizable protocol frames; reports such as `4`, `11`, `12`, `16` remain immediately interpretable. |
| Protocol Adherence | PASS | Commands in `5`, `7`, `9`, `14`, `17` are acknowledged in `6`, `8`, `10`, `15`, `18`. Multi-recipient call in `1` receives ordered acknowledgements in `2` and `3`. |
| Turn-Taking Plausibility | PASS | Response order is plausible and only addressed units answer direct orders. Self-initiated status traffic in `11`, `12`, `13`, `16` is contextually relevant. |
| Communication Flow Realism | PARTIAL | The progression is coherent, but the flow is very clean and serialized: command, immediate acknowledgement, completion report. Real transcript notes allow this, but the scenario underuses irregularity and interleaving. |
| Acknowledgement Patterns | PASS | Acknowledgements are present for all key commands and use acceptable compressed forms such as `verstanden` and `korrekt`. |
| Communication Economy and Style | PASS | Messages are short, direct, and operational. Longer reports `12` and `16` remain concise enough for radio traffic. |

#### Good

- `1` to `3` shows a plausible broadcast-to-sequential-response pattern.
- `12` and `13` distinguish search findings from suppression progress instead of collapsing all outcomes into one unrealistic message.
- `16` preserves incompletion explicitly, which matches the transcript guidance on partial progress reporting.

#### Issues

- Minor: `19` is a broad update with no follow-up acknowledgement. This is acceptable for a broadcast, but the scenario does not show any alternative acknowledgement behavior, so the exchange remains highly controlled rather than naturally varied.

#### Verdict

- Rubric verdict: `PASS`
- Pass/Fail judgment: `PASS`

---

### S2 - Tiefgaragenbrand Wohnblock

#### Criteria

| Criterion | Rating | Notes |
|---|---|---|
| Message Structure Validity | PASS | Most messages use stable radio structure; even shorter acknowledgements remain interpretable. |
| Protocol Adherence | PARTIAL | `12` is labeled `Meldung` but functions as a directed placement instruction with `antworten`. `19` also acts like a control instruction while framed as `Meldung` and without `antworten`. Intent stays recoverable, but label discipline is inconsistent. |
| Turn-Taking Plausibility | PASS | Directed responses are returned by the addressed units. Independent updates from `7`, `8`, `11`, `14`, `15`, `18`, `20` fit incident progression. |
| Communication Flow Realism | PASS | The scenario includes assignment, readiness, fire attack, monitoring setup, partial measurement, and non-final closure. That mix matches the source transcript style. |
| Acknowledgement Patterns | PASS | Key orders in `3`, `5`, `9`, `16` are acknowledged in `4`, `6`, `10`, `17`. |
| Communication Economy and Style | PASS | Messages remain compressed and task-focused. `11` and `20` are longer but still realistic status reports. |

#### Good

- `11`, `14`, `18`, and `20` give incremental progress rather than instant completion, which supports realistic sequencing.
- `15` provides a useful autonomous logistics update without requiring a prompt, consistent with the source transcript.

#### Issues

- Moderate: `12` mixes a staging instruction with the message type `Meldung` and still demands `antworten`. Structurally this behaves like a command, not a pure report.
- Minor: `19` again uses `Meldung` for what is effectively a directed area control constraint. This is still interpretable but weakens protocol consistency.

#### Verdict

- Rubric verdict: `PASS`
- Pass/Fail judgment: `PASS`

---

### S3 - Kellerbrand Schulhaus

#### Criteria

| Criterion | Rating | Notes |
|---|---|---|
| Message Structure Validity | PASS | Individual messages are easy to parse and maintain sender/receiver clarity. |
| Protocol Adherence | PARTIAL | `12` is addressed only to `Angriffstrupp` but contains an operative instruction for `Wassertrupp` ("Wassertrupp bleibt an Kellertreppe in Reserve") without direct address or acknowledgement. That weakens traceable command structure. |
| Turn-Taking Plausibility | PARTIAL | Because `12` embeds a second-unit instruction without allocating a turn to that unit, the scenario blurs who is expected to respond. `13` acknowledges only the attack-trupp portion, leaving the water-trupp instruction unconfirmed. |
| Communication Flow Realism | PARTIAL | The overall sequence is coherent, but it is unusually linear and single-threaded. After initial deployment, almost every turn directly advances one task chain with little realistic overlap or conversational friction. |
| Acknowledgement Patterns | PASS | Direct commands in `2`, `4`, `7`, `12` receive acknowledgement behavior, although `12` is only partially acknowledged due to the embedded second instruction. |
| Communication Economy and Style | PASS | The messages are concise and radio-like. |

#### Good

- `10`, `11`, and `15` form a plausible reconnaissance-to-control progression.
- `6` is a concise role-appropriate access-control report.

#### Issues

- Moderate: `12` issues two functional instructions to two different units but only one recipient is formally addressed. This is the clearest structural defect in the dataset because it breaks explicit routing and acknowledgement expectations.
- Moderate: `13` confirms only the `Angriffstrupp` portion of `12`, leaving the `Wassertrupp` reserve instruction unacknowledged.
- Minor: The scenario underuses interleaving and feels more generated than transcribed.

#### Verdict

- Rubric verdict: `PARTIAL`
- Pass/Fail judgment: `FAIL`

---

### S4 - Werkstattbrand mit Gasflaschen

#### Criteria

| Criterion | Rating | Notes |
|---|---|---|
| Message Structure Validity | PASS | Sender/receiver framing is consistent and reports are interpretable throughout. |
| Protocol Adherence | PASS | Commands in `3`, `5`, `8`, `10`, `14`, `18`, `22` are acknowledged in the next relevant turns. |
| Turn-Taking Plausibility | PASS | Units respond when called and also send plausible autonomous updates such as `7`, `12`, `13`, `16`, `17`, `20`, `21`. |
| Communication Flow Realism | PARTIAL | The scenario includes multiple strands, but they are still overly neat. Nearly every instruction is answered immediately and fully, with little protocol noise or compression variation despite the construction log claiming such variation. |
| Acknowledgement Patterns | PASS | Acknowledgements are clear and semantically aligned with the commands. |
| Communication Economy and Style | PASS | Style is concise, task-focused, and readable. |

#### Good

- `13` and `20` provide partial completion states rather than forced task closure, which is structurally realistic.
- `10` to `16` models dependency sequencing plausibly: cooling first, then interior foam attack.

#### Issues

- Minor: `24` uses the phrase "Einsatzstelle bleibt in laufender Phase", which is interpretable but sounds more synthetic than naturally compressed radio phrasing.
- Minor: The scenario remains cleaner and more protocol-complete than the stated target of mixed transcript realism.

#### Verdict

- Rubric verdict: `PASS`
- Pass/Fail judgment: `PASS`

---

### S5 - Dachstockbrand Reihenhaus

#### Criteria

| Criterion | Rating | Notes |
|---|---|---|
| Message Structure Validity | PASS | Calls, orders, and reports are clearly formatted and interpretable. |
| Protocol Adherence | PARTIAL | `21` is labeled `Anfrage`, but the content is really a handover notification/request rather than a crisp radio question. This is not a breakdown, but the intent marker is looser than the rest of the dataset. |
| Turn-Taking Plausibility | PASS | `9` instructs the attack team to proceed after the ladder report; `11` then unlocks the action and `12` follows plausibly. |
| Communication Flow Realism | PASS | The sequence includes deployment, readiness setup, dependent attack start, control, verification, and handover. |
| Acknowledgement Patterns | PASS | Orders in `4`, `6`, `9`, `13`, `15`, `18` are acknowledged in `5`, `7`, `10`, `14`, `16`, `19`. |
| Communication Economy and Style | PASS | Messages are compact and operational; longer control messages remain acceptable. |

#### Good

- `9` to `12` captures a realistic dependency chain without requiring a redundant extra release from command.
- `20` is a structurally strong completion report because it gives result plus residual-condition check.

#### Issues

- Moderate: `21` uses `Anfrage` where the actual function is closer to coordination/handover initiation. The reply in `22` makes the intent understandable, but the label is not fully tight.
- Minor: The scenario ends immediately after police acknowledgement, so the closeout is structurally coherent but still somewhat more scripted than transcript-like.

#### Verdict

- Rubric verdict: `PASS`
- Pass/Fail judgment: `PASS`

---

## Dataset-Level Assessment

### Overall Structural Quality

The dataset is consistently interpretable. Speakers, recipients, and task state transitions remain clear across all five scenarios. No scenario collapses into non-radio narrative text, and all scenarios remain coherent under transcript-style rendering with omitted punctuation or reduced closures.

The strongest structural property is traceability: assignments, acknowledgements, progress reports, and completion or non-completion states can usually be linked cleanly at message level.

### Cross-Dataset Critical Issues

- None found.

### Cross-Dataset Moderate Issues

- Overcontrolled protocol style across the whole set. The construction log claims "mixed protocol completeness" and "delayed or reduced acknowledgements", but actual traffic is dominated by clean `An ... von ...` structures and immediate direct acknowledgements. This reduces realism diversity.
- Limited protocol noise. Real transcript guidance explicitly allows missing labels, omitted `schluss`, reduced closures, and elliptical shorthand. Those features appear only lightly here, so the dataset does not fully exercise the intended representation range.
- One genuine routing defect appears in S3 `12` and `13`, where a second unit receives an implicit instruction without direct addressing or acknowledgement.

### Cross-Dataset Minor Issues

- Message type labels are occasionally semantically loose, especially when a directive is framed as `Meldung` or a coordination statement is framed as `Anfrage`:
  - S2 `12`
  - S2 `19`
  - S5 `21`
- Most scenarios are highly serialized: command, acknowledgement, progress, completion. Interleaving exists, but stress-pattern disorder and partial protocol collapse are underrepresented.
- Closure usage is almost uniformly polished. This is structurally valid, but less realistic relative to the cited transcript notes.

### What Is Good Across the Dataset

- Every scenario remains understandable without outside operational knowledge.
- Key actions are usually acknowledged, satisfying the core protocol requirement.
- Units mostly report only what they can plausibly observe within the scenario framing.
- Partial task states are represented well in S1, S2, and S4, which helps transcript realism.

### Coherence Under Intended Transcript Representations

The dataset remains coherent under lightly compressed transcript representation because message meaning is explicit and redundant enough to survive omission of punctuation or closure markers.

However, robustness under more natural transcript-style variation is only partially demonstrated. Because the dataset is so controlled, there is limited evidence that the scenarios would still feel realistic if rendered with stronger ellipsis, reduced acknowledgements, or noisier sequencing. In other words: coherence is strong, but realism range is narrow.

---

## Overall Judgment

- Overall rubric verdict: `PARTIAL`
- Explicit overall pass/fail judgment: `FAIL`

Reason:

- Four scenarios meet rubric `PASS`.
- One scenario, S3, is `PARTIAL` due to a concrete routing/acknowledgement defect.
- Dataset-level realism variation is narrower than claimed in the construction log, so the collection does not fully satisfy the intended transcript-realism target.

---

## Concrete Revision List

1. Fix S3 `12` and `13` by separating the `Wassertrupp` reserve instruction into its own directly addressed message and requiring an acknowledgement from `Wassertrupp`.
2. Tighten message-type labeling where directives are currently framed as reports:
   - S2 `12`
   - S2 `19`
   - S5 `21`
3. Introduce a small number of controlled realistic deviations per scenario:
   - omit `Schluss` in some non-critical turns
   - use shorter acknowledgements such as `verstanden` without full restatement
   - allow occasional compressed self-status lines without full `An ... von ...` framing
4. Add at least one delayed or interleaved acknowledgement pattern in multiple scenarios so the traffic does not always resolve in immediate one-command/one-reply order.
5. Increase transcript-style variation promised by the construction log:
   - more elliptical field shorthand
   - a few partial readbacks
   - occasional mixed-form messages where status and request are combined
6. Preserve interpretability while varying polish. The current dataset is readable, but it needs more controlled imperfection to match the cited real transcript guidance.
