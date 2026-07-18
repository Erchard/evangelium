# IDE Codex Prompt: Controlled Reader-Candidate Pass for 46A and 91A v0.1

## Task

Execute a controlled clean-reader candidate pass for the two candidates promoted by Review C:

- Logion 46A: John / least-in-kingdom core.
- Logion 91A: recognition-of-time core.

The task is to decide whether these cores should enter the clean reconstructed reader. Do not include the full Thomas forms.

## Context

The project reconstructs the earliest recoverable sayings gospel, not the full Gospel of Thomas. The clean reader must remain selective, numbered according to the Gospel of Thomas, and free of technical comments on the first reader pages.

Review C promoted 46A and 91A to this pass because both have strong external controls and plausible early cores. It did not authorize automatic inclusion.

## Required Inputs

Read and cross-check:

- `reconstruction/earliest-sayings-gospel/split-core-high-early-pressure-review-c-v0.1.md`
- `reconstruction/earliest-sayings-gospel/notes/logion-046-evidence-en.md`
- `reconstruction/earliest-sayings-gospel/notes/logion-091-evidence-en.md`
- `controls/synoptic-parallels/logion-046-john-least-kingdom-controls.md`
- `controls/synoptic-parallels/logion-091-recognition-time-controls.md`
- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-uk.md`
- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-en.md`
- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-coptic.md`
- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-greek.md`
- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-ar-quranic-register.md`
- `reconstruction/earliest-sayings-gospel/parallel-edition.md`
- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-uk-apparatus.md`
- `reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-uk.md`
- `corpus/tables/logia-workflow-matrix.md`
- `reconstruction/earliest-sayings-gospel/all-114-publication-decision-table-v0.1.md`

## Method

For each candidate:

1. Test compactness.
2. Test whether the candidate is materially distinct from already included units.
3. Test whether the evidence is adequate for a marked reader inclusion.
4. Preserve Greek policy: no extant Greek Thomas witness means `Greek retroversion, hypothetical`.
5. Include only the split core if accepted.
6. If accepted, update all synchronized reader layers in the same pass.
7. If rejected, document why and leave all reader layers unchanged.

## Acceptance Criteria

- If 46A or 91A is accepted, the clean reader, English reader, Coptic layer, Greek layer, Arabic literary layer, parallel edition, Ukrainian apparatus, workflow matrix, all-114 table, and full appendix are synchronized.
- The clean reader remains clean: only numbered logia, no brackets, markers, or explanations.
- Full Logion 46 and full Logion 91 remain appendix-only.
- The appendix contains exact `Чистий текст реконструкції` anchors for any newly included core.
- `tools/qa_crosscheck.py` is updated only if the reader set intentionally changes.
- Run:

```bash
python3 tools/probability_reader_audit.py
python3 tools/qa_crosscheck.py
git diff --check
```

Do not mark the final reader frozen after this pass. This is still a controlled pre-freeze expansion.
