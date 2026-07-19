# IDE Codex Prompt: Final Production Typesetting And Copyedit Gate v0.1

You are Codex working in `/Users/arseny/BOOKS/EUAGELIA`.

## Goal

Move the project from proof-complete artifacts toward final publication readiness. The corpus, paper books, and digital companion now exist. The next task is to decide the final production path and perform a disciplined final copyedit/proof gate across the Ukrainian paper book, English paper book, and digital companion.

## Context

Completed:

- frozen 37-unit clean reader;
- all 114 cards and appendix sections;
- Ukrainian full paper proof after page-level QA;
- English full paper proof after page-level QA;
- expanded digital scholarly companion with Markdown/TSV/PDF artifacts;
- browsable static HTML companion with 114 logion panels and valid local links.

Remaining risk:

- ReportLab proofs are acceptable proof artifacts but may not be final production typography;
- Ukrainian and English books still need final human-level copyedit;
- digital companion needs final public-release polish and rights/source snapshot check.

## Tasks

1. Run baseline QA:

   ```bash
   python3 tools/qa_crosscheck.py
   ```

2. Inspect current generated outputs:

   - `output/uk-paper-book/euagelia-uk-full-proof.pdf`
   - `output/en-paper-book/euagelia-en-full-proof.pdf`
   - `output/digital-scholarly-companion/euagelia-digital-companion-full-proof.pdf`
   - `output/digital-scholarly-companion/html/index.html`

3. Decide and document the final production path:

   - keep ReportLab for final PDFs;
   - move final books to Typst;
   - move final books to LaTeX;
   - or keep ReportLab as proof-only and define a separate manual/professional typesetting handoff.

4. Create a final copyedit/proof checklist covering:

   - Ukrainian clean reader;
   - Ukrainian appendix;
   - English clean reader;
   - English appendix;
   - evidence dossier;
   - bibliography and rights notes;
   - digital companion HTML;
   - consistency of logion numbering and included/excluded decisions.

5. Perform the highest-value safe fixes discovered during the inspection. Do not change clean-reader membership or scholarly decisions without opening a separate decision pass.

6. Update documentation:

   - `README.md`
   - `project/project-completion-roadmap.md`
   - `project/publication-remediation-plan-2026-07-18.md`
   - `project/open-task-prompt-queue-2026-07-18.md`
   - `project/project-map.md`
   - `project/repository-structure.md`
   - `project/final-product-specification.md`

7. Save a completion report, for example:

   - `project/final-production-typesetting-copyedit-gate-v0.1.md`

8. Run final QA:

   ```bash
   python3 tools/qa_crosscheck.py
   ```

## Quality Rules

- Preserve the clean-reader-first principle.
- Preserve all 114 appendix coverage.
- Preserve uncertainty and source-status distinctions.
- Keep paper books print-safe.
- Keep digital companion source-rich and audit-friendly.
- Do not claim the edition is final unless production typography and human copyedit are actually complete.

## Expected Output

- documented production path decision;
- final copyedit/proof checklist;
- safe corrections if any are found;
- updated roadmap and queue;
- next-step recommendation toward release candidate status.
