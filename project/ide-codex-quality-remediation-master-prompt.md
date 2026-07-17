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

Current recommended first phase:

**Phase 1. P.Oxy. XML Extraction Cleanup**

Close the pending P.Oxy. XML extraction gap before finalizing all-114 decisions.

## Phase 1 Specific Instructions

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

## After Phase 1

If Phase 1 is complete, proceed to Phase 2:

**Documentation Sync Pass**

Fix the internal documentation contradictions found in `project-quality-audit-v0.1.md`, especially:

- roadmap duplicate numbering;
- nearest-action ambiguity;
- publication gap audit filename/title mismatch or version note;
- evidence-note statistics mismatch;
- SBLGNT vs SYN-MATT/SYN-MARK/SYN-LUKE source-register ambiguity.

## Required Final Report For Each Run

At the end of the run, report:

- files changed;
- logia affected;
- what became more reliable;
- what remains unresolved;
- next recommended phase.

If changes were made, commit them with a clear message and push to the remote branch, unless explicitly told not to.

