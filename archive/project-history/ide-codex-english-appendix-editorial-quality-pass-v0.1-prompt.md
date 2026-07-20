# IDE Codex Prompt: English Appendix Editorial Quality Pass v0.1

You are working in the EUAGELIA project.

## Objective

Raise `reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-en.md` from a complete generated structural draft to a genuinely readable English commentary appendix suitable for the English paper book.

Do not change the frozen clean reader or the publication decisions. This is an editorial and explanatory quality pass.

## Required Inputs

Read:

- `reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-en.md`
- `reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-uk.md`
- `reconstruction/earliest-sayings-gospel/all-114-publication-decision-table-v0.1.md`
- `reconstruction/earliest-sayings-gospel/evidence-dossier-en.md`
- `project/english-full-114-logion-appendix-generation-v0.1.md`
- `project/full-ukrainian-book-proof-qa-appendix-typography-v0.1.md`
- `tools/qa_crosscheck.py`
- `tools/assemble_full_book_sources.py`
- `tools/render_full_book_proofs.py`

## Work Plan

1. Run `python3 tools/qa_crosscheck.py` before edits.
2. Audit the English appendix for generic repeated wording, thin interpretation, awkward generated prose, and places where Ukrainian appendix nuance was lost.
3. Prioritize quality in this order:
   - all clean-reader logia and split-core logia;
   - Logion 114 as the explicit exclusion case;
   - high-interest appendix-only or deferred logia: 7, 8, 11, 17, 18, 21, 23, 24, 27-30, 37-40, 42, 44, 48-52, 55-60, 64-66, 76-82, 90, 92-94, 97-98, 101, 104-106, 109-113;
   - remaining lower-risk deferred logia.
4. Rewrite commentary sections into plain but serious English:
   - explain what the saying seems to mean;
   - explain why the project includes, marks, defers, or excludes it;
   - name the source situation without relying on clickable paths;
   - make uncertainty understandable to a non-specialist reader.
5. Preserve every `## Logion N` heading for N=1-114.
6. Preserve paper safety: no repository paths in the English paper-facing appendix.
7. Regenerate the English full book proof.
8. Run structural QA and paper-safety scans.
9. Create an execution report:
   - `project/english-appendix-editorial-quality-pass-v0.1.md`
10. Update README, project map, roadmap, remediation plan, and open-task queue.

## Acceptance Criteria

- English appendix still has exactly 114 logion sections.
- The most repeated generated phrases are reduced.
- Included and excluded logia are understandable to ordinary English readers.
- The English proof renders successfully.
- QA crosscheck passes.
- Paper-facing English output has no repository paths and no obsolete "appendix absent" language.
