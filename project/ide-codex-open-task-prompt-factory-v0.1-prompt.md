# IDE Codex Prompt: Open-Task Prompt Factory and Execution Queue v0.1

## Objective

Create a controlled set of high-quality IDE Codex prompts for the project's still-open tasks, prioritize them, and execute the prompt-factory pass without flattening major research work into superficial edits.

The goal is not to invent new goals. The goal is to convert the current roadmap, quality audit, final product specification, and workflow matrix into a practical execution queue where every remaining major task has:

- a saved prompt;
- clear inputs;
- clear outputs;
- quality rules;
- validation commands;
- dependency order;
- execution status.

## Required Context

Read before generating or executing prompts:

- `README.md`
- `project/final-product-specification.md`
- `project/project-completion-roadmap.md`
- `project/project-quality-audit-v0.1.md`
- `project/project-map.md`
- `project/print-and-digital-publication-architecture.md`
- `corpus/tables/logia-workflow-matrix.md`
- `reconstruction/earliest-sayings-gospel/README.md`
- `reconstruction/earliest-sayings-gospel/all-114-publication-decision-table-v0.1.md`
- `reconstruction/earliest-sayings-gospel/inclusion-decisions-table.md`
- `reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-uk.md`
- `reconstruction/earliest-sayings-gospel/evidence-dossier-en.md`
- `tools/qa_crosscheck.py`

## Open Tasks To Cover

Create saved prompts for these unresolved tasks:

1. Full appendix editorial consolidation for Logia 61-70.
2. Wealth/renunciation cluster-control pass.
3. Logion 114 publication-level exclusion rationale.
4. Evidence dossier publication pass.
5. Ritual-ethics / bridegroom follow-up for 104A.
6. Bibliography, rights, citation, and source reproducibility pass.
7. Greek retroversion publication polish.

If the context shows a task is already completed, do not create a duplicate prompt. Instead, mark it complete in the queue and cite the closing file.

## Prompt Quality Standard

Each generated prompt must include:

- objective;
- why this task matters for the final product;
- exact files to read;
- exact files to create or update;
- constraints that protect the clean reader first principle;
- print/digital split requirements;
- source hierarchy and Greek retroversion rules where relevant;
- explicit non-goals;
- validation commands;
- final report requirements.

Do not generate vague prompts such as "improve documentation" or "polish text." Every prompt must be executable by another Codex session without needing this conversation.

## Execution Policy

This prompt-factory pass must execute the prompt-generation layer now:

1. Create or update `project/open-task-prompt-queue-2026-07-18.md`.
2. Save one prompt file per open task.
3. Mark each generated prompt as `READY`.
4. Mark tasks whose prerequisites are not satisfied as `BLOCKED_BY`.
5. Mark tasks that should be executed first as `NEXT`.
6. Update project documentation enough that future work points to this queue rather than stale one-off prompts.
7. Run structural validation.

Do not execute all large downstream research/editorial prompts in the same pass unless the task is small and can be completed without reducing quality. Prefer a correct queue and one well-chosen next execution over rushed completion of multiple publication passes.

## Required Outputs

Create:

- `project/open-task-prompt-queue-2026-07-18.md`
- `project/ide-codex-full-appendix-editorial-consolidation-061-070-v0.1-prompt.md`
- `project/ide-codex-wealth-renunciation-cluster-control-v0.1-prompt.md`
- `project/ide-codex-logion-114-publication-exclusion-rationale-v0.1-prompt.md`
- `project/ide-codex-evidence-dossier-publication-pass-v0.1-prompt.md`
- `project/ide-codex-ritual-ethics-bridegroom-104a-followup-v0.1-prompt.md`
- `project/ide-codex-bibliography-rights-citation-reproducibility-v0.1-prompt.md`
- `project/ide-codex-greek-retroversion-publication-polish-v0.1-prompt.md`
- `project/open-task-prompt-factory-execution-v0.1.md`

Update:

- `project/project-completion-roadmap.md`
- `project/project-map.md`
- `README.md`

## Validation

Run:

```bash
python3 tools/qa_crosscheck.py
git diff --check
```

Optionally run:

```bash
python3 tools/probability_reader_audit.py
```

## Final Report

Report:

- which open tasks were converted into prompts;
- which prompt is next to execute;
- which tasks are blocked by earlier passes;
- which files were created or updated;
- QA results;
- any known documentation drift discovered but not fixed in this pass.
