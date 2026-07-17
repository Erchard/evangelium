# IDE Codex Prompt: Normalize All Logion Cards to the Gold-Standard Analytical Level

## Project Goal

The project reconstructs the earliest recoverable sayings-gospel layer preserved in the Gospel of Thomas tradition. The card corpus must support that goal by making every logion assessable under the same evidentiary method.

## Problem

Not all `05_Logia_Corpus/cards/logion-*.md` cards have the same quality. Some cards are deep analytical cards, while many later cards are short primary cards. This makes it difficult to compare logia fairly.

## Gold Standard

Use `05_Logia_Corpus/cards/logion-002.md` as the formal gold-standard card because the workflow matrix already marks it as `Gold standard v0.2`.

Use `05_Logia_Corpus/cards/logion-006.md` as a secondary model for composite sayings, because it separates a possible early core from a larger uncertain composition.

## Task

Bring all 114 logion cards to a shared analytical baseline without inventing new source data.

## Required Work

1. Create or update a project standard document explaining what makes a logion card high quality.
2. For every `05_Logia_Corpus/cards/logion-*.md` file, add a standardized quality-alignment block if it does not already exist.
3. The block must include:
   - the formal standard used;
   - current reconstruction decision;
   - reader-text status;
   - Greek witness status;
   - preliminary layer;
   - probability profile from the index where available;
   - evidence note status and link where available;
   - synoptic/control file links where available;
   - immediate next action;
   - a warning not to treat hypothetical Greek retroversion as extant manuscript evidence.
4. Use only existing project data from:
   - `05_Logia_Corpus/tables/logia-index.md`;
   - `05_Logia_Corpus/tables/logia-workflow-matrix.md`;
   - `06_Reconstructions/earliest-sayings-gospel/notes/`;
   - `04_Synoptic_Parallels/`.
5. Do not alter the clean Ukrainian reader text.
6. Do not change inclusion decisions during this task.
7. Update `05_Logia_Corpus/cards/LOGION_TEMPLATE.md` so future cards follow the same standard.
8. Update `02_Sources_And_Manuscripts/primary_texts/collection-log.md`.

## Quality Standard

This task is a normalization and audit step, not a full scholarly rewrite of every card. The goal is to make every card comparable, transparent, and ready for targeted deepening.

Cards with no evidence note or control table must say so explicitly. This is a feature, not a failure: it shows the remaining work.

## Verification

After editing, verify:

- there are still 114 logion cards;
- all 114 cards contain `## Еталонне вирівнювання картки v0.1`;
- the clean Ukrainian reader file is untouched;
- no card claims that `Greek retroversion, hypothetical` is an extant Greek witness.
