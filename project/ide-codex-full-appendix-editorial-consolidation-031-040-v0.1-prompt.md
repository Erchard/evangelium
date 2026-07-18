# IDE Codex Prompt: Print-Safe Full Appendix Editorial Consolidation, Logia 31-40 v0.1

## Goal

Continue print-safe publication-level editorial consolidation of the Ukrainian full 114-logion appendix by editing Logia 31-40 in:

- `reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-uk.md`

This package follows the completed packages for Logia 1-10, 11-20, and 21-30. It must preserve the clean-reader decisions while making each appendix chapter usable in a future paper book without relying on clickable repository links.

## Controlling Documents

Use:

- `project/print-and-digital-publication-architecture.md`
- `project/clean-text-plus-commentary-concept.md`
- `project/final-product-specification.md`
- `reconstruction/earliest-sayings-gospel/full-appendix-editorial-consolidation-021-030-v0.1.md`

## Scope

Edit only the full appendix chapters for:

- Logion 31
- Logion 32
- Logion 33
- Logion 34
- Logion 35
- Logion 36
- Logion 37
- Logion 38
- Logion 39
- Logion 40

Do not change the clean reader or inclusion decisions.

## Required Work

For each of Logia 31-40:

1. Remove the separate `### Читацьке тлумачення з картки` block.
2. Remove the working-index skeleton sentence where present.
3. Integrate useful content into a single coherent Ukrainian reader-facing chapter.
4. Add or normalize `### Непевність і межі`.
5. Preserve source/control sections in a separable apparatus layer.
6. Use print-safe references in reader prose: logion numbers, witness labels, canonical references, and plain-language explanation.
7. Clearly distinguish extant Greek, partial Greek, fragmentary Greek, and hypothetical retroversion.

## Logion-Specific Guidance

- Logion 31: preserve `INCLUDE_WITH_MARKER`; explain prophet-in-hometown core and lower-confidence physician clause.
- Logion 32: preserve `INCLUDE_WITH_MARKER`; explain city-on-hill visibility and the uncertain "will not fall" expansion.
- Logion 33: preserve `INCLUDE_WITH_MARKER`; explain two-unit composition: ear/rooftops and lamp. P.Oxy. 1 supports the opening only.
- Logion 34: preserve `INCLUDE_WITH_MARKER`; explain blind-leading-blind as strong synoptic control but Greek Thomas is hypothetical.
- Logion 35: preserve `INCLUDE_WITH_MARKER`; explain strong-man saying and avoid overloading it with later exorcistic interpretation.
- Logion 36: preserve `INCLUDE_WITH_MARKER`; explain anxiety/clothing, P.Oxy. 655 restoration, P.Oxy. 5575 control, and Matt/Luke complex.
- Logion 37: keep appendix-only `UNCERTAIN`; explain nakedness/no-shame/children/Son of the Living One and P.Oxy. 655 support.
- Logion 38: keep appendix-only `UNCERTAIN`; explain desire to hear, future seeking, and P.Oxy. 655 fragmentary status.
- Logion 39: preserve `INCLUDE_WITH_MARKER`; explain keys of knowledge plus wise-serpents/pure-doves composition and P.Oxy. 655.
- Logion 40: keep `UNCERTAIN`; explain plant not planted by Father and Matt 15:13 control, without treating it as secure early Thomas.

## Documentation Updates

After editing, update:

- `README.md`
- `project/project-map.md`
- `project/project-completion-roadmap.md`
- `project/project-quality-audit-v0.1.md`
- `project/documentation-refresh-2026-07-18-v0.1.md`
- `reconstruction/earliest-sayings-gospel/README.md`

Create:

- `reconstruction/earliest-sayings-gospel/full-appendix-editorial-consolidation-031-040-v0.1.md`

## Acceptance Checks

Verify:

- appendix still has 114 logion headings;
- appendix still has 114 `### Джерела й контрольні файли` sections;
- Logia 31-40 contain no `### Читацьке тлумачення з картки`;
- Logia 31-40 contain no `Цей опис узято з робочого індексу логій`;
- Logia 31-40 each contain `### Непевність і межі`;
- remaining card-derived appendix blocks decrease from 84 to 74;
- remaining working-index skeleton phrases decrease from 57 to the verified new count;
- `git diff --check` passes.

## Output Summary

Report:

- prompt file created;
- appendix package completed;
- documentation updated;
- verification counts;
- next logical step.
