# Structure Validation Report

Dataset: `data/scenarios/synthetic_firefighter_radio_controlled_v1`

Validation basis:
- `./.agents/datasetgeneration/dataset_validation_structure.md`
- `./.agents/datasetgeneration/source_notes_sprechregeln.md`
- `./.agents/datasetgeneration/source_notes_real_transcript.md`

Scope limits:
- Evaluated only structural validity and communication realism.
- Did not evaluate operational correctness.

Binary rule used here:
- `PASS` verdict => `Pass`
- `PARTIAL` or `FAIL` verdict => `Fail`

## Scenario S1: Kuechenbrand Mehrfamilienhaus

### Criterion Scores
| Criterion | Score | Notes |
|---|---|---|
| Message Structure Validity | PASS | Most turns have identifiable sender, receiver, and actionable intent. |
| Protocol Adherence | PARTIAL | Command acknowledgements are present, but protocol markers are inconsistent. |
| Turn-Taking Plausibility | PASS | Exchange order is readable and role-consistent. |
| Communication Flow Realism | PASS | Realistic progression from initial report to tasking, update, and incomplete ventilation. |
| Acknowledgement Patterns | PASS | Key commands are acknowledged in compressed but interpretable form. |
| Communication Economy and Style | PASS | Mostly short, compressed, radio-like phrasing. |

### Good
- Clear command-to-acknowledgement structure in messages `5 -> 6`, `7 -> 8`, `14 -> 15`.
- Self-initiated status reports from `11`, `12`, `13`, and `16` fit the transcript notes well.
- Message lengths stay concise while still preserving state traceability.

### Critical Issues
- None.

### Moderate Issues
- `10`: `"Lueftungstrupp verstanden, Ueberdruckbeluefter am Hauseingang in Bereitstellung"` omits `Schluss` while surrounding traffic uses closure markers consistently. This is acceptable noise once, but it weakens structural regularity.

### Minor Issues
- `1`: Broadcast-style initial message to two named units does not collect ordered acknowledgements. This is still interpretable because it is a `Meldung`, but it is less structured than the ideal multi-recipient pattern in the guidance.
- `4`: Ends with `antworten`, but the reply is not a direct acknowledgement. `5` is a new command rather than a clear response to the report.
- `11`: `"Wassertrupp an Einsatzleitung"` reverses the dominant addressing pattern (`An Einsatzleitung von Wassertrupp`). Interpretable, but stylistically inconsistent with the rest of the dataset.

### Scenario Verdict
- Overall verdict: `PASS`
- Pass/Fail judgment: `Pass`

## Scenario S2: Tiefgaragenbrand Wohnblock

### Criterion Scores
| Criterion | Score | Notes |
|---|---|---|
| Message Structure Validity | PASS | Sender/receiver roles and message intent remain clear throughout. |
| Protocol Adherence | PASS | Commands are acknowledged and follow-up reports are structurally coherent. |
| Turn-Taking Plausibility | PASS | Multi-unit traffic is interleaved but remains interpretable. |
| Communication Flow Realism | PASS | Good mix of assignment, readiness, tactical report, measurement, and incomplete clearance. |
| Acknowledgement Patterns | PASS | Key `Befehl` turns receive timely confirmations. |
| Communication Economy and Style | PASS | Compact phrasing with realistic radio compression. |

### Good
- `3 -> 6 -> 7` and `9 -> 10 -> 11` show clean command, acknowledgement, and progress-report patterns.
- `12 -> 13 -> 15 -> 16 -> 17` models a realistic staged task release: pre-assignment, hold condition, activation, then incomplete measurement report.
- Units speak within plausible observation scope; messages do not drift into narrative exposition.

### Critical Issues
- None.

### Moderate Issues
- None.

### Minor Issues
- `1`: Broadcast opening does not solicit or record acknowledgements from all addressed parties. This is still acceptable under the real-transcript flexibility notes.
- `19`: `"An Messgruppe von Einsatzleitung, Meldung: Bereich Vorraum und Rampe bleibt bis zu eurer Freimeldung gesperrt, Schluss"` is structurally fine, but it functions partly like a standing instruction while being labeled only as `Meldung`. This is a minor label-choice inconsistency, not an interpretability problem.

