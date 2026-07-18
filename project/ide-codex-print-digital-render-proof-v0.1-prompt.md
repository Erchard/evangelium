# IDE Codex Prompt: Print / Digital Render Proof Preparation v0.1

You are working in the EUAGELIA project.

## Objective

Prepare the project for generating two print books and one digital scholarly companion from the current controlled corpus.

The user wants:

- a Ukrainian paper book;
- an English paper book;
- a richer digital scholarly companion that preserves full source paths, URLs, snapshots, card history, apparatus, and audit trail.

Paper readers cannot click hyperlinks. The paper books must therefore be self-contained through logion numbers, witness labels, short bibliography keys, indexes, and print-safe notes. The digital companion may preserve detailed repository paths and links.

## Inputs

Read first:

- `output/uk-paper-book/book-source-uk.md`
- `output/en-paper-book/book-source-en.md`
- `output/digital-scholarly-companion/companion-manifest.md`
- `bibliography/bibliography-working.md`
- `bibliography/source-rights-register.md`
- `project/print-and-digital-publication-architecture.md`
- `project/final-bibliography-rights-verify-v0.1.md`
- `project/open-task-prompt-queue-2026-07-18.md`

## Tasks

1. Run preflight QA:
   - `python3 tools/qa_crosscheck.py`
   - `git diff --check`
   - a grep check proving that Ukrainian and English paper-book sources do not contain internal repository paths or clickable web URLs.

2. Create a print-safe citation key table for both paper books:
   - every key must resolve to `bibliography/bibliography-working.md`;
   - paper-facing entries should use witness labels and author/title keys, not repository paths;
   - protected sources must be clearly marked as control-only in the bibliography, not in the clean text.

3. Create a render-readiness report:
   - record the frozen 37-unit clean-reader corpus;
   - record source-layer separation between paper and digital companion;
   - list remaining blockers before final PDF generation;
   - list recommended rendering order for Ukrainian book, English book, then digital companion.

4. If safe and scoped, create skeleton render scripts or make targets only if the repository already has a rendering pattern. If no rendering pattern exists, do not invent a large toolchain; document the required renderer interface instead.

5. Update documentation:
   - mark final bibliography and rights verify as done in the queue;
   - add this task as current `NEXT` or mark it done if completed;
   - update README/project-map/roadmap status language from bibliography verification to render proof preparation.

## Quality Rules

- Do not change the clean-reader corpus unless QA discovers a real mismatch.
- Do not add digital-only paths to paper books.
- Do not remove source detail from the digital companion.
- Do not reproduce protected modern edition text.
- Keep Ukrainian and English book structures parallel.
- Preserve all logion numbering from the standard Gospel of Thomas numbering.

## Required Output

Create:

- `project/print-digital-render-proof-prep-v0.1.md`

Then report:

- QA command results;
- whether paper sources are print-safe;
- remaining blockers;
- the next logical task after render-proof preparation.
