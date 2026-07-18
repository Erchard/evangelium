# Greek Layer Freeze Audit

Status: completed publication-control pass, 2026-07-18.

## Purpose

This audit closes the Greek-layer publication risk before the next appendix and dossier passes. The project now prints 37 clean-reader logia/cores. The Greek layer must therefore distinguish three things without ambiguity:

- materially preserved Greek Thomas papyrus text;
- lacunose or partial Greek Thomas papyrus text;
- hypothetical Greek retroversion from Coptic, controlled by canonical or internal parallels.

The third category is useful for comparison, but it is not manuscript evidence.

## Defect Found

The main Greek files were mostly using correct witness labels, but `greek-retroversion-confidence-audit-v0.1.md` was stale. It still described the earlier 34-unit reader and lacked the three later promoted reader cores:

- Logion 46A, John / least-in-kingdom core;
- Logion 91A, recognition-of-time core;
- Logion 103A, thief/watchfulness core.

Two language files also retained stale status prose saying they were synchronized with the 34-unit reader.

## Remediation Plan

1. Update the Greek retroversion confidence audit from v0.1 status to v0.2 publication-freeze status.
2. Add Logia 46, 91, and 103 to the Greek confidence table as `Greek retroversion, hypothetical`.
3. Update reader counts from 34 to 37 without changing clean-reader membership.
4. Clarify that the `Greek Status` column in the all-114 decision table records loaded Greek Thomas witness status, not the publication Greek layer where a retroversion may still be printed.
5. Update stale 34-unit status prose in the English and Coptic reader files.
6. Verify that the parallel edition uses publication-safe witness labels for all 37 rows.

## Implementation Completed

- `reconstruction/earliest-sayings-gospel/greek-retroversion-confidence-audit-v0.1.md` now has v0.2 status, 37-unit summary, and explicit rows for Logia 46, 91, and 103.
- `reconstruction/earliest-sayings-gospel/parallel-edition.md` now records the Greek-layer freeze status.
- `reconstruction/earliest-sayings-gospel/all-114-publication-decision-table-v0.1.md` now explains the scope of its `Greek Status` column.
- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-en.md` and `reconstruction/earliest-sayings-gospel/reconstructed-gospel-coptic.md` no longer describe themselves as synchronized with the old 34-unit reader.

## Frozen Publication Rule

For public-facing output:

1. Use `Extant Greek` only where a loaded Greek Thomas papyrus witness materially preserves the unit.
2. Use `Partial extant Greek` where only a subunit or phrase is materially preserved.
3. Use `Lacunose P.Oxy.` where a Greek papyrus witness exists but the text depends on substantial restoration.
4. Use `Greek retroversion, hypothetical` for all Greek forms reconstructed from Coptic and controls without an extant Greek Thomas witness.
5. Never cite a hypothetical retroversion as manuscript evidence.

## Result

Greek-layer status is now safe enough for the next print/digital editorial stage. Full appendix consolidation is now complete for Logia 1-114; the next high-value task is wealth/renunciation cluster-control before the evidence dossier publication pass.
