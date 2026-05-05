# dataset_validation_content.md

## 1. Objective

* Validate whether a generated scenario is **operationally realistic and task-consistent**.
* Evaluation must be grounded exclusively in:

  * `source_notes_einsatzfuehrung.md`
  * `source_notes_real_transcript.md`

---

## 2. Evaluation Scope

The validator MUST evaluate:

* task realism and validity
* scenario plausibility
* correctness of task assignments
* role consistency
* task sequencing and dependencies
* validity of completion signals
* traceability of gold task states to message evidence

The validator MUST NOT evaluate:

* strict protocol formatting (handled in structure validation)
* stylistic aspects unless they affect interpretability of tasks

---

## 3. Evaluation Criteria

## 3.1 Task Realism

### Criteria

Tasks must align with operational task families defined in `source_notes_einsatzfuehrung.md`:

* command and coordination
* safety and hazard control
* rescue
* fire containment and suppression
* ventilation and smoke control
* traffic and scene organization
* logistics and resource management
* handover and demobilization

Tasks must:

* be actionable
* be communicable over radio
* be observable through updates or completion reports

### Acceptable Patterns (from transcript)

* short operational phrasing
* implicit context (e.g. location omitted but inferable)
* compressed task naming

### Failure Conditions

* tasks that are abstract, vague, or not operational
* tasks outside firefighter domain
* tasks that cannot produce observable completion evidence

---

## 3.2 Scenario Plausibility

### Criteria

Scenario must follow realistic incident evolution from `source_notes_einsatzfuehrung.md`:

* alarm → deployment → arrival → assessment → tasking → execution → stabilization → completion
* dynamic updates and evolving understanding
* decisions based on partial information
* realistic constraints such as access, smoke, hazards

### Acceptable Variations (from transcript)

* non-linear message order
* parallel unit updates
* incomplete early information
* incremental situation clarification

### Failure Conditions

* impossible or contradictory incident progression
* missing critical phases (e.g. no assessment before complex tasking)
* unrealistic instantaneous outcomes without intermediate steps

---

## 3.3 Role and Assignment Correctness

### Criteria

Assignments must follow role constraints:

* Einsatzleitung assigns tasks
* units execute within their functional capability
* sub-units report from their operational perspective

Assignments must:

* identify a responsible unit
* match the unit’s capability (e.g. ventilation not assigned to unrelated role)
* be consistent across messages

### Acceptable Variations

* compressed or indirect assignment phrasing
* paraphrased readbacks
* implicit confirmation of responsibility

### Failure Conditions

* tasks assigned to implausible roles
* conflicting assignments without clarification
* unit completing tasks it was never assigned

---

## 3.4 Task Sequencing and Dependencies

### Criteria

Task order must reflect dependencies defined in `source_notes_einsatzfuehrung.md`:

* safety before deep interior action
* rescue prioritized when applicable
* containment before full resolution
* ventilation linked to smoke conditions
* handover only after stabilization and checks

### Acceptable Patterns

* overlapping tasks when operationally justified
* partial parallelization of independent tasks
* dynamic reordering based on new information

### Failure Conditions

* tasks executed in impossible order
* missing prerequisite steps (e.g. suppression without access)
* handover before control of hazards

---

## 3.5 Completion Signal Validity

### Criteria

Completion must be supported by valid evidence:

* observable or measurable outcome
* reported by a role capable of observing it
* aligned with task type

Valid examples (from sources):

* fire extinguished or no open flame visible
* search completed with result
* road secured and traffic redirected
* smoke reduced after ventilation
* final measurements or checks completed
* handover readiness confirmed

### Acceptable Variations

* paraphrased completion statements
* embedded completion within longer report

### Failure Conditions

* completion claimed without evidence
* weak statements such as:

  * “verstanden”
  * “läuft”
* completion contradicts earlier state without explanation

---

## 3.6 Traceability of Gold Task States

### Criteria

Each `gold_task_states` entry must be derivable from `messages`:

* assignment must be explicitly or clearly inferable
* assigned unit must match message evidence
* completion must be supported by a specific message
* `completion_outcome` must correspond to actual message content

### Acceptable Variations

* paraphrased assignment or completion wording
* slight mismatch in wording but same semantic meaning

### Failure Conditions

* gold label not supported by any message
* wrong assigned unit
* completion outcome not present in messages
* completion marked true without sufficient evidence

---

## 3.7 Consistency Across Scenario

### Criteria

* tasks, assignments, and completions must be internally consistent
* no contradictions across messages and labels
* scenario must maintain a coherent operational picture

### Failure Conditions

* contradictory task states
* unit reports inconsistent with assigned task
* mutually exclusive outcomes without resolution

---

## 4. Scoring Framework

Each criterion is evaluated as:

* PASS
* PARTIAL
* FAIL

### Criteria List

1. Task Realism
2. Scenario Plausibility
3. Role and Assignment Correctness
4. Task Sequencing and Dependencies
5. Completion Signal Validity
6. Traceability of Gold Task States
7. Consistency Across Scenario

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
* OR critical inconsistency in task labeling or scenario logic

---

## 6. LLM-as-a-Judge Prompt Template

Use the following prompt for evaluation:

---

You are evaluating a firefighter radio communication scenario.

Evaluate ONLY content and operational validity.

Ground your judgment strictly in:

* source_notes_einsatzfuehrung.md
* source_notes_real_transcript.md

Do NOT evaluate protocol formatting unless it affects task interpretation.

For the given scenario:

1. Assess the following criteria:

   * Task Realism
   * Scenario Plausibility
   * Role and Assignment Correctness
   * Task Sequencing and Dependencies
   * Completion Signal Validity
   * Traceability of Gold Task States
   * Consistency Across Scenario

2. For each criterion, assign:

   * PASS
   * PARTIAL
   * FAIL

3. Provide a short justification referencing observable evidence.

4. Provide an overall verdict:

   * PASS
   * PARTIAL
   * FAIL

---

## 7. Traceability to Source Notes

### source_notes_einsatzfuehrung.md

* operational task families
* role definitions and constraints
* task sequencing and dependencies
* valid completion evidence
* incident phase logic

### source_notes_real_transcript.md

* realistic phrasing of tasks and reports
* how completion is expressed in practice
* variability in assignment and reporting
* realistic imperfections and compression

All judgments must be explicitly grounded in these sources.

---

## 8. Reproducibility Constraints

* evaluation must rely only on scenario content and source notes
* no external firefighter knowledge allowed
* all decisions must be explainable from observable evidence
* interpretation must be consistent across different evaluators