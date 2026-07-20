# IDE Codex Prompt: English Full 114-Logion Appendix Generation v0.1

You are working in the EUAGELIA project.

## Objective

Create the first complete English 114-logion commentary appendix for the English paper book, matching the structure and scholarly honesty of the Ukrainian full appendix while keeping the English book self-contained for paper readers.

The English paper book must eventually mirror the Ukrainian book architecture:

1. clean reconstructed text first;
2. a short reader-orientation page;
3. a full commentary appendix covering all 114 logia, including included, marked, uncertain, deferred, appendix-only, and excluded logia;
4. print-safe bibliography and source keys.

## Required Inputs

Read and use:

- `reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-uk.md`
- `corpus/cards/`
- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-en.md`
- `reconstruction/earliest-sayings-gospel/evidence-dossier-en.md`
- `reconstruction/earliest-sayings-gospel/all-114-publication-decision-table-v0.1.md`
- `project/print-and-digital-publication-architecture.md`
- `project/full-ukrainian-book-proof-qa-appendix-typography-v0.1.md`
- `tools/qa_crosscheck.py`
- `tools/assemble_full_book_sources.py`
- `tools/render_full_book_proofs.py`

## Work Plan

1. Run `python3 tools/qa_crosscheck.py` before edits.
2. Create `reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-en.md`.
3. Use the Ukrainian appendix as the structural model, but do not do a flat machine-like translation. Produce readable English prose for ordinary readers, with enough scholarly specificity for serious evaluation.
4. Preserve conventional Gospel of Thomas logion numbering for all 114 logia.
5. For every logion, include:
   - reconstruction status;
   - source witnesses and controls;
   - clean text or appendix-only reason;
   - possible interpretations in plain English;
   - why the logion is included, marked, uncertain, deferred, or excluded.
6. Keep paper-facing prose print-safe:
   - use logion numbers, witness labels, canonical references, and bibliography keys;
   - do not rely on clickable links;
   - do not expose repository paths in the paper-facing English appendix.
7. Update `tools/assemble_full_book_sources.py` so the English full paper source uses the new English appendix instead of only the evidence dossier. Preserve the digital companion as the place for repo paths and the fuller research apparatus.
8. Regenerate:
   - `output/en-paper-book/book-source-en-full.md`
   - `output/en-paper-book/euagelia-en-full-proof.pdf`
   - `output/render-log-full-book-proofs-v0.1.md`
9. Run structural QA again:
   - `python3 tools/qa_crosscheck.py`
10. Run paper-safety checks against the English full paper source/PDF extracted text for internal repository paths and raw unresolved markers.
11. Create an execution report:
   - `project/english-full-114-logion-appendix-generation-v0.1.md`
12. Update:
   - `README.md`
   - `project/project-map.md`
   - `project/project-completion-roadmap.md`
   - `project/publication-remediation-plan-2026-07-18.md`
   - `project/open-task-prompt-queue-2026-07-18.md`

## Quality Rules

- Do not change the frozen clean reader unless a separate explicit decision pass requires it.
- Do not invent extant Greek where only a hypothetical retroversion exists.
- Do not hide rejected logia; rejected and appendix-only logia must receive the same reader-friendly explanatory care as included logia.
- Do not copy protected modern translations as the English base text.
- If a section cannot yet be finished at publication quality, mark the limitation clearly in the execution report and keep the paper-facing text honest.

## Acceptance Criteria

- `full-logion-commentary-appendix-en.md` exists and covers Logia 1-114.
- English full paper source no longer says that the full English 114-logion appendix is absent.
- English full proof renders successfully.
- QA crosscheck passes.
- Paper-facing English output is free of internal repository paths and unresolved technical markers.
- Documentation and the open-task queue identify the next true blocker after this pass.
