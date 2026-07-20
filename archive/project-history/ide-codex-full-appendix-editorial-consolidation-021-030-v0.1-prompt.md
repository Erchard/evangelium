# IDE Codex Prompt: Print-Safe Full Appendix Editorial Consolidation, Logia 21-30 v0.1

## Goal

Continue publication-level editorial consolidation of the Ukrainian full 114-logion appendix by editing Logia 21-30 in:

- `reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-uk.md`

This package must follow the new print/digital publication architecture:

- paper-facing prose must be self-contained;
- repository paths may remain only in separable source/control sections;
- every important source or parallel reference needs a print-safe equivalent.

## Controlling Documents

Use these as binding context:

- `project/print-and-digital-publication-architecture.md`
- `project/clean-text-plus-commentary-concept.md`
- `project/final-product-specification.md`
- `project/project-quality-audit-v0.1.md`
- `reconstruction/earliest-sayings-gospel/full-appendix-editorial-consolidation-001-010-v0.1.md`
- `reconstruction/earliest-sayings-gospel/full-appendix-editorial-consolidation-011-020-v0.1.md`

## Scope

Edit only the full appendix chapters for:

- Logion 21
- Logion 22
- Logion 23
- Logion 24
- Logion 25
- Logion 26
- Logion 27
- Logion 28
- Logion 29
- Logion 30

Do not change the clean reader text or the inclusion decisions in this pass.

## Required Work

For each of Logia 21-30:

1. Remove the separate `### Читацьке тлумачення з картки` block.
2. Remove the working-index skeleton sentence where present.
3. Integrate useful content from the old card-derived block into one coherent reader-facing chapter.
4. Preserve the current reconstruction status and decision.
5. Preserve source/control material, but keep repository paths in the source/control layer rather than in the main prose.
6. Add or normalize `### Непевність і межі`.
7. Make the prose print-safe: use logion numbers, witness names, canonical references, and plain-language explanation.
8. Avoid raw technical language in reader-facing prose unless it is explained.

## Logion-Specific Guidance

- Logion 21: treat as appendix-only `UNCERTAIN`; explain the composite field/children/thief/watchfulness/harvest material and why it needs subunit splitting.
- Logion 22: preserve the included children/kingdom core with marker; explain why the unity expansion remains apparatus-only.
- Logion 23: keep appendix-only / cluster-deferred; explain election and unity without treating internal Thomas coherence as direct evidence of earliest origin.
- Logion 24: keep deferred; explain the light-person saying and the uncertain P.Oxy. 655 relationship.
- Logion 25: preserve included status with marker; explain brother-love, soul, and apple-of-eye language with print-safe biblical controls.
- Logion 26: preserve included status with marker; explain speck/log saying with P.Oxy. 1 partial control and Matt/Luke parallels.
- Logion 27: keep appendix-only `UNCERTAIN`; explain fasting from the world and true Sabbath as ritual-symbolic language.
- Logion 28: keep appendix-only `UNCERTAIN`; explain world/drunkenness/thirst/blindness and partial P.Oxy. 1 control.
- Logion 29: keep `DEFER`; explain flesh/spirit/body and wealth-in-poverty as anthropological cluster material.
- Logion 30: keep appendix-only / cluster-deferred; explain the textually complex one/two/three and Jesus-presence problem, including relation to Logion 77b and Matt 18:20.

## Documentation Updates

After editing, update:

- `README.md`
- `project/project-map.md`
- `project/project-completion-roadmap.md`
- `project/project-quality-audit-v0.1.md`
- `project/documentation-refresh-2026-07-18-v0.1.md`
- `reconstruction/earliest-sayings-gospel/README.md`

Create:

- `reconstruction/earliest-sayings-gospel/full-appendix-editorial-consolidation-021-030-v0.1.md`

## Acceptance Checks

Verify:

- appendix still has 114 logion headings;
- appendix still has 114 `### Джерела й контрольні файли` sections;
- Logia 21-30 contain no `### Читацьке тлумачення з картки`;
- Logia 21-30 contain no `Цей опис узято з робочого індексу логій`;
- Logia 21-30 each contain `### Непевність і межі`;
- remaining card-derived appendix blocks decrease from 94 to 84;
- remaining working-index skeleton phrases decrease from 59 to the verified new count;
- `git diff --check` passes.

## Output Summary

Report:

- prompt file created;
- appendix package completed;
- documentation updated;
- verification counts;
- next logical step.
