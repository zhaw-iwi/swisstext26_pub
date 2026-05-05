# STRUCTURE_VALIDATION_REPORT

Validation basis:
- `./.agents/datasetgeneration/dataset_validation_structure.md`
- `./.agents/datasetgeneration/source_notes_sprechregeln.md`
- `./.agents/datasetgeneration/source_notes_real_transcript.md`

Scope limits:
- Evaluated only structural validity and communication realism.
- Did not evaluate operational correctness or tactical soundness.

Pass/fail rule used:
- `PASS` scenario verdict means `pass`.
- `PARTIAL` or `FAIL` scenario verdict means `fail`.

## Per-Scenario Assessment

### S1 - Kuechenbrand Mehrfamilienhaus

Criterion scores:

| Criterion | Score | Notes |
| --- | --- | --- |
| Message Structure Validity | PASS | Most turns have clear sender/receiver structure or recognisable compressed acknowledgement forms. |
| Protocol Adherence | PARTIAL | Directed commands are acknowledged, but the multi-recipient opening in `1` requests answers while `2` turns immediately into action rather than a cleaner acknowledgement; `15` omits `Schluss`. |
| Turn-Taking Plausibility | PASS | Directed calls are answered by the addressed unit; sequencing remains interpretable. |
| Communication Flow Realism | PASS | Good mix of initial briefing, tasking, acknowledgements, status, progress, and incomplete completion for ventilation. |
| Acknowledgement Patterns | PASS | Commands in `5`, `7`, `9`, `14`, `17` are acknowledged in `6`, `8`, `10`, `15`, `18`. |
| Communication Economy and Style | PASS | Short, compressed, radio-like phrasing with only limited verbosity in situation reports. |

Critical issues:
- None.

Moderate issues:
- `2`: `Angriffstrupp verstanden, ruecken vor zum Hauseingang` responds to a multi-recipient incident briefing in `1`, but it blends acknowledgement with self-deployment without explicit assignment. It remains interpretable, but it weakens protocol clarity.

Minor issues:
- `15`: `Lueftungstrupp korrekt, Entrauchung laeuft an` lacks `Schluss` and is lighter than the surrounding acknowledgement pattern.

Good structural qualities:
- `5` -> `6`, `7` -> `8`, `9` -> `10`, `14` -> `15`, `17` -> `18` show consistent command/acknowledgement pairing.
- `12`, `13`, `16` provide incremental progress rather than abrupt task completion, which is realistic under the transcript guidance.

Scenario verdict: `PASS`

Explicit pass/fail judgment: `PASS`

### S2 - Tiefgaragenbrand Wohnblock

Criterion scores:

| Criterion | Score | Notes |
| --- | --- | --- |
| Message Structure Validity | PASS | All turns remain identifiable as radio traffic; sender intent is inferable throughout. |
| Protocol Adherence | PARTIAL | `19` is phrased as a directed command to `Messgruppe` but uses no `antworten`, and `20` functions as a report rather than a direct acknowledgement. |
| Turn-Taking Plausibility | PASS | Response ownership is mostly disciplined and no implausible cross-talk appears. |
| Communication Flow Realism | PASS | Strong operational flow from access preparation to attack, post-fire measurement, and restricted-area status. |
| Acknowledgement Patterns | PASS | Most commands are acknowledged promptly and in compressed but interpretable form. |
| Communication Economy and Style | PASS | Phrasing is concise and field-like; reports expand only when justified. |

Critical issues:
- None.

Moderate issues:
- `19` -> `20`: `An Messgruppe ... Befehl: Bereich Vorraum und Rampe bis zu eurer Freimeldung gesperrt halten, Schluss` is structurally awkward. The addressee is also the measuring unit, and `20` reports readings instead of clearly acknowledging the hold/sperr concept. The exchange is still interpretable but protocol coupling is weak.

Minor issues:
- `13`: `Messgruppe verstanden, Bereitstellung Vorraum Nord, Nachkontrolle nach Freigabe Angriffstrupp` lacks `Schluss`.

Good structural qualities:
- `3` -> `4` -> `7` and `5` -> `6` -> `8` are strong tasking-confirmation-completion chains.
- `11`, `14`, `18`, `20` create a realistic staged progression instead of a single oversized completion report.

Scenario verdict: `PASS`

Explicit pass/fail judgment: `PASS`

### S3 - Kellerbrand Schulhaus

Criterion scores:

| Criterion | Score | Notes |
| --- | --- | --- |
| Message Structure Validity | PASS | Very clear sender/receiver structure and intent throughout. |
| Protocol Adherence | PASS | Commands are acknowledged and progress reports follow the tasking sequence cleanly. |
| Turn-Taking Plausibility | PASS | Addressed units respond, and interleaving remains coherent. |
| Communication Flow Realism | PASS | Good blend of perimeter control, hose deployment, interior attack, reserve posture, and final control report. |
| Acknowledgement Patterns | PASS | All key taskings receive recognisable acknowledgements. |
| Communication Economy and Style | PASS | Messages are compact and radio-like, with longer detail only where justified. |

Critical issues:
- None.

Moderate issues:
- None.

Minor issues:
- `13`: `Wassertrupp verstanden, Reserve an der Kellertreppe, Leitung bleibt unter Druck` omits `Schluss`, which is a recurring minor protocol reduction across the dataset.

Good structural qualities:
- `2` -> `3` -> `6`, `4` -> `5` -> `9`, and `7` -> `8` -> `10` -> `11` -> `15` are all structurally strong and easy to follow.
- `11` and `15` distinguish partial progress from full completion well, which supports transcript realism.

Scenario verdict: `PASS`

Explicit pass/fail judgment: `PASS`

