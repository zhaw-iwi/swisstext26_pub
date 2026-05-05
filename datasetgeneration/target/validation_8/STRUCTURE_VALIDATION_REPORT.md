# Structure Validation Report

## Scope

Assessment basis:
- `./.agents/datasetgeneration/dataset_validation_structure.md`
- `./.agents/datasetgeneration/source_notes_sprechregeln.md`
- `./.agents/datasetgeneration/source_notes_real_transcript.md`

Assessment limits:
- Evaluated: structural validity and communication realism only
- Not evaluated: operational correctness, tactics, or domain decision quality

Pass/fail rule used:
- Scenario `PASS`: no criterion `FAIL` and at most 2 criteria `PARTIAL`
- Scenario `FAIL`: otherwise

Transcript-representation check:
- I also checked whether each scenario remains interpretable under the repository’s intended transcript forms: `structured_dialogue`, `no_speaker`, and `continuous_transcript`

---

## Per-Scenario Assessment

### S1: Kuechenbrand Mehrfamilienhaus

**Criterion ratings**
- Message Structure Validity: `PASS`
- Protocol Adherence: `PARTIAL`
- Turn-Taking Plausibility: `PASS`
- Communication Flow Realism: `PASS`
- Acknowledgement Patterns: `PASS`
- Communication Economy and Style: `PASS`

**What is good**
- The scenario has a clear command chain: reconnaissance (`m4`), assignment (`m5`, `m7`, `m9`, `m14`), acknowledgement (`m6`, `m8`, `m10`, `m15`), then progress/completion reporting (`m11` to `m16`).
- Messages stay short and compressed. That matches the source notes well.
- The text remains coherent in `no_speaker` and `continuous_transcript` because most turns contain either explicit addressing or a unit self-reference such as `"Angriffstrupp verstanden"`.

**Critical issues**
- None found.

**Moderate issues**
- None found.

**Minor issues**
- `m1` is a broadcast to `"Alle"`, but only two units acknowledge immediately in `m2` and `m3`; the later involved `Lueftungstrupp` does not. Under the stricter speaking-rules note, multi-recipient traffic should collect ordered responses. This is still acceptable because the real-transcript notes allow looser broadcast behavior, but it weakens strict protocol adherence.

**Scenario judgment**
- `PASS`

---

### S2: Tiefgaragenbrand Wohnblock

**Criterion ratings**
- Message Structure Validity: `PASS`
- Protocol Adherence: `PASS`
- Turn-Taking Plausibility: `PASS`
- Communication Flow Realism: `PARTIAL`
- Acknowledgement Patterns: `PASS`
- Communication Economy and Style: `PASS`

**What is good**
- Directed commands are consistently acknowledged: `m3` to `m6`, `m4` to `m5`, `m9` to `m10`, `m12` to `m13`, `m15` to `m16`.
- The scenario contains a realistic mix of assignment, status, partial completion, and non-completion reporting. `m17` clearly keeps the measurement task open instead of forcing an artificial completion.
- Representation robustness is strong. In reduced transcript conditions, unit identity still survives because the utterances frequently self-identify.

**Critical issues**
- None found.

**Moderate issues**
- The communication flow is somewhat too linear and tidy relative to the source transcript notes. After the initial alert, the scenario mostly advances in single-thread blocks: secure power, lay hose, assign attack, assign measurement, then final updates. It is interpretable and plausible, but the overlap is narrower than the source notes’ more interleaved style.

**Minor issues**
- `m12` gives the `Messgruppe` a conditional task `"nach Freigabe"`, while `m15` later issues the actual start command. This is still plausible, but it creates a slightly staged two-step assignment pattern that feels more synthetic than naturally compressed radio traffic.

**Scenario judgment**
- `PASS`

---

### S3: Kellerbrand Schulhaus

**Criterion ratings**
- Message Structure Validity: `PASS`
- Protocol Adherence: `PASS`
- Turn-Taking Plausibility: `PASS`
- Communication Flow Realism: `PASS`
- Acknowledgement Patterns: `PASS`
- Communication Economy and Style: `PASS`

**What is good**
- This is the structurally strongest scenario in the set. The tasking and reporting chain is easy to follow without becoming verbose.
- Turn-taking is plausible: only addressed units acknowledge commands, and unprompted updates come from units already engaged in the incident.
- The transcript remains coherent under all intended renderings because nearly every message carries enough internal identity and task context to survive speaker stripping.

**Critical issues**
- None found.

**Moderate issues**
- None found.

**Minor issues**
- `m11` already reports `"Brand am Trockner abgeloescht"`, and `m12` then issues a follow-up command focused on closing out the shaft check. This is still plausible, but the sequence is slightly staged and cleaner than the more irregular progression described in the real-transcript notes.

**Scenario judgment**
- `PASS`

---

### S4: Werkstattbrand mit Gasflaschen

**Criterion ratings**
- Message Structure Validity: `PASS`
- Protocol Adherence: `PASS`
- Turn-Taking Plausibility: `PASS`
- Communication Flow Realism: `PARTIAL`
- Acknowledgement Patterns: `PASS`
- Communication Economy and Style: `PASS`

