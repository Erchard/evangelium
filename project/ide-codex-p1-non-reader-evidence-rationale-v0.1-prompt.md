# IDE Codex Prompt: P1 Non-Reader Evidence Rationale Pass v0.1

You are working in the EUAGELIA project. Execute the next Phase 5 quality step after the first P1 non-reader appendix expansion.

## Purpose

Convert the reader-facing appendix expansion for the first P1 non-reader package into citable evidence/no-note rationale files. The goal is to reduce real evidence-control gaps without changing the clean reader.

## Required Context

Read first:

1. `project/ide-codex-quality-remediation-master-prompt.md`
2. `reconstruction/earliest-sayings-gospel/full-appendix-p1-non-reader-package-v0.1.md`
3. `reconstruction/earliest-sayings-gospel/all-114-publication-decision-table-v0.1.md`
4. `reconstruction/earliest-sayings-gospel/evidence-control-inventory-v0.1.md`
5. `corpus/tables/logia-workflow-matrix.md`
6. `reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-uk.md`
7. Target cards for Logia 23, 24, 28, 29, 30, 37, 38, 75, 77, 104, 106.

## Target Logia

Create evidence/no-note rationale files for:

- 23, 24, 28, 29, 30, 37, 38, 75, 77, 104, 106.

## Required Output

Create these files:

- `reconstruction/earliest-sayings-gospel/notes/logion-023-evidence-en.md`
- `reconstruction/earliest-sayings-gospel/notes/logion-024-evidence-en.md`
- `reconstruction/earliest-sayings-gospel/notes/logion-028-evidence-en.md`
- `reconstruction/earliest-sayings-gospel/notes/logion-029-evidence-en.md`
- `reconstruction/earliest-sayings-gospel/notes/logion-030-evidence-en.md`
- `reconstruction/earliest-sayings-gospel/notes/logion-037-evidence-en.md`
- `reconstruction/earliest-sayings-gospel/notes/logion-038-evidence-en.md`
- `reconstruction/earliest-sayings-gospel/notes/logion-075-evidence-en.md`
- `reconstruction/earliest-sayings-gospel/notes/logion-077-evidence-en.md`
- `reconstruction/earliest-sayings-gospel/notes/logion-104-evidence-en.md`
- `reconstruction/earliest-sayings-gospel/notes/logion-106-evidence-en.md`

Also create:

- `reconstruction/earliest-sayings-gospel/p1-non-reader-evidence-rationale-pass-v0.1.md`

## Required Structure For Each Evidence File

Each note must include:

1. Status.
2. Decision.
3. Working unit.
4. Textual witnesses:
   - Coptic base;
   - P.Oxy. 1 / 654 / 655 status;
   - canonical controls where relevant;
   - cluster notes where relevant.
5. Main evidence.
6. Reason for non-inclusion.
7. Reconstruction implication.
8. Remaining work.

## Quality Rules

- Do not change the clean reader.
- Do not promote any target logion.
- Do not invent Greek manuscript text.
- Distinguish extant Greek, partial Greek, tiny overlap, fragmentary restored Greek, possible/uncertain P.Oxy. association, and hypothetical retroversion.
- Treat canonical Greek as control only, never as a Thomas witness.
- For Logion 24, explicitly separate the Coptic light saying from the P.Oxy. 655 Thomas 24(?) / Logion 37 appearance-undressing material.
- For Logia 30 and 77, explicitly separate P.Oxy. 1 Thomas 30 material from 77b stone/wood material.
- For Logia 23, 75, and 106, explain unity/monachos language as a Thomasine warning marker unless independently controlled.
- For Logion 104, separate possible bridegroom-fasting core from Thomas ritual/bridal-chamber framing.

## Synchronization Work

After creating evidence files:

- update `corpus/tables/logia-workflow-matrix.md` for the target logia from evidence `NO` to `YES` where applicable;
- update target cards so their Evidence Links point to the new files;
- update `reconstruction/earliest-sayings-gospel/evidence-control-inventory-v0.1.md`;
- update `reconstruction/earliest-sayings-gospel/all-114-publication-decision-table-v0.1.md` counts and rows for the target logia;
- update project status docs only if next-step wording becomes stale;
- update `sources/primary_texts/collection-log.md`.

## Final Report

Report:

- files created;
- target logia whose evidence gap is now closed at note level;
- target logia that still need deeper academic bibliography or external verification;
- whether the clean reader changed;
- recommended next package.

Commit and push the changes unless explicitly instructed not to.
