# STRUCTURE_VALIDATION_REPORT

## Scope

This report evaluates only structural validity and communication realism for:

- `data/scenarios/synthetic_firefighter_radio_controlled_v1/s1.json`
- `data/scenarios/synthetic_firefighter_radio_controlled_v1/s2.json`
- `data/scenarios/synthetic_firefighter_radio_controlled_v1/s3.json`
- `data/scenarios/synthetic_firefighter_radio_controlled_v1/s4.json`
- `data/scenarios/synthetic_firefighter_radio_controlled_v1/s5.json`

Grounding sources:

- `./.agents/datasetgeneration/dataset_validation_structure.md`
- `./.agents/datasetgeneration/source_notes_sprechregeln.md`
- `./.agents/datasetgeneration/source_notes_real_transcript.md`

Operational content validity is intentionally excluded.

Pass/fail rule used here:

- Scenario pass/fail judgment = `PASS` only if the framework verdict is `PASS`
- Scenario pass/fail judgment = `FAIL` if the framework verdict is `PARTIAL` or `FAIL`

---

## Per-Scenario Assessment

### S1 - Kuechenbrand Mehrfamilienhaus

| Criterion | Rating | Notes |
| --- | --- | --- |
| Message Structure Validity | PASS | Messages `1`, `4`, `5`, `7`, `9`, `14`, `16` use explicit address and intent. Short replies in `2`, `3`, `8`, `10`, `15` remain clearly interpretable as radio acknowledgements. |
| Protocol Adherence | PASS | Directed orders in `5`, `7`, `9`, `14` are acknowledged in `6`, `8`, `10`, `15`. Later reports follow the established task threads cleanly. |
| Turn-Taking Plausibility | PASS | Only the relevant unit answers each directed order, and the self-initiated reports in `11`, `12`, `13`, `16` fit the active work streams. |
| Communication Flow Realism | PARTIAL | The scenario is coherent, but it ends on an open monitoring thread: `14 -> 15 -> 16` establishes ongoing entrainment work without a visible closure or release. |
| Acknowledgement Patterns | PASS | Readbacks are short but preserve task core and do not contradict the orders. |
| Communication Economy and Style | PASS | Phrasing is compressed, operational, and consistent with the real-transcript shorthand allowance. |

What is good:

- `5 -> 6` is a strong command/readback pair: the assignee compresses the order but preserves location, task, and constraint.
- `11`, `12`, `13`, `16` create realistic autonomous reporting instead of making command issue every next step explicitly.
- The scenario remains coherent in flattened transcript forms because unit identity is repeated inside most messages.

Critical issues:

- None.

Moderate issues:

- `16` reports that entrainment is still ongoing and not completed. Structurally this leaves the last active command loop unresolved at scenario end.

Minor issues:

- `1` is an `An Alle` broadcast without sequential acknowledgements. That is acceptable under the transcript notes, but it underuses the stricter multi-recipient rule pattern.

Verdict:

- Framework verdict: `PASS`
- Scenario pass/fail judgment: `PASS`

---

### S2 - Tiefgaragenbrand Wohnblock

| Criterion | Rating | Notes |
| --- | --- | --- |
| Message Structure Validity | PASS | Structure is clear across alerts, orders, readbacks, and updates. Even the free report in `2` remains recognizably radio-like. |
| Protocol Adherence | PASS | Orders in `3`, `4`, `9`, `12`, `15` receive direct acknowledgements in `6`, `5`, `10`, `13`, `16`. |
| Turn-Taking Plausibility | PASS | `2` is a plausible unsolicited size-up, and the later exchanges stay owned by the addressed units. |
| Communication Flow Realism | PARTIAL | The sequence is realistic overall, but `15 -> 16 -> 17` opens a continuing measurement thread that remains unresolved when the scenario ends. |
| Acknowledgement Patterns | PASS | Acknowledgements are compressed and clear, with some wording variation (`verstanden`, `korrekt`). |
| Communication Economy and Style | PASS | The scenario stays concise and task-focused without drifting into narrative speech. |

What is good:

- `3 -> 6 -> 7` and `4 -> 5 -> 8` are plausible short support-task control loops.
- `12 -> 13 -> 15 -> 16 -> 17` is structurally credible as a deferred assignment released after suppression progress.
- The scenario remains interpretable under `no_speaker` because locations, tasks, and units are mostly repeated in-message.

Critical issues:

- None.

Moderate issues:

