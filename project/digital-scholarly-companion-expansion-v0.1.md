# Digital Scholarly Companion Expansion v0.1

Status: completed 2026-07-19.

## Scope

This pass executed `project/ide-codex-digital-scholarly-companion-expansion-v0.1-prompt.md`.

The goal was to move the digital companion beyond a simple source-map proof into a real research-navigation layer. Paper books remain print-safe; the digital companion intentionally preserves repository paths, source paths, evidence notes, control files, audit trail, checksums, and reproducibility data.

## New Or Updated Artifacts

- `tools/generate_digital_companion.py`
- `output/digital-scholarly-companion/companion-source-full.md`
- `output/digital-scholarly-companion/companion-manifest.md`
- `output/digital-scholarly-companion/README.md`
- `output/digital-scholarly-companion/logion-cross-reference-index.tsv`
- `output/digital-scholarly-companion/source-witness-inventory.tsv`
- `output/digital-scholarly-companion/artifact-checksums.tsv`
- `output/digital-scholarly-companion/audit-trail-index.tsv`
- `output/digital-scholarly-companion/euagelia-digital-companion-full-proof.pdf`
- `output/digital-scholarly-companion/euagelia-digital-companion-full-proof.source.md`

## Coverage

The generated companion now includes:

- landing/overview and how-to-use section;
- clean-reader manifest for Ukrainian, English, Coptic, Greek, Arabic literary, and parallel layers;
- all-114 logion research index;
- per-logion links to cards, evidence notes, and direct control files where present;
- source witness inventory for Coptic/NHC II, Greek P.Oxy. 1, P.Oxy. 654, P.Oxy. 655, P.Oxy. 5575 control material, translations, and source-verification notes;
- bibliography, rights, source reproducibility, and commons policy references;
- audit trail index for major project pass/audit/review files;
- reproducibility checklist and QA commands.

Machine-readable coverage:

| File | Rows |
| --- | ---: |
| `logion-cross-reference-index.tsv` | 115 including header; 114 logia |
| `source-witness-inventory.tsv` | 137 including header; 136 source files |
| `artifact-checksums.tsv` | 24 including header |
| `audit-trail-index.tsv` | 64 including header; 63 audit/pass/review files |

## Proof QA

The companion was rendered as:

- `output/digital-scholarly-companion/euagelia-digital-companion-full-proof.pdf`

PDF check:

- pages: 16;
- contains Logion 114;
- contains Source Witness Inventory;
- rendered to PNG pages and inspected through a contact sheet;
- no visible clipping or missing ending was observed.

The all-114 index is dense in PDF form, especially pages 5-10. This is acceptable for a technical proof but not ideal as the final user experience.

## Boundary Between Paper And Digital

This pass preserves the intended publication architecture:

- paper books remain clean, self-contained, and print-safe;
- digital companion contains the larger apparatus that would be clumsy or impossible on paper;
- internal repository paths are allowed only in the digital companion;
- source rights distinctions remain explicit.

## Remaining Issue

The companion is now structurally complete as a Markdown/TSV/PDF research package, but not yet excellent as a reader-facing digital product. The next quality step is a browsable HTML/static-site companion with filters, anchors, per-logion pages or sections, and easy navigation between cards, evidence notes, controls, source witnesses, and paper-book references.

## Next Recommended Step

Build a browsable digital companion interface from the generated TSV/Markdown artifacts. It should not replace the paper books; it should be the research workbench behind them.
