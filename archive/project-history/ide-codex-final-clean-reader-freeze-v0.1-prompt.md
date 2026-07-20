# IDE Codex Prompt: Final Clean-Reader Freeze v0.1

You are Codex working in `/Users/arseny/BOOKS/EUAGELIA`.

## Objective

Perform the final clean-reader freeze pass before book generation. The goal is to confirm that the reconstructed clean reader is internally consistent, publication-safe, and ready to become the source text for Ukrainian and English print books plus the digital scholarly companion.

## Core Principle

Do not expand or reduce the clean reader unless you find a documented contradiction that makes the current 37-unit corpus unsafe. This is a freeze pass, not a new creative selection pass.

## Required Inputs

Read and cross-check:

- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-uk.md`
- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-en.md`
- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-coptic.md`
- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-greek.md`
- `reconstruction/earliest-sayings-gospel/parallel-edition.md`
- `reconstruction/earliest-sayings-gospel/inclusion-decisions-table.md`
- `reconstruction/earliest-sayings-gospel/all-114-publication-decision-table-v0.1.md`
- `reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-uk.md`
- `reconstruction/earliest-sayings-gospel/evidence-dossier-en.md`
- `reconstruction/earliest-sayings-gospel/greek-retroversion-confidence-audit-v0.1.md`
- `project/probability-vs-reader-decision-audit-2026-07-18.md`
- `project/open-task-prompt-queue-2026-07-18.md`

## Tasks

1. Confirm the clean reader contains exactly these 37 logia or marked cores:
   `1, 2, 3, 4, 5, 6, 9, 10, 16, 20, 22, 25, 26, 31, 32, 33, 34, 35, 36, 39, 41, 45A, 46A, 47B, 54, 63, 72, 73, 86, 89, 91A, 95, 96, 99, 100, 103A, 107`.
2. Check that Ukrainian, English, Coptic, Greek, and parallel layers all represent the same units in the same order.
3. Check that clean-reader files remain clean: numbered logia only, without commentary, probability labels, bracketed editorial explanations, or internal repo links.
4. Check that every included or excluded/deferred logion has a corresponding appendix pathway for the reader.
5. Check probability-vs-reader tensions: no high-late or late-composite unit should appear in the clean reader without a documented marker/frame/core rationale; no high-early unit should remain outside without a documented exclusion/defer rationale.
6. Check Greek-status consistency one more time: no hypothetical Greek retroversion should read as an extant manuscript witness.
7. Write a freeze report at `reconstruction/earliest-sayings-gospel/final-clean-reader-freeze-v0.1.md`.
8. If small documentation updates are necessary, update README/roadmap/queue files. Do not perform book generation in this pass.

## Required Output

Create `reconstruction/earliest-sayings-gospel/final-clean-reader-freeze-v0.1.md` with:

- final clean-reader unit list;
- any discrepancies found and fixed;
- any discrepancies found but deferred;
- publication readiness verdict;
- next recommended step.

Update `project/open-task-prompt-queue-2026-07-18.md` so this task becomes `DONE` after execution and the next task becomes generator-ready Ukrainian/English book production.

## Validation

Run:

```bash
python3 tools/qa_crosscheck.py
python3 tools/probability_reader_audit.py
git diff --check
```

If a validation command fails, fix the cause if feasible and re-run it. If it cannot be fixed safely in this pass, document the blocker clearly in the freeze report.
