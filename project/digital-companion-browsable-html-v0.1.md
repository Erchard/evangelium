# Browsable Digital Companion HTML v0.1

Status: completed 2026-07-19.

## Scope

This pass executed `project/ide-codex-digital-companion-browsable-html-v0.1-prompt.md`.

The goal was to turn the expanded Markdown/TSV/PDF digital companion into a usable static HTML research workbench.

## New Artifact

- `tools/render_digital_companion_html.py`
- `output/digital-scholarly-companion/html/index.html`

## What The HTML Companion Contains

- overview and section navigation;
- summary counts for logia, clean-reader units, source files, and audit/pass files;
- searchable/filterable all-114 logion index;
- per-logion expandable detail panels;
- direct links to cards, evidence notes, control files, Ukrainian appendix, English appendix, witness groups, source inventory, rights policy, and audit trail;
- source witness sections grouped by Coptic/NHC II, P.Oxy. 1, P.Oxy. 654, P.Oxy. 655, P.Oxy. 5575 control material, translation controls, and general source corpus;
- audit trail table;
- bibliography/rights/commons links;
- reproducibility checklist and core artifact checksums.

## QA Results

Baseline and final structural QA:

```bash
python3 tools/qa_crosscheck.py
```

Result:

- card files: 114/114;
- appendix sections: 114/114;
- appendix source/control sections: 114/114;
- reader sets: 37/37 synchronized;
- clean-text anchors: present for all clean-reader logia.

HTML structural checks:

- logion detail panels: 114;
- search input present;
- reader filter present;
- decision-family filter present;
- Greek-status filter present;
- source witness section present;
- reproducibility section present.

Local link check:

- total hrefs: 1006;
- internal anchor links: 244;
- local project file links: 762;
- missing local file links: 0.

Static server check:

- `http://127.0.0.1:8765/output/digital-scholarly-companion/html/index.html` returned HTTP 200 during temporary local QA.

## Design Decision

The HTML companion is intentionally quiet and utilitarian. It is a research workbench, not a landing page. Paper books remain the clean reading layer; this HTML companion is the apparatus layer for verification and deeper study.

## Remaining Issue

The HTML is now usable as a static proof, but it has not been final-polished as a public website. Future improvement could add per-logion standalone pages, source-row backlinks, keyboard navigation, print-friendly exports of selected logion dossiers, and better visual hierarchy after real reader testing.

## Next Recommended Step

Move to production-grade finalization: decide the final book typesetting path, then run a final copyedit/proof gate for Ukrainian book, English book, and digital companion together.
