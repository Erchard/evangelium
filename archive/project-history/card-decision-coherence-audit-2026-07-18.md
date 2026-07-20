# Card Decision Coherence Audit

Status: Phase B metadata-coherence pass completed, 2026-07-18.

## Purpose

This audit records the first card decision coherence pass after all technical `CREATE_CONTROL_FILE` gaps were closed.

The goal was not to change clean-reader membership. The goal was to remove stale metadata that could mislead an editor or reader into thinking evidence notes or control packages were still missing after they had already been created.

## Defect Found

The strongest current defect was metadata drift between three layers:

1. Individual cards had newer evidence/control apparatus.
2. `corpus/tables/logia-workflow-matrix.md` still marked several existing evidence notes as `NO`.
3. `reconstruction/earliest-sayings-gospel/all-114-publication-decision-table-v0.1.md` still used stale phrases such as `no direct evidence; no control file` for logia whose evidence notes and, in some cases, control packages already existed.

This was a publication-quality risk because the project could make future decisions from stale central tables instead of the current card apparatus.

## Remediation Plan

1. Scan all 114 cards for stale gold-level phrases:
   - `Evidence note in matrix: NO`
   - `окремого evidence note ще немає`
   - `окремого direct evidence note ще немає`
   - `окремого control file ще немає`
2. Update card gold-level blocks only where the local file already exists or the card already contains a valid control/rationale.
3. Synchronize `corpus/tables/logia-workflow-matrix.md` so every existing local evidence note is marked `YES`.
4. Update `all-114-publication-decision-table-v0.1.md` for rows where stale evidence/control language contradicted existing notes or control packages.
5. Preserve all clean-reader decisions unchanged.
6. Run structural QA and probability/reader audit.

## Work Completed

### Card gold-level metadata

Updated 51 card files where gold-level Evidence Links still contained stale missing-evidence or missing-control wording.

The update rule was conservative:

- if a local evidence note exists, the card now links it directly;
- if a control package exists, the card now links it directly;
- if an existing cluster-control applies, the card now identifies cluster-control support;
- if no direct external control exists, the card now says this is an explicit no-direct-control rationale rather than an unresolved technical gap.

### Workflow matrix

`corpus/tables/logia-workflow-matrix.md` was synchronized so evidence notes created during earlier remediation passes are no longer marked `NO`.

Additional status alignment was applied for the newly closed technical-control group:

- Logia 81 and 110: wealth-renunciation technical control.
- Logia 83, 84, and 85: image/preexistence/Adam technical control.
- Logia 87 and 112: body-soul anthropology technical control.
- Logion 88: revelation/transmission technical control.
- Logion 114: Mary/Peter/gender-transformation exclusion control.

### All-114 decision table

Updated 23 rows that still said `no direct evidence; no control file` even though evidence notes now exist:

12, 13, 15, 19, 43, 53, 61, 70, 71, 74, 80, 83, 84, 85, 87, 88, 98, 102, 105, 108, 110, 112, 114.

Also clarified Logia 1 and 7 so `no control file` is not mistaken for an unresolved technical gap.

## Current Result

Machine checks after this pass should confirm:

- no stale `Evidence note in matrix: NO` remains in card gold-level blocks;
- no stale Ukrainian missing-evidence phrase remains in card gold-level blocks;
- no stale Ukrainian missing-control phrase remains in card gold-level blocks;
- no `no direct evidence; no control file` phrase remains in the all-114 decision table;
- clean-reader membership remains unchanged.

## What This Pass Did Not Do

This pass did not rewrite the full prose of the appendix or evidence dossier. It also did not resolve deeper semantic questions where older sections such as `Попередній статус`, `Поточне рішення`, and `Publication Status` all coexist but agree in substance.

Those duplicated blocks remain the next editorial-coherence task.

## Next Step

Run Phase B.2: duplicate-status prose audit.

The next pass should inspect all cards for reader-facing confusion caused by multiple status sections, especially:

- older `Попередній статус` sections;
- older `Поточне рішення` sections;
- later `Gold-level status check` sections;
- split-core decisions where only a core is included but the full logion remains appendix-only.

The next pass may standardize labels, but it must not change clean-reader membership unless a separate controlled decision review is explicitly opened.
