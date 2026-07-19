# Release-Candidate Audit v1.0-rc1

Status: release-candidate audit completed with external production blocker, 2026-07-19.

## Verdict

The project is **content-complete and proof-package complete**, but it is **not yet a fully signed-off release candidate** because final production PDFs have not been compiled in Typst/professional layout and final human copyedit has not been signed off.

Working readiness estimate after this pass: **99.75%**.

## What Is Complete

- 114/114 logion cards.
- 114/114 appendix sections.
- Frozen 36-unit clean reader.
- Ukrainian full paper proof: 118 pages.
- English full paper proof: 177 pages.
- Digital scholarly companion PDF proof: 16 pages.
- Browsable static HTML companion: 114 panels, 762 valid local file links.
- Typst-ready production handoff package.
- Release manifest generator.
- Current paper PDF repo-path leakage: 0 for Ukrainian and English full proofs.

## Current QA Snapshot

```bash
python3 tools/qa_crosscheck.py
```

Result:

- card files: 114/114;
- appendix sections: 114/114;
- appendix source/control sections: 114/114;
- reader sets: 36/36 synchronized;
- clean-text anchors: present for all clean-reader logia.

## Release Artifacts

Paper proofs:

- `output/uk-paper-book/euagelia-uk-full-proof.pdf`
- `output/en-paper-book/euagelia-en-full-proof.pdf`

Digital companion:

- `output/digital-scholarly-companion/euagelia-digital-companion-full-proof.pdf`
- `output/digital-scholarly-companion/html/index.html`
- `output/digital-scholarly-companion/logion-cross-reference-index.tsv`
- `output/digital-scholarly-companion/source-witness-inventory.tsv`
- `output/digital-scholarly-companion/audit-trail-index.tsv`

Production handoff:

- `output/production-typst/euagelia-template.typ`
- `output/production-typst/uk-pilot.typ`
- `output/production-typst/en-pilot.typ`
- `output/production-typst/production-handoff-checklist.md`
- `output/production-typst/production-pilot-manifest.tsv`

Release manifest:

- `output/release-candidate-manifest-v1.0-rc1.tsv`

## Remaining Blockers Before 100%

1. Compile the Typst pilot or formally accept professional handoff.
2. Expand the accepted production template to the full Ukrainian and English books.
3. Perform final human copyedit signoff for Ukrainian and English books.
4. Run final page-by-page visual QA on production PDFs.
5. Complete final public-source redistribution review.
6. Generate final frozen checksums after production PDFs and copyedit are frozen.
7. Tag or otherwise mark the release version.

## 100% Definition

The project reaches 100% when the final production PDFs and digital companion are frozen, checked, checksummed, documented, and ready to publish without known blockers.

The current state is one step earlier: a complete scholarly/proof package plus a Typst-ready production handoff.
