# IDE Codex Prompt: Quality Remediation Master Pass v0.1

You are working in the EUAGELIA project. Your task is to execute the quality-remediation plan with maximum scholarly care, preserving the final goal of the project: a clean Ukrainian reconstruction of the earliest reachable sayings gospel, supported by Coptic, Greek, English, full commentary, and a defensible English evidence dossier.

## Core Documents To Read First

Read these before making changes:

1. `project/project-quality-audit-v0.1.md`
2. `project/project-quality-remediation-plan-v0.1.md`
3. `project/project-completion-roadmap.md`
4. `project/final-product-specification.md`
5. `project/clean-text-plus-commentary-concept.md`
6. `project/clean-reader-text-first-page-principle.md`
7. `sources/primary_texts/source-register.md`
8. `corpus/tables/logia-workflow-matrix.md`
9. `corpus/cards/five-source-apparatus-audit-v0.1.md`
10. `corpus/cards/canonical-greek-extraction-audit-v0.1.md`

## Non-Negotiable Principles

- Do not pollute the clean reader with comments, status labels, brackets, disclaimers, or scholarly apparatus.
- Treat the Coptic NHC II text as the main preserved base witness where Greek Thomas is absent.
- Treat extant Greek papyri as witnesses only where they are actually preserved.
- Treat Greek retroversion as hypothetical reconstruction, never as a manuscript witness.
- Do not invent primary text. If a line cannot be extracted or verified, say so explicitly.
- Do not treat canonical Greek parallels as Thomas witnesses. They are control/reconstruction aids only.
- Explain excluded/deferred logia with the same seriousness as included logia.
- Preserve Thomas logion numbering for reader navigation.
- Leave an audit trail for every major pass.

## Execution Strategy

Work in controlled phases. Do not try to polish everything at once. At the start of each run, identify the highest-priority unfinished phase from `project/project-quality-remediation-plan-v0.1.md`, then execute that phase as completely as possible.

Current project status after execution:

- Phase 1, P.Oxy. XML Extraction Cleanup, has been completed in `corpus/cards/poxy-xml-extraction-audit-v0.1.md`.
- Phase 2, Documentation Sync Pass, has received a basic sync after P.Oxy. cleanup.
- Phase 3, Evidence and Control Inventory, has been completed in `reconstruction/earliest-sayings-gospel/evidence-control-inventory-v0.1.md`.
- Phase 4, True All-114 Publication Decision Table, has been completed in `reconstruction/earliest-sayings-gospel/all-114-publication-decision-table-v0.1.md`.
- Phase 5 has started. The first P1 non-reader appendix package has been completed in `reconstruction/earliest-sayings-gospel/full-appendix-p1-non-reader-package-v0.1.md`.
- The first P1 non-reader evidence-rationale pass has been completed in `reconstruction/earliest-sayings-gospel/p1-non-reader-evidence-rationale-pass-v0.1.md`.

Current recommended next phase:

**Phase 5. Full Appendix Expansion**

Continue the Phase 5 evidence/no-note rationale pass for the remaining `NEEDS_EVIDENCE_BEFORE_FINAL` logia. The first P1 package is complete; do not repeat Logia 23, 24, 28, 29, 30, 37, 38, 75, 77, 104, or 106 except for later deeper technical control notes.

## Completed Phase 1 Specific Instructions

### Target Logia

Update these 8 cards if the XML supports card-ready extraction:

- P.Oxy. 1: logia 27, 28, 29, 30, 77;
- P.Oxy. 655: logia 24, 37, 38.

### Source XML Files

- `sources/primary_texts/greek_poxy/dclp-poxy1-62838.xml`
- `sources/primary_texts/greek_poxy/dclp-poxy655-62839.xml`

### Required Work

1. Inspect the TEI/XML structure carefully.
2. Extract only text that can be responsibly tied to the relevant logion.
3. Preserve uncertainty:
   - extant letters;
   - lacunae;
   - supplied/restored text;
   - editorial uncertainty;
   - unusable or unassignable fragments.
4. Replace `pending local line extraction` in the relevant card only when a real extract has been made.
5. If extraction cannot be responsibly completed, replace the vague pending note with a precise explanation of why.
6. Update the card's five-source apparatus, not the clean reader.
7. Create `corpus/cards/poxy-xml-extraction-audit-v0.1.md` documenting:
   - source files used;
   - logia updated;
   - logia still unresolved;
   - extraction limits;
   - how lacunae/supplied text were handled.
8. Update `sources/primary_texts/collection-log.md`.
9. Update project status docs only if they mention the pending P.Oxy. gap.

### Quality Bar

The result must make the source layer more honest, not merely prettier. It is acceptable to leave a logion unresolved if the XML does not support a responsible extraction. It is not acceptable to silently turn uncertain restorations into secure Greek.

## Completed Phase 3 Work

Phase 3 created:

- `reconstruction/earliest-sayings-gospel/evidence-control-inventory-v0.1.md`

Key findings:

- no clean-reader unit lacks an evidence trail;
- 65 logia have direct evidence-note coverage after the first P1 evidence-rationale pass;
- workflow matrix evidence-note status is aligned for the first P1 package;
- 27 logia remain P1 evidence/control targets;
- 22 logia are P2 appendix/no-note-rationale targets.

## Completed Phase 4 Work

Phase 4 created:

- `reconstruction/earliest-sayings-gospel/all-114-publication-decision-table-v0.1.md`

Key findings:

- 114/114 logia are covered;
- 34 units remain `READER_INCLUDE_MARKED`;
- 26 non-reader rows need evidence/no-note rationale before final publication after the first P1 evidence-rationale pass;
- the clean reader was not expanded in this pass.

## Completed Phase 5 Work So Far

Phase 5 first package created:

- `project/ide-codex-full-appendix-p1-non-reader-package-v0.1-prompt.md`
- `project/ide-codex-p1-non-reader-evidence-rationale-v0.1-prompt.md`
- `reconstruction/earliest-sayings-gospel/full-appendix-p1-non-reader-package-v0.1.md`
- `reconstruction/earliest-sayings-gospel/p1-non-reader-evidence-rationale-pass-v0.1.md`

Expanded appendix sections:

- 23, 24, 28, 29, 30, 37, 38, 75, 77, 104, 106.

The clean reader was not changed.

Direct evidence notes now exist for all 11 first-package logia.

## Current Next Work

Proceed within Phase 5:

**Evidence / No-Note Rationale Pass For Remaining P1 Logia**

Required work:

- create evidence/no-note rationale files for the remaining P1 rows still marked `NEEDS_EVIDENCE_BEFORE_FINAL`;
- use existing cards and appendix sections as summaries, not as replacements for evidence files;
- prioritize logia with stronger controls or higher interpretive value before low-information rows;
- keep canonical parallels as controls, not Thomas witnesses;
- do not change the clean reader unless a separate decision pass is created.

## Required Final Report For Each Run

At the end of the run, report:

- files changed;
- logia affected;
- what became more reliable;
- what remains unresolved;
- next recommended phase.

If changes were made, commit them with a clear message and push to the remote branch, unless explicitly told not to.
