# IDE Codex Prompt: Typst Production Pilot v0.1

You are Codex working in `/Users/arseny/BOOKS/EUAGELIA`.

## Goal

Create the first production-typesetting pilot for EUAGELIA. The final production gate chose Typst/professional handoff as the preferred path and kept ReportLab as proof-only. This task should test whether the project can produce a cleaner final book layout from the existing generated sources.

## Inputs

- `project/final-production-typesetting-copyedit-gate-v0.1.md`
- `output/uk-paper-book/book-source-uk-full.md`
- `output/en-paper-book/book-source-en-full.md`
- `output/digital-scholarly-companion/companion-source-full.md`
- `output/digital-scholarly-companion/logion-cross-reference-index.tsv`
- `project/bible-style-paper-layout-policy-v0.1.md`
- `project/print-and-digital-publication-architecture.md`

## Tasks

1. Run baseline QA:

   ```bash
   python3 tools/qa_crosscheck.py
   ```

2. Check whether Typst is available locally:

   ```bash
   typst --version
   ```

3. If Typst is available, create a deterministic pilot under `output/production-typst/`:

   - `euagelia-template.typ`
   - `uk-pilot.typ`
   - `en-pilot.typ`
   - compiled pilot PDFs if possible.

4. If Typst is not available, still create a source/handoff package under `output/production-typst/`:

   - Typst-ready source skeletons;
   - a compile README;
   - a handoff checklist for a human/professional typesetter.

5. The pilot should prove the final design direction, not typeset all 177 pages immediately. Include:

   - title/front matter;
   - clean-reader first section;
   - one included logion appendix section;
   - one excluded or appendix-only logion section, preferably Logion 114;
   - bibliography/source-key sample.

6. Preserve rules:

   - clean text first;
   - paper books print-safe;
   - no internal repo paths in paper PDFs;
   - digital companion remains source-rich;
   - no clean-reader membership changes.

7. Save a QA report:

   - `project/typst-production-pilot-v0.1.md`

8. Update documentation and the task queue:

   - `README.md`
   - `project/project-completion-roadmap.md`
   - `project/publication-remediation-plan-2026-07-18.md`
   - `project/open-task-prompt-queue-2026-07-18.md`
   - `project/project-map.md`
   - `project/repository-structure.md`

9. Run final QA:

   ```bash
   python3 tools/qa_crosscheck.py
   ```

## Expected Output

- Typst pilot or Typst-ready handoff package.
- Clear decision on whether Typst is viable in the current environment.
- Updated release-candidate blocker list.
- Next-step recommendation.
