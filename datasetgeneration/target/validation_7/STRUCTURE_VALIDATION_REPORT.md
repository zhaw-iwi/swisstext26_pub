# Structure Validation Report

Dataset: `synthetic_firefighter_radio_controlled_v1`  
Scope: structural validity and communication realism only  
Sources used: `dataset_validation_structure.md`, `source_notes_sprechregeln.md`, `source_notes_real_transcript.md`

## Rating Convention

- Criterion ratings: `PASS`, `PARTIAL`, `FAIL`
- Scenario verdicts follow the source framework: `PASS`, `PARTIAL`, `FAIL`
- Pass/fail judgment below is binary:
  - `PASS` only if scenario verdict is `PASS`
  - `FAIL` if scenario verdict is `PARTIAL` or `FAIL`

## Scenario S1: Kuechenbrand Mehrfamilienhaus

### Criterion Ratings

- Message Structure Validity: `PASS`
- Protocol Adherence: `PARTIAL`
- Turn-Taking Plausibility: `PASS`
- Communication Flow Realism: `PASS`
- Acknowledgement Patterns: `PARTIAL`
- Communication Economy and Style: `PASS`

### Assessment

Good:
- Clear command and report chain with recognizable radio structure throughout.
- Message ids `5` -> `6`, `7` -> `8`, `9` -> `10`, `14` -> `15` show plausible directed command acknowledgement behavior.
- The flow includes assignment, acknowledgement, task progress, completion, and continued monitoring. That matches the source notes well.
- Language stays compressed and operational. Most turns are short enough to work as radio traffic.

Moderate issues:
- `id 17`: `"An Lueftungstrupp von Einsatzleitung, Meldung: Entrauchung fortsetzen..."` is functionally a directive but is labeled as `Meldung` and receives no acknowledgement. This weakens protocol consistency because the text behaves like a renewed tasking rather than a pure report.

Minor issues:
- `id 1`: `"An Alle..."` is a broad alert, but only some units acknowledge later and not as a coordinated sequence. This is still acceptable under the real-transcript guidance, but it is cleaner than realistic and not fully aligned with the strict multi-recipient ideal.
- `ids 12` and `13` are slightly repetitive status updates from the same unit. They remain interpretable, but the repetition feels generator-shaped rather than naturally opportunistic.

### Scenario Verdict

- Overall verdict: `PASS`
- Pass/fail judgment: `PASS`

## Scenario S2: Tiefgaragenbrand Wohnblock

### Criterion Ratings

- Message Structure Validity: `PASS`
- Protocol Adherence: `PARTIAL`
- Turn-Taking Plausibility: `PASS`
- Communication Flow Realism: `PASS`
- Acknowledgement Patterns: `PARTIAL`
- Communication Economy and Style: `PASS`

### Assessment

Good:
- Strong interleaving of subordinate units. `ids 7`, `8`, `11`, `14`, `17`, `18` create a believable parallel incident picture instead of a single linear dialogue.
- Commands are usually acknowledged and then converted into short progress reports. `ids 9` -> `10` -> `11` and `15` -> `16` -> `17` are structurally plausible.
- The style is concise and operational, with good use of short state phrases.

Moderate issues:
- `id 19`: `"An Messgruppe von Einsatzleitung, Meldung: Bereich Vorraum und Rampe bleibt gesperrt, Nachkontrolle bei freier Sicht fortsetzen, Schluss"` again functions like a directive while being labeled as `Meldung`, and there is no acknowledgement. This is the clearest protocol inconsistency in the scenario.

Minor issues:
- `ids 3` and `4` are issued in sequence, but acknowledgements arrive in reverse order at `ids 5` and `6`. This is still plausible under live traffic pressure, but it adds mild sequencing looseness.
- The scenario is realistic enough, but the turns are very cleanly segmented and lack the small protocol irregularities seen in the transcript notes.

### Scenario Verdict

- Overall verdict: `PASS`
- Pass/fail judgment: `PASS`

## Scenario S3: Kellerbrand Schulhaus

### Criterion Ratings

- Message Structure Validity: `PASS`
- Protocol Adherence: `PARTIAL`
- Turn-Taking Plausibility: `PARTIAL`
- Communication Flow Realism: `PARTIAL`
- Acknowledgement Patterns: `PARTIAL`
- Communication Economy and Style: `PASS`

### Assessment

Good:
- All turns remain interpretable as radio traffic.
- Core command chains are clear. `ids 2` -> `5`, `3` -> `4`, `7` -> `8` work structurally.
- Language is concise and the units report only task-relevant information.

Moderate issues:
- `id 12`: `"An Angriffstrupp von Einsatzleitung, Befehl: Kontrolle Installationsschacht abschliessen und Rueckmeldung zur Ausbreitung geben, antworten"` expects a directed response, but there is no acknowledgement. `id 13` jumps straight to outcome reporting. That is a direct weakness in acknowledgement structure and turn allocation.
- The scenario becomes too linear and thin after the initial setup. After `id 9`, almost all traffic is just the attack team talking to command. The source notes expect interleaving and some non-linear overlap; this scenario underdelivers on that realism dimension.

Minor issues:
- There is no follow-up confirmation from command after the final report at `id 13`. Not mandatory every time, but the ending feels abruptly clipped.
- Compared with the other scenarios, this one has the least variation in exchange type and the most obvious synthetic step-by-step progression.

### Scenario Verdict

- Overall verdict: `PARTIAL`
- Pass/fail judgment: `FAIL`

