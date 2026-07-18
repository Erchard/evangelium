# IDE Codex Prompt: Evidence Dossier Publication Pass v0.1

## Objective

Transform `reconstruction/earliest-sayings-gospel/evidence-dossier-en.md` from a working dossier into a publication-facing English evidence document that can be read by an external reviewer.

## Why This Matters

The clean reader is persuasive only if the evidence trail is transparent. The dossier must explain why this is a reconstruction of an earliest recoverable sayings gospel, not a translation of Thomas and not a maximal collection of attractive sayings.

## Prerequisites

Preferably execute after:

- full appendix consolidation through at least Logia 1-80;
- wealth/renunciation cluster-control;
- Logion 114 exclusion rationale;
- bibliography/rights/citation pass.

If any prerequisite is missing, either mark the relevant subsection as provisional or defer this prompt.

## Required Inputs

Read:

- `project/final-product-specification.md`
- `project/print-and-digital-publication-architecture.md`
- `project/project-completion-roadmap.md`
- `reconstruction/earliest-sayings-gospel/evidence-dossier-en.md`
- `reconstruction/earliest-sayings-gospel/all-114-publication-decision-table-v0.1.md`
- `reconstruction/earliest-sayings-gospel/inclusion-decisions-table.md`
- `reconstruction/earliest-sayings-gospel/greek-retroversion-confidence-audit-v0.1.md`
- all cluster-control notes in `reconstruction/earliest-sayings-gospel/notes/`
- `sources/primary_texts/source-register.md`
- bibliography and rights files if present.

## Required Structure

The dossier should include:

1. methodological introduction;
2. source hierarchy;
3. reconstruction method;
4. clean-reader selection principles;
5. Greek witness and retroversion policy;
6. cluster-control method;
7. included logia/core summaries;
8. major appendix-only high-impact cases;
9. exclusion rationale, including Logion 114;
10. uncertainty model and alternative reconstructions;
11. bibliography and citation/rights note.

## Required Outputs

Update:

- `reconstruction/earliest-sayings-gospel/evidence-dossier-en.md`

Create:

- `reconstruction/earliest-sayings-gospel/evidence-dossier-publication-pass-v0.1.md`

Update:

- `project/project-completion-roadmap.md`
- `project/project-map.md`
- `project/open-task-prompt-queue-2026-07-18.md`

## Non-Goals

- Do not invent bibliography.
- Do not cite protected modern translations as base text.
- Do not collapse digital repository paths into paper-facing citations without print-safe equivalents.

## Validation

Run:

```bash
python3 tools/qa_crosscheck.py
git diff --check
```

## Final Report

Report:

- dossier structural changes;
- provisional sections still needing bibliography verification;
- QA result;
- whether dossier is publication-ready or still draft.
