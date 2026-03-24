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

Operational correctness is intentionally excluded.

Pass/fail rule used here:

- Scenario pass/fail judgment = `PASS` only if the framework verdict is `PASS`
- Scenario pass/fail judgment = `FAIL` if the framework verdict is `PARTIAL` or `FAIL`

---

## Per-Scenario Assessment

### S1 - Kuechenbrand Mehrfamilienhaus

| Criterion | Rating | Notes |
| --- | --- | --- |
| Message Structure Validity | PASS | Messages `1`, `4`, `5`, `7`, `9`, `14`, `16` use clear radio framing; the shorter acknowledgements in `2`, `3`, `8`, `10`, `15` are still interpretable. |
| Protocol Adherence | PASS | Directed commands in `5`, `7`, `9`, `14` are acknowledged by the addressed unit in `6`, `8`, `10`, `15`. |
| Turn-Taking Plausibility | PASS | Request-response order is clear and only the called unit answers the directed orders. |
| Communication Flow Realism | PASS | The scenario mixes initial alert, arrival report, tasking, supply confirmation, search result, suppression progress, and ventilation update in plausible sequence. |
| Acknowledgement Patterns | PASS | Readbacks are short but preserve the operational core of each command. |
| Communication Economy and Style | PASS | Phrasing stays compressed and operational throughout. |

What is good:

- `5 -> 6` is a strong command/readback pair with a plausible compressed repetition.
- `11`, `12`, `13`, `16` provide self-initiated updates from the executing units rather than making command traffic do all the work.
- The scenario remains coherent under `no_speaker` and `continuous_transcript` because unit identity is repeated inside most utterances.

Critical issues:

- None.

Moderate issues:

- None.

Minor issues:

- `1` is an `An Alle` broadcast with no ordered acknowledgement collection. This is acceptable under the real-transcript notes, but it means the dataset does not exercise the stricter multi-recipient protocol pattern here.

Verdict:

- Framework verdict: `PASS`
- Scenario pass/fail judgment: `PASS`

---

### S2 - Tiefgaragenbrand Wohnblock

| Criterion | Rating | Notes |
| --- | --- | --- |
| Message Structure Validity | PASS | Structure is clear across alerts, orders, readbacks, and reports; even the free report in `2` remains recognizably radio-like. |
| Protocol Adherence | PASS | Commands in `3`, `4`, `9`, `12`, `15` receive direct acknowledgements in `6`, `5`, `10`, `13`, `16`. |
| Turn-Taking Plausibility | PASS | `2` is a plausible unsolicited size-up; later responses come from the addressed units and the order of events is easy to follow. |
| Communication Flow Realism | PASS | The transcript interleaves reconnaissance, safety setup, supply, suppression, and measurement in a realistic way. |
| Acknowledgement Patterns | PASS | Readbacks are compressed and non-contradictory. |
| Communication Economy and Style | PASS | Messages are short, direct, and avoid narrative wording. |

What is good:

- `3 -> 6 -> 7` and `4 -> 5 -> 8` are credible short control loops for support tasks.
- `12 -> 13 -> 15 -> 16 -> 17` is structurally strong because the measurement task is assigned early, held pending, then explicitly released.
- The scenario is robust under transcript flattening because locations, units, and task states are repeated in-message.

Critical issues:

- None.

Moderate issues:

- None.

Minor issues:

- `3` and `4` are issued back-to-back before any acknowledgement is heard. This is still plausible under stress and does not break interpretation, but it is a slightly tidy synthetic pattern repeated elsewhere in the dataset.

Verdict:

- Framework verdict: `PASS`
- Scenario pass/fail judgment: `PASS`

---

### S3 - Kellerbrand Schulhaus

| Criterion | Rating | Notes |
| --- | --- | --- |
| Message Structure Validity | PASS | The scenario keeps sender, receiver, and intent recoverable almost everywhere. |
| Protocol Adherence | PASS | Orders in `2`, `3`, `7`, `12` are acknowledged or answered in recognisable form by `5`, `4`, `8`, `13`. |
| Turn-Taking Plausibility | PASS | Multiple units speak in plausible order without conflicting overlap. |
| Communication Flow Realism | PASS | The sequence moves naturally from perimeter control and water supply into interior attack and final spread check. |
| Acknowledgement Patterns | PASS | Readbacks are brief but preserve the assigned task. |
| Communication Economy and Style | PASS | This is one of the cleanest examples of compressed radio style in the set. |

What is good:

- `7 -> 8 -> 10 -> 11 -> 12 -> 13` is an especially coherent chain of assignment, readback, first finding, partial result, clarification order, and final status.
- `6` and `9` give short task-completion style reports from non-attack units, which improves flow realism.
- Nearly every message contains enough internal anchoring to survive `no_speaker`.

Critical issues:

- None.

Moderate issues:

- None.

Minor issues:

- `2` and `3` are consecutive orders with delayed acknowledgements in `4` and `5`. This is acceptable realism noise, but a stricter protocol rendering would usually resolve one directed order before the next.

Verdict:

- Framework verdict: `PASS`
- Scenario pass/fail judgment: `PASS`

---

### S4 - Werkstattbrand mit Gasflaschen

| Criterion | Rating | Notes |
| --- | --- | --- |
| Message Structure Validity | PASS | Messages are clearly interpretable as radio turns and unit ownership stays stable. |
| Protocol Adherence | PASS | Directed commands in `2`, `4`, `6`, `11`, `13` are acknowledged in `3`, `5`, `7`, `12`, `14`. |
| Turn-Taking Plausibility | PASS | The relevant units speak on the threads they own, and the command/reply order is understandable. |
| Communication Flow Realism | PARTIAL | The cooling thread remains active through `10`, `11`, `12`, `16`, but the scenario stops before that reiterated control loop gets any further visible state change. |
| Acknowledgement Patterns | PASS | Acknowledgement behavior is consistent and compressed. |
| Communication Economy and Style | PASS | Style stays concise and operational. |

