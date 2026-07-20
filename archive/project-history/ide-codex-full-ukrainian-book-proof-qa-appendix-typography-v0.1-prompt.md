# IDE Codex Prompt: Full Ukrainian Book Proof QA And Appendix Typography v0.1

You are working in the EUAGELIA project.

## Objective

Perform the first full page-by-page QA of the 118-page Ukrainian full book proof and improve appendix typography where defects can be fixed without changing the frozen clean-reader corpus.

The Ukrainian full book proof now exists for the first time. The next task is to determine whether it is merely structurally complete or visually usable as a serious paper-book proof.

## Inputs

Read first:

- `project/full-book-assembly-typesetting-pipeline-v0.1.md`
- `tools/assemble_full_book_sources.py`
- `tools/render_full_book_proofs.py`
- `output/uk-paper-book/book-source-uk-full.md`
- `output/uk-paper-book/euagelia-uk-full-proof.pdf`
- `output/render-log-full-book-proofs-v0.1.md`
- `project/open-task-prompt-queue-2026-07-18.md`

## Tasks

1. Re-run full source assembly and full proof rendering.
2. Generate PNG previews for all pages of `output/uk-paper-book/euagelia-uk-full-proof.pdf`.
3. Inspect all pages and record:
   - clipping or overflow;
   - orphan headings;
   - blank or nearly blank pages;
   - unreadable table/list formatting;
   - awkward clean-text or appendix transitions;
   - footer/header problems;
   - Ukrainian language glitches introduced by paper sanitization.
4. Fix renderer or assembly issues that are mechanical and safe:
   - heading/page-break rules;
   - orphaned punctuation after removed source paths;
   - blockquote indentation;
   - list spacing;
   - appendix section flow.
5. Do not rewrite scholarly content in this pass except to remove mechanical paper-output artifacts.
6. Run:
   - `python3 tools/qa_crosscheck.py`;
   - `git diff --check`;
   - paper path-safety extraction scan.
7. Create:
   - `project/full-ukrainian-book-proof-qa-appendix-typography-v0.1.md`
   - update queue and active documentation.

## Quality Rules

- The clean reader must remain unchanged.
- The first substantial reader-facing content must remain the clean reconstructed text.
- Do not hide excluded or deferred logia from the appendix.
- Do not add repository paths or URLs to paper PDFs.
- Do not call the Ukrainian book release-ready unless all 118 pages are inspected after the final render.

## Required Output

Report:

- page-by-page QA summary;
- typography fixes made;
- remaining blockers;
- whether ReportLab remains acceptable for the next proof;
- next logical task, especially the English full appendix generation plan.
