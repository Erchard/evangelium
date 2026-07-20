# IDE Codex Prompt: Thief / Watchfulness Cluster-Control for Logia 21 and 103 v0.1

## Objective

Resolve the pending thief/watchfulness cluster that blocks a responsible reader decision for Logion 103A and clarifies the composite status of Logion 21.

The project reconstructs the earliest recoverable sayings gospel, not the whole Gospel of Thomas. Therefore the task is not to include or exclude whole Thomas logia mechanically. Separate early, controlled cores from later, composite, or Thomas-specific expansions, and keep the clean reader free of commentary, brackets, and uncertainty markers.

## Required Inputs

Read and use:

- `corpus/cards/logion-021.md`
- `corpus/cards/logion-103.md`
- `reconstruction/earliest-sayings-gospel/notes/logion-021-evidence-en.md`
- `reconstruction/earliest-sayings-gospel/notes/logion-103-evidence-en.md`
- `controls/synoptic-parallels/logion-103-thief-watchfulness-controls.md`
- `reconstruction/earliest-sayings-gospel/split-core-decision-review-b-v0.1.md`
- `reconstruction/earliest-sayings-gospel/split-core-high-early-pressure-review-c-v0.1.md`
- `reconstruction/earliest-sayings-gospel/controlled-reader-candidate-pass-46a-91a-v0.1.md`
- current clean reader and language layers in `reconstruction/earliest-sayings-gospel/`
- `corpus/tables/logia-workflow-matrix.md`
- `reconstruction/earliest-sayings-gospel/all-114-publication-decision-table-v0.1.md`
- `reconstruction/earliest-sayings-gospel/inclusion-decisions-table.md`
- `reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-uk.md`

## Method

1. Treat Logion 21 as a composite Thomas unit with at least four subunits:
   - children on another's field;
   - thief / householder / watchfulness;
   - anti-world guarding language;
   - harvest / sickle / ripe fruit.
2. Treat Logion 103 as a shorter thief/watchfulness beatitude with a plausible early core and a secondary-risk expansion:
   - possible early core: knowing when the thief comes and being ready/watchful;
   - likely secondary-risk material: gathering kingdom/domain, girding language, and the expanded entry scene.
3. Compare the cluster against Matthew 24:43, Luke 12:39, Mark 13:33-37, and Mark 4:29 as canonical controls, while keeping clear that these are not Thomas manuscript witnesses.
4. Decide whether the clean reader should:
   - include no unit;
   - include a short 103A reader core with marker;
   - include a short 21 thief/watchfulness core with marker;
   - include both, only if duplication is defensible.
5. Prefer the smallest, most controlled reader unit. Do not include a full composite logion.

## Expected Decision Standard

Promote a unit only if:

- it has clear early-tradition control;
- it can be stated as a compact saying without Thomas-specific expansion;
- its inclusion does not duplicate another printed unit in a confusing way;
- the appendix can explain exactly what was included and what was left out.

If promoted, mark it as `INCLUDE_WITH_MARKER`, not as unqualified certainty.

## Required Outputs

Create:

- `reconstruction/earliest-sayings-gospel/notes/thief-watchfulness-cluster-control-21-103-en.md`
- `reconstruction/earliest-sayings-gospel/thief-watchfulness-cluster-control-pass-21-103-v0.1.md`

If the decision changes the clean reader, update:

- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-uk.md`
- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-en.md`
- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-coptic.md`
- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-greek.md`
- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-ar-quranic-register.md`
- `reconstruction/earliest-sayings-gospel/parallel-edition.md`
- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-uk-apparatus.md`
- `reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-uk.md`
- `corpus/cards/logion-021.md`
- `corpus/cards/logion-103.md`
- `reconstruction/earliest-sayings-gospel/notes/logion-021-evidence-en.md`
- `reconstruction/earliest-sayings-gospel/notes/logion-103-evidence-en.md`
- `controls/synoptic-parallels/logion-103-thief-watchfulness-controls.md`
- `corpus/tables/logia-workflow-matrix.md`
- `reconstruction/earliest-sayings-gospel/all-114-publication-decision-table-v0.1.md`
- `reconstruction/earliest-sayings-gospel/inclusion-decisions-table.md`
- `reconstruction/earliest-sayings-gospel/evidence-dossier-en.md`
- project documentation that reports reader counts and next actions.

Update `tools/qa_crosscheck.py` if and only if the clean reader count changes.

## Quality Rules

- Do not present reconstructed Greek as extant Greek.
- Do not hide excluded material. Full Logia 21 and 103 must remain discussed in the appendix even if 103A is promoted.
- Use print-safe prose in reader-facing appendix material; repository paths may remain in digital apparatus sections.
- Preserve Thomas numbering in the clean reader.
- Run:

```bash
python3 tools/qa_crosscheck.py
python3 tools/probability_reader_audit.py
git diff --check
```

## Final Report

Report:

- the cluster decision;
- whether the clean reader changed;
- which files were created or updated;
- QA results;
- the next logical step after this pass.
