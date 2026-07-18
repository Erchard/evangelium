# Final Clean-Reader Freeze v0.1

Status: completed, 2026-07-18.

## Purpose

This pass freezes the clean reconstructed reader before book generation. It does not reopen selection unless a contradiction makes the 37-unit corpus unsafe.

## Frozen Clean-Reader Corpus

The final clean reader for this edition contains 37 logia or marked cores:

`1, 2, 3, 4, 5, 6, 9, 10, 16, 20, 22, 25, 26, 31, 32, 33, 34, 35, 36, 39, 41, 45A, 46A, 47B, 54, 63, 72, 73, 86, 89, 91A, 95, 96, 99, 100, 103A, 107`.

The print-facing clean reader may display the inherited Thomas logion numbers without suffixes. The suffixes remain editorial control labels for the apparatus:

- 45A: grapes/thorns core.
- 46A: John / least-in-kingdom core.
- 47B: two-masters core.
- 91A: recognition-of-time core.
- 103A: thief/watchfulness core.

## Cross-Layer Result

| Layer | Result |
| --- | --- |
| Ukrainian clean reader | 37/37 in expected order; clean-text audit passed. |
| English clean reader | 37/37 in expected order after removing status text, bracketed expansion labels, and notes. |
| Coptic base witness | 37/37 in expected order. |
| Greek layer | 37/37 in expected order; publication-polished Greek witness labels retained. |
| Parallel edition | 37/37 in expected order. |
| All-114 decision table | Reader set matches the frozen 37-unit corpus. |
| Full Ukrainian appendix | 114/114 sections; clean-text anchors exist for all 37 reader units. |
| Probability-vs-reader audit | Known tensions are documented and do not require membership changes in this edition. |

## Discrepancy Found And Fixed

The English clean reader still carried pre-freeze apparatus material:

- file title and working status line;
- bracketed labels such as `[Collection frame:]` and `[Possible Thomasine expansion:]`;
- explanatory notes under Logia 2, 3, and 4.

These were removed from `reconstructed-gospel-en.md`. The underlying English text and the 37-unit corpus were not changed.

## Known Tensions Retained With Rationale

The probability audit still reports one included late-leaning unit and ten excluded high-early units. These are not freeze blockers because each case is already controlled by a documented editorial rationale:

- Logion 1 remains in the clean reader only as a collection frame / prologue case, not as an ordinary reconstructed saying.
- Logia 64, 76, 78, 79, 90, 93, 94, 104, 109, and 113 remain outside the clean reader despite early-pressure scores because they are duplicative, Matthew/Luke-dependent risk cases, composite units, or too tightly bound to Thomasine editorial frames.

## Frozen Edition Verdict

The 37-unit clean reader is frozen for this edition.

No clean-reader membership change is recommended before book generation. Future changes should require new manuscript/source evidence or a separately documented post-freeze revision pass.

## Remaining Work Before Public Release

1. Generate the Ukrainian paper-book source package.
2. Generate the English paper-book source package.
3. Generate the digital scholarly companion with full evidence apparatus.
4. Close final bibliography `VERIFY` items and source-rights checks.
5. Run print/digital proof QA: numbering, indexes, page references, bibliography, rights notices, and absence of internal-only repository paths in paper-facing prose.

## Validation

Commands run:

```bash
python3 tools/qa_crosscheck.py
python3 tools/probability_reader_audit.py
git diff --check
```

Additional freeze checks confirmed that Ukrainian, English, Coptic, Greek, and parallel layers each contain the same 37 units in the same order, and that Ukrainian and English clean-reader files contain no status lines, apparatus markers, probability labels, P.Oxy. notes, repository paths, or hyperlinks.