- `17` explicitly states that the CO follow-up check is not complete, but the scenario ends there. This weakens structural closure.

Minor issues:

- `3` and `4` are issued back-to-back before any acknowledgement is heard. This is plausible, but it is a relatively neat synthetic control style repeated across the dataset.

Verdict:

- Framework verdict: `PASS`
- Scenario pass/fail judgment: `PASS`

---

### S3 - Kellerbrand Schulhaus

| Criterion | Rating | Notes |
| --- | --- | --- |
| Message Structure Validity | PASS | Sender, receiver, and intent remain recoverable in every turn. |
| Protocol Adherence | PASS | Orders in `2`, `3`, `7`, `12` are acknowledged or answered in clear form by `5`, `4`, `8`, `13`. |
| Turn-Taking Plausibility | PASS | Multiple units speak in plausible order without conflicting ownership of the same thread. |
| Communication Flow Realism | PASS | The transcript moves credibly from perimeter control and water supply into interior attack and final spread check. |
| Acknowledgement Patterns | PASS | Readbacks are brief but preserve the assigned task and location. |
| Communication Economy and Style | PASS | This is the most compressed and consistently radio-like scenario in the set. |

What is good:

- `7 -> 8 -> 10 -> 11 -> 12 -> 13` forms a strong multi-step operational thread with reconnaissance, partial completion, clarification, and final update.
- `6` and `9` are short but meaningful task-completion style reports from non-attack units, which improves realism.
- Nearly every message carries enough internal anchoring to survive transcript flattening.

Critical issues:

- None.

Moderate issues:

- None.

Minor issues:

- `2` and `3` are consecutive directed orders with acknowledgements arriving afterward in `4` and `5`. This is still acceptable, but again slightly cleaner than the noisier sequencing described in the source transcript notes.

Verdict:

- Framework verdict: `PASS`
- Scenario pass/fail judgment: `PASS`

---

### S4 - Werkstattbrand mit Gasflaschen

| Criterion | Rating | Notes |
| --- | --- | --- |
| Message Structure Validity | PARTIAL | Most turns are clear, but `14` is labeled as `Meldung` while functionally acting as a directed instruction, and `18` drops the normal address/message-type framing even though it gives a concrete directed continuation. |
| Protocol Adherence | PARTIAL | `14` behaves like a command but uses report framing; `18` gives a follow-up instruction without explicit address or turn allocation. Both remain interpretable, but they weaken protocol consistency. |
| Turn-Taking Plausibility | PASS | The relevant units respond on the threads they own, and no unit intrudes implausibly into another task thread. |
| Communication Flow Realism | PARTIAL | `11 -> 12 -> 13 -> 17 -> 18` shows a monitored-risk loop, but the loop is still active at the end and never reaches a closure or release point. |
| Acknowledgement Patterns | PASS | Acknowledgements are concise and stable; `15` is a credible short confirmation. |
| Communication Economy and Style | PASS | Style stays compressed and operational throughout. |

What is good:

- `7 -> 8 -> 11 -> 12 -> 13 -> 17 -> 18` models continuing supervision rather than a one-shot task, which is structurally useful.
- `9` and `16` are credible completion-style reports with explicit outcomes.
- The scenario stays understandable in flattened transcript form because the acting unit is almost always named inside the utterance.

Critical issues:

- None.

Moderate issues:

- `14` should structurally be a `Befehl` rather than a `Meldung`; the wording is directive, not informational.
- `17` says the cooling task is still incomplete, and `18` continues the task, but the scenario stops before the commanded closure message ever arrives.

Minor issues:

- `2` ends with `antworten`, but the immediate next transmission `3` goes to another unit before the response relevant to `2` arrives in `5`. This is still interpretable, but it introduces a slightly awkward turn handoff.

Verdict:

- Framework verdict: `PARTIAL`
- Scenario pass/fail judgment: `FAIL`

---

### S5 - Dachstockbrand Reihenhaus

| Criterion | Rating | Notes |
| --- | --- | --- |
| Message Structure Validity | PASS | Most turns are well formed, and the shorter field report in `3` is still clearly interpretable. |
| Protocol Adherence | PASS | Orders in `4`, `6`, `10`, `12`, `15` receive direct acknowledgements in `5`, `7`, `11`, `13`, `16`; `18 -> 19` is a plausible directed handover notice and acknowledgement. |
| Turn-Taking Plausibility | PASS | The right units answer each call, and the deferred handoff to `Sicherungstrupp` is explicitly managed. |
| Communication Flow Realism | PASS | The scenario moves plausibly through setup, opening-up, hotspot detection, extinguishment, final check, and handover. |
| Acknowledgement Patterns | PASS | There is useful variation between `verstanden`, `wiederholt`, and `korrekt` without losing clarity. |
| Communication Economy and Style | PASS | The messages stay short and radio-like even where they carry more detail. |

