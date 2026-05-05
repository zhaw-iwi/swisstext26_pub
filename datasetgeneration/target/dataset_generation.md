# dataset_generation.md

## 1. Generation Objective

* Generate reproducible, research grade synthetic firefighter radio communication scenarios in German for task state monitoring.
* Each scenario must contain:

  * a realistic radio message sequence
  * a fixed list of predefined tasks
  * gold task state labels derived strictly from the message sequence
* All generated samples must be grounded in:

  * `source_notes_sprechregeln.md` for communication structure and protocol constraints
  * `source_notes_real_transcript.md` for surface realism, compression, variability, and controlled irregularity
  * `source_notes_einsatzfuehrung.md` for operational validity, task sequencing, role realism, and completion evidence

---

## 2. Fixed Target Schema

## 2.1 Schema Status

* The schema is fixed.
* No additional top level fields are allowed.
* No additional nested fields are allowed unless explicitly listed below.
* Field names must match exactly.
* Data types must match exactly.
* All generated scenarios must conform exactly to this structure.

## 2.2 Fixed JSON Structure

```json
{
  "scenario_id": "string",
  "scenario_name": "string",
  "metadata": {
    "language": "de",
    "domain": "firefighter_radio",
    "synthetic": true
  },
  "messages": [
    {
      "id": "integer",
      "speaker": "string",
      "text": "string"
    }
  ],
  "predefined_tasks": [
    {
      "task_id": "string",
      "task_name": "string"
    }
  ],
  "gold_task_states": [
    {
      "task_id": "string",
      "assigned": "boolean",
      "assigned_unit": "string",
      "completed": "boolean",
      "completion_outcome": "string"
    }
  ]
}
```

---

## 3. Field Constraints

## 3.1 Top Level Fields

### `scenario_id`

* Type: string
* Required: yes
* Must uniquely identify the scenario within the dataset
* Recommended format:

  * `S1`
  * `S2`
  * `S3`
  * or another fixed, consistent string identifier pattern

### `scenario_name`

* Type: string
* Required: yes
* Must be a concise scenario label
* Should describe the operational situation at scenario level
* Examples of valid style:

  * `Wohnhausbrand`
  * `Kuechenbrand Mehrfamilienhaus`
  * `Tiefgaragenbrand`

### `metadata`

* Type: object
* Required: yes
* Must contain exactly the following fixed values:

  * `"language": "de"`
  * `"domain": "firefighter_radio"`
  * `"synthetic": true`

### `messages`

* Type: array of objects
* Required: yes
* Must contain the complete radio communication sequence for the scenario

### `predefined_tasks`

* Type: array of objects
* Required: yes
* Must define the task inventory to be monitored in the scenario

### `gold_task_states`

* Type: array of objects
* Required: yes
* Must contain exactly one gold label object per task listed in `predefined_tasks`

---

## 3.2 Message Object Constraints

Each entry in `messages` must contain exactly:

### `id`

* Type: integer
* Required: yes
* Must be unique within the scenario
* Must be strictly increasing
* Should begin at `1`
* Must reflect chronological order of utterances

### `speaker`

* Type: string
* Required: yes
* Must identify the speaking role or unit
* Must be operationally plausible for the scenario
* Must be consistent across the scenario
* Examples of valid style:

  * `Einsatzleitung`
  * `Angriffstrupp`
  * `Wassertrupp`
  * `Atemschutztrupp`
  * `Lueftungstrupp`
  * `Sicherungstrupp`

### `text`

* Type: string
* Required: yes
* Must be a single radio utterance
* Must be in German
* Must reflect firefighter radio communication style
* Must be interpretable without external hidden annotations

---

## 3.3 Predefined Task Object Constraints

Each entry in `predefined_tasks` must contain exactly:

### `task_id`

* Type: string
* Required: yes
* Must uniquely identify the task within the scenario
* Must be referenced by exactly one item in `gold_task_states`
* Recommended format:

  * `T1`
  * `T2`
  * `T3`

### `task_name`

* Type: string
* Required: yes
* Must express one monitorable operational task
* Must be concise
* Must be operationally realistic
* Must be specific enough that assignment and completion can be inferred from messages

---

## 3.4 Gold Task State Object Constraints

Each entry in `gold_task_states` must contain exactly:

### `task_id`

* Type: string
* Required: yes
* Must match one existing `task_id` from `predefined_tasks`

### `assigned`

* Type: boolean
* Required: yes
* Indicates whether the task was explicitly assigned in the scenario

### `assigned_unit`

* Type: string
* Required: yes
* Must name the operational unit assigned to the task
* Must match the message content and scenario speaker inventory

### `completed`

* Type: boolean
* Required: yes
* Indicates whether the task was completed within the scenario based on message evidence

### `completion_outcome`

* Type: string
* Required: yes
* Must be the textual completion evidence associated with that task
* Must correspond to an utterance in `messages`
* Must be consistent with the operational doctrine and observed communication
* Must not invent evidence absent from the message sequence

