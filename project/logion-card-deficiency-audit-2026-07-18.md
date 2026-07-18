# Logion Card Deficiency Audit

Status: актуалізований аудит карток, 2026-07-18.

## Scope

Цей документ фіксує поточні недоліки 114 карток `corpus/cards/logion-NNN.md` після P0-ремедіації clean-reader суперечностей.

Контрольні шари:

- `corpus/tables/logia-workflow-matrix.md`
- `reconstruction/earliest-sayings-gospel/all-114-publication-decision-table-v0.1.md`
- current clean-reader set: 37 logia/cores
- `tools/qa_crosscheck.py`
- `tools/probability_reader_audit.py`

## Current Finding

Найважливіший попередній дефект був усунений: картки логій, які вже входять до clean reader, більше не містять локальних тверджень `Reader text: NO` або формулювання, що включене ядро "ще не внесене в головну реконструкцію".

Залишковий автоматично виявлений борг за точними P0/P1-патернами зараз закритий:

| Metric | Count |
| --- | ---: |
| Cards reviewed | 114 |
| Cards with exact-pattern unresolved defects | 0 |
| Cards clean by exact-pattern audit | 114 |
| `READER_STATUS_CONFLICT` | 0 |
| `INCLUDED_TEXT_SAYS_NOT_MAIN` | 0 |
| `LOCAL_NOT_DECIDED` | 0 |
| `MISSING_PROBABILITY` | 0 |

Structural QA passes, but `tools/probability_reader_audit.py` still flags a higher-level editorial problem:

- 114/114 cards now have a current/latest numeric probability profile.
- 0 cards have duplicate current probability profiles after superseded-profile labeling.
- 1 included unit has high late/post-130 risk by the current numeric profile: Logion 1.
- 10 excluded/deferred units have early probability >= 60: 64, 76, 78, 79, 90, 93, 94, 104, 109, 113.
- 20 excluded/deferred units have early probability >= 50.

This does not automatically mean the decisions are wrong. The first remediation response is now complete: the tension cards have explicit rationale blocks explaining why probability and reader decision pull in different directions.

## Severity

### P0: Closed In This Pass

- `READER_STATUS_CONFLICT`: included cards with stale `Reader text: NO`.
- `INCLUDED_TEXT_SAYS_NOT_MAIN`: included clean-reader unit saying it was not in the main reconstruction.

Closed cards:

- 6
- 46
- 86
- 89
- 91
- 95
- 96
- 99
- 100
- 103
- 107

Details are recorded in `project/card-p0-remediation-clean-reader-2026-07-18.md`.

### P0/P1: Closed In This Pass

These issues were fixed after the clean-reader contradiction pass because they could confuse editors and readers working from the card layer.

| Logion | Reader | Evidence Note | Deficiencies |
| ---: | --- | --- | --- |
| 1 | YES | YES | CLOSED: MISSING_PROBABILITY |
| 7 | NO | YES | CLOSED: MISSING_PROBABILITY |
| 12 | NO | NO | CLOSED: LOCAL_NOT_DECIDED |
| 13 | NO | NO | CLOSED: LOCAL_NOT_DECIDED |
| 15 | NO | NO | CLOSED: LOCAL_NOT_DECIDED |
| 17 | NO | YES | CLOSED: LOCAL_NOT_DECIDED |
| 18 | NO | YES | CLOSED: LOCAL_NOT_DECIDED |
| 19 | NO | NO | CLOSED: LOCAL_NOT_DECIDED |
| 24 | NO | YES | CLOSED: LOCAL_NOT_DECIDED |
| 28 | NO | YES | CLOSED: LOCAL_NOT_DECIDED |
| 29 | NO | YES | CLOSED: LOCAL_NOT_DECIDED |
| 30 | NO | YES | CLOSED: MISSING_PROBABILITY |

Definitions:

- `LOCAL_NOT_DECIDED`: an older local block still says `Рішення: NOT_DECIDED`, while the project already has a higher-level workflow decision.
- `MISSING_PROBABILITY`: the probability table still contains `не виставлено` instead of a numeric estimate or an explicit exceptional rationale.

