# IDE Codex Prompt: Logion 63 Status Hotfix v0.1

You are working in the EUAGELIA project.

## Goal

Fix the P0 synchronization defect identified in:

- `project/logion-numbering-text-crosscheck-2026-07-18.md`

Logion 63 is already included in the clean reader as a marked short rich-fool core, but the full Ukrainian appendix and some control notes still contain stale pre-promotion language.

## Current Correct Decision

For Logion 63:

- short rich-fool core: `INCLUDE_WITH_MARKER`;
- full Thomas logion: `UNCERTAIN`;
- reader text: YES;
- Greek status: `Greek retroversion, hypothetical`;
- main control: Luke 12:16-21;
- key caution: Luke-dependence remains possible, and the reader should not import Luke's divine speech or explicit moral conclusion.

## Files To Edit

1. `reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-uk.md`
2. `reconstruction/earliest-sayings-gospel/notes/logion-063-evidence-en.md`
3. `controls/synoptic-parallels/logion-063-rich-fool-luke-control.md`
4. `project/logion-numbering-text-crosscheck-2026-07-18.md`

## Required Changes

### Appendix

Rewrite only the Logion 63 section.

The section must say clearly:

- Logion 63 is partially in the clean reconstruction.
- The printed clean-reader core is:
  - `Багатий чоловік мав багато майна. Він планував посіяти, пожати, посадити і наповнити комори, щоб не мати нестачі. Тієї ночі він помер.`
- The full logion remains uncertain.
- No loaded Greek Oxyrhynchus witness preserves Thomas 63.
- Luke 12:16-21 is the key canonical control.
- The appendix must explain possible Thomas-shorter-core vs Luke-dependence options without deciding more than the evidence allows.

Remove stale lines saying:

- `Reader status: Не включено`
- `Рішення: UNCERTAIN` as the whole decision
- `Не включено, бо...`
- `Compare Luke 12 rich fool; decide core separately.`

### Evidence Note

Update the note from pre-promotion candidate language to post-promotion rationale:

- Decision: rich-fool core `INCLUDE_WITH_MARKER`; full Logion 63 `UNCERTAIN`.
- Reconstruction implication: already included in clean reader with marker.
- Remaining work: publication polish, full Coptic/source verification, Luke-dependence warning.

### Control File

Update from candidate language to current control language:

- It is no longer "strongest remaining non-included candidate."
- Decision should be:
  - short rich-fool core: `READER_INCLUDE_MARKED`;
  - full Thomas form: `UNCERTAIN`.
- Next work should no longer say "before promotion"; it should say "before final publication/freeze."

### Audit

Mark the P0 Logion 63 defect as resolved in the crosscheck audit and keep a short note of what was changed.

## Verification

Run checks confirming:

- Logion 63 appendix section does not contain `Reader status: Не включено`.
- Logion 63 appendix section contains `Чистий текст реконструкції`.
- Logion 63 appendix section contains `INCLUDE_WITH_MARKER`.
- Logion 63 appendix section contains `Luke 12:16-21`.
- Evidence note no longer says `not ready for reader inclusion`.
- Control file no longer says `non-included candidate`.
- Clean-reader number set remains unchanged at 34 units.

Do not change the clean reader text in this hotfix.
