# Final Proof Polish, Bibliography, And TOC v0.1

Date: 2026-07-19

## Objective

Polish the Ukrainian and English Bible-style paper proofs toward publication-grade first editions without changing the frozen 37-unit clean-reader corpus.

This pass focused on front matter, proof-stable contents, compact print bibliography, index density, and proof QA.

## Plan Executed

1. Read the saved prompt, Bible-style policy, previous design/index report, renderer, paper-book sources, bibliography, rights register, and current proof outputs.
2. Keep the clean reconstructed text unchanged.
3. Improve front matter with a calmer title page, edition note, commons notice, and reader-facing subtitle.
4. Replace the placeholder contents page with a proof-stable section order note that avoids fake page precision before final typesetting.
5. Replace raw bibliography-group text in paper PDFs with compact print-facing source keys.
6. Keep detailed rights/source information in the digital companion and project bibliography files.
7. Reduce non-included-logia index density by removing the Greek column from that long table and moving Greek evidence lookup to the witness index.
8. Compress long number lists in witness/status indexes into ranges where safe.
9. Re-render Ukrainian, English, and digital companion proofs.
10. Validate structure, whitespace, PDF path-safety, page counts, checksums, and visual previews.

## Files Updated

- `tools/render_first_proofs.py`
- `output/uk-paper-book/euagelia-uk-proof.pdf`
- `output/en-paper-book/euagelia-en-proof.pdf`
- `output/digital-scholarly-companion/euagelia-digital-companion-proof.pdf`
- `output/render-log-first-proofs-v0.1.md`

## Renderer Changes

- Paper proof label updated to v0.4.
- Title page now has a publication-oriented title, short subtitle, proof note, and commons notice.
- Contents page now explicitly states that page numbers may change during final typesetting.
- Bibliography page now prints compact source keys:
  - `NHC II,2`;
  - `P.Oxy. 1`;
  - `P.Oxy. 654`;
  - `P.Oxy. 655`;
  - `SBLGNT`;
  - `Mattison Thomas`;
  - protected scholarly controls such as Layton, Lambdin, DeConick, Patterson / Meyer, Brill CGL, NA / UBS;
  - `P.Oxy. 5575` as protected control material.
- Long non-included-logia table reduced to logion / status / subject.
- Witness and status index number lists now compress simple numeric runs, for example `1-5, 7`.
- Paper PDFs remain free of internal repository paths and URLs.

## Generated Proofs

| Proof | Pages | SHA256 |
| --- | ---: | --- |
| Ukrainian paper proof | 9 | `b6d9fa5c86b2fdc1b5a64db62b492bc115a74232eab55efd995aa57a3f29e7dd` |
| English paper proof | 9 | `776618b5236c9e9f6910770155e6de687a9c609524774d0c5a3d9b3d7dcb208e` |
| Digital scholarly companion proof | 2 | `b5569b13d848728c7c92a06e434b4d6a7f639c1b3e8fb9316d5cc0cebe68e93a` |

Full render manifest: `output/render-log-first-proofs-v0.1.md`.

## Validation

Commands run:

```bash
/Users/arseny/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 tools/render_first_proofs.py
python3 tools/qa_crosscheck.py
git diff --check
pdfinfo output/uk-paper-book/euagelia-uk-proof.pdf
pdfinfo output/en-paper-book/euagelia-en-proof.pdf
pdfinfo output/digital-scholarly-companion/euagelia-digital-companion-proof.pdf
```

Structural QA result:

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

- Ukrainian title page is calm and proof-marked;
- Ukrainian contents page avoids false final page numbers;
- Ukrainian clean reader keeps compact Bible-style two-column layout;
- Ukrainian non-included index continues across pages without losing rows;
- Ukrainian witness/status indexes are more compact after range compression;
- Ukrainian bibliography page no longer exposes raw working bibliography headings.

## Remaining Blockers Before Final Print Release

1. Full page-by-page visual proofing still needs a release-candidate pass for both Ukrainian and English PDFs.
2. The current renderer is still a first-proof ReportLab renderer, not a professional book typesetting system.
3. True final TOC page references should wait until layout is locked.
4. Bibliography is now print-facing but not yet a fully styled final bibliography with all page-specific checks.
5. The digital companion still needs a richer scholarly cross-reference index beyond the current manifest proof.
6. Cover design, trim size, printer settings, PDF/A or print-production conformance, and final metadata remain outside this proof pass.

## Completion Decision

Final proof polish, bibliography, and TOC pass is complete at v0.1.

The paper proofs are closer to release-candidate form, but the project should not be called final until a dedicated release-candidate visual proof and packaging audit is complete.

## Next Recommended Task

Run release-candidate proof package audit:

- render final preview PNGs for every page of Ukrainian and English PDFs;
- inspect each page for overflow, awkward breaks, cramped tables, broken Ukrainian/English text, and footer/header issues;
- decide whether to keep the current ReportLab renderer or migrate to a stronger print/typesetting pipeline;
- create a release-candidate checklist for paper and digital outputs;
- produce a single final blockers list before any publication claim.
