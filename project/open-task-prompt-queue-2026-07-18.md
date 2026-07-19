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
| 6 | `DONE` | Wealth/renunciation cluster-control | `project/ide-codex-wealth-renunciation-cluster-control-v0.1-prompt.md` | `reconstruction/earliest-sayings-gospel/wealth-renunciation-cluster-control-pass-v0.1.md` |
| 7 | `DONE` | Logion 114 publication-level exclusion rationale | `project/ide-codex-logion-114-publication-exclusion-rationale-v0.1-prompt.md` | `reconstruction/earliest-sayings-gospel/logion-114-publication-exclusion-rationale-v0.1.md` |
| 8 | `DONE` | Evidence dossier publication pass | `project/ide-codex-evidence-dossier-publication-pass-v0.1-prompt.md` | `reconstruction/earliest-sayings-gospel/evidence-dossier-publication-pass-v0.1.md` |
| 9 | `DONE` | Bibliography, rights, citation, source reproducibility | `project/ide-codex-bibliography-rights-citation-reproducibility-v0.1-prompt.md` | `project/bibliography-rights-citation-reproducibility-pass-v0.1.md` |
| 10 | `DONE` | Ritual-ethics / bridegroom follow-up for 104A | `project/ide-codex-ritual-ethics-bridegroom-104a-followup-v0.1-prompt.md` | `reconstruction/earliest-sayings-gospel/ritual-ethics-bridegroom-104a-followup-v0.1.md` |
| 11 | `DONE` | Greek retroversion publication polish | `project/ide-codex-greek-retroversion-publication-polish-v0.1-prompt.md` | `reconstruction/earliest-sayings-gospel/greek-retroversion-publication-polish-v0.1.md` |
| 12 | `DONE` | Final clean-reader freeze | `project/ide-codex-final-clean-reader-freeze-v0.1-prompt.md` | `reconstruction/earliest-sayings-gospel/final-clean-reader-freeze-v0.1.md` |
| 13 | `DONE` | Generator-ready Ukrainian and English books | `project/ide-codex-generator-ready-books-v0.1-prompt.md` | `project/generator-ready-books-pass-v0.1.md` |
| 14 | `DONE` | Final bibliography and rights verify | `project/ide-codex-final-bibliography-rights-verify-v0.1-prompt.md` | `project/final-bibliography-rights-verify-v0.1.md` |
| 15 | `DONE` | Print / digital render proof preparation | `project/ide-codex-print-digital-render-proof-v0.1-prompt.md` | `project/print-digital-render-proof-prep-v0.1.md` |
| 16 | `DONE` | Render pipeline and first proofs | `project/ide-codex-render-pipeline-first-proofs-v0.1-prompt.md` | `project/render-pipeline-first-proofs-v0.1.md` |
| 17 | `DONE` | First proof QA and layout corrections | `project/ide-codex-first-proof-qa-layout-corrections-v0.1-prompt.md` | `project/first-proof-qa-layout-corrections-v0.1.md` |
| 18 | `DONE` | Bible-style book design and index pass | `project/ide-codex-bible-style-book-design-index-pass-v0.1-prompt.md` | `project/bible-style-book-design-index-pass-v0.1.md` |
| 19 | `DONE` | Final proof polish, bibliography, and TOC | `project/ide-codex-final-proof-polish-bibliography-toc-v0.1-prompt.md` | `project/final-proof-polish-bibliography-toc-v0.1.md` |
| 20 | `DONE` | Release-candidate proof package audit | `project/ide-codex-release-candidate-proof-package-audit-v0.1-prompt.md` | `project/release-candidate-proof-package-audit-v0.1.md` |
| 21 | `DONE` | Full book assembly and typesetting pipeline | `project/ide-codex-full-book-assembly-typesetting-pipeline-v0.1-prompt.md` | `project/full-book-assembly-typesetting-pipeline-v0.1.md` |
| 22 | `DONE` | Full Ukrainian book proof QA and appendix typography | `project/ide-codex-full-ukrainian-book-proof-qa-appendix-typography-v0.1-prompt.md` | `project/full-ukrainian-book-proof-qa-appendix-typography-v0.1.md` |
| 23 | `DONE` | English full 114-logion appendix generation | `project/ide-codex-english-full-114-logion-appendix-generation-v0.1-prompt.md` | `project/english-full-114-logion-appendix-generation-v0.1.md` |
| 24 | `DONE` | English appendix editorial quality pass | `project/ide-codex-english-appendix-editorial-quality-pass-v0.1-prompt.md` | `project/english-appendix-editorial-quality-pass-v0.1.md` |
| 25 | `DONE` | Full English book proof QA and typography | `project/ide-codex-full-english-book-proof-qa-typography-v0.1-prompt.md` | `project/full-english-book-proof-qa-typography-v0.1.md` |
| 26 | `DONE` | Digital scholarly companion expansion | `project/ide-codex-digital-scholarly-companion-expansion-v0.1-prompt.md` | `project/digital-scholarly-companion-expansion-v0.1.md` |
| 27 | `DONE` | Browsable digital companion HTML | `project/ide-codex-digital-companion-browsable-html-v0.1-prompt.md` | `project/digital-companion-browsable-html-v0.1.md` |
| 28 | `NEXT` | Final production typesetting and copyedit gate | `project/ide-codex-final-production-typesetting-copyedit-gate-v0.1-prompt.md` | Decide final production path and run final copyedit/proof checklist |

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
| Wealth/renunciation cluster-control | `reconstruction/earliest-sayings-gospel/wealth-renunciation-cluster-control-pass-v0.1.md` |
| Logion 114 publication-level exclusion rationale | `reconstruction/earliest-sayings-gospel/logion-114-publication-exclusion-rationale-v0.1.md` |
| Evidence dossier publication pass | `reconstruction/earliest-sayings-gospel/evidence-dossier-publication-pass-v0.1.md` |
| Bibliography, rights, citation, source reproducibility pass | `project/bibliography-rights-citation-reproducibility-pass-v0.1.md` |
| Ritual-ethics / bridegroom 104A follow-up | `reconstruction/earliest-sayings-gospel/ritual-ethics-bridegroom-104a-followup-v0.1.md` |
| Greek retroversion publication polish | `reconstruction/earliest-sayings-gospel/greek-retroversion-publication-polish-v0.1.md` |
| Final clean-reader freeze | `reconstruction/earliest-sayings-gospel/final-clean-reader-freeze-v0.1.md` |
| Generator-ready Ukrainian and English books | `project/generator-ready-books-pass-v0.1.md` |
| Final bibliography and rights verify | `project/final-bibliography-rights-verify-v0.1.md` |
| Print / digital render proof preparation | `project/print-digital-render-proof-prep-v0.1.md` |
| Render pipeline and first proofs | `project/render-pipeline-first-proofs-v0.1.md` |
| First proof QA and layout corrections | `project/first-proof-qa-layout-corrections-v0.1.md` |
| Bible-style book design and index pass | `project/bible-style-book-design-index-pass-v0.1.md` |
| Final proof polish, bibliography, and TOC | `project/final-proof-polish-bibliography-toc-v0.1.md` |
| Release-candidate proof package audit | `project/release-candidate-proof-package-audit-v0.1.md` |
| Full book assembly and typesetting pipeline | `project/full-book-assembly-typesetting-pipeline-v0.1.md` |
| Full Ukrainian book proof QA and appendix typography | `project/full-ukrainian-book-proof-qa-appendix-typography-v0.1.md` |
| English full 114-logion appendix generation | `project/english-full-114-logion-appendix-generation-v0.1.md` |
| English appendix editorial quality pass | `project/english-appendix-editorial-quality-pass-v0.1.md` |
| Full English book proof QA and typography | `project/full-english-book-proof-qa-typography-v0.1.md` |
| Digital scholarly companion expansion | `project/digital-scholarly-companion-expansion-v0.1.md` |
| Browsable digital companion HTML | `project/digital-companion-browsable-html-v0.1.md` |

## Why The Next Task Is Final Production Typesetting And Copyedit Gate

The project now has full corpus coverage, reader interpretation coverage, all-114 decision control, a frozen 37-unit clean reader, consolidated Ukrainian and English appendix prose for all Logia 1-114, a publication-facing evidence dossier, completed Greek retroversion publication polish, completed final clean-reader freeze, full-book assembly, completed Ukrainian full-proof QA, completed English full-proof QA, an expanded Markdown/TSV/PDF digital scholarly companion, and a browsable static HTML companion. The strongest remaining quality gate is final production: decide the final typesetting path and run a disciplined human-level copyedit/proof checklist before release-candidate status.

## Execution Note

This queue intentionally separates prompt generation from large downstream execution. The downstream prompts are ready, but executing all of them in one pass would risk rushed scholarship and inconsistent documentation.
