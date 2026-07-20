# IDE Codex Prompt: Generator-Ready Ukrainian And English Books v0.1

You are Codex working in `/Users/arseny/BOOKS/EUAGELIA`.

## Objective

Create the first generator-ready source packages for the Ukrainian and English paper books, plus a matching digital scholarly companion plan, using the frozen 37-unit clean reader and the full 114-logion appendix.

## Required Principle

Paper books must be self-contained. Do not rely on clickable repository links in paper-facing prose. Convert internal references into print-safe references: logion numbers, witness labels, canonical references, bibliography keys, appendix section numbers, and indexes.

The digital scholarly companion should preserve the fuller research apparatus, including repository paths, evidence notes, source snapshots, audit trail, and machine-checkable links.

## Required Inputs

Read:

- `reconstruction/earliest-sayings-gospel/final-clean-reader-freeze-v0.1.md`
- `project/print-and-digital-publication-architecture.md`
- `project/final-product-specification.md`
- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-uk.md`
- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-en.md`
- `reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-uk.md`
- `reconstruction/earliest-sayings-gospel/evidence-dossier-en.md`
- `reconstruction/earliest-sayings-gospel/parallel-edition.md`
- `bibliography/bibliography-working.md`
- `bibliography/source-rights-register.md`
- `project/rights-and-citation-policy.md`

## Tasks

1. Create an output structure under `output/` if needed:
   - `output/uk-paper-book/`
   - `output/en-paper-book/`
   - `output/digital-scholarly-companion/`
2. Create a generator-ready Ukrainian book source file that begins with the clean 37-unit reader, then adds a print-safe appendix pathway for all 114 logia.
3. Create a generator-ready English book source file that begins with the clean 37-unit reader, then adds the English evidence/dossier material in a print-safe structure.
4. Create a digital companion source/manifest that preserves the full apparatus and points to cards, notes, primary sources, controls, audits, and bibliography.
5. Add a short production README in each output folder explaining what the file is, what still needs proofing, and which source files generated it.
6. Do not create final PDFs yet unless the repo already has an established generator. This pass should prepare clean source packages for the later rendering/proof stage.
7. Update project documentation and the open-task queue.

## Required Outputs

Produce:

- `output/uk-paper-book/book-source-uk.md`
- `output/en-paper-book/book-source-en.md`
- `output/digital-scholarly-companion/companion-manifest.md`
- `output/uk-paper-book/README.md`
- `output/en-paper-book/README.md`
- `output/digital-scholarly-companion/README.md`
- an execution report at `project/generator-ready-books-pass-v0.1.md`

## Validation

Run:

```bash
python3 tools/qa_crosscheck.py
git diff --check
```

Also run a print-safety grep against `output/uk-paper-book/` and `output/en-paper-book/` for internal-only repository paths such as `corpus/`, `reconstruction/`, `project/`, `sources/`, `controls/`, and `notes/`. If any remain in paper-facing files, replace them with print-safe references or document the exception.
