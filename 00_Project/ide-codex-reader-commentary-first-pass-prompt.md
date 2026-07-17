# IDE Codex Prompt: First Ukrainian Reader Commentary Pass

## Objective

Create the first substantive Ukrainian reader-commentary layer for the reconstructed text already present in:

`06_Reconstructions/earliest-sayings-gospel/reconstructed-gospel-uk.md`

The goal is to make the reconstruction readable and meaningful for a non-specialist but serious Ukrainian reader, without inserting explanations into the clean reconstructed text.

## Project Context

The final product now has a two-level Ukrainian reader structure:

1. clean reconstructed text;
2. separate reader commentary for each included logion or subunit.

The commentary must help answer the reader's natural question: "What might this saying mean, and why is it here?"

## Required Inputs

Read first:

- `00_Project/ide-codex-master-project-prompt.md`
- `00_Project/clean-text-plus-commentary-concept.md`
- `00_Project/final-product-specification.md`
- `06_Reconstructions/earliest-sayings-gospel/reconstructed-gospel-uk.md`
- `06_Reconstructions/earliest-sayings-gospel/reconstructed-gospel-uk-apparatus.md`
- `06_Reconstructions/earliest-sayings-gospel/inclusion-decisions-table.md`
- `06_Reconstructions/earliest-sayings-gospel/evidence-dossier-en.md`
- relevant cards in `05_Logia_Corpus/cards/`
- relevant evidence notes in `06_Reconstructions/earliest-sayings-gospel/notes/`

Use local sources first:

- Coptic: `02_Sources_And_Manuscripts/primary_texts/coptic/linssen-thomas-coptic-unicode-working.txt`
- Greek P.Oxy.: `02_Sources_And_Manuscripts/primary_texts/greek_poxy/`
- Synoptic controls: `/tmp/euagelia-sblgnt/`

## Scope

Update:

`06_Reconstructions/earliest-sayings-gospel/reader-commentary-uk.md`

Create first-pass commentary sections for all logia or subunits currently included in `reconstructed-gospel-uk.md`:

- 1
- 2
- 3
- 4
- 5
- 6 ethical core
- 9 sower core
- 10 fire core
- 16 division core
- 20 mustard seed
- 22 children/kingdom core
- 25
- 26
- 31
- 32
- 33
- 34
- 35
- 36
- 39

Also update:

- `02_Sources_And_Manuscripts/primary_texts/collection-log.md`

Do not change the clean reconstructed text unless a clear typo is discovered.

## Commentary Section Template

For each included unit, use this structure:

```md
### Логія N

**Реконструйований текст**

> ...

**Коротко**

...

**Походження і джерела**

- Коптський текст:
- Грецький свідок:
- Рішення:
- Картка:
- Evidence note:

**Паралелі**

...

**Можливі тлумачення**

1. ...
2. ...
3. ...

**Що лишається непевним**

...

**Чому це увійшло до реконструкції**

...
```

## Quality Rules

- Write in Ukrainian.
- Keep the tone clear, calm, historically honest, and non-dogmatic.
- Do not preach.
- Do not force a single interpretation where several are plausible.
- Distinguish text, reconstruction, interpretation, and evidence.
- Do not copy modern copyrighted translations.
- Mention Greek evidence only when extant; otherwise use `No extant Greek witness in loaded P.Oxy.` or `Greek retroversion, hypothetical` if applicable.
- Keep each section compact enough for readers, but rich enough to be useful.
- Make it clear when only a core of a logion is included and the fuller Thomas form remains outside the clean text.

## Expected Result

After completion:

- `reader-commentary-uk.md` should no longer be only a template.
- Every currently included unit should have a first-pass explanatory section.
- The collection log should record the commentary sprint.
- The final report should name what was updated and identify the next best improvement pass.
