# STRUCTURE_VALIDATION_REPORT

## Scope and Method

This report evaluates only structural validity and communication realism, grounded strictly in:

- `./.agents/datasetgeneration/dataset_validation_structure.md`
- `./.agents/datasetgeneration/source_notes_sprechregeln.md`
- `./.agents/datasetgeneration/source_notes_real_transcript.md`

Operational correctness is intentionally excluded.

Pass/fail gate used in this report:

- `PASS` = scenario receives overall framework verdict `PASS`
- `FAIL` = scenario receives overall framework verdict `PARTIAL` or `FAIL`

Intended transcript representations checked for coherence:

- `structured_dialogue`
- `no_speaker`
- `continuous_transcript`

---

## Per-Scenario Assessment

### S1 - Kuechenbrand Mehrfamilienhaus

#### Criteria

| Criterion | Rating | Notes |
| --- | --- | --- |
| Message Structure Validity | PASS | Most turns are clearly radio-like, with explicit addressee/sender framing in messages 1, 4, 5, 7, 9, 14. |
| Protocol Adherence | PARTIAL | Commands are acknowledged well in 6, 8, 10, 15, but message 13 ends with `antworten` and receives no direct acknowledgement or confirmation. |
| Turn-Taking Plausibility | PASS | Directed commands are answered by the correct unit; sequencing around 5->6, 7->8, 9->10, 14->15 is plausible. |
| Communication Flow Realism | PASS | Good mix of alert, acknowledgement, tasking, status update, progress report, and partial completion. |
| Acknowledgement Patterns | PARTIAL | Acknowledgement behavior exists, but the expectation created in 13 is left hanging. |
| Communication Economy and Style | PASS | Short, compressed, operational phrasing throughout. |

#### What is good

- Message 5 -> 6 is a realistic directed order/readback pair.
- Message 11 gives a concise self-initiated completion update from the assigned unit.
- The scenario remains interpretable in all three transcript representations because most turns embed sender/receiver or unit identity directly in the text.

#### Critical issues

- None.

#### Moderate issues

- Message 13: `"An Einsatzleitung von Angriffstrupp, Meldung: Kuechenbrand mit Kleinloeschgeraet niedergeschlagen, Nachkontrolle laeuft, antworten"` requests a turn response but no direct reply follows. Message 14 is a new command to another unit, not a clear response to 13.

#### Minor issues

- Message 1 is an `An Alle` broadcast, but only some units acknowledge before new tasking starts. This is acceptable under the real-transcript notes, but it weakens the stricter multi-recipient pattern from the speech rules.

#### Transcript-representation coherence

- `structured_dialogue`: strong.
- `no_speaker`: still coherent because unit names are usually in-message.
- `continuous_transcript`: still readable due to repeated `Schluss` and `antworten`, but the unresolved `antworten` in 13 is more noticeable.

#### Verdict

- Framework verdict: `PASS`
- Scenario pass/fail judgment: `PASS`

---

### S2 - Tiefgaragenbrand Wohnblock

#### Criteria

| Criterion | Rating | Notes |
| --- | --- | --- |
| Message Structure Validity | PASS | Strong sender/receiver marking and clear speech-act types for most tasking turns. |
| Protocol Adherence | PASS | Commands in 3, 4, 9, 12 receive recognisable acknowledgements in 5, 6, 10, 13. |
| Turn-Taking Plausibility | PASS | Autonomous update in 2 is plausible; subsequent tasking and reports stay logically ordered. |
| Communication Flow Realism | PASS | Good interleaving of reconnaissance, safety measure, suppression, and measurement traffic. |
| Acknowledgement Patterns | PASS | Readbacks are compressed but consistent and non-contradictory. |
| Communication Economy and Style | PARTIAL | Message 6 is slightly conversational (`"Strom und Tor gehen wir an"`) compared with the otherwise compressed radio style. |

#### What is good

- Message 2 is a realistic early status report before detailed tasking.
- Messages 9 -> 10 -> 12 -> 13 form a plausible staged assignment, acknowledgement, release, and execution sequence for the measurement unit.
- Completion evidence remains interpretable under `no_speaker` and `continuous_transcript` because task names, locations, and units are repeated in-text.

#### Critical issues

- None.

#### Moderate issues

- None.

#### Minor issues

- Message 6 is less formulaic than the rest of the dataset and leans toward conversational phrasing rather than standardized compressed readback.

#### Transcript-representation coherence

- `structured_dialogue`: strong.
- `no_speaker`: strong, since unit names remain embedded in most lines.
- `continuous_transcript`: strong, because sequencing markers and repeated task/location references preserve interpretation.

#### Verdict

- Framework verdict: `PASS`
- Scenario pass/fail judgment: `PASS`

---

### S3 - Kellerbrand Schulhaus

