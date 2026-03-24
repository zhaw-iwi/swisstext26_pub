# Dataset Revision Log

## Scope

Revision target:
- `data/scenarios/synthetic_firefighter_radio_controlled_v1`

Revision policy applied:
- local fixes where possible
- no full-scenario regeneration was required
- fixed schema and closed-world task setup preserved

## Changed Files

- `s1.json`
- `s4.json`
- `s5.json`

## Fixes Applied

### `s1.json`

Fix type:
- Local revision

Issues fixed:
- Narrowed the opening broadcast from `Alle` to the units that actually acknowledge immediately, reducing the broadcast-acknowledgement mismatch noted in structural validation.
- Expanded the search completion report slightly so the initial unknown-persons situation is resolved more clearly at the apartment-access level without changing task scope.
- Added one controlled protocol irregularity by shortening the ventilation acknowledgement while preserving interpretability.

Remaining limitations:
- The scenario still ends with ventilation ongoing rather than final closure, which is intentional and consistent with the incomplete-task design.

### `s4.json`

Fix type:
- Local revision

Issues fixed:
- Added an explicit enabling readiness step before suppression and gas-cylinder cooling: west-side water supply and a protected cooling position are now established and reported before tactical execution.
- Renamed `T3` from `Gasflaschen kuehlen` to `Gasflaschen kuehlen bis Kaltmeldung herstellen` so the predefined task matches the operational objective shown in the messages.
- Replaced a repetitive reinforcement order with a status update from the traffic unit to improve communication-flow realism while preserving the completed access-control task.

Remaining limitations:
- The gas-cylinder task remains intentionally incomplete at scenario end because one cylinder is still warm.

### `s5.json`

Fix type:
- Local revision

Issues fixed:
- Tightened the dependency between rear-side access and attic operations by making the attack order explicitly conditional on the ladder readiness message.
- Renamed `T2` to match the assignment chain already present in the messages: opening the roof area, searching for hotspots, and extinguishing them.
- Added a small positional clarification in the first attack progress report so the rear-side causal chain remains visible in reduced transcript forms.

Remaining limitations:
- Rear-side readiness is still represented as a conditional assignment followed by confirmation, which keeps realistic compression instead of turning the exchange into an overly clean script.

## Unchanged Files

- `s2.json`
- `s3.json`

Reason:
- Validation findings for these files were minor and did not justify riskier edits. They already passed both validation frameworks without traceability problems.

## Overall Remaining Limitations

- The dataset remains somewhat cleaner than highly noisy real radio traffic; that was preserved deliberately to maintain reliable gold-label traceability.
- Full handover and readiness-restoration logic is still concentrated mainly in `S5`; end-state coverage improved indirectly through dependency handling, but closure diversity remains limited.
- Message-type variety is still constrained; this revision focused on report-driven fixes rather than broad stylistic rewrites.
