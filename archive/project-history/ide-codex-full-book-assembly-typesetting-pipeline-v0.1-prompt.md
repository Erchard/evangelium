# IDE Codex Prompt: Full Book Assembly And Typesetting Pipeline v0.1

You are working in the EUAGELIA project.

## Objective

Close the largest remaining publication blocker: the current paper PDFs are proof skeletons, not complete books. Build the next-generation full book assembly pipeline for Ukrainian and English outputs while preserving the digital scholarly companion.

Do not change the frozen 37-unit clean-reader corpus unless a verified numbering/text corruption is discovered.

## Inputs

Read first:

- `project/release-candidate-proof-package-audit-v0.1.md`
- `project/print-and-digital-publication-architecture.md`
- `project/clean-text-plus-commentary-concept.md`
- `project/clean-reader-text-first-page-principle.md`
- `project/final-product-specification.md`
- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-uk.md`
- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-en.md`
- `reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-uk.md`
- `reconstruction/earliest-sayings-gospel/evidence-dossier-en.md`
- `output/uk-paper-book/book-source-uk.md`
- `output/en-paper-book/book-source-en.md`
- `tools/render_first_proofs.py`
- `project/open-task-prompt-queue-2026-07-18.md`

## Tasks

1. Decide the best immediate production strategy:
   - keep and extend ReportLab;
   - or create a cleaner structured Markdown/Typst/LaTeX pipeline for full-length books.
2. Assemble a complete Ukrainian paper-book source that includes:
   - title/front matter;
   - clean reconstructed text as the first reader-facing text;
   - reader orientation;
   - full 114-logion commentary appendix;
   - print-safe source keys;
   - bibliography;
   - indexes.
3. Define the English paper-book strategy:
   - if a full English appendix exists or can be safely generated from existing structured material, assemble it;
   - otherwise create an honest English proof package with clean text, method/evidence dossier, source keys, and indexes, and record that full English appendix generation remains a blocker.
4. Preserve the digital scholarly companion as the place for:
   - repository paths;
   - source files;
   - full card apparatus;
   - evidence notes;
   - machine-readable tables;
   - cross-reference index.
5. Render new full-book proofs or, if a renderer migration is required, create the new source/package scaffold and document exact next render command.
6. Run:
   - `python3 tools/qa_crosscheck.py`;
   - `git diff --check`;
   - paper path-safety extraction checks.
7. Create:
   - `project/full-book-assembly-typesetting-pipeline-v0.1.md`
   - update the open-task queue and active documentation.

## Quality Rules

- The first reader-facing pages must remain clean text only: numbered logia, no comments or disclaimers.
- Paper books must be self-contained and not depend on clickable links.
- Do not dump raw card files into paper books. Convert appendix material into readable book chapters.
- Do not hide excluded logia; all 114 must remain available in the appendix or companion with reasons for inclusion/non-inclusion.
- If English full appendix generation is not publication-safe in one pass, document it as a blocker instead of faking completion.
- Do not call the result release-ready until full-length PDFs are rendered and page-by-page QA is complete.

## Required Output

Report:

- pipeline decision;
- assembled/updated sources;
- rendered artifacts or exact blocker;
- QA results;
- remaining blockers;
- next logical task.
