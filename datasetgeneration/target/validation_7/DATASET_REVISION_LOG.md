# DATASET_REVISION_LOG

Dataset folder: `data/scenarios/synthetic_firefighter_radio_controlled_v1`

## Changed Files

- `s1.json`
- `s2.json`
- `s3.json`
- `s5.json`
- `DATASET_REVISION_LOG.md`

## File-Level Revision Details

### `s1.json`

- Fix type: local revision
- Issues fixed:
  - softened the initial smoke description so later reconnaissance no longer reads like an unexplained downgrade
  - reduced generator-shaped repetition in the second Angriffstrupp status update
  - rewrote the final Einsatzleitung message into a true status/constraint message instead of a directive-like `Meldung`
- Result:
  - better internal consistency between early alarm information and later observation
  - cleaner distinction between report traffic and commands

### `s2.json`

- Fix type: local revision
- Issues fixed:
  - rewrote the final Einsatzleitung message to remove directive behavior from a message labeled as `Meldung`
- Result:
  - improved protocol-label consistency without changing task logic or gold labels

### `s3.json`

- Fix type: local revision
- Issues fixed:
- added the missing acknowledgement after the directed command about the Installationsschacht check
  - added an interleaved Wassertrupp update so the scenario no longer collapses into a single narrow command thread
  - replaced the previous split completion evidence for `T3` with one final Angriffstrupp report that explicitly covers extinguishment, no spread, and control
  - added a short command-level follow-up message so the ending is less abruptly clipped
- Result:
  - stronger structural realism
  - strict traceability for `T3` completion evidence
  - improved fit to both structure and content validation criteria

### `s5.json`

- Fix type: local revision
- Issues fixed:
  - made the early Angriffstrupp report structurally more explicit by restoring receiver/sender framing
  - inserted a prerequisite setup thread for a rear-side securing line before roof opening begins
  - updated the roof-opening command so the enabling measure is visible in the radio picture
  - expanded the closing sequence so handover is explicitly justified by the negative final control result
- Result:
  - better dependency realism for roof-space work
  - stronger structural traceability after metadata stripping
  - less compressed end-phase logic

## Full-Scenario Regeneration Assessment

- No full-scenario regeneration was performed.
- The validation reports pointed to localized protocol, sequencing, and traceability problems rather than irreparable scenario design failures.
- Good task inventories, scenario identities, and most message chains were preserved.

## Remaining Limitations

- The dataset still remains relatively clean and annotation-friendly compared with messier real radio traffic; this is deliberate but should be rechecked against the structure framework.
- Broadcast handling (`An Alle`) is still simplified rather than fully modeled with ordered acknowledgements.
- Some scenarios still use fairly disciplined command/acknowledgement patterns, so the next validation round should confirm that realism remains controlled rather than overly templatic.

## Revision Summary

- Structural issues addressed:
  - directive/report label drift reduced
  - one missing acknowledgement repaired
  - one structurally weak free-form report tightened
  - interleaving improved where a scenario had become too linear
- Content issues addressed:
  - multi-part task completion in `S3/T3` is now supported by a single explicit completion message
  - prerequisite setup for `S5` roof work is now visible before opening actions
  - end-phase justification was strengthened where closure had been too abrupt
