# STRUCTURE_VALIDATION_REPORT

## Scope
Assessed only structural validity and communication realism, grounded in:

- `.agents/datasetgeneration/dataset_validation_structure.md`
- `.agents/datasetgeneration/source_notes_sprechregeln.md`
- `.agents/datasetgeneration/source_notes_real_transcript.md`

Operational correctness was not evaluated.

## Per-Scenario Assessment

### S1 - Kuechenbrand Mehrfamilienhaus

**Criterion scores**

- Message Structure Validity: PASS
- Protocol Adherence: PARTIAL
- Turn-Taking Plausibility: PASS
- Communication Flow Realism: PASS
- Acknowledgement Patterns: PARTIAL
- Communication Economy and Style: PASS

**What is good**

- The scenario has a clear deployment progression: initial incident picture, tasking, acknowledgements, progress update, then follow-up action.
- Message roles remain interpretable throughout. Sender, recipient, and intent are usually recoverable even when the full ideal structure is shortened.
- Readbacks are compact but still operationally clear, especially `2`, `6`, `8`, `10`, `14`.

**Critical issues**

- None found.

**Moderate issues**

- `12` ends with `antworten`, which allocates a response turn, but no direct response to the `Angriffstrupp` follows. The next transmission is a new order to `Lueftungstrupp` in `13`. This weakens protocol closure for a directed report.

**Minor issues**

- The opening broadcast in `1` is acknowledged only by some units (`2`, `3`), while `Lueftungstrupp` appears only later in `9`. This is still interpretable, but the dataset uses broadcast structure loosely.
- `10` is a plausible acknowledgement, but it is more conversational than the tighter protocol style used elsewhere.

**Overall verdict**

- Overall verdict: PASS
- Pass/fail judgment: PASS

### S2 - Tiefgaragenbrand Wohnblock

**Criterion scores**

- Message Structure Validity: PASS
- Protocol Adherence: PARTIAL
- Turn-Taking Plausibility: PASS
- Communication Flow Realism: PASS
- Acknowledgement Patterns: PARTIAL
- Communication Economy and Style: PASS

**What is good**

- The scenario has realistic interleaving: self-initiated status in `2`, command traffic in `3` and `4`, later measurement coordination in `9` to `13`.
- The phrasing is compressed and mostly radio-like. Messages such as `8`, `11`, and `13` are plausible short field reports.
- Different interaction types are present: assignment, acknowledgement, progress report, follow-up order, and technical status update.

**Critical issues**

- None found.

**Moderate issues**

- `7` ends with `antworten`, but no direct response from `Einsatzleitung` follows.
- `8` also ends with `antworten`, but the following traffic shifts to a new unit in `9`.
- `12` is functionally a release/start instruction to `Messgruppe`, but it is labeled `Meldung` rather than `Befehl`. Because it directs action, this is a protocol mismatch.

**Minor issues**

- `2`, `5`, and `10` omit `Schluss` and formal addressing. This is acceptable under realistic compression, but the scenario relies on this relaxation repeatedly.
- `10` uses `korrekt` as a short acknowledgement without explicit sender/receiver framing. Plausible, but structurally light.

**Overall verdict**

- Overall verdict: PASS
- Pass/fail judgment: PASS

### S3 - Kellerbrand Schulhaus

**Criterion scores**

- Message Structure Validity: PASS
- Protocol Adherence: PARTIAL
- Turn-Taking Plausibility: PASS
- Communication Flow Realism: PASS
- Acknowledgement Patterns: PARTIAL
- Communication Economy and Style: PASS

**What is good**

- The scenario remains easy to follow at transcript level: perimeter control, water supply, attack line, then fire control.
- The tasking chain is plausible and compact. `2` to `5`, `3` to `4` and `9`, and `7` to `8` to `13` form readable subthreads.
- Units generally report only what they could plausibly observe within the transcript.

**Critical issues**

- Transcript-to-label coherence breaks for task completion. `gold_task_states.T3` marks the attack task as completed with completion outcome message `11`, but `11` says `Kontrolle im Installationsschacht laeuft noch`. That is not a completion report. The actual completion-style closure is closer to `13`. This is an internal representation inconsistency, not just a protocol variation.

**Moderate issues**

- `12` is a directed follow-up instruction but labeled `Meldung` instead of `Befehl`.
- `9`, `10`, and `11` all end with `antworten`, yet none receives an explicit direct reply. This creates repeated incomplete turn allocation.

**Minor issues**

- `4` and `8` omit `Schluss`. Acceptable individually, but consistent omission reduces protocol discipline.

**Overall verdict**

- Overall verdict: FAIL
- Pass/fail judgment: FAIL

### S4 - Werkstattbrand mit Gasflaschen

**Criterion scores**

- Message Structure Validity: PASS
- Protocol Adherence: PARTIAL
- Turn-Taking Plausibility: PASS
- Communication Flow Realism: PASS
- Acknowledgement Patterns: PARTIAL
- Communication Economy and Style: PASS

**What is good**

- The scenario has strong operational-radio compression. `8`, `9`, and `10` are short, specific, and easy to map to ongoing tasks.
- Interleaving is realistic: traffic control, extinguishment, and cooling updates proceed in parallel.
- The unfinished state of the gas bottle cooling task is represented coherently in the transcript and in `gold_task_states`.

