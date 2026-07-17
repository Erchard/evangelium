# IDE Codex Prompt: Corpus Sprint 61-80 With Reconstruction-Quality Controls

## Objective

Move the project toward full completion by creating a high-quality first-pass corpus layer for Logia 61-80.

This sprint is not meant to force new material into the clean reconstructed gospel. Its purpose is to reduce the remaining blind zone in the corpus, identify strong candidates for later deepening, and prevent future inclusion decisions from being based only on already attractive or familiar sayings.

## Project Goal

The project aims to produce:

- a clean Ukrainian reconstruction of the earliest recoverable sayings-gospel layer;
- a separate Ukrainian reader commentary for every included unit;
- Coptic, Greek / Greek retroversion, Ukrainian, and English parallel forms;
- a transparent inclusion / exclusion table;
- an English evidence dossier suitable for public or scholarly review.

## Required Context To Read First

Before editing anything, read:

- `00_Project/ide-codex-master-project-prompt.md`
- `00_Project/final-product-specification.md`
- `00_Project/clean-text-plus-commentary-concept.md`
- `00_Project/project-completion-roadmap.md`
- `05_Logia_Corpus/tables/logia-workflow-matrix.md`
- `05_Logia_Corpus/tables/logia-index.md`
- `06_Reconstructions/earliest-sayings-gospel/reconstructed-gospel-uk.md`
- `06_Reconstructions/earliest-sayings-gospel/reader-commentary-uk.md`
- `06_Reconstructions/earliest-sayings-gospel/inclusion-decisions-table.md`
- `06_Reconstructions/earliest-sayings-gospel/evidence-dossier-en.md`

## Scope

Work on Logia 61-80 only.

Create or update primary cards:

- `05_Logia_Corpus/cards/logion-061.md`
- `05_Logia_Corpus/cards/logion-062.md`
- `05_Logia_Corpus/cards/logion-063.md`
- `05_Logia_Corpus/cards/logion-064.md`
- `05_Logia_Corpus/cards/logion-065.md`
- `05_Logia_Corpus/cards/logion-066.md`
- `05_Logia_Corpus/cards/logion-067.md`
- `05_Logia_Corpus/cards/logion-068.md`
- `05_Logia_Corpus/cards/logion-069.md`
- `05_Logia_Corpus/cards/logion-070.md`
- `05_Logia_Corpus/cards/logion-071.md`
- `05_Logia_Corpus/cards/logion-072.md`
- `05_Logia_Corpus/cards/logion-073.md`
- `05_Logia_Corpus/cards/logion-074.md`
- `05_Logia_Corpus/cards/logion-075.md`
- `05_Logia_Corpus/cards/logion-076.md`
- `05_Logia_Corpus/cards/logion-077.md`
- `05_Logia_Corpus/cards/logion-078.md`
- `05_Logia_Corpus/cards/logion-079.md`
- `05_Logia_Corpus/cards/logion-080.md`

## Required Source Checks

Use local project sources first:

- Coptic source: `02_Sources_And_Manuscripts/primary_texts/coptic/linssen-thomas-coptic-unicode-working.txt`
- Greek P.Oxy. files: `02_Sources_And_Manuscripts/primary_texts/greek_poxy/`
- source register: `02_Sources_And_Manuscripts/primary_texts/source-register.md`
- local SBLGNT controls where relevant:
  - `/tmp/euagelia-sblgnt/Matt.txt`
  - `/tmp/euagelia-sblgnt/Mark.txt`
  - `/tmp/euagelia-sblgnt/Luke.txt`

If a needed primary or scholarly source is missing locally, do not invent it. Mark the issue as needing external verification.

## Special Attention In This Sprint

Pay special attention to:

