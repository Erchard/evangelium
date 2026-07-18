# IDE Codex Prompt: Logion 114 Publication-Level Exclusion Rationale v0.1

## Objective

Create a calm, publication-quality rationale for excluding Logion 114 from the reconstructed earliest sayings gospel while still explaining it seriously in the appendix.

## Why This Matters

Logion 114 is a high-risk reader-facing case. Without a clear rationale, exclusion may look ideological rather than historical-critical. The project must explain why this logion is likely secondary without dismissing the text or treating it polemically.

## Required Inputs

Read:

- `corpus/cards/logion-114.md`
- `corpus/tables/logia-workflow-matrix.md`
- `corpus/tables/logia-index.md`
- `reconstruction/earliest-sayings-gospel/all-114-publication-decision-table-v0.1.md`
- `reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-uk.md`
- `reconstruction/earliest-sayings-gospel/evidence-dossier-en.md`
- `project/final-product-specification.md`

Also inspect any source text and internal Thomas parallels referenced in the card.

## Required Analysis

Address:

- Coptic witness status;
- absence or presence of loaded Greek witness;
- dialogue frame with Simon Peter and Mary;
- gender transformation language;
- relation to Thomasine community/redactional concerns;
- why this looks unlike a compact early sayings-gospel core;
- how to explain the logion responsibly to a modern reader.

## Required Outputs

Create:

- `reconstruction/earliest-sayings-gospel/notes/logion-114-exclusion-rationale-en.md`
- `reconstruction/earliest-sayings-gospel/logion-114-publication-exclusion-rationale-v0.1.md`

Update:

- `corpus/cards/logion-114.md`
- `corpus/tables/logia-workflow-matrix.md`
- `reconstruction/earliest-sayings-gospel/all-114-publication-decision-table-v0.1.md`
- `reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-uk.md`
- `reconstruction/earliest-sayings-gospel/evidence-dossier-en.md`
- `project/open-task-prompt-queue-2026-07-18.md`

## Tone Rules

- No polemic.
- No apologetic shortcut.
- No modern doctrinal framing.
- Explain the reconstruction decision historically and textually.
- Make clear that appendix inclusion is part of transparency.

## Validation

Run:

```bash
python3 tools/qa_crosscheck.py
git diff --check
```

## Final Report

Report:

- exclusion rationale summary;
- files updated;
- whether any project status changed;
- remaining risk.
