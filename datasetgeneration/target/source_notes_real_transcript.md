# source_notes_real_transcript.md

## 1. Source Scope

### In Scope

* Radio style utterances between operational units
* Dispatch style alerts that trigger deployment
* Status updates on movement, arrival, task progress, and completion
* Tasking exchanges between command and subordinate roles
* Short acknowledgements and confirmations
* Escalation messages
* Requests for resources or support
* Situation reports from operational subareas
* Transfer of command messages
* Completion evidence communicated over radio
* Multi party coordination tied directly to the incident

### Out of Scope

* Rich tactical reasoning not normally spoken over radio unless explicitly present in transcript
* Long formal meeting style dialogue except where it appears as a recorded operational rapport
* Non operational commentary such as transcript annotations for the evaluator
* Meta instructions to the AI such as plan lookup comments
* Pure timestamping or logging metadata
* Orthographic errors as targets to preserve exactly rather than model as optional noise
* Highly object specific planning artifacts unless generalized into realistic operational references

---

## 2. Utterance Style and Phrasing Variability

### High Frequency Surface Forms

* Unit self status reports are short and formulaic

  * "Kolin 7 rückt aus"
  * "Kolin 11 im Warteraum"
  * "Kolin 21 vor Ort"
  * "Kolin 7 rückt ein"
* Directed calls often compress sender and receiver naming

  * "Kolin 20 von Kolin 7, antworten"
  * "Kolin 9 von 153, antworten"
  * "Offizier auf Kolin 6 von Kolin 7, antworten"
* Acknowledgements vary in completeness

  * "verstanden"
  * "Verstanden, antworten"
  * "Kolin 1 verstanden"
  * "Richtig, Schluss"
  * "Korrekt, Schluss"

### Mixed Register

* Some transmissions closely follow protocol formulae
* Others move into freer operational speech with longer task oriented sentences
* Register shifts with function

  * movement and availability updates are short
  * reconnaissance findings are longer and more descriptive
  * task assignments often combine situation, intent, and assignment in one turn

### Lexical Variability

* Repeated core verbs with variation

  * "rückt aus"
  * "vorziehen"
  * "einrichten"
  * "erstellen"
  * "schicken"
  * "beginnen"
  * "aufheben"
  * "übergeben"
* Similar intents can be phrased differently

  * "Brand Mittel via ZuPo eskalieren"
  * "Einsatz bei ZuPo auf Brand Mittel eskalieren"

---

## 3. Elliptical and Implicit Communication

### Frequent Ellipsis

* Articles, subjects, and full sentence framing are often omitted
* Operational shorthand assumes shared context

  * "vorziehen auf Parkplatz oberhalb Pulverturm"
  * "Anleiterbereitschaft auf Zugerbergstrasse erstellen"
  * "keine weiteren Mittel ausrücken lassen"
* Many messages omit explicit message type labels even when the function is clearly a command or report

### Implicit Context Recovery

* Units infer location, task, and incident context from previous turns
* Replies often restate only the actionable core

  * order received as full instruction
  * response compresses to task restatement
* Situation updates assume prior knowledge of structure and plan

  * references to kitchen, treppenhaus, 1. Stock, 4. OG without repeated incident framing

### Intent Embedded in Report

* Reports often contain both status and request

  * update on smoke spread plus request for smoke curtain
* Completion claims are embedded in causal narrative

  * cause identified, extinguishment complete, now moving to ventilation

---

## 4. Expression of Status Updates

### Common Status Categories

* Mobilization

  * unit departed
  * personnel composition on departure
* Staging

  * waiting area status
  * moved forward to designated point
* Arrival

  * "vor Ort"
* Occupancy and resource status

  * "besetzt"
* Task execution

  * reconnaissance underway
  * ventilation underway
  * traffic redirection established
* Demobilization

  * stand down of incoming resources
  * unit returns to base

### Typical Status Update Form

* Unit identifier first
* Short action or state phrase second
* Optional resource composition third
* Optional location fourth

### Status Compression Patterns

* Minimal style

  * "[Unit] vor Ort"
  * "[Unit] rückt ein"
* Slightly expanded style

  * "[Unit] rückt aus, [crew composition]"
* Event keyed status

  * "[Unit] vor Ort, Feststellung schwarzer Rauch aus Fenster 1. Stock"

---

## 5. Sequencing Behavior

### Non Linear Operational Flow

* Multiple units update in parallel around the same minute
* Command traffic interleaves with autonomous status updates
* Task assignment, reconnaissance, escalation, and logistics overlap in time

### Multi Step Exchange Pattern

