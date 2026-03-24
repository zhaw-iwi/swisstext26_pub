# STRUCTURE_VALIDATION_REPORT

Scope: structural validity and communication realism only, grounded in:
- `./.agents/datasetgeneration/dataset_validation_structure.md`
- `./.agents/datasetgeneration/source_notes_sprechregeln.md`
- `./.agents/datasetgeneration/source_notes_real_transcript.md`

Dataset inspected:
- `data/scenarios/synthetic_firefighter_radio_controlled_v1/s1.json`
- `data/scenarios/synthetic_firefighter_radio_controlled_v1/s2.json`
- `data/scenarios/synthetic_firefighter_radio_controlled_v1/s3.json`
- `data/scenarios/synthetic_firefighter_radio_controlled_v1/s4.json`
- `data/scenarios/synthetic_firefighter_radio_controlled_v1/s5.json`

Pass/fail convention used here:
- Scenario `PASS` => pass
- Scenario `PARTIAL` or `FAIL` => fail

## Scenario S1: Kuechenbrand Mehrfamilienhaus

### Criteria
- Message Structure Validity: `PASS`
- Protocol Adherence: `PASS`
- Turn-Taking Plausibility: `PASS`
- Communication Flow Realism: `PASS`
- Acknowledgement Patterns: `PASS`
- Communication Economy and Style: `PASS`

### Assessment
Good:
- `1` to `3` is a plausible opening: a multi-recipient situation message followed by two short acknowledgements in sequence.
- `5`/`6`, `7`/`8`, `9`/`10`, and `14`/`15` are clean command-acknowledgement pairs with recognizable radio structure.
- `11` to `17` gives a realistic mix of supply status, search result, knockdown update, ventilation release, and ventilation progress. The exchange remains interpretable under `structured_dialogue`, `no_speaker`, and `continuous_transcript` because the short acknowledgements still self-identify.

Critical issues:
- None.

Moderate issues:
- None.

Minor issues:
- `1` addresses two units but uses `Schluss` rather than explicit turn allocation such as `antworten`. The follow-up acknowledgements still make the sequence understandable, but the opening is slightly hybrid between a one-sided broadcast and a directed multi-party call.

### Overall verdict
- Structural verdict: `PASS`
- Pass/fail judgment: `PASS`

## Scenario S2: Tiefgaragenbrand Wohnblock

### Criteria
- Message Structure Validity: `PASS`
- Protocol Adherence: `PARTIAL`
- Turn-Taking Plausibility: `PASS`
- Communication Flow Realism: `PASS`
- Acknowledgement Patterns: `PASS`
- Communication Economy and Style: `PASS`

### Assessment
Good:
- `1`, `2`, `7`, `8`, `11`, `14`, `17`, and `18` create a coherent operational arc from arrival through localization, suppression, and post-fire measurement.
- The scenario uses short, compressed status lines that match the source notes well.
- Messages remain coherent under `no_speaker` and `continuous_transcript` because most lines contain sender or receiver identity inside the utterance text.

Critical issues:
- None.

Moderate issues:
- `3` and `4` are both directed `Befehl ... antworten` turns sent back-to-back before any acknowledgement appears in `5` and `6`. This is still interpretable, but it compresses strict turn allocation more than the guidance in `source_notes_sprechregeln.md` suggests.

Minor issues:
- `13` (`Messgruppe korrekt, Nachkontrolle nach Freigabe ab Zugang West, Schluss`) is realistic shorthand, but it is another instance of the dataset favoring a very regular acknowledgement template rather than a wider mix of readback styles.

### Overall verdict
- Structural verdict: `PASS`
- Pass/fail judgment: `PASS`

## Scenario S3: Kellerbrand Schulhaus

### Criteria
- Message Structure Validity: `PASS`
- Protocol Adherence: `PASS`
- Turn-Taking Plausibility: `PASS`
- Communication Flow Realism: `PARTIAL`
- Acknowledgement Patterns: `PASS`
- Communication Economy and Style: `PASS`

### Assessment
Good:
- `2` to `9` is structurally strong. Directed tasks are clear, acknowledgements are immediate, and the hose-line readiness report arrives at the right point in the exchange.
- `7`/`8` is a good example of a fuller readback that preserves the command core while staying short.
- The messages survive the transcript transformations well because almost every line carries an internal sender cue or explicit addressing.

Critical issues:
- None.

Moderate issues:
- `10`, `11`, `13`, and `15` create a long late-stage stretch dominated by the same unit with only one short command-side intervention at `12`. The sequence remains understandable, but the coordination layer feels more authored than observed and less interleaved than the real-transcript notes suggest.

Minor issues:
- `11` and `15` repeat the phrase `Brand am Trockner abgeloescht`. Repetition is plausible, but here it makes the progression slightly more schematic than necessary.

### Overall verdict
- Structural verdict: `PASS`
- Pass/fail judgment: `PASS`

## Scenario S4: Werkstattbrand mit Gasflaschen

### Criteria
- Message Structure Validity: `PASS`
- Protocol Adherence: `PASS`
- Turn-Taking Plausibility: `PASS`
- Communication Flow Realism: `PARTIAL`
- Acknowledgement Patterns: `PASS`
- Communication Economy and Style: `PASS`

### Assessment
Good:
- `3`/`4`, `5`/`6`, `8`/`9`, `10`/`11`, `15`/`16`, and `21`/`22` are all structurally clean command-acknowledgement pairs.
- The scenario interleaves three units in a controlled way and keeps every message short enough for radio traffic.
- `12`, `13`, `14`, `19`, and `20` are good examples of concise progress reports tied to task state.

