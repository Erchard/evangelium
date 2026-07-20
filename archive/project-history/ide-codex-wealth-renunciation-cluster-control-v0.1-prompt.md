# IDE Codex Prompt: Wealth / Renunciation Cluster-Control v0.1

## Objective

Create the next major cluster-control pass for wealth, possessions, renunciation, treasure, lending, inheritance, and dependence-risk parables.

This pass should clarify which wealth/renunciation materials are already represented in the clean reader, which remain appendix-only, and which require later decision review.

## Why This Matters

The project's clean reader already includes several wealth-related cores: Logia 63, 72, 95, 100, and related anti-possession material. Other strong candidates remain outside the reader, especially Logia 64, 76, 81, 90, 109, and 110. Without a cluster-level note, the reader may not understand why some wealth sayings are printed while others are excluded or deferred.

## Required Inputs

Read:

- `project/project-completion-roadmap.md`
- `project/project-quality-audit-v0.1.md`
- `reconstruction/earliest-sayings-gospel/all-114-publication-decision-table-v0.1.md`
- `reconstruction/earliest-sayings-gospel/inclusion-decisions-table.md`
- `corpus/tables/logia-workflow-matrix.md`
- `reconstruction/earliest-sayings-gospel/evidence-dossier-en.md`
- `reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-uk.md`

Target cards and notes:

- `corpus/cards/logion-063.md`
- `corpus/cards/logion-064.md`
- `corpus/cards/logion-072.md`
- `corpus/cards/logion-076.md`
- `corpus/cards/logion-081.md`
- `corpus/cards/logion-090.md`
- `corpus/cards/logion-095.md`
- `corpus/cards/logion-100.md`
- `corpus/cards/logion-109.md`
- `corpus/cards/logion-110.md`
- related evidence notes and control files for these logia.

## Method

Cluster the material into at least these subgroups:

- rich fool / death and possessions;
- inheritance/division refusal;
- money lending / anti-usury / gift without repayment;
- Caesar/God possession boundary;
- banquet/exclusion and dependence risk;
- pearl/treasure/merchant;
- yoke/rest and Matthean dependence;
- hidden treasure and dependence risk;
- renunciation of world/wealth as possible Thomasine development.

For each subgroup, decide:

- current clean-reader representative;
- appendix-only material;
- dependence risk;
- secondary-layer markers;
- whether any new reader-candidate pass is justified.

## Required Outputs

Create:

- `reconstruction/earliest-sayings-gospel/notes/wealth-renunciation-cluster-control-en.md`
- `reconstruction/earliest-sayings-gospel/wealth-renunciation-cluster-control-pass-v0.1.md`

Update:

- target cards' cluster/context note links;
- `corpus/tables/logia-workflow-matrix.md`;
- `reconstruction/earliest-sayings-gospel/all-114-publication-decision-table-v0.1.md`;
- `reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-uk.md`;
- `reconstruction/earliest-sayings-gospel/evidence-dossier-en.md`;
- `project/project-completion-roadmap.md`;
- `project/project-map.md`;
- `project/open-task-prompt-queue-2026-07-18.md`.

## Non-Goals

- Do not add any new clean-reader unit unless the cluster argument explicitly promotes it to a later controlled reader pass.
- Do not remove already included clean-reader units.
- Do not treat hypothetical Greek retroversions as extant witnesses.

## Validation

Run:

```bash
python3 tools/qa_crosscheck.py
python3 tools/probability_reader_audit.py
git diff --check
```

## Final Report

Report:

- cluster decision by subgroup;
- whether clean reader changed;
- which logia remain appendix-only and why;
- next task after this pass.
