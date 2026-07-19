# Status Review And Remediation, 2026-07-19

Status: completed repo-internal cleanup pass, updated after full regeneration.

## Project State

EUAGELIA is now a complete scholarly proof package, but not yet a final publication release.

Approximate readiness:

- **Scholarly corpus and proof package:** 99%.
- **Final publishable books:** 96-97%.

The gap is no longer basic reconstruction work. The remaining work is final reader-facing copyedit, production typesetting, visual QA, source-rights freeze, and release tagging.

## Main Weak Point Found

The weakest current layer is no longer corpus completeness. It is the **final human editorial layer**: a slow read of the Ukrainian and English books as books, not as project output.

Examples of the class of problem:

- remaining awkward sentences that only a human-style copyedit can reliably catch;
- final decision on whether Logion 1 remains appendix-only or returns as the numbered prologue;
- final production layout beyond the current ReportLab proof renderer;
- external source-rights and citation freeze before public release.

## Actions Completed In This Pass

- Updated `README.md` to reflect the current 2026-07-19 state and current proof sizes.
- Added `project/project-completion-plan-2026-07-19.md` as the active route from proof package to 100%.
- Strengthened the Ukrainian paper-book sanitizer in `tools/assemble_full_book_sources.py`.
- Cleaned the Ukrainian appendix source from the most obvious leftover "marker", XML, project-internal, and machine-translation style phrases.
- Removed incomplete placeholder English translation slots from the Ukrainian appendix.
- Added an English paper-book sanitizer for internal status/code language.
- Normalized the Ukrainian proof typography toward a minimal book-style serif system: Times New Roman for Ukrainian/English and Greek text, with Noto Sans Coptic only as the required Coptic-script fallback.
- Added a clean majuscule Greek reconstruction layer for the unnumbered Greek reader section.
- Regenerated Ukrainian, English, and digital paper/digital sources and full PDF proofs.
- Removed obsolete first-proof generated artifacts from `output/` so the current `*-full` proofs are the only active proof outputs.
- Ran structural QA and PDF text checks.

## Verification Completed

- `tools/render_full_book_proofs.py` rendered 6 current artifacts.
- `tools/qa_crosscheck.py` passed: 114/114 cards, 114/114 appendix sections, 114/114 source/control sections, synchronized reader sets, and Ukrainian translation anchors.
- Ukrainian full PDF: 237 pages; blocked technical phrases not found.
- English full PDF: 294 pages; blocked technical phrases not found.
- Digital companion full PDF: 29 pages.
- Font sample: Times New Roman for Ukrainian/English/Greek text; Noto Sans Coptic only for Coptic-script text.

## Remaining Work

1. Final human copyedit signoff for the Ukrainian book.
2. Final human copyedit signoff for the English book.
3. Editorial decision on Logion 1 and the first words/title question.
4. Full production layout build in Typst or another professional print system.
5. Page-by-page visual QA after production layout.
6. Final source-rights and redistribution review.
7. Final checksums, manifest, git tag/release marker.

## Recommended Next Step

Make the final **Logion 1 / title / opening-words decision** before production typesetting. This is the one remaining editorial decision that affects the identity of the reconstructed text itself, not merely its formatting.
