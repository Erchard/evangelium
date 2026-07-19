# Bible-Style Book Design And Index Pass v0.1

Date: 2026-07-19

## Objective

Improve the Ukrainian and English paper-book proofs so they move from technical proof toward a familiar mass-Bible-style book layout, while preserving the digital scholarly companion as the technical apparatus layer.

The frozen 37-unit clean-reader corpus was not changed.

## Plan Executed

1. Read the current queue, Bible-style policy, renderer, and paper-book source files.
2. Fix the active queue heading drift from the older bibliography task.
3. Improve paper front matter and contents placeholder.
4. Preserve the compact two-column clean text with inline logion numbers.
5. Replace raw all-114 paper tables with print-friendly split indexes.
6. Re-render Ukrainian, English, and digital companion proofs.
7. Validate structural QA, whitespace, PDF extraction, page counts, and paper path safety.
8. Record remaining design work and next task.

## Renderer Changes

Updated:

- `tools/render_first_proofs.py`

Changes:

- kept the paper renderer separate from the digital companion renderer;
- preserved compact Bible-style clean reader layout;
- improved front-matter wording from first proof to Bible-style proof v0.3;
- created a reader note page from the paper source's "how to read" section;
- parsed the all-114 table from paper-book sources;
- replaced raw all-114 table output with four print-oriented indexes:
  - included logia;
  - non-included logia;
  - witness / Greek-layer index;
  - decision-status index;
- separated the non-included index onto its own page;
- kept paper PDFs free from repository paths, URLs, and output paths;
- preserved the digital companion as a technical manifest with paths.

## Generated Proofs

Regenerated:

- `output/uk-paper-book/euagelia-uk-proof.pdf`
- `output/en-paper-book/euagelia-en-proof.pdf`
- `output/digital-scholarly-companion/euagelia-digital-companion-proof.pdf`
- `output/render-log-first-proofs-v0.1.md`

Current page counts:

| Proof | Pages |
| --- | ---: |
| Ukrainian paper proof | 9 |
| English paper proof | 9 |
| Digital companion proof | 2 |

## Validation

Commands run:

```bash
/Users/arseny/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 tools/render_first_proofs.py
python3 tools/qa_crosscheck.py
git diff --check
```

Results:

- structural QA passed;
- whitespace diff check passed;
- 114/114 card files present;
- 114/114 appendix sections present;
- 114/114 appendix source/control sections present;
- 36/36 reader units synchronized across language layers and control tables;
- clean-text anchors present for all clean-reader logia.

Paper PDF extracted-text safety:

- no `corpus/`;
- no `reconstruction/`;
- no `project/`;
- no `sources/`;
- no `controls/`;
- no `notes/`;
- no `http://` or `https://`;
- no `output/`;
- no replacement-character failure detected.

Visual spot checks:

- clean reader has the intended compact two-column Bible-style direction;
- included-logia index is readable;
- non-included-logia index is now separated from the included index;
- witness/status index is readable;
- non-included index is still dense and should be polished in a later design pass.

## Remaining Design Work

1. Title page is still a proof placeholder, not a publication-ready title page.
2. TOC is still a stable placeholder, not generated from final page numbers.
3. Non-included logia index remains dense; it may need smaller grouped sections or two pages.
4. Witness/status indexes could be improved with compressed number ranges.
5. Bibliography is still not formatted as a final print bibliography.
6. Digital companion still needs a generated cross-reference index beyond the manifest proof.
7. Final PDF proofing still needs page-by-page visual review after the next render.

## Completion Decision

Bible-style book design and first index replacement are complete at v0.1.

The paper proofs are no longer raw technical exports; they now have a credible Bible-style clean reader direction and paper-safe indexes.

## Next Recommended Task

Run final proof polish and bibliography/TOC pass:

- refine title page and publication note;
- generate or stabilize TOC with page references;
- format final bibliography section;
- compress witness/status indexes;
- improve non-included index density;
- re-render and inspect full PDF page set;
- create final proof-polish report.
