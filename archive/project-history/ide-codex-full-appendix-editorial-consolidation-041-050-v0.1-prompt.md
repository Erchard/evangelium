# IDE Codex Prompt: Full Appendix Editorial Consolidation, Logia 41-50 v0.1

You are working in the EUAGELIA project.

## Goal

Continue publication-level, print-safe editorial consolidation of the Ukrainian full 114-logion appendix by editing Logia 41-50 in:

- `reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-uk.md`

This project presents a clean reconstructed earliest sayings-gospel text first, then gives the reader a complete appendix for all 114 Gospel of Thomas logia, including included, marked, uncertain, deferred, appendix-only, and excluded material. The appendix must be readable on paper without clickable links, while still preserving enough source/control information for the digital scholarly companion.

## Current State

- Full appendix has 114 logion sections.
- Logia 1-40 have already been editorially consolidated.
- Logia 41-114 still contain duplicated `### Читацьке тлумачення з картки` blocks and, in many cases, working-index navigation prose.
- Current remaining counts before this package:
  - 74 `### Читацьке тлумачення з картки` blocks.
  - 56 working-index navigation phrases: `Цей опис узято з робочого індексу логій`.

## Task

Edit Logia 41-50 only.

For each logion:

1. Preserve the current reconstruction decision unless the existing evidence files clearly require a correction.
2. Remove the separate `### Читацьке тлумачення з картки` block.
3. Remove working-index navigation prose.
4. Integrate the useful interpretive material into the main reader-facing commentary.
5. Keep the Ukrainian prose suitable for a non-specialist reader:
   - explain what the saying appears to mean;
   - explain why it is included, marked, uncertain, deferred, or excluded;
   - explain possible interpretations without turning them into claims of certainty;
   - explain uncertainty in plain language.
6. Preserve source/control sections as separable apparatus sections:
   - cite P.Oxy. witnesses where extant;
   - distinguish extant Greek from hypothetical Greek retroversion;
   - distinguish Coptic NHC II from Greek papyrus witnesses and canonical controls;
   - do not rely on clickable repository paths for paper-reader comprehension.
7. Add or normalize `### Непевність і межі` for every edited logion.

## Special Attention

- Logion 41: included/marked material about having and receiving more; explain relation to Mark 4:25 / Matt 13:12 / Luke 8:18 / Luke 19:26 without overclaiming Thomas Greek evidence.
- Logion 42: very short appendix-only saying; avoid pretending a one-word imperative has more evidential support than it has.
- Logion 43: polemical identity saying; keep it appendix-only unless stronger evidence is present.
- Logion 44: blasphemy saying; explain synoptic control but preserve uncertainty about Thomas form and theological development.
- Logion 45: tree-fruit / heart-mouth complex; included with marker if that is the current project decision, but clearly mark composition and control limits.
- Logion 46: John the Baptist / least in kingdom comparison; explain synoptic strength and Thomas form limits.
- Logion 47: split-core saying; preserve the current partial reader decision for 47B and explain why the full logion remains uncertain.
- Logion 48: agreement / mountain-moving saying; explain relation to unity/presence cluster and Matt 18:19-20 without premature inclusion.
- Logion 49: solitary/elect saying; explain monachos/unity theme and why it remains appendix-only.
- Logion 50: light/origin/election/sign saying; explain symbolic value and why it remains appendix-only.

## Deliverables

1. Updated `reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-uk.md`.
2. New completion audit:
   - `reconstruction/earliest-sayings-gospel/full-appendix-editorial-consolidation-041-050-v0.1.md`
3. Updated project documentation where it names the current appendix consolidation state and next step:
   - `README.md`
   - `project/project-map.md`
   - `project/project-completion-roadmap.md`
   - `project/project-quality-audit-v0.1.md`
   - `project/repository-structure.md`
   - `reconstruction/earliest-sayings-gospel/README.md`

## Verification

Run checks confirming:

- appendix still has 114 `## Логія` headings;
- appendix still has 114 `### Джерела й контрольні файли` sections;
- Logia 41-50 contain no `### Читацьке тлумачення з картки`;
- Logia 41-50 contain no working-index navigation prose;
- Logia 41-50 each contain `### Непевність і межі`;
- global remaining `### Читацьке тлумачення з картки` count decreases from 74 to 64;
- global remaining working-index navigation phrase count decreases from 56 to 47.

## Output Discipline

Do not finalize the whole project in this pass. This is one controlled publication-quality package. Preserve uncertainty, avoid speculative certainty, and keep the clean reconstruction selective.
