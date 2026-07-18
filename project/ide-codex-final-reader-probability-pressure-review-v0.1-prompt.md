# IDE Codex Prompt: Final Reader Probability-Pressure Review v0.1

## Mission

Execute a controlled review of probability pressure against the current clean reader before any final reader freeze.

This task follows:

- `project/probability-vs-reader-decision-audit-2026-07-18.md`
- `tools/probability_reader_audit.py`

The purpose is to resolve the most visible risk: the project may appear inconsistent if a late-leaning logion is printed in the clean reader, or if an early-leaning logion is excluded without a clear rationale.

## Non-Negotiable Rule

Do not automatically change the clean reader.

Probability score is an input, not the decision rule. A logion can be excluded despite early probability if:

- the preserved Thomas form is composite;
- the early core is already represented by a stronger clean-reader unit;
- the unit has dependence risk;
- the early core has not been safely isolated;
- Greek / Coptic / canonical controls are insufficient.

## Files To Use

Primary inputs:

- `project/probability-vs-reader-decision-audit-2026-07-18.md`
- `tools/probability_reader_audit.py`
- `corpus/tables/logia-workflow-matrix.md`
- `reconstruction/earliest-sayings-gospel/all-114-publication-decision-table-v0.1.md`
- `reconstruction/earliest-sayings-gospel/inclusion-decisions-table.md`
- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-uk.md`
- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-uk-apparatus.md`

Key cards:

- Included late-pressure case: `corpus/cards/logion-001.md`
- High-early non-reader cases: `corpus/cards/logion-046.md`, `064`, `076`, `078`, `079`, `090`, `091`, `093`, `094`, `103`, `104`, `109`, `113`
- Broader watchlist: `021`, `055`, `057`, `065`, `066`, `068`, `069`, `092`, `101`, `111`
- Missing numeric profile: `corpus/cards/logion-030.md`

Output:

- `reconstruction/earliest-sayings-gospel/final-reader-probability-pressure-review-v0.1.md`

## Required Review Decisions

For each reviewed logion, assign one of these review outcomes:

- `KEEP_IN_CLEAN_READER_WITH_FRAME_WARNING`
- `MOVE_TO_FRAME_REVIEW_BEFORE_FINAL_FREEZE`
- `PROMOTE_CANDIDATE_FOR_SPLIT_CORE_REVIEW`
- `KEEP_APPENDIX_ONLY_WITH_EXPLICIT_RATIONALE`
- `KEEP_APPENDIX_ONLY_AS_REDUNDANT_WITH_READER_UNIT`
- `DEFER_TO_CLUSTER_BEFORE_ANY_READER_CHANGE`
- `PROBABILITY_PROFILE_CLEANUP_REQUIRED`

## Required Analysis

1. Review Logion 1:
   - Is it a saying in the same sense as the other clean-reader units?
   - Does its late-leaning probability profile make clean-reader placement misleading?
   - Should it remain as a numbered clean-reader unit, or be moved to a prologue/frame review before final freeze?

2. Review the high-early non-reader group:
   - 94, 46, 90, 93, 103, 64, 76, 78, 79, 91, 104, 109, 113.
   - For each, state why high early probability does or does not justify reader promotion.

3. Review the broader early-pressure watchlist:
   - 21, 55, 57, 65, 66, 68, 69, 92, 101, 111.
   - Identify only those that should get priority before final freeze.

4. Identify probability-profile cleanup tasks:
   - duplicate profiles in 24 cards;
   - missing numeric profile for Logion 30;
   - split-core logia where full-logion probability and included-core probability must be separated.

## Acceptance Criteria

- Do not edit the clean reader in this pass.
- Produce a clear ranked recommendation list.
- Make Logion 1 decision pressure explicit.
- Make high-early non-reader rationale explicit.
- Run:

```bash
python3 tools/probability_reader_audit.py
python3 tools/qa_crosscheck.py
git diff --check
```

## Expected Result

The project should have a defensible pre-freeze review document showing that clean-reader inclusion is not based on raw percentages alone, while also identifying exactly which probability tensions must be resolved before final publication.
