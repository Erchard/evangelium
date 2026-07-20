# IDE Codex Prompt: Bible-Style Book Design And Index Pass v0.1

You are working in the EUAGELIA project.

## Objective

Improve the Ukrainian and English paper-book proofs so they look less like technical exports and more like familiar mass Bible editions, while preserving the digital scholarly companion for the full technical apparatus.

The clean reader must remain frozen at 37 units.

## Inputs

Read first:

- `project/bible-style-paper-layout-policy-v0.1.md`
- `project/first-proof-qa-layout-corrections-v0.1.md`
- `tools/render_first_proofs.py`
- `output/uk-paper-book/book-source-uk.md`
- `output/en-paper-book/book-source-en.md`
- `output/uk-paper-book/euagelia-uk-proof.pdf`
- `output/en-paper-book/euagelia-en-proof.pdf`
- `bibliography/bibliography-working.md`
- `project/open-task-prompt-queue-2026-07-18.md`

## Tasks

1. Improve Bible-style paper layout:
   - refine margins;
   - refine font sizes;
   - preserve compact two-column clean text;
   - keep logion numbers inline;
   - avoid oversized headings in the clean reader.

2. Improve front matter:
   - title page;
   - commons / rights notice;
   - short publication note;
   - table of contents or stable TOC placeholder.

3. Replace the raw all-114 table in paper proofs:
   - create print-friendly split indexes or compact reference sections;
   - preserve full technical tables in the digital companion;
   - keep paper indexes readable without repository paths.

4. Add first paper indexes if feasible:
   - logion index;
   - witness index;
   - canonical parallels index;
   - inclusion-status index.

5. Re-render proofs and validate:
   - `python3 tools/qa_crosscheck.py`;
   - `git diff --check`;
   - paper PDF extracted text contains no internal repository paths or URLs;
   - PNG previews show no obvious blank pages, clipping, broken glyphs, or unreadable tables.

6. Create report:
   - `project/bible-style-book-design-index-pass-v0.1.md`

## Quality Rules

- Do not change the clean-reader corpus.
- Do not add technical paths to paper PDFs.
- Do not remove technical paths from the digital companion.
- Do not over-design; keep the pipeline repeatable and understandable.
- Record known defects honestly.

## Required Output

Create or update:

- `project/bible-style-book-design-index-pass-v0.1.md`
- `tools/render_first_proofs.py`
- regenerated proof artifacts if changes are made;
- queue status.

Then report:

- what design improvements were made;
- what remains before final print design;
- the next logical task.
