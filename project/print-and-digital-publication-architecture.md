# Print and Digital Publication Architecture

Status: working publication architecture v0.1, created 2026-07-18.

## Purpose

The project must support two different public uses without splitting into disconnected projects:

1. readable paper books for Ukrainian and English readers;
2. a fuller digital scholarly companion for verification, source control, and future research.

Paper readers cannot click repository links. Digital readers and researchers, however, need the full apparatus: cards, source files, evidence notes, Greek confidence labels, cluster-control notes, and decision tables. The solution is not to remove the digital apparatus, but to separate print-facing references from digital file references.

## Final Output Families

### 1. Ukrainian Paper Book

Working output folder:

- `output/print/uk/`

Purpose:

- the main reader-facing Ukrainian book;
- self-contained on paper;
- suitable for reading without access to the repository.

Main content:

1. title page;
2. clean reconstructed Ukrainian text;
3. short reader introduction;
4. commentary on included logia and included subunits;
5. full appendix to all 114 logia;
6. short methodology;
7. bibliography;
8. indexes: logia, witnesses, canonical parallels, key themes.

### 2. English Paper Book

Working output folder:

- `output/print/en/`

Purpose:

- the main international reader-facing English book;
- self-contained on paper;
- somewhat more explicit methodologically than the Ukrainian reader book, but still not a full repository dump.

Main content:

1. title page;
2. clean reconstructed English text;
3. short introduction;
4. commentary on included logia and included subunits;
5. full appendix to all 114 logia;
6. methodological summary;
7. bibliography;
8. indexes: logia, witnesses, canonical parallels, key themes.

### 3. Digital Scholarly Companion

Working output folder:

- `output/digital/scholarly/`

Purpose:

- full evidence apparatus;
- reproducibility layer;
- source-controlled research archive;
- place for hyperlinks, repository paths, machine-readable tables, and detailed notes.

Main content:

1. complete 114 logion card set;
2. five-source apparatus;
3. Coptic, Greek, English, Ukrainian, Arabic, and parallel layers;
4. evidence dossier;
5. logion-level evidence notes;
6. cluster-control notes;
7. Greek retroversion confidence audit;
8. all-114 decision tables;
9. bibliography, rights notes, and source provenance;
10. generated cross-reference index linking print references to repository files.

## Core Rule

There must be one controlled scholarly corpus and multiple generated outputs.

The source corpus may contain technical metadata, file paths, links, and audit history. The paper books must not expose that raw infrastructure as their primary reader apparatus.

## Canonical Sources of Truth

The current canonical source files are:

- `corpus/cards/logion-XXX.md` for logion-level research data;
- `corpus/tables/logia-index.md` and `corpus/tables/logia-workflow-matrix.md` for corpus-wide status;
- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-uk.md` for the clean Ukrainian reader;
- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-en.md` for the clean English reader;
- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-coptic.md` for the Coptic reader layer;
- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-greek.md` for extant Greek and marked retroversion layer;
- `reconstruction/earliest-sayings-gospel/parallel-edition.md` for research alignment;
- `reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-uk.md` for the current Ukrainian 114-logion appendix;
- `reconstruction/earliest-sayings-gospel/evidence-dossier-en.md` for the English evidence argument;
- `reconstruction/earliest-sayings-gospel/notes/` for detailed logion and cluster evidence.

Future English appendix work should either be generated from a bilingual structured source or maintained as a separate English print-facing appendix that follows the same print-safe rules.

## Print-Safe Reference Rules

Paper references must be readable without clicking.

Use:

- logion numbers: `Logion 20`, `Логія 20`;
- witness labels: `NHC II,2`, `P.Oxy. 1`, `P.Oxy. 654`, `P.Oxy. 655`;
- canonical references: `Mark 4:30-32`, `Matt 13:31-32`, `Luke 13:18-19`;
- short bibliography keys: `Patterson 1993`, `DeConick 2006`, `NHC II Facsimile`;
- appendix references: `see Appendix, Logion 20`;
- table references: `see Witness Index`, `see Parallel Index`;
- clear confidence language: `extant Greek`, `fragmentary Greek`, `Greek retroversion, hypothetical`.

Do not use repository paths as the only print reference.

Bad print form:

> See `corpus/cards/logion-020.md`.

Good print form:

> See Appendix, Logion 20; compare Mark 4:30-32, Matt 13:31-32, and Luke 13:18-19; Greek is reconstructed from the Coptic and canonical controls.

Digital-only or digital-companion form:

> See `corpus/cards/logion-020.md` and `reconstruction/earliest-sayings-gospel/notes/logion-020-evidence-en.md`.

## Hyperlink Policy

Every important digital hyperlink must have a print-safe equivalent.

Digital output may use:

- clickable file links;
- repository paths;
- external URLs;
- anchors;
- generated cross-reference tables.

Print output must use:

- human-readable labels;
- stable logion numbers;
- witness abbreviations;
- printed bibliography;
- printed indexes.