### P1/P2: Requires Semantic Review, Not Only Pattern Replacement

The previous audit also identified broader quality risks such as generic early-core placeholders, generic secondary-risk descriptions, and evidence/control warnings. The stale `Primary card v0.1` status residue, the first generic early-core placeholder class, and the generic secondary-risk descriptions have now been normalized in card files.

Therefore the next normalization phase should review them semantically rather than mechanically deleting every occurrence.

High-value semantic review targets:

- duplicated status blocks where the later block silently overrides the earlier one;
- evidence/control warnings that may be stale after notes and cluster controls were added;
- cards with no Greek Oxyrhynchus witness where the distinction between "no direct Greek witness" and "possible retroverted Greek Vorlage" must stay explicit. This risk is now controlled at the publication Greek-layer level by `project/greek-layer-freeze-audit-2026-07-18.md`.

## Remediation Completed On 2026-07-18

The clean-reader contradiction pass updated the following cards without changing clean-reader membership:

- `corpus/cards/logion-006.md`
- `corpus/cards/logion-046.md`
- `corpus/cards/logion-086.md`
- `corpus/cards/logion-089.md`
- `corpus/cards/logion-091.md`
- `corpus/cards/logion-095.md`
- `corpus/cards/logion-096.md`
- `corpus/cards/logion-099.md`
- `corpus/cards/logion-100.md`
- `corpus/cards/logion-103.md`
- `corpus/cards/logion-107.md`

Main editorial rule applied:

- if only a compact core is included, the card must say exactly that;
- the fuller Thomas form can remain appendix-only or uncertain;
- old `Reader text: NO` statements must not remain inside a card whose core is printed in the clean reader.

Additional card-control remediation completed:

- Logia 12, 13, 15, 17, 18, 19, 24, 28, and 29 no longer contain stale local `NOT_DECIDED` decisions.
- Logia 1, 7, and 30 no longer contain `не виставлено` probability rows.
- Logion 30 now has a current numeric profile while remaining outside the clean reader because P.Oxy. 1 is textually complex and linked with the 77b sequence.
- Probability / reader-decision rationale v0.1 blocks were added to Logia 1, 64, 76, 78, 79, 90, 93, 94, 104, 109, and 113.
- Stale local decision labels were synchronized in Logia 90, 94, 104, 109, and 113.
- Historical probability tables in Logia 1, 2, 3, 4, 5, 6, 7, 9, 16, 20, 22, 23, 25, 26, 27, 31, 32, 33, 34, 35, 36, 37, 38, and 39 were explicitly labeled as superseded/local historical profiles. The current audit now counts only `### Ймовірнісний профіль` blocks as current profiles.
- Stale top-level `Статус: первинна корпусна картка v0.1` lines were normalized in 75 cards to explicit workflow-status headers.
- Stale Ukrainian `Поточний робочий статус: Primary card v0.1` rows and English `Current work status: Primary card v0.1` rows were normalized to workflow-status rows. Exact stale-status residue in cards is now 0.
- Generic early-core placeholders were replaced with logion-specific layer models in Logia 7, 8, 11, 17, 18, 23, 27, 28, 30, 37, 38, 40, 42, 44, 48, 49, 50, 51, 52, 55, 56, 57, 58, 59, 60, 62, 65, 66, 67, 68, 69, 81, 82, 90, 92, 93, 97, 101, and 111. Current exact-pattern count: 0.
- Generic secondary-risk descriptions were replaced with logion-specific secondary-layer explanations in 89 card locations. Current exact-pattern counts: `generic_dependence_risk` 0; `generic_composite_risk` 0.
- Softer generic early-core formulas were replaced with logion-specific layer models in 53 cards:
  - 24 included/marked reconstruction-candidate rows: Logia 1, 2, 3, 4, 5, 6, 9, 10, 16, 20, 22, 25, 26, 31, 32, 33, 34, 35, 36, 39, 41, 54, 72, and 73.
  - 29 deferred/appendix-only rows: Logia 12, 13, 14, 15, 19, 24, 29, 43, 53, 61, 70, 71, 74, 75, 77, 80, 83, 84, 85, 87, 88, 98, 102, 104, 105, 106, 108, 110, and 112.
  - Current exact-pattern counts: `generic_reconstruction_candidate` 0; `generic_defer_core` 0.
