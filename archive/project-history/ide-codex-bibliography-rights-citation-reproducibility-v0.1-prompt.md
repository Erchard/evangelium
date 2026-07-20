# IDE Codex Prompt: Bibliography, Rights, Citation, and Reproducibility Pass v0.1

## Objective

Create the publication safety layer for bibliography, rights, citation policy, source hierarchy, and reproducibility.

## Why This Matters

The project is intended for paper and digital publication. It must not depend on hidden web links, protected modern translations, or undocumented local source extraction. Paper readers need print-safe citations; digital researchers need source paths and reproducibility notes.

## Required Inputs

Read:

- `sources/primary_texts/source-register.md`
- `sources/primary_texts/collection-log.md`
- `project/print-and-digital-publication-architecture.md`
- `project/final-product-specification.md`
- `reconstruction/earliest-sayings-gospel/evidence-dossier-en.md`
- `reconstruction/earliest-sayings-gospel/greek-retroversion-confidence-audit-v0.1.md`
- any existing files in `bibliography/`

## Required Outputs

Create or update:

- `project/rights-and-citation-policy.md`
- `project/source-reproducibility-note.md`
- `bibliography/bibliography-working.md`
- `bibliography/source-rights-register.md`
- `project/open-task-prompt-queue-2026-07-18.md`

Update:

- `project/project-completion-roadmap.md`
- `project/project-map.md`
- `README.md`

## Required Content

Include:

- public-domain / open / protected-source distinctions;
- rule that modern protected translations are controls, not base text;
- citation format for paper books;
- digital companion source-path policy;
- local source snapshot policy;
- SBLGNT working-control note;
- P.Oxy. / NHC II witness labels;
- bibliography placeholders only where exact bibliographic data still requires human verification.

## Non-Goals

- Do not invent complete bibliographic details.
- Do not claim rights status without evidence.
- Do not add long copyrighted quotations.

## Validation

Run:

```bash
git diff --check
```

Run `python3 tools/qa_crosscheck.py` if any reconstruction files are touched.

## Final Report

Report:

- created policy files;
- unresolved bibliographic verification needs;
- publication risks reduced.
