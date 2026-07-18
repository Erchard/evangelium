# IDE Codex Prompt: Print and Digital Publication Architecture v0.1

## Goal

Design and document the publication architecture for the EUAGELIA project so that the same scholarly corpus can generate:

1. a Ukrainian paper book;
2. an English paper book;
3. a larger digital scholarly apparatus.

The key constraint is that paper readers cannot click hyperlinks, while digital researchers must not lose the fuller apparatus, file-level evidence, source notes, and reproducibility trail.

## Context

The project reconstructs the earliest recoverable sayings gospel preserved mainly in the Gospel of Thomas tradition.

The final reader model already has two layers:

- clean reconstructed text first;
- commentary / appendix / evidence apparatus after the clean text.

The project now needs an explicit publication architecture that distinguishes print-safe book content from digital-only scholarly material.

## Required Document

Create:

- `project/print-and-digital-publication-architecture.md`

The document must define:

1. The final output families.
2. The structure of the Ukrainian print book.
3. The structure of the English print book.
4. The structure of the digital scholarly companion.
5. Print-safe citation and cross-reference rules.
6. Digital apparatus rules.
7. Which files are canonical sources of truth.
8. Which repository paths must never appear as the only reference in print.
9. How future appendix/commentary passes should be written so they can be used for print and digital outputs.
10. A practical generation pipeline for future automation.

## Required Decisions

The architecture must explicitly state:

- Paper books must be self-contained.
- Internal repository paths are allowed in digital apparatus, but not as reader-facing references in print.
- Print references should use logion numbers, witness labels, canonical abbreviations, short bibliography keys, and printed indexes.
- Hyperlinks may exist in digital outputs, but every important link must have a print-safe equivalent.
- The Ukrainian and English paper books should be separate books, not a bilingual cluttered volume.
- The full scholarly evidence apparatus should remain digital-first.
- The clean reconstructed text must remain free of commentary and technical markers.

## Update Existing Docs

Update at least:

- `README.md`
- `project/project-map.md`
- `project/project-completion-roadmap.md`
- `project/final-product-specification.md`
- `project/clean-text-plus-commentary-concept.md`
- `reconstruction/earliest-sayings-gospel/README.md`

These updates should be concise and should not duplicate the full architecture document.

## Acceptance Checks

After editing, verify:

- the new architecture file exists;
- project map references it;
- README mentions separate Ukrainian and English paper books plus digital scholarly apparatus;
- future appendix/editorial work is instructed to use print-safe references;
- `git diff --check` passes.

## Output Summary

Report:

- the new file created;
- the main architectural decision;
- which documents were updated;
- the next logical project step after this architecture pass.
