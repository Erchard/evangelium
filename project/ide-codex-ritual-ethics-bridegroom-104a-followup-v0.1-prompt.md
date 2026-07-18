# IDE Codex Prompt: Ritual-Ethics / Bridegroom Follow-Up for 104A v0.1

## Objective

Resolve the pending 104A bridegroom-fasting reader pressure through a focused ritual-ethics / bridegroom cluster pass.

## Why This Matters

Logion 104 has strong canonical bridegroom-fasting controls, but the Thomas form includes ritual questions, sin/overcome language, and bridal-chamber framing. The project must decide whether any short 104A core belongs in the clean reader or remains appendix-only.

## Required Inputs

Read:

- `corpus/cards/logion-006.md`
- `corpus/cards/logion-014.md`
- `corpus/cards/logion-027.md`
- `corpus/cards/logion-104.md`
- `reconstruction/earliest-sayings-gospel/notes/ritual-ethics-cluster-006-014-027-104-en.md`
- `reconstruction/earliest-sayings-gospel/notes/logion-104-evidence-en.md`
- `reconstruction/earliest-sayings-gospel/split-core-high-early-pressure-review-c-v0.1.md`
- `reconstruction/earliest-sayings-gospel/all-114-publication-decision-table-v0.1.md`
- `reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-uk.md`
- `reconstruction/earliest-sayings-gospel/evidence-dossier-en.md`

Canonical controls:

- Mark 2:18-20
- Matthew 9:14-15
- Luke 5:33-35

## Required Decision

Choose one:

- promote only a short bridegroom-fasting core to a later controlled reader pass;
- keep 104A appendix-only;
- defer further because the bridal-chamber layer is too entangled.

Do not include full Logion 104 in the clean reader.

## Required Outputs

Create:

- `reconstruction/earliest-sayings-gospel/ritual-ethics-bridegroom-104a-followup-v0.1.md`

Update:

- `reconstruction/earliest-sayings-gospel/notes/ritual-ethics-cluster-006-014-027-104-en.md`
- `reconstruction/earliest-sayings-gospel/notes/logion-104-evidence-en.md`
- `corpus/cards/logion-104.md`
- `corpus/tables/logia-workflow-matrix.md`
- `reconstruction/earliest-sayings-gospel/all-114-publication-decision-table-v0.1.md`
- `reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-uk.md`
- `reconstruction/earliest-sayings-gospel/evidence-dossier-en.md`
- `project/open-task-prompt-queue-2026-07-18.md`

## Validation

Run:

```bash
python3 tools/qa_crosscheck.py
python3 tools/probability_reader_audit.py
git diff --check
```

## Final Report

Report:

- 104A decision;
- whether clean reader changed;
- rationale for full 104 exclusion;
- next task.
