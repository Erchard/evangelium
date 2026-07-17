# IDE Codex Prompt: High-Candidate Deepening Sprint B

## Mission

Execute the next high-candidate deepening pass for Logia 86, 89, 90, 93, 94, 95, and 96.

The goal is not to expand the clean reader immediately. The goal is to remove major evidence gaps before the final decision audit, so that no strong `UNCERTAIN` logion is left untested.

## Project Goal

The project aims to reconstruct the earliest recoverable sayings-gospel layer behind or preserved in the Gospel of Thomas.

The final product must contain:

- a clean Ukrainian reader text first, with only numbered reconstructed logia and no comments, brackets, statuses, or disclaimers;
- a full commentary appendix for all 114 logia, including excluded and deferred logia;
- Coptic source layer;
- extant Greek witness layer where preserved;
- clearly labeled `Greek retroversion, hypothetical` where Greek is reconstructed but not extant;
- English reader layer;
- an English evidence dossier suitable for outside review.

## Required Inputs

Read before editing:

- `project/final-product-specification.md`
- `project/clean-reader-text-first-page-principle.md`
- `project/project-completion-roadmap.md`
- `project/publication-gap-audit-v0.1.md`
- `project/logion-card-gold-standard.md`
- `corpus/cards/logion-086.md`
- `corpus/cards/logion-089.md`
- `corpus/cards/logion-090.md`
- `corpus/cards/logion-093.md`
- `corpus/cards/logion-094.md`
- `corpus/cards/logion-095.md`
- `corpus/cards/logion-096.md`
- `corpus/tables/logia-workflow-matrix.md`
- `reconstruction/earliest-sayings-gospel/inclusion-decisions-table.md`

## Work Package

For each logion in the Sprint B set, create an English evidence note:

- `reconstruction/earliest-sayings-gospel/notes/logion-086-evidence-en.md`
- `reconstruction/earliest-sayings-gospel/notes/logion-089-evidence-en.md`
- `reconstruction/earliest-sayings-gospel/notes/logion-090-evidence-en.md`
- `reconstruction/earliest-sayings-gospel/notes/logion-093-evidence-en.md`
- `reconstruction/earliest-sayings-gospel/notes/logion-094-evidence-en.md`
- `reconstruction/earliest-sayings-gospel/notes/logion-095-evidence-en.md`
- `reconstruction/earliest-sayings-gospel/notes/logion-096-evidence-en.md`

For each logion, create a synoptic/control file:

- `controls/synoptic-parallels/logion-086-foxes-birds-son-of-man-controls.md`
- `controls/synoptic-parallels/logion-089-cup-inside-outside-controls.md`
- `controls/synoptic-parallels/logion-090-yoke-rest-controls.md`
- `controls/synoptic-parallels/logion-093-holy-dogs-pearls-swine-controls.md`
- `controls/synoptic-parallels/logion-094-seek-knock-controls.md`
- `controls/synoptic-parallels/logion-095-money-lending-controls.md`
- `controls/synoptic-parallels/logion-096-leaven-controls.md`

## Required Analysis for Each Evidence Note

Each note must include:

- current decision;
- confidence;
- Coptic witness;
- Greek witness status;
- synoptic or Jewish controls;
- main evidence;
- early-core assessment;
- secondary-layer indicators;
- limits;
- probability assessment;
- reconstruction implication;
- next work.

## Decision Discipline

Do not add any Sprint B logion to the clean Ukrainian reader in this pass.

Allowed outcomes:

- `UNCERTAIN`
- `UNCERTAIN`; possible marked-core candidate
- `UNCERTAIN`; split-core candidate
- `DEFER`
- `EXCLUDE_AS_SECONDARY`

Use `INCLUDE_WITH_MARKER` only if the evidence clearly requires it, and only after checking that the clean reader remains coherent and the evidence dossier can support the decision. For this sprint, the expected outcome is evidence/control deepening, not reader expansion.

## Greek Policy

If no extant Greek Thomas witness is loaded, do not describe any Greek text as extant.

Use:

- `No loaded Greek Oxyrhynchus Thomas witness preserves this logion.`
- `Any Greek form must be labeled Greek retroversion, hypothetical.`

If a Greek retroversion is likely, discuss only confidence and controls. Do not invent a manuscript witness.

## Files to Update

After creating notes and control files, update:

- `corpus/tables/logia-workflow-matrix.md`
- `reconstruction/earliest-sayings-gospel/inclusion-decisions-table.md`
- `corpus/cards/card-quality-audit-v0.1.md`
- `project/publication-gap-audit-v0.1.md`
- `project/project-completion-roadmap.md`
- `sources/primary_texts/collection-log.md`

## Quality Bar

- Keep the clean reader untouched unless a separate final decision pass is explicitly performed.
- Mark all uncertainty plainly.
- Separate compact early cores from later Thomasine, Matthean, Lukan, or editorial frames.
- Make the result useful for the later full 114-logion appendix.
- Prefer cautious scholarly language over impressive but unsupported certainty.

## Expected Outcome

At the end of this task:

- Sprint B no longer appears as an unprocessed evidence gap.
- Each Sprint B logion has an evidence note and control file.
- The workflow matrix and inclusion table agree.
- The roadmap points to Sprint C: Logia 99, 100, 103, 107, 109, and 113.
- The clean Ukrainian reader still contains only previously justified logia.
