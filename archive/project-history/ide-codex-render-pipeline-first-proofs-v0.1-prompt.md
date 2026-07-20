# IDE Codex Prompt: Render Pipeline And First Proofs v0.1

You are working in the EUAGELIA project.

## Objective

Create the first renderable proof artifacts for:

- the Ukrainian paper book;
- the English paper book;
- the digital scholarly companion manifest/index.

Use the already prepared source packages and keep the paper/digital separation intact.

## Inputs

Read first:

- `project/print-digital-render-proof-prep-v0.1.md`
- `output/uk-paper-book/book-source-uk.md`
- `output/en-paper-book/book-source-en.md`
- `output/digital-scholarly-companion/companion-manifest.md`
- `bibliography/bibliography-working.md`
- `bibliography/source-rights-register.md`
- `project/open-task-prompt-queue-2026-07-18.md`

## Tasks

1. Inspect local rendering capabilities:
   - check for `pandoc`, `typst`, `wkhtmltopdf`, LaTeX, Python PDF libraries, or other available tools;
   - do not assume an external renderer exists without checking.

2. Choose the simplest reliable first-proof path:
   - prefer a tool that supports Ukrainian, Greek, Coptic, page numbers, table of contents, and wide Markdown tables;
   - if full PDF generation is not safe in one pass, create HTML proofs first and document why.

3. Create a minimal repeatable render script or Makefile target:
   - Ukrainian proof from `output/uk-paper-book/book-source-uk.md`;
   - English proof from `output/en-paper-book/book-source-en.md`;
   - digital companion proof from `output/digital-scholarly-companion/companion-manifest.md`;
   - write outputs into the same output family folders.

4. Generate first proof artifacts if possible.

5. Validate:
   - run `python3 tools/qa_crosscheck.py`;
   - run `git diff --check`;
   - verify paper inputs still contain no internal repository paths or clickable URLs;
   - if PDFs/HTML files are generated, inspect file existence, size, and basic text extraction if tooling allows.

6. Create a proof-generation report:
   - rendering tool chosen;
   - commands used;
   - artifacts generated;
   - known layout risks;
   - next proof-QA corrections.

## Quality Rules

- Do not change the 37-unit clean-reader corpus.
- Do not add digital-only paths or links to paper-book sources.
- Do not remove paths or links from the digital companion.
- Do not reproduce protected modern edition text.
- Keep scripts small, transparent, and repeatable.
- If no reliable renderer is available, document the blocker and create the smallest useful scaffold rather than faking generated outputs.

## Required Output

Create:

- `project/render-pipeline-first-proofs-v0.1.md`

Possible generated artifacts:

- `output/uk-paper-book/euagelia-uk-proof.*`
- `output/en-paper-book/euagelia-en-proof.*`
- `output/digital-scholarly-companion/euagelia-digital-companion-proof.*`

Then update the queue and report the next logical task.
