# IDE Codex Prompt: Final Bibliography And Rights Verify v0.1

You are Codex working in `/Users/arseny/BOOKS/EUAGELIA`.

## Objective

Close the remaining bibliography `VERIFY` items and source-rights uncertainties before final rendering or public release.

## Required Inputs

Read:

- `bibliography/bibliography-working.md`
- `bibliography/source-rights-register.md`
- `project/rights-and-citation-policy.md`
- `project/source-reproducibility-note.md`
- `project/generator-ready-books-pass-v0.1.md`
- `output/uk-paper-book/book-source-uk.md`
- `output/en-paper-book/book-source-en.md`
- `output/digital-scholarly-companion/companion-manifest.md`

## Tasks

1. Count all remaining `VERIFY`, `UNRESOLVED`, and rights-sensitive markers.
2. For each bibliography item, decide whether it can be verified from local project context or needs external/library/physical-edition checking.
3. Update bibliography entries that can be safely completed from local data.
4. Preserve unresolved items honestly; do not invent publication data.
5. Update the source-rights register with clear release rules for paper books and digital companion.
6. Create a report at `project/final-bibliography-rights-verify-v0.1.md`.
7. Update the open-task queue with the next task: print/digital proof QA and rendering preparation.

## Validation

Run:

```bash
python3 tools/qa_crosscheck.py
git diff --check
```

Also report the final counts of remaining `VERIFY`, `UNRESOLVED`, and protected-source restrictions.