* Call up
* Contact confirmation
* Main instruction or report
* Readback or compressed acknowledgement
* Final confirmation
* Closure

### Deviations from Strict Sequence

* Some exchanges omit one confirmation layer
* Some turns end without explicit "Schluss"
* Some orders are acknowledged without exact protocol order
* Broadcasts to all may not collect individual acknowledgements

### Periodic Coordination Layer

* The transcript includes a structured rapport sequence that aggregates:

  * situation orientation
  * subarea updates
  * requests
  * commander decision
* This introduces a different interaction mode from ordinary radio turns
* Such sequences are realistic but should be modeled as distinct from rapid tactical radio traffic

---

## 6. Irregularities and Noise Patterns

### Surface Noise

* Typos and spelling inconsistencies

  * "Vertanden"
  * "Manschaft"
  * "Einsatzleitzer"
* Inconsistent capitalization and punctuation
* Minor grammatical infelicities are common

### Protocol Noise

* Missing message type labels
* Missing or inconsistent use of "antworten"
* Missing or reduced closure forms
* "Richtig" and "Korrekt" both appear as confirmation forms
* Some acknowledgements are partial rather than full protocol compliant readbacks

### Content Noise

* Repetition of the same status in acknowledgement
* Slight reformulation during readback that preserves intent but changes wording
* Uneven specificity across units

  * some reports give exact crew composition
  * others only mention task or state

### Practical Implication for Dataset

* Noise should be modeled as controlled realism
* Deviations should not make task state uninterpretable
* Imperfect protocol adherence is common and should be expected in realistic samples

---

## 7. Task Assignment and Completion Language

### Assignment Patterns

* Command commonly provides:

  * current situation
  * intended effect
  * explicit area of responsibility
  * location or reporting line
* Example assignment structure in practice

  * situation statement
  * "Ich will ..."
  * "Dein Auftrag ..."
* Shorter assignment variant

  * direct imperative without explicit rationale

### Readback Patterns

* Assignee often restates:

  * responsibility label
  * immediate action
  * resources used
* Readback may be compressed but usually preserves operational core

### Completion Evidence Patterns

* "Brand konnte abgelöscht werden"
* "Strassensperrung ... vorgenommen"
* "Schlussmessungen sind negativ"
* "Einsatzstelle kann der Polizei übergeben werden"
* Valid completion signals often combine:

  * task result
  * residual condition
  * next permissible transition

---

## 8. Role and Responsibility Signals Visible in Transcript

### Command Role

* Escalates incident level
* Assigns subarea responsibilities
* Transfers leadership channel
* Decides on stand down and release of resources

### Subordinate Functional Roles

* Interior operations role reports fire, smoke, containment, extinguishment, ventilation status
* Traffic role reports road closure and diversion status
* Rescue role reports medical check and readiness
* Police role reports investigation readiness and access dependencies

### Dataset Relevant Implication

* Roles are operationally meaningful and not interchangeable
* Messages should reflect what each role can plausibly observe, decide, or request

---

## 9. Realism Constraints Derived from Transcript

* Radio traffic mixes strict protocol fragments with natural operational shorthand
* Messages are usually short but not uniformly short
* Longer descriptive turns occur during reconnaissance and subarea reports
* Units frequently self initiate status updates without being prompted
* Readbacks often paraphrase instead of repeating verbatim
* Command messages often contain both intent and assignment
* Tactical conversation can include resource requests tied to current conditions
* Incident progression should be incremental:

  * dispatch
  * departure
  * arrival
  * hazard recognition
  * escalation
  * tasking
  * mitigation
  * stabilization
  * handover
  * return

---

## 10. Boundaries for Synthetic Dataset Design

### Should Be Included

* Imperfect but interpretable radio protocol
* Elliptical phrasing
* Operational shorthand
* Variable acknowledgement quality
* Concurrent subproblems within one incident
* Evidence based status changes

### Should Be Excluded

* Arbitrary chaos that breaks task traceability
* Long expository dialogue without operational function
* Free form narrative detached from radio exchange structure
* Highly polished language that removes authentic field compression
* Impossible knowledge claims by roles without access to that information

## 11. Actionable Constraints for Generation

* Use a mix of:

  * terse status lines
  * structured call and response
  * longer tactical updates when justified
* Allow omissions of ideal protocol markers in a controlled way
* Preserve interpretability of speaker, task, and state despite noise
* Include paraphrastic acknowledgements rather than exact duplication only
* Model concurrent updates from different units
* Ensure completion claims are supported by observable or reported evidence
* Keep scenario content within plausible fireground coordination scope