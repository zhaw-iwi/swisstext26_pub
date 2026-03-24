# DATASET_REVISION_LOG

Revision basis:
- `./.agents/datasetgeneration/dataset_generation.md`
- `./.agents/datasetgeneration/dataset_validation_structure.md`
- `./.agents/datasetgeneration/dataset_validation_content.md`
- `data/scenarios/synthetic_firefighter_radio_controlled_v1/STRUCTURE_VALIDATION_REPORT.md`
- `data/scenarios/synthetic_firefighter_radio_controlled_v1/CONTENT_VALIDATION_REPORT.md`

## Changed Files

- `s1.json`
- `s2.json`
- `s3.json`
- `s4.json`
- `s5.json`

## Applied Revisions

### `s1.json`
- Fix type: local
- Issues fixed:
  - adjusted the opening multi-recipient transmission so it now explicitly requests replies with `antworten`
  - preserved the rest of the scenario because the validation issues were minor and structural only

### `s2.json`
- Fix type: local
- Issues fixed:
  - removed the stacked directed-order pattern at the start by letting `Sicherheitstrupp` acknowledge before the next directed command
  - diversified acknowledgement surface forms to reduce repeated templating
  - kept task assignments and gold labels unchanged because they were already content-valid

### `s3.json`
- Fix type: local
- Issues fixed:
  - removed the early stacked directed-order pattern by making acknowledgements follow the first order before the second directed order
  - reduced repetitive completion phrasing in the late attack-trupp reporting sequence
  - strengthened late-stage coordination texture with a fuller command-side coordination message and closing status aggregation
  - preserved the existing closed-world task inventory and gold-label policy

### `s4.json`
- Fix type: local
- Issues fixed:
  - revised the tactical sequence so the known gas-cylinder hazard is handled first through explicit cooling before the offensive suppression push
  - made the suppression order contingent on established cooling, improving safety and dependency realism
  - reduced repetitive late-stage cooling loop wording and improved command-side coordination phrasing
  - updated message flow while preserving the same schema, scenario identity, task set, and gold task outcomes

### `s5.json`
- Fix type: local
- Issues fixed:
  - diversified acknowledgement phrasing to reduce repeated `verstanden ... Schluss` templating
  - made the directed handover message explicitly request a reply with `antworten`
  - preserved the scenario because validation findings were minor

## Remaining Limitations

- `s3.json` and `s5.json` still contain composite predefined tasks. They are now more traceable in-message, but the task granularity remains broader than an ideal one-step-per-task design.
- The dataset still leans slightly cleaner and more coordinated than fully raw field radio traffic. This is intentional to preserve annotation reliability.
- Some scenarios still end before full demobilization or handover depth. This remains acceptable for partial-incident snapshots but limits end-phase variety.

## Revision Outcome

- No scenario required full regeneration.
- The main content-level failure in `S4` was corrected locally.
- Structural realism was improved across the set through better turn-taking, slightly more varied acknowledgements, and less templated late-stage coordination.