### S4 - Werkstattbrand mit Gasflaschen

Criterion scores:

| Criterion | Score | Notes |
| --- | --- | --- |
| Message Structure Validity | PASS | Directed tasking and compressed acknowledgements remain clear throughout. |
| Protocol Adherence | PASS | Commands are normally acknowledged, and ordered dependencies are visible. |
| Turn-Taking Plausibility | PASS | The right units answer the right calls; no implausible simultaneous response behavior appears. |
| Communication Flow Realism | PASS | Strong interleaving of access control, cooling, attack timing, and unresolved residual hazard. |
| Acknowledgement Patterns | PASS | `3`, `5`, `8`, `10`, `18`, `22` all receive direct acknowledgement. |
| Communication Economy and Style | PASS | Concise, compressed traffic with longer content only in condition reports. |

Critical issues:
- None.

Moderate issues:
- None.

Minor issues:
- `19` slightly softens the earlier closure in `12` and `17` by shifting from full closure to conditional access handling. This is still realistic, but it introduces a small wording wobble in how the traffic unit frames the access state.

Good structural qualities:
- `10` is a good example of dependent tasking: the attack is delayed until cooling is established, and `13` then supports `14`.
- The unresolved task state in `20` and the continued order in `22` -> `23` preserve realistic incompleteness rather than forcing artificial closure.

Scenario verdict: `PASS`

Explicit pass/fail judgment: `PASS`

### S5 - Dachstockbrand Reihenhaus

Criterion scores:

| Criterion | Score | Notes |
| --- | --- | --- |
| Message Structure Validity | PASS | Most transmissions are structurally clear and recognisable as radio utterances. |
| Protocol Adherence | PARTIAL | `13` is labelled as `Meldung` but contains an operational instruction (`Abschluss nach dem Abloeschen melden`), so the message type does not match the function. |
| Turn-Taking Plausibility | PASS | Tasking and follow-up responses are coherent; no irrelevant unit answers. |
| Communication Flow Realism | PASS | The scenario progresses plausibly from setup to opening, extinguishment, final thermal check, and handover. |
| Acknowledgement Patterns | PASS | Main commands are acknowledged in compressed but credible form. |
| Communication Economy and Style | PASS | Strongly compressed, field-like phrasing with only modest expansion where needed. |

Critical issues:
- None.

Moderate issues:
- `13`: `An Angriffstrupp von Einsatzleitung, Meldung: Glut in zwei Sparrenfeldern bestaetigt, Abschluss nach dem Abloeschen melden` uses `Meldung` even though the second clause is a directed instruction. Structurally this should be a `Befehl`, or the instruction should be separated from the report-style confirmation.

Minor issues:
- `13` also omits `Schluss`.

Good structural qualities:
- `4` -> `5` -> `11`, `9` -> `10` -> `12` -> `17`, and `15` -> `16` -> `18` -> `19` -> `20` form strong multi-step exchanges.
- `21` -> `22` is a plausible closing coordination exchange after the monitored tasks are completed.

Scenario verdict: `PASS`

Explicit pass/fail judgment: `PASS`

## Dataset-Level Assessment

Overall strengths:
- The dataset consistently preserves interpretable sender ownership and message intent.
- The scenarios do not collapse into rigid artificial ping-pong; they include realistic status self-reports and interleaving.
- Task progression is usually incremental, with intermediate reports before completion.
- Communication style is generally compressed and compatible with both stricter and noisier transcript representations.

Cross-dataset critical issues:
- None.

Cross-dataset moderate issues:
- Message-type discipline weakens in a few places. The clearest case is S5 `13`, where a turn marked `Meldung` performs an instruction.
- Some directed command-like turns reduce acknowledgement structure too far, especially S2 `19` -> `20`, where the link between instruction and acknowledgement is weaker than elsewhere in the dataset.

Cross-dataset minor issues:
- Recurrent omission of `Schluss` in short acknowledgements: S1 `15`, S2 `13`, S3 `13`, S5 `13`.
- Multi-recipient / broadcast structure is used conservatively. This avoids confusion, but it also means the dataset under-tests ordered multi-station acknowledgement behavior described in the speaking-rules guidance.
- The dataset is slightly cleaner than the real-transcript notes in one respect: there is little spelling/protocol noise beyond reduced closures. That is acceptable, but it narrows realism variation.

Representation-coherence assessment:
- The dataset remains coherent under stricter transcript representations because sender, addressee, and action ownership are usually explicit.
- The dataset also remains coherent under noisier transcript representations because the compressed turns still preserve task traceability.
- The main structural fragility is not interpretability but inconsistency in how formal markers are applied. This matters most if downstream evaluation assumes message-type labels are functionally reliable.

Overall dataset verdict: `PASS`

Explicit overall pass/fail judgment: `PASS`

## Concrete Revision List

1. Normalize short acknowledgements that currently omit closure by appending `Schluss` where no realism reason exists to omit it: S1 `15`, S2 `13`, S3 `13`, S5 `13`.
2. In S5 `13`, change the message type from `Meldung` to `Befehl`, or split the confirmation and the instruction into two turns so the label matches the function.
3. In S2 `19` -> `20`, strengthen the acknowledgement link by either adding `antworten` to `19` and a direct acknowledgement in `20`, or by rephrasing `19` as a one-sided instruction not expecting immediate reply.
4. In S1 `1` -> `2`, tighten the multi-recipient response logic by making `2` first acknowledge the opening call more explicitly before reporting movement, or by turning `1` into a pure broadcast not requesting both units to answer.
5. Add at least one scenario in a future dataset revision that exercises ordered multi-unit acknowledgements after `An Alle ... [unit] antworten`, because the current set does not really test that structure.
