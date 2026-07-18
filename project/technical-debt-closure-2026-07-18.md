# Technical Debt Closure

Date: 2026-07-18

## Scope

This pass closed the current technical debts identified in project documentation after the Logion 63 crosscheck.

It did not change the clean reconstruction corpus, the 34 reader units, or any inclusion/exclusion decision.

## Closed Items

### 1. Reusable QA Crosscheck Script

Status: closed.

New script:

- `tools/qa_crosscheck.py`

The script verifies:

- 114 card files;
- card filename / heading agreement;
- 114 appendix logion sections in order;
- 114 appendix source/control sections;
- 114 appendix status sections;
- clean-reader number sets across Ukrainian, English, Greek, Coptic, Arabic literary register, Ukrainian apparatus, and parallel edition;
- workflow `Reader text = YES` agreement with clean reader;
- all-114 `READER_INCLUDE_MARKED` agreement with clean reader;
- clean-text anchors in appendix for all 34 clean-reader logia/cores;
- appendix status agreement for included and non-included logia.

Current verification result:

```text
QA crosscheck OK
- card files: 114/114
- appendix sections: 114/114
- appendix source/control sections: 114/114
- reader sets: 34/34 synchronized across language layers and control tables
- clean-text anchors: present for all clean-reader logia
```

Run:

```bash
python3 tools/qa_crosscheck.py
```

### 2. Exact Clean-Text Anchors In Appendix

Status: closed for current clean-reader units.

All 34 current clean-reader logia/cores now have a `Чистий текст реконструкції` anchor in:

- `reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-uk.md`

This gives the print appendix an exact local bridge back to the clean Ukrainian reader and prevents drift between the reader layer and commentary layer.

### 3. Reader Heading Format Handling

Status: closed by documented tooling support.

The project intentionally allows different source heading labels by language:

- Ukrainian clean reader: `## N`
- English / Greek / Coptic: `## Logion N`
- Arabic literary register: `## قول N`
- Ukrainian apparatus: `## Логія N`

The QA script parses each format explicitly. Final print generation may still display only the number for reader-facing cleanliness.

### 4. Logion 63 Status Drift

Status: closed.

The previous P0 drift is resolved:

- Logion 63 appendix status now matches clean reader and control tables.
- Logion 63 evidence note and Luke control file are now post-promotion v0.2.
- QA confirms the reader set remains synchronized.

## Remaining Non-Technical Work

The major remaining work is editorial/research work, not basic technical consistency:

- continue full appendix editorial consolidation from Logia 81-90;
- complete wealth/renunciation cluster-control;
- write publication-level Logion 114 exclusion rationale;
- prepare the evidence dossier for publication;
- build final Ukrainian and English print outputs and digital scholarly companion.
