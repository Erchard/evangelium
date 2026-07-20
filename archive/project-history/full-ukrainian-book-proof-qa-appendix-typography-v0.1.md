# Full Ukrainian Book Proof QA And Appendix Typography v0.1

Status: completed, 2026-07-19.

## Scope

This pass executed the saved prompt `project/ide-codex-full-ukrainian-book-proof-qa-appendix-typography-v0.1-prompt.md`.

The goal was to verify the full Ukrainian paper proof as a reader-facing book, not only as a generated artifact. The pass covered:

- the 118-page Ukrainian full proof PDF;
- the clean-reader-first book order;
- the full 114-logion appendix;
- paper-safe appendix typography and status labels;
- structural QA against the 114-card and 37-reader control layers.

## Files Checked Or Regenerated

- `output/uk-paper-book/book-source-uk-full.md`
- `output/uk-paper-book/euagelia-uk-full-proof.pdf`
- `output/uk-paper-book/euagelia-uk-full-proof.source.md`
- `output/render-log-full-book-proofs-v0.1.md`
- `project/full-ukrainian-book-proof-page-scan-v0.1.tsv`

## Page-Level QA Summary

The regenerated Ukrainian proof has 118 A4 pages.

| Page Range | Result |
| --- | --- |
| 1 | Title page present; intentionally sparse. |
| 2 | Clean reconstructed text appears first, before commentary and apparatus. |
| 3 | Reader orientation page present; no internal repository paths. |
| 4-117 | Full 114-logion appendix present, visually stable, no blank-page run, no visible clipping, no footer collision, no page overflow detected in contact-sheet review. |
| 117 | Logion 114 present in appendix with exclusion rationale layer; it remains outside the clean reconstruction. |
| 118 | Bibliography and rights page present. |

Machine-readable page metrics were saved in `project/full-ukrainian-book-proof-page-scan-v0.1.tsv`. The only intentionally short page is the title page; no appendix page fell below the low-content threshold used in this pass.

## Typography Fix Applied

The main safe defect found during proof review was not a page-break failure but a reader-register problem: the Ukrainian appendix still exposed English/internal labels such as `Reader status`, `Greek witness status`, `Publication status`, and raw decision codes.

The generator now localizes these paper-facing status lines in `tools/assemble_full_book_sources.py`:

- `Reader status:` -> `Статус у читацькому виданні:`
- `Greek witness status:` -> `Грецьке свідчення:`
- `Publication status:` -> `Статус публікації:`
- raw decision codes are rendered as Ukrainian reader-facing labels, while the digital companion can still preserve technical codes and paths.

This is an output-layer change only. It does not alter clean-reader membership, logion numbering, source text, card decisions, or evidence logic.

## QA Commands

```bash
python3 tools/assemble_full_book_sources.py
/Users/arseny/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 tools/render_full_book_proofs.py --only uk
python3 tools/qa_crosscheck.py
pdfinfo output/uk-paper-book/euagelia-uk-full-proof.pdf
```

Structural QA result:

- 114/114 card files;
- 114/114 appendix sections;
- 114/114 appendix source/control sections;
- 37/37 reader sets synchronized across language layers and control tables;
- exact clean-text anchors present for all clean-reader logia.

Paper-output text scan result:

- no remaining `Reader status`, `Greek witness status`, `Publication status`, or raw all-caps decision-code leakage in `output/uk-paper-book/book-source-uk-full.md`;
- PDF page count remains 118 after the typography fix.

## Current Verdict

The Ukrainian full proof is now usable as a serious first full paper proof. It is still a proof, not a final press-ready book, because final production should later decide whether to keep the current ReportLab layout or move to a stronger book typesetting system. But the biggest immediate Ukrainian-blocker is closed: the reader now sees a clean text first and a full appendix whose status layer no longer looks like raw project metadata.

## Remaining Production Risks

1. The English paper book still lacks a full 114-logion commentary appendix; it currently pairs the clean English text with the evidence dossier.
2. The digital scholarly companion is still a source-map proof, not a full research edition.
3. Final print production still needs a dedicated typography decision: current ReportLab output is good for proofing, but not yet the ideal final book layout engine.

## Recommended Next Step

Generate the full English 114-logion commentary appendix from the Ukrainian appendix and controlled card/evidence layers, then assemble and render an English full proof that mirrors the Ukrainian book architecture.
