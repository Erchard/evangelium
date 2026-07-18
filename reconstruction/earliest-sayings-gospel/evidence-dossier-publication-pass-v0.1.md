# Evidence Dossier Publication Pass v0.1

Status: completed 2026-07-18.

## Scope

This pass transformed `reconstruction/earliest-sayings-gospel/evidence-dossier-en.md` from a working evidence dossier into a publication-facing English draft.

The clean reader was not changed. The current reader remains 37 logia or marked cores:

1, 2, 3, 4, 5, 6, 9, 10, 16, 20, 22, 25, 26, 31, 32, 33, 34, 35, 36, 39, 41, 45A, 46A, 47B, 54, 63, 72, 73, 86, 89, 91A, 95, 96, 99, 100, 103A, and 107.

## Main Changes

- Reframed the dossier under the title `Evidence Dossier For The Earliest Sayings Gospel Reconstruction`.
- Updated the status to `publication-facing draft v1.4`.
- Added a clear thesis explaining that the project reconstructs an earliest recoverable sayings-gospel layer, not the whole Coptic Gospel of Thomas.
- Added a source hierarchy that distinguishes extant manuscript witnesses, Greek papyri, Coptic NHC II, DCLP/Papyri.info working access, canonical Greek controls, hypothetical Greek retroversions, academic editions, and modern translations.
- Added a reconstruction method section with decision categories for included, marked, uncertain, appendix-only, deferred, and secondary material.
- Added clean-reader selection principles explaining why attractive or plausibly old sayings are not automatically printed in the clean reconstruction.
- Added explicit Greek witness / retroversion policy: hypothetical Greek retroversions must never be treated as manuscript witnesses.
- Added probability-versus-reader-decision control to explain why high early probability is not identical to inclusion.
- Added cluster-control method and summaries for beatitudes, seek/find, family-renunciation, fire/kingdom, wealth/renunciation, and thief/watchfulness.
- Added a current 37-unit reader block.
- Added a major appendix-only and exclusion table covering Logia 64, 76, 90, 93, 94, 104, 109, 113, and 114.
- Added an uncertainty model and alternative-reconstruction section.
- Added a provisional bibliography, rights, and citation note.
- Preserved the existing logion-by-logion summaries and the Logion 114 exclusion summary as the detailed evidence layer.

## Publication Caveats

The dossier is now fit as a serious publication-facing draft, but it is not yet a fully final academic apparatus.

Remaining caveats:

- final bibliography entries still require verification;
- rights statements for external source families still need a dedicated pass;
- paper-facing citation keys must replace or supplement repository paths before print generation;
- source snapshots and reproducibility notes must be consolidated;
- academic editions must be cited as scholarly controls without reproducing protected modern text;
- the English prose should receive a final style pass after bibliography and citation keys are stable.

## Next Recommended Step

Execute `project/ide-codex-bibliography-rights-citation-reproducibility-v0.1-prompt.md`.

Reason: the evidence dossier now openly depends on a final bibliography / rights / citation / reproducibility layer. Closing that layer is the highest-value next step before Greek publication polish, final clean-reader freeze, and book generation.

## Validation

Run after this pass:

```bash
python3 tools/qa_crosscheck.py
git diff --check
```
