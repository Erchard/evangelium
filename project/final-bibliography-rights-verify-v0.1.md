# Final Bibliography And Rights Verify v0.1

Date: 2026-07-18

## Purpose

This pass converts the remaining generic bibliography and rights uncertainty into concrete release decisions before book rendering.

The goal is not to pretend that every protected modern scholarly source has been fully cleared. The goal is to separate:

- sources that are verified open enough for project use;
- ancient witnesses that still need critical-edition reading checks;
- protected modern controls that may be cited or consulted but not reproduced;
- local snapshots that must not be redistributed without permission.

## Initial Marker Count

Raw markers before this pass:

| Area | `VERIFY` | `UNRESOLVED` | Main risk |
| --- | ---: | ---: | --- |
| `bibliography/bibliography-working.md` | 9 | 0 | Bibliographic and rights uncertainty mixed into one marker. |
| `bibliography/source-rights-register.md` | 0 | 7 | Several source families were not release-classified. |
| `output/uk-paper-book/book-source-uk.md` | 1 | 0 | Paper package still mentioned technical verification markers. |
| `output/en-paper-book/book-source-en.md` | 1 | 0 | Paper package still mentioned technical verification markers. |
| `output/digital-scholarly-companion/companion-manifest.md` | 1 | 0 | Digital companion still mentioned technical verification markers. |

## Verified Open Or Public-Domain Controls

| Source | Decision | Evidence used |
| --- | --- | --- |
| DCLP / Papyri.info XML for P.Oxy. 1, 654, 655 | `OPEN_WITH_ATTRIBUTION_VERIFIED` | Local TEI XML files state Digital Corpus of Literary Papyri copyright and Creative Commons Attribution 3.0 license. |
| SBLGNT | `OPEN_WITH_ATTRIBUTION_VERIFIED` | Official SBLGNT GitHub repository identifies CC BY 4.0 licensing and version history through v1.2, dated 2023-07-10. |
| Linssen Unicode Coptic transcription | `PUBLIC_DOMAIN_VERIFIED` | Local snapshot states that the Unicode transcription of Thomas is released into the public domain. |
| Mattison / Gospels.net Thomas translation | `PUBLIC_DOMAIN_VERIFIED` | Local snapshot and current Gospels.net page state public-domain dedication and use for any purpose. |
| EUAGELIA original reconstruction and commentary | `PROJECT_COMMONS` | Project-owned policy recorded in `LICENSE.md` and `project/commons-dedication-and-use-policy.md`. |

## Protected Or Control-Only Sources

These sources may support scholarly checking and be cited where appropriate, but they must not become the reproduced base text of EUAGELIA:

- P.Oxy. 5575 printed edition.
- Lambdin translation / *The Nag Hammadi Library in English*.
- Layton / Brill Coptic Gnostic Library materials.
- DeConick reconstruction and commentary.
- Patterson / Meyer / Polebridge materials.
- NA / UBS critical Greek New Testament editions.
- NASSCAL pages beyond fair citation / bibliographic use.

## Redistribution-Restricted Local Controls

These may remain in the digital research audit, but should not be redistributed as public content without permission or a stronger rights basis:

- Grondin interlinear / facsimile snapshots.
- Agraphos snapshots.
- Gnosis snapshots and protected translation collections.

## Bibliographic Updates Made

- Replaced generic `VERIFY` markers with concrete release statuses in `bibliography/bibliography-working.md`.
- Identified P.Oxy. 5575 citation as: Fish, Jeffrey, Daniel B. Wallace, and Michael W. Holmes. "5575. Sayings of Jesus." Pages 6-14 in vol. 87 of *The Oxyrhynchus Papyri*. Edited by Peter J. Parsons and Nikolaos Gonis. London: Egypt Exploration Society, 2023.
- Recorded DCLP ids for the three extant Greek Thomas papyri used locally: 62838, 62840, and 62839.
- Recorded SBLGNT official source/license/version policy.
- Converted Q and Didache from unresolved source families to `NOT_USED_IN_CURRENT_RELEASE`.
- Routed Paul / James Greek controls through the same SBLGNT policy as the other canonical controls.

## Final Marker Count

Release-table rows after this pass:

| Marker type | Count | Meaning |
| --- | ---: | --- |
| Generic `VERIFY` rows | 0 | No bibliography row now depends on an undefined verification marker. |
| Generic `UNRESOLVED` rows | 0 | No rights-register row remains unclassified. |
| `PROTECTED_CONTROL_ONLY` rows | 8 | These sources are safe to cite/consult but not safe to reproduce as base text. |
| `NEEDS_PERMISSION_FOR_REDISTRIBUTION` rows | 3 | These local controls should not be distributed publicly without permission. |
| `NEEDS_LIBRARY_CHECK` notes | 4 | These affect final page-level citations and exact protected-source references, not the clean-reader corpus. |

## Remaining Release Risks

1. The project still needs final library-level checks for protected scholarly controls if page-specific citations are printed.
2. NHC II,2 exact Coptic readings should be checked against facsimile or critical edition before claiming critical-edition precision.
3. Grondin, Agraphos, and Gnosis snapshots should stay digital/private unless permission is obtained.
4. The final bibliography still needs one uniform style before book rendering.
5. Paper books must keep print-safe keys and not rely on repository paths or clickable links.

## Validation

Commands run after this pass:

```bash
python3 tools/qa_crosscheck.py
git diff --check
```

Result:

- structural QA passed: 114/114 card files, 114/114 appendix sections, 37/37 reader units synchronized across language layers and control tables;
- whitespace diff check passed;
- Ukrainian and English paper-book source grep for internal repository paths and clickable web URLs returned no matches;
- active bibliography markers after pass: `VERIFY` = 0, `UNRESOLVED` = 0;
- source-rights table rows after pass: `OPEN_WITH_ATTRIBUTION_VERIFIED` = 3, `PUBLIC_DOMAIN_VERIFIED` = 2, `PROTECTED_CONTROL_ONLY` = 8, `NEEDS_PERMISSION_FOR_REDISTRIBUTION` = 3, `NOT_USED_IN_CURRENT_RELEASE` = 2.

## Source URLs Checked In This Pass

- SBLGNT official repository: https://github.com/LogosBible/SBLGNT
- Gospels.net Thomas page: https://www.gospels.net/thomas
- NASSCAL P.Oxy. 5575 entry: https://www.nasscal.com/e-clavis-christian-apocrypha/papyrus-oxyrhynchus-5575/
- Daniel B. Wallace note on P.Oxy. 5575 publication: https://danielbwallace.com/2023/09/04/sayings-of-jesus-papyrus-p-oxy-5575-now-published/
- Brill Layton volume page: https://brill.com/display/title/933

## Next Recommended Task

Run print/digital render proof preparation:

- build a print-safe citation key table for Ukrainian and English books;
- verify that paper source files contain no internal repository paths or digital-only notes;
- define the rendering workflow for separate Ukrainian and English paper books;
- define the digital companion manifest as the place for full URLs, source paths, snapshots, and audit trail;
- create a proof-QA report before generating final PDFs.
