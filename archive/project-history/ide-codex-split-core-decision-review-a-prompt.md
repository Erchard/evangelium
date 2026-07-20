# IDE Codex Prompt: Split-Core Decision Review A

## Mission

Execute the next work package identified by `final-all-114-decision-audit-v0.1.md`: split-core decision review for the strongest remaining non-included candidates.

Target logia:

- Logion 45: grapes/thorns and good/evil heart treasure
- Logion 47: two masters, new wine/wineskins, patch
- Logion 63: rich fool / storage and death
- Logion 64: banquet invitation and anti-merchant ending
- Logia 65-66: wicked tenants and rejected stone

## Primary Outputs

Create or update:

- `reconstruction/earliest-sayings-gospel/split-core-decision-review-a-v0.1.md`
- missing control files in `controls/synoptic-parallels/`
- `reconstruction/earliest-sayings-gospel/inclusion-decisions-table.md`
- `corpus/tables/logia-workflow-matrix.md`
- `project/project-completion-roadmap.md`
- `project/publication-gap-audit-v0.1.md`
- `sources/primary_texts/collection-log.md`

Do not edit the clean Ukrainian reader in this pass.

## Required Work

For each target:

1. Separate the full Thomas logion into possible early cores and likely secondary arrangement.
2. Identify synoptic/scriptural controls.
3. Decide one of:
   - `PROMOTE_CANDIDATE_FOR_READER_PASS`
   - `KEEP_APPENDIX_ONLY_FOR_NOW`
   - `DEFER_CLUSTER`
   - `EXCLUDE_AS_SECONDARY`
4. Mark Greek status clearly:
   - no loaded extant Greek Thomas witness for these targets;
   - any future Greek form is `Greek retroversion, hypothetical`.
5. Explain whether the full logion, a short core, or no part should be considered for clean-reader promotion.

## Quality Bar

Do not promote a full composite unit just because one of its subunits is early-looking. Prefer smaller cores and honest uncertainty.

If a core is strong but not ready for direct clean-reader editing, mark it as a candidate for a later controlled clean-reader pass.

## Verification

After editing:

- confirm `reconstructed-gospel-uk.md` was not edited;
- confirm all target logia have control/review references;
- confirm workflow matrix no longer says the target package has no dedicated control;
- run `git diff --check`.