Critical issues:
- None.

Moderate issues:
- `14` to `22` becomes repetitive in a way that reads more synthetic than transcript-like. `14`, `15`, `16`, `20`, `21`, and `22` cycle through nearly the same cooling-status pattern with very little variation in phrasing or coordination density. The sequence is still valid, but it is the most templated flow in the dataset.

Minor issues:
- `18` (`An Verkehrstrupp von Einsatzleitung, Meldung: verstanden, Sicherheitsbereich beibehalten, Schluss`) is interpretable, but the embedded `verstanden` inside a new directed message is slightly awkward compared with the more natural confirmation patterns elsewhere.

### Overall verdict
- Structural verdict: `PASS`
- Pass/fail judgment: `PASS`

## Scenario S5: Dachstockbrand Reihenhaus

### Criteria
- Message Structure Validity: `PASS`
- Protocol Adherence: `PASS`
- Turn-Taking Plausibility: `PASS`
- Communication Flow Realism: `PASS`
- Acknowledgement Patterns: `PASS`
- Communication Economy and Style: `PASS`

### Assessment
Good:
- This is the strongest scenario structurally. `2` and `3` provide plausible self-initiated arrival/status traffic before later tasking.
- `4`/`5`, `6`/`7`, `9`/`10`, `13`/`14`, `15`/`16`, and `18`/`19` are all clean directed exchanges with clear response structure.
- `11` gates `12` plausibly: the attack crew does not report interior roof-space work until the ladder readiness message is in.
- `20` to `22` gives a realistic short closing sequence from final check to handover. The scenario stays coherent even in `continuous_transcript` because the message texts carry their own identities and transitions.

Critical issues:
- None.

Moderate issues:
- None.

Minor issues:
- `21` is a directed handover message without `antworten`, but a reply still follows in `22`. That is realistic enough and does not damage interpretation.

### Overall verdict
- Structural verdict: `PASS`
- Pass/fail judgment: `PASS`

## Dataset-Level Assessment

### Cross-dataset strengths
- The dataset is consistently interpretable as radio traffic. None of the scenarios contain narrative prose, meta commentary, or structurally opaque turns.
- Sender and receiver cues are embedded in the utterance text often enough that the scenarios remain coherent under `structured_dialogue`, `no_speaker`, and `continuous_transcript`.
- The set covers a good mix of assignments, acknowledgements, progress reports, partial completion reports, and final completion or hold-state reports.
- Communication economy is strong across all five scenarios. Messages are generally short, direct, and compressed in a way that fits the source notes.
- Protocol noise is controlled rather than chaotic. Deviations from the idealized format do not make task state or speaking responsibility hard to recover.

### Cross-dataset critical issues
- None.

### Cross-dataset moderate issues
- The dataset is slightly too regular compared with the variability described in `source_notes_real_transcript.md`. A large share of acknowledgements use the same compact shape: `[Unit] verstanden, [task core], Schluss`.
- There are a few cases where strict turn allocation is compressed by stacking directed commands before replies, most clearly `S2-3` and `S2-4`, and to a lesser extent `S3-2` and `S3-3`.
- Some later-stage sequences are more linear and polished than naturally messy radio traffic, especially `S3-10` to `S3-15` and `S4-14` to `S4-22`.

### Cross-dataset minor issues
- The set underuses some realistic protocol variation documented in the source notes, especially shorter unclosed acknowledgements, more varied confirmation forms, and occasional freer shorthand.
- The dataset relies heavily on `Meldung` and `Befehl`, with very little visible use of explicit `Antwort` or `Verbindungskontrolle` forms. This is not a structural failure, but it narrows realism variety.

### Overall dataset verdict
- Structural verdict: `PASS`
- Overall pass/fail judgment: `PASS`

Reason for overall pass:
- No scenario has a criterion-level `FAIL`.
- The identified weaknesses are mostly about regularity and transcript texture rather than broken protocol logic or loss of interpretability.

## Concrete Revision List

1. Diversify acknowledgement surface forms without reducing clarity.
   Target recurring templates such as `S2-5`, `S2-6`, `S3-4`, `S3-5`, `S4-4`, `S4-6`, `S5-5`, and `S5-7`.

2. Avoid stacking multiple `... antworten` orders before any reply when strict directed turn-taking is intended.
   Highest-priority fix: `S2-3` and `S2-4`.
   Secondary case: `S3-2` and `S3-3`.

3. Add one brief command-side coordination or confirmation turn in `S3` after the attack-trupp reporting sequence.
   Best insertion points are after `S3-11` or after `S3-15`.
   Goal: reduce the authored single-thread feel late in the scenario.

4. Reduce the templated repetition in the late gas-cylinder cooling loop in `S4`.
   Rework `S4-14` to `S4-22` so one of the repeated progress or re-tasking steps is merged, paraphrased, or replaced with a short command-side confirmation.

5. Introduce a little more controlled realism noise across the dataset while preserving transcript-condition coherence.
   Good candidates are:
   - one or two acknowledgements without `Schluss`
   - one or two shorter self-initiated status reports
   - one additional `korrekt` or `richtig` style confirmation outside the current small set

6. Keep the current strong internal sender cues when revising.
   This matters for `no_speaker` and `continuous_transcript`, where attribution depends on the text itself rather than the JSON speaker field.
