# IDE Codex Prompt: Full Appendix Editorial Consolidation, Logia 11-20 v0.1

## Goal

Continue the full reader-facing appendix consolidation for the reconstructed earliest sayings gospel project by editing Logia 11-20 in:

- `reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-uk.md`

The purpose is to turn the synchronized card-derived working blocks into polished Ukrainian appendix chapters that an ordinary reader can understand, while preserving the scholarly transparency needed for publication.

## Project Context

The final project has two layers:

1. A clean reconstructed text, printed first, with only numbered logia and no commentary, brackets, confidence labels, or apparatus.
2. A full appendix covering all 114 logia, including included, partly included, uncertain, deferred, and excluded material.

Logia rejected from the reconstruction must still receive serious appendix treatment: source texts, parallels, interpretation, and a clear explanation of why they are not printed in the clean reconstructed text.

Logia 1-10 have already been editorially consolidated and should be used as the style model for this pass.

## Scope

Edit only the appendix chapters for:

- Logion 11
- Logion 12
- Logion 13
- Logion 14
- Logion 15
- Logion 16
- Logion 17
- Logion 18
- Logion 19
- Logion 20

Do not revise the clean reader text in this pass.

## Required Work

For each of Logia 11-20:

1. Remove the section titled `### Читацьке тлумачення з картки`.
2. Remove any sentence saying that the description was taken from the working logia index.
3. Replace the working/card-derived material with a coherent reader-facing commentary.
4. Preserve the existing factual decision: included, partly included, uncertain, deferred, or appendix-only.
5. Preserve all source-control sections and project file references already present in the appendix.
6. Add or normalize a section titled `### Непевність і межі`.
7. Make clear why the logion is included, partly included, deferred, uncertain, or not included.
8. Explain plausible interpretations in plain Ukrainian prose, not in telegraphic research notes.

## Quality Bar

Each chapter should let a reader answer:

- What does this saying appear to say?
- Why does the project treat it this way?
- What are the strongest early-tradition arguments?
- What are the strongest reasons for caution?
- How can the saying be interpreted without forcing a single dogmatic reading?

The writing should be clear, calm, and transparent. It should not overclaim. Where Greek is reconstructed rather than extant, say so plainly.

## Special Attention

- Logion 11: keep the full logion appendix-only, but explain the controlled heaven-passing subunit and the living/dead/world cluster.
- Logion 12: explain why James succession material is historically important but not a secure earliest sayings-gospel unit.
- Logion 13: treat Thomas authority and secret-words framing as collection-level material.
- Logion 14: explain the composite structure: ritual critique, mission hospitality, and mouth-defilement saying.
- Logion 15: explain the uncertainty around "not born of woman" and Father recognition.
- Logion 16: keep the division/household-conflict core as partly included, while keeping fire/sword/war and monachos material in the apparatus.
- Logion 17: explain the relation to hidden/revealed wisdom traditions and 1 Cor 2:9 / Isa 64:4 controls.
- Logion 18: explain beginning/end and "not taste death" as important but not yet clean-reader material.
- Logion 19: explain the composite pre-existence/five-trees/deathlessness material.
- Logion 20: keep the mustard seed as included with marker, while stating that Thomas Greek is retroverted here.

## Documentation Updates

After editing the appendix, update:

- `README.md`
- `project/project-map.md`
- `project/project-completion-roadmap.md`
- `project/project-quality-audit-v0.1.md`
- `reconstruction/earliest-sayings-gospel/README.md`

Create a short completion audit:

- `reconstruction/earliest-sayings-gospel/full-appendix-editorial-consolidation-011-020-v0.1.md`

## Acceptance Checks

Run checks confirming:

- The appendix still has 114 logion headings.
- The appendix still has 114 `### Джерела й контрольні файли` sections.
- Logia 11-20 no longer contain `### Читацьке тлумачення з картки`.
- Logia 11-20 no longer contain `Цей опис узято з робочого індексу логій`.
- Logia 11-20 each contain `### Непевність і межі`.
- `git diff --check` passes.

Report the final counts in the completion note.
