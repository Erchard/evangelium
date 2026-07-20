# Working Bibliography

Status: release verification pass v0.2, updated 2026-07-18.

## Purpose

This file lists source families and scholarly works needed for EUAGELIA publication. It is not yet a final formatted bibliography, but the earlier generic verification markers have been converted into concrete release statuses.

Release statuses used here:

- `VERIFIED_OPEN`: source identity and open-use claim have been checked against local source text, an official source, or both.
- `PRIMARY_WITNESS_WITH_EDITION_CHECK_PENDING`: ancient witness is identified, but final facsimile / critical-edition citation and reading checks still require library-level verification.
- `PROTECTED_CONTROL_ONLY`: source may be cited or consulted, but must not become the project's reproduced base text.
- `NEEDS_LIBRARY_CHECK`: bibliographic skeleton is usable for internal planning, but final page references, imprint, edition, or copyright details require a library catalogue, publisher page, or physical/digital edition.
- `NOT_USED_IN_CURRENT_RELEASE`: do not cite in the printed book unless a later pass adds a defined source.

## Verification Summary 2026-07-18

- DCLP / Papyri.info XML files for P.Oxy. 1, 654, and 655 locally state Digital Corpus of Literary Papyri copyright and Creative Commons Attribution 3.0 licensing.
- Linssen's Unicode Coptic Thomas snapshot locally states that the Unicode transcription is released into the public domain.
- Gospels.net / Mark M. Mattison's Thomas page locally and currently online states that the English translation is committed to the public domain and may be used for any purpose.
- The official SBLGNT GitHub repository identifies the SBLGNT as CC BY 4.0, with version history through v1.2, 2023-07-10.
- NASSCAL gives a usable bibliographic citation for P.Oxy. 5575; the printed Oxyrhynchus edition remains protected and is control-only.
- Brill / Layton, Lambdin, DeConick, Patterson / Meyer, NA / UBS, and similar modern scholarly controls remain protected unless a specific open license or permission is obtained.

## Primary Witnesses And Open Working Sources

### NHC II,2

Short key: `NHC II,2`

Witness label for print: `NHC II,2`

Working description: Coptic Gospel of Thomas in Nag Hammadi Codex II, tractate 2, pages 32.10-51.28.

Status: `PRIMARY_WITNESS_WITH_EDITION_CHECK_PENDING`.

Release note: the project may cite the ancient witness as `NHC II,2`, but final public claims about exact Coptic readings should be checked against a facsimile or a critical edition. Do not reproduce protected Brill / Layton edition text as the open base.

Use in EUAGELIA: complete preserved Coptic witness and base source family for Coptic layer.

### P.Oxy. 1

Short key: `P.Oxy. 1`

Witness label for print: `P.Oxy. 1`

Working description: Greek Oxyrhynchus papyrus fragment preserving Thomas material, using local DCLP/Papyri.info TEI XML snapshot `sources/primary_texts/greek_poxy/dclp-poxy1-62838.xml`.

Status: `VERIFIED_OPEN` for the local DCLP/Papyri.info TEI XML layer; printed-edition comparison remains a scholarly quality check.

DCLP id: `62838`; DCLP hybrid id in local XML: `p.oxy;1;1`.

Rights note: local XML states Creative Commons Attribution 3.0 licensing for the DCLP work.

Use in EUAGELIA: extant or partial Greek witness for relevant clean-reader and appendix units.

### P.Oxy. 654

Short key: `P.Oxy. 654`

Witness label for print: `P.Oxy. 654`

Working description: Greek Oxyrhynchus papyrus fragment preserving Thomas prologue / early logia, using local DCLP/Papyri.info TEI XML snapshot `sources/primary_texts/greek_poxy/dclp-poxy654-62840.xml`.

Status: `VERIFIED_OPEN` for the local DCLP/Papyri.info TEI XML layer; printed-edition comparison remains a scholarly quality check.

DCLP id: `62840`; DCLP hybrid id in local XML: `p.oxy;4;654`.

Rights note: local XML states Creative Commons Attribution 3.0 licensing for the DCLP work.

Use in EUAGELIA: extant / lacunose Greek witness for Logia 1-7.

### P.Oxy. 655

Short key: `P.Oxy. 655`

Witness label for print: `P.Oxy. 655`

Working description: Greek Oxyrhynchus papyrus fragment preserving Thomas-related material around Logia 24(?), 36-39, using local DCLP/Papyri.info TEI XML snapshot `sources/primary_texts/greek_poxy/dclp-poxy655-62839.xml`.

Status: `VERIFIED_OPEN` for the local DCLP/Papyri.info TEI XML layer; printed-edition comparison remains a scholarly quality check.

DCLP id: `62839`; DCLP hybrid id in local XML: `p.oxy;4;655`.

Rights note: local XML states Creative Commons Attribution 3.0 licensing for the DCLP work.

Use in EUAGELIA: Greek witness/control for relevant papyrus-boundary logia.

### P.Oxy. 5575

Short key: `P.Oxy. 5575`

Witness label for print: `P.Oxy. 5575`

Working citation: Fish, Jeffrey, Daniel B. Wallace, and Michael W. Holmes. "5575. Sayings of Jesus." Pages 6-14 in vol. 87 of *The Oxyrhynchus Papyri*. Edited by Peter J. Parsons and Nikolaos Gonis. London: Egypt Exploration Society, 2023.

