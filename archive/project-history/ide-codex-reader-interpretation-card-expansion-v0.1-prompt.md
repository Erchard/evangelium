# IDE Codex Prompt: Reader-Facing Interpretation Expansion for All Logion Cards v0.1

## Project Goal

The project reconstructs the earliest recoverable gospel-like sayings collection behind or alongside the Gospel of Thomas. The final publication must give readers:

- a clean reconstructed text without comments, brackets, status labels, or disclaimers;
- a full appendix for every Thomas logion, including logia excluded from the reconstruction;
- transparent evidence for inclusion, exclusion, uncertainty, and cluster-level decisions;
- source-language control through Coptic, extant Greek papyri, Greek retroversion, and canonical Greek parallels where relevant.

## Task

Improve the interpretive layer in every corpus card, `corpus/cards/logion-001.md` through `corpus/cards/logion-114.md`.

Add or replace a dedicated Ukrainian section:

`## Читацьке тлумачення`

This section must be written for a thoughtful non-specialist reader, not as a text-critical student outline. It must explain what the saying may mean, why it matters, and why the project includes, marks, defers, or excludes it.

## Required Structure per Card

Each card must include:

1. `### Простий сенс`
   - Explain the plain meaning of the logion in ordinary Ukrainian.
   - Avoid assuming the reader already knows Thomasine studies, Coptic, Greek, Q, synoptic redaction, or Nag Hammadi context.

2. `### Як це можна розуміти`
   - Present several plausible interpretive options.
   - Include spiritual, ethical, social, literary, and reconstruction-oriented readings where appropriate.
   - Make clear that multiple interpretations can coexist when the evidence does not force one reading.

3. `### Чому це важливо для реконструкції`
   - Explain how this logion functions in the project.
   - For included logia: explain why a reconstructed core is plausible.
   - For `INCLUDE_WITH_MARKER`: explain what is printed cleanly and what remains uncertain.
   - For `UNCERTAIN`, `APPENDIX_ONLY_UNCERTAIN`, or `DEFER_TO_CLUSTER`: explain why the saying is useful but not safe as clean text yet.
   - For `EXCLUDE_AS_SECONDARY`: explain why exclusion is part of intellectual honesty, not dismissal.

4. `### Обережність`
   - Name the main interpretive risk in plain language.
   - Mention manuscript limits when relevant: Coptic translation base, no extant Greek witness, lacunose Greek witness, or canonical dependence risk.
   - Avoid overclaiming historical certainty.

## Quality Standard

- Write in clear Ukrainian prose.
- Do not write compressed notes.
- Do not merely repeat the decision table.
- Do not turn commentary into devotional preaching.
- Do not erase uncertainty.
- Treat excluded and deferred logia with the same seriousness as included logia.
- Keep the clean reconstructed text separate from commentary.

## Deliverables

- Updated `corpus/cards/logion-001.md` through `corpus/cards/logion-114.md`.
- A short audit file documenting coverage and limits of the pass.
- Documentation updates that make the new reader-facing interpretation layer discoverable.
- Verification that all 114 logion cards contain `## Читацьке тлумачення`.

