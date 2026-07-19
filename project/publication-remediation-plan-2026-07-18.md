# Publication Remediation Plan

Status: active remediation plan, updated 2026-07-19.

## Current Readiness Estimate

Working estimate: 99.75%.

The project is no longer blocked by corpus coverage. The main text, all 114 cards, evidence notes, control classification, clean-reader synchronization, full appendix consolidation, evidence dossier publication draft, bibliography/rights release verification, 104A ritual-ethics / bridegroom follow-up, Greek retroversion publication polish, final clean-reader freeze, generator-ready book source packages, render-proof preparation, first proof artifacts, first proof QA/layout correction, Bible-style book design/index pass, final proof polish, release-candidate audit, full Ukrainian book assembly, full Ukrainian proof QA, English full appendix structural generation, English appendix editorial-quality pass, full English proof QA, digital companion expansion, browsable companion HTML, final production/copyedit gate, Typst-ready production handoff package, and release-candidate audit v1.0-rc1 are in place. The remaining work is external Typst/professional production compilation, final human copyedit, release-candidate signoff, and final frozen checksums.

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
| 14 | Release-candidate proof package audit | CLOSED: current PDFs are proof skeletons, not release candidates. | A final blocker list and release-candidate verdict exist for paper and digital outputs. |
| 15 | Full book assembly and typesetting pipeline | CLOSED: 118-page Ukrainian full book proof generated; English proof package generated with explicit full-appendix blocker. | Ukrainian and English outputs include the promised book layers or explicit blockers before final render. |
| 16 | Full Ukrainian book proof QA and appendix typography | CLOSED: all 118 pages inspected; paper-facing appendix labels localized; QA passed. | Ukrainian full proof has page-by-page QA report and remaining blocker list. |
| 17 | English full 114-logion appendix generation | CLOSED: first complete structural English appendix exists and renders in a 177-page proof. | English paper proof includes clean text first plus all 114 commentary sections. |
| 18 | English appendix editorial quality pass | CLOSED: generator now creates less repetitive reader-facing English commentary and paper sanitizer removes draft/status leakage. | English appendix is readable as publication prose, not only a synchronized control draft. |
| 19 | Full English book proof QA and typography | CLOSED: 177-page English proof inspected textually and visually; no page-level blocker found. | English proof has page-level QA report and remaining blocker list. |
| 20 | Digital scholarly companion expansion | CLOSED: companion now has generated all-114 cross-reference index, source inventory, checksums, audit trail, Markdown source, and PDF proof. | Companion preserves source paths, evidence links, audit trail, all-114 logion navigation, rights, and reproducibility data. |
| 21 | Browsable digital companion HTML | CLOSED: static HTML companion has searchable/filterable all-114 index, expandable detail panels, source sections, audit trail, and valid local links. | Reader can search/filter all 114 logia and navigate to cards, evidence, controls, sources, audits, and reproducibility data. |
| 22 | Final production typesetting and copyedit gate | CLOSED: ReportLab is proof-only; Typst/professional handoff chosen as final path; checklist and blockers documented. | Project has a documented production path and release-candidate blockers list. |
| 23 | Typst production pilot / professional handoff | CLOSED AS HANDOFF: Typst-ready template, Ukrainian and English pilot sources, checklist, and manifest exist in `output/production-typst/`. Compilation is pending an external Typst/professional environment. | Project has a clear handoff package for final book layout. |
| 24 | External production compile and human copyedit signoff | NEXT: compile the Typst/professional production pilot outside this environment, expand the accepted template to the full books, perform final Ukrainian and English human copyedit, and freeze release checksums. | Final production PDFs are visually approved, copyedit is signed off, source redistribution is approved, and release manifest/checksums are frozen. |

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

### Phase F.5: Release-Candidate Proof Package Audit

CLOSED on 2026-07-19. Current PDFs passed structural and path-safety checks and have no visible clipping, but they are not release candidates for the final books because they do not yet include the full 114-logion commentary appendix. They are first public proof skeletons.

