# IDE Codex Prompt: Build the Full 114-Logion Commentary Appendix Skeleton

## Project Goal

The project reconstructs the earliest recoverable sayings-gospel layer preserved in the Gospel of Thomas tradition.

The final reader-facing product must distinguish two layers:

1. the clean reconstructed gospel text, containing only the most responsible early reconstruction;
2. a full commentary appendix covering all 114 logia, including included, uncertain, deferred, and excluded material.

Excluded logia must not disappear. The reader must be able to understand what each excluded logion says, why it was not included, and what interpretive or historical value it still has.

## Current State

The project already has:

- a clean Ukrainian reader text;
- a normalized parallel edition;
- 114 logion cards;
- a card-quality audit;
- a workflow matrix;
- an index of all logia;
- evidence notes for many high-priority logia;
- a documented principle that the full appendix must cover all 114 logia.

## Task

Create a Ukrainian full-commentary appendix skeleton for all 114 logia.

## Output File

Create:

`reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-uk.md`

## Required Structure

The file must include:

1. A short introduction explaining that the clean reconstruction is selective, but this appendix covers all 114 logia.
2. A status legend:
   - included in clean reconstruction;
   - included only as a core;
   - uncertain;
   - deferred;
   - excluded as secondary.
3. A concise table of all 114 logia with:
   - logion number;
   - reader status;
   - reconstruction decision;
   - preliminary layer;
   - evidence note status;
   - Greek witness status;
   - card link;
   - next action.
4. A section for every logion, 1-114, with this template:
   - `## Логія N`
   - `Статус у реконструкції`
   - `Що це за матеріал`
   - `Чому включено / не включено`
   - `Джерела й контрольні файли`
   - `Що треба допрацювати`

## Data Sources

Use only existing project data from:

- `corpus/tables/logia-index.md`;
- `corpus/tables/logia-workflow-matrix.md`;
- `corpus/cards/card-quality-audit-v0.1.md`;
- `reconstruction/earliest-sayings-gospel/notes/`;
- `controls/synoptic-parallels/`.

Do not invent new conclusions.

## Quality Rules

- Do not change the clean Ukrainian reader text.
- Do not change inclusion decisions.
- Do not claim that a hypothetical Greek retroversion is an extant Greek witness.
- Keep the appendix honest: if evidence note or control files are missing, say so.
- Use this as a scaffold for future full commentary, not as a final polished commentary.

## Verification

After creating the file, verify:

- it contains exactly 114 `## Логія N` sections;
- the summary table contains 114 logion rows;
- the clean Ukrainian reader file is untouched;
- the collection log is updated.
