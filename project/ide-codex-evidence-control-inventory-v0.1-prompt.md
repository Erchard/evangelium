# IDE Codex Prompt: Evidence and Control Inventory v0.1

You are working in the EUAGELIA project. Execute Phase 3 of the quality-remediation plan: Evidence and Control Inventory.

## Purpose

Before creating the true all-114 publication decision table, verify what evidence notes and control files actually exist. Do not rely only on the workflow matrix. The output must make visible where the project has real evidence support, where the matrix is stale, and which logia need the next evidence/control work.

## Required Context

Read first:

1. `project/project-quality-remediation-plan-v0.1.md`
2. `project/project-quality-audit-v0.1.md`
3. `project/project-completion-roadmap.md`
4. `corpus/tables/logia-workflow-matrix.md`
5. `project/clean-text-plus-commentary-concept.md`
6. `project/clean-reader-text-first-page-principle.md`
7. `corpus/cards/poxy-xml-extraction-audit-v0.1.md`

## Files To Scan

Evidence notes:

- `reconstruction/earliest-sayings-gospel/notes/`

Control files:

- `controls/`
- especially `controls/synoptic-parallels/`

Cards/table:

- `corpus/cards/logion-XXX.md`
- `corpus/tables/logia-workflow-matrix.md`

## Required Output

Create:

- `reconstruction/earliest-sayings-gospel/evidence-control-inventory-v0.1.md`

The inventory must include:

1. Executive summary.
2. Counts:
   - 114 logia covered;
   - evidence notes found;
   - matrix evidence YES/NO;
   - mismatches between matrix and actual files;
   - logia with control files;
   - logia with cluster-only controls;
   - logia with neither evidence note nor control file.
3. A full 114-logion table with:
   - logion number;
   - matrix evidence status;
   - actual evidence note files;
   - actual control / cluster files;
   - reader status;
   - current decision;
   - Greek witness status;
   - inventory priority;
   - next action.
4. A mismatch section:
   - matrix says YES but no actual evidence note found;
   - matrix says NO but actual evidence note found;
   - cards or docs say missing evidence/control but files now exist.
5. A prioritized next-work list:
   - P0: clean-reader units lacking evidence trail, if any;
   - P1: high-impact uncertain/deferred/excluded logia with strong Greek or synoptic control but missing evidence/control;
   - P2: low-priority appendix-only logia that still need at least short rationale.

## Quality Rules

- Do not create new evidence notes in this pass.
- Do not change clean reader content.
- Do not promote or demote any logion.
- If a control file covers multiple logia, mark it as cluster control.
- If a note covers a split unit, mark the exact coverage honestly.
- If a matrix entry appears stale, flag it; do not silently rewrite history.
- Treat this pass as a map for the next phase, not as final scholarship.

## Documentation Updates

After creating the inventory:

- update `project/project-map.md`;
- update `project/project-quality-remediation-plan-v0.1.md` to mark Phase 3 as completed;
- update `sources/primary_texts/collection-log.md`;
- update the master remediation prompt so the next recommended phase becomes Phase 4: true all-114 publication decision table.

## Final Report

Report:

- files changed;
- key counts;
- most important gaps found;
- recommended next step.

Commit and push the changes unless explicitly instructed not to.

