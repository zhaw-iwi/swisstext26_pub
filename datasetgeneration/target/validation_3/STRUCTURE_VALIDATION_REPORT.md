# Structure Validation Report

Dataset: `synthetic_firefighter_radio_controlled_v1`  
Scope: structural validity and communication realism only  
Grounding sources: `dataset_validation_structure.md`, `source_notes_sprechregeln.md`, `source_notes_real_transcript.md`

## Evaluation Summary

Pass/fail rule used for this report:
- `PASS` if the scenario's overall verdict is `PASS`
- `FAIL` if the scenario's overall verdict is `PARTIAL` or `FAIL`

| Scenario | Overall verdict | Pass/fail judgment |
|---|---|---|
| S1 | PASS | PASS |
| S2 | PASS | PASS |
| S3 | PASS | PASS |
| S4 | PASS | PASS |
| S5 | PASS | PASS |

Overall dataset verdict: `PASS`  
Overall dataset pass/fail judgment: `PASS`

## Per-Scenario Assessment

### S1 - Kuechenbrand Mehrfamilienhaus

Criteria:

| Criterion | Rating | Notes |
|---|---|---|
| Message Structure Validity | PASS | Most turns have clear sender/receiver structure or are still interpretable as compressed radio replies. |
| Protocol Adherence | PASS | Directed commands in `5`, `7`, `9`, `13` are acknowledged in `6`, `8`, `10`, `14`. |
| Turn-Taking Plausibility | PASS | Units respond to their own calls and assignments without implausible cross-talk. |
| Communication Flow Realism | PASS | The sequence mixes tasking, acknowledgement, progress, and partial completion in a plausible incident progression. |
| Acknowledgement Patterns | PASS | Readbacks are compressed but preserve the operational core. |
| Communication Economy and Style | PASS | Messages are short and mostly formulaic, with longer descriptive turns only where justified. |

Critical issues:
- None.

Moderate issues:
- `10`: "Lueftungstrupp verstanden, Ueberdruckbeluefter steht am Eingang, Schluss" acknowledges the order and simultaneously reports completion. This is still interpretable, but it compresses two phases into one turn and reduces the clearer call-confirm-execute pattern seen in the source notes.

Minor issues:
- `1`: broadcast to `Alle` is not followed by acknowledgements from all initially addressed parties. This is acceptable under the real-transcript notes, but it makes the opening slightly more schematic than a fully traced multi-party exchange.
- `2`, `3`, `8`, `10`, `14`: replies omit explicit receiver naming and message-type labels. This is acceptable variation, but it weakens strict protocol traceability.

What is good:
- `4`, `5`, `6` form a plausible contact-report-command-readback sequence.
- `11`, `12`, `15` provide evidence-based status updates rather than narrative exposition.
- The scenario remains coherent even under compressed transcript representations because speaker identity and task state stay recoverable turn by turn.

Scenario verdict: `PASS`  
Pass/fail judgment: `PASS`

### S2 - Tiefgaragenbrand Wohnblock

Criteria:

| Criterion | Rating | Notes |
|---|---|---|
| Message Structure Validity | PASS | Most turns are interpretable radio utterances with identifiable intent. |
| Protocol Adherence | PARTIAL | One directed command is followed by reporting instead of a clear acknowledgement, but the exchange remains interpretable. |
| Turn-Taking Plausibility | PASS | Responses come from the addressed units and the incident flow is readable. |
| Communication Flow Realism | PASS | The scenario mixes initial observation, tasking, suppression progress, and monitoring well. |
| Acknowledgement Patterns | PARTIAL | Acknowledgements exist for most commands, but one command chain is incomplete. |
| Communication Economy and Style | PASS | Short, compressed phrasing is maintained without drifting into narrative prose. |

Critical issues:
- None.

Moderate issues:
- `12` -> `13`: `Einsatzleitung` issues a directed `Befehl` to `Messgruppe` in `12`, but `13` is only a report. The expected acknowledgement layer is skipped. This does not break interpretation, but it is a concrete protocol gap.
- `2`: "Angriffstrupp vor Ort, Sicht in der Rampe schlecht, keine Personen sichtbar" has no explicit receiver, no message-type marker, and no `Schluss`. The real-transcript notes allow this kind of compression, but it is structurally weaker than the rest of the scenario.

