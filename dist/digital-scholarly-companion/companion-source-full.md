# EUAGELIA Digital Scholarly Companion

Status: expanded digital scholarly companion v0.1, 2026-07-19.

## How To Use This Companion

This companion is the digital research layer behind the Ukrainian and English paper books. The paper books are intentionally clean and print-safe; this file intentionally preserves repository paths, evidence notes, source snapshots, control files, checksums, and audit history.

For a normal reading experience, start with the paper books. For verification, start here and move logion by logion: card -> evidence note -> control files -> source witness inventory -> publication decision table.

## Generated Machine Indexes

- `dist/digital-scholarly-companion/logion-cross-reference-index.tsv` - all 114 logia with cards, evidence notes, controls, decisions, Greek status, and next actions.
- `dist/digital-scholarly-companion/source-witness-inventory.tsv` - local source corpus inventory with categories and SHA256 checksums.
- `dist/digital-scholarly-companion/artifact-checksums.tsv` - checksums for core publication artifacts and paper proofs.
- `dist/digital-scholarly-companion/audit-trail-index.tsv` - major audit/pass/review files with checksums.

## Clean-Reader Manifest

The frozen clean reader contains 36 printed units. Reader membership is controlled by `research/audits/final-clean-reader-freeze-v0.1.md` and synchronized by `build/scripts/qa_crosscheck.py`.

| Layer | Path | Role |
| --- | --- | --- |
| Ukrainian clean reader | `book/text/logia-uk.md` | First paper-reader layer. |
| English clean reader | `book/text/logia-en.md` | English paper-reader layer. |
| Coptic reader layer | `book/translations/coptic.md` | Coptic source-facing layer for included units. |
| Greek reader layer | `book/translations/greek.md` | Extant Greek plus clearly marked hypothetical retroversions. |
| Arabic literary layer | `book/translations/arabic-quranic-register.md` | Literary/theological reception layer, not a source witness. |
| Parallel edition | `book/translations/parallel-edition.md` | Synchronized multilingual view of the frozen reader. |

## All-114 Logion Research Index

Each row links the core card and the currently known evidence/control apparatus. `Reader text = YES` means the logion or a marked core appears in the clean reader; it does not mean unqualified certainty.