What is good:

- `6 -> 7 -> 10 -> 11 -> 12 -> 16` shows monitored-risk communication rather than a single one-shot task.
- `8` and `15` are strong completion-style reports with explicit outcome phrasing.
- The scenario remains coherent under the intended transcript representations because the key acting units are named in the message text.

Critical issues:

- None.

Moderate issues:

- `11` reiterates the cooling order and `16` still reports partial progress, but the transcript ends there. Structurally this leaves the last active command loop less closed than the others in the dataset.

Minor issues:

- The scenario is somewhat more sequential than the real-transcript notes suggest; command blocks and acknowledgements are very clean.

Verdict:

- Framework verdict: `PASS`
- Scenario pass/fail judgment: `PASS`

---

### S5 - Dachstockbrand Reihenhaus

| Criterion | Rating | Notes |
| --- | --- | --- |
| Message Structure Validity | PASS | Most turns are well formed; the shorter field report in `3` still has clear operational intent. |
| Protocol Adherence | PASS | Orders in `4`, `6`, `10`, `12`, `15`, `18` receive direct acknowledgements or follow-up responses in `5`, `7`, `11`, `13`, `16`, `19`. |
| Turn-Taking Plausibility | PASS | The handoff from attack task to final control is explicitly voiced and the right units answer each call. |
| Communication Flow Realism | PASS | The scenario moves plausibly through ladder setup, opening-up, hotspot detection, extinguishment, final control, and handover. |
| Acknowledgement Patterns | PASS | There is good variation between `verstanden`, `wiederholt`, and `korrekt` without losing clarity. |
| Communication Economy and Style | PASS | Messages remain short and radio-like even when carrying more detail. |

What is good:

- `12 -> 13 -> 14 -> 15 -> 16 -> 17` is the strongest deferred-task release sequence in the dataset.
- `18 -> 19` adds a credible handover tail rather than stopping immediately after the technical task is done.
- This scenario stays especially robust under `continuous_transcript` because almost every line includes strong speaker or receiver cues.

Critical issues:

- None.

Moderate issues:

- None.

Minor issues:

- `3` omits explicit `An ... von ...` framing and a message-type label. This is acceptable under the real-transcript notes, but it is another example of controlled shorthand rather than full protocol form.

Verdict:

- Framework verdict: `PASS`
- Scenario pass/fail judgment: `PASS`

---

## Dataset-Level Assessment

### Strengths

- All five scenarios are clearly interpretable as firefighter radio traffic rather than free-form narrative.
- The dataset consistently mixes alerting, directed tasking, acknowledgements, autonomous status reports, progress updates, and completion-style messages.
- Speaker intent is usually easy to recover because unit names and operational roles are repeated inside the utterances themselves.
- The set remains coherent under the intended transcript representations, especially `structured_dialogue` and `no_speaker`.
- Communication economy is strong across the dataset: messages are short, direct, and operational.

### Cross-Dataset Critical Issues

- None. No scenario contains a structural breakdown severe enough to make the traffic uninterpretable.

### Cross-Dataset Moderate Issues

- The dataset is still somewhat too tidy compared with the real-transcript notes. Many scenarios rely on clean command/readback blocks with little interruption, repair, or overlap.
- Multi-recipient protocol is under-modeled. Broadcast openings such as `An Alle` are used as one-way situational framing, but the stricter sequential acknowledgement pattern from the speech rules is mostly absent.
- Some scenarios stop while an active communication loop is still open. The clearest case is `S4`, where message `11` is reiterated in `12` and only partial progress is reported in `16` before the scenario ends.

### Cross-Dataset Minor Issues

- There is limited protocol-repair variety. The dataset rarely uses source-supported forms such as `wiederholen`, `nicht verstanden`, `falsch ich wiederhole`, or explicit commander confirmation after a key report.
- Acknowledgement phrasing is valid but somewhat repetitive across the set; many readbacks follow the same `Unit verstanden, task, Schluss` pattern.
- Several scenarios are cleaner and lower-noise than the source transcript notes. This does not invalidate them, but it narrows realism diversity.

### Coherence Under Intended Transcript Representations

- `structured_dialogue`: consistently coherent.
- `no_speaker`: coherent because most messages name the acting unit or receiver in the text.
- `continuous_transcript`: still coherent overall, but the dataset depends on repeated in-text unit naming to stay robust when speaker labels disappear.

### Overall Judgment

- Overall framework verdict: `PASS`
- Overall pass/fail judgment: `PASS`

The dataset is structurally valid for the intended transcript-style use. The main remaining weakness is not interpretability but synthetic neatness: protocol is generally clear, yet often cleaner and more orderly than the variability described in the source transcript notes.

---

## Concrete Revision List

1. Add a small amount of controlled protocol noise to selected scenarios so the dataset does not over-concentrate on clean command/readback pairs.
2. Decide whether `An Alle` broadcasts are purely informational or should trigger ordered replies, and apply that choice consistently within each scenario.
3. Where a scenario ends with an actively monitored thread, add one more short state update or explicit closure so the final control loop is structurally complete.
4. Increase acknowledgement variety using source-supported alternatives such as `korrekt`, `richtig`, paraphrased readbacks, and occasional repair turns.
5. Preserve the current brevity and transcript robustness, but avoid making every acknowledgement follow the same compact template.
