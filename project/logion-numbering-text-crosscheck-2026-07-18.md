# Logion Numbering and Text Crosscheck

Date: 2026-07-18

## Purpose

This audit checks whether recent high-volume work introduced mistakes in logion numbering, ordering, clean-reader membership, or text/status synchronization.

The audit compares:

- `corpus/cards/logion-001.md` through `corpus/cards/logion-114.md`;
- `reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-uk.md`;
- clean-reader files in Ukrainian, English, Greek, Coptic, Arabic literary register, Ukrainian apparatus, and `parallel-edition.md`;
- `corpus/tables/logia-workflow-matrix.md`;
- `reconstruction/earliest-sayings-gospel/all-114-publication-decision-table-v0.1.md`;
- `reconstruction/earliest-sayings-gospel/inclusion-decisions-table.md`.

## Checks Passed

### 1. Corpus Cards

- Card files found: 114/114.
- Missing card files: none.
- Duplicate card numbers: none.
- Card filename / `# Logion N` heading mismatches: none.

### 2. Full Ukrainian Appendix

- Appendix logion headings: 114/114.
- Missing appendix logia: none.
- Duplicate appendix logia: none.
- Out-of-order appendix logia: none.
- `### Статус у реконструкції` sections: 114/114.
- `### Джерела й контрольні файли` sections: 114/114.

### 3. Clean-Reader Number Sets

All main clean-reader layers contain the same 34 logia/cores in the same order:

1, 2, 3, 4, 5, 6, 9, 10, 16, 20, 22, 25, 26, 31, 32, 33, 34, 35, 36, 39, 41, 45, 47, 54, 63, 72, 73, 86, 89, 95, 96, 99, 100, 107.

Files checked:

- `reconstructed-gospel-uk.md`
- `reconstructed-gospel-en.md`
- `reconstructed-gospel-greek.md`
- `reconstructed-gospel-coptic.md`
- `reconstructed-gospel-ar-quranic-register.md`
- `reconstructed-gospel-uk-apparatus.md`
- `parallel-edition.md`

The Arabic file uses `## قول N` headings, not `## Logion N`; this is a format difference, not a numbering error.

### 4. Clean Reader vs Workflow Matrix

- Workflow matrix rows: 114/114.
- Workflow `Reader text = YES`: 34.
- The workflow `Reader text = YES` set exactly matches the Ukrainian clean reader.

### 5. Clean Reader vs Parallel Edition

- Ukrainian clean-reader text and the Ukrainian column in `parallel-edition.md` match for all 34 current reader units after whitespace normalization.

## Defects Found And Remediation Status

### P0. Logion 63 Appendix Status Was Stale

Location:

- `reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-uk.md`, Logion 63.

Status: resolved in hotfix `project/ide-codex-logion-063-status-hotfix-v0.1-prompt.md`.

Problem:

The Logion 63 appendix section still says:

- `Reader status: Не включено: непевний матеріал`
- `Рішення: UNCERTAIN`
- `Не включено, бо наявних підстав поки недостатньо...`

But current control files say the opposite:

- `corpus/tables/logia-workflow-matrix.md`: Logion 63 has `Reader text = YES`.
- `all-114-publication-decision-table-v0.1.md`: Logion 63 has `READER_INCLUDE_MARKED`.
- `inclusion-decisions-table.md`: Logion 63 rich-fool core is `INCLUDE_WITH_MARKER`.
- All clean-reader language files include Logion 63.

Correct current status:

- Short rich-fool core: `INCLUDE_WITH_MARKER`.
- Full Logion 63: `UNCERTAIN`.
- Greek status: `Greek retroversion, hypothetical`.
- Reader implication: clean reader prints the short rich-fool core with Luke-dependence warning in the apparatus.

Resolution:

- The Logion 63 appendix section now says that the short rich-fool core is `INCLUDE_WITH_MARKER`.
- The section now includes `Чистий текст реконструкції`.
- It explicitly keeps the full Thomas logion `UNCERTAIN`.
- It identifies Luke 12:16-21 as the key canonical control and keeps Luke-dependence caution visible.

### P0. Logion 63 Evidence Note and Control File Used Pre-Promotion Language

Locations:

- `reconstruction/earliest-sayings-gospel/notes/logion-063-evidence-en.md`
- `controls/synoptic-parallels/logion-063-rich-fool-luke-control.md`

Status: resolved in hotfix `project/ide-codex-logion-063-status-hotfix-v0.1-prompt.md`.

Problem:

These files still describe Logion 63 as a candidate for later promotion or say that work is required before promotion. That was accurate before the controlled clean-reader candidate pass, but it is now stale.

Correct current status:

- Logion 63 has already been promoted into the clean reader as a marked short core.
- The note should now explain the inclusion rather than propose it.
- Remaining work should be framed as publication polish, full Coptic/source verification, and Luke-dependence caution, not as a blocker to reader inclusion.

Resolution:

