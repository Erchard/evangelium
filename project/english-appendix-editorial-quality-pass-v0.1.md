# English Appendix Editorial Quality Pass v0.1

Status: completed system-level editorial pass, 2026-07-19.

## Scope

This pass executed `project/ide-codex-english-appendix-editorial-quality-pass-v0.1-prompt.md`.

The goal was to raise the English full appendix from a complete structural draft toward reader-facing commentary prose without changing the frozen clean reader, publication decisions, logion numbering, or evidence hierarchy.

## What Changed

The controlled appendix generator was improved:

- `tools/generate_english_appendix.py`

The generator now adds:

- `What This Saying Is About` for every logion;
- thematic explanatory hints based on the unit's motif;
- less repetitive possible-interpretation language;
- clearer source-status prose for extant Greek, partial/lacunose Greek, hypothetical retroversion, and Coptic-only cases;
- special reader-facing explanations for key logia: 1, 2, 3, 6, 21, 45, 63, 90, 103, 104, and 114;
- improved inclusion/exclusion/deferral paragraphs that no longer expose editor instructions such as `Explain...`.

The paper assembly sanitizer was improved:

- `tools/assemble_full_book_sources.py`

The English paper output now removes paper-facing `Status:` and obsolete `publication-facing draft` lines from dossier material.

## Generated Outputs

- `reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-en.md`
- `output/en-paper-book/book-source-en-full.md`
- `output/en-paper-book/euagelia-en-full-proof.pdf`
- `output/en-paper-book/euagelia-en-full-proof.source.md`
- `project/english-full-book-proof-page-scan-v0.1.tsv`

## QA

Commands run:

```bash
python3 tools/generate_english_appendix.py
python3 tools/assemble_full_book_sources.py
/Users/arseny/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 tools/render_full_book_proofs.py --only en
python3 tools/qa_crosscheck.py
```

Results:

- English appendix sections: 114/114.
- English full proof page count: 177.
- Structural QA passed: 114 cards, 114 appendix sections, 37 synchronized clean-reader units, clean-text anchors present.
- English paper PDF text scan found no internal repository paths.
- English paper PDF text scan found no obsolete "full English appendix absent" sentence.
- English paper PDF text scan found no `Explain ` editor-instruction leakage.
- English paper PDF text scan found no `Status:` or `draft` leakage from paper-facing dossier material.

## Current Verdict

The English appendix is no longer merely a skeletal control export. It is still generated prose and will benefit from future human literary copyediting, but it now gives ordinary English readers a clearer answer to the question, "What is this saying about, and why did the project include or exclude it?"

## Remaining Risk

The English proof grew into a real 177-page book. It has passed structural and text-safety checks, but it has not yet received the same full page-by-page visual proof pass that the Ukrainian 118-page book received.

## Recommended Next Step

Run a full English book proof QA and typography pass:

- render all 177 English pages to preview images;
- inspect every page for overflow, clipping, empty pages, orphan headings, and ugly section breaks;
- confirm clean reader first, full appendix, evidence dossier, summaries, and bibliography order;
- create a page-level QA report and remaining blocker list;
- decide whether the English proof can continue in ReportLab for public proofing or needs a stronger typesetting pipeline before release.
