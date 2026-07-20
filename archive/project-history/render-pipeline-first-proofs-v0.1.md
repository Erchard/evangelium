# Render Pipeline And First Proofs v0.1

Date: 2026-07-19

## Objective

Create the first repeatable proof artifacts for:

- Ukrainian paper book;
- English paper book;
- digital scholarly companion manifest/index.

This pass does not change the clean-reader corpus. It creates a minimal proof renderer and first HTML/PDF artifacts so that the project can move from source preparation into visual/text proof QA.

## Plan Executed

1. Inspect local rendering capabilities.
2. Choose the simplest reliable proof path.
3. Create a repeatable renderer script.
4. Generate first proof artifacts.
5. Validate generated files, page counts, text extraction, paper-source safety, and visual PNG previews.
6. Record layout risks and the next correction pass.

## Rendering Capability Audit

Available:

- Poppler `pdftoppm`;
- Poppler `pdfinfo`;
- bundled Codex Python runtime;
- Python packages in bundled runtime: `reportlab`, `pdfplumber`, `pypdf`;
- local Unicode font: `/System/Library/Fonts/Supplemental/Arial Unicode.ttf`.

Not available in the checked environment:

- `pandoc`;
- `typst`;
- `wkhtmltopdf`;
- local LaTeX command;
- Python `markdown`;
- Python `weasyprint`.

Decision: use a small ReportLab-based first-proof renderer, and generate HTML in parallel through a minimal standard-library Markdown conversion. This is a first proof pipeline, not the final book design system.

## Renderer Created

Created:

- `tools/render_first_proofs.py`

Command:

```bash
/Users/arseny/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 tools/render_first_proofs.py
```

The renderer creates:

- HTML proof;
- PDF proof;
- source snapshot copied next to the proof;
- SHA256 render log.

Paper PDF provenance was corrected so Ukrainian and English proof text does not expose repository or output paths. Digital companion provenance may preserve paths because that is the digital layer's purpose.

## Artifacts Generated

| Artifact | Status |
| --- | --- |
| `output/uk-paper-book/euagelia-uk-proof.html` | Generated |
| `output/uk-paper-book/euagelia-uk-proof.pdf` | Generated |
| `output/uk-paper-book/euagelia-uk-proof.source.md` | Generated |
| `output/en-paper-book/euagelia-en-proof.html` | Generated |
| `output/en-paper-book/euagelia-en-proof.pdf` | Generated |
| `output/en-paper-book/euagelia-en-proof.source.md` | Generated |
| `output/digital-scholarly-companion/euagelia-digital-companion-proof.html` | Generated |
| `output/digital-scholarly-companion/euagelia-digital-companion-proof.pdf` | Generated |
| `output/digital-scholarly-companion/euagelia-digital-companion-proof.source.md` | Generated |
| `output/render-log-first-proofs-v0.1.md` | Generated with SHA256 checksums |

PDF page counts:

| Proof | Pages | Page size |
| --- | ---: | --- |
| Ukrainian paper proof | 10 | A4 |
| English paper proof | 16 | A4 |
| Digital companion proof | 2 | A4 |

## Validation

Commands run:

```bash
python3 tools/qa_crosscheck.py
git diff --check
```

Result:

- structural QA passed;
- whitespace diff check passed;
- 114/114 card files present;
- 114/114 appendix sections present;
- 114/114 appendix source/control sections present;
- 37/37 reader units synchronized across language layers and control tables;
- clean-text anchors present for all clean-reader logia.

Paper PDF text extraction check:

- Ukrainian PDF extracted text length: 19,816 characters;
- English PDF extracted text length: 43,693 characters;
- no replacement-character failure detected in checked extraction;
- no `corpus/`, `reconstruction/`, `project/`, `sources/`, `controls/`, `notes/`, `http://`, `https://`, or `output/` strings found in Ukrainian or English paper PDF extracted text.

Visual PNG spot checks:

- Ukrainian clean-text page rendered and readable;
- English clean-text page rendered and readable;
- digital companion page rendered and preserves repository-path apparatus as expected;
- Ukrainian large all-114 table page rendered, but is dense and should be redesigned before final print.

## Known Layout Risks

1. The current renderer is functional, not beautiful. Typography, front matter, title pages, margins, and hierarchy need a real proof polish pass.
2. The all-114 tables render, but they are too dense for a high-quality paper book. They need splitting, landscape pages, appendix restructuring, or a compact index design.
3. The current PDF has no real table of contents yet.
4. The current PDF has no final title/copyright/commons pages.
5. The paper books still need final bibliography styling and print indexes.
6. The digital companion is still a manifest proof, not a generated cross-reference site/index.

## Completion Decision

This task is complete at first-proof level.

The project now has a repeatable proof renderer and first proof artifacts for all three output families.

## Next Recommended Task

Run first proof QA and layout correction pass:

1. Inspect generated Ukrainian and English proofs page by page.
2. Replace oversized 114-logion tables with print-friendly split tables or compact indexes.
3. Add title page, commons notice, short publication note, and table of contents.
4. Add first print indexes: logion index, witness index, canonical parallels index.
5. Re-render and compare checksums / page counts.