| Logion | Reader | Decision | Greek status | Card | Evidence | Controls |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | NO | `APPENDIX_ONLY_STABLE` | P.Oxy. 654 | [`research\logion-cards\logion-001.md`](../../research\logion-cards\logion-001.md) | [`research\evidence\notes\logion-001-evidence-en.md`](../../research\evidence\notes\logion-001-evidence-en.md) | None recorded |
| 2 | YES | `INCLUDE_WITH_MARKER` | P.Oxy. 654 | [`research\logion-cards\logion-002.md`](../../research\logion-cards\logion-002.md) | [`research\evidence\notes\logion-002-evidence-en.md`](../../research\evidence\notes\logion-002-evidence-en.md) | None recorded |
| 3 | YES | `INCLUDE_WITH_MARKER` | P.Oxy. 654 | [`research\logion-cards\logion-003.md`](../../research\logion-cards\logion-003.md) | [`research\evidence\notes\logion-003-evidence-en.md`](../../research\evidence\notes\logion-003-evidence-en.md) | None recorded |
| 4 | YES | `INCLUDE_WITH_MARKER` | P.Oxy. 654 | [`research\logion-cards\logion-004.md`](../../research\logion-cards\logion-004.md) | [`research\evidence\notes\logion-004-evidence-en.md`](../../research\evidence\notes\logion-004-evidence-en.md) | None recorded |
| 5 | YES | `INCLUDE_WITH_MARKER` | P.Oxy. 654 | [`research\logion-cards\logion-005.md`](../../research\logion-cards\logion-005.md) | [`research\evidence\notes\logion-005-evidence-en.md`](../../research\evidence\notes\logion-005-evidence-en.md) | None recorded |
| 6 | YES | `INCLUDE_WITH_MARKER` for ethical core; full logion `UNCERTAIN` | P.Oxy. 654, lacunose | [`research\logion-cards\logion-006.md`](../../research\logion-cards\logion-006.md) | [`research\evidence\notes\logion-006-evidence-en.md`](../../research\evidence\notes\logion-006-evidence-en.md) | None recorded |
| 7 | NO | `UNCERTAIN` | P.Oxy. 654 | [`research\logion-cards\logion-007.md`](../../research\logion-cards\logion-007.md) | [`research\evidence\notes\logion-007-evidence-en.md`](../../research\evidence\notes\logion-007-evidence-en.md) | None recorded |
| 8 | NO | `UNCERTAIN` | No loaded P.Oxy. witness | [`research\logion-cards\logion-008.md`](../../research\logion-cards\logion-008.md) | [`research\evidence\notes\logion-008-evidence-en.md`](../../research\evidence\notes\logion-008-evidence-en.md) | None recorded |
| 9 | YES | sower core `INCLUDE_WITH_MARKER`; full logion `UNCERTAIN` | Greek retroversion, hypothetical | [`research\logion-cards\logion-009.md`](../../research\logion-cards\logion-009.md) | [`research\evidence\notes\logion-009-evidence-en.md`](../../research\evidence\notes\logion-009-evidence-en.md) | None recorded |
| 10 | YES | fire-casting core `INCLUDE_WITH_MARKER`; full logion `UNCERTAIN` | Greek retroversion, hypothetical | [`research\logion-cards\logion-010.md`](../../research\logion-cards\logion-010.md) | [`research\evidence\notes\logion-010-evidence-en.md`](../../research\evidence\notes\logion-010-evidence-en.md) | None recorded |
| 11 | NO | `UNCERTAIN` | Greek retroversion, hypothetical | [`research\logion-cards\logion-011.md`](../../research\logion-cards\logion-011.md) | [`research\evidence\notes\logion-011-evidence-en.md`](../../research\evidence\notes\logion-011-evidence-en.md) | None recorded |
| 12 | NO | `DEFER` | No loaded P.Oxy. witness | [`research\logion-cards\logion-012.md`](../../research\logion-cards\logion-012.md) | [`research\evidence\notes\logion-012-evidence-en.md`](../../research\evidence\notes\logion-012-evidence-en.md) | None recorded |
| 13 | NO | `DEFER` | No loaded P.Oxy. witness | [`research\logion-cards\logion-013.md`](../../research\logion-cards\logion-013.md) | [`research\evidence\notes\logion-013-evidence-en.md`](../../research\evidence\notes\logion-013-evidence-en.md) | None recorded |
| 14 | NO | `DEFER` | Greek retroversion, hypothetical | [`research\logion-cards\logion-014.md`](../../research\logion-cards\logion-014.md) | [`research\evidence\notes\logion-014-evidence-en.md`](../../research\evidence\notes\logion-014-evidence-en.md) | None recorded |
| 15 | NO | `DEFER` | No loaded P.Oxy. witness | [`research\logion-cards\logion-015.md`](../../research\logion-cards\logion-015.md) | [`research\evidence\notes\logion-015-evidence-en.md`](../../research\evidence\notes\logion-015-evidence-en.md) | None recorded |
| 16 | YES | division/household core `INCLUDE_WITH_MARKER`; full logion `UNCERTAIN` | Greek retroversion, hypothetical | [`research\logion-cards\logion-016.md`](../../research\logion-cards\logion-016.md) | [`research\evidence\notes\logion-016-evidence-en.md`](../../research\evidence\notes\logion-016-evidence-en.md) | None recorded |
| 17 | NO | `UNCERTAIN` | No loaded P.Oxy. witness | [`research\logion-cards\logion-017.md`](../../research\logion-cards\logion-017.md) | [`research\evidence\notes\logion-017-evidence-en.md`](../../research\evidence\notes\logion-017-evidence-en.md) | None recorded |
| 18 | NO | `UNCERTAIN` | No loaded P.Oxy. witness | [`research\logion-cards\logion-018.md`](../../research\logion-cards\logion-018.md) | [`research\evidence\notes\logion-018-evidence-en.md`](../../research\evidence\notes\logion-018-evidence-en.md) | None recorded |
| 19 | NO | `DEFER` | No loaded P.Oxy. witness | [`research\logion-cards\logion-019.md`](../../research\logion-cards\logion-019.md) | [`research\evidence\notes\logion-019-evidence-en.md`](../../research\evidence\notes\logion-019-evidence-en.md) | None recorded |
| 20 | YES | `INCLUDE_WITH_MARKER` | Greek retroversion, hypothetical | [`research\logion-cards\logion-020.md`](../../research\logion-cards\logion-020.md) | [`research\evidence\notes\logion-020-branch-tree-commentary-check-en.md`](../../research\evidence\notes\logion-020-branch-tree-commentary-check-en.md), [`research\evidence\notes\logion-020-evidence-en.md`](../../research\evidence\notes\logion-020-evidence-en.md) | None recorded |
| 21 | NO | `DEFER_TO_CLUSTER`; thief subunit control material | No loaded P.Oxy. witness | [`research\logion-cards\logion-021.md`](../../research\logion-cards\logion-021.md) | [`research\evidence\notes\logion-021-evidence-en.md`](../../research\evidence\notes\logion-021-evidence-en.md) | None recorded |
| 22 | YES | children/kingdom core `INCLUDE_WITH_MARKER`; full logion `UNCERTAIN` | Greek retroversion, hypothetical | [`research\logion-cards\logion-022.md`](../../research\logion-cards\logion-022.md) | [`research\evidence\notes\logion-022-evidence-en.md`](../../research\evidence\notes\logion-022-evidence-en.md) | None recorded |
| 23 | NO | `UNCERTAIN` | No loaded P.Oxy. witness | [`research\logion-cards\logion-023.md`](../../research\logion-cards\logion-023.md) | [`research\evidence\notes\logion-023-evidence-en.md`](../../research\evidence\notes\logion-023-evidence-en.md) | None recorded |
| 24 | NO | `DEFER` | P.Oxy. 655 possible/uncertain | [`research\logion-cards\logion-024.md`](../../research\logion-cards\logion-024.md) | [`research\evidence\notes\logion-024-evidence-en.md`](../../research\evidence\notes\logion-024-evidence-en.md) | None recorded |
| 25 | YES | `INCLUDE_WITH_MARKER` | Greek retroversion, hypothetical | [`research\logion-cards\logion-025.md`](../../research\logion-cards\logion-025.md) | [`research\evidence\notes\logion-025-evidence-en.md`](../../research\evidence\notes\logion-025-evidence-en.md) | None recorded |
| 26 | YES | `INCLUDE_WITH_MARKER` | P.Oxy. 1 partial | [`research\logion-cards\logion-026.md`](../../research\logion-cards\logion-026.md) | [`research\evidence\notes\logion-026-evidence-en.md`](../../research\evidence\notes\logion-026-evidence-en.md) | None recorded |
| 27 | NO | `UNCERTAIN` | P.Oxy. 1; P.Oxy. 5575 control | [`research\logion-cards\logion-027.md`](../../research\logion-cards\logion-027.md) | [`research\evidence\notes\logion-027-evidence-en.md`](../../research\evidence\notes\logion-027-evidence-en.md) | None recorded |
| 28 | NO | `UNCERTAIN` | P.Oxy. 1 partial | [`research\logion-cards\logion-028.md`](../../research\logion-cards\logion-028.md) | [`research\evidence\notes\logion-028-evidence-en.md`](../../research\evidence\notes\logion-028-evidence-en.md) | None recorded |
| 29 | NO | `DEFER` | P.Oxy. 1 tiny fragment | [`research\logion-cards\logion-029.md`](../../research\logion-cards\logion-029.md) | [`research\evidence\notes\logion-029-evidence-en.md`](../../research\evidence\notes\logion-029-evidence-en.md) | None recorded |
| 30 | NO | `UNCERTAIN` | P.Oxy. 1, textually complex with 77b | [`research\logion-cards\logion-030.md`](../../research\logion-cards\logion-030.md) | [`research\evidence\notes\logion-030-evidence-en.md`](../../research\evidence\notes\logion-030-evidence-en.md) | None recorded |
| 31 | YES | `INCLUDE_WITH_MARKER` | P.Oxy. 1 | [`research\logion-cards\logion-031.md`](../../research\logion-cards\logion-031.md) | [`research\evidence\notes\logion-031-evidence-en.md`](../../research\evidence\notes\logion-031-evidence-en.md) | None recorded |
| 32 | YES | `INCLUDE_WITH_MARKER` | P.Oxy. 1 | [`research\logion-cards\logion-032.md`](../../research\logion-cards\logion-032.md) | [`research\evidence\notes\logion-032-evidence-en.md`](../../research\evidence\notes\logion-032-evidence-en.md) | None recorded |
| 33 | YES | `INCLUDE_WITH_MARKER` | P.Oxy. 1 opening only | [`research\logion-cards\logion-033.md`](../../research\logion-cards\logion-033.md) | [`research\evidence\notes\logion-033-evidence-en.md`](../../research\evidence\notes\logion-033-evidence-en.md) | None recorded |
| 34 | YES | `INCLUDE_WITH_MARKER` | Greek retroversion, hypothetical | [`research\logion-cards\logion-034.md`](../../research\logion-cards\logion-034.md) | [`research\evidence\notes\logion-034-evidence-en.md`](../../research\evidence\notes\logion-034-evidence-en.md) | None recorded |
| 35 | YES | `INCLUDE_WITH_MARKER` | Greek retroversion, hypothetical | [`research\logion-cards\logion-035.md`](../../research\logion-cards\logion-035.md) | [`research\evidence\notes\logion-035-evidence-en.md`](../../research\evidence\notes\logion-035-evidence-en.md) | None recorded |
| 36 | YES | `INCLUDE_WITH_MARKER` | P.Oxy. 655; P.Oxy. 5575 control | [`research\logion-cards\logion-036.md`](../../research\logion-cards\logion-036.md) | [`research\evidence\notes\logion-036-evidence-en.md`](../../research\evidence\notes\logion-036-evidence-en.md) | None recorded |
| 37 | NO | `UNCERTAIN` | P.Oxy. 655 | [`research\logion-cards\logion-037.md`](../../research\logion-cards\logion-037.md) | [`research\evidence\notes\logion-037-evidence-en.md`](../../research\evidence\notes\logion-037-evidence-en.md) | None recorded |
| 38 | NO | `UNCERTAIN` | P.Oxy. 655 fragmentary | [`research\logion-cards\logion-038.md`](../../research\logion-cards\logion-038.md) | [`research\evidence\notes\logion-038-evidence-en.md`](../../research\evidence\notes\logion-038-evidence-en.md) | None recorded |
| 39 | YES | `INCLUDE_WITH_MARKER` | P.Oxy. 655 | [`research\logion-cards\logion-039.md`](../../research\logion-cards\logion-039.md) | [`research\evidence\notes\logion-039-evidence-en.md`](../../research\evidence\notes\logion-039-evidence-en.md) | None recorded |
| 40 | NO | `UNCERTAIN` | No loaded P.Oxy. witness | [`research\logion-cards\logion-040.md`](../../research\logion-cards\logion-040.md) | [`research\evidence\notes\logion-040-evidence-en.md`](../../research\evidence\notes\logion-040-evidence-en.md) | None recorded |
| 41 | YES | `INCLUDE_WITH_MARKER` | No loaded P.Oxy. witness | [`research\logion-cards\logion-041.md`](../../research\logion-cards\logion-041.md) | [`research\evidence\notes\logion-041-evidence-en.md`](../../research\evidence\notes\logion-041-evidence-en.md) | None recorded |
| 42 | NO | `UNCERTAIN` | No loaded P.Oxy. witness | [`research\logion-cards\logion-042.md`](../../research\logion-cards\logion-042.md) | [`research\evidence\notes\logion-042-evidence-en.md`](../../research\evidence\notes\logion-042-evidence-en.md) | None recorded |
| 43 | NO | `DEFER` | No loaded P.Oxy. witness | [`research\logion-cards\logion-043.md`](../../research\logion-cards\logion-043.md) | [`research\evidence\notes\logion-043-evidence-en.md`](../../research\evidence\notes\logion-043-evidence-en.md) | None recorded |
| 44 | NO | `UNCERTAIN` | No loaded P.Oxy. witness | [`research\logion-cards\logion-044.md`](../../research\logion-cards\logion-044.md) | [`research\evidence\notes\logion-044-evidence-en.md`](../../research\evidence\notes\logion-044-evidence-en.md) | None recorded |
| 45 | YES | 45A `INCLUDE_WITH_MARKER`; 45B `KEEP_APPENDIX_ONLY_FOR_NOW`; full logion `UNCERTAIN` | Greek retroversion, hypothetical | [`research\logion-cards\logion-045.md`](../../research\logion-cards\logion-045.md) | [`research\evidence\notes\logion-045-evidence-en.md`](../../research\evidence\notes\logion-045-evidence-en.md) | None recorded |
| 46 | YES | 46A `INCLUDE_WITH_MARKER`; full logion appendix-only | Greek retroversion, hypothetical; no loaded P.Oxy. witness | [`research\logion-cards\logion-046.md`](../../research\logion-cards\logion-046.md) | [`research\evidence\notes\logion-046-evidence-en.md`](../../research\evidence\notes\logion-046-evidence-en.md) | None recorded |
| 47 | YES | 47B `INCLUDE_WITH_MARKER`; full logion `UNCERTAIN` | Greek retroversion, hypothetical | [`research\logion-cards\logion-047.md`](../../research\logion-cards\logion-047.md) | [`research\evidence\notes\logion-047-evidence-en.md`](../../research\evidence\notes\logion-047-evidence-en.md) | None recorded |
| 48 | NO | `UNCERTAIN` | No loaded P.Oxy. witness | [`research\logion-cards\logion-048.md`](../../research\logion-cards\logion-048.md) | [`research\evidence\notes\logion-048-evidence-en.md`](../../research\evidence\notes\logion-048-evidence-en.md) | None recorded |
| 49 | NO | `UNCERTAIN` | No loaded P.Oxy. witness | [`research\logion-cards\logion-049.md`](../../research\logion-cards\logion-049.md) | [`research\evidence\notes\logion-049-evidence-en.md`](../../research\evidence\notes\logion-049-evidence-en.md) | None recorded |
| 50 | NO | `UNCERTAIN` | No loaded P.Oxy. witness | [`research\logion-cards\logion-050.md`](../../research\logion-cards\logion-050.md) | [`research\evidence\notes\logion-050-evidence-en.md`](../../research\evidence\notes\logion-050-evidence-en.md) | None recorded |
| 51 | NO | `UNCERTAIN` | No loaded P.Oxy. witness | [`research\logion-cards\logion-051.md`](../../research\logion-cards\logion-051.md) | [`research\evidence\notes\logion-051-evidence-en.md`](../../research\evidence\notes\logion-051-evidence-en.md) | None recorded |
| 52 | NO | `UNCERTAIN` | No loaded P.Oxy. witness | [`research\logion-cards\logion-052.md`](../../research\logion-cards\logion-052.md) | [`research\evidence\notes\logion-052-evidence-en.md`](../../research\evidence\notes\logion-052-evidence-en.md) | None recorded |
| 53 | NO | `DEFER` | No loaded P.Oxy. witness | [`research\logion-cards\logion-053.md`](../../research\logion-cards\logion-053.md) | [`research\evidence\notes\logion-053-evidence-en.md`](../../research\evidence\notes\logion-053-evidence-en.md) | None recorded |
| 54 | YES | `INCLUDE_WITH_MARKER` | No loaded P.Oxy. witness | [`research\logion-cards\logion-054.md`](../../research\logion-cards\logion-054.md) | [`research\evidence\notes\logion-054-evidence-en.md`](../../research\evidence\notes\logion-054-evidence-en.md) | None recorded |
| 55 | NO | `UNCERTAIN` | No loaded P.Oxy. witness | [`research\logion-cards\logion-055.md`](../../research\logion-cards\logion-055.md) | [`research\evidence\notes\logion-055-evidence-en.md`](../../research\evidence\notes\logion-055-evidence-en.md) | None recorded |
| 56 | NO | `UNCERTAIN` | No loaded P.Oxy. witness | [`research\logion-cards\logion-056.md`](../../research\logion-cards\logion-056.md) | [`research\evidence\notes\logion-056-evidence-en.md`](../../research\evidence\notes\logion-056-evidence-en.md) | None recorded |
| 57 | NO | `UNCERTAIN` | No loaded P.Oxy. witness | [`research\logion-cards\logion-057.md`](../../research\logion-cards\logion-057.md) | [`research\evidence\notes\logion-057-evidence-en.md`](../../research\evidence\notes\logion-057-evidence-en.md) | None recorded |
| 58 | NO | `UNCERTAIN` | No loaded P.Oxy. witness | [`research\logion-cards\logion-058.md`](../../research\logion-cards\logion-058.md) | [`research\evidence\notes\logion-058-evidence-en.md`](../../research\evidence\notes\logion-058-evidence-en.md) | None recorded |
| 59 | NO | `UNCERTAIN` | No loaded P.Oxy. witness | [`research\logion-cards\logion-059.md`](../../research\logion-cards\logion-059.md) | [`research\evidence\notes\logion-059-evidence-en.md`](../../research\evidence\notes\logion-059-evidence-en.md) | None recorded |
| 60 | NO | `UNCERTAIN` | No loaded P.Oxy. witness | [`research\logion-cards\logion-060.md`](../../research\logion-cards\logion-060.md) | [`research\evidence\notes\logion-060-evidence-en.md`](../../research\evidence\notes\logion-060-evidence-en.md) | None recorded |
| 61 | NO | `DEFER` | No loaded P.Oxy. witness | [`research\logion-cards\logion-061.md`](../../research\logion-cards\logion-061.md) | [`research\evidence\notes\logion-061-evidence-en.md`](../../research\evidence\notes\logion-061-evidence-en.md) | None recorded |
| 62 | NO | `UNCERTAIN` | No loaded P.Oxy. witness | [`research\logion-cards\logion-062.md`](../../research\logion-cards\logion-062.md) | [`research\evidence\notes\logion-062-evidence-en.md`](../../research\evidence\notes\logion-062-evidence-en.md) | None recorded |
| 63 | YES | `INCLUDE_WITH_MARKER`; full logion `UNCERTAIN` | Greek retroversion, hypothetical | [`research\logion-cards\logion-063.md`](../../research\logion-cards\logion-063.md) | [`research\evidence\notes\logion-063-evidence-en.md`](../../research\evidence\notes\logion-063-evidence-en.md) | None recorded |
| 64 | NO | 64A/64B `KEEP_APPENDIX_ONLY_FOR_NOW` | No loaded P.Oxy. witness | [`research\logion-cards\logion-064.md`](../../research\logion-cards\logion-064.md) | [`research\evidence\notes\logion-064-evidence-en.md`](../../research\evidence\notes\logion-064-evidence-en.md) | None recorded |
| 65 | NO | `KEEP_APPENDIX_ONLY_FOR_NOW` | No loaded P.Oxy. witness | [`research\logion-cards\logion-065.md`](../../research\logion-cards\logion-065.md) | [`research\evidence\notes\logion-065-066-evidence-en.md`](../../research\evidence\notes\logion-065-066-evidence-en.md) | None recorded |
| 66 | NO | `KEEP_APPENDIX_ONLY_FOR_NOW` | No loaded P.Oxy. witness | [`research\logion-cards\logion-066.md`](../../research\logion-cards\logion-066.md) | [`research\evidence\notes\logion-065-066-evidence-en.md`](../../research\evidence\notes\logion-065-066-evidence-en.md) | None recorded |
| 67 | NO | `UNCERTAIN` | No loaded P.Oxy. witness | [`research\logion-cards\logion-067.md`](../../research\logion-cards\logion-067.md) | [`research\evidence\notes\logion-067-evidence-en.md`](../../research\evidence\notes\logion-067-evidence-en.md) | None recorded |
| 68 | NO | `UNCERTAIN` | No loaded P.Oxy. witness | [`research\logion-cards\logion-068.md`](../../research\logion-cards\logion-068.md) | [`research\evidence\notes\logion-068-evidence-en.md`](../../research\evidence\notes\logion-068-evidence-en.md) | None recorded |
| 69 | NO | `UNCERTAIN` | No loaded P.Oxy. witness | [`research\logion-cards\logion-069.md`](../../research\logion-cards\logion-069.md) | [`research\evidence\notes\logion-069-evidence-en.md`](../../research\evidence\notes\logion-069-evidence-en.md) | None recorded |
| 70 | NO | `DEFER` | No loaded P.Oxy. witness | [`research\logion-cards\logion-070.md`](../../research\logion-cards\logion-070.md) | [`research\evidence\notes\logion-070-evidence-en.md`](../../research\evidence\notes\logion-070-evidence-en.md) | None recorded |
| 71 | NO | `DEFER` | No loaded P.Oxy. witness | [`research\logion-cards\logion-071.md`](../../research\logion-cards\logion-071.md) | [`research\evidence\notes\logion-071-evidence-en.md`](../../research\evidence\notes\logion-071-evidence-en.md) | None recorded |
| 72 | YES | `INCLUDE_WITH_MARKER` | No loaded P.Oxy. witness | [`research\logion-cards\logion-072.md`](../../research\logion-cards\logion-072.md) | [`research\evidence\notes\logion-072-evidence-en.md`](../../research\evidence\notes\logion-072-evidence-en.md) | None recorded |
| 73 | YES | `INCLUDE_WITH_MARKER` | No loaded P.Oxy. witness | [`research\logion-cards\logion-073.md`](../../research\logion-cards\logion-073.md) | [`research\evidence\notes\logion-073-evidence-en.md`](../../research\evidence\notes\logion-073-evidence-en.md) | None recorded |
| 74 | NO | `DEFER` | No loaded P.Oxy. witness | [`research\logion-cards\logion-074.md`](../../research\logion-cards\logion-074.md) | [`research\evidence\notes\logion-074-evidence-en.md`](../../research\evidence\notes\logion-074-evidence-en.md) | None recorded |
| 75 | NO | `DEFER` | No loaded P.Oxy. witness | [`research\logion-cards\logion-075.md`](../../research\logion-cards\logion-075.md) | [`research\evidence\notes\logion-075-evidence-en.md`](../../research\evidence\notes\logion-075-evidence-en.md) | None recorded |
| 76 | NO | `KEEP_APPENDIX_ONLY_FOR_NOW` | No loaded P.Oxy. witness | [`research\logion-cards\logion-076.md`](../../research\logion-cards\logion-076.md) | [`research\evidence\notes\logion-076-evidence-en.md`](../../research\evidence\notes\logion-076-evidence-en.md) | None recorded |
| 77 | NO | `DEFER` | P.Oxy. 1 overlap for 77b only | [`research\logion-cards\logion-077.md`](../../research\logion-cards\logion-077.md) | [`research\evidence\notes\logion-077-evidence-en.md`](../../research\evidence\notes\logion-077-evidence-en.md) | None recorded |
| 78 | NO | `KEEP_APPENDIX_ONLY_FOR_NOW` | No loaded P.Oxy. witness | [`research\logion-cards\logion-078.md`](../../research\logion-cards\logion-078.md) | [`research\evidence\notes\logion-078-evidence-en.md`](../../research\evidence\notes\logion-078-evidence-en.md) | None recorded |
| 79 | NO | `KEEP_APPENDIX_ONLY_FOR_NOW` | No loaded P.Oxy. witness | [`research\logion-cards\logion-079.md`](../../research\logion-cards\logion-079.md) | [`research\evidence\notes\logion-079-evidence-en.md`](../../research\evidence\notes\logion-079-evidence-en.md) | None recorded |
| 80 | NO | `DEFER` | No loaded P.Oxy. witness | [`research\logion-cards\logion-080.md`](../../research\logion-cards\logion-080.md) | [`research\evidence\notes\logion-080-evidence-en.md`](../../research\evidence\notes\logion-080-evidence-en.md) | None recorded |
| 81 | NO | `DEFER_TO_CLUSTER` | No loaded P.Oxy. witness | [`research\logion-cards\logion-081.md`](../../research\logion-cards\logion-081.md) | [`research\evidence\notes\logion-081-evidence-en.md`](../../research\evidence\notes\logion-081-evidence-en.md) | None recorded |
| 82 | NO | `APPENDIX_ONLY_UNCERTAIN` | No loaded P.Oxy. witness | [`research\logion-cards\logion-082.md`](../../research\logion-cards\logion-082.md) | [`research\evidence\notes\logion-082-evidence-en.md`](../../research\evidence\notes\logion-082-evidence-en.md) | None recorded |
| 83 | NO | `DEFER` | No loaded P.Oxy. witness | [`research\logion-cards\logion-083.md`](../../research\logion-cards\logion-083.md) | [`research\evidence\notes\logion-083-evidence-en.md`](../../research\evidence\notes\logion-083-evidence-en.md) | None recorded |
| 84 | NO | `DEFER` | No loaded P.Oxy. witness | [`research\logion-cards\logion-084.md`](../../research\logion-cards\logion-084.md) | [`research\evidence\notes\logion-084-evidence-en.md`](../../research\evidence\notes\logion-084-evidence-en.md) | None recorded |
| 85 | NO | `DEFER` | No loaded P.Oxy. witness | [`research\logion-cards\logion-085.md`](../../research\logion-cards\logion-085.md) | [`research\evidence\notes\logion-085-evidence-en.md`](../../research\evidence\notes\logion-085-evidence-en.md) | None recorded |
| 86 | YES | `INCLUDE_WITH_MARKER` | Greek retroversion, hypothetical | [`research\logion-cards\logion-086.md`](../../research\logion-cards\logion-086.md) | [`research\evidence\notes\logion-086-evidence-en.md`](../../research\evidence\notes\logion-086-evidence-en.md) | None recorded |
| 87 | NO | `DEFER` | No loaded P.Oxy. witness | [`research\logion-cards\logion-087.md`](../../research\logion-cards\logion-087.md) | [`research\evidence\notes\logion-087-evidence-en.md`](../../research\evidence\notes\logion-087-evidence-en.md) | None recorded |
| 88 | NO | `DEFER` | No loaded P.Oxy. witness | [`research\logion-cards\logion-088.md`](../../research\logion-cards\logion-088.md) | [`research\evidence\notes\logion-088-evidence-en.md`](../../research\evidence\notes\logion-088-evidence-en.md) | None recorded |
| 89 | YES | `INCLUDE_WITH_MARKER` | Greek retroversion, hypothetical | [`research\logion-cards\logion-089.md`](../../research\logion-cards\logion-089.md) | [`research\evidence\notes\logion-089-evidence-en.md`](../../research\evidence\notes\logion-089-evidence-en.md) | None recorded |
| 90 | NO | `KEEP_APPENDIX_ONLY_FOR_NOW` | Greek retroversion, hypothetical | [`research\logion-cards\logion-090.md`](../../research\logion-cards\logion-090.md) | [`research\evidence\notes\logion-090-evidence-en.md`](../../research\evidence\notes\logion-090-evidence-en.md) | None recorded |
| 91 | YES | 91A `INCLUDE_WITH_MARKER`; full logion appendix-only | Greek retroversion, hypothetical | [`research\logion-cards\logion-091.md`](../../research\logion-cards\logion-091.md) | [`research\evidence\notes\logion-091-evidence-en.md`](../../research\evidence\notes\logion-091-evidence-en.md) | None recorded |
| 92 | NO | `UNCERTAIN` | Greek retroversion, hypothetical | [`research\logion-cards\logion-092.md`](../../research\logion-cards\logion-092.md) | [`research\evidence\notes\logion-092-evidence-en.md`](../../research\evidence\notes\logion-092-evidence-en.md) | None recorded |
| 93 | NO | `UNCERTAIN` | Greek retroversion, hypothetical | [`research\logion-cards\logion-093.md`](../../research\logion-cards\logion-093.md) | [`research\evidence\notes\logion-093-evidence-en.md`](../../research\evidence\notes\logion-093-evidence-en.md) | None recorded |
| 94 | NO | `KEEP_APPENDIX_ONLY_FOR_NOW` | Greek retroversion, hypothetical | [`research\logion-cards\logion-094.md`](../../research\logion-cards\logion-094.md) | [`research\evidence\notes\logion-094-evidence-en.md`](../../research\evidence\notes\logion-094-evidence-en.md) | None recorded |
| 95 | YES | `INCLUDE_WITH_MARKER` | Greek retroversion, hypothetical | [`research\logion-cards\logion-095.md`](../../research\logion-cards\logion-095.md) | [`research\evidence\notes\logion-095-evidence-en.md`](../../research\evidence\notes\logion-095-evidence-en.md) | None recorded |
| 96 | YES | `INCLUDE_WITH_MARKER` for leaven core; full logion `UNCERTAIN` | Greek retroversion, hypothetical | [`research\logion-cards\logion-096.md`](../../research\logion-cards\logion-096.md) | [`research\evidence\notes\logion-096-evidence-en.md`](../../research\evidence\notes\logion-096-evidence-en.md) | None recorded |
| 97 | NO | `UNCERTAIN` | No loaded P.Oxy. witness | [`research\logion-cards\logion-097.md`](../../research\logion-cards\logion-097.md) | [`research\evidence\notes\logion-097-evidence-en.md`](../../research\evidence\notes\logion-097-evidence-en.md) | None recorded |
| 98 | NO | `DEFER` | No loaded P.Oxy. witness | [`research\logion-cards\logion-098.md`](../../research\logion-cards\logion-098.md) | [`research\evidence\notes\logion-098-evidence-en.md`](../../research\evidence\notes\logion-098-evidence-en.md) | None recorded |
| 99 | YES | `INCLUDE_WITH_MARKER` for true-family core; full logion `UNCERTAIN` | Greek retroversion, hypothetical | [`research\logion-cards\logion-099.md`](../../research\logion-cards\logion-099.md) | [`research\evidence\notes\logion-099-evidence-en.md`](../../research\evidence\notes\logion-099-evidence-en.md) | None recorded |
| 100 | YES | `INCLUDE_WITH_MARKER` for Caesar/God core; full logion `UNCERTAIN` | Greek retroversion, hypothetical | [`research\logion-cards\logion-100.md`](../../research\logion-cards\logion-100.md) | [`research\evidence\notes\logion-100-evidence-en.md`](../../research\evidence\notes\logion-100-evidence-en.md) | None recorded |
| 101 | NO | `UNCERTAIN` | Greek retroversion, hypothetical | [`research\logion-cards\logion-101.md`](../../research\logion-cards\logion-101.md) | [`research\evidence\notes\logion-101-evidence-en.md`](../../research\evidence\notes\logion-101-evidence-en.md) | None recorded |
| 102 | NO | `DEFER` | No loaded P.Oxy. witness | [`research\logion-cards\logion-102.md`](../../research\logion-cards\logion-102.md) | [`research\evidence\notes\logion-102-evidence-en.md`](../../research\evidence\notes\logion-102-evidence-en.md) | None recorded |
| 103 | YES | `INCLUDE_WITH_MARKER` for thief/watchfulness core; full logion appendix-only | Greek retroversion, hypothetical | [`research\logion-cards\logion-103.md`](../../research\logion-cards\logion-103.md) | [`research\evidence\notes\logion-103-evidence-en.md`](../../research\evidence\notes\logion-103-evidence-en.md) | None recorded |
| 104 | NO | 104A bridegroom-fasting core `APPENDIX_ONLY_STABLE`; full logion appendix-only | Greek retroversion, hypothetical | [`research\logion-cards\logion-104.md`](../../research\logion-cards\logion-104.md) | [`research\evidence\notes\logion-104-evidence-en.md`](../../research\evidence\notes\logion-104-evidence-en.md) | None recorded |
| 105 | NO | `DEFER` | No loaded P.Oxy. witness | [`research\logion-cards\logion-105.md`](../../research\logion-cards\logion-105.md) | [`research\evidence\notes\logion-105-evidence-en.md`](../../research\evidence\notes\logion-105-evidence-en.md) | None recorded |
| 106 | NO | `DEFER` | Greek retroversion, hypothetical | [`research\logion-cards\logion-106.md`](../../research\logion-cards\logion-106.md) | [`research\evidence\notes\logion-106-evidence-en.md`](../../research\evidence\notes\logion-106-evidence-en.md) | None recorded |
| 107 | YES | `INCLUDE_WITH_MARKER` for lost-sheep core; full logion `UNCERTAIN` | Greek retroversion, hypothetical | [`research\logion-cards\logion-107.md`](../../research\logion-cards\logion-107.md) | [`research\evidence\notes\logion-107-evidence-en.md`](../../research\evidence\notes\logion-107-evidence-en.md) | None recorded |
| 108 | NO | `DEFER` | No loaded P.Oxy. witness | [`research\logion-cards\logion-108.md`](../../research\logion-cards\logion-108.md) | [`research\evidence\notes\logion-108-evidence-en.md`](../../research\evidence\notes\logion-108-evidence-en.md) | None recorded |
| 109 | NO | `KEEP_APPENDIX_ONLY_FOR_NOW` | Greek retroversion, hypothetical | [`research\logion-cards\logion-109.md`](../../research\logion-cards\logion-109.md) | [`research\evidence\notes\logion-109-evidence-en.md`](../../research\evidence\notes\logion-109-evidence-en.md) | None recorded |
| 110 | NO | `DEFER_TO_CLUSTER` | No loaded P.Oxy. witness | [`research\logion-cards\logion-110.md`](../../research\logion-cards\logion-110.md) | [`research\evidence\notes\logion-110-evidence-en.md`](../../research\evidence\notes\logion-110-evidence-en.md) | None recorded |
| 111 | NO | `UNCERTAIN` | Greek retroversion, hypothetical | [`research\logion-cards\logion-111.md`](../../research\logion-cards\logion-111.md) | [`research\evidence\notes\logion-111-evidence-en.md`](../../research\evidence\notes\logion-111-evidence-en.md) | None recorded |
| 112 | NO | `DEFER` | No loaded P.Oxy. witness | [`research\logion-cards\logion-112.md`](../../research\logion-cards\logion-112.md) | [`research\evidence\notes\logion-112-evidence-en.md`](../../research\evidence\notes\logion-112-evidence-en.md) | None recorded |
| 113 | NO | `KEEP_APPENDIX_ONLY_FOR_NOW` | Greek retroversion, hypothetical | [`research\logion-cards\logion-113.md`](../../research\logion-cards\logion-113.md) | [`research\evidence\notes\logion-113-evidence-en.md`](../../research\evidence\notes\logion-113-evidence-en.md) | None recorded |
| 114 | NO | `EXCLUDE_AS_SECONDARY` | No loaded P.Oxy. witness | [`research\logion-cards\logion-114.md`](../../research\logion-cards\logion-114.md) | [`research\evidence\notes\logion-114-evidence-en.md`](../../research\evidence\notes\logion-114-evidence-en.md), [`research\evidence\notes\logion-114-exclusion-rationale-en.md`](../../research\evidence\notes\logion-114-exclusion-rationale-en.md) | None recorded |

