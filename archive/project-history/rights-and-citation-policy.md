# Rights and Citation Policy

Status: publication-safety policy v0.1, created 2026-07-18.

## Purpose

This document defines how EUAGELIA may cite, reproduce, and distinguish source materials in paper books and in the digital scholarly companion.

The policy protects three things at once:

- the project's commons / anti-ownership commitment;
- the rights of external source holders and modern scholars;
- the reader's ability to verify the reconstruction without depending on hidden links.

## Project-Owned Work

The following EUAGELIA materials are original project contributions:

- reconstructed Ukrainian and English reader texts;
- hypothetical Greek retroversions created by this project;
- Arabic literary / Injil-layer rendering created by this project;
- commentary, interpretation, methodology, prompts, tables, and audit documents;
- selection, exclusion, and classification decisions.

These original contributions follow `project/commons-dedication-and-use-policy.md`: they may be used, adapted, published, and used commercially, provided no one claims exclusive ownership over the shared underlying EUAGELIA reconstruction or framework.

## External Materials

External materials keep their own rights status.

The project must not treat any external text as project-owned merely because it is copied into the working repository for research control.

### Public Domain / Open Materials

Open or public-domain materials may be used more freely, but still require attribution and source labels.

Current working examples:

- DCLP / Papyri.info papyrus XML: working open papyrus access layer; source register records CC BY 3.0 / CC BY status and final attribution still required.
- SBLGNT: open working canonical Greek control; GitHub repository states CC BY 4.0.
- Mark M. Mattison / Gospels.net Gospel of Thomas translation: site states the translation is committed to the public domain.

Even for open sources, the project should cite:

- source family;
- URL or repository;
- access date or snapshot date;
- license statement;
- local path in the digital companion.

### Protected Modern Sources

Protected sources may be used for verification, bibliography, scholarly comparison, and short lawful citation. They must not be reproduced as the base text of the project.

Current protected or rights-sensitive examples:

- Brill Coptic Gnostic Library materials;
- Bentley Layton editions and translations;
- April DeConick's reconstruction and translation work;
- Patterson / Meyer / Polebridge materials;
- Lambdin / Nag Hammadi Library in English materials where copyright is asserted or unclear;
- modern critical editions such as NA / UBS where not openly licensed.

Rule: protected modern translations are controls, not base text.

## Text Base Rules

The public EUAGELIA base text must be built from:

1. project-created translations and reconstructions;
2. extant manuscript witnesses where rights allow citation or transcription;
3. open source transcriptions where rights allow reuse;
4. clearly labeled hypothetical retroversions.

Do not base the clean Ukrainian or English reader on a protected modern translation.

## Greek Text Rules

Greek material must always be labeled by source status:

- `Extant Greek witness`: materially preserved in P.Oxy. 1, P.Oxy. 654, or P.Oxy. 655.
- `Lacunose extant Greek witness`: preserved but dependent on substantial restoration.
- `Partial extant Greek witness`: only part of the unit is materially preserved.
- `Greek retroversion, hypothetical`: reconstructed by EUAGELIA from Coptic and controls.

Hypothetical Greek retroversions are original project scholarship, but they are not manuscript witnesses.

## Paper Citation Rules

Paper books must not depend on repository paths or clickable links.

Use print-safe citation forms:

- `Logion 20`;
- `Appendix, Logion 20`;
- `NHC II,2`;
- `P.Oxy. 1`;
- `P.Oxy. 654`;
- `P.Oxy. 655`;
- `Mark 4:30-32`;
- `Matt 13:31-32`;
- `Luke 13:18-19`;
- short bibliography keys such as `SBLGNT`, `DCLP P.Oxy. 654`, `Mattison Thomas`, `Layton 1989`, `DeConick 2006`.

Repository paths may appear in the digital companion, not as the only citation in paper.

## Digital Companion Citation Rules

The digital scholarly companion may preserve full technical references:

- repository paths;
- source snapshots;
- TEI/XML file paths;
- evidence note paths;
- card paths;
- control-file paths;
- URLs;
- license URLs;
- commit hashes or download dates when available.

Each digital path should have a print-safe equivalent.

Example:

- print: `Logion 20; compare Mark 4:30-32, Matt 13:31-32, Luke 13:18-19; Greek layer: hypothetical retroversion.`
- digital: `corpus/cards/logion-020.md`; `reconstruction/earliest-sayings-gospel/notes/logion-020-evidence-en.md`.

## Source Snapshot Policy

Before final release, each source family should have either:

- a local snapshot under `sources/primary_texts/`;
- a stable public URL plus access date;
- a repository URL plus commit hash;
- a printed edition citation;
- or an explicit note that the source was consulted but not reproduced.

Temporary paths such as `/tmp/euagelia-sblgnt/` are acceptable during research, but final publication must replace them with a stable source note.

## Required Notice For Final Products

Each final Ukrainian paper book, English paper book, and digital scholarly companion should include:

1. a short EUAGELIA commons / anti-ownership notice;
2. a third-party source rights notice;
3. a statement that protected modern translations and editions were used only as controls unless rights allow more;
4. a statement that hypothetical Greek retroversions are project reconstructions, not manuscript witnesses.

## Remaining Verification

Before public release, verify:

- exact bibliographic data for modern editions;
- exact DCLP / Papyri.info attribution wording;
- exact SBLGNT version, source URL, and license wording;
- whether any local images or facsimile snapshots can be redistributed;
- whether a standard legal license can express the project's anti-ownership principle.