#### Criteria

| Criterion | Rating | Notes |
| --- | --- | --- |
| Message Structure Validity | PASS | Clear sender/receiver identity and recognizable order/report format throughout. |
| Protocol Adherence | PASS | Commands are acknowledged; follow-up report in 13 closes the control loop created in 12. |
| Turn-Taking Plausibility | PASS | Multiple units report in plausible order without conflicting overlap. |
| Communication Flow Realism | PASS | Natural progression from perimeter control and water supply to reconnaissance, suppression, and confirmation. |
| Acknowledgement Patterns | PASS | Readbacks in 4, 5, 8 are concise but structurally sound. |
| Communication Economy and Style | PASS | Strong compression with enough specificity to remain interpretable. |

#### What is good

- This is the cleanest scenario structurally.
- Messages 7 -> 8 -> 10 -> 11 -> 12 -> 13 form a convincing radio progression of assignment, acknowledgement, on-scene finding, partial completion, clarification order, and final status.
- The scenario survives `no_speaker` and `continuous_transcript` well because almost every message carries explicit internal role anchoring.

#### Critical issues

- None.

#### Moderate issues

- None.

#### Minor issues

- Messages 2 and 3 are consecutive commands with both acknowledgements delayed until 4 and 5. This is still realistic, but slightly more ordered confirmation would align better with the strict speech-rule template.

#### Transcript-representation coherence

- `structured_dialogue`: very strong.
- `no_speaker`: very strong.
- `continuous_transcript`: strong; message boundaries remain recoverable from phrasing and closures.

#### Verdict

- Framework verdict: `PASS`
- Scenario pass/fail judgment: `PASS`

---

### S4 - Werkstattbrand mit Gasflaschen

#### Criteria

| Criterion | Rating | Notes |
| --- | --- | --- |
| Message Structure Validity | PASS | Core structure is clear and messages are interpretable as radio turns. |
| Protocol Adherence | PARTIAL | Command 11 is acknowledged in 12, but it omits `antworten` despite requiring a response under the stricter rules. |
| Turn-Taking Plausibility | PASS | Unit traffic is assigned cleanly and reports come from the relevant roles. |
| Communication Flow Realism | PARTIAL | The cooling task remains open-ended, but the transcript ends without a later status showing whether the reiterated command in 11 changed state. |
| Acknowledgement Patterns | PASS | Directed orders generally receive short but acceptable acknowledgements. |
| Communication Economy and Style | PASS | Phrasing is concise and operational. |

#### What is good

- Messages 6 -> 7 -> 10 -> 11 -> 12 show a plausible monitored-risk workflow with reassessment and continuation order.
- Message 8 is a good short completion report for a traffic/perimeter task.
- The scenario stays coherent under `no_speaker` because the key units are named inside the utterances.

#### Critical issues

- None.

#### Moderate issues

- Message 11: `"An Wassertrupp von Einsatzleitung, Befehl: Kuehlung weiterfuehren bis beide Flaschen kalt gemeldet sind, Schluss"` is a command that expects continued compliance, but it drops `antworten` while still receiving a confirmation in 12. This creates a small protocol mismatch.
- The transcript ends after message 14 without any later update on the still-open gas-cylinder cooling thread. This is not an operational criticism; structurally it leaves the last control loop underdeveloped relative to the rest of the dataset.

#### Minor issues

- Message 13 is a broadcast restriction message with no follow-up acknowledgement from the unit most likely to enforce it. This is acceptable realism noise, but it contributes to uneven broadcast discipline across the dataset.

#### Transcript-representation coherence

- `structured_dialogue`: strong.
- `no_speaker`: strong enough; unit identities are mostly text-internal.
- `continuous_transcript`: still coherent, but the unresolved cooling thread is more apparent when all turns are flattened.

#### Verdict

- Framework verdict: `PASS`
- Scenario pass/fail judgment: `PASS`

---

### S5 - Dachstockbrand Reihenhaus

#### Criteria

| Criterion | Rating | Notes |
| --- | --- | --- |
| Message Structure Validity | PASS | Most turns are well-formed; compressed field report in 3 is still interpretable. |
| Protocol Adherence | PARTIAL | Messages 10 and 11 establish `Schlusskontrolle` only `nach Abschluss Angriffstrupp`, but no explicit release command follows before completion report 13. |
| Turn-Taking Plausibility | PARTIAL | Message 13 is plausible only by inference from 12; the handoff condition is not explicitly voiced. |
| Communication Flow Realism | PASS | Progression from initial arrival to ladder setup, hotspot search, control, final check, and handover is realistic. |
| Acknowledgement Patterns | PASS | Commands receive recognizable acknowledgements in 5, 7, 11, 15. |
| Communication Economy and Style | PASS | Mostly concise and suitably compressed. |

