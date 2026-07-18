# IDE Codex Prompt: Full Appendix Editorial Consolidation, Logia 51-60 v0.1

## Mission

Continue the publication-quality editorial consolidation of the Ukrainian full 114-logion appendix by rewriting Logia 51-60 as integrated, print-safe reader-facing appendix chapters.

This is the next logical step because the project already has:

- 114/114 logion cards;
- 114/114 appendix sections;
- synchronized 34-unit clean reader across Ukrainian, English, Greek, Coptic, Arabic literary, apparatus, and parallel layers;
- reusable structural QA in `tools/qa_crosscheck.py`;
- editorial consolidation completed for Logia 1-50.

The current weakest public-facing layer is not corpus coverage but the uneven appendix prose after Logion 50.

## Files To Use

Primary target:

- `reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-uk.md`

Controls:

- `corpus/cards/logion-051.md` through `corpus/cards/logion-060.md`
- `reconstruction/earliest-sayings-gospel/all-114-publication-decision-table-v0.1.md`
- `corpus/tables/logia-workflow-matrix.md`
- `reconstruction/earliest-sayings-gospel/notes/living-dead-world-cluster-control-en.md`
- `reconstruction/earliest-sayings-gospel/notes/beatitudes-cluster-control-en.md`
- `reconstruction/earliest-sayings-gospel/notes/family-renunciation-cluster-control-en.md`
- `project/print-and-digital-publication-architecture.md`
- `tools/qa_crosscheck.py`

Output audit:

- `reconstruction/earliest-sayings-gospel/full-appendix-editorial-consolidation-051-060-v0.1.md`

## Editorial Requirements

For Logia 51-60:

1. Remove separate `### Читацьке тлумачення з картки` blocks.
2. Remove working-index phrases such as `Попередній шар...` and `Цей опис узято...`.
3. Preserve all current decisions. Do not promote or demote any logion.
4. Keep Logion 54 in the clean reader as `INCLUDE_WITH_MARKER`.
5. Keep Logia 51, 52, 55, 56, 57, 58, 59, and 60 appendix-only `UNCERTAIN`.
6. Keep Logion 53 appendix-only `DEFER`.
7. Keep all `### Джерела й контрольні файли` sections so the digital scholarly companion remains separable.
8. Add or normalize `### Непевність і межі` in every edited section.
9. Write prose for a normal thoughtful reader, not only for a textual critic.
10. Maintain print-safe references: use logion numbers, witness labels, canonical references, and cluster names in the reader-facing prose; keep repository paths only in the source/control sections.

## Quality Bar

Each edited logion should answer, in clear Ukrainian:

- what the saying appears to say;
- why it matters;
- what interpretations are plausible;
- why it is included, not included, or deferred;
- what remains uncertain;
- which source/control materials support the decision.

Do not add comments into the clean reader. Do not change the 34-unit reader set.

## Verification

Before and after the edit, run:

```bash
python3 tools/qa_crosscheck.py
```

After editing, also check:

```bash
rg -n "Читацьке тлумачення з картки|Цей опис узято з робочого індексу|Попередній шар" reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-uk.md
```

For this pass, there should be no such hits inside Logia 51-60.

## Expected Result

- Logia 51-60 read as coherent appendix chapters.
- Source/control sections remain intact.
- QA crosscheck passes.
- A short audit file records decisions preserved, what changed, and the next recommended step.