### Scenario Verdict
- Overall verdict: `PASS`
- Pass/Fail judgment: `Pass`

## Scenario S3: Kellerbrand Schulhaus

### Criterion Scores
| Criterion | Score | Notes |
|---|---|---|
| Message Structure Validity | PASS | Message framing is consistent and easy to parse. |
| Protocol Adherence | PASS | Directed commands are acknowledged and follow-up reports fit the assigned tasks. |
| Turn-Taking Plausibility | PASS | Response order is plausible even with interleaved unit traffic. |
| Communication Flow Realism | PASS | Strong incremental progression from perimeter control to extinguishment and control. |
| Acknowledgement Patterns | PASS | Command acknowledgements are present and suitably compressed. |
| Communication Economy and Style | PASS | Short, direct, operationally focused radio language. |

### Good
- `2 -> 5 -> 6`, `3 -> 4 -> 9`, and `7 -> 8 -> 10/11/15` are structurally strong task chains.
- Repeated updates from the attack team (`10`, `11`, `15`) remain concise and support state progression rather than repeating empty filler.
- `16` works as a realistic aggregate command-layer update to all units.

### Critical Issues
- None.

### Moderate Issues
- None.

### Minor Issues
- `11` and `15` both report `"Brand am Trockner abgeloescht"`. The repetition is not unrealistic, but the second message would sound more natural if it focused more strongly on the newly requested spread check rather than repeating the extinguishment result.

### Scenario Verdict
- Overall verdict: `PASS`
- Pass/Fail judgment: `Pass`

## Scenario S4: Werkstattbrand mit Gasflaschen

### Criterion Scores
| Criterion | Score | Notes |
|---|---|---|
| Message Structure Validity | PASS | Most turns remain interpretable as radio utterances. |
| Protocol Adherence | PARTIAL | Core commands are acknowledged, but some marker usage is mismatched. |
| Turn-Taking Plausibility | PARTIAL | One explicit turn-allocation is not respected cleanly. |
| Communication Flow Realism | PASS | Overall incident progression is coherent. |
| Acknowledgement Patterns | PASS | Command acknowledgements exist where needed. |
| Communication Economy and Style | PASS | Messages stay compressed and operational. |

### Good
- `3 -> 4 -> 12` and `5 -> 6 -> 7` are structurally clean and support strong task traceability.
- `10 -> 11 -> 14 -> 15 -> 16 -> 20 -> 21 -> 22` gives a realistic repeated-monitoring loop for an unresolved hazard.
- Reports remain brief even when conveying multiple state variables.

### Critical Issues
- None.

### Moderate Issues
- `2`: `"An Einsatzleitung von Angriffstrupp, Meldung: ... , antworten"` explicitly requests turn return, but no direct reply follows. Instead, `3` and `5` address other units, and only `8` returns to the attack team. This breaks the documented meaning of `antworten` as explicit turn allocation and makes the local exchange structurally sloppy.
- `18`: `"Einsatzleitung richtig, Sicherheitsbereich beibehalten, Schluss"` uses `richtig` without a clear preceding readback that would normally be confirmed as correct. `17` is a status report, not a readback. The intent is inferable, but the confirmation form is mismatched.

### Minor Issues
- `9`: `"Angriffstrupp verstanden, Schaumangriff ueber Westtuere, Schluss"` acknowledges the order but drops the explicit hazard-monitoring part of the command (`Gasflaschenlage im Blick behalten`). This is still acceptable as compressed acknowledgement, but it is slightly thinner than the surrounding readbacks.

### Scenario Verdict
- Overall verdict: `PARTIAL`
- Pass/Fail judgment: `Fail`

## Scenario S5: Dachstockbrand Reihenhaus

