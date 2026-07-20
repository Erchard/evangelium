# IDE Codex Prompt: Final Proof Polish, Bibliography, And TOC v0.1

You are working in the EUAGELIA project.

## Objective

Polish the current Bible-style Ukrainian and English paper proofs toward publication-grade first editions without changing the frozen 37-unit clean-reader corpus.

The current papers now have Bible-style clean text and split paper indexes. The next task is to improve final proof usability: front matter, TOC, bibliography, index density, and page-by-page proof QA.

## Inputs

Read first:

- `project/bible-style-paper-layout-policy-v0.1.md`
- `project/bible-style-book-design-index-pass-v0.1.md`
- `tools/render_first_proofs.py`
- `bibliography/bibliography-working.md`
- `bibliography/source-rights-register.md`
- `output/uk-paper-book/book-source-uk.md`
- `output/en-paper-book/book-source-en.md`
- `output/uk-paper-book/euagelia-uk-proof.pdf`
- `output/en-paper-book/euagelia-en-proof.pdf`
- `project/open-task-prompt-queue-2026-07-18.md`

## Tasks

1. Improve front matter:
   - title page;
   - publication note;
   - commons / rights notice;
   - short reader orientation.

2. Improve TOC:
   - generate or stabilize TOC entries;
   - if exact page numbers are not safe yet, use a proof-stable TOC without fake precision.

3. Improve bibliography section:
   - convert current working bibliography groups into a compact print-facing bibliography summary;
   - keep detailed rights/source status in digital companion;
   - preserve protected-source caution.

4. Improve indexes:
   - compress long number lists where safe;
   - reduce density of non-included-logia index;
   - keep witness/status/logion indexes print-safe.

5. Re-render proofs and validate:
   - `python3 tools/qa_crosscheck.py`;
   - `git diff --check`;
   - paper PDF extracted text contains no internal repository paths or URLs;
   - render PNG previews for all pages or a representative full-page set;
   - record page counts and checksums.

6. Create report:
   - `project/final-proof-polish-bibliography-toc-v0.1.md`

## Quality Rules

- Do not change the 37-unit clean-reader corpus.
- Do not add repository paths, source paths, or web URLs to paper PDFs.
- Do not remove technical source detail from the digital companion.
- Do not claim final publication readiness if visual proof issues remain.
- Keep renderer changes understandable and repeatable.

## Required Output

Create or update:

- `project/final-proof-polish-bibliography-toc-v0.1.md`
- `tools/render_first_proofs.py`
- regenerated proof artifacts if changes are made;
- queue status.

Then report:

- improvements made;
- validation results;
- remaining blockers before final print release;
- next logical task.
