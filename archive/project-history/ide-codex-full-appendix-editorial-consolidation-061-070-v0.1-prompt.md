# IDE Codex Prompt: Full Appendix Editorial Consolidation, Logia 61-70 v0.1

## Objective

Continue print-safe publication-level editorial consolidation of the Ukrainian full 114-logion appendix by editing Logia 61-70 in:

- `reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-uk.md`

This is the next publication-quality editorial package after completed consolidation for Logia 1-60.

## Why This Matters

The project already has complete 114-logion appendix coverage, but Logia 61-114 still contain uneven prose, duplicated card-derived interpretation blocks, and technical phrasing that is acceptable for a working file but weak for a paper reader. This pass improves the most visible remaining reader-facing layer.

## Required Inputs

Read:

- `project/print-and-digital-publication-architecture.md`
- `project/final-product-specification.md`
- `project/project-completion-roadmap.md`
- `reconstruction/earliest-sayings-gospel/full-appendix-editorial-consolidation-051-060-v0.1.md`
- `reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-uk.md`
- `corpus/cards/logion-061.md` through `corpus/cards/logion-070.md`
- relevant evidence notes under `reconstruction/earliest-sayings-gospel/notes/`
- `corpus/tables/logia-workflow-matrix.md`
- `reconstruction/earliest-sayings-gospel/all-114-publication-decision-table-v0.1.md`

## Scope

Edit only Logia 61-70 appendix sections unless a directly required source/control note reference must be corrected.

Target logia:

- 61, 62, 63, 64, 65, 66, 67, 68, 69, 70.

## Required Editorial Treatment

For each target section:

1. Preserve the heading `## Логія NN`.
2. Preserve `### Статус у реконструкції`.
3. Preserve or add `Чистий текст реконструкції:` only if the logion is in the clean reader.
4. Consolidate duplicated older commentary and card-derived interpretation into one coherent reader-facing explanation.
5. Keep print-safe references in prose:
   - Logion number;
   - NHC II,2;
   - P.Oxy. label where applicable;
   - canonical references such as Luke 12:16-21;
   - short witness/control labels.
6. Keep repository paths only in `### Джерела й контрольні файли`.
7. Include why the logion is included, partially included, appendix-only, deferred, or excluded.
8. Keep uncertainty explicit without turning the appendix into a technical table.

## Non-Goals

- Do not change clean-reader membership.
- Do not add new reconstructed Greek unless already required by an existing evidence note.
- Do not rewrite Logia outside 61-70.
- Do not remove source/control sections.

## Expected Output

Create:

- `reconstruction/earliest-sayings-gospel/full-appendix-editorial-consolidation-061-070-v0.1.md`

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

- which Logia 61-70 sections were consolidated;
- whether clean reader changed;
- QA output;
- remaining appendix range to consolidate.