### Criterion Scores
| Criterion | Score | Notes |
|---|---|---|
| Message Structure Validity | PASS | Clear sender/receiver structure with readable role separation. |
| Protocol Adherence | PASS | Directed tasking is acknowledged and sequencing remains coherent. |
| Turn-Taking Plausibility | PASS | Conditional sequencing around ladder readiness is plausible. |
| Communication Flow Realism | PASS | Good move from staging to opening, suppression, control, and handover. |
| Acknowledgement Patterns | PASS | Command acknowledgements are present and fit the compressed style. |
| Communication Economy and Style | PASS | Phrasing is concise and radio-like throughout. |

### Good
- `4 -> 5 -> 11` and `9 -> 10 -> 12 -> 13 -> 14 -> 17` are strong structured exchanges.
- `15 -> 16 -> 18 -> 19 -> 20` gives a realistic delayed secondary task release.
- The scenario remains coherent under both strict transcript parsing and more compressed real-transcript interpretation.

### Critical Issues
- None.

### Moderate Issues
- None.

### Minor Issues
- `21 -> 22`: The police handover appears only at the end with no earlier presence on channel. This is still interpretable, but a prior mention or earlier call-up would make the communication chain feel slightly more grounded.

### Scenario Verdict
- Overall verdict: `PASS`
- Pass/Fail judgment: `Pass`

## Dataset-Level Assessment

### Overall Strengths
- The dataset consistently preserves interpretable sender, receiver, and task state.
- All scenarios show realistic incident progression rather than static dialogue fragments.
- Command-to-acknowledgement structure is present in the majority of directed task assignments.
- Language is generally compressed, operational, and compatible with the transcript-style notes.
- The scenarios remain coherent even when interpreted under the looser real-transcript representation.

### Cross-Dataset Critical Issues
- None.

### Cross-Dataset Moderate Issues
- Protocol markers are used inconsistently across the dataset. `Meldung` and `Befehl` appear frequently, but `Antwort` is effectively absent and `antworten` is sometimes used without a clean response path.
- Final confirmations from command after important subordinate reports are sparse. This is realistic in moderation, but across the dataset it creates a slightly generator-like pattern of report termination without command closure.

### Cross-Dataset Minor Issues
- Broadcast openings (`An Alle ...`) rarely collect acknowledgements. This is acceptable under the flexible transcript notes, but it weakens alignment with the stricter protocol notes.
- Closure markers are almost universal, but not fully consistent (`S1-10`).
- Addressing syntax varies between patterns like `An Einsatzleitung von Wassertrupp` and `Wassertrupp an Einsatzleitung`, suggesting template inconsistency.
- Confirmation words such as `korrekt` and `richtig` are sometimes inserted mechanically rather than in their clearest protocol context.

### Dataset Verdict
- Overall verdict: `PARTIAL`
- Overall Pass/Fail judgment: `Fail`

Reason:
- Four scenarios score `PASS`.
- One scenario (`S4`) scores `PARTIAL`.
- Because this report requires explicit binary pass/fail judgment, the dataset does not fully pass structural validation as a set.

## Concrete Revision List

1. Remove or correct dangling `antworten` markers when no direct response follows.
   - Highest priority example: `S4-2`.

2. Normalize acknowledgement wording after status reports versus readbacks.
   - Replace mismatched confirmations like `S4-18` with a plain acknowledgement or a directed follow-up.

3. Standardize addressing syntax across scenarios.
   - Prefer one dominant structure such as `An [Empfaenger] von [Absender]`.
   - Clean up outliers like `S1-11`.

4. Enforce closure consistency unless omission is deliberately injected as controlled noise.
   - Fix obvious singleton omissions like `S1-10`, or document them as intentional noise cases and distribute them more systematically.

5. Audit all uses of `antworten` against the next one or two turns.
   - If the next turn is not the addressed unit or does not function as a response, remove `antworten`.

6. Add a small number of command-layer acknowledgements after significant subordinate reports.
   - This should be selective, not universal, to avoid over-formalization.

7. Review broadcast openings for whether they should remain one-way alerts or become explicit multi-party acknowledgements.
   - Keep them as one-way alerts if intended, but then avoid implying ordered reply behavior elsewhere in the same pattern family.

8. Reduce template drift in compressed acknowledgements.
   - Keep compressed readbacks, but ensure they preserve the operational core of the order when the omitted detail is safety-relevant.
   - Example to review: `S4-9`.
