# Full Appendix Editorial Consolidation, Logia 81-90 v0.1

Date: 2026-07-18

## Scope

This pass continues print-safe publication-level editorial consolidation of:

- `reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-uk.md`

Edited appendix chapters:

- Logia 81-90

Prompt executed:

- `project/ide-codex-full-appendix-editorial-consolidation-081-090-v0.1-prompt.md`

## Plan Executed

1. Preserve all current clean-reader and appendix-only decisions.
2. Rewrite Logia 81-90 as integrated Ukrainian reader-facing appendix entries.
3. Preserve Logia 86 and 89 as the only clean-reader units in this package.
4. Keep Logia 81, 83, 84, 85, 87, and 88 cluster-bound or deferred.
5. Keep Logia 82 and 90 appendix-only despite strong interpretive interest.
6. Use print-safe source labels in prose and keep repository paths only in `### Джерела й контрольні файли`.
7. Update active project documentation and task queue.
8. Rerun structural QA.

## What Changed

- Removed separate `### Читацьке тлумачення з картки` blocks from Logia 81-90.
- Removed working-index navigation prose from Logia 81-90.
- Rewrote the sections as coherent print-facing commentary with:
  - status in the reconstruction;
  - reader-facing explanation;
  - inclusion/non-inclusion rationale;
  - possible interpretations;
  - uncertainty and limits;
  - print-facing source summary;
  - digital apparatus paths.
- Clarified why Logion 81 remains wealth/renunciation cluster material rather than a clean-reader saying.
- Integrated the technical control packages for Logia 83-85, 87/112, and 88 into reader-facing Ukrainian prose.
- Clarified that Logia 86 and 89 are included with markers because their controls are strong but Greek Thomas witnesses are not extant in the loaded corpus.
- Clarified why Logion 90 remains appendix-only despite high early pressure: Matthew 11:28-30 dominates the evidence.

## Editorial Decisions Preserved

| Logion | Decision after this pass |
| ---: | --- |
| 81 | Remains `DEFER_TO_CLUSTER`; wealth/power/renunciation logic unresolved without cluster decision. |
| 82 | Remains `APPENDIX_ONLY_UNCERTAIN`; important fire/kingdom appendix material, no clean-reader promotion. |
| 83 | Remains `DEFER_TO_CLUSTER`; image/light anthropology is internally coherent but externally undercontrolled. |
| 84 | Remains `DEFER_TO_CLUSTER`; preexistent-images language remains appendix-only. |
| 85 | Remains `DEFER_TO_CLUSTER`; Adam/deathlessness reflection remains appendix-only. |
| 86 | Remains `INCLUDE_WITH_MARKER`; foxes/birds/Son of Man homelessness core stays in clean reader. |
| 87 | Remains `DEFER_TO_CLUSTER`; body/soul dependence language remains appendix-only. |
| 88 | Remains `DEFER_TO_CLUSTER`; revelation/transmission language remains appendix-only. |
| 89 | Remains `INCLUDE_WITH_MARKER`; cup inside/outside core stays in clean reader with Luke-dependence warning. |
| 90 | Remains `KEEP_APPENDIX_ONLY_FOR_NOW`; rest/yoke saying remains appendix-only because of Matthew-dependence risk. |

## Verification

Post-pass checks:

- `python3 tools/qa_crosscheck.py` passes.
- Appendix logion headings remain 114/114.
- `### Джерела й контрольні файли` sections remain 114/114.
- Clean-reader set remains 37/37 synchronized across language layers and control tables.
- No target section from Logia 81-90 contains `### Читацьке тлумачення з картки`.
- No target section from Logia 81-90 contains working-index navigation prose.

Remaining appendix editorial debt after this pass:

- 22 remaining card-derived blocks.
- 14 remaining working-index skeleton phrases.

## Next Step

Continue the same print-safe editorial consolidation pattern for Logia 91-100. That range includes a mixed group: Logion 91A in the clean reader, seek/find appendix controls for 92 and 94, several appendix-only guarded sayings, and clean-reader units 95, 96, 99, and 100. It should preserve the current 37-unit clean-reader set unless a separate controlled decision pass changes it.
