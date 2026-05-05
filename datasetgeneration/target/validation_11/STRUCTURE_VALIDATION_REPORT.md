# Structure Validation Report

Dataset: `data/scenarios/synthetic_firefighter_radio_controlled_v1`

Scope of this review:
- structural validity only
- communication realism only
- no evaluation of operational correctness or tactical validity

Judgment basis:
- `./.agents/datasetgeneration/dataset_validation_structure.md`
- `./.agents/datasetgeneration/source_notes_sprechregeln.md`
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
| Message Structure Validity | PASS | Strong use of explicit addressing and message labels in `1`, `4`, `5`, `7`, `9`, `14`, `16`, `17`. |
| Protocol Adherence | PASS | Directed commands in `5`, `7`, `9`, `14` are acknowledged immediately in `6`, `8`, `10`, `15`. Multi-recipient call in `1` gets ordered replies in `2` and `3`. |
| Turn-Taking Plausibility | PASS | Response allocation is clear and the addressed units respond in plausible order. |
| Communication Flow Realism | PASS | The flow mixes alerting, arrival report, assignments, acknowledgements, progress reports, and a partial closure state. |
| Acknowledgement Patterns | PASS | Readbacks are short but aligned with the command content, especially `6`, `8`, `10`, `15`. |
| Communication Economy and Style | PASS | Short, compressed radio-style phrasing throughout, with slightly longer but plausible reconnaissance/status reports in `4`, `12`, `13`, `16`. |

Good:
- `1` to `3` is the cleanest multi-party opening in the dataset. The broadcast names recipients, requests replies, and gets compact acknowledgements in sequence.
- `12` and `13` are good examples of realistic longer operational updates: still compressed, but descriptive enough to justify later command traffic.
- The scenario remains interpretable in `no_speaker` and `continuous_transcript` because most turns self-identify sender or recipient inside the utterance text.

Issues:
- Minor: `17` is labeled as `Meldung` but functions partly as an instruction to the ventilation unit. It is still interpretable, but the message type is less exact than the idealized speaking-rules template.

Framework verdict: `PASS`

Explicit scenario pass/fail judgment: `PASS`

### S2 `Tiefgaragenbrand Wohnblock`

Criterion scores:

| Criterion | Score | Notes |
| --- | --- | --- |
| Message Structure Validity | PASS | Most messages remain clearly interpretable as radio utterances and include enough sender/receiver intent to track who is doing what. |
| Protocol Adherence | PARTIAL | Several transmissions weaken protocol completion. `6` and `13` omit `Schluss`, and the first Messgruppe acknowledgement in `13` is notably thin for a directed `Befehl` in `12`. |
| Turn-Taking Plausibility | PASS | Request-response order is still understandable, and no unrelated unit interrupts a directed exchange. |
| Communication Flow Realism | PARTIAL | The flow is coherent, but it is unusually clean and linear. The Messgruppe exchange in `12` to `15` reads more like staged dataset scaffolding than naturally interleaved traffic. |
| Acknowledgement Patterns | PARTIAL | Key commands are acknowledged, but some acknowledgements are under-specified. `13` only gives a reduced future-action confirmation after `12`, and `6` ends without closure. |
| Communication Economy and Style | PASS | Messages are generally short and compressed. |

Good:
- `9` to `11` is a plausible assignment-readback-report sequence.
- `16` is a good compressed measurement report: short, evidence-based, and clearly radio-like.
- Even without speaker labels, the scenario stays interpretable because most operational turns retain explicit internal addressing.

Issues:
- Moderate: `12` asks the `Messgruppe` to act only "nach Freigabe", but `13` gives only a reduced acknowledgement without closure or full readback. That is still understandable, but it is weaker than the documented command-acknowledgement pattern.
- Moderate: `12` to `15` creates a slightly synthetic two-step measurement setup: pre-brief in `12`, reduced acknowledgement in `13`, then nearly immediate activation in `15`. This is not impossible, but the sequencing feels authored for task-state traceability more than observed radio flow.
- Minor: `6` lacks `Schluss`.
- Minor: `13` lacks `Schluss`.
- Minor: `5` uses the fully explicit pattern `An Wassertrupp von Einsatzleitung`, which is valid, but the scenario overall relies much more on idealized command syntax than the source transcript notes suggest.

