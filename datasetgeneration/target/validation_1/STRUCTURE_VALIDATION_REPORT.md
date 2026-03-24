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
- Message Structure Validity: `PARTIAL`
- Protocol Adherence: `PARTIAL`
- Turn-Taking Plausibility: `PASS`
- Communication Flow Realism: `PASS`
- Acknowledgement Patterns: `PARTIAL`
- Communication Economy and Style: `PASS`

### Assessment
Good:
- Strong mixture of call-up, assignment, acknowledgement, progress update, and follow-up report.
- Messages `4`, `5`, `7`, `8`, `11`, `12`, and `14` use recognizable radio structure with explicit addressing.
- Compression is mostly plausible and remains interpretable in all transcript conditions.

Critical issues:
- None.

Moderate issues:
- `7` is a directed `Befehl` to `Wassertrupp` with `antworten`, but there is no immediate acknowledgement. `10` is a status report, not a clear readback. This weakens the "commands are typically acknowledged" rule.
- `14` ends with `antworten` but no follow-up appears. That leaves the turn structurally open.
- `13` is only `Verstanden, Entrauchung laeuft an, Schluss`. In `no_speaker` and especially `continuous_transcript`, the missing unit name makes attribution weaker than elsewhere in the dataset.

Minor issues:
- `6` is interpretable, but it drops explicit receiver/message-type framing and ends without `Schluss`.
- `9` also uses a reduced acknowledgement/report form without full protocol framing.

### Transcript representation coherence
- `structured_dialogue`: coherent.
- `no_speaker`: mostly coherent, but `13` becomes notably less attributable because it omits the unit name.
- `continuous_transcript`: still interpretable overall, but the reduced acknowledgement in `13` is the weakest point.

### Overall verdict
- Structural verdict: `PARTIAL`
- Pass/fail judgment: `FAIL`

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
- Realistic interleaving of directed tasking and self-initiated status reporting.
- `2`, `7`, `8`, `11`, and `13` provide a plausible operational progression from arrival to localization, knockdown, and monitoring.
- The scenario remains readable under speaker-stripped forms because most messages either self-identify or include explicit addressing.

Critical issues:
- None.

Moderate issues:
- `1` is a broadcast ending in `antworten`, but it does not collect ordered acknowledgements from addressed stations. This is a repeated protocol shortcut across the dataset.

Minor issues:
- `2` is a compressed status line without explicit addressee or closure, but it is realistic field shorthand.
- `10` is a reduced acknowledgement (`Messgruppe korrekt...`) rather than a fuller readback.

### Transcript representation coherence
- Coherent in all intended transcript representations.
- The scenario survives `no_speaker` and `continuous_transcript` well because message texts usually carry their own speaker or receiver signals.

### Overall verdict
- Structural verdict: `PASS`
- Pass/fail judgment: `PASS`

## Scenario S3: Kellerbrand Schulhaus

### Criteria
- Message Structure Validity: `PASS`
- Protocol Adherence: `PARTIAL`
- Turn-Taking Plausibility: `PASS`
- Communication Flow Realism: `PARTIAL`
- Acknowledgement Patterns: `PASS`
- Communication Economy and Style: `PASS`

### Assessment
Good:
- Directed commands to `Sicherungstrupp`, `Wassertrupp`, and `Angriffstrupp` are clear and receive interpretable acknowledgements in `4`, `5`, and `8`.
- `10`, `11`, and `12` form a plausible three-step operational update sequence: finding, knockdown, confirmation of no extension.
- Language stays short and operational.

Critical issues:
- None.

Moderate issues:
- `1` again ends with `antworten` without any ordered acknowledgement sequence.
- Communication flow is somewhat narrow after initial tasking. From `10` to `12`, the scenario becomes almost a single-unit reporting stream with no command-side confirmation or coordination layer, which makes it feel more authored than observed.

Minor issues:
- `5` is only `Sicherungstrupp verstanden` with no closure and no readback content.

### Transcript representation coherence
- Coherent in all three transcript forms.
- This scenario is relatively robust in `no_speaker` because even the compressed acknowledgements still self-identify.

### Overall verdict
- Structural verdict: `PASS`
- Pass/fail judgment: `PASS`

## Scenario S4: Werkstattbrand mit Gasflaschen

### Criteria
- Message Structure Validity: `PASS`
- Protocol Adherence: `PARTIAL`
- Turn-Taking Plausibility: `PASS`
- Communication Flow Realism: `PARTIAL`
- Acknowledgement Patterns: `PASS`
- Communication Economy and Style: `PASS`

### Assessment
Good:
- All three direct commands (`2`, `4`, `6`) get immediate acknowledgements (`3`, `5`, `7`).
- Status updates `8`, `9`, and `10` are concise and role-appropriate in form.
- Message compression is strong without collapsing interpretability.

Critical issues:
- None.

Moderate issues:
- `1` uses broadcast-plus-`antworten` structure but does not gather sequential replies.
- The scenario is the most linear and least variegated in the set. It is essentially: initial broadcast, three commands with acknowledgements, one status from each unit, final broadcast. That is interpretable, but it sits close to the "artificial dialogue" boundary described in the validation criteria.