## Scenario S4: Werkstattbrand mit Gasflaschen

### Criterion Ratings

- Message Structure Validity: `PASS`
- Protocol Adherence: `PASS`
- Turn-Taking Plausibility: `PASS`
- Communication Flow Realism: `PASS`
- Acknowledgement Patterns: `PASS`
- Communication Economy and Style: `PASS`

### Assessment

Good:
- This is the strongest scenario structurally.
- The traffic has credible interleaving between traffic control, fire attack, and gas-bottle cooling. `ids 9`, `10`, `11`, `12` -> `13`, `14` -> `15`, `17`, `18` -> `19` give a believable multi-threaded radio flow.
- Commands are clearly directed and acknowledged.
- Reports are compressed but still informative. The messages would remain coherent even if rendered as transcript-only text.
- Repeated cooling updates from `ids 11`, `17`, `19` are plausible because the task is ongoing and condition-based.

Minor issues:
- `id 2` ends with `antworten` although it is already a report. This is still interpretable because it works as a call-up expecting command reaction, but it is a slight formal mismatch.

### Scenario Verdict

- Overall verdict: `PASS`
- Pass/fail judgment: `PASS`

## Scenario S5: Dachstockbrand Reihenhaus

### Criterion Ratings

- Message Structure Validity: `PARTIAL`
- Protocol Adherence: `PASS`
- Turn-Taking Plausibility: `PASS`
- Communication Flow Realism: `PASS`
- Acknowledgement Patterns: `PASS`
- Communication Economy and Style: `PASS`

### Assessment

Good:
- Strong progression from arrival to setup, tasking, mitigation, control, and handover.
- `ids 4` -> `5` -> `8`, `6` -> `7` -> `9`, `10` -> `11` -> `14`, `12` -> `13` -> `15` -> `16` -> `17` form credible multi-step exchanges.
- The handover closeout at `ids 18` and `19` is structurally plausible and reads like operational radio traffic rather than narration.

Moderate issues:
- `id 3`: `"Angriffstrupp vor Ort, keine offenen Flammen aussen, Rauch aus zwei Feldern der Dachhaut, Schluss"` has no explicit receiver and no message type marker. The real-transcript notes allow this kind of compression, so it remains interpretable, but it is a structural weakening relative to the stricter rule set.

Minor issues:
- The scenario is slightly cleaner than real traffic and relies heavily on textbook task-completion sequencing.

### Scenario Verdict

- Overall verdict: `PASS`
- Pass/fail judgment: `PASS`

## Dataset-Level Assessment

### Overall Judgment

- Overall verdict: `PARTIAL`
- Overall pass/fail judgment: `FAIL`

### Cross-Dataset Strengths

- The dataset is consistently interpretable as firefighter radio traffic.
- All scenarios preserve short, compressed, operational phrasing rather than drifting into narrative prose.
- Most command chains are understandable even if transcript rendering strips some metadata.
- Units usually report in ways that match their local task thread, which supports transcript coherence.
- The dataset correctly mixes assignments, acknowledgements, progress reports, and completion reports.

### Cross-Dataset Critical Issues

- No cross-dataset critical structural breakdown was found. None of the scenarios becomes uninterpretable as radio traffic.

### Cross-Dataset Moderate Issues

- Several messages are labeled as `Meldung` while functioning as renewed instructions or constraints. The clearest cases are `S1 id 17` and `S2 id 19`. This blurs protocol categories in a patterned way rather than as controlled realism.
- The dataset is consistently cleaner and more deterministic than the real-transcript guidance. Most scenarios follow near-template command/ack/progress/completion sequences with limited disorder, limited overlap tension, and little protocol noise.
- Scenario `S3` is noticeably weaker on communication-flow realism because the traffic collapses into a narrow command/attack-team exchange without enough interleaving.

### Cross-Dataset Minor Issues

- Formal markers are sometimes omitted or softened in isolated messages, for example `S5 id 3`. These are acceptable individually but should be controlled deliberately.
- Multi-recipient alerts are rarely followed by any realistic acknowledgement strategy. They are neither fully sequential nor clearly modeled as broadcast-without-reply.
- There is low variation in acknowledgement style across the dataset. Many responses follow the same template shape, which increases synthetic feel.

## Concrete Revision List

1. Reclassify directive-like `Meldung` messages as `Befehl` when they issue an actionable order, or rewrite them into true status messages with no response expectation.
2. Add explicit acknowledgements after directed commands that end with `antworten`, especially in `S3 id 12`.
3. Strengthen `S3` by adding at least one interleaved update from another unit between `ids 10` and `13`, so the flow is less single-threaded and more incident-like.
4. Decide a consistent treatment for `An Alle` broadcasts: either model them as no-reply alerts, or include ordered acknowledgements from the named stations when a reply is expected.
5. Introduce controlled realism noise in a few places: partial readbacks, slightly compressed addressing, or omitted closure markers, but only where interpretability remains intact.
6. Reduce generator-shaped repetition by merging or differentiating closely similar updates such as `S1 ids 12` and `13`.
7. Review messages that rely on the external `speaker` field more than on transcript text. Where possible, make the text itself recoverable as radio traffic after metadata stripping.

## Final Recommendation

The dataset is close to structurally usable, but it does not fully pass as a set because `S3` is only `PARTIAL` and the dataset shows repeated protocol-label drift in directive messages. A fix pass should focus on acknowledgement discipline, better distinction between `Meldung` and `Befehl`, and slightly more realistic interleaving.