Minor issues:
- `3` and `4` are back-to-back commands from `Einsatzleitung` before any acknowledgement arrives. This is still plausible radio traffic, but it produces a slightly more staged sequence than the source notes' idealized turn allocation.
- `10`: "Messgruppe korrekt" is interpretable as acknowledgement, but the phrasing is terser than the more standard `verstanden` pattern.

What is good:
- `7`, `8`, `11`, `13`, `14` create a realistic interleaving of electrical isolation, suppression updates, air monitoring, and final knockdown.
- `8` and `11` show incremental progress reporting rather than a single artificial completion jump.
- The scenario stays coherent in transcript-like form because the unit-first reports are still attributable and state transitions are observable.

Scenario verdict: `PASS`  
Pass/fail judgment: `PASS`

### S3 - Kellerbrand Schulhaus

Criteria:

| Criterion | Rating | Notes |
|---|---|---|
| Message Structure Validity | PASS | Message structure is consistently recognizable and easy to parse. |
| Protocol Adherence | PASS | Commands are acknowledged and follow-up reporting is logically tied to prior tasking. |
| Turn-Taking Plausibility | PASS | Directed units answer, and no irrelevant unit intrudes into another exchange. |
| Communication Flow Realism | PASS | The scenario progresses through securing, supply, entry, knockdown, and control update in a plausible order. |
| Acknowledgement Patterns | PASS | Readbacks are short but adequate. |
| Communication Economy and Style | PASS | The language is compressed and radio-like throughout. |

Critical issues:
- None.

Moderate issues:
- None.

Minor issues:
- `2`, `3`, `7` are a clean sequence of command dispatches followed by acknowledgements in `4`, `5`, `8`. This is valid, but overall the scenario is somewhat tidier and more sequential than the noisier interleaving described in the real transcript notes.
- `12` -> `13` is structurally correct, but the command is mainly a prompt for a final state already being worked on. It reads slightly synthetic because the update could also have emerged as a self-initiated completion report.

What is good:
- `6`, `9`, `10`, `11`, `13` provide a credible progression from securing the perimeter to hose readiness to suppression and spread control.
- `8` is a strong compressed readback that preserves task, route, and equipment.
- This scenario is the strongest structurally because it balances protocol clarity with realistic brevity and remains robust under transcript compression.

Scenario verdict: `PASS`  
Pass/fail judgment: `PASS`

### S4 - Werkstattbrand mit Gasflaschen

Criteria:

| Criterion | Rating | Notes |
|---|---|---|
| Message Structure Validity | PASS | Messages remain interpretable and mostly follow radio structure. |
| Protocol Adherence | PARTIAL | One explicit command is not acknowledged, though the meaning remains recoverable. |
| Turn-Taking Plausibility | PASS | Units report only on their own assigned domain and the order of updates is plausible. |
| Communication Flow Realism | PASS | Traffic includes perimeter control, suppression, cooling, and access restriction in a believable mix. |
| Acknowledgement Patterns | PARTIAL | Most commands are acknowledged, but not all. |
| Communication Economy and Style | PASS | Phrasing is compressed and operational. |

Critical issues:
- None.

Moderate issues:
- `11`: "An Wassertrupp von Einsatzleitung, Befehl: Kuehlung weiterfuehren bis beide Flaschen kalt gemeldet sind, Schluss" is a direct command but there is no acknowledgement from `Wassertrupp`. Since command acknowledgements are a key structural expectation in the guidance, this is a concrete protocol miss.

Minor issues:
- `12`: broadcast restriction to `Alle` receives no visible acknowledgement. This is acceptable under the real-transcript notes, but it reduces explicit turn closure.
- `10`: "wir bleiben drauf" is understandable field shorthand, but it is looser and more conversational than the more formulaic style used elsewhere in the dataset.

What is good:
- `8`, `9`, `10` interleave traffic-management, suppression, and cooling updates in a realistic way.
- `9` and `13` show incremental completion evidence instead of a single abrupt task completion.
- The scenario stays coherent under transcript representation because the role-task mapping is stable and the status transitions are easy to infer.

Scenario verdict: `PASS`  
Pass/fail judgment: `PASS`

### S5 - Dachstockbrand Reihenhaus

Criteria:

