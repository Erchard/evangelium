# EUAGELIA Typst Production Pilot

Status: Typst-ready handoff; Typst not installed in this environment, 2026-07-19.

## Contents

- `euagelia-template.typ` - conservative book template pilot.
- `uk-pilot.typ` - Ukrainian pilot source.
- `en-pilot.typ` - English pilot source.
- `uk-pilot-source.md` - Markdown source excerpt used for the Ukrainian pilot.
- `en-pilot-source.md` - Markdown source excerpt used for the English pilot.
- `production-handoff-checklist.md` - checklist for Typst or professional typesetting.
- `production-pilot-manifest.tsv` - file sizes and checksums.

## Compile Commands

Install Typst, then run:

```bash
typst compile output/production-typst/uk-pilot.typ output/production-typst/uk-pilot.pdf
typst compile output/production-typst/en-pilot.typ output/production-typst/en-pilot.pdf
```

## Production Rule

ReportLab PDFs in `output/uk-paper-book/`, `output/en-paper-book/`, and `output/digital-scholarly-companion/` remain proof artifacts. Final release-candidate PDFs should come from this Typst/professional production path or from an explicitly approved equivalent.
