# Publication Remediation Plan

Status: active remediation plan, updated 2026-07-19.

## Current Readiness Estimate

Working estimate: 98.5%.

The project is no longer blocked by corpus coverage. The main text, all 114 cards, evidence notes, control classification, clean-reader synchronization, full appendix consolidation, evidence dossier publication draft, bibliography/rights release verification, 104A ritual-ethics / bridegroom follow-up, Greek retroversion publication polish, final clean-reader freeze, generator-ready book source packages, render-proof preparation, first proof artifacts, first proof QA/layout correction, Bible-style book design/index pass, and final proof polish are in place. The remaining work is release-candidate proof judgment: page-by-page visual QA, final blocker classification, renderer adequacy decision, and release-candidate packaging.

## Primary Defects To Remove

| Priority | Defect | Current State | Done When |
| ---: | --- | --- | --- |
| 1 | Remaining technical control files | CLOSED: 0 `CREATE_CONTROL_FILE` markers remain after the technical-control remediation pass. | All former markers are now `CREATE_CONTROL_FILE_RESOLVED` and linked to local control files. |
| 2 | Duplicated/overriding decision sections | CLOSED: metadata sync and duplicate-status prose audit are complete. | Card-level decision audit confirms local/historical blocks are clearly subordinate to gold-level publication status. |
| 3 | Greek-layer freeze | CLOSED: publication-control freeze pass completed; remaining Greek work is later style/bibliography polish, not witness-status clarification. | Every current clean-reader Greek layer is labeled as extant witness, partial/lacunose witness, or hypothetical retroversion with confidence and source basis. |
| 4 | Full appendix editorial consolidation | Complete for Logia 1-114. | All 114 appendix chapters read as a book, not as stitched card exports. |
| 5 | Evidence dossier publication pass | CLOSED: dossier is now publication-facing draft v1.4, with source hierarchy, uncertainty model, and bibliography/rights note. | English dossier has methodology, source hierarchy, logion summaries, inclusion/exclusion rationale, and uncertainty model. |
| 6 | Bibliography, rights, and citation | CLOSED at release verification v0.2: generic verification markers converted to concrete release statuses. | Bibliography and source/citation policy are safe for proof preparation, with protected controls clearly limited. |
| 6A | Ritual-ethics / bridegroom 104A | CLOSED: 104A stabilized as appendix-only; full Logion 104 remains appendix-only. | 104A is either included, stabilized appendix-only, or deferred with cluster-level rationale. |
| 6B | Greek retroversion publication polish | CLOSED: final Greek wording/status consistency pass completed. | Greek witness labels and hypothetical retroversions are safe across clean reader, apparatus, appendix, dossier, and parallel edition. |
| 6C | Final clean-reader freeze | CLOSED: frozen 37-unit reader confirmed across language, decision, probability, and appendix layers. | Frozen reader can be used as source for book generation. |
| 7 | Final product generation | PARTIAL: generator-ready source packages and digital companion manifest exist; final rendering/proofing not yet complete. | Ukrainian and English print-ready books plus digital scholarly companion can be generated and checked. |
| 8 | Final bibliography and rights verify | CLOSED: release-level bibliography and source-rights pass completed. | Bibliography and rights status are safe for proof preparation or clearly marked as protected/control-only. |
| 9 | Print / digital render proof preparation | CLOSED: paper books and digital companion checked at proof-prep level. | Ukrainian and English paper sources are print-safe, digital apparatus remains complete, and rendering blockers are listed. |
| 10 | Render pipeline and first proofs | CLOSED: minimal renderer and first proof artifacts created. | Ukrainian, English, and digital companion proofs exist or rendering blocker is explicitly documented. |
| 11 | First proof QA and layout corrections | CLOSED: first visible paper defects were corrected and paper PDFs are path-safe. | Proofs have acceptable first-pass layout, no paper-only path leakage, and documented remaining design work. |
| 12 | Bible-style book design and index pass | CLOSED: paper proofs now use compact Bible-style clean text and split print indexes. | Raw all-114 tables are replaced by reader-safe paper indexes, with no repo paths or URLs in paper PDFs. |
| 13 | Final proof polish, bibliography, and TOC | CLOSED: front matter, proof-stable TOC, print source keys, and index compression improved. | Ukrainian and English paper PDFs can become release candidates after visual proofing and final corrections. |
| 14 | Release-candidate proof package audit | NEXT: inspect every page and decide renderer/package readiness. | A final blocker list and release-candidate verdict exist for paper and digital outputs. |

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

Full appendix editorial consolidation is complete for Logia 1-114. The stable appendix has now been used as input for the evidence dossier publication pass.

### Phase E: Evidence Dossier And Bibliography

`evidence-dossier-en.md` is now a publication-facing defense of the reconstruction. It has methodology, uncertainty model, source hierarchy, cluster summaries, current reader list, and concise summaries for excluded/deferred high-impact logia. Bibliography, rights, citation keys, and source reproducibility now have a release verification layer in `project/rights-and-citation-policy.md`, `project/source-reproducibility-note.md`, `bibliography/bibliography-working.md`, `bibliography/source-rights-register.md`, and `project/final-bibliography-rights-verify-v0.1.md`.

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

### Phase E.2: Greek Retroversion Publication Polish

CLOSED on 2026-07-18. The public-facing Greek and parallel layers now use normalized labels for `Extant Greek witness`, `Partial extant Greek witness`, `Lacunose extant Greek witness`, and `Greek retroversion, hypothetical`. No clean-reader membership changed.

### Phase E.3: Final Clean-Reader Freeze

CLOSED on 2026-07-18. The 37-unit clean reader is frozen for this edition. Ukrainian, English, Coptic, Greek, and parallel layers contain the same units in the same order; the English clean reader was cleaned of residual apparatus notes.

### Phase F.1: Generator-Ready Book Sources

CLOSED on 2026-07-18. First print-safe source packages were created for the Ukrainian and English paper books, and a digital scholarly companion manifest was created.

### Phase F.2: Render Pipeline And First Proofs

CLOSED on 2026-07-19. First HTML/PDF proofs were generated for the Ukrainian paper book, English paper book, and digital companion.

### Phase F.3: First Proof QA And Bible-Style Design

CLOSED on 2026-07-19. Paper proofs were moved toward a compact mass-Bible-style design. The clean reader is two-column and reader-first; raw technical all-114 tables were replaced by split paper indexes; paper PDF extracted text has no internal repository paths or URLs.

### Phase F.4: Final Proof Polish, Bibliography, And TOC

CLOSED on 2026-07-19. Paper proofs now have calmer front matter, proof-stable contents, print source keys, less dense non-included index, compressed witness/status indexes, and confirmed paper path-safety.

Next active task: release-candidate proof package audit.
