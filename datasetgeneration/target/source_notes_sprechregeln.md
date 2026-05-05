# source_notes_sprechregeln.md

## 1. Message Structure Patterns

### Standard Transmission Structure
- Every transmission follows a fixed sequence:
  - **Recipient**: "An [Empfänger]"
  - **Sender**: "von [Absender]"
  - **Message Type (mandatory)**: "Meldung", "Befehl", "Anfrage", "Antwort", "Verbindungskontrolle"
  - **Content**
  - **Turn prompt**: "antworten" (if response expected)
  - **Closure**: "Schluss"

### Example Pattern
- "An [Empfänger] von [Absender], Meldung: [Inhalt], antworten"
- Response:
  - "[Empfänger] Meldung verstanden, antworten"
  - "Verstanden, Schluss"

### Multi-Recipient Pattern
- "An Alle von [Absender], Meldung: ..., [Station] antworten"
- Sequential acknowledgements required from each addressed station

### One-Sided Transmission
- Message sent without response expectation
- May include repetition:
  - "Ich wiederhole: ..."

---

## 2. Communication Protocol Rules

### Mandatory Elements
- Every transmission MUST include:
  - Clear sender and receiver identification
  - Explicit message type label
- Commands ("Befehl") MUST always be acknowledged

### Listening Discipline
- "Zuerst hören, dann sprechen"
- Avoid simultaneous transmissions

### Channel Switching
- Channel change only executed AFTER:
  - All stations acknowledge receipt

### Information Security
- No classified information over unprotected channels
- Transmission constraints depend on encryption level:
  - Unprotected: no classified info
  - Partially protected: confidential allowed
  - Protected: secret allowed

---

## 3. Turn-Taking Conventions

### Explicit Turn Allocation
- "antworten" explicitly assigns speaking turn
- Only addressed station responds

### Sequential Response Order
- In multi-party communication:
  - Stations respond in ordered sequence
  - Each must confirm before next speaks

### Conversation Closure
- "Schluss" signals:
  - End of transmission
  - Channel becomes free

---

## 4. Acknowledgement Patterns

### Standard Acknowledgements
- "Verstanden" → full receipt confirmed
- "Richtig" → confirmation that acknowledgement was correct

### Error Handling
- "Nicht verstanden" → message not received properly
- "Wiederholen" → request repetition
- "Falsch" → indicates incorrect part
- "Falsch ich wiederhole" → correction in progress

### Mandatory Acknowledgement Cases
- Commands (Befehl)
- Channel changes
- Directed responses ("antworten")

---

## 5. Communication Economy (Brevity & Compression)

### Core Principles
- Messages must be:
  - Short
  - Clear
  - Pre-structured before transmission

### Language Constraints
- Prefer written language ("Schriftsprache") for messages
- Conversations may use dialect but must remain concise

### Compression Techniques
- Avoid abbreviations unless necessary
- Use standardized phrases instead of free-form speech
- Use "STOP" to structure content segments if needed

---

## 6. Repetition and Redundancy Rules

- Repetition only used:
  - When requested
  - When clarity is insufficient
- Optional full repetition for one-sided transmissions
- Partial repetition allowed

---

## 7. Signal Quality Reporting

### Standard Scale
- ONE → poor / unusable
- TWO → limited / requires repetition
- THREE → clear

### When Required
- Initial contact
- After:
  - Location change
  - Channel change
  - Antenna change

---

## 8. Advanced Routing Mechanisms

### Transit Communication
- Used when direct communication fails
- Two types:
  - Predefined transit station
  - Spontaneous relay station

### Relay Operation
- Dedicated relay-configured stations may forward messages

---

## 9. Status Messaging System

### Numeric Status Codes (Example)
- 1 → Active deployment
- 2 → Reserve
- 3 → Busy
- 4 → Available
- 5 → Break
- 6 → Recovery/reset
- 7 → Movement
- 8 → Training
- 9 → Logged off

### Characteristics
- Highly compressed communication
- Encodes operational state without full sentence

---

## 10. Deviations and Practical Flexibility

### Allowed Variations
- Dialect usage in conversations
- Flexible adaptation under stress or special conditions

### Observed Constraints
- Rules describe idealized behavior
- Real-world usage may:
  - Skip formal structure
  - Reduce verbosity further
  - Omit non-critical elements

---

## 11. Key Constraints for Dataset Generation

- Every message should ideally:
  - Include sender, receiver, and message type
- Turn-taking must be explicit via protocol markers
- Acknowledgements are structured and predictable
- Communication is compressed and formulaic
- Multi-party communication requires ordered responses
- Deviations must be modeled as controlled variations