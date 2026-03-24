# dataset_validation_structure.md

## 1. Objective

* Validate whether a generated scenario adheres to:

  * radio communication protocol structure
  * message formatting conventions
  * turn-taking plausibility
  * communication flow realism
* Evaluation must be grounded exclusively in:

  * `source_notes_sprechregeln.md`
  * `source_notes_real_transcript.md`

---

## 2. Evaluation Scope

The validator MUST evaluate:

* message structure correctness
* protocol marker usage
* turn-taking behavior
* acknowledgement structure
* sequencing plausibility
* communication economy and style

The validator MUST NOT evaluate:

* task realism
* operational correctness of decisions
* domain-level task validity

---

## 3. Evaluation Criteria

## 3.1 Message Structure Validity

### Criteria

Each message should reflect recognizable structure patterns derived from `source_notes_sprechregeln.md`:

* presence of identifiable sender and/or receiver
* use of communication intent markers when applicable:

  * `Meldung`
  * `Befehl`
  * `Anfrage`
  * `Antwort`
  * `Verbindungskontrolle`
* structured phrasing such as:

  * `An [Empfänger] von [Absender]`
* use of turn control marker:

  * `antworten`
* optional closure marker:

  * `Schluss`

### Acceptable Variations (from `source_notes_real_transcript.md`)

* omission of some formal elements if intent remains clear
* compressed phrasing without full formal syntax
* partial adherence to protocol markers
* informal but interpretable structure

### Failure Conditions

* messages that are not interpretable as radio utterances
* missing identifiable speaker intent
* structure so degraded that assignment or response cannot be inferred

---

## 3.2 Protocol Adherence

### Criteria

Messages should reflect protocol rules:

* commands are typically acknowledged
* directed communication uses explicit addressing
* responses follow requests or commands
* communication uses standard phrases:

  * `verstanden`
  * `richtig`
  * `schluss`
  * `wiederholen` (optional)
* channel discipline:

  * no excessive simultaneous or conflicting turns

### Acceptable Deviations

* missing acknowledgement in some cases
* shortened acknowledgement forms
* variation in confirmation wording (`korrekt`, `richtig`)
* occasional omission of `schluss`

### Failure Conditions

* systematic absence of acknowledgements for all commands
* contradictory protocol usage that prevents interpretation
* messages violating basic communication logic

---

## 3.3 Turn-Taking Plausibility

### Criteria

Derived from both source files:

* turns follow logical request-response patterns
* "antworten" or implicit turn allocation is respected in most cases
* only the addressed unit responds when explicitly called
* multi-party responses occur in plausible order

### Acceptable Deviations

* occasional missing "antworten"
* slight disorder in response sequence under stress
* broadcast messages without full ordered replies

### Failure Conditions

* multiple units responding simultaneously without structure
* responses from units that were not addressed and not contextually relevant
* missing responses where required for interpretation

---

## 3.4 Communication Flow Realism

### Criteria

Derived from `source_notes_real_transcript.md`:

* mixture of:

  * assignments
  * acknowledgements
  * status updates
  * progress reports
  * completion reports
* non-linear but interpretable sequencing
* interleaving of different unit communications
* realistic progression of interaction types

### Acceptable Patterns

* parallel updates from multiple units
* interleaving command and status traffic
* variable message length
* occasional repetition or paraphrasing

### Failure Conditions

* purely linear artificial dialogue without variability
* unrealistic isolation of units without interaction
* absence of key communication types (e.g., no acknowledgements at all)

---

## 3.5 Acknowledgement Patterns

### Criteria

* acknowledgements exist for key actions:

  * commands
  * important updates
* acknowledgement forms align with:

  * `verstanden`
  * paraphrased confirmations
* readbacks may be:

  * exact
  * paraphrased

### Acceptable Deviations

* incomplete readbacks
* shortened confirmations
* paraphrased acknowledgements

### Failure Conditions

* no acknowledgement behavior present
* acknowledgements that contradict original message meaning

---

## 3.6 Communication Economy and Style

### Criteria

From both source files:

* messages are generally:

  * short
  * direct
  * compressed
* operational shorthand is used
* minimal unnecessary language
* clear operational meaning despite brevity

### Acceptable Deviations

* occasional longer messages for:

  * situation reports
  * tactical explanations
* minor grammatical or spelling inconsistencies

### Failure Conditions

* overly verbose narrative style
* non-operational conversational language
* lack of compression inconsistent with radio communication

---

## 4. Scoring Framework

Each criterion is evaluated as:

* PASS
* PARTIAL
* FAIL

### Criteria List

1. Message Structure Validity
2. Protocol Adherence
3. Turn-Taking Plausibility
4. Communication Flow Realism
5. Acknowledgement Patterns
6. Communication Economy and Style

---

## 5. Pass / Fail Decision Rules

### PASS (overall)

* no criterion marked FAIL
* at most 2 criteria marked PARTIAL

### PARTIAL (overall)

* 1–2 criteria marked FAIL
* OR more than 2 criteria marked PARTIAL

### FAIL (overall)

* 3 or more criteria marked FAIL
* OR critical breakdown in interpretability

---

## 6. LLM-as-a-Judge Prompt Template

Use the following prompt for evaluation:

---

You are evaluating a firefighter radio communication scenario.

Evaluate ONLY structural and communication aspects.

Ground your judgment strictly in:

* source_notes_sprechregeln.md
* source_notes_real_transcript.md

Do NOT evaluate operational correctness.

For the given scenario:

1. Assess the following criteria:

   * Message Structure Validity
   * Protocol Adherence
   * Turn-Taking Plausibility
   * Communication Flow Realism
   * Acknowledgement Patterns
   * Communication Economy and Style

2. For each criterion, assign:

   * PASS
   * PARTIAL
   * FAIL

3. Provide a short justification referencing observable patterns.

4. Provide an overall verdict:

   * PASS
   * PARTIAL
   * FAIL

---

## 7. Traceability to Source Notes

### source_notes_sprechregeln.md

* message structure requirements
* protocol rules
* acknowledgement conventions
* turn-taking structure
* communication brevity principles

### source_notes_real_transcript.md

* realistic deviations from protocol
* elliptical and compressed phrasing
* sequencing irregularities
* acknowledgement variability
* noise and imperfection patterns

All evaluation decisions must be justifiable through these sources.

---

## 8. Reproducibility Constraints

* evaluator must not rely on external firefighter knowledge
* all judgments must be based on observable message content
* deviations are acceptable if consistent with documented real-world patterns
* interpretation must remain consistent across scenarios