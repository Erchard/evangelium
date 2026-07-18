# IDE Codex Prompt: Full Appendix Reader Interpretation Sync v0.1

## Project Goal

EUAGELIA reconstructs the earliest recoverable sayings-gospel layer while keeping a strict separation between:

- the clean reconstructed reader text;
- the full 114-logion appendix;
- the evidence dossier and source-language apparatus.

The previous pass added reader-facing Ukrainian interpretation sections to all 114 corpus cards. The next quality step is to make that work visible in the full appendix, so the reader can use the appendix as a real second layer after the clean text.

## Task

Synchronize `reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-uk.md` with the new card-level reader interpretation layer.

For every `## Логія N` section, insert or replace a subsection:

`### Читацьке тлумачення з картки`

This subsection must be sourced from the matching card:

`corpus/cards/logion-NNN.md`

Use the card section:

`## Читацьке тлумачення`

Convert its internal headings from `###` to `####` so the appendix hierarchy remains valid.

## Editorial Rules

- Do not change the clean reconstructed reader text.
- Do not promote or exclude any logion in this pass.
- Do not remove source/evidence blocks.
- Preserve stronger existing appendix commentary.
- Remove obsolete scaffold language that says the section still needs to be turned into a full reader commentary when the new card-derived reader interpretation is now present.
- Keep uncertainty visible.
- Treat excluded, deferred, uncertain, and appendix-only logia with the same seriousness as included logia.

## Documentation

After the sync:

- update the appendix status line;
- create a short audit document for this sync pass;
- update project navigation/status files so the new appendix state is discoverable.

## Acceptance Criteria

- `full-logion-commentary-appendix-uk.md` has 114 `### Читацьке тлумачення з картки` sections.
- No remaining obsolete scaffold sentence: `Для фінального читацького додатку цей розділ треба перетворити з каркаса...`
- Existing evidence/source sections remain present.
- `git diff --check` passes.

