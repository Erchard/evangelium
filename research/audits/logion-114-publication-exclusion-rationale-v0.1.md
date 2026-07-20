# Logion 114 Publication Exclusion Rationale Pass v0.1

Status: completed 2026-07-18.

## Scope

This pass created a publication-facing rationale for excluding Logion 114 from the clean reconstructed earliest sayings gospel while preserving it in the appendix.

Target files:

- `corpus/cards/logion-114.md`
- `reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-uk.md`
- `reconstruction/earliest-sayings-gospel/evidence-dossier-en.md`
- `reconstruction/earliest-sayings-gospel/all-114-publication-decision-table-v0.1.md`
- `corpus/tables/logia-workflow-matrix.md`

## Created

- `reconstruction/earliest-sayings-gospel/notes/logion-114-exclusion-rationale-en.md`

## Decision

No clean-reader membership changed.

Logion 114 remains:

- Decision: `EXCLUDE_AS_SECONDARY`.
- Reader text: NO.
- Greek witness status: No loaded P.Oxy. witness.
- Coptic witness: NHC II,2 preserved in the project corpus.

## Rationale Summary

Logion 114 is excluded because it is a developed dialogue scene involving Peter, Mary, gendered worthiness, transformation into male, and access to the kingdom. It lacks a loaded Greek Thomas witness and lacks direct synoptic wording control. Internal Thomas parallels such as Logion 22 and Logion 13 are useful for context but do not make the unit a clean early sayings-gospel core.

The exclusion is not censorship. The logion remains in the full appendix with source text, translation, interpretation, and rationale. It should be used in the evidence dossier as a transparent example of how secondary material is handled.

## Validation Required

Run after updates:

```bash
python3 tools/qa_crosscheck.py
git diff --check
```

## Next Recommended Step

Proceed to the evidence dossier publication pass. The dossier can now use Logion 114 as a fully documented exclusion example.