---

## 4. Invariants

* `metadata.language` must always be `de`
* `metadata.domain` must always be `firefighter_radio`
* `metadata.synthetic` must always be `true`
* Every `predefined_tasks.task_id` must appear exactly once in `gold_task_states.task_id`
* Every `gold_task_states.task_id` must correspond to an existing predefined task
* `messages.id` must define the temporal order of the scenario
* `completion_outcome` must be traceable to the message sequence
* No field may be omitted
* No undeclared field may be added

---

## 5. Generation Rules

## 5.1 Message Sequence Construction

* Generate a chronologically coherent incident level radio sequence.
* The sequence must contain enough evidence to infer:

  * who was assigned each task
  * whether the task was completed
  * what utterance serves as completion evidence
* Messages must include a realistic mix of:

  * task assignments
  * acknowledgements
  * progress reports
  * status updates
  * requests
  * completion signals
* The sequence must remain interpretable even when controlled irregularities are included.

## 5.2 Assignment Evidence Rule

* A task may only be labeled as assigned when the message sequence contains explicit assignment evidence.
* Assignment evidence should usually appear as:

  * command to a named unit
  * operational request to a named unit that clearly establishes responsibility
* Preferred evidence pattern:

  * `An [unit] von [command] Befehl: ...`
* Controlled variants may omit ideal protocol framing if the responsible unit and assigned action remain clear.

## 5.3 Completion Evidence Rule

* A task may only be labeled as completed when the message sequence contains explicit, plausible completion evidence.
* Completion evidence must be operationally adequate for the task type.
* Completion evidence must be observable, reportable, or verifiable by the reporting role.
* Examples of acceptable completion evidence:

  * water supply established
  * search completed with result
  * smoke reduced after ventilation
  * road secured and access free
  * fire knocked down and no open fire visible
  * negative final measurements
  * handover readiness confirmed
* Completion evidence must align with `source_notes_einsatzfuehrung.md` and `source_notes_real_transcript.md`.

## 5.4 Unit Consistency Rule

* `assigned_unit` must be consistent with:

  * the named assignee in the assignment message
  * the role capability implied by the task
  * the later reporting messages
* Units must not complete tasks outside plausible operational scope unless reassignment is explicitly communicated.

## 5.5 Task Inventory Rule

* `predefined_tasks` must include only tasks intended for monitoring.
* Each task must be actionable and scenario specific.
* Tasks must correspond to operations that can plausibly be assigned and reported over radio.
* Avoid abstract or purely internal cognitive tasks.

## 5.6 Traceability Rule

* Every gold label must be recoverable from the message sequence alone.
* No gold label may require hidden knowledge.
* Task definitions, assignments, and completions must be mutually consistent.

---

## 6. Realism Constraints

## 6.1 Communication Realism

Consult `source_notes_sprechregeln.md` for protocol structure and `source_notes_real_transcript.md` for practical variation.

Generation must reflect:

* explicit sender and receiver naming in many messages
* frequent use of short formulaic transmissions
* occasional longer tactical updates when justified
* acknowledgement patterns such as:

  * `verstanden`
  * `antworten`
  * `richtig`
  * `schluss`
* controlled omission of ideal markers in some cases
* compressed field language rather than polished prose

## 6.2 Operational Realism

Consult `source_notes_einsatzfuehrung.md`.

Scenarios must reflect:

* standing mission priorities:

  * sichern
  * retten
  * halten
  * schuetzen
  * bewaeltigen
* plausible incident phase progression
* role consistent assignments
* realistic dependencies between tasks
* dynamic updates under uncertainty
* control of hazards before or alongside deeper tactical action

## 6.3 Incident Plausibility

* Scenario progression must be physically and tactically plausible.
* New facts may emerge over time.
* Decisions can occur with incomplete information.
* Resource use, timing, and task ordering must remain believable.
* Messages must remain within firefighter radio scope.

---

## 7. Variability Requirements

Each scenario should vary along several controlled dimensions while preserving schema stability.

## 7.1 Surface Variation

* degree of protocol completeness
* phrasing of acknowledgements
* terse versus expanded status messages
* explicit versus elliptical wording
* amount of paraphrase in readback

## 7.2 Operational Variation

* task family mix
* number of units involved
* number of monitored tasks
* incident stage at which new information appears
* need for escalation, support, or handover

## 7.3 Structural Variation

* simple one step assignments
* interleaved multi unit updates
* partial readbacks
* mid incident reassessment
* broadcast messages alongside directed messages

---

## 8. Difficulty Requirements

Scenarios should include controlled difficulty relevant to task state monitoring.

### Easy cases

* explicit assignment
* explicit completion
* same unit assigns and reports clearly
* minimal ambiguity

### Moderate cases

* paraphrased readback
* completion expressed in natural shorthand
* multiple active tasks interleaved
* some protocol markers omitted

