# Documentation Refresh 2026-07-18 v0.1

## Scope

This pass updated active project documentation after the print/digital publication architecture decision, the completion of full appendix editorial consolidation packages for Logia 1-80, the technical-debt closure pass, and the Greek-layer freeze.

## Current Canonical Status

- Clean Ukrainian reader: 37 logia or included cores.
- English, Coptic, Greek, and parallel layers: synchronized for the current 37-unit reader.
- Full 114-logion appendix: 114/114 logion sections.
- Appendix source/control sections: 114/114.
- Appendix editorial consolidation: Logia 1-80 complete.
- Remaining unconsolidated card-derived appendix blocks: 31.
- Remaining working-index skeleton phrases: 20.
- Evidence/control inventory: complete.
- All-114 publication decision table: complete v0.1.
- `NEEDS_EVIDENCE_BEFORE_FINAL`: 0.
- Print/digital publication architecture: complete v0.1.
- Technical QA baseline: complete in `tools/qa_crosscheck.py`.
- Exact clean-text anchors in full appendix: complete for all 37 current clean-reader units.

## Documents Updated

- `README.md`
- `project/project-map.md`
- `project/project-completion-roadmap.md`
- `project/project-quality-audit-v0.1.md`
- `project/project-quality-remediation-plan-v0.1.md`
- `project/technical-debt-closure-2026-07-18.md`
- `project/repository-structure.md`
- `project/publication-gap-audit-v0.2.md`
- `project/final-product-specification.md`
- `project/clean-text-plus-commentary-concept.md`
- `project/logion-card-gold-standard.md`
- `reconstruction/earliest-sayings-gospel/README.md`
- `reconstruction/earliest-sayings-gospel/all-114-publication-decision-table-v0.1.md`
- `reconstruction/earliest-sayings-gospel/final-all-114-decision-audit-v0.1.md`
- `reconstruction/earliest-sayings-gospel/controlled-clean-reader-candidate-pass-v0.1.md`
- `reconstruction/earliest-sayings-gospel/split-core-decision-review-a-v0.1.md`
- `reconstruction/earliest-sayings-gospel/split-core-decision-review-b-v0.1.md`
- `reconstruction/earliest-sayings-gospel/full-appendix-editorial-consolidation-001-010-v0.1.md`
- `reconstruction/earliest-sayings-gospel/full-appendix-editorial-consolidation-051-060-v0.1.md`

## Main Corrections

- Replaced older descriptions of the full appendix as a mostly skeletal expansion target with the current state: full 114-section coverage, with Logia 1-80 editorially consolidated and Logia 81-114 pending consolidation.
- Replaced older evidence-gap language with the current evidence-control state: evidence/control inventory complete and `NEEDS_EVIDENCE_BEFORE_FINAL` reduced to 0.
- Added print/digital publication architecture references to active navigation and product documents.
- Added Greek-layer freeze status: extant, partial/lacunose, and hypothetical retroversion labels are now publication-safe for the current 37-unit clean reader.
- Updated the recommended next step to print-safe full appendix editorial consolidation for Logia 81-90.
- Added the reusable structural QA baseline and documented that `python3 tools/qa_crosscheck.py` must be run before and after major editorial/generation passes.
- Documented the accepted heading-format differences across language layers and the exact clean-text appendix anchors for all current reader units.
- Preserved historical dates and completed-pass context where documents are primarily audit records, but added superseded next-step notes where old guidance could mislead current work.

## Verification

- Stale key phrases checked and cleared from active documentation:
  - `попередніх 31`
  - `каркас для всіх 114`
  - `11-114`
  - `104/114`
  - `10/114`
  - `67 сек`
  - `55 логій`
  - `59 ще`
  - old Phase 5 appendix-expansion next-step wording
- Appendix metrics verified:
  - 114 logion headings
  - 114 source/control sections
  - 31 remaining card-derived blocks
  - 20 remaining working-index skeleton phrases
- `python3 tools/qa_crosscheck.py` passed.

## Current Next Step

Proceed with print-safe full appendix editorial consolidation for Logia 81-90, using `project/print-and-digital-publication-architecture.md` as a controlling document and `tools/qa_crosscheck.py` as the structural guardrail.
