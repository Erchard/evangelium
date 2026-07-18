# Evidence / Control Gap Audit

Status: created 2026-07-18 after evidence/control warning reconciliation.

## Purpose

This audit separates stale card warnings from true remaining gaps. Earlier card text used generic warnings such as "немає окремого файлу; прогалина лишається видимою." Those warnings were not precise enough for publication work because they mixed three different states:

- a local evidence/control file already exists and should be linked;
- no local file exists and the gap is real;
- no separate cluster note is required for the current decision.

## Current Counts

| Category | Count | Meaning |
| --- | ---: | --- |
| Old generic evidence/control warning phrases | 0 | The stale exact phrases were removed from card apparatus sections. |
| Evidence-note TRUE_GAP markers | 0 | The 23 missing evidence notes were created and linked back into their cards. |
| Synoptic/control TRUE_GAP markers | 0 | The 47 former markers were classified and replaced with concrete card-level decisions. |
| Cluster/context "not required" markers | 68 | These cards do not currently need a cluster note unless a future cluster pass reopens them. |

## Evidence Notes Remediated

Dedicated evidence notes were created for Logia:

12, 13, 15, 19, 43, 53, 61, 70, 71, 74, 80, 83, 84, 85, 87, 88, 98, 102, 105, 108, 110, 112, 114.

Each new note now records decision, textual witness state, Greek policy, control state, main evidence, early-core assessment, secondary-layer indicators, reconstruction implication, and next work. The corresponding card evidence-note field now links to the local note.

## Synoptic / Control Gaps Classified

The former synoptic/control gaps in these Logia were classified:

1, 7, 24, 28, 29, 30, 40, 42, 43, 48, 49, 50, 51, 52, 53, 56, 58, 59, 60, 61, 62, 67, 68, 69, 70, 71, 74, 77, 80, 81, 82, 83, 84, 85, 87, 88, 92, 97, 98, 101, 102, 105, 108, 110, 111, 112, 114.

The classification is recorded in `project/synoptic-control-gap-classification-2026-07-18.md`.

Current classification counts:

- `MERGE_WITH_EXISTING_CLUSTER`: 15
- `MERGE_WITH_EXISTING_CONTROL`: 1
- `CREATE_CONTROL_FILE_RESOLVED`: 17
- `CREATE_CONTROL_FILE`: 0
- `NO_DIRECT_CONTROL_RATIONALE`: 14

## Remediation Rule

Do not delete a `TRUE_GAP` marker unless one of these actions has been completed:

- a local evidence note or control file has been created and linked in the card;
- an existing local note/control file has been identified and linked in the card;
- a concise no-direct-control rationale has been written directly in the card and recorded in the audit.

Do not change clean-reader membership during this documentary pass.

## Recommended Next Step

Run the next publication-quality pass: card decision coherence audit for duplicated or superseded status blocks, followed by Greek-layer freeze and appendix publication editing.
