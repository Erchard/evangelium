# IDE Codex Prompt: Full Appendix Editorial Consolidation, Logia 81-90 v0.1

## Objective

Continue print-safe publication-level editorial consolidation of the Ukrainian full 114-logion appendix by editing Logia 81-90 in:

- `reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-uk.md`

This is the next publication-quality editorial package after completed consolidation for Logia 1-80.

## Why This Matters

Logia 81-90 include several high-impact interpretive fields: wealth and power, fire/kingdom, image/preexistence, body-soul, revelation/transmission, cup inside/outside, and rest/yoke material. The appendix must explain them clearly for paper readers without depending on clickable repository paths.

## Required Inputs

Read:

- `project/print-and-digital-publication-architecture.md`
- `project/final-product-specification.md`
- `project/project-completion-roadmap.md`
- `reconstruction/earliest-sayings-gospel/full-appendix-editorial-consolidation-071-080-v0.1.md`
- `reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-uk.md`
- `corpus/cards/logion-081.md` through `corpus/cards/logion-090.md`
- relevant evidence notes under `reconstruction/earliest-sayings-gospel/notes/`
- relevant control files under `controls/synoptic-parallels/`
- `corpus/tables/logia-workflow-matrix.md`
- `reconstruction/earliest-sayings-gospel/all-114-publication-decision-table-v0.1.md`

## Scope

Edit only Logia 81-90 appendix sections unless a directly required source/control note reference must be corrected.

Target logia:

- 81, 82, 83, 84, 85, 86, 87, 88, 89, 90.

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

- Logion 86 is in the clean reader; preserve the foxes/birds/Son of Man homelessness core and its Matthew/Luke control.
- Logion 89 is in the clean reader; preserve the cup inside/outside core and its Luke/Matthew control.
- Logion 81 belongs to wealth/renunciation control with Logia 63 and 110; do not promote.
- Logia 83-85 have a new image/preexistence/Adam/deathlessness control package; use it, but do not promote.
- Logia 87 and 112 have body-soul control; use it, but do not promote Logion 87.
- Logion 88 has revelation/transmission control; keep appendix-only.
- Logion 90 has high early pressure but remains appendix-only because Matthew 11:28-30 dependence risk is high.

## Non-Goals

- Do not change clean-reader membership.
- Do not add new reconstructed Greek unless already required by an existing evidence note.
- Do not rewrite Logia outside 81-90.
- Do not remove source/control sections.

## Expected Output

Create:

- `reconstruction/earliest-sayings-gospel/full-appendix-editorial-consolidation-081-090-v0.1.md`

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

- which Logia 81-90 sections were consolidated;
- whether clean reader changed;
- QA output;
- remaining appendix range to consolidate.
