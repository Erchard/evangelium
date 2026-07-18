# Duplicate-Status Prose Audit

Status: Phase B.2 completed, 2026-07-18.

## Purpose

This pass removes the most visible card-level decision-coherence risk after the metadata sync. The problem was not missing evidence. The problem was that many cards preserved multiple status layers with headings that could make a historical/local block look equal to the current gold-level publication status.

No clean-reader membership changes were made.

## Plan

1. Scan all 114 cards for:
   - old `## Попередній статус` headings;
   - old `### Поточне рішення` headings;
   - missing `### Publication Status` blocks;
   - local/gold-level decision disagreement.
2. Rename historical/local headings so their hierarchy is explicit.
3. Align only unambiguous wording conflicts between local decision snapshot and gold-level publication status.
4. Check for broken `Evidence Links` / `Synoptic/control files` sections.
5. Run project QA.

## Work Completed

### Heading hierarchy

All 114 cards now use `### Локальний зріз рішення` instead of `### Поточне рішення`.

This matters because the old Ukrainian heading sounded like the final current decision, even though each card also has a later `Gold-level status check v0.2` block.

The 79 cards that preserved an older `## Попередній статус` section now use `## Історичний локальний статус` with an explicit note:

- it is a historical/local layer;
- if it disagrees with the gold-level block, the gold-level block has priority.

### Decision alignment

Five substantive stale/confusing cases were aligned:

- Logion 21: gold-level status now matches `DEFER_TO_CLUSTER`; the thief/watchfulness subunit is control material for 103A, not a separate clean-reader unit.
- Logion 65: local decision now matches `KEEP_APPENDIX_ONLY_FOR_NOW`.
- Logion 66: local decision now matches `KEEP_APPENDIX_ONLY_FOR_NOW`.
- Logion 90: gold-level status now matches `KEEP_APPENDIX_ONLY_FOR_NOW`.
- Logion 104: gold-level status now matches `DEFER_TO_CLUSTER_BEFORE_READER_DECISION` for the bridegroom-fasting core, with full logion appendix-only.

Six additional split-core wording differences were normalized without changing decisions:

- Logion 46
- Logion 91
- Logion 96
- Logion 100
- Logion 103
- Logion 107

### Structural checks

Checked for empty or broken sections:

- `Evidence note / dossier files`
- `Synoptic/control files`

No empty/broken sections remained after the pass.

## Verification Result

Machine audit after remediation:

- local/gold-level decision conflicts: 0;
- cards missing gold-level publication status: 0;
- old `## Попередній статус` headings: 0;
- old `### Поточне рішення` headings: 0;
- new `### Локальний зріз рішення` headings: 114;
- new `## Історичний локальний статус` headings: 79.

## Remaining Work

The next high-value project task is no longer card-status synchronization. The next task is publication-layer polish:

1. Greek-layer freeze: verify that every Greek line is clearly labeled as extant witness or hypothetical retroversion.
2. Print-safe appendix consolidation: especially Logia 81-114.
3. Evidence dossier publication pass: methodology, bibliography, source hierarchy, and concise inclusion/exclusion defense.

Recommended next task: start with Greek-layer freeze because it protects both print books and the scholarly digital companion.