**What is good**
- The scenario preserves radio compression while still showing parallel subproblems: perimeter control, extinguishment, and cooling.
- Acknowledgements are consistent and compressed in a realistic way, especially `m4`, `m6`, `m8`, `m13`, `m15`, `m19`.
- The incomplete cooling task is handled well structurally. `m11`, `m17`, and `m19` all keep the state open rather than jumping to closure.

**Critical issues**
- None found.

**Moderate issues**
- The middle and late sequence is somewhat repetitive and linear. `m12` and `m18` both restate that cooling should continue; `m14` also reaffirms a task already completed in `m9`. Reinforcement orders are plausible, but here the pattern reads more like controlled dataset shaping than naturally messy radio flow.

**Minor issues**
- `m2` ends with `"antworten"` although it is an unsolicited reconnaissance report rather than a more formal call-up. This is still interpretable, but slightly formulaic.

**Scenario judgment**
- `PASS`

---

### S5: Dachstockbrand Reihenhaus

**Criterion ratings**
- Message Structure Validity: `PASS`
- Protocol Adherence: `PASS`
- Turn-Taking Plausibility: `PASS`
- Communication Flow Realism: `PASS`
- Acknowledgement Patterns: `PASS`
- Communication Economy and Style: `PASS`

**What is good**
- This scenario has the clearest progression from setup to final handover: ladder readiness, water readiness, opening/search, extinguishment, final control, then transfer.
- Directed calls and acknowledgements are clean and interpretable, and task closure evidence is explicit in `m11`, `m17`, and `m20`.
- It stays coherent in reduced transcript forms because the messages embed both the acting unit and the action itself.

**Critical issues**
- None found.

**Moderate issues**
- None found.

**Minor issues**
- The final handover exchange `m21` to `m22` is structurally plausible, but cleaner and more compressed than the more irregular rapport-style transitions described in the source notes. This is a realism limitation, not a structural failure.

**Scenario judgment**
- `PASS`

---

## Dataset-Level Assessment

**Overall judgment**
- `PASS`

**Why the dataset passes**
- All five scenarios remain interpretable as radio traffic.
- All scenarios contain recognizable sender/receiver structure, assignment logic, acknowledgements, and short operational phrasing.
- None of the scenarios breaks under the intended transcript representations. This is a major structural strength of the dataset: messages usually carry enough identity and action content inside the text itself, so removing speaker labels does not collapse coherence.

**Dataset-level critical issues**
- None found.

**Dataset-level moderate issues**
- The dataset is consistently cleaner and more orderly than the realism profile described in `source_notes_real_transcript.md`. There are few genuine irregularities: almost no missing closures, almost no broken readbacks, no misunderstandings, no repair turns, and very little disorder under pressure.
- Interleaving exists, but most scenarios still progress in a strongly managed command-response pattern. The source notes describe more overlap, more self-initiated updates, and more uneven sequencing than this dataset usually shows.

**Dataset-level minor issues**
- Message-type variety is narrow. The dataset relies heavily on `Meldung` and `Befehl`; `Anfrage`, `Antwort`, and `Verbindungskontrolle` are effectively absent.
- Initial `An Alle` broadcasts are not followed by ordered acknowledgement chains. This is acceptable under the real-transcript notes, but it does diverge from the stricter speaking-rules document.
- The phrasing is very polished across the board. Controlled realism noise exists only lightly.

---

## Cross-Dataset Patterns

### Positive patterns
- Strong self-identification inside message text improves robustness for `no_speaker` and `continuous_transcript`.
- Commands are usually acknowledged promptly and in compressed form.
- Incomplete tasks are represented correctly rather than being forced to completion for convenience.
- Message length is consistently close to realistic radio economy.

### Recurring realism limitations
- Too few imperfect protocol moments compared with the source notes.
- Too little friction in transitions between reconnaissance, command, and completion.
- Too much syntactic regularity across scenarios; several sequences read as deliberately templated rather than naturally varied.

---

## Concrete Revision List

1. Add controlled protocol noise to a subset of scenarios: occasional missing `Schluss`, shortened acknowledgements, or a partial readback that still preserves interpretability.
2. Introduce at least a few `Anfrage` or `Antwort`-style turns so the dataset is not almost entirely `Meldung` plus `Befehl`.
3. Make one or two scenarios more interleaved by inserting self-initiated updates from already deployed units between command turns.
4. For broadcast openings, either add sequential acknowledgements or make the broadcast style consistently looser across the dataset so the pattern is clearly intentional.
5. Reduce templated reinforcement commands where no new communication pressure is visible, especially in scenarios like S4.
6. Preserve the current strength of internal self-identification so that `no_speaker` and `continuous_transcript` remain structurally usable.
7. Keep incomplete-task scenarios such as S1, S2, and S4, but diversify how non-completion is phrased so the pattern does not become formulaic.

---

## Final Summary

- S1: `PASS`
- S2: `PASS`
- S3: `PASS`
- S4: `PASS`
- S5: `PASS`
- Overall dataset: `PASS`
