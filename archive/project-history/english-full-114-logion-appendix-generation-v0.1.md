# English Full 114-Logion Appendix Generation v0.1

Status: completed first structural draft, 2026-07-19.

## Scope

This pass executed `project/ide-codex-english-full-114-logion-appendix-generation-v0.1-prompt.md`.

The objective was to close the largest English paper-book asymmetry: before this pass, the Ukrainian paper book had a full 114-logion commentary appendix, while the English full proof still paired the clean reader with the evidence dossier only.

## Implementation

Created a controlled generator:

- `tools/generate_english_appendix.py`

Generated:

- `reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-en.md`

Updated the full-book assembly:

- `tools/assemble_full_book_sources.py`

Regenerated:

- `output/en-paper-book/book-source-en-full.md`
- `output/en-paper-book/euagelia-en-full-proof.pdf`
- `output/en-paper-book/euagelia-en-full-proof.source.md`
- `output/render-log-full-book-proofs-v0.1.md`

Created QA support:

- `project/english-full-book-proof-page-scan-v0.1.tsv`

## What The English Appendix Now Contains

The English appendix now has 114/114 conventional Gospel of Thomas logion sections.

Each section includes:

- reconstruction status;
- clean-reader yes/no status;
- confidence;
- Greek witness status;
- English clean-reader text where the unit is printed in the reconstruction;
- source/control summary;
- reason for inclusion, non-inclusion, deferral, appendix-only treatment, or exclusion;
- possible interpretive readings;
- uncertainty and limits.

The appendix is print-safe: it uses logion numbers, witness labels, and source/control summaries instead of repository paths.

## QA

Commands run:

```bash
python3 tools/generate_english_appendix.py
python3 tools/assemble_full_book_sources.py
/Users/arseny/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 tools/render_full_book_proofs.py --only en
python3 tools/qa_crosscheck.py
pdfinfo output/en-paper-book/euagelia-en-full-proof.pdf
```

Results:

- English appendix sections: 114/114.
- English full proof page count: 177.
- Structural QA passed: 114 cards, 114 Ukrainian appendix sections, 37 synchronized clean-reader units.
- Paper-safety scan of the English PDF found no internal repository paths.
- The old paper-facing blocker sentence, "A full English 114-logion commentary appendix has not yet been generated," is gone.
- A quick visual proof check of contact sheets for the beginning, middle, and end found no obvious clipping, overlap, or failed rendering.

## Important Limitation

This is a first complete structural English appendix draft, not the final literary or scholarly English prose.

The generator intentionally privileges consistency, coverage, and decision-table synchronization over beautiful commentary prose. The next pass must copyedit the English appendix into reader-friendly publication language while preserving the same 114-section structure and not changing clean-reader membership.

## Current Verdict

The English book now has the missing full appendix layer. The main blocker has shifted from "English appendix absent" to "English appendix prose needs publication-quality editorial deepening."

## Recommended Next Step

Run an English appendix editorial-quality pass:

- keep all 114 sections;
- preserve decision-table synchronization;
- improve generic generated language into clearer reader-facing prose;
- especially deepen included logia, excluded Logion 114, and high-interest appendix-only logia;
- rerender the English proof and perform a fuller page-level proof QA.