## Source Witness Inventory

The local source inventory currently contains 136 files under `sources/primary_texts/`. The full machine-readable table is `source-witness-inventory.tsv`.

| Witness family | Digital role |
| --- | --- |
| Coptic / NHC II,2 | Main surviving complete-language witness for the Gospel of Thomas tradition used by the project. |
| Greek P.Oxy. 1 | Early Greek fragmentary witness; direct Thomas witness where extant. |
| Greek P.Oxy. 654 | Early Greek fragmentary witness; especially important for opening logia. |
| Greek P.Oxy. 655 | Early Greek fragmentary witness; important but lacunose/uncertain in several places. |
| Canonical Greek controls | Synoptic/control channel, not Thomas manuscript evidence. |
| Translation controls | Open or protected translations used only according to rights/citation policy. |

## Cluster And Control Notes

Cluster notes prevent isolated decisions from distorting the reconstruction. They are especially important for motifs such as seek/find, family renunciation, wealth, beatitudes, living/dead/world, fire/kingdom, ritual practice, and thief/watchfulness.

- [`research\evidence\notes\beatitudes-cluster-control-en.md`](../../research\evidence\notes\beatitudes-cluster-control-en.md)
- [`research\evidence\notes\family-renunciation-cluster-control-en.md`](../../research\evidence\notes\family-renunciation-cluster-control-en.md)
- [`research\evidence\notes\fire-kingdom-cluster-control-en.md`](../../research\evidence\notes\fire-kingdom-cluster-control-en.md)
- [`research\evidence\notes\living-dead-world-cluster-control-en.md`](../../research\evidence\notes\living-dead-world-cluster-control-en.md)
- [`research\evidence\notes\ritual-ethics-cluster-006-014-027-104-en.md`](../../research\evidence\notes\ritual-ethics-cluster-006-014-027-104-en.md)
- [`research\evidence\notes\seek-find-cluster-control-en.md`](../../research\evidence\notes\seek-find-cluster-control-en.md)
- [`research\evidence\notes\thief-watchfulness-cluster-control-21-103-en.md`](../../research\evidence\notes\thief-watchfulness-cluster-control-21-103-en.md)
- [`research\evidence\notes\thomas-unity-monachos-cluster-en.md`](../../research\evidence\notes\thomas-unity-monachos-cluster-en.md)
- [`research\evidence\notes\wealth-renunciation-cluster-control-en.md`](../../research\evidence\notes\wealth-renunciation-cluster-control-en.md)

