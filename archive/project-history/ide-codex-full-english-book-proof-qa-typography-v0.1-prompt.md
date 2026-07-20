# IDE Codex Prompt: Full English Book Proof QA And Typography v0.1

You are working in the EUAGELIA project.

## Objective

Perform a full page-level proof QA of the 177-page English full paper book after the English appendix editorial-quality pass.

This is a proofing and typography task. Do not change the frozen clean reader, all-114 publication decisions, or reconstruction membership unless a separate explicit decision pass requires it.

## Required Inputs

Read:

- `project/english-appendix-editorial-quality-pass-v0.1.md`
- `project/english-full-114-logion-appendix-generation-v0.1.md`
- `project/full-ukrainian-book-proof-qa-appendix-typography-v0.1.md`
- `output/en-paper-book/book-source-en-full.md`
- `output/en-paper-book/euagelia-en-full-proof.pdf`
- `tools/assemble_full_book_sources.py`
- `tools/render_full_book_proofs.py`
- `tools/qa_crosscheck.py`

## Work Plan

1. Run `python3 tools/qa_crosscheck.py`.
2. Rebuild the English full source and proof from current sources.
3. Render every English proof page to PNG previews.
4. Create contact sheets for all pages.
5. Inspect every contact sheet for:
   - blank or near-blank unintended pages;
   - clipping or overflow;
   - headings orphaned alone at page bottoms;
   - text colliding with footers;
   - excessive section-opener pages;
   - paper-facing technical labels or raw draft markers.
6. Run PDF extracted-text checks for:
   - internal repository paths;
   - obsolete appendix-absent language;
   - editor-instruction leakage;
   - Ukrainian status words in English paper output;
   - `Status:` / `draft` leakage.
7. Apply safe typography or sanitizer fixes only if they do not alter scholarly decisions.
8. Regenerate the proof after fixes.
9. Save a page-scan TSV and an execution report:
   - `project/full-english-book-proof-qa-typography-v0.1.md`
10. Update README, project map, roadmap, remediation plan, and open-task queue.

## Acceptance Criteria

- English full proof renders successfully.
- English full proof has a documented page count.
- All pages are visually checked through contact sheets.
- QA crosscheck passes.
- Paper-facing English PDF has no repo paths, obsolete appendix-absent language, editor instructions, Ukrainian status words, `Status:`, or `draft` leakage.
- Remaining blockers and next step are clearly documented.
