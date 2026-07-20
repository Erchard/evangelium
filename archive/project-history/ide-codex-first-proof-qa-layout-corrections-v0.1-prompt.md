# IDE Codex Prompt: First Proof QA And Layout Corrections v0.1

You are working in the EUAGELIA project.

## Objective

Perform the first real proof QA pass on the generated Ukrainian and English paper-book proofs and the digital companion proof.

The project now has a minimal renderer and first proof artifacts. The next task is to improve proof quality without changing the frozen 37-unit clean-reader corpus.

## Inputs

Read first:

- `project/render-pipeline-first-proofs-v0.1.md`
- `tools/render_first_proofs.py`
- `output/render-log-first-proofs-v0.1.md`
- `output/uk-paper-book/book-source-uk.md`
- `output/en-paper-book/book-source-en.md`
- `output/uk-paper-book/euagelia-uk-proof.pdf`
- `output/en-paper-book/euagelia-en-proof.pdf`
- `output/digital-scholarly-companion/euagelia-digital-companion-proof.pdf`
- `project/open-task-prompt-queue-2026-07-18.md`

## Tasks

1. Render PNG previews of representative pages:
   - title / first page;
   - clean-text opening;
   - all-114 table section;
   - bibliography / rights section;
   - digital companion first page.

2. Inspect the previews for:
   - blank pages;
   - broken glyphs;
   - clipped text;
   - overcrowded tables;
   - poor heading hierarchy;
   - paper PDFs exposing repository paths or URLs.

3. Implement the smallest high-value layout improvements:
   - remove technical proof text from paper-facing pages if any remains;
   - add simple title page / commons notice / table of contents placeholders;
   - split or compact large all-114 tables if feasible;
   - improve renderer spacing and heading hierarchy;
   - preserve digital paths in the digital companion only.

4. Re-render proofs.

5. Validate:
   - `python3 tools/qa_crosscheck.py`;
   - `git diff --check`;
   - paper PDF text extraction contains no internal repository paths or URLs;
   - page counts and checksums are recorded.

6. Create a report:
   - `project/first-proof-qa-layout-corrections-v0.1.md`

## Quality Rules

- Do not change the frozen 37-unit clean-reader corpus.
- Do not add digital-only paths to Ukrainian or English paper proof text.
- Do not remove digital-only paths from the digital companion.
- Do not chase final book design perfection yet; prioritize visible proof defects and repeatability.
- Keep renderer changes small and understandable.

## Required Output

Create or update:

- `project/first-proof-qa-layout-corrections-v0.1.md`
- generated proof artifacts, if re-rendered;
- queue status.

Then report:

- what visual defects were found;
- what was fixed;
- what remains for final book design;
- the next logical task.