- Evidence/control warning reconciliation pass completed:
  - Old generic card-warning phrases now have exact-pattern count 0: `немає окремого файлу; прогалина лишається видимою`, `немає окремого synoptic/control file`, and `окремий cluster/context note не привязаний`.
  - Existing local evidence/control files were linked directly where detected.
  - Real remaining gaps were converted to explicit `TRUE_GAP` markers rather than ambiguous warning text.
  - Remaining gap inventory is recorded in `project/evidence-control-gap-audit-2026-07-18.md`.
- Evidence-note gap remediation completed for 23 logia: 12, 13, 15, 19, 43, 53, 61, 70, 71, 74, 80, 83, 84, 85, 87, 88, 98, 102, 105, 108, 110, 112, and 114. Current evidence-note `TRUE_GAP` count: 0.
- Synoptic/control gap classification completed for 47 logia. Current synoptic/control `TRUE_GAP` count: 0. Classification inventory is recorded in `project/synoptic-control-gap-classification-2026-07-18.md`:
  - `MERGE_WITH_EXISTING_CLUSTER`: 15
  - `MERGE_WITH_EXISTING_CONTROL`: 1
  - `CREATE_CONTROL_FILE_RESOLVED`: 17
  - `CREATE_CONTROL_FILE`: 0
  - `NO_DIRECT_CONTROL_RATIONALE`: 14
- Papyrus-boundary technical control package created and linked for Logia 24, 28, 29, 30, and 77: `controls/synoptic-parallels/logia-024-028-029-030-077-papyrus-boundary-controls.md`.
- Canonical/cluster technical control package created and linked for Logia 40, 48, and 62, with Logion 106 linked as internal control for 48: `controls/synoptic-parallels/logia-040-048-062-canonical-cluster-controls.md`.
- Wealth-renunciation / anti-world technical control package created and linked for Logia 81 and 110: `controls/synoptic-parallels/logia-081-110-wealth-renunciation-controls.md`.
- Image / preexistence / Adam / deathlessness technical control package created and linked for Logia 83, 84, and 85: `controls/synoptic-parallels/logia-083-084-085-image-preexistence-controls.md`.
- Body-soul anthropology technical control package created and linked for Logia 87 and 112: `controls/synoptic-parallels/logia-087-112-body-soul-controls.md`.
- Revelation/transmission technical control package created and linked for Logion 88: `controls/synoptic-parallels/logion-088-revelation-transmission-controls.md`.
- Mary/Peter/gender-transformation exclusion control package created and linked for Logion 114: `controls/synoptic-parallels/logion-114-mary-peter-gender-exclusion-controls.md`.
- Phase B metadata-coherence pass completed: 51 card gold-level evidence/control blocks, workflow-matrix evidence-note flags, and 23 stale all-114 decision-table rows were synchronized. Details: `project/card-decision-coherence-audit-2026-07-18.md`.
- Phase B.2 duplicate-status prose audit completed: old status headings were renamed, 0 local/gold-level decision conflicts remain, and split-core wording was normalized. Details: `project/duplicate-status-prose-audit-2026-07-18.md`.

## Recommended Fix Order

1. Continue print-safe appendix consolidation after the completed Greek-layer freeze, beginning with Logia 61-70.
2. Prepare the evidence dossier publication pass with source hierarchy, methodology, bibliography, and inclusion/exclusion defense.
3. Run the later Greek retroversion publication polish against academic editions after appendix and bibliography work, but do not reopen the basic witness-status freeze unless new source evidence is added.

## Validation Commands

```bash
python3 tools/qa_crosscheck.py
python3 tools/probability_reader_audit.py
git diff --check
```

## Recommended Next Prompt

Run print-safe full appendix editorial consolidation for Logia 61-70. Preserve the clean reader unchanged, remove card-export duplication, make each appendix section readable on paper without relying on clickable links, retain digital source/control paths in the scholarly layer, and rerun structural QA.
