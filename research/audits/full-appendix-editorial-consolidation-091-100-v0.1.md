# Full Appendix Editorial Consolidation, Logia 91-100 v0.1

Date: 2026-07-18

## Scope

This pass continues print-safe publication-level editorial consolidation of:

- `reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-uk.md`

Edited appendix chapters:

- Logia 91-100

Prompt executed:

- `project/ide-codex-full-appendix-editorial-consolidation-091-100-v0.1-prompt.md`

## Plan Executed

1. Preserve all current clean-reader and appendix-only decisions.
2. Rewrite Logia 91-100 as integrated Ukrainian reader-facing appendix entries.
3. Preserve 91A, 95, 96, 99, and 100 as the clean-reader units in this package.
4. Keep Logia 92, 93, 94, 97, and 98 outside the clean reader.
5. Use print-safe source labels in prose and keep repository paths only in `### Джерела й контрольні файли`.
6. Update active project documentation and task queue.
7. Rerun structural QA.

## What Changed

- Removed separate `### Читацьке тлумачення з картки` blocks from Logia 91-100.
- Removed working-index navigation prose from Logia 91-100.
- Rewrote the sections as coherent print-facing commentary with:
  - status in the reconstruction;
  - reader-facing explanation;
  - inclusion/non-inclusion rationale;
  - possible interpretations;
  - uncertainty and limits;
  - print-facing source summary;
  - digital apparatus paths.
- Clarified why Logion 91 contributes only the recognition-of-time core.
- Clarified why Logia 92 and 94 remain appendix-only despite strong seek/find controls: Logion 2 remains the clean-reader representative.
- Clarified why Logion 93 remains appendix-only despite proverb-like force and Matthew 7:6 control.
- Clarified why Logia 95, 96, 99, and 100 are printed only as marked cores.
- Corrected the appendix source trail for Logia 97 and 98: both now point to their existing evidence notes.

## Editorial Decisions Preserved

| Logion | Decision after this pass |
| ---: | --- |
| 91 | 91A recognition-of-time core remains `INCLUDE_WITH_MARKER`; full dialogue frame remains appendix-only. |
| 92 | Remains `DEFER_TO_CLUSTER`; seek/find opening embedded in collection-memory expansion. |
| 93 | Remains appendix-only / `UNCERTAIN`; Matthew-only control and secrecy function require caution. |
| 94 | Remains `KEEP_APPENDIX_ONLY_FOR_NOW`; strong seek/knock unit but redundant with Logion 2 under current model. |
| 95 | Remains `INCLUDE_WITH_MARKER`; anti-usury / non-repayment giving core stays in clean reader. |
| 96 | Leaven core remains `INCLUDE_WITH_MARKER`; Father/ears frame remains apparatus material. |
| 97 | Remains `APPENDIX_ONLY_UNCERTAIN`; possible independent parable lacks close external control. |
| 98 | Remains `DEFER_TO_CLUSTER`; violent/power parable is vivid but externally undercontrolled. |
| 99 | True-family core remains `INCLUDE_WITH_MARKER`; kingdom-of-Father ending remains apparatus material. |
| 100 | Caesar/God core remains `INCLUDE_WITH_MARKER`; Thomas-specific third clause remains apparatus material. |

## Verification

Post-pass checks:

- `python3 tools/qa_crosscheck.py` passes.
- Appendix logion headings remain 114/114.
- `### Джерела й контрольні файли` sections remain 114/114.
- Clean-reader set remains 37/37 synchronized across language layers and control tables.
- No target section from Logia 91-100 contains `### Читацьке тлумачення з картки`.
- No target section from Logia 91-100 contains working-index navigation prose.

Remaining appendix editorial debt after this pass:

- 13 remaining card-derived blocks.
- 9 remaining working-index skeleton phrases.

## Next Step

Finish the appendix editorial consolidation with Logia 101-114. This is the final appendix package and should also prepare the project for evidence dossier publication polish, because it includes high-impact exclusions and deferred units such as 101, 104, 109, 110, 111, 112, 113, and 114.
