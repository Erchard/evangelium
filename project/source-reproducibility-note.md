# Source Reproducibility Note

Status: release verification pass v0.2, updated 2026-07-18.

## Purpose

EUAGELIA must remain reproducible in two environments:

- paper readers, who need stable printed references;
- digital researchers, who need local source paths, snapshots, and extraction notes.

This file records how the current source base can be checked again.

## Current Source Families

| Source family | Current local basis | Print-safe label | Reproducibility status |
| --- | --- | --- | --- |
| Coptic Thomas | `sources/primary_texts/coptic/linssen-thomas-coptic-unicode-working.txt`; Grondin snapshots and images | `NHC II,2` | Linssen public-domain claim verified locally; final facsimile / Brill / Layton reading check still needed for critical-edition precision. |
| Greek Thomas P.Oxy. 1 | `sources/primary_texts/greek_poxy/dclp-poxy1-62838.xml`; Agraphos and NASSCAL snapshots | `P.Oxy. 1` | DCLP TEI/XML local snapshot exists and carries CC BY 3.0 license; final printed-edition comparison remains scholarly QA. |
| Greek Thomas P.Oxy. 654 | `sources/primary_texts/greek_poxy/dclp-poxy654-62840.xml`; Agraphos and NASSCAL snapshots | `P.Oxy. 654` | DCLP TEI/XML local snapshot exists and carries CC BY 3.0 license; final printed-edition comparison remains scholarly QA. |
| Greek Thomas P.Oxy. 655 | `sources/primary_texts/greek_poxy/dclp-poxy655-62839.xml`; Agraphos and NASSCAL snapshots | `P.Oxy. 655` | DCLP TEI/XML local snapshot exists and carries CC BY 3.0 license; final printed-edition comparison remains scholarly QA. |
| P.Oxy. 5575 | `sources/primary_texts/greek_poxy/gospels-net-poxy5575-snapshot.html`; `sources/primary_texts/notes/nasscal-poxy5575-snapshot.html` | `P.Oxy. 5575` | Bibliographic citation identified; protected control only; not a direct Thomas witness for the clean reader. |
| Canonical Greek controls | Extracted locally from SBLGNT cache during canonical Greek pass | `SBLGNT` | Official source/license/version identified: SBLGNT GitHub, CC BY 4.0, v1.2 dated 2023-07-10. |
| Modern translations | Link/snapshot controls only where allowed | author-date keys | Protected controls unless a public-domain or open-license notice is verified. Mattison Thomas is verified public-domain; Lambdin/Layton/DeConick/Patterson/Meyer remain control-only. |

## Reproducibility Rules

1. Every source cited in print must have a human-readable label.
2. Every digital source path must map to a print-safe label.
3. Every local extraction must identify whether it comes from:
   - extant witness;
   - open transcription;
   - project retroversion;
   - canonical control;
   - protected modern scholarly control.
4. Temporary extraction caches must not be the only reproducibility basis.
5. Protected sources may be named and cited, but not reproduced as the project's open base text.

## SBLGNT Working-Control Note

The project used SBLGNT as the local working Greek control for Matthew, Mark, and Luke. This is a canonical comparison layer, not a Thomas manuscript witness.

Earlier extraction used a temporary local cache path:

- `/tmp/euagelia-sblgnt/Matt.txt`
- `/tmp/euagelia-sblgnt/Mark.txt`
- `/tmp/euagelia-sblgnt/Luke.txt`

For final release, do not cite those temporary paths. Cite:

- official repository or distribution URL;
- version number, currently v1.2 dated 2023-07-10;
- CC BY 4.0 license statement;
- access date;
- optional local stable snapshot path if redistribution is compatible and useful for digital reproducibility.

## Papyrus XML Note

The DCLP / Papyri.info XML files are local working access points to Greek papyri, not substitutes for final papyrological checking.

Current files:

- `sources/primary_texts/greek_poxy/dclp-poxy1-62838.xml`
- `sources/primary_texts/greek_poxy/dclp-poxy654-62840.xml`
- `sources/primary_texts/greek_poxy/dclp-poxy655-62839.xml`

Current release status:

- local DCLP XML license wording verified as Creative Commons Attribution 3.0;
- DCLP ids recorded in the bibliography: 62838, 62840, and 62839;
- source URLs and access dates should still be included in final formatted bibliography;
- compare important readings with printed editions where available;
- preserve lacuna and restoration markers in any public Greek layer.

## Coptic Note

The current full Coptic working text depends mainly on Linssen / Grondin working materials and local extractions from NHC II,2.

Before final critical-edition-level release:

- verify the exact Coptic text of included units against facsimile or a critical edition;
- avoid reproducing protected Brill / Layton text beyond lawful citation;
- record page / tractate coordinates for each included unit;
- preserve `NHC II,2` as the print-safe witness label.

## Minimum Final Checklist

Before final book generation:

- `bibliography/bibliography-working.md` has no generic unresolved essential source family;
- `bibliography/source-rights-register.md` has a status for each source family;
- every final print citation resolves to a bibliography key;
- every source snapshot used in a card or dossier has a local path or stable external URL;
- every hypothetical Greek retroversion is labeled as hypothetical;
- protected sources are used only as controls unless permission or open terms are documented;
- QA passes with `python3 tools/qa_crosscheck.py`;
- whitespace check passes with `git diff --check`.
