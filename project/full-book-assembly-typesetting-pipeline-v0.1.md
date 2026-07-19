# Full Book Assembly And Typesetting Pipeline v0.1

Date: 2026-07-19

## Objective

Close the largest blocker found by the release-candidate audit: the previous paper PDFs were proof skeletons, not complete books.

This pass assembled full-length paper-facing sources, rendered new full-book proofs, and made an explicit typesetting decision.

The frozen 37-unit clean-reader corpus was not changed.

## Plan Executed

1. Read the release-candidate audit, publication architecture, clean-text-first principle, final product specification, Ukrainian and English clean readers, Ukrainian full appendix, English evidence dossier, current book sources, renderer, and queue.
2. Decide the immediate production strategy.
3. Create a full book source assembly script.
4. Create a separate full-book proof renderer instead of destabilizing the existing first-proof renderer.
5. Assemble a complete Ukrainian paper-book source with clean text first and full 114-logion appendix.
6. Assemble an honest English paper-book source with clean text and evidence dossier, while recording that a full English appendix remains missing.
7. Assemble a fuller digital companion source map.
8. Render full-length proof PDFs.
9. Run structural QA, whitespace QA, paper path-safety checks, page counts, and checksum logging.
10. Do selective visual inspection of beginning, middle, and end pages.

## Pipeline Decision

Immediate decision: **keep ReportLab as the proof-generation pipeline for now**, but do not treat it as final book-production typesetting.

Reason:

- ReportLab successfully rendered a full Ukrainian book proof with the 114-logion appendix.
- It preserves Unicode and can create repeatable checksummed artifacts.
- It is good enough for structural proofing and page-count discovery.
- It is not yet ideal for final print typography, long-form appendix layout, running heads, true TOC generation, professional indexes, widow/orphan control, or press-ready output.

Final production may still need migration to Typst, LaTeX, or a stronger structured Markdown-to-PDF workflow after the next full-book visual QA pass.

## New Tools

Created:

- `tools/assemble_full_book_sources.py`
- `tools/render_full_book_proofs.py`

The assembly script creates paper-facing sources and keeps repository paths out of paper outputs. The render script produces long-form proof PDFs and a checksum manifest.

## New Sources

Created:

- `output/uk-paper-book/book-source-uk-full.md`
- `output/en-paper-book/book-source-en-full.md`
- `output/digital-scholarly-companion/companion-source-full.md`

### Ukrainian Source

The Ukrainian full source now contains:

1. title;
2. clean reconstructed text first;
3. short reader orientation;
4. full 114-logion commentary appendix;
5. print source keys and rights note.

Paper sanitization removed internal repository paths and digital-only source-path sections from the printed appendix layer.

### English Source

The English full source now contains:

1. title;
2. clean reconstructed text first;
3. reader orientation;
4. evidence dossier and methodological defense;
5. print source keys and rights note.

The English source does **not** claim to contain a full 114-logion appendix. That remains a real blocker.

### Digital Companion Source

The digital source map preserves repository paths by design and points to paper outputs, corpus cards, language layers, bibliography, and rights files.

## Rendered Full Proofs

| Proof | Pages | SHA256 |
| --- | ---: | --- |
| Ukrainian full book proof | 118 | `f2d5e46779f5f69c59a28fc0396c0c5810aa5c2a063a9ec8f6b871ed3a314c6a` |
| English full book proof | 61 | `7e667810bb78babfc89def75c6efa02bb786250a9f065710e1052a907faa0b94` |
| Digital companion full proof | 5 | `c1a09f06de9f037adbc221b9d8a6c649a08ea6d5ccba144d550264524feebf79` |

Full render manifest:

- `output/render-log-full-book-proofs-v0.1.md`

## Validation

Commands run:

```bash
python3 tools/assemble_full_book_sources.py
/Users/arseny/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 tools/render_full_book_proofs.py
python3 tools/qa_crosscheck.py
git diff --check
pdfinfo output/uk-paper-book/euagelia-uk-full-proof.pdf
pdfinfo output/en-paper-book/euagelia-en-full-proof.pdf
pdfinfo output/digital-scholarly-companion/euagelia-digital-companion-full-proof.pdf
```

Structural QA:

- 114/114 card files present;
- 114/114 appendix sections present;
- 114/114 appendix source/control sections present;
- 37/37 reader units synchronized across language layers and control tables;
- clean-text anchors present for all clean-reader logia.

Paper path-safety:

- Ukrainian full proof: no `corpus/`, `reconstruction/`, `project/`, `sources/`, `controls/`, `notes/`, `http://`, `https://`, or `output/`.
- English full proof: no `corpus/`, `reconstruction/`, `project/`, `sources/`, `controls/`, `notes/`, `http://`, `https://`, or `output/`.
- No replacement-character extraction failure detected.

Selective visual QA:

- clean reader remains the first substantial reader-facing text;
- Ukrainian appendix pages render without visible clipping in sampled beginning, middle, and end pages;
- former standalone transition-heading pages were reduced by changing appendix/dossier labels to subsection headings in the assembled source;
- long-form typography remains proof-level and needs a dedicated full-book visual QA pass.

## Remaining Blockers

1. Full Ukrainian PDF needs page-by-page visual QA across all 118 pages.
2. English paper book still lacks a full 114-logion commentary appendix.
3. Digital companion is still a source map, not a full bundled scholarly companion.
4. ReportLab remains a proof renderer; final production may require Typst, LaTeX, or a stronger book pipeline.
5. Superseded by `project/full-ukrainian-book-proof-qa-appendix-typography-v0.1.md`: the most visible Ukrainian paper-facing technical status labels have now been localized.
6. True final TOC and indexes require stable full-book pagination.

## Completion Decision

Full book assembly and typesetting pipeline v0.1 is complete.

The project now has a real full Ukrainian paper-book proof for the first time. The English package is honest but incomplete because the full English appendix still needs to be generated or editorially translated.

## Next Recommended Task

Superseded next recommended task, 2026-07-19: full Ukrainian book proof QA and appendix typography polish, English full 114-logion appendix structural generation, English appendix editorial quality pass, full English book proof QA, digital scholarly companion expansion, and browsable digital companion HTML are complete. The current next task is final production typesetting and copyedit gate:

- decide whether final PDFs stay in ReportLab or move to Typst, LaTeX, or professional handoff;
- run final Ukrainian, English, and digital companion copyedit/proof checklist;
- preserve paper books as print-safe and the digital companion as source-rich;
- document remaining release-candidate blockers.
