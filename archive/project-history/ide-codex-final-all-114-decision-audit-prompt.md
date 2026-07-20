# IDE Codex Prompt: Final All-114 Decision Audit

## Mission

Perform the next publication-critical control pass for the project: a final all-114 decision audit before any further clean-reader expansion or finalization.

The goal is not to force every uncertain logion into a final decision prematurely. The goal is to identify which decisions are stable, which decisions are still provisional, which files are stale, and which logia must be deepened before the clean reconstruction can be called final.

## Primary Outputs

Create or update:

- `reconstruction/earliest-sayings-gospel/final-all-114-decision-audit-v0.1.md`
- `corpus/tables/logia-workflow-matrix.md`
- `project/project-completion-roadmap.md`
- `project/publication-gap-audit-v0.1.md`
- `sources/primary_texts/collection-log.md`

Do not edit `reconstruction/earliest-sayings-gospel/reconstructed-gospel-uk.md` in this pass.

## Reference Files

- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-uk.md`
- `reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-uk.md`
- `reconstruction/earliest-sayings-gospel/inclusion-decisions-table.md`
- `reconstruction/earliest-sayings-gospel/full-corpus-classification-v0.1.md`
- `corpus/tables/logia-workflow-matrix.md`
- `reconstruction/earliest-sayings-gospel/notes/`
- `controls/synoptic-parallels/`
- `project/publication-gap-audit-v0.1.md`
- `project/project-completion-roadmap.md`

## Required Audit Questions

Answer these questions explicitly:

1. Is the current 31-unit clean reader internally supported by evidence notes, controls, language layers, and full appendix commentary?
2. Which included logia remain weakest and need publication polish before finalization?
3. Which non-included logia are the strongest remaining candidates that could still change the clean reader?
4. Which non-included logia need only appendix explanation, not reader promotion?
5. Which files are stale or inconsistent with the current project state?
6. What exact next work package should follow this audit?

## Decision Categories

Use these audit categories:

- `STABLE_CURRENT_READER`
- `CURRENT_READER_NEEDS_PUBLICATION_POLISH`
- `REOPEN_AS_STRONG_CANDIDATE`
- `SPLIT_CORE_REVIEW`
- `APPENDIX_ONLY_UNCERTAIN`
- `CLUSTER_DEFER`
- `LIKELY_SECONDARY_OR_FRAME`
- `EXCLUDE_AS_SECONDARY`
- `DOCUMENTATION_STALE`

## Quality Bar

Be honest rather than optimistic. Do not inflate certainty. A strong audit should make the next work smaller, sharper, and safer.

The audit should preserve the project's core principle: the clean reconstruction is selective, but the full appendix must eventually explain all 114 logia, including rejected or deferred material.

## Verification

After editing:

- confirm the clean Ukrainian reader was not changed;
- confirm the new audit file exists;
- confirm stale `Needs multilingual sync` notes for already synchronized current-reader units are removed or corrected;
- confirm roadmap and publication gap audit point to the next concrete work package after the audit;
- run `git diff --check`.
