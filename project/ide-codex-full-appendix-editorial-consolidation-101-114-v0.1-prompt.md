# IDE Codex Prompt: Full Appendix Editorial Consolidation, Logia 101-114 v0.1

## Objective

Finish print-safe publication-level editorial consolidation of the Ukrainian full 114-logion appendix by editing Logia 101-114 in:

- `reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-uk.md`

This is the final appendix editorial package after completed consolidation for Logia 1-100.

## Why This Matters

Logia 101-114 are the last unconsolidated appendix range. This range includes one clean-reader unit or core already stabilized in earlier passes, several high-early appendix-only candidates, living/dead/world and body/soul material, a major wealth/world-renunciation saying, and the high-impact Logion 114 exclusion. Finishing this range will make the entire 114-logion appendix book-readable.

## Required Inputs

Read:

- `project/print-and-digital-publication-architecture.md`
- `project/final-product-specification.md`
- `project/project-completion-roadmap.md`
- `reconstruction/earliest-sayings-gospel/full-appendix-editorial-consolidation-091-100-v0.1.md`
- `reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-uk.md`
- `corpus/cards/logion-101.md` through `corpus/cards/logion-114.md`
- relevant evidence notes under `reconstruction/earliest-sayings-gospel/notes/`
- relevant control files under `controls/synoptic-parallels/`
- `corpus/tables/logia-workflow-matrix.md`
- `reconstruction/earliest-sayings-gospel/all-114-publication-decision-table-v0.1.md`

## Scope

Edit only Logia 101-114 appendix sections unless a directly required source/control note reference must be corrected.

Target logia:

- 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114.

## Required Editorial Treatment

For each target section:

1. Preserve the heading `## Логія NN`.
2. Preserve `### Статус у реконструкції`.
3. Preserve or add `Чистий текст реконструкції:` only if the logion or subunit is in the clean reader.
4. Consolidate duplicated older commentary and card-derived interpretation into one coherent reader-facing explanation.
5. Keep print-safe references in prose: Logion number, NHC II,2, P.Oxy. label where applicable, canonical references, witness/control labels.
6. Keep repository paths only in `### Джерела й контрольні файли`.
7. Explain why the logion is included, partly included, appendix-only, deferred, or excluded.
8. Keep uncertainty explicit without turning the appendix into a technical table.

## Special Cautions

- Logion 101 belongs to family-renunciation control; do not promote without a separate decision.
- Logion 103A is in the clean reader as a marked watchfulness/thief core; preserve the distinction between 103A and the full logion.
- Logion 104 / 104A remains deferred to ritual-ethics / bridegroom follow-up; do not promote in this editorial pass.
- Logion 107 is in the clean reader; preserve the lost-sheep core and its Synoptic controls.
- Logion 109 remains appendix-only despite high early pressure; treat as treasure/field parable material requiring parable-cluster control.
- Logion 110 belongs to wealth/world-renunciation control; do not promote.
- Logia 111-113 belong to living/dead/world and kingdom-presence controls; preserve appendix-only decisions.
- Logion 114 must have an explicit reader-facing exclusion rationale: explain why the Mary/Peter/gender-transformation ending is secondary or at least not part of the reconstructed earliest sayings gospel.

## Non-Goals

- Do not change clean-reader membership.
- Do not add new reconstructed Greek unless already required by an existing evidence note.
- Do not rewrite Logia outside 101-114.
- Do not remove source/control sections.

## Expected Output

Create:

- `reconstruction/earliest-sayings-gospel/full-appendix-editorial-consolidation-101-114-v0.1.md`

Update as needed:

- `reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-uk.md`
- `project/project-completion-roadmap.md`
- `project/project-map.md`
- `README.md`
- `project/open-task-prompt-queue-2026-07-18.md`

## Validation

Run before and after:

```bash
python3 tools/qa_crosscheck.py
```

Run after:

```bash
git diff --check
```

## Final Report

Report:

- which Logia 101-114 sections were consolidated;
- whether clean reader changed;
- QA output;
- whether remaining card-derived and working-index appendix debt is now 0;
- recommended next project step after full appendix completion.