Framework verdict: `PARTIAL`

Explicit scenario pass/fail judgment: `FAIL`

### S3 `Kellerbrand Schulhaus`

Criterion scores:

| Criterion | Score | Notes |
| --- | --- | --- |
| Message Structure Validity | PASS | Clear sender/receiver signaling and recognizable command/report structure throughout. |
| Protocol Adherence | PASS | Directed commands in `2`, `4`, `7`, `12` are acknowledged in `3`, `5`, `8`, `13`. |
| Turn-Taking Plausibility | PASS | The sequence respects role allocation and keeps responses with the addressed unit. |
| Communication Flow Realism | PASS | Good mix of broadcast orientation, directed assignments, resource status, reconnaissance, follow-up instruction, and incident-wide update. |
| Acknowledgement Patterns | PASS | Readbacks are compressed but functional. |
| Communication Economy and Style | PASS | Concise and operationally compressed without becoming opaque. |

Good:
- `7` to `10` is one of the stronger tactical micro-sequences in the dataset: command, readback, logistics readiness, then reconnaissance/update.
- `12` to `15` shows a plausible second-cycle command after initial knockdown rather than ending immediately after the first success report.
- `16` is a realistic incident-wide recap: short, broadcast-oriented, and still operationally specific.

Issues:
- Minor: `16` is a broad closing update without acknowledgements from recipients. This is acceptable under the real-transcript notes for broadcasts, but it adds to the dataset-wide pattern of clean one-way wrap-up messages.

Framework verdict: `PASS`

Explicit scenario pass/fail judgment: `PASS`

### S4 `Werkstattbrand mit Gasflaschen`

Criterion scores:

| Criterion | Score | Notes |
| --- | --- | --- |
| Message Structure Validity | PASS | Strong explicit addressing keeps the multi-unit scene easy to parse. |
| Protocol Adherence | PARTIAL | `18` is labeled as `Meldung` but functions partly as an instruction to `Verkehrstrupp`. This is interpretable, but it blurs the documented message-type distinction. |
| Turn-Taking Plausibility | PASS | Responses come from the addressed unit and parallel updates are kept orderly. |
| Communication Flow Realism | PARTIAL | The sequence is readable, but the scenario ends on an acknowledged ongoing cooling task in `21` to `22` with no subsequent update. That ending feels abruptly cut for a radio transcript, even if an open task is allowed in the dataset. |
| Acknowledgement Patterns | PASS | Commands are acknowledged consistently and usually with short readback. |
| Communication Economy and Style | PASS | Good compression and role-specific reporting. |

Good:
- `8` to `15` shows convincing interleaving between cooling readiness and delayed attack authorization.
- `13` is a good state update because it is short but still gives a meaningful residual condition.
- The scenario remains coherent under `continuous_transcript` because the command/report markers are repeated frequently enough to survive flattening.

Issues:
- Moderate: `18` is structurally mixed. "Sicherheitsbereich beibehalten" acts like a direction to `Verkehrstrupp`, but the transmission is labeled `Meldung` and does not use `antworten`.
- Moderate: the scenario terminates after `21` and `22` while the cooling task is still explicitly open. That is acceptable for task monitoring, but as a stand-alone radio scene it feels truncated rather than naturally wound down.

Framework verdict: `PASS`

Explicit scenario pass/fail judgment: `PASS`

### S5 `Dachstockbrand Reihenhaus`

Criterion scores:

| Criterion | Score | Notes |
| --- | --- | --- |
| Message Structure Validity | PASS | Strong explicit structure and clear sender/receiver references throughout. |
| Protocol Adherence | PARTIAL | `5` omits `Schluss`, and `21` is formally tagged `Meldung` while pragmatically functioning as a directed handover request. |
| Turn-Taking Plausibility | PASS | The sequencing around the ladder readiness in `4` to `11` and the control team activation in `15` to `20` is plausible. |
| Communication Flow Realism | PASS | Good progression from initial size-up to staging, access readiness, internal check, extinguishment, final control, and handover. |
| Acknowledgement Patterns | PARTIAL | Commands are acknowledged, but `5` is a reduced acknowledgement with no closure and the final police exchange is slightly stylized. |
| Communication Economy and Style | PASS | Compact and radio-like, with longer turns reserved for task progress. |

