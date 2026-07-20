# First Proof QA And Layout Corrections v0.1

Date: 2026-07-19

## Trigger

The first PDF render proved that the renderer works, but the paper output looked too much like a technical Markdown export. The user noted that readers are more accustomed to the visual style of mass Bible editions.

This pass therefore pivots the paper proof direction toward a compact Bible-style layout.

## Plan Executed

1. Inspect the first generated proof pages.
2. Identify visible defects.
3. Implement the smallest high-value renderer changes.
4. Re-render all proof artifacts.
5. Validate structural QA, whitespace, page counts, extracted text, and paper-path safety.
6. Record the next design task.

## Defects Found

| Defect | Severity | Decision |
| --- | --- | --- |
| Paper PDFs looked like raw Markdown / technical PDF output | High | Replace first paper render mode with Bible-style proof mode. |
| Clean text used oversized heading rhythm rather than scripture-like compact numbering | High | Render clean text as compact numbered units. |
| Paper proof typography used a technical sans look | Medium | Prefer Times New Roman when available. |
| Clean text had too much vertical whitespace | Medium | Use compact paragraph leading. |
| Large all-114 tables were too dense and spreadsheet-like | Medium | Compact columns for first proof; leave full redesign for next pass. |
| First two-column attempt flowed row-by-row rather than column-by-column | Medium | Corrected to left column top-to-bottom, then right column top-to-bottom. |

## Changes Made

Updated:

- `tools/render_first_proofs.py`

Renderer changes:

- added separate paper-PDF rendering path;
- kept digital companion rendering technical;
- added simple title page;
- added simple contents page;
- added commons notice;
- rendered clean text in compact two-column form;
- changed default font priority to Times New Roman before Arial Unicode;
- rendered logion numbers inline;
- compacted reference tables to key print columns;
- removed paper-facing repository/output path exposure;
- corrected two-column reading order.

Created:

- `project/bible-style-paper-layout-policy-v0.1.md`

Regenerated:

- `output/uk-paper-book/euagelia-uk-proof.pdf`
- `output/en-paper-book/euagelia-en-proof.pdf`
- `output/digital-scholarly-companion/euagelia-digital-companion-proof.pdf`
- HTML/source snapshots and render log.

## Validation Results

Commands run:

```bash
/Users/arseny/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 tools/render_first_proofs.py
python3 tools/qa_crosscheck.py
git diff --check
```

PDF checks:

| Proof | Pages | Result |
| --- | ---: | --- |
| Ukrainian paper proof | 6 | Generated; Bible-style clean text visible. |
| English paper proof | 6 | Generated; Bible-style clean text visible. |
| Digital companion proof | 2 | Generated; technical paths preserved as expected. |

Paper extracted-text safety:

- no `corpus/`;
- no `reconstruction/`;
- no `project/`;
- no `sources/`;
- no `controls/`;
- no `notes/`;
- no `http://` or `https://`;
- no `output/`.

Structural QA:

- 114/114 card files;
- 114/114 appendix sections;
- 114/114 appendix source/control sections;
- 37/37 reader units synchronized across language layers and control tables;
- clean-text anchors present for all clean-reader logia.

## Remaining Layout Work

1. The clean text now has the right general direction, but the columns need final page balancing and possibly narrower margins.
2. The title page is still a placeholder.
3. The contents page is still a placeholder, not a generated TOC.
4. The all-114 apparatus table is still not book-quality; it should become split indexes or a clearer appendix reference system.
5. The paper books still need final front matter, bibliography styling, witness index, logion index, canonical parallels index, and theme index.
6. The digital companion still needs a generated cross-reference index, not only a manifest.

## Completion Decision

First proof QA and the first visible layout correction pass are complete.

The project now has a working Bible-style paper proof direction, not merely a technical render.

## Next Recommended Task

Run Bible-style book design and index pass:

- improve paper title/front matter;
- generate a real TOC or stable TOC placeholder;
- replace the all-114 table with print-friendly split indexes;
- add logion, witness, and canonical parallel indexes;
- re-render Ukrainian and English proofs;
- preserve the digital companion as the place for the full technical apparatus.
