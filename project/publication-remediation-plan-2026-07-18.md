# Publication Remediation Plan

Status: active remediation plan, 2026-07-18.

## Current Readiness Estimate

Working estimate: 82-85%.

The project is no longer blocked by corpus coverage. The main text, all 114 cards, evidence notes, control classification, and clean-reader synchronization are in place. The remaining work is publication-quality control: technical control files, final appendix editing, evidence dossier polish, Greek retroversion verification, bibliography/rights, and final print/digital generation.

## Primary Defects To Remove

| Priority | Defect | Current State | Done When |
| ---: | --- | --- | --- |
| 1 | Remaining technical control files | CLOSED: 0 `CREATE_CONTROL_FILE` markers remain after the technical-control remediation pass. | All former markers are now `CREATE_CONTROL_FILE_RESOLVED` and linked to local control files. |
| 2 | Duplicated/overriding decision sections | CLOSED: metadata sync and duplicate-status prose audit are complete. | Card-level decision audit confirms local/historical blocks are clearly subordinate to gold-level publication status. |
| 3 | Greek-layer freeze | CLOSED: publication-control freeze pass completed; remaining Greek work is later style/bibliography polish, not witness-status clarification. | Every current clean-reader Greek layer is labeled as extant witness, partial/lacunose witness, or hypothetical retroversion with confidence and source basis. |
| 4 | Full appendix editorial consolidation | Logia 1-80 are more consolidated; 81-114 still need print-safe editing. | All 114 appendix chapters read as a book, not as stitched card exports. |
| 5 | Evidence dossier publication pass | Dossier is useful but still working-level. | English dossier has methodology, source hierarchy, logion summaries, inclusion/exclusion rationale, and bibliography. |
| 6 | Bibliography, rights, and citation | Principles exist, final apparatus not complete. | Bibliography and source/citation policy are ready for public release. |
| 7 | Final product generation | Print/digital architecture exists. | Ukrainian and English print-ready books plus digital scholarly companion can be generated and checked. |

## Execution Order

### Phase A: Finish Remaining Technical Controls

Resolved the former `CREATE_CONTROL_FILE` group in thematic packages:

1. CLOSED: Logia 81 and 110: wealth-renunciation and anti-world control. Use Logion 63 and living/dead/world controls.
2. CLOSED: Logia 83, 84, 85: image, preexistence, Adam, and deathlessness control.
3. CLOSED: Logia 87 and 112: body-soul anthropology control.
4. CLOSED: Logion 88: revelation/transmission control.
5. CLOSED: Logion 114: Mary/Peter/gender-transformation exclusion control.

### Phase B: Card Decision Coherence Audit

Review duplicated decision/status sections and update stale local statements that may conflict with current gold-level blocks. Do not change clean-reader membership unless a separate decision pass explicitly requires it.

Phase B.1 completed:

- stale card gold-level evidence/control metadata synchronized;
- workflow matrix evidence-note flags synchronized;
- all-114 decision table stale `no direct evidence; no control file` rows updated.

Phase B.2 completed:

- old `Попередній статус` and `Поточне рішення` headings were renamed to explicit historical/local layers;
- local/gold-level decision conflicts were reduced to 0;
- split-core wording differences were normalized without changing clean-reader membership.

### Phase C: Greek Layer Freeze

CLOSED on 2026-07-18. Extant Greek witness versus `Greek retroversion, hypothetical` was audited for the clean reader and parallel edition. The stale 34-unit Greek confidence audit was updated to the current 37-unit reader, Logia 46, 91, and 103 were added as hypothetical retroversions, and the all-114 table now clarifies that its `Greek Status` column records loaded Greek Thomas papyrus evidence rather than the whole publication Greek layer.

### Phase D: Appendix Publication Editing

Continue print-safe editorial consolidation from Logia 81-114. Remove card-derived duplication, keep source/control trail available for digital use, and make the paper-readable commentary self-contained.

### Phase E: Evidence Dossier And Bibliography

Turn `evidence-dossier-en.md` into a publication-facing defense of the reconstruction. Add methodology, uncertainty model, source hierarchy, bibliography, rights/citation policy, and concise summaries for excluded/deferred high-impact logia.

### Phase F: Final Book Generation

Generate and inspect:

- Ukrainian clean text + appendix book.
- English clean text + appendix/evidence book or companion.
- Digital scholarly companion retaining full repo paths and machine-checkable evidence links.

## Current Execution

Completed task: Phase A, all remaining technical-control packages.

Expected output:

- local control file in `controls/synoptic-parallels/`;
- card links for Logia 83, 84, 85, 87, 88, 112, and 114;
- updated classification and deficiency audits;
- QA pass.

Output created:

- `controls/synoptic-parallels/logia-083-084-085-image-preexistence-controls.md`
- `controls/synoptic-parallels/logia-087-112-body-soul-controls.md`
- `controls/synoptic-parallels/logion-088-revelation-transmission-controls.md`
- `controls/synoptic-parallels/logion-114-mary-peter-gender-exclusion-controls.md`
- Logia 83, 84, 85, 87, 88, 112, and 114 cards linked to new control packages.
- `CREATE_CONTROL_FILE_RESOLVED`: 17.
- Remaining `CREATE_CONTROL_FILE`: 0.

Next active task: Phase D, print-safe full appendix editorial consolidation for Logia 81-114, beginning with Logia 81-90.
