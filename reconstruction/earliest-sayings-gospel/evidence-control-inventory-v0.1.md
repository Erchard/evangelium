# Evidence and Control Inventory v0.1

Статус: виконано Phase 3 quality remediation, 2026-07-17.

## Мета

Цей документ звіряє фактичні evidence notes і control files із `corpus/tables/logia-workflow-matrix.md` перед створенням true all-114 publication decision table. Він не змінює рішень про включення логій і не додає нових evidence notes; це карта того, що вже існує і що ще треба закрити.

## Executive Summary

| Metric | Count |
| --- | ---: |
| Logia covered | 114 |
| Matrix evidence YES | 55 |
| Matrix evidence NO | 59 |
| Actual direct evidence-note coverage | 54 |
| Logia with direct control file | 42 |
| Logia with cluster/range control file | 14 |
| Logia with cluster/context note but no direct evidence note | 6 |
| Matrix YES but no actual direct evidence note found | 1 |
| Matrix NO but actual direct evidence note found | 0 |
| Logia with neither evidence note nor control/cluster support | 53 |

## Priority Counts

| Priority | Count | Meaning |
| --- | ---: | --- |
| `P0` | 0 | Clean-reader unit lacks evidence trail |
| `P1` | 38 | High-impact missing evidence/control before all-114 table |
| `P1-control` | 1 | Included/reader unit has evidence but may need dedicated control check |
| `P2` | 22 | Low-priority appendix/no-note rationale needed |
| `OK` | 53 | Sufficient for next decision-table pass |

## Mismatches

- Matrix says `YES` but no actual direct evidence note found: 23.
- Matrix says `NO` but actual direct evidence note found: none.
- Cards still claiming missing evidence despite an actual evidence note file: 1, 2, 3, 5, 7, 8, 9, 10, 20, 25, 26, 31, 32, 33, 34, 35, 36, 39, 41, 44, 46, 54, 55, 57, 65, 66, 72, 73, 86, 89, 90, 93, 95, 96, 99, 100, 107.

Interpretation: the workflow matrix is mostly aligned with actual direct evidence files. The only matrix/direct-file mismatch is Logion 23: it is cluster-checked through the Thomas unity / monachos note, but it does not yet have a dedicated `logion-023-evidence-en.md` file. Remaining work is therefore not broad matrix repair; it is creating targeted evidence/control coverage for logia still marked `NO`, with priority based on reader risk, Greek witness status, and control availability.

## Highest-Priority Next Work

### P1

