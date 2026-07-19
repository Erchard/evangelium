# Release-Candidate Proof Package Audit v0.1

Date: 2026-07-19

## Objective

Audit the current Ukrainian paper proof, English paper proof, and digital scholarly companion proof as a possible release-candidate package.

This pass did not change the frozen 37-unit clean-reader corpus. It assessed publication fitness, page-by-page visual quality, package completeness, and remaining blockers.

## Plan Executed

1. Read the saved release-candidate prompt, previous proof-polish report, print/digital architecture, render log, queue, and current proof artifacts.
2. Re-render all proof artifacts from current sources.
3. Generate PNG previews for every page:
   - Ukrainian paper proof: 9 pages;
   - English paper proof: 9 pages;
   - digital scholarly companion proof: 2 pages.
4. Build contact sheets for complete visual inspection.
5. Inspect every page for clipping, overflow, awkward breaks, dense tables, wrong-language leakage, title/TOC/bibliography/index problems, and footer/header issues.
6. Run automated checks:
   - `python3 tools/qa_crosscheck.py`;
   - `git diff --check`;
   - extracted-text paper path-safety scan;
   - `pdfinfo` page-count and format checks;
   - checksum review from `output/render-log-first-proofs-v0.1.md`.
7. Record release-candidate verdict and next production task.

## Artifacts Checked

| Artifact | Pages | Page size | SHA256 |
| --- | ---: | --- | --- |
| `output/uk-paper-book/euagelia-uk-proof.pdf` | 9 | A4 | `141acc4439f0d3cd99fc8a3794d635c24d711453cdcf4c1156ed8eab726eab3a` |
| `output/en-paper-book/euagelia-en-proof.pdf` | 9 | A4 | `cb420495e20212e457a9c6dd0e65b2b73c1a7a3bca996ade1956e99ebaf80f50` |
| `output/digital-scholarly-companion/euagelia-digital-companion-proof.pdf` | 2 | A4 | `645327a4eede404b2bc4e5b047eb3dd4bea119d8874732f811c76abe8e2b0389` |

Full render manifest: `output/render-log-first-proofs-v0.1.md`.

## Automated QA Results

Structural QA:

- 114/114 card files present;
- 114/114 appendix sections present;
- 114/114 appendix source/control sections present;
- 37/37 reader units synchronized across language layers and control tables;
- clean-text anchors present for all clean-reader logia.

Whitespace:

- `git diff --check` passed.

Paper PDF extracted-text safety:

- Ukrainian paper PDF has no `corpus/`, `reconstruction/`, `project/`, `sources/`, `controls/`, `notes/`, `http://`, `https://`, or `output/`.
- English paper PDF has no `corpus/`, `reconstruction/`, `project/`, `sources/`, `controls/`, `notes/`, `http://`, `https://`, or `output/`.
- No replacement-character extraction failure detected.

Digital companion:

- Repository paths are present by design and are allowed in the digital layer.

## Page-By-Page Visual QA

### Ukrainian Paper Proof

| Page | Content | QA Result |
| ---: | --- | --- |
| 1 | Title page | No clipping or overlap. Still proof-marked, not final title-page design. |
| 2 | Contents | No clipping. Contents is proof-stable and avoids false final page numbers. Visually sparse but acceptable for proof. |
| 3 | Clean reconstructed text | Strongest page. Compact two-column Bible-style reader works; no apparatus clutter. |
| 4 | How to read this edition | Readable, sparse, no visible overflow. |
| 5 | Included-logia index | Table is readable but visually technical. Acceptable for proof, not final book design. |
| 6 | Non-included-logia index, first part | No clipping, but very dense. Needs design improvement before final print. |
| 7 | Non-included-logia index, continuation | No clipping; large white remainder. Page break is acceptable but visually unfinished. |
| 8 | Witness/status indexes | Range compression works; still table-like but readable. |
| 9 | Bibliography and rights | No clipping. Print source keys are clearer than the previous raw bibliography headings. Still not a final styled bibliography. |

### English Paper Proof

| Page | Content | QA Result |
| ---: | --- | --- |
| 1 | Title page | No clipping or overlap. Still proof-marked, not final title-page design. |
| 2 | Contents | No clipping. Proof-stable TOC is honest and readable. |
| 3 | Clean reconstructed text | Strong compact two-column reader page; no visible overflow. |
| 4 | How to read this edition | Readable, sparse, no visible overflow. |
| 5 | Included-logia index | Readable but visually technical. |
| 6 | Non-included-logia index, first part | No clipping; dense but less overloaded than earlier versions. |
| 7 | Non-included-logia index, continuation | No clipping; large white remainder. |
| 8 | Witness/status indexes | Readable; table style remains proof-level. |
| 9 | Bibliography and rights | No clipping; compact source-key block is readable. Not final bibliography styling. |

### Digital Scholarly Companion Proof

| Page | Content | QA Result |
| ---: | --- | --- |
| 1 | Companion manifest, first half | No visible clipping. Repository paths are allowed here. |
| 2 | Companion manifest, second half | No visible clipping. Still a manifest proof, not a full digital companion. |

## Blocking Issues

1. The current Ukrainian and English PDFs are not complete final books. They contain the clean text, reader orientation, indexes, and source-key pages, but they do not yet include the full reader-facing 114-logion commentary appendix promised by the project concept.
2. The digital scholarly companion proof is still a manifest, not a complete companion package with the full apparatus, cross-reference index, and bundled research files.
3. The current ReportLab renderer is acceptable for proof skeletons, but not yet adequate as the final book-production system if the paper books must include hundreds of pages of commentary, bibliography, and indexes.
4. Final TOC page references cannot be generated honestly until the full paper books are assembled and pagination is stable.

## Non-Blocking Polish Issues

1. Paper title pages still identify themselves as proof pages. This is correct for now, but must change in a release edition.
2. Index pages are readable but still table-like; a professional print edition should use cleaner book-index typography.
3. Page 7 in both paper proofs has a short continuation table with large blank space.
4. Bibliography is print-facing but not yet in one final citation style with page-specific checks.
5. The footer says `EUAGELIA proof - N`; this is appropriate for proofs, not release files.

## Future Edition Issues

1. Cover design, trim size, printer profile, PDF/A or press-ready PDF conformance, ISBN/imprint metadata, and copyright/commons front matter remain future packaging work.
2. The Arabic Injil layer is documented conceptually but not part of these paper proof packages.
3. A richer digital companion should eventually be generated as HTML/PDF with cross-links and machine-readable indexes.

## Release-Candidate Verdict

Current PDFs are **not release candidates for the final paper books**.

They are acceptable as **first public proof skeletons** for reviewing the clean reader, basic Bible-style direction, print-safe references, and early index strategy.

The current renderer should not be treated as the final production pipeline until it proves it can assemble and paginate the full Ukrainian and English books with the full 114-logion appendix.

## Next Recommended Task

Run a full book assembly and typesetting pipeline pass:

- assemble a complete Ukrainian paper book with:
  - clean text first;
  - reader orientation;
  - full 114-logion commentary appendix;
  - print-safe source keys;
  - bibliography;
  - indexes;
- define the English paper book strategy:
  - either generate/translate a full English appendix;
  - or publish the English book as clean text plus evidence dossier and indexes until the full English appendix exists;
- decide whether to keep ReportLab or migrate to a stronger typesetting pipeline such as Typst, LaTeX, or a structured Markdown-to-PDF workflow;
- regenerate full-length proofs;
- rerun page-by-page QA after full assembly.