### Phase F.6: Full Book Assembly And Typesetting Pipeline

CLOSED on 2026-07-19. A separate full-book assembly/render pipeline now generates `book-source-uk-full.md`, `book-source-en-full.md`, and the digital companion source. Later passes expanded this into a 118-page Ukrainian full proof, a 177-page English full proof, a 16-page digital companion PDF proof, and a browsable HTML companion. ReportLab remains acceptable for proof generation, not final production typography.

### Phase F.7: Full Ukrainian Book Proof QA And Appendix Typography

CLOSED on 2026-07-19. The 118-page Ukrainian full proof was inspected through regenerated PNG/contact-sheet proofing; the title page, clean text, orientation page, all appendix pages, Logion 114, and bibliography page are present. The generator now localizes paper-facing appendix status labels instead of exposing English/internal metadata labels.

### Phase F.8: English Full 114-Logion Appendix Generation

CLOSED on 2026-07-19. A generator now creates `full-logion-commentary-appendix-en.md` from the frozen all-114 decision table and English clean reader. The English full proof now has 177 pages and includes all 114 appendix sections. The remaining English problem is prose quality, not structural absence.

### Phase F.9: English Appendix Editorial Quality Pass

CLOSED on 2026-07-19. The English appendix generator now adds reader-facing thematic explanations, special notes for key logia, clearer source-status prose, and less repetitive interpretation options. The English paper sanitizer removes obsolete draft/status leakage from paper-facing dossier material.

### Phase F.10: Full English Book Proof QA And Typography

CLOSED on 2026-07-19. The 177-page English full proof was rebuilt, scanned textually, rendered to PNG pages, inspected through contact sheets, and checked with image diagnostics. The clean text, all 114 appendix chapters, evidence dossier, included-logia/core summaries, Logion 114 exclusion summary, and bibliography are present without visible clipping, accidental blank pages, or paper-only path leakage.

### Phase F.11: Digital Scholarly Companion Expansion

CLOSED on 2026-07-19. A deterministic generator now creates the digital companion source, all-114 logion cross-reference TSV, source-witness inventory, artifact checksums, audit-trail index, expanded companion manifest, README, and a 16-page digital companion PDF proof. The companion intentionally preserves repository paths and machine-checkable apparatus excluded from paper books.

### Phase F.12: Browsable Digital Companion HTML

CLOSED on 2026-07-19. A deterministic HTML renderer now creates `output/digital-scholarly-companion/html/index.html` from the generated TSV indexes. The static companion has 114 expandable logion panels, search, reader/decision/Greek-status filters, source witness sections, audit trail, bibliography/rights links, reproducibility checklist, and 762 validated local file links.

### Phase F.13: Final Production Typesetting And Copyedit Gate

CLOSED on 2026-07-19. The current PDF outputs and HTML companion were inspected; stale documentation describing the English proof and digital companion as incomplete was corrected. The gate decision keeps ReportLab as proof-only and chooses Typst/professional handoff as the final production path. Final release-candidate blockers are now Typst production pilot or handoff, final human copyedit, public-source redistribution review, and final frozen checksums.

### Phase F.14: Typst Production Pilot / Professional Handoff

CLOSED AS HANDOFF on 2026-07-19. The current environment has no available `typst`, `xelatex`, or `pdflatex` compiler, so a compiled production pilot could not be generated here. Instead, the project now has a Typst-ready handoff package in `output/production-typst/`, including a template, Ukrainian and English pilot sources, README, checklist, and manifest.

### Phase F.15: Release-Candidate Audit v1.0-rc1

CLOSED WITH EXTERNAL BLOCKER on 2026-07-19. `project/release-candidate-audit-v1.0-rc1.md` records the project as content-complete and proof-package complete, but not a fully signed-off release candidate until production compile and human copyedit are completed outside this environment.

Next active task: external production compile and human copyedit signoff.
