# Final 100% Execution Pass Report

Date: 2026-07-19.

Prompt executed: `project/ide-codex-final-100-percent-execution-master-prompt-2026-07-19.md`.

## What Was Done

- Ran baseline structural QA.
- Audited the Ukrainian paper-book source for reader-facing technical noise.
- Strengthened `tools/assemble_full_book_sources.py` so the Ukrainian paper book removes or rewrites:
  - accidental Markdown bold inside normal paragraphs;
  - backtick/code-style fragments;
  - `clean reader`, `appendix-only`, `marker`, `synoptic`, `profile`, `control`, `retroversion`, and similar internal terms;
  - leftover English phrases such as `wisdom-style`, `Canonical`, `Cluster`, `Living/dead`, `seek/find`;
  - several grammatical artifacts created by earlier automatic substitutions.
- Regenerated paper and digital sources.
- Regenerated all proof PDFs.
- Regenerated the Typst production pilot package.
- Re-ran structural QA successfully.

## Current Ukrainian Paper-Book Metrics

- Logion appendix sections: 114/114.
- `### Коптський текст`: 114/114.
- `### Грецький текст`: 114/114.
- `### Український переклад`: 114/114.
- `### Як це можна зрозуміти`: 114/114.
- `### Рішення щодо реконструкції`: 78/114.
- `### Короткий висновок`: 1/114.

## Reader-Facing Noise Check

The current generated Ukrainian paper-book source has zero occurrences of the following checked terms:

- `**`;
- `clean reader`;
- `appendix-only`;
- `marker`;
- `маркер`;
- `синоптик` / `синоптич`;
- `профіль`;
- `контроль` / `контролює`;
- `ретроверсія`;
- `DCLP XML`;
- `локальний робочий`;
- `Статус у читацькому виданні`;
- leftover English labels such as `Canonical`, `Cluster`, `Living/dead`, `Beatitudes`, `wisdom-style`, `seek/find`.

## Verified Commands

```bash
python3 tools/qa_crosscheck.py
/Users/arseny/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 tools/assemble_full_book_sources.py
/Users/arseny/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 tools/render_full_book_proofs.py
/Users/arseny/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 tools/build_typst_production_pilot.py
python3 tools/qa_crosscheck.py
```

Final QA result: OK.

## Remaining High-Priority Gaps

1. Standardize the appendix ending for all 114 logia.
   - Every logion should have a clearly named decision section.
   - Every logion should have a short final conclusion with likely date range, confidence, and reason.
   - Current state: decision heading 78/114; short conclusion 1/114.

2. Perform a human-level Ukrainian copyedit after structural normalization.
   - Automatic sanitizing now removes major jargon, but some prose may still sound stiff.
   - The next pass should read logia as continuous book prose, not only as machine-searchable text.

3. Move final book production from ReportLab proofs to full Typst or professional layout.
   - ReportLab remains useful for proof PDFs.
   - Final paper publication still needs professional hyphenation, page breaking, column flow, and visual signoff.

4. Resolve the Logion 1 / opening-words / title decision before final freeze.
   - This remains conceptually important because it determines whether the reconstructed text begins with the collection prologue or the first reconstructed saying of Jesus.

## Next Best Step

Run a dedicated all-114 appendix ending normalization pass:

- add or normalize `### Рішення щодо реконструкції` for every logion;
- add `### Короткий висновок` for every logion;
- keep the language plain and reader-facing;
- do not change clean-reader membership unless a separate decision note is created.
