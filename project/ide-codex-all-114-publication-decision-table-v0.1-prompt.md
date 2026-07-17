# IDE Codex Prompt: True All-114 Publication Decision Table v0.1

You are working in the EUAGELIA project. Execute Phase 4 of the quality-remediation plan: create the true all-114 publication decision table.

## Purpose

Create one publication-control document that covers all 114 Gospel of Thomas logia and split-core units. This table must be the bridge between the current working corpus and the final clean reader / appendix / evidence dossier.

The goal is not to invent new decisions. The goal is to consolidate the best current decisions, expose uncertainty, and make every inclusion/exclusion/defer decision traceable.

## Required Context

Read first:

1. `project/project-quality-remediation-plan-v0.1.md`
2. `reconstruction/earliest-sayings-gospel/evidence-control-inventory-v0.1.md`
3. `corpus/tables/logia-workflow-matrix.md`
4. `reconstruction/earliest-sayings-gospel/inclusion-decisions-table.md`
5. `reconstruction/earliest-sayings-gospel/final-all-114-decision-audit-v0.1.md`
6. `reconstruction/earliest-sayings-gospel/controlled-clean-reader-candidate-pass-v0.1.md`
7. `reconstruction/earliest-sayings-gospel/split-core-decision-review-a-v0.1.md`
8. `reconstruction/earliest-sayings-gospel/split-core-decision-review-b-v0.1.md`
9. `corpus/cards/poxy-xml-extraction-audit-v0.1.md`

## Required Output

Create:

- `reconstruction/earliest-sayings-gospel/all-114-publication-decision-table-v0.1.md`

The file must include:

1. Executive summary.
2. Decision taxonomy.
3. Counts by publication status.
4. Clean-reader freeze candidate list.
5. Full all-114 table.
6. Split-core notes for logia where only a subunit enters or remains live.
7. Publication blockers before final freeze.
8. Recommended next step.

## Required Table Columns

For every logion or split-core unit:

- Logion / unit;
- publication status;
- clean reader status;
- confidence;
- Greek status;
- evidence/control status;
- primary rationale;
- appendix obligation;
- next action before final freeze.

## Decision Taxonomy

Use these statuses consistently:

- `READER_INCLUDE_MARKED`: included in the clean reader with apparatus marker/caution.
- `APPENDIX_ONLY_STABLE`: should not enter the clean reader under the current model, but has enough evidence/control to be explained confidently in appendix.
- `APPENDIX_ONLY_UNCERTAIN`: interesting but unresolved; appendix explanation required before publication.
- `DEFER_TO_CLUSTER`: not individually ready; treat in a thematic/source cluster.
- `EXCLUDE_AS_SECONDARY`: likely secondary or outside the earliest reconstructed sayings gospel.
- `NEEDS_EVIDENCE_BEFORE_FINAL`: cannot receive publication-level confidence until direct evidence/no-note rationale is created.

## Quality Rules

- Do not change the clean reader.
- Do not promote new logia into the clean reader.
- Keep all Greek retroversions explicitly hypothetical.
- Do not treat canonical parallels as Thomas witnesses.
- For included split-core units, identify the included core and the excluded/appendix material.
- For excluded/deferred material, still require appendix explanation.
- If evidence is missing, say so; do not hide the gap behind a confident label.
- Use `evidence-control-inventory-v0.1.md` for evidence/control status.

## Documentation Updates

After creating the decision table:

- update `project/project-map.md`;
- update `project/project-quality-remediation-plan-v0.1.md` to mark Phase 4 as completed;
- update `project/ide-codex-quality-remediation-master-prompt.md` so the next recommended phase becomes Phase 5: full appendix expansion;
- update `README.md`;
- update `sources/primary_texts/collection-log.md`.

## Final Report

Report:

- files changed;
- number of clean-reader marked units;
- number of appendix-only/defer/exclude/needs-evidence rows;
- the strongest remaining blockers;
- recommended next step.

Commit and push the changes unless explicitly instructed not to.

