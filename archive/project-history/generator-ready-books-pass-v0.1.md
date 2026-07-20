# Generator-Ready Books Pass v0.1

Status: completed, 2026-07-18.

## Purpose

This pass creates the first generator-ready source packages for the Ukrainian and English paper books and a matching digital scholarly companion manifest.

## Plan Executed

1. Created dedicated output folders for Ukrainian paper, English paper, and digital companion packages.
2. Generated a Ukrainian book source beginning with the frozen clean reader and followed by a print-safe 114-logion appendix pathway.
3. Generated an English book source beginning with the frozen clean reader and followed by a print-safe all-114 evidence pathway.
4. Generated a digital scholarly companion manifest preserving repository paths, evidence notes, source families, controls, audits, bibliography, and rights files.
5. Added production README files for all three output packages.
6. Checked paper-facing files for internal-only repository paths.

## Outputs

- `output/uk-paper-book/book-source-uk.md`
- `output/en-paper-book/book-source-en.md`
- `output/digital-scholarly-companion/companion-manifest.md`
- `output/uk-paper-book/README.md`
- `output/en-paper-book/README.md`
- `output/digital-scholarly-companion/README.md`

## Print-Safety Result

The first paper book source files do not contain internal-only repository paths such as `corpus/`, `reconstruction/`, `project/`, `sources/`, `controls/`, or `notes/`.

## Remaining Limits

These are source packages, not final PDFs. They still need:

- final bibliography and source-rights release clearance;
- title-page and front-matter design;
- page-layout rendering;
- proof QA for numbering, indexes, references, and typography.

## Next Step

Run print / digital render proof preparation. This should confirm that the paper books are self-contained and print-safe while the digital companion preserves the full scholarly apparatus.
