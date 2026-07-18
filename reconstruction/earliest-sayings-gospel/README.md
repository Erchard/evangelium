# Earliest Sayings Gospel Reconstruction

Status: working reconstruction v0.8, updated 2026-07-18.

This folder contains the projected public-facing reconstruction of the earliest recoverable layer of the sayings gospel tradition preserved in the Gospel of Thomas.

The projected publication architecture now separates print and digital outputs: a Ukrainian paper book, an English paper book, and a fuller digital scholarly companion. Paper-facing prose must use print-safe references rather than depending on clickable repository links.

The reconstruction is not a simple translation of the Coptic Gospel of Thomas. It distinguishes:

- reconstructed early layer;
- extant Coptic witness;
- extant Greek witness;
- possible expansions or secondary redaction;
- uncertain material retained in the apparatus.

## Files

| File | Purpose |
| --- | --- |
| `reconstructed-gospel-uk.md` | Main Ukrainian reader-facing reconstruction: only numbered logia, without disclaimers, markers, brackets, or commentary. |
| `reconstructed-gospel-uk-apparatus.md` | Ukrainian apparatus explaining confidence, partial inclusion, exclusions, and reconstruction markers outside the clean text. |
| `reconstructed-gospel-coptic.md` | Coptic base witness for included units. |
| `reconstructed-gospel-greek.md` | Extant Greek witnesses where available plus explicitly labeled hypothetical retroversions where no loaded Greek Thomas witness exists. |
| `reconstructed-gospel-en.md` | English reader-facing reconstruction. |
| `reconstructed-gospel-ar-quranic-register.md` | Arabic literary reader layer in a high classical / Qur'anic-adjacent register; explicitly not Qur'an, not a sura, and not a claim of revelation. |
| `parallel-edition.md` | Parallel research edition, publication-polished for Greek witness-status labels. |
| `inclusion-decisions-table.md` | Inclusion / exclusion decisions. |
| `evidence-dossier-en.md` | English evidence dossier, now a publication-facing draft v1.4 with provisional bibliography/rights note. |
| `full-logion-commentary-appendix-uk.md` | Ukrainian full 114-logion commentary appendix: all 114 logia have reader-facing explanation and all Logia 1-114 are editorially consolidated into print-safe chapters. |
| `notes/` | Detailed logion-level evidence notes. |
| `greek-retroversion-confidence-audit-v0.1.md` | Audit distinguishing extant Greek witnesses, lacunose/partial Greek witnesses, mixed cases, and hypothetical Greek retroversions; updated to publication-polish v0.3. |
| `final-clean-reader-freeze-v0.1.md` | Freeze report confirming the 37-unit clean reader before book generation. |
| `final-all-114-decision-audit-v0.1.md` | Pre-freeze audit of all-114 reader support, split-core candidates, stale files, and next work package; superseded for corpus freeze by `final-clean-reader-freeze-v0.1.md`. |
| `all-114-publication-decision-table-v0.1.md` | Publication-control table for all 114 logia: reader, appendix-only, deferred, evidence-blocked, and excluded decisions. |
| `living-dead-world-cluster-control-pass-v0.1.md` | Audit of the first cluster-control pass for Logia 11, 18, 52, 56, 59, 60, 80, and 111. |
| `beatitudes-cluster-control-pass-v0.1.md` | Audit of the second cluster-control pass for Logia 54, 58, 68, and 69. |
| `seek-find-cluster-control-pass-v0.1.md` | Audit of the third cluster-control pass for Logia 2, 92, and 94. |
| `family-renunciation-cluster-control-pass-v0.1.md` | Audit of the fourth cluster-control pass for Logia 16, 55, 99, and 101. |
| `fire-kingdom-cluster-control-pass-v0.1.md` | Audit of the fifth cluster-control pass for Logia 10 and 82. |
| `wealth-renunciation-cluster-control-pass-v0.1.md` | Audit of the wealth/renunciation cluster-control pass for Logia 63, 64, 72, 76, 81, 90, 95, 100, 109, and 110. |
| `logion-114-publication-exclusion-rationale-v0.1.md` | Publication-facing rationale for excluding Logion 114 from the clean reader while preserving it in the appendix. |
| `evidence-dossier-publication-pass-v0.1.md` | Audit of the pass that turned the English dossier into publication-facing draft v1.4. |
| `ritual-ethics-bridegroom-104a-followup-v0.1.md` | Follow-up decision for 104A: appendix-only stable, no clean-reader promotion. |
| `logion-001-frame-status-review-v0.1.md` | Pre-freeze editorial decision: Logion 1 is a collection frame/prologue case, not an ordinary included saying. |
| `split-core-high-early-pressure-review-c-v0.1.md` | Pre-freeze review for high-early non-reader pressure: Logia 46, 90, 91, 103, and 104. |
| `split-core-decision-review-a-v0.1.md` | Split-core review for Logia 45, 47, 63, 64, and 65-66. |

## Current Scope

The current clean reconstructed reader covers 37 logia or marked cores.