**Critical issues**

- None found.

**Moderate issues**

- `11` directs continued action to `Wassertrupp` but is labeled `Meldung` instead of `Befehl`.
- `8`, `9`, and `10` all end with `antworten`, but only `10` receives a direct follow-up, and even there the answer is a continuation order rather than a clean acknowledgement chain.

**Minor issues**

- `3` and `5` are minimal acknowledgements without `Schluss`. Plausible, but structurally lighter than the surrounding messages.

**Overall verdict**

- Overall verdict: PASS
- Pass/fail judgment: PASS

### S5 - Dachstockbrand Reihenhaus

**Criterion scores**

- Message Structure Validity: PASS
- Protocol Adherence: PARTIAL
- Turn-Taking Plausibility: PASS
- Communication Flow Realism: PASS
- Acknowledgement Patterns: PARTIAL
- Communication Economy and Style: PASS

**What is good**

- This is the strongest scenario structurally. It shows a plausible sequence from initial size-up through access setup, attack, secondary control, and handover readiness.
- The interaction types vary appropriately: terse self-status (`2`, `3`), formal orders (`4`, `6`, `10`), progress update (`9`), completion reports (`12`, `13`), and final handover signal (`14`).
- The secondary control by `Sicherungstrupp` after attack completion is coherent under the transcript representation.

**Critical issues**

- None found.

**Moderate issues**

- `9` and `12` end with `antworten`, but no explicit direct acknowledgement follows either message.

**Minor issues**

- `2`, `3`, `5`, `7`, and `11` are compressed and omit `Schluss`. This is realistic, but the dataset again leans on omitted closure markers.
- `13` appears after the attack completion in `12` without an explicit release message from `Einsatzleitung`; this is still inferable from context, so it is only a minor structural looseness.

**Overall verdict**

- Overall verdict: PASS
- Pass/fail judgment: PASS

## Dataset-Level Assessment

### Cross-Dataset Strengths

- All five scenarios are interpretable as radio incidents with clear speaker identity and readable task progression.
- The dataset consistently mixes short acknowledgements, assignment turns, progress reports, and completion-style reports.
- Interleaving across units is present in multiple scenarios, which is closer to the real-transcript notes than a purely linear dialogue.
- The language is generally compressed and operational rather than narrative.

### Cross-Dataset Critical Issues

- Scenario `S3` contains a transcript-to-label coherence error: the declared completion outcome for `T3` does not actually express completion. This breaks reliability under downstream transcript/task-state representations.

### Cross-Dataset Moderate Issues

- The dataset systematically overuses `antworten` on status and progress messages without supplying the corresponding reply turn. This pattern appears in `S1:12`, `S2:7`, `S2:8`, `S2:11`, `S3:9`, `S3:10`, `S3:11`, `S4:8`, `S4:9`, `S4:10`, `S5:9`, `S5:12`.
- Several directed follow-up instructions are labeled `Meldung` although they function as commands. Clear cases: `S2:12`, `S3:12`, `S4:11`.
- Closure discipline is repeatedly loosened in acknowledgements and short status turns. This is realistic in moderation, but here it is a recurrent dataset pattern rather than occasional controlled noise.

### Cross-Dataset Minor Issues

- Broadcast handling is simplified. Scenarios often open with `An Alle`, but do not establish a consistent convention for whether acknowledgements are expected.
- The dataset is somewhat template-heavy. Many scenarios follow a very similar structure: incident broadcast, 2 to 3 formal taskings, compressed acknowledgements, mid-task report, completion report. This is not invalid, but it reduces realism variety.

## Overall Judgment

- Overall verdict: FAIL
- Overall pass/fail judgment: FAIL

Reason:

- Four scenarios are structurally usable, but one scenario (`S3`) fails due to an internal transcript-to-label coherence error.
- In addition, the recurring `antworten` without reply pattern is systematic enough that the dataset should not be treated as cleanly validated yet.

## Concrete Revision List

1. Fix `S3` task-state coherence:
   - Change `gold_task_states` for `T3` so the completion outcome points to a true completion-style message, most likely `13`, or revise message `11` so it actually expresses completed control.

2. Audit every message ending with `antworten`:
   - Either add a direct reply turn after the message or remove `antworten` when no response is intended.
   - Priority messages: `S1:12`, `S2:7`, `S2:8`, `S2:11`, `S3:9`, `S3:10`, `S3:11`, `S4:8`, `S4:9`, `S4:10`, `S5:9`, `S5:12`.

3. Relabel directed action messages from `Meldung` to `Befehl` where they function as commands:
   - `S2:12`
   - `S3:12`
   - `S4:11`

4. Normalize closure usage selectively:
   - Keep some realistic omissions, but ensure the dataset does not omit `Schluss` so often that it becomes the dominant pattern in acknowledgements.

5. Make broadcast handling consistent:
   - Decide whether `An Alle` messages in this dataset representation usually require acknowledgements.
   - Apply that choice consistently across all scenarios.

6. Increase variation in protocol looseness:
   - Some scenarios can stay more formal, others more compressed, but the current dataset repeats the same structure and the same kinds of omissions too uniformly.