- Logion 14: DEFER; reader `NO`; Greek `Greek retroversion, hypothetical`; cluster note. Next: Create direct evidence note because source/control material already exists.
- Logion 17: UNCERTAIN; reader `NO`; Greek `No loaded P.Oxy. witness`; no evidence/control file. Next: Create evidence/no-note rationale before deciding whether this can affect the final corpus.
- Logion 18: UNCERTAIN; reader `NO`; Greek `No loaded P.Oxy. witness`; no evidence/control file. Next: Create evidence/no-note rationale before deciding whether this can affect the final corpus.
- Logion 21: UNCERTAIN; reader `NO`; Greek `No loaded P.Oxy. witness`; no evidence/control file. Next: Create evidence/no-note rationale before deciding whether this can affect the final corpus.
- Logion 23: UNCERTAIN; reader `NO`; Greek `No loaded P.Oxy. witness`; cluster note. Next: Create direct evidence note because source/control material already exists.
- Logion 24: DEFER; reader `NO`; Greek `P.Oxy. 655 possible/uncertain`; no evidence/control file. Next: Create direct evidence note because source/control material already exists.
- Logion 28: UNCERTAIN; reader `NO`; Greek `P.Oxy. 1 partial`; no evidence/control file. Next: Create direct evidence note because source/control material already exists.
- Logion 29: DEFER; reader `NO`; Greek `P.Oxy. 1 tiny fragment`; no evidence/control file. Next: Create direct evidence note because source/control material already exists.
- Logion 30: UNCERTAIN; reader `NO`; Greek `P.Oxy. 1, textually complex with 77b`; no evidence/control file. Next: Create direct evidence note because source/control material already exists.
- Logion 37: UNCERTAIN; reader `NO`; Greek `P.Oxy. 655`; cluster control, cluster note. Next: Create direct evidence note because source/control material already exists.
- Logion 38: UNCERTAIN; reader `NO`; Greek `P.Oxy. 655 fragmentary`; cluster control. Next: Create direct evidence note because source/control material already exists.
- Logion 40: UNCERTAIN; reader `NO`; Greek `No loaded P.Oxy. witness`; no evidence/control file. Next: Create evidence/no-note rationale before deciding whether this can affect the final corpus.
- Logion 42: UNCERTAIN; reader `NO`; Greek `No loaded P.Oxy. witness`; no evidence/control file. Next: Create evidence/no-note rationale before deciding whether this can affect the final corpus.
- Logion 48: UNCERTAIN; reader `NO`; Greek `No loaded P.Oxy. witness`; no evidence/control file. Next: Create evidence/no-note rationale before deciding whether this can affect the final corpus.
- Logion 49: UNCERTAIN; reader `NO`; Greek `No loaded P.Oxy. witness`; no evidence/control file. Next: Create evidence/no-note rationale before deciding whether this can affect the final corpus.
- Logion 50: UNCERTAIN; reader `NO`; Greek `No loaded P.Oxy. witness`; no evidence/control file. Next: Create evidence/no-note rationale before deciding whether this can affect the final corpus.
- Logion 51: UNCERTAIN; reader `NO`; Greek `No loaded P.Oxy. witness`; no evidence/control file. Next: Create evidence/no-note rationale before deciding whether this can affect the final corpus.
- Logion 52: UNCERTAIN; reader `NO`; Greek `No loaded P.Oxy. witness`; no evidence/control file. Next: Create evidence/no-note rationale before deciding whether this can affect the final corpus.
- Logion 56: UNCERTAIN; reader `NO`; Greek `No loaded P.Oxy. witness`; no evidence/control file. Next: Create evidence/no-note rationale before deciding whether this can affect the final corpus.
- Logion 58: UNCERTAIN; reader `NO`; Greek `No loaded P.Oxy. witness`; no evidence/control file. Next: Create evidence/no-note rationale before deciding whether this can affect the final corpus.
- Logion 59: UNCERTAIN; reader `NO`; Greek `No loaded P.Oxy. witness`; no evidence/control file. Next: Create evidence/no-note rationale before deciding whether this can affect the final corpus.
- Logion 60: UNCERTAIN; reader `NO`; Greek `No loaded P.Oxy. witness`; no evidence/control file. Next: Create evidence/no-note rationale before deciding whether this can affect the final corpus.
- Logion 62: UNCERTAIN; reader `NO`; Greek `No loaded P.Oxy. witness`; no evidence/control file. Next: Create evidence/no-note rationale before deciding whether this can affect the final corpus.
- Logion 67: UNCERTAIN; reader `NO`; Greek `No loaded P.Oxy. witness`; no evidence/control file. Next: Create evidence/no-note rationale before deciding whether this can affect the final corpus.
- Logion 68: UNCERTAIN; reader `NO`; Greek `No loaded P.Oxy. witness`; no evidence/control file. Next: Create evidence/no-note rationale before deciding whether this can affect the final corpus.
- Logion 69: UNCERTAIN; reader `NO`; Greek `No loaded P.Oxy. witness`; no evidence/control file. Next: Create evidence/no-note rationale before deciding whether this can affect the final corpus.
- Logion 75: DEFER; reader `NO`; Greek `No loaded P.Oxy. witness`; cluster note. Next: Create direct evidence note because source/control material already exists.
- Logion 77: DEFER; reader `NO`; Greek `P.Oxy. 1 overlap for 77b only`; no evidence/control file. Next: Create direct evidence note because source/control material already exists.
- Logion 81: UNCERTAIN; reader `NO`; Greek `No loaded P.Oxy. witness`; no evidence/control file. Next: Create evidence/no-note rationale before deciding whether this can affect the final corpus.
- Logion 82: UNCERTAIN; reader `NO`; Greek `No loaded P.Oxy. witness`; no evidence/control file. Next: Create evidence/no-note rationale before deciding whether this can affect the final corpus.
- Logion 91: UNCERTAIN; reader `NO`; Greek `Greek retroversion, hypothetical`; no evidence/control file. Next: Create evidence/no-note rationale before deciding whether this can affect the final corpus.
- Logion 92: UNCERTAIN; reader `NO`; Greek `Greek retroversion, hypothetical`; no evidence/control file. Next: Create evidence/no-note rationale before deciding whether this can affect the final corpus.
- Logion 97: UNCERTAIN; reader `NO`; Greek `No loaded P.Oxy. witness`; no evidence/control file. Next: Create evidence/no-note rationale before deciding whether this can affect the final corpus.
- Logion 101: UNCERTAIN; reader `NO`; Greek `Greek retroversion, hypothetical`; no evidence/control file. Next: Create evidence/no-note rationale before deciding whether this can affect the final corpus.
- Logion 104: DEFER; reader `NO`; Greek `Greek retroversion, hypothetical`; cluster note. Next: Create direct evidence note because source/control material already exists.
- Logion 106: DEFER; reader `NO`; Greek `Greek retroversion, hypothetical`; cluster note. Next: Create direct evidence note because source/control material already exists.
- Logion 111: UNCERTAIN; reader `NO`; Greek `Greek retroversion, hypothetical`; no evidence/control file. Next: Create evidence/no-note rationale before deciding whether this can affect the final corpus.
- Logion 114: EXCLUDE_AS_SECONDARY; reader `NO`; Greek `No loaded P.Oxy. witness`; no evidence/control file. Next: Create explicit rationale before all-114 publication decision table.

### P1-control

- Logion 1: INCLUDE_WITH_MARKER; reader `YES`; Greek `P.Oxy. 654`; evidence exists. Next: Evidence note exists; check whether a dedicated control file is needed.

### P2