## Bibliography, Rights, And Commons Policy

- `book/bibliography/bibliography-working.md` - working bibliography with print keys.
- `book/bibliography/source-rights-register.md` - source-rights status table.
- `project/rights-and-citation-policy.md` - print/digital citation policy.
- `project/source-reproducibility-note.md` - source reproducibility note.
- `LICENSE.md` and `project/commons-dedication-and-use-policy.md` - commons / anti-ownership policy for the original EUAGELIA work.

The original EUAGELIA reconstruction, translations, commentary, prompts, tables, and research architecture are intended as a commons. External witnesses, modern editions, translations, facsimiles, and websites retain their own legal status.

## Audit Trail

The current audit-trail index contains 28 project pass/audit/review files. Use `audit-trail-index.tsv` for checksums and exact file paths.

Major publication-stage reports include:

- `project/full-ukrainian-book-proof-qa-appendix-typography-v0.1.md`
- `project/full-english-book-proof-qa-typography-v0.1.md`
- `project/english-appendix-editorial-quality-pass-v0.1.md`
- `project/full-book-assembly-typesetting-pipeline-v0.1.md`
- `project/final-bibliography-rights-verify-v0.1.md`
- `project/publication-remediation-plan-2026-07-18.md`

## Reproducibility Checklist

1. Run `python3 build/scripts/qa_crosscheck.py`.
2. Regenerate paper and companion sources with `python3 build/scripts/assemble_full_book_sources.py` and `python3 build/scripts/generate_digital_companion.py`.
3. Render proofs with `python3 build/scripts/render_full_book_proofs.py`.
4. Compare checksums in `artifact-checksums.tsv` and `dist/render-log-full-book-proofs-v0.1.md`.
5. Review all changed files with `git status --short` and `git diff` before release.

## Remaining Digital Work

- Turn this Markdown/PDF proof into a polished HTML or static-site companion with better browsing, filters, and back-links.
- Add final production checksums only after final copyedit and typesetting decisions.
- Add a final external-source redistribution review before publishing downloadable source snapshots.