### Hard cases

* overlapping task progress from several units
* completion implied through operationally valid evidence rather than literal task repetition
* delayed acknowledgements
* interrupted or non linear sequencing
* ambiguous or partial updates that do not yet justify completion

Difficulty must not destroy traceability or label reliability.

---

## 9. Negative and Edge Cases

Scenarios should include negative and edge cases, but labels must remain exact.

## 9.1 Missing Acknowledgement

* A task may be clearly assigned even if the ideal acknowledgement is missing.
* The gold state should still reflect assignment if responsibility is explicit.

## 9.2 Ambiguous Progress Update

* Progress messages that show work underway but not completion must not be labeled as completed.
* Example patterns:

  * work in progress
  * search ongoing
  * ventilation continuing
  * control running

## 9.3 Incomplete Task

* A task may be assigned but not completed by scenario end.
* In such cases:

  * `assigned: true`
  * `completed: false`
* `completion_outcome` must still remain within the fixed schema and should contain the best available task state evidence from the messages only if your pipeline expects a string in all cases.
* Because the provided example does not show incomplete tasks, preserve the field exactly as a string and ensure dataset wide handling is consistent.

## 9.4 Reassignment or Command Transfer

* If responsibility changes, this must be explicit in the messages.
* `assigned_unit` should reflect the unit that holds the task in the gold labeling policy adopted for the dataset.
* Any reassignment policy must be applied consistently across the dataset.

## 9.5 Contradictory Reports

* Contradictory reports may appear as realism elements.
* Final gold labels must follow the strongest chronologically supported evidence.
* Contradictions should be resolvable from the message sequence.

## 9.6 Task Without Valid Completion Signal

* A task is not completed unless completion evidence is operationally sufficient.
* Generic statements like `verstanden` or `laeuft` are not completion evidence.

---

## 10. Content Constraints for `messages`

* Use German text only.
* Keep one utterance per message object.
* Do not include timestamps inside the schema unless already part of `text`.
* Do not include evaluator comments, annotations, or hidden tags.
* Do not include explanatory narration outside speaker utterances.
* Do not inject source note citations into generated data.

---

## 11. Content Constraints for `predefined_tasks`

* Tasks must be operationally valid according to `source_notes_einsatzfuehrung.md`.
* Tasks should be concrete enough to admit assignment and completion evidence.
* Suitable task families include:

  * water supply
  * interior attack
  * search
  * ventilation
  * traffic control
  * scene safety
  * resource delivery
  * containment
  * final control
  * handover related sub tasks
* Avoid tasks that are:

  * purely mental
  * too vague
  * not communicatively observable
  * outside the plausible role structure

---

## 12. Gold Labeling Procedure

For each predefined task:

1. locate assignment evidence in `messages`
2. determine the responsible unit
3. set `assigned`
4. inspect later messages for operationally valid completion evidence
5. set `completed`
6. copy the completion evidence text into `completion_outcome`
7. verify consistency between:

   * task definition
   * assignment
   * role capability
   * completion evidence

---

## 13. Traceability to Source Notes

## 13.1 `source_notes_sprechregeln.md`

Use for:

* message structure patterns
* sender receiver framing
* content labels such as `Meldung`, `Befehl`, `Anfrage`, `Antwort`
* acknowledgement conventions
* turn taking markers such as `antworten`
* closure markers such as `Schluss`
* brevity and compression rules

## 13.2 `source_notes_real_transcript.md`

Use for:

* realistic wording and compression
* elliptical field phrasing
* variation in acknowledgement style
* non linear sequencing
* imperfect but interpretable protocol adherence
* realistic completion and progress wording
* controlled noise and paraphrastic readback

## 13.3 `source_notes_einsatzfuehrung.md`

Use for:

* valid task families
* role specific responsibilities
* typical task sequences
* dependencies between tasks
* valid completion evidence
* realistic operational progression
* safety and command priorities

---

## 14. Explicit Source Consultation Instruction

When generating each scenario, consult:

* `source_notes_sprechregeln.md` for communication structure
* `source_notes_real_transcript.md` for surface realism
* `source_notes_einsatzfuehrung.md` for task validity

All generation decisions must be traceable to these files.

---

## 15. Reproducibility Rules

* Keep the target schema fixed across the entire dataset.
* Apply one consistent labeling policy for assignment and completion.
* Ensure every gold label is justified by explicit message evidence.
* Avoid hidden assumptions not recoverable from the scenario itself.
* Use only controlled variability that preserves annotation reliability.
* Keep task names and unit names internally consistent within each scenario.

---

## 16. Quality Checklist

Before accepting a generated scenario, verify:

* schema matches exactly
* no extra fields exist
* all required fields are present
* messages are chronologically ordered
* every predefined task has one gold label
* every assigned unit is plausible
* every completed task has valid completion evidence
* communication style matches the source notes
* operational logic matches doctrine
* scenario is realistic and reproducible