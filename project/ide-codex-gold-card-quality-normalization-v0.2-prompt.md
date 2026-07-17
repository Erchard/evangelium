# Codex Prompt: Gold-Level Card Quality Normalization v0.2

## Mission

Bring all 114 logion cards to the same operational quality level as the best current card, without pretending that every card has the same depth of academic research.

The formal gold card is `corpus/cards/logion-002.md`. For composite or layered sayings, use `corpus/cards/logion-006.md` as the practical model.

## Core Principle

Every logion card must now help answer two questions:

1. Can this saying, or a recoverable subunit of it, responsibly belong to the clean reconstruction of the earliest sayings gospel?
2. If it does not belong, how will the reader understand the saying, its sources, its interpretive possibilities, and the reason for exclusion?

Rejected, deferred, uncertain, and appendix-only logia are not discarded material. They belong in the full 114-logion appendix and must receive serious explanatory treatment.

## Required Actions

1. Read the current project documentation and verify the active state:
   - `README.md`
   - `project/project-map.md`
   - `project/logion-card-gold-standard.md`
   - `corpus/tables/logia-workflow-matrix.md`
   - `reconstruction/earliest-sayings-gospel/README.md`
2. Confirm the best current card:
   - `corpus/cards/logion-002.md` as the formal gold standard;
   - `corpus/cards/logion-006.md` as the model for split-core and composite logia.
3. Add or refresh a `## Gold-level status check v0.2` block in every `corpus/cards/logion-XXX.md` file.
4. The v0.2 block must include:
   - current decision from the workflow matrix;
   - reader-text status;
   - Greek witness status;
   - current work status;
   - evidence note status;
   - links to evidence notes where present;
   - links to synoptic/control files where present;
   - Greek/Coptic policy;
   - clean-reader implication;
   - full-appendix obligation;
   - remaining next action.
5. Make the v0.2 block explicitly supersede older local status labels where they conflict.
6. Do not turn hypothetical Greek retroversions into manuscript witnesses.
7. Do not promote new logia into the clean reader during this pass.
8. Update project documentation so later work treats the v0.2 block as the current card-quality control layer.

## Deliverables

- All 114 logion cards contain `## Gold-level status check v0.2`.
- `project/logion-card-gold-standard.md` updated to v0.2.
- `corpus/cards/card-quality-audit-v0.2.md` created.
- Navigation/status documents updated.
- Verification confirms 114/114 cards have the v0.2 block and no markdown/file integrity errors are introduced.

## Success Criteria

The project should end this pass with no hidden contradiction about the current state of a card. A reader or future editor should be able to open any logion card and immediately see:

- whether it is in the clean reconstruction;
- whether the full saying or only a core is under consideration;
- what Greek evidence exists or does not exist;
- what evidence/control files support the decision;
- what still must be done before publication.
