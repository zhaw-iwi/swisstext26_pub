# Dataset Revision Log

Dataset: `data/scenarios/synthetic_firefighter_radio_controlled_v1`

Revision goal:
- Improve alignment with `dataset_validation_structure.md` and `dataset_validation_content.md`
- Preserve the fixed JSON schema, closed-world task setup, scenario diversity, and internal consistency

## Changed Files

- `s1.json`
- `s3.json`
- `s4.json`

## Fixes Applied

### `s1.json`

- Fix type: Local revision
- Issues fixed:
  - Removed a dangling `antworten` from message `4` by converting the report into a closed one-way status message.
  - Strengthened safety/sequence evidence for the early search release by adding `Zugang bis Wohnungstuer frei` to message `4`.
  - Added the missing closure marker `Schluss` to message `10`.
  - Standardized message `11` to the dominant addressing pattern `An [Empfaenger] von [Absender]`.
- Validation impact:
  - Improves protocol consistency and addressing regularity.
  - Reduces the content-level concern that interior search was released with too little explicit access/safety evidence.

### `s3.json`

- Fix type: Local revision
- Issues fixed:
  - Renamed predefined task `T3` from `Brandraum Keller West erkunden und abloeschen` to `Brandraum Keller West erkunden, abloeschen und Installationsschacht kontrollieren`.
- Validation impact:
  - Aligns the closed-world tracked task wording with the actual monitored work and completion evidence in messages `11`, `12`, and `15`.
  - Reduces the mismatch previously noted between task wording and the broader completion report.

### `s4.json`

- Fix type: Local revision
- Issues fixed:
  - Removed the dangling `antworten` from message `2`, where no direct response followed.
  - Expanded message `9` so the acknowledgement preserves the safety-relevant order element `Gasflaschenlage im Blick`.
  - Replaced the structurally mismatched confirmation in message `18` with a clear command-layer acknowledgement using the dominant sender/receiver framing.
- Validation impact:
  - Resolves the main structural weakness that caused scenario `S4` to score `PARTIAL` in the structure report.
  - Improves acknowledgement quality without simplifying the operational hazard picture.

## Regeneration Summary

- Full-scenario regenerations: none
- All fixes were local edits because the reports identified isolated structural and wording problems rather than irreparable scenario design failures.

## Remaining Limitations

- The dataset still keeps some controlled protocol variability, including broadcast openings without explicit ordered acknowledgements. This is intentional and consistent with the real-transcript source notes.
- Several scenarios still end at stabilization rather than full demobilization or readiness restoration. This remains compatible with the closed-world task design, but closure coverage is uneven across the dataset.
- The dataset remains cleaner than highly chaotic real incidents. The revision preserved that balance rather than adding new complexity not requested by the reports.

## Readiness Note

- After this revision, the dataset is a reasonable candidate for another validation round.
- The main previously failing structural case (`S4`) was repaired locally, and the key content-level wording mismatch (`S3-T3`) and sequencing evidence weakness (`S1`) were tightened without altering schema or task inventory design.