External URLs may appear in print only in bibliography or source-provenance sections, and only when they are useful as stable public references. They must not be required for understanding the argument.

## QA Baseline

Before and after major editorial or generation passes, run:

```bash
python3 tools/qa_crosscheck.py
```

The current source headings intentionally vary by layer:

- Ukrainian clean reader: `## N`
- English / Greek / Coptic readers: `## Logion N`
- Arabic literary register: `## قول N`
- Ukrainian apparatus: `## Логія N`

This is an accepted source-format difference. Final print may display clean numbers only, while tooling must parse each layer explicitly and verify that all reader layers keep the same 34-unit set.

## Commentary and Appendix Writing Rules

Future appendix/editorial passes must write prose that can be reused in paper books.

Each logion appendix section should contain:

1. status in the reconstruction in plain language;
2. what the saying appears to say;
3. why it is included, partly included, uncertain, deferred, or excluded;
4. possible interpretations;
5. uncertainty and limits;
6. source witnesses in print-safe labels;
7. digital apparatus references in a clearly separable internal section.

When a section includes source files, it should distinguish:

- print-facing source reference: `Evidence note for Logion 20`;
- digital path: `reconstruction/earliest-sayings-gospel/notes/logion-020-evidence-en.md`.

The paper book can keep the print-facing reference and omit or move the digital path into the digital companion.

## Separation of Layers

### Clean Text Layer

The clean reconstructed text must remain free of:

- commentary;
- confidence statuses;
- square-bracket uncertainty markers;
- repository paths;
- source notes;
- footnote overload.

This applies to both Ukrainian and English clean readers.

### Print Commentary Layer

The print commentary may contain:

- short source labels;
- canonical parallels;
- brief methodological explanations;
- cross-references to appendix sections;
- bibliography keys;
- concise uncertainty language.

It should not contain:

- raw TODO language;
- working prompt names;
- internal repo-only paths as primary references;
- long evidence-note dumps.

### Digital Scholarly Layer

The digital scholarly companion should preserve:

- all repository paths;
- all detailed notes;
- all source-level apparatus;
- audit documents;
- prompts only when useful for reproducibility;
- machine-readable indexes;
- long-form evidence dossiers.

## Treatment of Rejected and Deferred Logia

Rejected, uncertain, and deferred logia must appear in the full appendix of both paper books.

The print reader should be able to see:

- what the logion says;
- why it was not included in the clean reconstruction;
- what early material may still be present;
- what evidence would be needed to change the decision;
- where to find the fuller digital evidence trail.

This prevents the clean reconstruction from looking arbitrary or cherry-picked.

## Ukrainian and English Book Relationship

The Ukrainian and English books should be separate books, not one bilingual volume.

Reason:

- paper readability is better;
- layout is simpler;
- each audience gets a coherent reading experience;
- the scholarly apparatus can be sized differently for each language.

The Ukrainian book should prioritize clear Ukrainian prose and reader understanding.

The English book should preserve the same reconstruction but may carry a slightly more explicit methodological tone because it is also the international-facing version.

## Digital Companion Relationship to Paper Books

Each paper book should mention the existence of the digital scholarly companion, but should not depend on it.

Recommended print wording:

> A fuller digital scholarly companion contains the logion cards, source apparatus, Greek retroversion controls, cluster notes, and detailed evidence files. The printed book gives stable logion, witness, and bibliography references so the argument remains readable without hyperlinks.

The digital companion should include a generated index mapping:

- print logion number;
- print section title;
- card path;
- evidence note path;
- cluster note path;
- source files;
- canonical controls.

## Generation Pipeline

Future automation should generate outputs in this order:

1. Validate canonical corpus:
   - 114 card files exist;
   - current reader logia match decision tables;
   - Greek status labels are valid;
   - print-safe source labels exist.
2. Generate clean Ukrainian and English book text:
   - no technical statuses;
   - no raw repository paths;
   - only numbered logia.
3. Generate print commentary and appendix:
   - include all 114 logia;
   - convert digital file references into print-safe references;
   - keep internal file paths out of the main printed prose.
4. Generate bibliography and indexes:
   - logion index;
   - witness index;
   - canonical parallel index;
   - theme index;
   - bibliography.
5. Generate digital scholarly companion:
   - preserve links and repository paths;
   - include complete evidence apparatus;
   - include source provenance and audit trail.
6. Run print-readiness checks:
   - no unresolved TODOs;
   - no raw repo paths in print files except optional technical appendix;
   - every hyperlink has a printed equivalent;
   - every logion reference resolves;
   - bibliography keys resolve.

## Practical Next Step

All future full-appendix editorial consolidation packages should now apply this architecture.

For Logia 61-70 and later, the editor should:

- keep the reader prose print-safe;
- use logion numbers, witness labels, canonical references, and bibliography keys;
- isolate digital repository paths under source/control sections that can be removed or transformed during print generation;
- avoid language that only makes sense inside the repository.

This architecture should be treated as a controlling document before final book generation begins.
