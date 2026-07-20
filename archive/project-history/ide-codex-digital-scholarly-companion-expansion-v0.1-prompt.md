# IDE Codex Prompt: Digital Scholarly Companion Expansion v0.1

You are Codex working in `/Users/arseny/BOOKS/EUAGELIA`.

## Goal

Build the next publication-quality layer after the Ukrainian and English paper proofs: a full digital scholarly companion that preserves the research apparatus that paper readers cannot click through.

The paper books must remain clean and print-safe. The digital companion may and should contain repository paths, source paths, audit links, detailed evidence notes, control files, machine-readable tables, and reproducibility information.

## Context

Already completed:

- all 114 logion cards exist;
- all 114 cards have five-source original-language apparatus v0.1;
- clean reader is frozen at 37 units for this edition;
- Ukrainian full paper proof has passed page-level QA;
- English full paper proof has passed page-level QA;
- paper books are intended to be self-contained and should not depend on clickable links;
- digital companion is the place where the larger scholarly apparatus must be preserved.

## Tasks

1. Run baseline QA:

   ```bash
   python3 tools/qa_crosscheck.py
   ```

2. Inspect the current digital companion artifacts under:

   - `output/digital-scholarly-companion/`
   - `project/generator-ready-books-pass-v0.1.md`
   - `project/print-and-digital-publication-architecture.md`
   - `project/source-reproducibility-note.md`
   - `project/rights-and-citation-policy.md`
   - `bibliography/`
   - `corpus/logion-cards/`
   - `reconstruction/earliest-sayings-gospel/`
   - `controls/`
   - `sources/`

3. Design a clear digital companion structure with at least these layers:

   - landing/overview and how to use it;
   - clean-reader manifest;
   - all-114 logion index;
   - per-logion links to cards, appendix sections, evidence notes, control files, and source snapshots;
   - source witness inventory for Coptic, P.Oxy. 1, P.Oxy. 654, P.Oxy. 655, and canonical Greek controls;
   - bibliography and rights/register layer;
   - audit trail of major passes;
   - reproducibility checklist and QA commands.

4. Implement the companion source as generated or maintained project artifacts. Prefer deterministic scripts if the output is derived from existing files. Do not hand-copy large tables when a script can reliably generate them.

5. Generate a proof artifact for the digital companion. It may include internal paths and links; unlike the paper PDFs, those are desirable here.

6. Add or update a QA report documenting:

   - what the companion includes;
   - how all 114 logia are covered;
   - which links are local project links versus external/public references;
   - what remains unresolved before final publication.

7. Update project documentation:

   - `README.md`
   - `project/project-completion-roadmap.md`
   - `project/publication-remediation-plan-2026-07-18.md`
   - `project/open-task-prompt-queue-2026-07-18.md`
   - `project/project-map.md`
   - `project/repository-structure.md`

8. Run final QA:

   ```bash
   python3 tools/qa_crosscheck.py
   ```

## Quality Rules

- Do not change clean-reader membership unless a separate decision pass is explicitly opened.
- Do not remove paper-safe protections from Ukrainian or English books.
- Do not replace scholarly uncertainty with false certainty.
- Keep print-facing and digital-only apparatus clearly separated.
- Preserve commons/anti-ownership policy and third-party source-rights distinctions.
- Make the output useful for a serious reader who wants to audit the reconstruction logion by logion.

## Expected Output

- Expanded digital scholarly companion artifact(s).
- A digital-companion QA report.
- Updated documentation and task queue.
- A clear next-step recommendation after this pass.
