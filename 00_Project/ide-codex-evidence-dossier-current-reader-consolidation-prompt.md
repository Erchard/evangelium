# IDE Codex Prompt: Consolidate Evidence Dossier for the Current Reader Text

## Project Goal

The project aims to produce a reconstruction of the earliest recoverable sayings-gospel layer preserved in the Gospel of Thomas tradition. The final product must contain:

1. a clean Ukrainian reader text first, without comments, brackets, statuses, or technical warnings;
2. a parallel Coptic / Greek / Ukrainian / English edition;
3. a second explanatory layer with apparatus and commentary;
4. an English evidence dossier that can justify the reconstruction publicly.

## Current State

The clean Ukrainian reader and the normalized parallel edition currently contain 24 logia:

1, 2, 3, 4, 5, 6, 9, 10, 16, 20, 22, 25, 26, 31, 32, 33, 34, 35, 36, 39, 41, 54, 72, 73.

The file `06_Reconstructions/earliest-sayings-gospel/evidence-dossier-en.md` already contains a methodology and summary blocks for many of these logia, but it is not yet synchronized with the latest current reader set. In particular, Logia 41, 54, 72, and 73 must be integrated into the dossier.

## Task

Update `06_Reconstructions/earliest-sayings-gospel/evidence-dossier-en.md` so that it supports the current 24-logion reader text.

## Required Work

1. Update the dossier status from the previous working version to a new working version.
2. Update the current block summary so it explicitly includes Logia 41, 54, 72, and 73.
3. Add concise but publication-useful English summary sections for:
   - Logion 41
   - Logion 54
   - Logion 72
   - Logion 73
4. For each of these four logia include:
   - decision;
   - marked reader text;
   - main reason for inclusion;
   - Greek witness status;
   - evidence note reference;
   - synoptic control table reference;
   - reconstruction implication.
5. Keep the dossier honest:
   - do not claim extant Greek Thomas evidence where the project only has a hypothetical retroversion;
   - do not use hypothetical Greek retroversions as manuscript witnesses;
   - keep `INCLUDE_WITH_MARKER` language where uncertainty remains.
6. Do not alter the clean Ukrainian reader text in this task.
7. Update `02_Sources_And_Manuscripts/primary_texts/collection-log.md` with a short dated note describing the work.

## Quality Standard

The result should make the evidence dossier usable as the main English justification layer for the current reconstructed reader text. It does not need to be a final monograph chapter yet, but it must no longer omit any logion currently printed in the clean reader.

## Verification

After editing, verify:

- the dossier contains summary headings for all 24 current reader logia;
- Logia 41, 54, 72, and 73 have evidence note and synoptic control references;
- no new claim presents a hypothetical Greek retroversion as extant Greek;
- the clean Ukrainian reader remains untouched.