- Logion 12: DEFER; reader `NO`; Greek `No loaded P.Oxy. witness`; no evidence/control file. Next: Provide short appendix rationale / no-note rationale.
- Logion 13: DEFER; reader `NO`; Greek `No loaded P.Oxy. witness`; no evidence/control file. Next: Provide short appendix rationale / no-note rationale.
- Logion 15: DEFER; reader `NO`; Greek `No loaded P.Oxy. witness`; no evidence/control file. Next: Provide short appendix rationale / no-note rationale.
- Logion 19: DEFER; reader `NO`; Greek `No loaded P.Oxy. witness`; no evidence/control file. Next: Provide short appendix rationale / no-note rationale.
- Logion 43: DEFER; reader `NO`; Greek `No loaded P.Oxy. witness`; no evidence/control file. Next: Provide short appendix rationale / no-note rationale.
- Logion 53: DEFER; reader `NO`; Greek `No loaded P.Oxy. witness`; no evidence/control file. Next: Provide short appendix rationale / no-note rationale.
- Logion 61: DEFER; reader `NO`; Greek `No loaded P.Oxy. witness`; no evidence/control file. Next: Provide short appendix rationale / no-note rationale.
- Logion 70: DEFER; reader `NO`; Greek `No loaded P.Oxy. witness`; no evidence/control file. Next: Provide short appendix rationale / no-note rationale.
- Logion 71: DEFER; reader `NO`; Greek `No loaded P.Oxy. witness`; no evidence/control file. Next: Provide short appendix rationale / no-note rationale.
- Logion 74: DEFER; reader `NO`; Greek `No loaded P.Oxy. witness`; no evidence/control file. Next: Provide short appendix rationale / no-note rationale.
- Logion 80: DEFER; reader `NO`; Greek `No loaded P.Oxy. witness`; no evidence/control file. Next: Provide short appendix rationale / no-note rationale.
- Logion 83: DEFER; reader `NO`; Greek `No loaded P.Oxy. witness`; no evidence/control file. Next: Provide short appendix rationale / no-note rationale.
- Logion 84: DEFER; reader `NO`; Greek `No loaded P.Oxy. witness`; no evidence/control file. Next: Provide short appendix rationale / no-note rationale.
- Logion 85: DEFER; reader `NO`; Greek `No loaded P.Oxy. witness`; no evidence/control file. Next: Provide short appendix rationale / no-note rationale.
- Logion 87: DEFER; reader `NO`; Greek `No loaded P.Oxy. witness`; no evidence/control file. Next: Provide short appendix rationale / no-note rationale.
- Logion 88: DEFER; reader `NO`; Greek `No loaded P.Oxy. witness`; no evidence/control file. Next: Provide short appendix rationale / no-note rationale.
- Logion 98: DEFER; reader `NO`; Greek `No loaded P.Oxy. witness`; no evidence/control file. Next: Provide short appendix rationale / no-note rationale.
- Logion 102: DEFER; reader `NO`; Greek `No loaded P.Oxy. witness`; no evidence/control file. Next: Provide short appendix rationale / no-note rationale.
- Logion 105: DEFER; reader `NO`; Greek `No loaded P.Oxy. witness`; no evidence/control file. Next: Provide short appendix rationale / no-note rationale.
- Logion 108: DEFER; reader `NO`; Greek `No loaded P.Oxy. witness`; no evidence/control file. Next: Provide short appendix rationale / no-note rationale.
- Logion 110: DEFER; reader `NO`; Greek `No loaded P.Oxy. witness`; no evidence/control file. Next: Provide short appendix rationale / no-note rationale.
- Logion 112: DEFER; reader `NO`; Greek `No loaded P.Oxy. witness`; no evidence/control file. Next: Provide short appendix rationale / no-note rationale.

## Full 114-Logion Inventory

