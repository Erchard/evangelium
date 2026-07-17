# IDE Codex Prompt: Split-Core Decision Review B

## Task

Close the weakest remaining methodological gap before any further clean-reader expansion: complete Split-Core Decision Review B for Logia 76, 78, 79, 94, 103, 109, and 113.

## Goal

The project reconstructs the earliest reachable sayings gospel, not the full Gospel of Thomas. Therefore, do not promote a whole Thomas logion when only a smaller earlier-looking core is defensible. The purpose of this pass is to decide which subunits are strong enough to be considered in a later controlled clean-reader candidate pass, and which must remain appendix-only.

## Sources to Read First

- `reconstruction/earliest-sayings-gospel/final-all-114-decision-audit-v0.1.md`
- `reconstruction/earliest-sayings-gospel/split-core-decision-review-a-v0.1.md`
- `reconstruction/earliest-sayings-gospel/inclusion-decisions-table.md`
- `corpus/tables/logia-workflow-matrix.md`
- `corpus/cards/logion-076.md`
- `corpus/cards/logion-078.md`
- `corpus/cards/logion-079.md`
- `corpus/cards/logion-094.md`
- `corpus/cards/logion-103.md`
- `corpus/cards/logion-109.md`
- `corpus/cards/logion-113.md`
- matching evidence notes in `reconstruction/earliest-sayings-gospel/notes/`
- matching control files in `controls/synoptic-parallels/`

## Required Decisions

For each target, decide at subunit level:

- `PROMOTE_CANDIDATE_FOR_READER_PASS`
- `KEEP_APPENDIX_ONLY_FOR_NOW`
- `CLUSTER_DEFER`
- `EXCLUDE_AS_SECONDARY`

Do not edit `reconstruction/earliest-sayings-gospel/reconstructed-gospel-uk.md` in this pass.

## Required Output

Create:

- `reconstruction/earliest-sayings-gospel/split-core-decision-review-b-v0.1.md`

Update:

- `reconstruction/earliest-sayings-gospel/inclusion-decisions-table.md`
- `corpus/tables/logia-workflow-matrix.md`
- `reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-uk.md`
- the seven target cards so their evidence apparatus no longer says evidence/control files are absent
- `README.md`
- `project/project-completion-roadmap.md`
- `project/publication-gap-audit-v0.1.md`
- `project/project-map.md`
- `project/repository-structure.md`
- `project/final-product-specification.md`
- `reconstruction/earliest-sayings-gospel/README.md`
- `sources/primary_texts/collection-log.md`

## Editorial Rules

- Keep the clean reader untouched.
- Greek forms without extant Thomas Greek witnesses must remain labeled `Greek retroversion, hypothetical`.
- Prefer caution: a plausible saying should remain appendix-only if its dependence, duplication, or secondary expansion risk is high.
- After this pass, the next project step should become a controlled clean-reader candidate pass for promoted cores from Reviews A and B.
