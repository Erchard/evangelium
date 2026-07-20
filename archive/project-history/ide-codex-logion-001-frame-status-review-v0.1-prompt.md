# IDE Codex Prompt: Logion 1 Frame-Status Review v0.1

## Task

Perform the pre-freeze editorial review for Logion 1 before finalizing the clean reader.

The project is reconstructing the earliest recoverable sayings gospel, not simply translating the Gospel of Thomas. Logion 1 is currently printed in the clean reader, but the probability-pressure audit flags it as a likely collection frame rather than an independently secure early Jesus saying. Resolve this editorial status clearly and document the decision.

## Required Inputs

Read and cross-check:

- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-uk.md`
- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-en.md`
- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-coptic.md`
- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-greek.md`
- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-uk-apparatus.md`
- `reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-uk.md`
- `reconstruction/earliest-sayings-gospel/notes/logion-001-evidence-en.md`
- `reconstruction/earliest-sayings-gospel/inclusion-decisions-table.md`
- `reconstruction/earliest-sayings-gospel/final-reader-probability-pressure-review-v0.1.md`
- `project/probability-vs-reader-decision-audit-2026-07-18.md`

## Editorial Requirements

1. Decide whether Logion 1 should remain in the clean reader, move to a prefatory frame, or remain only in apparatus.
2. Do not silently treat Logion 1 as an ordinary reconstructed saying.
3. Preserve the clean-reader first-page rule: the public clean text should contain only numbered logia without technical comments, brackets, or disclaimers.
4. Preserve synchronization across Ukrainian, English, Coptic, Greek, Arabic, and parallel layers unless a deliberate generation/freeze pass updates all layers together.
5. If the decision affects the final print model, document the print implication separately from the current source-layer reader file.
6. Keep repository paths in the scholarly/digital apparatus; reader-facing print prose must use logion numbers, witness labels, and plain explanations.

## Required Outputs

Create:

- `reconstruction/earliest-sayings-gospel/logion-001-frame-status-review-v0.1.md`

Update, if needed:

- `reconstruction/earliest-sayings-gospel/notes/logion-001-evidence-en.md`
- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-uk-apparatus.md`
- `reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-uk.md`
- `reconstruction/earliest-sayings-gospel/README.md`
- `project/project-completion-roadmap.md`
- `project/project-map.md`
- `README.md`

## Acceptance Criteria

- Logion 1 has a clear final editorial recommendation.
- The recommendation distinguishes current source-layer synchronization from final print presentation.
- The clean reader is not expanded or reduced accidentally.
- The apparatus states that Logion 1 is a collection frame, not an independently secure earliest saying.
- The full appendix gives an ordinary reader a clear explanation of why Logion 1 is useful but marked.
- Project navigation documents point to the new review.
- Run:

```bash
python3 tools/probability_reader_audit.py
python3 tools/qa_crosscheck.py
git diff --check
```

Do not mark the project publication-ready merely because this review is complete. The next content-level work remains split-core probability-pressure review and cluster-control work; the next editorial work remains full appendix consolidation for Logia 61-70.
