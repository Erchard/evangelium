# Open-Task Prompt Queue

Status: active execution queue, generated 2026-07-18.

This queue replaces ad hoc selection among older one-off prompts. It does not delete historical prompts; it identifies the current executable prompts for the remaining publication-quality work.

## Queue Policy

- `NEXT`: execute first unless the user explicitly chooses another task.
- `READY`: prompt is saved and prerequisites are satisfied.
- `BLOCKED_BY`: prompt is saved, but should wait for an earlier dependency.
- `DONE`: completed task; do not re-run unless a later audit reopens it.

Run `python3 tools/qa_crosscheck.py` before and after every task that changes clean reader, appendix, language layers, decision tables, or project documentation.

## Current Ordered Queue

| Priority | Status | Task | Prompt | Main Output |
| ---: | --- | --- | --- | --- |
| 1 | `DONE` | Full appendix editorial consolidation, Logia 61-70 | `project/ide-codex-full-appendix-editorial-consolidation-061-070-v0.1-prompt.md` | `reconstruction/earliest-sayings-gospel/full-appendix-editorial-consolidation-061-070-v0.1.md` |
| 2 | `DONE` | Full appendix editorial consolidation, Logia 71-80 | `project/ide-codex-full-appendix-editorial-consolidation-071-080-v0.1-prompt.md` | `reconstruction/earliest-sayings-gospel/full-appendix-editorial-consolidation-071-080-v0.1.md` |
| 3 | `DONE` | Full appendix editorial consolidation, Logia 81-90 | `project/ide-codex-full-appendix-editorial-consolidation-081-090-v0.1-prompt.md` | `reconstruction/earliest-sayings-gospel/full-appendix-editorial-consolidation-081-090-v0.1.md` |
| 4 | `DONE` | Full appendix editorial consolidation, Logia 91-100 | `project/ide-codex-full-appendix-editorial-consolidation-091-100-v0.1-prompt.md` | `reconstruction/earliest-sayings-gospel/full-appendix-editorial-consolidation-091-100-v0.1.md` |
| 5 | `DONE` | Full appendix editorial consolidation, Logia 101-114 | `project/ide-codex-full-appendix-editorial-consolidation-101-114-v0.1-prompt.md` | `reconstruction/earliest-sayings-gospel/full-appendix-editorial-consolidation-101-114-v0.1.md` |
| 6 | `NEXT` | Wealth/renunciation cluster-control | `project/ide-codex-wealth-renunciation-cluster-control-v0.1-prompt.md` | Cluster note, pass audit, table/card/appendix updates |
| 7 | `READY` | Logion 114 publication-level exclusion rationale | `project/ide-codex-logion-114-publication-exclusion-rationale-v0.1-prompt.md` | Evidence/exclusion note and appendix/dossier updates |
| 8 | `BLOCKED_BY 5-7` | Evidence dossier publication pass | `project/ide-codex-evidence-dossier-publication-pass-v0.1-prompt.md` | Publication-ready English evidence dossier draft |
| 8 | `READY` | Ritual-ethics / bridegroom follow-up for 104A | `project/ide-codex-ritual-ethics-bridegroom-104a-followup-v0.1-prompt.md` | Cluster follow-up resolving 104A reader pressure |
| 9 | `READY` | Bibliography, rights, citation, source reproducibility | `project/ide-codex-bibliography-rights-citation-reproducibility-v0.1-prompt.md` | Rights/citation policy and bibliography/reproducibility files |
| 10 | `BLOCKED_BY 5,8,9` | Greek retroversion publication polish | `project/ide-codex-greek-retroversion-publication-polish-v0.1-prompt.md` | Final Greek confidence and retroversion consistency polish |

## Completed Recent Dependencies

| Task | Closing File |
| --- | --- |
| Thief/watchfulness cluster-control for Logia 21/103 | `reconstruction/earliest-sayings-gospel/thief-watchfulness-cluster-control-pass-21-103-v0.1.md` |
| Controlled reader pass 46A/91A | `reconstruction/earliest-sayings-gospel/controlled-reader-candidate-pass-46a-91a-v0.1.md` |
| Fire/kingdom cluster-control | `reconstruction/earliest-sayings-gospel/fire-kingdom-cluster-control-pass-v0.1.md` |
| Full appendix editorial consolidation 51-60 | `reconstruction/earliest-sayings-gospel/full-appendix-editorial-consolidation-051-060-v0.1.md` |
| Greek-layer freeze | `project/greek-layer-freeze-audit-2026-07-18.md` |
| Full appendix editorial consolidation 61-70 | `reconstruction/earliest-sayings-gospel/full-appendix-editorial-consolidation-061-070-v0.1.md` |
| Full appendix editorial consolidation 71-80 | `reconstruction/earliest-sayings-gospel/full-appendix-editorial-consolidation-071-080-v0.1.md` |
| Full appendix editorial consolidation 81-90 | `reconstruction/earliest-sayings-gospel/full-appendix-editorial-consolidation-081-090-v0.1.md` |
| Full appendix editorial consolidation 91-100 | `reconstruction/earliest-sayings-gospel/full-appendix-editorial-consolidation-091-100-v0.1.md` |
| Full appendix editorial consolidation 101-114 | `reconstruction/earliest-sayings-gospel/full-appendix-editorial-consolidation-101-114-v0.1.md` |

## Why The Next Task Is Wealth/Renunciation Cluster-Control

The project now has full corpus coverage, reader interpretation coverage, all-114 decision control, 37 synchronized clean-reader units, and consolidated appendix prose for all Logia 1-114. The next unresolved content-control pressure is the wealth/renunciation cluster, especially Logia 81 and 110, before the evidence dossier publication pass and final reader freeze.

## Execution Note

This queue intentionally separates prompt generation from large downstream execution. The downstream prompts are ready, but executing all of them in one pass would risk rushed scholarship and inconsistent documentation.
