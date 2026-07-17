# IDE Codex Prompt: Greek Retroversion Confidence Audit

## Mission

Audit the Greek layer for the current 31-unit clean reader.

The project now has a synchronized Ukrainian, English, Coptic, Greek, parallel, commentary, and evidence layer. The next methodological risk is that a reader may mistake hypothetical Greek retroversions for extant Greek witnesses. This task creates a clear confidence audit for every Greek-layer unit in the current reader.

## Inputs

Read:

- `06_Reconstructions/earliest-sayings-gospel/reconstructed-gospel-uk.md`
- `06_Reconstructions/earliest-sayings-gospel/reconstructed-gospel-greek.md`
- `06_Reconstructions/earliest-sayings-gospel/parallel-edition.md`
- `06_Reconstructions/earliest-sayings-gospel/inclusion-decisions-table.md`
- evidence notes and control files for included units where needed
- `00_Project/final-product-specification.md`

## Required Output

Create:

- `06_Reconstructions/earliest-sayings-gospel/greek-retroversion-confidence-audit-v0.1.md`

The audit must cover all 31 current reader units:

1, 2, 3, 4, 5, 6, 9, 10, 16, 20, 22, 25, 26, 31, 32, 33, 34, 35, 36, 39, 41, 54, 72, 73, 86, 89, 95, 96, 99, 100, 107.

## Categories

Use these categories:

- `Extant Greek witness`
- `Lacunose extant Greek witness`
- `Partial extant Greek witness`
- `Extant Greek plus hypothetical retroversion`
- `Greek retroversion, hypothetical`

For hypothetical retroversions, assign:

- `high`
- `medium-high`
- `medium`
- `low-medium`
- `low`

## Required Columns

The audit table must include:

- Logion
- Greek layer category
- Confidence
- Main controls
- Main risk
- Publication instruction

## Rules

- Never call a retroversion an extant witness.
- For P.Oxy. material, distinguish preserved text from reconstructed lacunae.
- Where Greek is only partial, state what part is extant and what remains Coptic/synoptic controlled.
- Where no loaded Greek Thomas witness exists, publication instruction must include `Label as Greek retroversion, hypothetical`.
- Do not rewrite the whole Greek text unless needed. The audit is the controlling document.

## Project Updates

After creating the audit:

- update `reconstructed-gospel-greek.md` status/header to point to the audit;
- update `project-completion-roadmap.md`;
- update `publication-gap-audit-v0.1.md`;
- update `collection-log.md`.

## Expected Next Step

After this audit, the logical next step is not another Greek pass. It is either:

- all-114 final decision audit, or
- full appendix expansion for included 31 logia/cores.