- Logia 1, 2, 3, 4, 5, 6, 9, 10, 16, 20, 22, 25, 26, 31, 32, 33, 34, 35, 36, 39, 41, 45A, 46A, 47B, 54, 63, 72, 73, 86, 89, 91A, 95, 96, 99, 100, 103A, and 107 are currently printed in the clean Ukrainian reader.
- Logion 2 remains the methodological gold-standard card.
- All 114 logion cards now contain `Gold-level status check v0.2`; see `../../corpus/cards/card-quality-audit-v0.2.md`.
- All 114 logion cards now contain `Five-source original-language apparatus v0.1`; see `../../corpus/cards/five-source-apparatus-audit-v0.1.md`.
- Canonical Greek controls from the local SBLGNT cache have been inserted into 81 logion cards; see `../../corpus/cards/canonical-greek-extraction-audit-v0.1.md`.
- The Ukrainian reader text is now a clean numbered text; technical cautions, markers, and explanations belong in `reconstructed-gospel-uk-apparatus.md` and `reader-commentary-uk.md`.
- English, Coptic, Greek, Arabic literary, and parallel layers are synchronized for the frozen 37-unit reader.
- All 37 clean-reader units now have exact `Чистий текст реконструкції` anchors inside `full-logion-commentary-appendix-uk.md`.
- The Greek layer is controlled by `greek-retroversion-confidence-audit-v0.1.md`; the 2026-07-18 publication-polish pass normalized witness labels, and hypothetical retroversions must not be treated as manuscript witnesses.
- `full-logion-commentary-appendix-uk.md` covers all 114 logia with reader-facing explanation. Logia 1-114 are now consolidated entries.
- Print/digital publication architecture v0.1 is now active: future appendix and commentary work should use print-safe references for paper books and keep repository paths in a separable digital apparatus layer.
- Editorial consolidation has reached Logia 1-114: the appendix no longer carries duplicated card-derived blocks or working-index prose.
- The first Phase 5 P1 non-reader appendix package has expanded sections for Logia 23, 24, 28, 29, 30, 37, 38, 75, 77, 104, and 106.
- The first matching evidence-rationale pass created direct English evidence notes for those 11 logia; Packages A and B then reduced `NEEDS_EVIDENCE_BEFORE_FINAL` to 0 rows.
- The first cluster-control pass now exists for the living/dead/world group: Logia 11, 18, 52, 56, 59, 60, 80, and 111. It did not expand the clean reader; it gave Logion 80 cluster support without treating that support as a direct evidence note.
- The second cluster-control pass now exists for the beatitudes group: Logia 54, 58, 68, and 69. It keeps Logion 54 in the clean reader with marker and keeps Logia 58, 68, and 69 appendix-only.
- The third cluster-control pass now exists for the seek/find group: Logia 2, 92, and 94. It keeps Logion 2 as the clean reader's main seek/find unit and keeps Logia 92 and 94 appendix-only.
- The fourth cluster-control pass now exists for the family-renunciation group: Logia 16, 55, 99, and 101. It keeps Logia 16 and 99 as marked clean-reader cores and keeps Logia 55 and 101 appendix-only.
- The fifth cluster-control pass now exists for the fire/kingdom group: Logia 10 and 82. It keeps Logion 10 as the marked fire-casting core and keeps Logion 82 appendix-only.
- The wealth/renunciation cluster-control pass now exists for Logia 63, 64, 72, 76, 81, 90, 95, 100, 109, and 110. It keeps the current wealth-related reader representatives and does not expand the clean reader.
- Logion 114 now has a publication-level exclusion rationale. It remains excluded from the clean reader and fully present in the appendix/dossier.
- Logion 1 now has a dedicated frame-status review. It remains in the synchronized source-layer reader for now, but the final edition must treat it as an opening collection frame/prologue rather than an ordinary early-saying datum.
- Controlled reader-candidate pass 46A/91A now exists. It includes 46A and 91A as marked clean-reader cores and keeps 90 appendix-only.
- Thief/watchfulness cluster-control for Logia 21 and 103 now exists. It includes 103A as a marked clean-reader core, keeps full Logion 103 appendix-only, and keeps full Logion 21 appendix-only as composite control material.
- `evidence-dossier-en.md` is now publication-facing draft v1.4. It still requires the bibliography / rights / citation / reproducibility pass before final publication.
- Ritual-ethics / bridegroom follow-up for 104A now exists. It keeps 104A appendix-only stable and does not change the 37-unit clean reader.
- Final clean-reader freeze v0.1 now exists. It freezes the 37-unit clean reader for this edition and cleaned the English reader layer of residual apparatus notes.

This is a working reconstruction, not a final academic edition.

## Full Commentary Principle

The clean reconstruction is selective. Not all 114 logia of the Gospel of Thomas belong in the reconstructed earliest sayings gospel.

However, the reader-facing appendix and commentary must eventually cover all 114 logia. Excluded, deferred, and uncertain logia still need context, interpretation, source notes, parallels, and a clear explanation of why they were not included in the clean reconstruction.

The final reader experience should therefore have two layers:

1. clean reconstructed text: only the most responsible early reconstruction;
2. full commentary appendix: all 114 logia, including rejected or deferred material.

For publication, these layers generate three outputs: a Ukrainian paper book, an English paper book, and a digital scholarly companion. The paper books must be self-contained; the digital companion preserves the full source/evidence apparatus.

Split-Core Decision Reviews A/B/C, the controlled clean-reader candidate passes, the all-114 publication decision table, the first P1 non-reader appendix expansion, the matching evidence-rationale pass, Package B evidence-rationale pass, living/dead/world cluster-control, beatitudes cluster-control, seek/find cluster-control, family-renunciation cluster-control, fire/kingdom cluster-control, thief/watchfulness cluster-control, wealth/renunciation cluster-control, ritual-ethics / bridegroom 104A follow-up, Logion 114 publication-level exclusion rationale, evidence dossier publication pass, Greek retroversion publication polish, final clean-reader freeze, generator-ready book source packages, Logion 1 frame-status review, card-level reader interpretation expansion, full-appendix reader interpretation sync, editorial consolidation packages for Logia 1-114, and the reusable QA crosscheck now exist. Before and after major edits, run `python3 ../../tools/qa_crosscheck.py` from this folder or `python3 tools/qa_crosscheck.py` from the repository root. The next high-priority task is final bibliography and rights verify.