- `notes/logion-063-evidence-en.md` is now v0.2 and post-promotion.
- `controls/synoptic-parallels/logion-063-rich-fool-luke-control.md` is now v0.2 and uses `READER_INCLUDE_MARKED` for the short core.
- Both files now frame remaining work as publication polish rather than a condition for reader inclusion.

### P1. Ukrainian Clean Reader Heading Format Differs From Other Main Layers

Location:

- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-uk.md`

Status: resolved as documented tooling behavior in `tools/qa_crosscheck.py` and `project/print-and-digital-publication-architecture.md`.

Observation:

The Ukrainian clean reader uses headings like `## 63`, while English, Greek, Coptic, Ukrainian apparatus, and most tooling expect explicit forms like `## Logion 63` or `## Логія 63`.

This is not a content error and does not confuse a human reader. It is a tooling and generation risk because simple cross-layer scripts can miss the Ukrainian file unless they know its special format.

Recommended decision:

- For final print, preserve simple visible numbering if desired.
- For source consistency, either standardize source headings to `## Логія N` and strip the word in print generation, or document the Ukrainian clean-reader heading exception in the generation pipeline.

### P1. Appendix Does Not Always Quote the Exact Clean-Reader Text

Observation:

Status: resolved by backfilling exact `Чистий текст реконструкції` anchors for all 34 clean-reader units.

For several clean-reader units, especially in not-yet-consolidated or earlier mixed sections, the appendix explains the logion but does not always reproduce the exact clean-reader wording as a clearly labeled text line.

This is not a numbering error. The clean reader and `parallel-edition.md` agree. But for publication quality, every appendix section should begin with or include a stable line:

- `Чистий текст реконструкції: ...`

For partial inclusions, it should also state:

- `У clean reader входить тільки ядро: ...`
- `Повна логія лишається в appendix / uncertain.`

This will prevent reader confusion and make print/digital generation safer.

## Remediation Plan

### Step 1. Fix Logion 63 Status Across Appendix and Notes

Priority: P0. Status: completed.

Actions:

1. Rewrite Logion 63 in `full-logion-commentary-appendix-uk.md` to match current decision:
   - short rich-fool core `INCLUDE_WITH_MARKER`;
   - full logion `UNCERTAIN`;
   - no extant Greek Thomas witness;
   - Luke 12:16-21 dependence remains possible.
2. Update `notes/logion-063-evidence-en.md` from candidate language to post-promotion rationale.
3. Update `controls/synoptic-parallels/logion-063-rich-fool-luke-control.md` from candidate language to current marked-reader control.
4. Verify Logion 63 remains present in all clean-reader language layers.

Acceptance criteria:

- No active checked file says Logion 63 is simply not included.
- All checked control files agree that the short core is included with marker and the full logion remains uncertain.

### Step 2. Add Exact Clean-Reader Text Anchors to Appendix

Priority: P1. Status: completed.

Actions:

1. During each future appendix consolidation package, add a stable line for included or partially included logia:
   - `Чистий текст реконструкції: ...`
2. For split-core logia, identify the printed core explicitly.
3. Backfill this line into already consolidated Logia 1-50 where useful, especially for partial-core cases.

Acceptance criteria:

- Every clean-reader logion has an exact Ukrainian clean-reader text line in its appendix section.
- Split-core logia clearly distinguish printed core from full Thomas form.

### Step 3. Standardize or Document Heading Formats

Priority: P1. Status: completed by documenting and tooling support.

Actions:

1. Decide whether source files should use explicit headings:
   - Ukrainian: `## Логія N`
   - English/Greek/Coptic: `## Logion N`
   - Arabic: `## قول N`
2. If clean print should show only numbers, make that a generation rule rather than a source-file inconsistency.
3. Add this rule to the print/digital generation architecture.

Acceptance criteria:

- Cross-layer scripts can parse all reader files without custom one-off assumptions.
- Print output can still display clean numbers only.

### Step 4. Add a Reusable Crosscheck Script

Priority: P1. Status: completed in `tools/qa_crosscheck.py`.

Actions:

Create a small project QA script that verifies:

- 114 card files;
- 114 appendix sections in order;
- 114 appendix source/control sections;
- clean-reader number sets match across Ukrainian, English, Greek, Coptic, Arabic, Ukrainian apparatus, and parallel edition;
- workflow `Reader text = YES` matches clean-reader files;
- all-114 `READER_INCLUDE_MARKED` rows match clean-reader files;
- every clean-reader logion has a corresponding appendix status that says included or partially included.

Acceptance criteria:

- The script exits nonzero on mismatch.
- The script prints a concise defect list.
- It can be run before every final publication/export pass.

## Recommended Next Action

Run `python3 tools/qa_crosscheck.py` before and after each major editorial pass, then continue print-safe full appendix editorial consolidation for Logia 81-90. After that, close the wealth/renunciation cluster-control group and move toward the evidence dossier publication pass.
