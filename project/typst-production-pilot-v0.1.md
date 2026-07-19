# Typst Production Pilot v0.1

Status: completed as Typst-ready handoff package, 2026-07-19.

## Scope

This pass executed `project/ide-codex-typst-production-pilot-v0.1-prompt.md`.

The final production gate chose Typst/professional handoff as the preferred final production path and kept ReportLab as proof-only. The current environment does not have Typst, XeLaTeX, or pdfLaTeX installed, so this pass created a deterministic Typst-ready handoff package rather than pretending to compile final PDFs.

## Toolchain Result

- `typst`: not installed.
- `xelatex`: not installed.
- `pdflatex`: not installed.

Decision: Typst remains the preferred final production target, but compilation is an external/local-environment step.

## Created Production Package

Directory:

- `output/production-typst/`

Files:

- `output/production-typst/README.md`
- `output/production-typst/euagelia-template.typ`
- `output/production-typst/uk-pilot-source.md`
- `output/production-typst/en-pilot-source.md`
- `output/production-typst/uk-pilot.typ`
- `output/production-typst/en-pilot.typ`
- `output/production-typst/production-handoff-checklist.md`
- `output/production-typst/production-pilot-manifest.tsv`

Generator:

- `tools/build_typst_production_pilot.py`

## Pilot Coverage

Both Ukrainian and English Typst pilot sources include:

- title/front matter;
- full clean reader;
- Logion 2 as included/marked sample;
- Logion 114 as excluded secondary-material sample;
- bibliography/source-key sample;
- production note preserving the paper/digital boundary.

## QA

Structural checks:

- Ukrainian pilot has clean reader: yes.
- Ukrainian pilot has Logion 2: yes.
- Ukrainian pilot has Logion 114: yes.
- English pilot has clean reader: yes.
- English pilot has Logion 2: yes.
- English pilot has Logion 114: yes.
- Repo-path scan in paper pilot sources: 0 hits.

Baseline/final project QA:

```bash
python3 tools/qa_crosscheck.py
```

Result:

- card files: 114/114;
- appendix sections: 114/114;
- appendix source/control sections: 114/114;
- reader sets: 37/37 synchronized;
- clean-text anchors: present for all clean-reader logia.

## Compile Instructions

After installing Typst:

```bash
typst compile output/production-typst/uk-pilot.typ output/production-typst/uk-pilot.pdf
typst compile output/production-typst/en-pilot.typ output/production-typst/en-pilot.pdf
```

Then render/inspect the PDFs page by page before promoting the template to full-book production.

## Remaining Blocker

The project now has a Typst-ready production pilot package, but it does not yet have compiled Typst PDFs in this environment. Release-candidate status still requires a compiled pilot or a formal professional typesetting handoff acceptance.

## Next Recommended Step

Install Typst locally or run the handoff package in a Typst-capable environment, compile `uk-pilot.typ` and `en-pilot.typ`, inspect the resulting PDFs, and then decide whether to expand the template to the full Ukrainian and English books.
