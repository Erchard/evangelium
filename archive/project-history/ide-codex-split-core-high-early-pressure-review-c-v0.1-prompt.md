# IDE Codex Prompt: Split-Core / High-Early Pressure Review C v0.1

## Task

Perform the next pre-freeze content review for the strongest high-early-score non-reader logia:

- Logion 46
- Logion 90
- Logion 91
- Logion 103
- Logion 104

The goal is not to expand the clean reader automatically. The goal is to decide which units deserve a later controlled clean-reader candidate pass, which must remain appendix-only, and which require cluster handling before any reader decision.

## Context

The project reconstructs the earliest recoverable sayings gospel, not the full Gospel of Thomas. The clean reader must remain short, defensible, and free of obvious late or dependent material. A high early-probability score is not by itself enough for inclusion.

The current probability-pressure audit flags these five logia as the strongest non-reader pressure points:

- Logion 46: John the Baptist / least in the kingdom.
- Logion 90: come to me / yoke / rest.
- Logion 91: recognizing sky and earth but not the time.
- Logion 103: thief / watchfulness.
- Logion 104: fasting / bridegroom.

## Required Inputs

Read and cross-check:

- `project/probability-vs-reader-decision-audit-2026-07-18.md`
- `reconstruction/earliest-sayings-gospel/final-reader-probability-pressure-review-v0.1.md`
- `reconstruction/earliest-sayings-gospel/inclusion-decisions-table.md`
- `reconstruction/earliest-sayings-gospel/all-114-publication-decision-table-v0.1.md`
- `reconstruction/earliest-sayings-gospel/controlled-clean-reader-candidate-pass-v0.1.md`
- `reconstruction/earliest-sayings-gospel/split-core-decision-review-b-v0.1.md`
- evidence notes for Logia 46, 90, 91, 103, and 104
- corpus cards for Logia 21, 22, 46, 90, 91, 103, and 104
- existing control files for Logia 46, 90, 103, and ritual-ethics / bridegroom-fasting material
- Ukrainian full appendix sections for Logia 46, 90, 91, 103, and 104

## Method

For each target logion:

1. Separate possible early core from full Thomas form.
2. Identify direct manuscript witness status: extant Greek Thomas, Coptic only, or hypothetical Greek retroversion.
3. Identify canonical controls and whether they are multiple-control, one-source-control, or internal-only.
4. Test dependence risk.
5. Test duplication against already included clean-reader units.
6. Decide one of:
   - `PROMOTE_TO_CONTROLLED_READER_CANDIDATE_PASS`
   - `KEEP_APPENDIX_ONLY_FOR_NOW`
   - `DEFER_TO_CLUSTER_BEFORE_READER_DECISION`
   - `EXCLUDE_AS_SECONDARY`
7. Do not edit the clean reader in this pass unless the evidence is overwhelming and all language layers are updated together.

## Required Outputs

Create:

- `reconstruction/earliest-sayings-gospel/split-core-high-early-pressure-review-c-v0.1.md`

Create or update, if needed:

- `controls/synoptic-parallels/logion-091-recognition-time-controls.md`
- evidence notes for Logia 46, 90, 91, 103, and 104
- `reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-uk.md`
- `corpus/tables/logia-workflow-matrix.md`
- `reconstruction/earliest-sayings-gospel/all-114-publication-decision-table-v0.1.md`
- `reconstruction/earliest-sayings-gospel/inclusion-decisions-table.md`
- project navigation docs

## Acceptance Criteria

- Clean reader count remains unchanged unless a fully synchronized reader-generation pass is explicitly performed.
- The five target logia have explicit pre-freeze decisions.
- Logion 46 is compared with the already included Logion 22 child/smallness core.
- Logion 90 is evaluated for Matthew-dependence risk.
- Logion 91 is split between dialogue frame and recognition-of-time core.
- Logion 103 is tied to the unresolved Logion 21 / thief-watchfulness cluster.
- Logion 104 is split between bridegroom-fasting core and Thomas ritual / bridal-chamber frame.
- Stale appendix statements saying evidence notes/control files are missing are corrected where those files now exist.
- Run:

```bash
python3 tools/probability_reader_audit.py
python3 tools/qa_crosscheck.py
git diff --check
```

Do not claim the project is complete after this pass. The next major work will be either a controlled reader-candidate pass for promoted units or a cluster-control pass for thief/watchfulness and wealth/renunciation material.