Good:
- `9` to `12` is structurally strong: conditional assignment, readback, enabling readiness message, then progress report.
- `15` to `20` models a credible "after attack, independent control check" pattern.
- This is one of the best scenarios for transcript-representation robustness because sender and receiver are repeatedly named inside the message text itself.

Issues:
- Moderate: `21` says `Meldung` but is effectively a directed handover prompt to `Polizei` because it explicitly expects a reply with `antworten`.
- Minor: `5` lacks `Schluss`.

Framework verdict: `PASS`

Explicit scenario pass/fail judgment: `PASS`

## Dataset-Level Assessment

### Overall result

Framework-level scenario outcomes:
- `S1`: `PASS`
- `S2`: `PARTIAL`
- `S3`: `PASS`
- `S4`: `PASS`
- `S5`: `PASS`

Explicit overall pass/fail judgment: `FAIL`

Reason:
- One scenario (`S2`) does not meet the framework `PASS` threshold.
- The dataset is broadly usable and mostly coherent, but it is not yet consistently strong enough to pass a strict independent structural validation across all scenarios.

### Cross-Dataset Strengths

- Addressing is consistently explicit enough that all five scenarios remain interpretable under `structured_dialogue`, `no_speaker`, and `continuous_transcript`.
- Commands are usually followed by acknowledgements, and the addressed unit is almost always the one that responds.
- Message economy is strong. The dataset avoids long narrative exposition and keeps most turns compact.
- Several scenarios include a good mix of assignments, acknowledgements, progress reports, and completion-style reports instead of using only one message pattern.

### Cross-Dataset Patterns That Reduce Realism

- The dataset is generally more polished and more protocol-explicit than the real-transcript notes suggest. It uses many idealized `An X von Y, Meldung/Befehl` constructions and relatively little natural shorthand variation.
- There is very little protocol noise. Missing `Schluss` appears occasionally, but there are almost no examples of repair traffic, repetition requests, partial misunderstanding, or messy interleaving.
- Message-type labels are sometimes used loosely. Some transmissions marked `Meldung` act partly as instructions or reply-seeking turns:
  - `S1-17`
  - `S4-18`
  - `S5-21`
- Several scenarios end as soon as the monitored task state is clear, rather than at a more natural conversational stopping point. This is most visible in:
  - `S4-21` to `S4-22`
- Compared with the source transcript notes, concurrent traffic is still relatively sparse and controlled. The dataset often reads as one command chain at a time rather than overlapping operational radio traffic.

### Coherence Under Intended Transcript Representations

- `structured_dialogue`: fully coherent across all scenarios.
- `no_speaker`: still coherent because the utterances themselves usually encode speaker/recipient identity.
- `continuous_transcript`: still mostly coherent, but the dataset depends heavily on repeated explicit addressing to survive flattening. This works technically, but it also exposes how authored and formulaic many turns are.

## Concrete Revision List

Apply the following revisions in a later fix pass:

1. Strengthen `S2` first. Improve `12` to `15` so the `Messgruppe` exchange reads more like natural radio traffic and less like a staged two-step task marker.
2. Add missing closure markers where currently omitted without clear stylistic reason:
   - `S2-6`
   - `S2-13`
   - `S5-5`
3. Tighten message-type labeling where a transmission functions as a command or directed request rather than a plain report:
   - `S1-17`
   - `S4-18`
   - `S5-21`
4. Introduce slightly more real-transcript-style variation in at least some scenarios:
   - shorter elliptical acknowledgements
   - occasional sender compression without full formal syntax
   - one or two imperfect but still interpretable protocol deviations
5. Increase non-linear interleaving in at least `S2` and `S4` so the traffic feels less serialized and less authored around task boundaries.
6. Where a scenario intentionally ends with open tasks, add one explicit framing cue before the end so the transcript does not feel cut off mid-traffic.
7. Preserve cross-representation robustness during revisions. Any reduction in formal syntax must still keep the message sequence interpretable in `no_speaker` and `continuous_transcript`.

## Bottom Line

The dataset is structurally stronger than many synthetic radio sets because it stays interpretable under all three transcript representations and usually maintains disciplined command-response flow. It still falls short of a strict full pass because `S2` is only `PARTIAL`, and because the dataset as a whole is somewhat too clean, too uniformly authored, and occasionally loose with message-type labels relative to the source realism notes.
