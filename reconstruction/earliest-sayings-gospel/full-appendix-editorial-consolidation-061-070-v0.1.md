# Full Appendix Editorial Consolidation, Logia 61-70 v0.1

Date: 2026-07-18

## Scope

This pass continues print-safe publication-level editorial consolidation of:

- `reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-uk.md`

Edited appendix chapters:

- Logia 61-70

Prompt executed:

- `project/ide-codex-full-appendix-editorial-consolidation-061-070-v0.1-prompt.md`

## Plan Executed

1. Preserve all current clean-reader and appendix-only decisions.
2. Remove card-export style blocks from Logia 61, 62, and 64-70.
3. Keep Logion 63 as the only clean-reader unit in this package and lightly normalize its heading spacing.
4. Convert each target section into print-safe Ukrainian commentary with source labels readable on paper.
5. Keep repository paths only in `### Джерела й контрольні файли`.
6. Update active project documentation and task queue.
7. Rerun structural QA.

## What Changed

- Logia 61, 62, and 64-70 were rewritten as integrated reader-facing appendix entries.
- Generic `### Читацьке тлумачення з картки` blocks were removed from this range.
- Working-index placeholder prose was removed from this range.
- Each target logion now has a direct explanation of why it is included, not included, deferred, or appendix-only.
- Print-facing source summaries now use NHC II,2, P.Oxy. labels, canonical references, and cluster/control names before digital file paths.
- Logion 63 remains the included marked rich-fool core; no clean-reader wording changed.

## Editorial Decisions Preserved

| Logion | Decision after this pass |
| ---: | --- |
| 61 | Remains `DEFER_TO_CLUSTER`; Salome / couch / whole-divided material requires cluster treatment. |
| 62 | Remains `DEFER_TO_CLUSTER`; Matthew 6:3 controls the right/left-hand subunit, but the mystery frame remains apparatus material. |
| 63 | Remains `INCLUDE_WITH_MARKER`; short rich-fool core is printed, full logion remains uncertain. |
| 64 | Remains appendix-only stable / `KEEP_APPENDIX_ONLY_FOR_NOW`; banquet core is important but not promoted here, anti-merchant ending remains apparatus-only. |
| 65 | Remains appendix-only stable / `KEEP_APPENDIX_ONLY_FOR_NOW`; tenants parable is strong but allegorically risky. |
| 66 | Remains appendix-only stable / `KEEP_APPENDIX_ONLY_FOR_NOW`; rejected-stone saying is strongly controlled but likely interpretive/proof-text material. |
| 67 | Remains `APPENDIX_ONLY_UNCERTAIN`; self-knowledge aphorism has mainly internal Thomas support. |
| 68 | Remains `APPENDIX_ONLY_UNCERTAIN`; persecution beatitude has strong controls but difficult Thomas ending. |
| 69 | Remains `APPENDIX_ONLY_UNCERTAIN`; persecution/hunger beatitude material is composite and distinctive. |
| 70 | Remains `DEFER_TO_CLUSTER`; inner salvation/destruction requires self-knowledge anthropology control. |

## Verification

Post-pass checks:

- `python3 tools/qa_crosscheck.py` passes.
- Appendix logion headings remain 114/114.
- `### Джерела й контрольні файли` sections remain 114/114.
- Clean-reader set remains 37/37 synchronized across language layers and control tables.
- No target section from Logia 61-70 contains `### Читацьке тлумачення з картки`.
- No target section from Logia 61-70 contains working-index navigation prose.

## Next Step

Continue the same print-safe editorial consolidation pattern for Logia 71-80. That range includes inheritance, harvest, hidden/solitary/election motifs, and P.Oxy.-adjacent boundary material; it should preserve appendix-only/deferred decisions unless a separate controlled reader pass explicitly changes them.