What is good:

- `12 -> 13 -> 14 -> 15 -> 16 -> 17` is the cleanest deferred-task-release sequence in the dataset.
- `18 -> 19` provides a credible tail after technical completion instead of ending abruptly.
- This scenario is especially robust under `continuous_transcript` because nearly every line repeats the acting unit or receiver.

Critical issues:

- None.

Moderate issues:

- None.

Minor issues:

- `3` omits explicit `An ... von ...` framing and a message-type label. This is acceptable under the real-transcript notes, but it is still shorthand rather than full protocol form.

Verdict:

- Framework verdict: `PASS`
- Scenario pass/fail judgment: `PASS`

---

## Dataset-Level Assessment

### Strengths

- All five scenarios are recognizably firefighter radio traffic rather than free-form narrative.
- The dataset consistently includes alerting, tasking, acknowledgements, autonomous progress reports, and completion-style reporting.
- Unit identity is usually repeated inside the utterances, so the scenarios remain readable under the intended flattened transcript representations.
- Communication economy is strong across the set: messages are short, direct, and operational.

### Cross-Dataset Critical Issues

- None. No scenario becomes uninterpretable under the allowed realism deviations.

### Cross-Dataset Moderate Issues

- Several scenarios end on unresolved active threads rather than on a closed communication loop. This occurs clearly in `S1` message `16`, `S2` message `17`, and `S4` messages `17-18`.
- Broadcast openings of the form `An Alle` are used as one-way framing only. The stricter sequential acknowledgement pattern from the speech rules is largely absent from the dataset.
- The dataset is cleaner than the source transcript notes in its control structure. Many exchanges use tidy command/readback blocks with limited interruption, repair, or partial misunderstanding.
- `S4` contains the clearest protocol-label inconsistency: message `14` is directive in function but marked as `Meldung`.

### Cross-Dataset Minor Issues

- Repair vocabulary from the source notes is barely represented. Forms such as `wiederholen`, `nicht verstanden`, or correction turns are rare.
- Back-to-back orders before acknowledgement appear in multiple scenarios (`S2`, `S3`) and contribute to a somewhat synthetic command cadence.
- Acknowledgement templates are valid but repetitive; many follow the same `Unit verstanden, task, Schluss` pattern.

### Coherence Under Intended Transcript Representations

- `structured_dialogue`: coherent across the full dataset.
- `no_speaker`: coherent overall because most messages name the acting unit or receiver in the text.
- `continuous_transcript`: still coherent, but robustness depends heavily on repeated in-text unit naming and would weaken if that redundancy were reduced.

### Overall Judgment

- Overall framework verdict: `PARTIAL`
- Overall pass/fail judgment: `FAIL`

The dataset is broadly usable from a structural perspective, but it does not fully pass a strict validation pass because one scenario (`S4`) falls to `PARTIAL`, and multiple scenarios end with open communication loops rather than explicit closure.

---

## Concrete Revision List

1. Revise `S4` message `14` so the utterance label matches its function. It should be framed as a directed instruction (`Befehl`) rather than a `Meldung`.
2. Revise `S4` message `18` to restore explicit direct-address structure, for example `An Wassertrupp von Einsatzleitung, Befehl: ...`, unless the dataset intentionally models a reduced-form commander acknowledgement there.
3. Add one short closure message to `S1` after message `16` so the active ventilation thread ends with either completion or an explicit hold/release state.
4. Add one short closure message to `S2` after message `17` so the measurement thread ends with either completion, continued exclusion, or a deferred follow-up instruction.
5. Add one short closure message to `S4` after message `18` so the cooling task reaches explicit completion or controlled continuation.
6. Decide whether `An Alle` broadcasts in this dataset are informational only or require ordered replies, and apply that choice consistently scenario by scenario.
7. Increase realism variety by adding a small amount of controlled protocol noise from the source notes, but keep interpretability intact. Use this sparingly rather than across every scenario.
8. Diversify acknowledgement wording so fewer readbacks use the same compact template.
