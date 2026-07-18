# IDE Codex Prompt: Full Appendix Editorial Consolidation, Logia 71-80 v0.1

## Objective

Continue print-safe publication-level editorial consolidation of the Ukrainian full 114-logion appendix by editing Logia 71-80 in:

- `reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-uk.md`

This is the next publication-quality editorial package after completed consolidation for Logia 1-70.

## Why This Matters

The project already has complete 114-logion appendix coverage, but Logia 71-114 still contain uneven prose, duplicated card-derived interpretation blocks, and technical phrasing that is acceptable for a working file but weak for a paper reader. This pass continues turning the appendix into a coherent book layer.

## Required Inputs

Read:

- `project/print-and-digital-publication-architecture.md`
- `project/final-product-specification.md`
- `project/project-completion-roadmap.md`
- `reconstruction/earliest-sayings-gospel/full-appendix-editorial-consolidation-061-070-v0.1.md`
- `reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-uk.md`
- `corpus/cards/logion-071.md` through `corpus/cards/logion-080.md`
- relevant evidence notes under `reconstruction/earliest-sayings-gospel/notes/`
- relevant control files under `controls/synoptic-parallels/`
- `corpus/tables/logia-workflow-matrix.md`
- `reconstruction/earliest-sayings-gospel/all-114-publication-decision-table-v0.1.md`

## Scope

Edit only Logia 71-80 appendix sections unless a directly required source/control note reference must be corrected.

Target logia:

- 71, 72, 73, 74, 75, 76, 77, 78, 79, 80.

## Required Editorial Treatment

For each target section:

1. Preserve the heading `## Логія NN`.
2. Preserve `### Статус у реконструкції`.
3. Preserve or add `Чистий текст реконструкції:` only if the logion or subunit is in the clean reader.
4. Consolidate duplicated older commentary and card-derived interpretation into one coherent reader-facing explanation.
5. Keep print-safe references in prose:
   - Logion number;
   - NHC II,2;
   - P.Oxy. label where applicable;
   - canonical references such as Luke 12:13-14 or Matthew 9:37-38;
   - short witness/control labels.
6. Keep repository paths only in `### Джерела й контрольні файли`.
7. Explain why the logion is included, partly included, appendix-only, deferred, or excluded.
8. Keep uncertainty explicit without turning the appendix into a technical table.

## Special Cautions

- Logion 72 is in the clean reader; preserve the inheritance-dispute refusal core and keep Luke-dependence risk explicit.
- Logion 73 is in the clean reader; preserve the harvest/workers core and its Matthew/Luke controls.
- Logion 75 belongs to the Thomas unity / monachos and bridal-chamber field; do not promote.
- Logion 77 has P.Oxy. 1 overlap only for 77b / boundary material; do not cite P.Oxy. 1 as support for the whole logion.
- Logion 80 belongs to the living/dead/world cluster; keep appendix-only unless a separate controlled pass changes it.

## Non-Goals

- Do not change clean-reader membership.
- Do not add new reconstructed Greek unless already required by an existing evidence note.
- Do not rewrite Logia outside 71-80.
- Do not remove source/control sections.

## Expected Output

Create:

- `reconstruction/earliest-sayings-gospel/full-appendix-editorial-consolidation-071-080-v0.1.md`

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

- which Logia 71-80 sections were consolidated;
- whether clean reader changed;
- QA output;
- remaining appendix range to consolidate.