#### What is good

- Message 3 is a realistic terse self-initiated field update.
- Message 12 provides a strong completion-style signal for the attack task and supports later stabilization.
- Messages 14 -> 15 add a realistic handover tail, which improves end-of-incident communication flow.

#### Critical issues

- None.

#### Moderate issues

- Messages 10 -> 11 assign the final check only after attack-team completion, but message 13 reports that final check as done without an explicit release or start message from `Sicherungstrupp`. The inference is possible from 12, but the turn transition is not cleanly voiced.

#### Minor issues

- Message 3 lacks explicit `An ... von ...` framing and message type label. This is allowed under the real-transcript notes, but it is another example of the dataset leaning on compressed shorthand rather than balanced variation.

#### Transcript-representation coherence

- `structured_dialogue`: strong.
- `no_speaker`: still coherent because `Angriffstrupp` is named in 3 and most other turns embed units explicitly.
- `continuous_transcript`: coherent, but the implicit handoff from 12 to 13 is easier to miss once speaker labels and line breaks disappear.

#### Verdict

- Framework verdict: `PASS`
- Scenario pass/fail judgment: `PASS`

---

## Dataset-Level Assessment

### Overall structural strengths

- All five scenarios are interpretable as firefighter radio traffic rather than free-form narrative.
- The dataset consistently uses a realistic mix of broadcast alert, directed tasking, acknowledgement, progress report, and completion-style reporting.
- Most commands are acknowledged by the addressed unit with compressed but recognizable readbacks.
- Unit/task/location references are repeated often enough that the scenarios remain coherent under `structured_dialogue`, `no_speaker`, and usually also `continuous_transcript`.
- The dataset generally respects communication economy: messages are short, direct, and operational.

### Cross-dataset critical issues

- None. There is no scenario with a structural breakdown severe enough to make turns uninterpretable.

### Cross-dataset moderate issues

- Recurrent unresolved or weakly closed control loops:
  - S1 message 13 ends with `antworten` but receives no direct response.
  - S5 messages 10 -> 13 rely on implicit rather than explicit release of the final-check unit.
  - S4 message 11 restarts/continues a control loop, but the scenario ends before that thread gets another visible state update.
- Broadcast discipline is inconsistent:
  - some `An Alle` turns behave like one-way information broadcasts,
  - others implicitly expect actor uptake without explicit acknowledgements,
  - the dataset does not use a stable pattern for when broad recipients should or should not answer.
- The dataset slightly over-favors clean single-turn command/readback pairs and underuses realistic protocol repair signals such as `wiederholen`, `nicht verstanden`, `falsch ich wiederhole`, or explicit confirmation from command after a key report.

### Cross-dataset minor issues

- Some acknowledgements are more conversational than formulaic, especially S2 message 6.
- There is repeated reliance on unit names inside the text to preserve coherence under `no_speaker`; this works, but it also means the raw message design is somewhat optimized for downstream representation robustness rather than purely natural variation.
- Several scenarios are very clean and low-noise compared with the real-transcript notes. This is not invalid, but it reduces realism diversity.

### Coherence under intended transcript representations

- `structured_dialogue`: dataset is consistently coherent.
- `no_speaker`: dataset remains coherent because many messages explicitly restate the acting unit in the text itself.
- `continuous_transcript`: still mostly coherent, but the weakest points are exactly where response expectation or handoff is only implicit. These flattened views amplify unresolved `antworten` markers and implicit task-release transitions.

### Overall judgment

- Overall framework verdict: `PASS`
- Overall pass/fail judgment: `PASS`

The dataset is structurally valid and usable for transcript-based evaluation, but it would benefit from tightening several repeated protocol-edge cases so that the realism remains robust even when speaker labels and line breaks are removed.

---

## Concrete Revision List

1. Fix unresolved response prompts. Any message ending in `antworten` should be followed by a direct acknowledgement, confirmation, or explicit reason for no reply.
2. Make deferred task releases explicit. When a task is assigned `nach Freigabe` or `nach Abschluss` of another unit, add a short release or start message before the completion report.
3. Normalize broadcast behavior. Decide per scenario whether `An Alle` is a one-way information message or a turn-allocating call, and write follow-up acknowledgements consistently.
4. Tighten command-response symmetry. If a command clearly expects confirmation, include `antworten`; if it is truly one-way, avoid a later confirmation that was never solicited unless the unit is self-initiating.
5. Add a small amount of realistic protocol repair variety. Introduce occasional but controlled uses of `wiederholen`, `korrekt`, `richtig`, or partial clarifications without reducing interpretability.
6. Keep at least one explicit closure of every major communication thread before scenario end, especially for incomplete tasks that receive reiterated orders.
7. Preserve current brevity, but replace the few conversational readbacks with slightly more radio-like compressed formulations.