| Criterion | Rating | Notes |
|---|---|---|
| Message Structure Validity | PASS | The scenario is structurally clear even where messages are compressed. |
| Protocol Adherence | PASS | Directed commands in `4`, `6`, `10` are acknowledged in `5`, `7`, `11`. |
| Turn-Taking Plausibility | PASS | The participating units answer only for their own tasks and in a plausible sequence. |
| Communication Flow Realism | PASS | The flow from access setup to opening, suppression, final control, and handover is coherent. |
| Acknowledgement Patterns | PASS | Acknowledgements are short but consistently tied to preceding commands. |
| Communication Economy and Style | PASS | The style is concise and operational, with descriptive length only where needed. |

Critical issues:
- None.

Moderate issues:
- None.

Minor issues:
- `2`: "Drehleiter rueckt rueckseitig an, Schluss" has no explicit receiver or message-type marker. It remains realistic as a self-initiated status line, but it is structurally lighter than the protocol ideal.
- `14`: "An Polizei von Einsatzleitung, Meldung: Einsatzstelle nach Schlusskontrolle zur Uebergabe bereit, Schluss" is a one-sided closing transmission without an observed reply. This is interpretable, but the handover would be slightly stronger structurally with a confirming acknowledgement.

What is good:
- `8`, `9`, `12`, `13` give a believable sequence of setup, intermediate finding, extinguishment, and final negative control.
- `10` is a good example of conditional tasking that still remains concise.
- The scenario remains coherent in transcript form because completion evidence is explicit and unit ownership of each task is stable.

Scenario verdict: `PASS`  
Pass/fail judgment: `PASS`

## Dataset-Level Assessment

### Strengths

- All five scenarios remain interpretable as radio traffic. None contains free-form narrative or meta text that would break transcript realism.
- Speaker intent is usually easy to recover because the dataset consistently uses identifiable unit names and operationally grounded short forms.
- The dataset reflects the intended transcript representation reasonably well: many messages are compressed, some omit full formal structure, and the traffic still stays understandable.
- Task progression is generally realistic at a structural level: initial scene message, assignment, acknowledgement, progress update, and completion or partial completion.
- Units usually speak within their own responsibility area, which helps communication coherence.

### Cross-Dataset Patterns That Need Attention

Critical patterns:
- None.

Moderate patterns:
- Several scenarios still rely on very clean command-response blocks. Compared with the real transcript notes, the dataset is somewhat over-ordered and less noisy than authentic radio traffic.
- Some directed `Befehl` turns are not followed by a distinct acknowledgement layer. The clearest cases are `S2:12` and `S4:11`.
- Self-initiated status lines sometimes drop too many formal markers at once. Examples include `S2:2`, `S5:2`, and to a lesser extent some short acknowledgements across the set.

Minor patterns:
- Broadcasts to `Alle` rarely receive visible follow-up, which is acceptable but makes some openings feel schematic.
- Many acknowledgements use the same compact pattern (`verstanden ... Schluss`). This is valid, but slightly repetitive across the dataset.
- The dataset contains little protocol noise beyond marker omission. Real transcript notes suggest more varied imperfections, paraphrases, and occasional unevenness.

### Overall Judgment

The dataset passes structural validation. The main reason is that all scenarios remain interpretable, role-consistent, and plausible as compressed firefighter radio traffic. The recurring weaknesses are not severe enough to break interpretation, but they do show a synthetic bias toward tidy sequencing and slightly under-modeled acknowledgement variability.

Overall verdict: `PASS`  
Overall pass/fail judgment: `PASS`

## Concrete Revision List

1. Add an explicit acknowledgement turn after every directed `Befehl` that currently jumps straight to a report. Priority fixes: `S2:12` and `S4:11`.
2. For self-initiated status messages that omit receiver, message type, and closure all at once, restore at least one structural anchor. Priority fix: `S2:2`; optional consistency fix: `S5:2`.
3. Increase transcript realism by adding a small amount of controlled protocol noise rather than keeping all scenarios equally clean. Use omissions selectively, not uniformly.
4. Vary acknowledgement forms across scenarios using source-supported alternatives such as `verstanden`, `korrekt`, paraphrased readbacks, and occasional shortened confirmations.
5. In at least some scenarios, interleave autonomous status updates more irregularly with command traffic to reduce the synthetic command-block pattern.
6. Where a broadcast to `Alle` is operationally important, consider adding one or two visible follow-up acknowledgements or a later confirming update so the channel flow looks less staged.
7. Preserve current strengths during revision: short unit-first status lines, evidence-based completion reports, and stable mapping between unit role and reported information.
