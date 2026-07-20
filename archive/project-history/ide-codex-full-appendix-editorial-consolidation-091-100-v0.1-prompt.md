# IDE Codex Prompt: Full Appendix Editorial Consolidation, Logia 91-100 v0.1

## Objective

Continue print-safe publication-level editorial consolidation of the Ukrainian full 114-logion appendix by editing Logia 91-100 in:

- `reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-uk.md`

This is the next publication-quality editorial package after completed consolidation for Logia 1-90.

## Why This Matters

Logia 91-100 include several units visible to the final reader: 91A, 95, 96, 99, and 100. The same range also includes important appendix-only or uncertain sayings: seek/find parallels, guarded sayings, parables, and family/authority material. The appendix must explain both included and excluded material in ordinary reader-facing prose that works on paper without clickable links.

## Required Inputs

Read:

- `project/print-and-digital-publication-architecture.md`
- `project/final-product-specification.md`
- `project/project-completion-roadmap.md`
- `reconstruction/earliest-sayings-gospel/full-appendix-editorial-consolidation-081-090-v0.1.md`
- `reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-uk.md`
- `corpus/cards/logion-091.md` through `corpus/cards/logion-100.md`
- relevant evidence notes under `reconstruction/earliest-sayings-gospel/notes/`
- relevant control files under `controls/synoptic-parallels/`
- `corpus/tables/logia-workflow-matrix.md`
- `reconstruction/earliest-sayings-gospel/all-114-publication-decision-table-v0.1.md`

## Scope

Edit only Logia 91-100 appendix sections unless a directly required source/control note reference must be corrected.

Target logia:

- 91, 92, 93, 94, 95, 96, 97, 98, 99, 100.

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

- Logion 91A is in the clean reader as a marked core; preserve only the time-discernment core and explain why the full sign-seeking frame remains controlled.
- Logia 92 and 94 belong to the seek/find cluster; Logion 2 remains the clean-reader representative, so do not promote 92 or 94.
- Logion 95 is in the clean reader; preserve the lend-without-interest / no-return expectation core.
- Logion 96 is in the clean reader; preserve the leaven/meal kingdom parable core and its Matthew/Luke controls.
- Logia 97 and 98 are appendix-only parabolic material; do not promote them without a separate parable-control decision.
- Logion 99 is in the clean reader with marker; preserve the true-family core and its family-renunciation cluster decision.
- Logion 100 is in the clean reader with marker; preserve the Caesar/God core and its Mark/Matthew/Luke control.

## Non-Goals

- Do not change clean-reader membership.
- Do not add new reconstructed Greek unless already required by an existing evidence note.
- Do not rewrite Logia outside 91-100.
- Do not remove source/control sections.

## Expected Output

Create:

- `reconstruction/earliest-sayings-gospel/full-appendix-editorial-consolidation-091-100-v0.1.md`

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

- which Logia 91-100 sections were consolidated;
- whether clean reader changed;
- QA output;
- remaining appendix range to consolidate.
