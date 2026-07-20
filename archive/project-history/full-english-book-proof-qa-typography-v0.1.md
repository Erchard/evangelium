# Full English Book Proof QA And Typography v0.1

Status: completed 2026-07-19.

## Scope

This pass executed `project/ide-codex-full-english-book-proof-qa-typography-v0.1-prompt.md`.

Primary artifact checked:

- `output/en-paper-book/euagelia-en-full-proof.pdf`

Related generated/QA artifacts:

- `output/en-paper-book/book-source-en-full.md`
- `reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-en.md`
- `project/english-full-book-proof-page-scan-v0.1.tsv`
- `project/english-full-book-proof-image-scan-v0.1.tsv`

## Rebuild And Structural QA

The English full appendix, full paper source, PDF proof, and structural QA were regenerated before inspection.

Final structural QA result:

- card files: 114/114
- appendix sections: 114/114
- source/control appendix sections: 114/114
- clean-reader synchronization: 37/37
- exact clean-text appendix anchors: present

## PDF Text QA

PDF metadata/check:

- pages: 177
- page size: A4
- title: `EUAGELIA English Full Book Proof`

No paper-facing leakage was found for:

- internal repository paths: `corpus/`, `reconstruction/`, `project/`, `sources/`, `controls/`, `notes/`, `output/`
- obsolete draft markers: `draft`, `Status:`, `Explain `
- Ukrainian status leakage in the English proof: `включено`, `виключено`, `відкладено`, `непевно`, `залишено`
- obsolete blocker phrase: `full English 114-logion commentary appendix has not yet been generated`

Expected low-text pages:

| Page | Reason |
| ---: | --- |
| 1 | Title page |
| 4 | Section opener: full 114-logion commentary appendix |
| 120 | Section opener: evidence dossier |
| 134 | Section opener: included logia and core summaries |

## Visual Page QA

The full PDF was rendered to PNG pages and inspected through compact contact sheets covering all 177 pages.

Visual result:

- page 1 title page present;
- page 2 clean reconstructed text present and readable as the first substantive reader layer;
- page 3 reader orientation present;
- pages 4-119 contain the full 114-logion commentary appendix, with Logion 1 beginning on page 6 and Logion 114 present on page 119;
- pages 120-133 contain the evidence dossier;
- pages 134-176 contain included-logia/core summaries and Logion 114 exclusion summary;
- page 177 contains bibliography and rights material;
- no visible clipping, overlap, missing footer, missing page number, accidental blank page, or duplicated-page block was observed;
- denser pages, especially around page 77, remain inside safe margins;
- the evidence dossier and summary pages are visually lighter than the appendix, but this reflects short methodological/summary blocks rather than layout failure.

Automated image diagnostics found:

- low-ink page: 134 only, expected section opener;
- edge/cropping flags: 0.

## Verdict

The English full proof passes current proof-level QA. It is now structurally comparable to the Ukrainian full proof: clean text first, full appendix present, evidence/dossier material present, no paper-only path leakage, and no visible page-level rendering blocker.

This does not yet make the PDF a final production edition. Remaining production decisions are:

- whether to keep ReportLab proof rendering or move final books into a stronger book-typesetting system;
- final human copyedit of English and Ukrainian prose;
- final paper design choices for section openers, running headers, line spacing, and bibliography/index styling.

## Next Recommended Step

The paper-book layer is now substantially proofed in both Ukrainian and English. The next strongest unresolved layer is the digital scholarly companion: it should preserve the full evidence apparatus that cannot fit comfortably into paper books, including source paths, machine-checkable manifests, audit trail, evidence notes, control files, and links between every logion card and its publication-facing representation.
