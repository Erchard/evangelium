# Full Appendix Editorial Consolidation, Logia 31-40 v0.1

Date: 2026-07-18

## Scope

This pass continues print-safe publication-level editorial consolidation of:

- `reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-uk.md`

Edited appendix chapters:

- Logia 31-40

## What Changed

- Removed separate `### Читацьке тлумачення з картки` blocks from Logia 31-40.
- Removed working-index navigation prose from Logion 40.
- Rewrote Logia 31-40 as integrated Ukrainian reader-facing appendix entries.
- Preserved current inclusion, partial inclusion, uncertain, and appendix-only decisions.
- Applied print-safe prose rules: reader-facing sections now use logion numbers, witness labels, canonical references, and plain-language explanation rather than relying on clickable repository paths.
- Preserved source/control material in separable source sections for the digital scholarly companion.
- Added or normalized `### Непевність і межі` for Logia 31-40.

## Editorial Decisions Preserved

| Logion | Decision after this pass |
| ---: | --- |
| 31 | Remains `INCLUDE_WITH_MARKER`; prophet-in-hometown core is stronger than physician clause. |
| 32 | Remains `INCLUDE_WITH_MARKER`; city-on-hill core is stronger than the "will not fall" expansion. |
| 33 | Remains `INCLUDE_WITH_MARKER`; P.Oxy. 1 supports the opening only, lamp unit remains hypothetical retroversion. |
| 34 | Remains `INCLUDE_WITH_MARKER`; Greek Thomas form remains hypothetical retroversion. |
| 35 | Remains `INCLUDE_WITH_MARKER`; strong-man saying is included without overclaiming exorcistic context. |
| 36 | Remains `INCLUDE_WITH_MARKER`; P.Oxy. 655 / P.Oxy. 5575 / Matt-Luke relationship remains complex. |
| 37 | Remains appendix-only `UNCERTAIN`; nakedness/no-shame expansion needs cluster control. |
| 38 | Remains appendix-only `UNCERTAIN`; P.Oxy. 655 remains fragmentary. |
| 39 | Remains `INCLUDE_WITH_MARKER`; keys-of-knowledge and wise-serpents/pure-doves composition remains marked. |
| 40 | Remains `UNCERTAIN`; Matt 15:13 control does not make it secure early Thomas. |

## Verification

Post-pass checks:

- Appendix logion headings: 114/114.
- `### Джерела й контрольні файли` sections: 114/114.
- Logia 31-40 contain no `### Читацьке тлумачення з картки`.
- Logia 31-40 contain no working-index navigation prose.
- Logia 31-40 each contain `### Непевність і межі`.
- Historical post-pass unconsolidated card-derived appendix blocks at this stage: 74.
- Historical post-pass working-index navigation phrases at this stage: 56.

Superseded current metrics after later Logia 41-50 consolidation and technical-debt closure:

- Remaining unconsolidated card-derived appendix blocks: 63.
- Remaining working-index navigation phrases: 46.
- Structural QA now passes through `python3 tools/qa_crosscheck.py`.

## Next Step

Superseded: Logia 41-50 consolidation has since been completed. The current next editorial package is Logia 51-60.
