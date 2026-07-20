# IDE Codex Prompt: Full Appendix Editorial Consolidation 001-010 v0.1

## Project Goal

EUAGELIA presents a clean reconstructed sayings-gospel text first, then gives the reader a complete appendix for all 114 Gospel of Thomas logia. The appendix must become a coherent reader-facing commentary, not a stack of working layers.

## Next Logical Step

Execute the first controlled full-appendix editorial consolidation package: Logia 1-10.

This is the correct first package because the first appendix pages establish reader trust. They must show the final editorial pattern before the same method is applied to the rest of the appendix.

## Target File

- `reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-uk.md`

## Scope

Consolidate only:

- Logia 1, 2, 3, 4, 5, 6, 7, 8, 9, 10.

## Required Work

1. Remove duplicated `### Читацьке тлумачення з картки` blocks from Logia 1-10 after their content has been editorially absorbed.
2. Preserve source/evidence/control sections.
3. Preserve uncertainty and Greek witness cautions.
4. Preserve clean-reader decisions; do not promote or demote any logion.
5. Convert skeleton-style sections into real reader-facing commentary, especially Logia 7 and 8.
6. Keep included, partial, uncertain, and appendix-only logia equally serious.
7. Make each section readable as one coherent appendix entry, not as a pasted card excerpt.

## Desired Section Pattern

For each logion:

- `### Статус у реконструкції`
- `### Що це за матеріал`
- `### Чому включено / не включено`
- `### Можливі тлумачення`
- `### Непевність і межі`
- `### Джерела й контрольні файли`
- `### Що треба допрацювати`

Do not force the pattern mechanically if an existing section already reads well, but the first ten entries should converge toward this structure.

## Acceptance Criteria

- Logia 1-10 contain no `### Читацьке тлумачення з картки` subsection.
- Logia 1-10 contain no sentence `Цей опис узято з робочого індексу логій`.
- Logia 7 and 8 are no longer skeleton entries.
- Appendix still has 114 logion headings.
- Appendix still has 114 source sections.
- `git diff --check` passes.

