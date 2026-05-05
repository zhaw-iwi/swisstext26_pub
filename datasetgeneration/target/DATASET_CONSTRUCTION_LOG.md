# DATASET_CONSTRUCTION_LOG

Guidance used:
- `./.agents/datasetgeneration/dataset_generation.md`
- `./.agents/datasetgeneration/source_notes_sprechregeln.md`
- `./.agents/datasetgeneration/source_notes_real_transcript.md`
- `./.agents/datasetgeneration/source_notes_einsatzfuehrung.md`

Dataset size:
- 5 scenario JSON files

Intentional realism variation:
- mixed protocol completeness, including both strict `An ... von ...` structure and compressed field shorthand
- delayed or reduced acknowledgements
- interleaved updates from multiple units
- partial progress reports that do not yet justify task completion
- assigned but incomplete tasks with explicit best-available state evidence
- variation in task families across building fire, garage fire, school cellar fire, workshop fire, and roof-space fire

Important design decisions:
- kept a fixed closed-world task inventory per scenario with one gold label per predefined task
- required explicit assignment evidence for every monitored task
- used only message-grounded completion evidence copied from the scenario messages
- kept all scenarios operationally coherent with safety, containment, control, and final-check progression
- used stable filenames `s1.json` to `s5.json` inside a dedicated dataset folder under `data/scenarios`
