# IDE Codex Prompt: Greek Retroversion Publication Polish v0.1

## Objective

Polish the Greek layer for publication by checking consistency of extant Greek labels, hypothetical retroversion labels, confidence levels, and reader-facing explanations.

## Why This Matters

The project allows Greek retroversion where Greek circulation is historically likely, but retroversion must never be confused with manuscript evidence. This pass protects the scholarly credibility of the Greek layer.

## Prerequisites

Preferably execute after:

- wealth/renunciation cluster-control;
- ritual-ethics / bridegroom 104A follow-up;
- bibliography/source reproducibility pass.

## Required Inputs

Read:

- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-greek.md`
- `reconstruction/earliest-sayings-gospel/parallel-edition.md`
- `reconstruction/earliest-sayings-gospel/greek-retroversion-confidence-audit-v0.1.md`
- `reconstruction/earliest-sayings-gospel/evidence-dossier-en.md`
- `reconstruction/earliest-sayings-gospel/all-114-publication-decision-table-v0.1.md`
- `sources/primary_texts/greek_poxy/`
- `sources/primary_texts/source-register.md`
- all current reader cards.

## Required Checks

For every clean-reader unit:

- verify Greek status label;
- verify whether extant P.Oxy. witness exists;
- verify confidence label if hypothetical;
- ensure Greek retroversion is not called a witness;
- ensure Coptic/Synoptic basis is stated;
- ensure parallel edition and Greek file agree.

## Required Outputs

Create:

- `reconstruction/earliest-sayings-gospel/greek-retroversion-publication-polish-v0.1.md`

Update:

- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-greek.md`
- `reconstruction/earliest-sayings-gospel/parallel-edition.md`
- `reconstruction/earliest-sayings-gospel/greek-retroversion-confidence-audit-v0.1.md`
- `reconstruction/earliest-sayings-gospel/evidence-dossier-en.md`
- `project/open-task-prompt-queue-2026-07-18.md`

## Non-Goals

- Do not invent extant Greek.
- Do not replace publication verification against critical editions with confidence assertions.
- Do not change clean-reader membership.

## Validation

Run:

```bash
python3 tools/qa_crosscheck.py
git diff --check
```

## Final Report

Report:

- Greek label inconsistencies fixed;
- remaining cases needing human/critical-edition verification;
- whether parallel edition and Greek layer are synchronized.
