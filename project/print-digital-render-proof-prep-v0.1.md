# Print / Digital Render Proof Preparation v0.1

Date: 2026-07-18

## Purpose

This pass prepares EUAGELIA for actual book rendering:

- one Ukrainian paper book;
- one English paper book;
- one digital scholarly companion preserving full source paths, links, audit trail, and apparatus.

The clean-reader corpus is not changed in this pass. The frozen reader remains the 37-unit edition:

`1, 2, 3, 4, 5, 6, 9, 10, 16, 20, 22, 25, 26, 31, 32, 33, 34, 35, 36, 39, 41, 45A, 46A, 47B, 54, 63, 72, 73, 86, 89, 91A, 95, 96, 99, 100, 103A, 107`.

## Current Action Plan

1. Confirm structural QA before touching rendering sources.
2. Confirm Ukrainian and English paper-book sources are print-safe.
3. Create a print-safe citation key table that both paper books can use.
4. Keep digital-only paths and URLs inside the digital companion, not in paper-book prose.
5. Define renderer interface without inventing a large toolchain before the repository has one.
6. Update the open-task queue so the next step is actual render pipeline / proof generation.

## Preflight Results

Commands run:

```bash
python3 tools/qa_crosscheck.py
git diff --check
rg -n "corpus/|reconstruction/|project/|sources/|controls/|notes/|https?://" output/uk-paper-book output/en-paper-book
```

Results:

- structural QA passed;
- 114/114 card files are present;
- 114/114 appendix sections are present;
- 114/114 appendix source/control sections are present;
- 37/37 reader units are synchronized across language layers and control tables;
- all clean-reader logia have appendix clean-text anchors;
- whitespace diff check passed;
- paper-source grep returned no matches, which means the Ukrainian and English paper-book source files do not expose internal repository paths or clickable web URLs.

## Print-Safe Citation Key Table

These keys are safe for Ukrainian and English paper books because they resolve to the working bibliography and do not require repository paths.

| Print key | Ukrainian paper label | English paper label | Release status | Use in paper |
| --- | --- | --- | --- | --- |
| `NHC II,2` | `NHC II,2` | `NHC II,2` | Primary witness; critical-edition reading check pending | Coptic base witness label for Thomas material. |
| `P.Oxy. 1` | `P.Oxy. 1` | `P.Oxy. 1` | DCLP open transcription verified; printed-edition check pending | Extant Greek witness for relevant logia. |
| `P.Oxy. 654` | `P.Oxy. 654` | `P.Oxy. 654` | DCLP open transcription verified; printed-edition check pending | Extant/lacunose Greek witness for Logia 1-7. |
| `P.Oxy. 655` | `P.Oxy. 655` | `P.Oxy. 655` | DCLP open transcription verified; printed-edition check pending | Extant/lacunose Greek witness for Logia 24(?), 36-39. |
| `P.Oxy. 5575` | `P.Oxy. 5575` | `P.Oxy. 5575` | Protected control only | Control for early sayings circulation, not direct Thomas witness. |
| `DCLP` | `DCLP / Papyri.info` | `DCLP / Papyri.info` | Open with attribution verified | Bibliographic/source-provenance note, not clean-text apparatus. |
| `SBLGNT` | `SBLGNT` | `SBLGNT` | CC BY 4.0 open control verified | Canonical Greek comparison layer for Matthew, Mark, Luke, Paul, James where needed. |
| `Mattison Thomas` | `Mattison / Gospels.net` | `Mattison / Gospels.net` | Public-domain control verified | Open English translation control only. |
| `Lambdin` | `Lambdin` | `Lambdin` | Protected control only; library check for page-specific references | Modern translation control, not base text. |
| `Layton` | `Layton` | `Layton` | Protected control only; library check for page-specific references | Coptic/Greek academic control, not reproduced base text. |
| `DeConick` | `DeConick` | `DeConick` | Protected control only; library check for page-specific references | Reconstruction and stratification model. |
| `Patterson / Meyer` | `Patterson / Meyer` | `Patterson / Meyer` | Protected control only; library check for page-specific references | Scholarly translation/commentary control. |
| `Brill CGL` | `Brill CGL` | `Brill CGL` | Protected control only | Critical-edition checking, not reproduced source text. |
| `NA / UBS` | `NA / UBS` | `NA / UBS` | Protected control only; not selected as open base | Optional scholarly checking only; SBLGNT is the current open base. |

Keys not used in the current release:

| Print key | Status | Rule |
| --- | --- | --- |
| `Q` | `NOT_USED_IN_CURRENT_RELEASE` | Do not cite generic Q unless a later pass selects a specific edition/model. |
| `Didache` | `NOT_USED_IN_CURRENT_RELEASE` | Do not cite until a specific public-domain or licensed edition is selected. |

## Paper / Digital Layer Separation

### Paper Books

Paper books may include:

- clean reconstructed text;
- logion numbers;
- appendix references by logion number;
- witness labels such as `NHC II,2`, `P.Oxy. 1`, `P.Oxy. 654`, `P.Oxy. 655`;
- canonical references in normal print form;
- short bibliography keys;
- short rights and commons notice;
- print indexes.

Paper books must not depend on:

- repository file paths;
- clickable URLs as the only evidence path;
- protected modern editions as reproduced base text;
- long digital audit histories.

### Digital Scholarly Companion

The digital companion should preserve:

- corpus cards;
- source snapshots;
- evidence notes;
- Greek retroversion confidence audit;
- full decision tables;
- source paths;
- external URLs;
- rights register;
- prompt/audit trail;
- generated cross-reference index.

## Renderer Interface

No existing render toolchain or Makefile was found in the repository. Therefore this pass does not create a large rendering system.

The next renderer should accept:

```text
input: output/uk-paper-book/book-source-uk.md
output: output/uk-paper-book/euagelia-uk-proof.pdf
format: print PDF, Ukrainian typography, page numbers, table handling
```

```text
input: output/en-paper-book/book-source-en.md
output: output/en-paper-book/euagelia-en-proof.pdf
format: print PDF, English typography, page numbers, table handling
```

```text
input: output/digital-scholarly-companion/companion-manifest.md
output: output/digital-scholarly-companion/euagelia-digital-companion-manifest.html or PDF
format: digital companion index with repository paths and links preserved
```

Minimum renderer requirements:

- preserve heading hierarchy;
- handle wide all-114 tables;
- keep logion numbers visible in running text and table sections;
- generate table of contents;
- support Ukrainian text and Greek/Coptic characters;
- generate page numbers;
- keep paper sources free of internal paths;
- produce a render log and checksum for each generated artifact.

## Remaining Blockers Before Final PDF Generation

1. Choose the actual rendering toolchain: Pandoc/LaTeX, Typst, Quarto, or another controlled renderer.
2. Convert working bibliography into one final print style.
3. Decide how to format the large 114-logion tables in paper: full-width landscape appendix, compact tables, or split tables.
4. Add title/copyright/commons pages for Ukrainian and English books.
5. Add print indexes: logion index, witness index, canonical parallels index, key themes index.
6. Run visual proof QA after PDF generation.
7. Add final rendered-file manifest and checksums to the digital companion.

## Recommended Rendering Order

1. Ukrainian paper book proof.
2. English paper book proof.
3. Digital scholarly companion manifest/index.
4. Visual QA pass over generated artifacts.
5. Final correction pass from proof findings.

## Completion Decision

Render proof preparation is complete at planning/preflight level.

The next task should generate the first proof artifacts or choose and install the rendering pipeline if no local renderer is available.