| Logion | Matrix Evidence | Actual Evidence Note(s) | Control / Cluster File(s) | Reader | Decision | Greek Status | Priority | Inventory Next Action |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | YES | `reconstruction/earliest-sayings-gospel/notes/logion-001-evidence-en.md` | — | YES | INCLUDE_WITH_MARKER | P.Oxy. 654 | `P1-control` | Evidence note exists; check whether a dedicated control file is needed. |
| 2 | YES | `reconstruction/earliest-sayings-gospel/notes/logion-002-evidence-en.md` | `controls/synoptic-parallels/logion-002-matthew-luke.md` | YES | INCLUDE_WITH_MARKER | P.Oxy. 654 | `OK` | Carry forward into all-114 decision table; polish as needed. |
| 3 | YES | `reconstruction/earliest-sayings-gospel/notes/logion-003-evidence-en.md` | `controls/synoptic-parallels/logion-003-luke-17-kingdom.md` | YES | INCLUDE_WITH_MARKER | P.Oxy. 654 | `OK` | Carry forward into all-114 decision table; polish as needed. |
| 4 | YES | `reconstruction/earliest-sayings-gospel/notes/logion-004-evidence-en.md` | `controls/synoptic-parallels/logion-004-first-last.md`<br>`reconstruction/earliest-sayings-gospel/notes/thomas-unity-monachos-cluster-en.md` | YES | INCLUDE_WITH_MARKER | P.Oxy. 654 | `OK` | Carry forward into all-114 decision table; polish as needed. |
| 5 | YES | `reconstruction/earliest-sayings-gospel/notes/logion-005-evidence-en.md` | `controls/synoptic-parallels/logion-005-hidden-revealed.md` | YES | INCLUDE_WITH_MARKER | P.Oxy. 654 | `OK` | Carry forward into all-114 decision table; polish as needed. |
| 6 | YES | `reconstruction/earliest-sayings-gospel/notes/logion-006-evidence-en.md` | `controls/synoptic-parallels/logion-006-ethical-core.md`<br>`controls/synoptic-parallels/logion-006-matthew-6-ritual-practice.md`<br>`reconstruction/earliest-sayings-gospel/notes/ritual-ethics-cluster-006-014-027-104-en.md` | YES | INCLUDE_WITH_MARKER for ethical core; full logion UNCERTAIN | P.Oxy. 654, lacunose | `OK` | Carry forward into all-114 decision table; polish as needed. |
| 7 | YES | `reconstruction/earliest-sayings-gospel/notes/logion-007-evidence-en.md` | — | NO | UNCERTAIN | P.Oxy. 654 | `OK` | Carry forward into all-114 decision table; polish as needed. |
| 8 | YES | `reconstruction/earliest-sayings-gospel/notes/logion-008-evidence-en.md` | `controls/synoptic-parallels/logia-008-020-022-high-candidate-controls.md` | NO | UNCERTAIN | No loaded P.Oxy. witness | `OK` | Carry forward into all-114 decision table; polish as needed. |
| 9 | YES | `reconstruction/earliest-sayings-gospel/notes/logion-009-evidence-en.md` | `controls/synoptic-parallels/logion-009-sower-core-final-controls.md`<br>`controls/synoptic-parallels/logion-009-sower.md` | YES | sower core INCLUDE_WITH_MARKER; full logion UNCERTAIN | Greek retroversion, hypothetical | `OK` | Carry forward into all-114 decision table; polish as needed. |
| 10 | YES | `reconstruction/earliest-sayings-gospel/notes/logion-010-evidence-en.md` | `controls/synoptic-parallels/logion-010-fire-luke-control.md` | YES | fire-casting core INCLUDE_WITH_MARKER; full logion UNCERTAIN | Greek retroversion, hypothetical | `OK` | Carry forward into all-114 decision table; polish as needed. |
| 11 | YES | `reconstruction/earliest-sayings-gospel/notes/logion-011-evidence-en.md` | `controls/synoptic-parallels/logion-011-heaven-passing-controls.md`<br>`reconstruction/earliest-sayings-gospel/notes/thomas-unity-monachos-cluster-en.md` | NO | UNCERTAIN | Greek retroversion, hypothetical | `OK` | Carry forward into all-114 decision table; polish as needed. |
| 12 | NO | — | — | NO | DEFER | No loaded P.Oxy. witness | `P2` | Provide short appendix rationale / no-note rationale. |
| 13 | NO | — | — | NO | DEFER | No loaded P.Oxy. witness | `P2` | Provide short appendix rationale / no-note rationale. |
| 14 | NO | — | `reconstruction/earliest-sayings-gospel/notes/ritual-ethics-cluster-006-014-027-104-en.md` | NO | DEFER | Greek retroversion, hypothetical | `P1` | Create direct evidence note because source/control material already exists. |
| 15 | NO | — | — | NO | DEFER | No loaded P.Oxy. witness | `P2` | Provide short appendix rationale / no-note rationale. |
| 16 | YES | `reconstruction/earliest-sayings-gospel/notes/logion-016-evidence-en.md` | `controls/synoptic-parallels/logion-016-division-core-final-controls.md`<br>`controls/synoptic-parallels/logion-016-division-family.md` | YES | division/household core INCLUDE_WITH_MARKER; full logion UNCERTAIN | Greek retroversion, hypothetical | `OK` | Carry forward into all-114 decision table; polish as needed. |
| 17 | NO | — | — | NO | UNCERTAIN | No loaded P.Oxy. witness | `P1` | Create evidence/no-note rationale before deciding whether this can affect the final corpus. |
| 18 | NO | — | — | NO | UNCERTAIN | No loaded P.Oxy. witness | `P1` | Create evidence/no-note rationale before deciding whether this can affect the final corpus. |
| 19 | NO | — | — | NO | DEFER | No loaded P.Oxy. witness | `P2` | Provide short appendix rationale / no-note rationale. |
| 20 | YES | `reconstruction/earliest-sayings-gospel/notes/logion-020-evidence-en.md` | `controls/synoptic-parallels/logion-020-mustard-seed.md`<br>`controls/synoptic-parallels/logia-008-020-022-high-candidate-controls.md`<br>`reconstruction/earliest-sayings-gospel/notes/logion-020-branch-tree-commentary-check-en.md` | YES | INCLUDE_WITH_MARKER | Greek retroversion, hypothetical | `OK` | Carry forward into all-114 decision table; polish as needed. |
| 21 | NO | — | — | NO | UNCERTAIN | No loaded P.Oxy. witness | `P1` | Create evidence/no-note rationale before deciding whether this can affect the final corpus. |
| 22 | YES | `reconstruction/earliest-sayings-gospel/notes/logion-022-evidence-en.md` | `controls/synoptic-parallels/logion-022-children-kingdom.md`<br>`controls/synoptic-parallels/logia-008-020-022-high-candidate-controls.md`<br>`reconstruction/earliest-sayings-gospel/notes/thomas-unity-monachos-cluster-en.md` | YES | children/kingdom core INCLUDE_WITH_MARKER; full logion UNCERTAIN | Greek retroversion, hypothetical | `OK` | Carry forward into all-114 decision table; polish as needed. |
| 23 | YES | — | `reconstruction/earliest-sayings-gospel/notes/thomas-unity-monachos-cluster-en.md` | NO | UNCERTAIN | No loaded P.Oxy. witness | `P1` | Create direct evidence note because source/control material already exists. |
| 24 | NO | — | — | NO | DEFER | P.Oxy. 655 possible/uncertain | `P1` | Create direct evidence note because source/control material already exists. |
| 25 | YES | `reconstruction/earliest-sayings-gospel/notes/logion-025-evidence-en.md` | `controls/synoptic-parallels/logion-025-love-brother.md` | YES | INCLUDE_WITH_MARKER | Greek retroversion, hypothetical | `OK` | Carry forward into all-114 decision table; polish as needed. |
| 26 | YES | `reconstruction/earliest-sayings-gospel/notes/logion-026-evidence-en.md` | `controls/synoptic-parallels/logion-026-speck-beam.md` | YES | INCLUDE_WITH_MARKER | P.Oxy. 1 partial | `OK` | Carry forward into all-114 decision table; polish as needed. |
| 27 | YES | `reconstruction/earliest-sayings-gospel/notes/logion-027-evidence-en.md` | `controls/synoptic-parallels/logion-027-fasting-sabbath.md`<br>`reconstruction/earliest-sayings-gospel/notes/ritual-ethics-cluster-006-014-027-104-en.md` | NO | UNCERTAIN | P.Oxy. 1; P.Oxy. 5575 control | `OK` | Carry forward into all-114 decision table; polish as needed. |
| 28 | NO | — | — | NO | UNCERTAIN | P.Oxy. 1 partial | `P1` | Create direct evidence note because source/control material already exists. |
| 29 | NO | — | — | NO | DEFER | P.Oxy. 1 tiny fragment | `P1` | Create direct evidence note because source/control material already exists. |
| 30 | NO | — | — | NO | UNCERTAIN | P.Oxy. 1, textually complex with 77b | `P1` | Create direct evidence note because source/control material already exists. |
| 31 | YES | `reconstruction/earliest-sayings-gospel/notes/logion-031-evidence-en.md` | `controls/synoptic-parallels/logia-031-033-poxy1-synoptic-controls.md` | YES | INCLUDE_WITH_MARKER | P.Oxy. 1 | `OK` | Carry forward into all-114 decision table; polish as needed. |
| 32 | YES | `reconstruction/earliest-sayings-gospel/notes/logion-032-evidence-en.md` | `controls/synoptic-parallels/logia-031-033-poxy1-synoptic-controls.md` | YES | INCLUDE_WITH_MARKER | P.Oxy. 1 | `OK` | Carry forward into all-114 decision table; polish as needed. |
| 33 | YES | `reconstruction/earliest-sayings-gospel/notes/logion-033-evidence-en.md` | `controls/synoptic-parallels/logia-031-033-poxy1-synoptic-controls.md` | YES | INCLUDE_WITH_MARKER | P.Oxy. 1 opening only | `OK` | Carry forward into all-114 decision table; polish as needed. |
| 34 | YES | `reconstruction/earliest-sayings-gospel/notes/logion-034-evidence-en.md` | `controls/synoptic-parallels/logia-034-035-bridge-synoptic-controls.md` | YES | INCLUDE_WITH_MARKER | Greek retroversion, hypothetical | `OK` | Carry forward into all-114 decision table; polish as needed. |
| 35 | YES | `reconstruction/earliest-sayings-gospel/notes/logion-035-evidence-en.md` | `controls/synoptic-parallels/logia-034-035-bridge-synoptic-controls.md` | YES | INCLUDE_WITH_MARKER | Greek retroversion, hypothetical | `OK` | Carry forward into all-114 decision table; polish as needed. |
| 36 | YES | `reconstruction/earliest-sayings-gospel/notes/logion-036-evidence-en.md` | `controls/synoptic-parallels/logia-036-039-poxy655-synoptic-controls.md` | YES | INCLUDE_WITH_MARKER | P.Oxy. 655; P.Oxy. 5575 control | `OK` | Carry forward into all-114 decision table; polish as needed. |
| 37 | NO | — | `controls/synoptic-parallels/logia-036-039-poxy655-synoptic-controls.md`<br>`reconstruction/earliest-sayings-gospel/notes/thomas-unity-monachos-cluster-en.md` | NO | UNCERTAIN | P.Oxy. 655 | `P1` | Create direct evidence note because source/control material already exists. |
| 38 | NO | — | `controls/synoptic-parallels/logia-036-039-poxy655-synoptic-controls.md` | NO | UNCERTAIN | P.Oxy. 655 fragmentary | `P1` | Create direct evidence note because source/control material already exists. |
| 39 | YES | `reconstruction/earliest-sayings-gospel/notes/logion-039-evidence-en.md` | `controls/synoptic-parallels/logia-036-039-poxy655-synoptic-controls.md` | YES | INCLUDE_WITH_MARKER | P.Oxy. 655 | `OK` | Carry forward into all-114 decision table; polish as needed. |
| 40 | NO | — | — | NO | UNCERTAIN | No loaded P.Oxy. witness | `P1` | Create evidence/no-note rationale before deciding whether this can affect the final corpus. |
| 41 | YES | `reconstruction/earliest-sayings-gospel/notes/logion-041-evidence-en.md` | `controls/synoptic-parallels/logion-041-has-given-controls.md` | YES | INCLUDE_WITH_MARKER | No loaded P.Oxy. witness | `OK` | Carry forward into all-114 decision table; polish as needed. |
| 42 | NO | — | — | NO | UNCERTAIN | No loaded P.Oxy. witness | `P1` | Create evidence/no-note rationale before deciding whether this can affect the final corpus. |
| 43 | NO | — | — | NO | DEFER | No loaded P.Oxy. witness | `P2` | Provide short appendix rationale / no-note rationale. |
| 44 | YES | `reconstruction/earliest-sayings-gospel/notes/logion-044-evidence-en.md` | `controls/synoptic-parallels/logion-044-blasphemy-spirit-controls.md` | NO | UNCERTAIN | No loaded P.Oxy. witness | `OK` | Carry forward into all-114 decision table; polish as needed. |
| 45 | YES | `reconstruction/earliest-sayings-gospel/notes/logion-045-evidence-en.md` | `controls/synoptic-parallels/logion-045-tree-fruit-heart-controls.md` | YES | 45A INCLUDE_WITH_MARKER; 45B KEEP_APPENDIX_ONLY_FOR_NOW; full logion UNCERTAIN | Greek retroversion, hypothetical | `OK` | Carry forward into all-114 decision table; polish as needed. |
| 46 | YES | `reconstruction/earliest-sayings-gospel/notes/logion-046-evidence-en.md` | `controls/synoptic-parallels/logion-046-john-least-kingdom-controls.md` | NO | UNCERTAIN; possible marked core candidate | No loaded P.Oxy. witness | `OK` | Carry forward into all-114 decision table; polish as needed. |
| 47 | YES | `reconstruction/earliest-sayings-gospel/notes/logion-047-evidence-en.md` | `controls/synoptic-parallels/logion-047-incompatibility-sayings-controls.md` | YES | 47B INCLUDE_WITH_MARKER; full logion UNCERTAIN | Greek retroversion, hypothetical | `OK` | Carry forward into all-114 decision table; polish as needed. |
| 48 | NO | — | — | NO | UNCERTAIN | No loaded P.Oxy. witness | `P1` | Create evidence/no-note rationale before deciding whether this can affect the final corpus. |
| 49 | NO | — | — | NO | UNCERTAIN | No loaded P.Oxy. witness | `P1` | Create evidence/no-note rationale before deciding whether this can affect the final corpus. |
| 50 | NO | — | — | NO | UNCERTAIN | No loaded P.Oxy. witness | `P1` | Create evidence/no-note rationale before deciding whether this can affect the final corpus. |
| 51 | NO | — | — | NO | UNCERTAIN | No loaded P.Oxy. witness | `P1` | Create evidence/no-note rationale before deciding whether this can affect the final corpus. |
| 52 | NO | — | — | NO | UNCERTAIN | No loaded P.Oxy. witness | `P1` | Create evidence/no-note rationale before deciding whether this can affect the final corpus. |
| 53 | NO | — | — | NO | DEFER | No loaded P.Oxy. witness | `P2` | Provide short appendix rationale / no-note rationale. |
| 54 | YES | `reconstruction/earliest-sayings-gospel/notes/logion-054-evidence-en.md` | `controls/synoptic-parallels/logion-054-blessed-poor-controls.md` | YES | INCLUDE_WITH_MARKER | No loaded P.Oxy. witness | `OK` | Carry forward into all-114 decision table; polish as needed. |
| 55 | YES | `reconstruction/earliest-sayings-gospel/notes/logion-055-evidence-en.md` | `controls/synoptic-parallels/logion-055-discipleship-cross-controls.md` | NO | UNCERTAIN | No loaded P.Oxy. witness | `OK` | Carry forward into all-114 decision table; polish as needed. |
| 56 | NO | — | — | NO | UNCERTAIN | No loaded P.Oxy. witness | `P1` | Create evidence/no-note rationale before deciding whether this can affect the final corpus. |
| 57 | YES | `reconstruction/earliest-sayings-gospel/notes/logion-057-evidence-en.md` | `controls/synoptic-parallels/logion-057-weeds-controls.md` | NO | UNCERTAIN | No loaded P.Oxy. witness | `OK` | Carry forward into all-114 decision table; polish as needed. |
| 58 | NO | — | — | NO | UNCERTAIN | No loaded P.Oxy. witness | `P1` | Create evidence/no-note rationale before deciding whether this can affect the final corpus. |
| 59 | NO | — | — | NO | UNCERTAIN | No loaded P.Oxy. witness | `P1` | Create evidence/no-note rationale before deciding whether this can affect the final corpus. |
| 60 | NO | — | — | NO | UNCERTAIN | No loaded P.Oxy. witness | `P1` | Create evidence/no-note rationale before deciding whether this can affect the final corpus. |
| 61 | NO | — | — | NO | DEFER | No loaded P.Oxy. witness | `P2` | Provide short appendix rationale / no-note rationale. |
| 62 | NO | — | — | NO | UNCERTAIN | No loaded P.Oxy. witness | `P1` | Create evidence/no-note rationale before deciding whether this can affect the final corpus. |
| 63 | YES | `reconstruction/earliest-sayings-gospel/notes/logion-063-evidence-en.md` | `controls/synoptic-parallels/logion-063-rich-fool-luke-control.md` | YES | INCLUDE_WITH_MARKER; full logion UNCERTAIN | Greek retroversion, hypothetical | `OK` | Carry forward into all-114 decision table; polish as needed. |
| 64 | YES | `reconstruction/earliest-sayings-gospel/notes/logion-064-evidence-en.md` | `controls/synoptic-parallels/logion-064-banquet-invitation-controls.md` | NO | 64A/64B KEEP_APPENDIX_ONLY_FOR_NOW | No loaded P.Oxy. witness | `OK` | Carry forward into all-114 decision table; polish as needed. |
| 65 | YES | `reconstruction/earliest-sayings-gospel/notes/logion-065-066-evidence-en.md` | `controls/synoptic-parallels/logia-065-066-tenants-stone-controls.md` | NO | KEEP_APPENDIX_ONLY_FOR_NOW | No loaded P.Oxy. witness | `OK` | Carry forward into all-114 decision table; polish as needed. |
| 66 | YES | `reconstruction/earliest-sayings-gospel/notes/logion-065-066-evidence-en.md` | `controls/synoptic-parallels/logia-065-066-tenants-stone-controls.md` | NO | KEEP_APPENDIX_ONLY_FOR_NOW | No loaded P.Oxy. witness | `OK` | Carry forward into all-114 decision table; polish as needed. |
| 67 | NO | — | — | NO | UNCERTAIN | No loaded P.Oxy. witness | `P1` | Create evidence/no-note rationale before deciding whether this can affect the final corpus. |
| 68 | NO | — | — | NO | UNCERTAIN | No loaded P.Oxy. witness | `P1` | Create evidence/no-note rationale before deciding whether this can affect the final corpus. |
| 69 | NO | — | — | NO | UNCERTAIN | No loaded P.Oxy. witness | `P1` | Create evidence/no-note rationale before deciding whether this can affect the final corpus. |
| 70 | NO | — | — | NO | DEFER | No loaded P.Oxy. witness | `P2` | Provide short appendix rationale / no-note rationale. |
| 71 | NO | — | — | NO | DEFER | No loaded P.Oxy. witness | `P2` | Provide short appendix rationale / no-note rationale. |
| 72 | YES | `reconstruction/earliest-sayings-gospel/notes/logion-072-evidence-en.md` | `controls/synoptic-parallels/logion-072-inheritance-dispute-controls.md` | YES | INCLUDE_WITH_MARKER | No loaded P.Oxy. witness | `OK` | Carry forward into all-114 decision table; polish as needed. |
| 73 | YES | `reconstruction/earliest-sayings-gospel/notes/logion-073-evidence-en.md` | `controls/synoptic-parallels/logion-073-harvest-workers-controls.md` | YES | INCLUDE_WITH_MARKER | No loaded P.Oxy. witness | `OK` | Carry forward into all-114 decision table; polish as needed. |
| 74 | NO | — | — | NO | DEFER | No loaded P.Oxy. witness | `P2` | Provide short appendix rationale / no-note rationale. |
| 75 | NO | — | `reconstruction/earliest-sayings-gospel/notes/thomas-unity-monachos-cluster-en.md` | NO | DEFER | No loaded P.Oxy. witness | `P1` | Create direct evidence note because source/control material already exists. |
| 76 | YES | `reconstruction/earliest-sayings-gospel/notes/logion-076-evidence-en.md` | `controls/synoptic-parallels/logion-076-pearl-treasure-controls.md` | NO | KEEP_APPENDIX_ONLY_FOR_NOW | No loaded P.Oxy. witness | `OK` | Carry forward into all-114 decision table; polish as needed. |
| 77 | NO | — | — | NO | DEFER | P.Oxy. 1 overlap for 77b only | `P1` | Create direct evidence note because source/control material already exists. |
| 78 | YES | `reconstruction/earliest-sayings-gospel/notes/logion-078-evidence-en.md` | `controls/synoptic-parallels/logion-078-wilderness-reed-controls.md` | NO | KEEP_APPENDIX_ONLY_FOR_NOW | No loaded P.Oxy. witness | `OK` | Carry forward into all-114 decision table; polish as needed. |
| 79 | YES | `reconstruction/earliest-sayings-gospel/notes/logion-079-evidence-en.md` | `controls/synoptic-parallels/logion-079-womb-word-controls.md` | NO | KEEP_APPENDIX_ONLY_FOR_NOW | No loaded P.Oxy. witness | `OK` | Carry forward into all-114 decision table; polish as needed. |
| 80 | NO | — | — | NO | DEFER | No loaded P.Oxy. witness | `P2` | Provide short appendix rationale / no-note rationale. |
| 81 | NO | — | — | NO | UNCERTAIN | No loaded P.Oxy. witness | `P1` | Create evidence/no-note rationale before deciding whether this can affect the final corpus. |
| 82 | NO | — | — | NO | UNCERTAIN | No loaded P.Oxy. witness | `P1` | Create evidence/no-note rationale before deciding whether this can affect the final corpus. |
| 83 | NO | — | — | NO | DEFER | No loaded P.Oxy. witness | `P2` | Provide short appendix rationale / no-note rationale. |
| 84 | NO | — | — | NO | DEFER | No loaded P.Oxy. witness | `P2` | Provide short appendix rationale / no-note rationale. |
| 85 | NO | — | — | NO | DEFER | No loaded P.Oxy. witness | `P2` | Provide short appendix rationale / no-note rationale. |
| 86 | YES | `reconstruction/earliest-sayings-gospel/notes/logion-086-evidence-en.md` | `controls/synoptic-parallels/logion-086-foxes-birds-son-of-man-controls.md` | YES | INCLUDE_WITH_MARKER | Greek retroversion, hypothetical | `OK` | Carry forward into all-114 decision table; polish as needed. |
| 87 | NO | — | — | NO | DEFER | No loaded P.Oxy. witness | `P2` | Provide short appendix rationale / no-note rationale. |
| 88 | NO | — | — | NO | DEFER | No loaded P.Oxy. witness | `P2` | Provide short appendix rationale / no-note rationale. |
| 89 | YES | `reconstruction/earliest-sayings-gospel/notes/logion-089-evidence-en.md` | `controls/synoptic-parallels/logion-089-cup-inside-outside-controls.md` | YES | INCLUDE_WITH_MARKER | Greek retroversion, hypothetical | `OK` | Carry forward into all-114 decision table; polish as needed. |
| 90 | YES | `reconstruction/earliest-sayings-gospel/notes/logion-090-evidence-en.md` | `controls/synoptic-parallels/logion-090-yoke-rest-controls.md` | NO | UNCERTAIN | Greek retroversion, hypothetical | `OK` | Carry forward into all-114 decision table; polish as needed. |
| 91 | NO | — | — | NO | UNCERTAIN | Greek retroversion, hypothetical | `P1` | Create evidence/no-note rationale before deciding whether this can affect the final corpus. |
| 92 | NO | — | — | NO | UNCERTAIN | Greek retroversion, hypothetical | `P1` | Create evidence/no-note rationale before deciding whether this can affect the final corpus. |
| 93 | YES | `reconstruction/earliest-sayings-gospel/notes/logion-093-evidence-en.md` | `controls/synoptic-parallels/logion-093-holy-dogs-pearls-swine-controls.md` | NO | UNCERTAIN | Greek retroversion, hypothetical | `OK` | Carry forward into all-114 decision table; polish as needed. |
| 94 | YES | `reconstruction/earliest-sayings-gospel/notes/logion-094-evidence-en.md` | `controls/synoptic-parallels/logion-094-seek-knock-controls.md` | NO | KEEP_APPENDIX_ONLY_FOR_NOW | Greek retroversion, hypothetical | `OK` | Carry forward into all-114 decision table; polish as needed. |
| 95 | YES | `reconstruction/earliest-sayings-gospel/notes/logion-095-evidence-en.md` | `controls/synoptic-parallels/logion-095-money-lending-controls.md` | YES | INCLUDE_WITH_MARKER | Greek retroversion, hypothetical | `OK` | Carry forward into all-114 decision table; polish as needed. |
| 96 | YES | `reconstruction/earliest-sayings-gospel/notes/logion-096-evidence-en.md` | `controls/synoptic-parallels/logion-096-leaven-controls.md` | YES | INCLUDE_WITH_MARKER for leaven core; full logion UNCERTAIN | Greek retroversion, hypothetical | `OK` | Carry forward into all-114 decision table; polish as needed. |
| 97 | NO | — | — | NO | UNCERTAIN | No loaded P.Oxy. witness | `P1` | Create evidence/no-note rationale before deciding whether this can affect the final corpus. |
| 98 | NO | — | — | NO | DEFER | No loaded P.Oxy. witness | `P2` | Provide short appendix rationale / no-note rationale. |
| 99 | YES | `reconstruction/earliest-sayings-gospel/notes/logion-099-evidence-en.md` | `controls/synoptic-parallels/logion-099-true-family-controls.md` | YES | INCLUDE_WITH_MARKER for true-family core; full logion UNCERTAIN | Greek retroversion, hypothetical | `OK` | Carry forward into all-114 decision table; polish as needed. |
| 100 | YES | `reconstruction/earliest-sayings-gospel/notes/logion-100-evidence-en.md` | `controls/synoptic-parallels/logion-100-caesar-god-controls.md` | YES | INCLUDE_WITH_MARKER for Caesar/God core; full logion UNCERTAIN | Greek retroversion, hypothetical | `OK` | Carry forward into all-114 decision table; polish as needed. |
| 101 | NO | — | — | NO | UNCERTAIN | Greek retroversion, hypothetical | `P1` | Create evidence/no-note rationale before deciding whether this can affect the final corpus. |
| 102 | NO | — | — | NO | DEFER | No loaded P.Oxy. witness | `P2` | Provide short appendix rationale / no-note rationale. |
| 103 | YES | `reconstruction/earliest-sayings-gospel/notes/logion-103-evidence-en.md` | `controls/synoptic-parallels/logion-103-thief-watchfulness-controls.md` | NO | KEEP_APPENDIX_ONLY_FOR_NOW | Greek retroversion, hypothetical | `OK` | Carry forward into all-114 decision table; polish as needed. |
| 104 | NO | — | `reconstruction/earliest-sayings-gospel/notes/ritual-ethics-cluster-006-014-027-104-en.md` | NO | DEFER | Greek retroversion, hypothetical | `P1` | Create direct evidence note because source/control material already exists. |
| 105 | NO | — | — | NO | DEFER | No loaded P.Oxy. witness | `P2` | Provide short appendix rationale / no-note rationale. |
| 106 | NO | — | `reconstruction/earliest-sayings-gospel/notes/thomas-unity-monachos-cluster-en.md` | NO | DEFER | Greek retroversion, hypothetical | `P1` | Create direct evidence note because source/control material already exists. |
| 107 | YES | `reconstruction/earliest-sayings-gospel/notes/logion-107-evidence-en.md` | `controls/synoptic-parallels/logion-107-lost-sheep-controls.md` | YES | INCLUDE_WITH_MARKER for lost-sheep core; full logion UNCERTAIN | Greek retroversion, hypothetical | `OK` | Carry forward into all-114 decision table; polish as needed. |
| 108 | NO | — | — | NO | DEFER | No loaded P.Oxy. witness | `P2` | Provide short appendix rationale / no-note rationale. |
| 109 | YES | `reconstruction/earliest-sayings-gospel/notes/logion-109-evidence-en.md` | `controls/synoptic-parallels/logion-109-hidden-treasure-controls.md` | NO | KEEP_APPENDIX_ONLY_FOR_NOW | Greek retroversion, hypothetical | `OK` | Carry forward into all-114 decision table; polish as needed. |
| 110 | NO | — | — | NO | DEFER | No loaded P.Oxy. witness | `P2` | Provide short appendix rationale / no-note rationale. |
| 111 | NO | — | — | NO | UNCERTAIN | Greek retroversion, hypothetical | `P1` | Create evidence/no-note rationale before deciding whether this can affect the final corpus. |
| 112 | NO | — | — | NO | DEFER | No loaded P.Oxy. witness | `P2` | Provide short appendix rationale / no-note rationale. |
| 113 | YES | `reconstruction/earliest-sayings-gospel/notes/logion-113-evidence-en.md` | `controls/synoptic-parallels/logion-113-kingdom-not-observed-controls.md` | NO | KEEP_APPENDIX_ONLY_FOR_NOW | Greek retroversion, hypothetical | `OK` | Carry forward into all-114 decision table; polish as needed. |
| 114 | NO | — | — | NO | EXCLUDE_AS_SECONDARY | No loaded P.Oxy. witness | `P1` | Create explicit rationale before all-114 publication decision table. |

## Recommended Next Step

Superseded next-step note, 2026-07-17: Phase 4 has been completed in `reconstruction/earliest-sayings-gospel/all-114-publication-decision-table-v0.1.md`. Use this inventory together with that table for Phase 5 full appendix expansion.
