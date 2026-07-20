# Full Appendix Editorial Consolidation, Logia 71-80 v0.1

Date: 2026-07-18

## Scope

This pass continues print-safe publication-level editorial consolidation of:

- `reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-uk.md`

Edited appendix chapters:

- Logia 71-80

Prompt executed:

- `project/ide-codex-full-appendix-editorial-consolidation-071-080-v0.1-prompt.md`

## Plan Executed

1. Preserve all current clean-reader and appendix-only decisions.
2. Rewrite Logia 71-80 as integrated Ukrainian reader-facing appendix entries.
3. Preserve Logia 72 and 73 as the only clean-reader units in this package.
4. Keep Logia 71, 74, 75, 77, and 80 deferred or cluster-bound.
5. Keep Logia 76, 78, and 79 appendix-only despite strong controls because their current Thomas forms remain composite or dependence-risky.
6. Use print-safe source labels in prose and keep repository paths only in `### Джерела й контрольні файли`.
7. Update active project documentation and task queue.
8. Rerun structural QA.

## What Changed

- Removed separate `### Читацьке тлумачення з картки` blocks from Logia 71-80.
- Removed working-index navigation prose from Logia 71-80.
- Rewrote the sections as coherent print-facing commentary with:
  - status in the reconstruction;
  - reader-facing explanation;
  - inclusion/non-inclusion rationale;
  - possible interpretations;
  - uncertainty and limits;
  - print-facing source summary;
  - digital apparatus paths.
- Clarified that P.Oxy. 1 supports only the 77b stone/wood unit, not the full Coptic Logion 77.
- Clarified Luke-dependence risk for Logion 72 and Matthew/Luke mission-formula control for Logion 73.

## Editorial Decisions Preserved

| Logion | Decision after this pass |
| ---: | --- |
| 71 | Remains `DEFER_TO_CLUSTER`; house-destruction referent unresolved. |
| 72 | Remains `INCLUDE_WITH_MARKER`; inheritance-dispute refusal core printed with Luke-dependence warning. |
| 73 | Remains `INCLUDE_WITH_MARKER`; harvest/workers formula printed with Matthew/Luke controls. |
| 74 | Remains `DEFER_TO_CLUSTER`; water/well/access image lacks direct control. |
| 75 | Remains `DEFER_TO_CLUSTER`; `monachos` and bridal-chamber language remain Thomasine caution markers. |
| 76 | Remains `APPENDIX_ONLY_STABLE`; pearl and imperishable-treasure subunits need split-core review before any promotion. |
| 77 | Remains `DEFER_TO_CLUSTER`; full light/all form appendix-only, 77b remains high-priority split-core candidate. |
| 78 | Remains `APPENDIX_ONLY_STABLE`; wilderness/reed core strong, truth/soft-clothing ending not clean enough. |
| 79 | Remains `APPENDIX_ONLY_STABLE`; hearing/keeping core embedded in composite Lukan-like sequence. |
| 80 | Remains `DEFER_TO_CLUSTER`; living/dead/world and body/world cluster material. |

## Verification

Post-pass checks:

- `python3 tools/qa_crosscheck.py` passes.
- Appendix logion headings remain 114/114.
- `### Джерела й контрольні файли` sections remain 114/114.
- Clean-reader set remains 37/37 synchronized across language layers and control tables.
- No target section from Logia 71-80 contains `### Читацьке тлумачення з картки`.
- No target section from Logia 71-80 contains working-index navigation prose.

## Next Step

Continue the same print-safe editorial consolidation pattern for Logia 81-90. That range includes wealth/renunciation, image/preexistence, body-soul, revelation/transmission, and appendix-only high-early pressure material. It should be handled carefully because several logia have new technical control packages and because Logion 89 is included in the clean reader.