Status: `PROTECTED_CONTROL_ONLY`.

Release note: NASSCAL identifies transcription on p. 9 and English translation on p. 11. Use as bibliographic/control evidence only; do not reproduce the modern edition text as project base text.

Use in EUAGELIA: control for early sayings circulation; not a direct Thomas witness for the clean reader.

### DCLP / Papyri.info

Short key: `DCLP`

Working description: Digital Corpus of Literary Papyri / Papyri.info TEI XML access points for papyrus transcriptions.

Rights note: `VERIFIED_OPEN`; local TEI XML states Creative Commons Attribution 3.0 licensing. Include attribution to the Digital Corpus of Literary Papyri / Papyri.info in digital apparatus and where DCLP readings materially support a printed claim.

Use in EUAGELIA: open working access to Greek papyri.

### SBLGNT

Short key: `SBLGNT`

Working description: Society of Biblical Literature Greek New Testament, used as open Greek canonical control for Matthew, Mark, and Luke.

Rights note: `VERIFIED_OPEN`; official GitHub repository states Creative Commons Attribution 4.0 International licensing. Version history on the repository identifies v1.2, 2023-07-10.

Use in EUAGELIA: canonical Greek control only; not a Thomas witness.

Release note: cite official source URL and access date in the final bibliography. SBLGNT remains a canonical comparison layer only, not a Thomas witness.

## Open Or Public-Domain Translation Controls

### Mattison Thomas

Short key: `Mattison Thomas`

Working description: Mark M. Mattison, public-domain English translation of the Gospel of Thomas on Gospels.net.

Rights note: `VERIFIED_OPEN`; local snapshot and current Gospels.net page state public-domain dedication and allow use for any purpose.

Use in EUAGELIA: open translation control only; not the base text of the EUAGELIA reconstruction.

## Protected Or Rights-Sensitive Scholarly Controls

### Lambdin / Nag Hammadi Library in English

Short key: `Lambdin`

Working description: Thomas O. Lambdin's English translation in James M. Robinson, ed., *The Nag Hammadi Library in English*.

Status: `PROTECTED_CONTROL_ONLY`; `NEEDS_LIBRARY_CHECK` for the exact edition / printing and any page-specific citation used in print.

Rights note: use as control only; do not reproduce the protected translation as project base text.

### Layton

Short key: `Layton`

Working description: Bentley Layton, ed., *Nag Hammadi Codex II, 2-7, together with XIII, 2*, Brit. Lib. Or. 4926(1), and P.Oxy. 1, 654, 655*. Nag Hammadi Studies / Coptic Gnostic Library 20. Leiden: E. J. Brill, 1989.

Status: `PROTECTED_CONTROL_ONLY`; Brill bibliographic identity checked online, but page-specific use still needs library/edition check.

Rights note: protected modern academic work; use as control only.

### DeConick

Short key: `DeConick`

Working description: April D. DeConick, *The Original Gospel of Thomas in Translation: With a Commentary and New English Translation of the Complete Gospel*. Library of New Testament Studies 287. London / New York: T&T Clark / A&C Black, 2006/2007.

Status: `PROTECTED_CONTROL_ONLY`; `NEEDS_LIBRARY_CHECK` for exact imprint/year and page-specific references.

Rights note: protected modern academic work; use as scholarly model and control only.

### Patterson / Meyer

Short key: `Patterson`, `Meyer`

Working description: Stephen J. Patterson, Marvin Meyer, and related materials in Robert J. Miller, ed., *The Complete Gospels: Annotated Scholars Version*. Sonoma, CA: Polebridge Press, 1992 and later editions.

Status: `PROTECTED_CONTROL_ONLY`; `NEEDS_LIBRARY_CHECK` for exact edition and page references if cited in print.

Rights note: protected modern translations and commentary; use as controls only.

### Brill Coptic Gnostic Library

Short key: `Brill CGL`

Working description: Brill / Coptic Gnostic Library editions and related academic access, especially Layton's Nag Hammadi Codex II,2-7 volume.

Status: `PROTECTED_CONTROL_ONLY`; final page references require library/edition check.

Rights note: protected academic source; use for verification, not as reproduced base text.

### NA / UBS Greek New Testament

Short key: `NA`, `UBS`

Working description: modern critical editions of the Greek New Testament.

Status: `PROTECTED_CONTROL_ONLY`; not selected as the open canonical base for the current release.

Rights note: protected critical editions; use for final scholarly checking and citation, not as open base text unless rights allow. The current public canonical control policy uses SBLGNT instead.

## Sources To Define Later

### Q Reconstructions

Short key: `Q`

Status: `NOT_USED_IN_CURRENT_RELEASE`. Select a specific edition or model only if the project later uses Q as a cited control.

### Didache

Short key: `Didache`

Status: `NOT_USED_IN_CURRENT_RELEASE`. Select a public-domain or licensed Greek edition before citation.

### Paul / James

Short key: `Paul`, `James`

Status: canonical controls follow the current SBLGNT policy unless a later task selects another edition.

## Final Bibliography Tasks

- Convert `NEEDS_LIBRARY_CHECK` entries into final formatted citations before publication if they are cited with page-level specificity.
- Choose final bibliography style.
- Add publisher, year, edition, and page data where needed.
- Add stable URLs and access dates for open digital resources.
- Ensure every print citation key used in final books resolves here.
