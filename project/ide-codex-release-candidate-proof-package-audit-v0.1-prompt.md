# IDE Codex Prompt: Release-Candidate Proof Package Audit v0.1

You are working in the EUAGELIA project.

## Objective

Perform the final release-candidate proof package audit for the Ukrainian and English paper books plus the digital scholarly companion.

Do not change the frozen 37-unit clean-reader corpus unless a verified numbering/text corruption is found. This task is about publication fitness, page-by-page visual QA, package completeness, and final blockers.

## Inputs

Read first:

- `project/final-proof-polish-bibliography-toc-v0.1.md`
- `project/bible-style-paper-layout-policy-v0.1.md`
- `project/print-and-digital-publication-architecture.md`
- `tools/render_first_proofs.py`
- `output/render-log-first-proofs-v0.1.md`
- `output/uk-paper-book/euagelia-uk-proof.pdf`
- `output/en-paper-book/euagelia-en-proof.pdf`
- `output/digital-scholarly-companion/euagelia-digital-companion-proof.pdf`
- `project/open-task-prompt-queue-2026-07-18.md`

## Tasks

1. Re-render all proof artifacts from current sources.
2. Generate PNG previews for every page of:
   - Ukrainian paper proof;
   - English paper proof;
   - digital scholarly companion proof.
3. Inspect every page visually and record:
   - overflow;
   - clipped text;
   - awkward page breaks;
   - unreadably dense tables;
   - wrong language leakage;
   - internal path or URL leakage in paper PDFs;
   - title/TOC/bibliography/index problems;
   - footer/header problems.
4. Run automated checks:
   - `python3 tools/qa_crosscheck.py`;
   - `git diff --check`;
   - extracted-text path-safety scan for paper PDFs;
   - page counts and checksums.
5. Decide whether the current ReportLab renderer is acceptable for the first public proof or whether the next step must be a stronger typesetting pipeline.
6. Create:
   - `project/release-candidate-proof-package-audit-v0.1.md`
   - update queue status.

## Quality Rules

- Do not claim publication readiness unless every page has been inspected.
- Do not hide defects. Separate `blocking`, `non-blocking polish`, and `future edition` issues.
- Keep paper books self-contained; no repo paths or URLs in paper PDFs.
- Preserve digital scholarly companion detail.
- If the renderer cannot produce acceptable print pages, recommend a typesetting migration instead of forcing a weak final PDF.

## Required Output

Report:

- artifacts checked;
- page-by-page QA summary;
- blockers;
- whether current PDFs are release candidates;
- exact next task.