Minor issues:
- `11` is a one-sided broadcast at the end with no subsequent traffic. Acceptable, but it contributes to the abrupt stop.

### Transcript representation coherence
- Coherent in all three transcript forms.
- Because the message texts themselves carry unit names or addressing, speaker removal does not materially damage interpretation.

### Overall verdict
- Structural verdict: `PASS`
- Pass/fail judgment: `PASS`

## Scenario S5: Dachstockbrand Reihenhaus

### Criteria
- Message Structure Validity: `PASS`
- Protocol Adherence: `PARTIAL`
- Turn-Taking Plausibility: `PASS`
- Communication Flow Realism: `PASS`
- Acknowledgement Patterns: `PASS`
- Communication Economy and Style: `PASS`

### Assessment
Good:
- Best overall communication flow in the dataset.
- `2` and `3` are plausible self-initiated status updates before later formal tasking.
- `4`/`5`, `6`/`7`, and `10`/`11` form clear assignment-acknowledgement pairs.
- `8`, `9`, `12`, `13`, and `14` create a convincing progression from setup through suppression, verification, and handover readiness.

Critical issues:
- None.

Moderate issues:
- `1` again ends with `antworten` but does not receive ordered acknowledgements from addressed stations.

Minor issues:
- `11` is a compressed acknowledgement without full protocol framing, but it remains realistic and clear.

### Transcript representation coherence
- Coherent in all intended transcript representations.
- This scenario remains especially robust under `no_speaker` and `continuous_transcript` because nearly every line contains a strong sender/receiver cue.

### Overall verdict
- Structural verdict: `PASS`
- Pass/fail judgment: `PASS`

## Dataset-Level Assessment

### Cross-dataset strengths
- The dataset consistently uses short, compressed, operationally legible utterances rather than narrative prose.
- Most scenarios mix formal `An ... von ...` turns with realistic shorthand, which matches the source-note expectation of controlled protocol noise.
- Turn-taking is generally interpretable. There are no major cases of contradictory simultaneous responses or unit confusion.
- The scenarios mostly remain coherent under `structured_dialogue`, `no_speaker`, and `continuous_transcript` because many messages embed sender/receiver cues directly in the text.

### Cross-dataset critical issues
- None.

### Cross-dataset moderate issues
- Systematic broadcast misuse of `antworten`: `S1-1`, `S2-1`, `S3-1`, `S4-1`, and `S5-1` all invite replies but do not follow the stricter sequential acknowledgement pattern described in `source_notes_sprechregeln.md`. This is the clearest repeated protocol weakness.
- Some scenarios rely on reduced acknowledgements that become weak under speaker removal. The main example is `S1-13` (`Verstanden, Entrauchung laeuft an, Schluss`), which is much less attributable in `no_speaker` and `continuous_transcript`.
- Flow realism is uneven. `S4` is notably schematic, and `S3` becomes single-threaded late in the incident. The set as a whole is interpretable, but not all scenarios show the same level of interleaving and coordination density.

### Cross-dataset minor issues
- Closure markers are inconsistent throughout the set. This is realistic in moderation, but the omissions are slightly too patterned because they often disappear in acknowledgements specifically.
- Some command acknowledgements are minimal and do not clearly read back the actionable core.

### Overall dataset verdict
- Structural verdict: `PARTIAL`
- Overall pass/fail judgment: `FAIL`

Reason for overall fail:
- The dataset is structurally usable and often realistic, but it contains a repeated protocol pattern that is weak across all five scenarios, plus one scenario-level transcript-coherence issue (`S1`) that should be corrected before calling the set structurally clean.

## Concrete Revision List

1. Revise all opening broadcast messages that currently end with `antworten` (`S1-1`, `S2-1`, `S3-1`, `S4-1`, `S5-1`).
   Replace them with either:
   - a true broadcast without reply expectation, or
   - a broadcast that explicitly requests ordered acknowledgements and then actually includes them.

2. Fix reduced acknowledgements that lose attribution when speaker labels are removed.
   Priority case:
   - `S1-13`: prepend the unit identity, for example a `Lueftungstrupp ...` form.

3. Ensure every directed `Befehl` with `antworten` receives a recognisable acknowledgement immediately after the order unless the scenario intentionally models a realistic interruption.
   Priority case:
   - `S1-7` should get an explicit `Wassertrupp` acknowledgement before or instead of jumping directly to `10`.

4. Remove structurally open turns unless a reply actually follows.
   Priority case:
   - `S1-14` should not end with `antworten` if no answer is present.

5. Increase flow variability in the weakest scenarios without changing task content.
   - `S4`: add at least one command-side reaction or coordination turn after `10`, or one additional interleaved update, so the scenario is less purely staged.
   - `S3`: add one brief command-side confirmation or coordination turn after the attack-trupp updates to reduce the single-threaded ending.

6. Standardize acknowledgement quality slightly.
   Keep realism noise, but ensure most acknowledgements include at least one of:
   - unit identity
   - explicit `verstanden`/`korrekt`
   - compressed readback of the task core

7. Re-run structural validation after edits and specifically check speaker-stripped coherence for:
   - isolated acknowledgements
   - final reports ending in `antworten`
   - sequences where multiple reduced confirmations appear back to back