- Logion 61: division, reclining, Salome; possible dialogue and identity layer.
- Logion 62: mysteries / right hand / left hand; secrecy motif.
- Logion 63: rich man and death; compare Luke 12:16-21.
- Logion 64: banquet invitation; compare Matt 22:1-14 and Luke 14:15-24.
- Logion 65: wicked tenants; compare Mark 12:1-12, Matt 21:33-46, Luke 20:9-19.
- Logion 66: rejected stone; compare Mark 12:10-11 and synoptic parallels.
- Logion 67: knowing all but oneself; self-knowledge cluster.
- Logion 68-69: persecution / blessedness; compare Matt 5 and Luke 6 where relevant.
- Logion 70: what is within you will save/destroy; internalized salvation motif.
- Logion 71: destruction of house; possible temple/body/Thomasine symbol.
- Logion 72: inheritance dispute; compare Luke 12:13-15.
- Logion 73-75: harvest/laborers and bridal chamber; cluster cautiously.
- Logion 76: pearl/treasure; compare Matt 13:44-46.
- Logion 77: light / all / split wood / lift stone; important Thomasine high-Christology or presence cluster, and possible P.Oxy. 1 overlap with 30/77b.
- Logion 78: wilderness/reed/soft clothing; compare John Baptist material.
- Logion 79: womb/breasts; compare Luke 11:27-28.
- Logion 80: world/body/corpse; compare Thomas 56 and world-renunciation cluster.

## Method For Each Logion

For each logion:

1. Extract the Coptic text from the local Coptic source.
2. Check whether a loaded Greek Oxyrhynchus witness preserves any part of the logion.
3. If no extant Greek Thomas witness exists, say so clearly.
4. If a Greek form is historically likely but not extant, note that future reconstruction must be labeled `Greek retroversion, hypothetical`.
5. Provide a literal Ukrainian translation.
6. Provide a smoother working Ukrainian translation.
7. Identify obvious synoptic, early Christian, Jewish, or internal Thomas controls.
8. Split the logion into subunits if it is composite.
9. Identify early-layer indicators and secondary-layer indicators.
10. Assign a provisional status.

Allowed provisional statuses:

- `NOT_DECIDED`
- `UNCERTAIN`
- `DEFER`
- `INCLUDE_WITH_MARKER`
- `EXCLUDE_AS_SECONDARY`

Do not use unmarked `INCLUDE` in this sprint unless the evidence is unusually strong and fully documented.

## Card Template

Each card should use this structure:

```md
# Logion NN

Статус: первинна корпусна картка v0.1.

## Текст

### Коптський текст

Джерело: `02_Sources_And_Manuscripts/primary_texts/coptic/linssen-thomas-coptic-unicode-working.txt`.

> ...

### Грецький свідок

...

### Буквальний український переклад

...

### Робочий український переклад

...

## Попередні паралелі

| Джерело | Місце | Нотатка |
| --- | --- | --- |

## Аналіз

...

## Попередній статус

Рішення: `...`.

Наступна дія: ...
```

## Files To Update

After creating the cards, update:

- `05_Logia_Corpus/tables/logia-workflow-matrix.md`
- `05_Logia_Corpus/tables/logia-index.md`
- `02_Sources_And_Manuscripts/primary_texts/collection-log.md`

Only update these if a logion receives a strong decision beyond ordinary first-pass work:

- `06_Reconstructions/earliest-sayings-gospel/inclusion-decisions-table.md`
- `06_Reconstructions/earliest-sayings-gospel/evidence-dossier-en.md`
- `06_Reconstructions/earliest-sayings-gospel/reconstructed-gospel-uk.md`
- `06_Reconstructions/earliest-sayings-gospel/reader-commentary-uk.md`

In this sprint, do not add new text to the clean reconstruction unless the evidence is exceptionally strong and separable. The default outcome should be corpus coverage and candidate identification, not reader expansion.

## Quality Rules

- Preserve the difference between extant Greek witnesses and hypothetical Greek retroversions.
- Do not use modern translations as primary evidence.
- Do not force inclusion.
- Prefer subunit analysis over whole-logion judgment.
- Keep Ukrainian translations provisional but readable.
- Mark uncertainty honestly.
- Treat internal Thomas parallels as important but not sufficient proof of earliest tradition.
- Avoid turning theological interpretation into evidence.
- Update control tables so no Logia 61-80 remain `NOT_STARTED`.

## Expected Final Report

At the end, report in Ukrainian:

- which cards were created or updated;
- which logia look like strong candidates for later deepening;
- which logia look likely secondary, composite, or Thomasine;
- which logia require external source verification;
- whether any reader text was changed;
- what the next best sprint should be.
