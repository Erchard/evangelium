# Final Production Typesetting And Copyedit Gate v0.1

Status: completed as production-gate decision, 2026-07-19.

## Scope

This pass executed `project/ide-codex-final-production-typesetting-copyedit-gate-v0.1-prompt.md`.

The task was not to change the reconstruction, clean-reader membership, or logion decisions. It was to decide the final production path, inspect the current outputs, fix safe documentation/proof-gate defects, and define the remaining release-candidate blockers.

## Baseline QA

Command:

```bash
python3 tools/qa_crosscheck.py
```

Result:

- card files: 114/114;
- appendix sections: 114/114;
- appendix source/control sections: 114/114;
- reader sets: 37/37 synchronized;
- clean-text anchors: present for all clean-reader logia.

## Output Inspection

| Output | Current state | Gate result |
| --- | --- | --- |
| `output/uk-paper-book/euagelia-uk-full-proof.pdf` | 118 pages | Paper proof exists; repo-path leakage scan = 0; Logion 114 present. |
| `output/en-paper-book/euagelia-en-full-proof.pdf` | 177 pages | Paper proof exists; repo-path leakage scan = 0; Logion 114 present. |
| `output/digital-scholarly-companion/euagelia-digital-companion-full-proof.pdf` | 16 pages | Digital proof exists; repo paths present by design; Logion 114 present. |
| `output/digital-scholarly-companion/html/index.html` | Static HTML companion | 114 logion panels; 1006 hrefs; 762 valid local file links; 0 missing local links. |

## Tool Availability

Local production tools checked:

- `typst`: not installed;
- `xelatex`: not installed;
- `pdflatex`: not installed.

Therefore the current environment can regenerate ReportLab proofs, but cannot yet compile a final Typst or LaTeX production edition.

## Production Path Decision

Decision: **ReportLab remains the proof renderer; final publication should move to a Typst production pipeline or a professional handoff generated from Typst-ready sources.**

Rationale:

- ReportLab is already useful for deterministic proof PDFs, page counts, text extraction, and visual QA.
- ReportLab output is not ideal as the final book typography layer: it is script-controlled, serviceable, and stable, but not as maintainable for nuanced book design, running heads, typography, final indexes, and print-ready refinements.
- LaTeX is strong for books but heavier for this multilingual project and not available in the current environment.
- Typst is a better final target for this project: easier source generation from Markdown/TSV, strong typography, good multilingual support potential, and more maintainable templates than direct ReportLab layout code.

Release rule: **do not call the current PDFs final production files.** They are strong full proofs. Release-candidate status requires either:

1. a compiled Typst production pilot that matches the paper-book requirements; or
2. an explicit professional typesetting handoff package with source, checklist, and acceptance criteria.

## Copyedit / Proof Checklist

### Ukrainian Paper Book

- Verify clean-reader first-page experience: clean numbered logia only.
- Read all 37 clean-reader units aloud for Ukrainian rhythm and consistency.
- Check Ukrainian terminology: `логія`, `реконструкція`, `додаток`, `свідок`, `джерело`, `ймовірність`, `включено`, `виключено`.
- Check that appendix comments remain reader-friendly and do not slide back into private working notes.
- Check Logion 114 exclusion wording for clarity and tone.
- Check bibliography/source-key page for print-safe usefulness.

### English Paper Book

- Verify clean-reader first-page experience and conventional Thomas numbering.
- Read all 37 clean-reader units for English literary consistency.
- Check that `What This Saying Is About` sections sound like public prose, not generated scaffolding.
- Check repeated phrases in deferred/uncertain logia; repetition is acceptable structurally but should not feel mechanical in the final book.
- Check evidence dossier tone: scholarly, cautious, and not overclaiming.
- Check bibliography/source-key page for print-safe usefulness.

### Digital Companion

- Verify 114 logion panels in HTML.
- Verify all file links are local and valid.
- Check that manuscript witnesses, canonical controls, translations, and hypothetical retroversions are visually and conceptually distinct.
- Check rights/source snapshot notes before public redistribution.
- Preserve machine-readable TSVs and checksums.

### Cross-Product Consistency

- Confirm the same 37 reader units across Ukrainian, English, Coptic, Greek, Arabic literary, and parallel layers.
- Confirm Logion 1 remains handled as frame/prologue in interpretation, without breaking source-layer synchronization.
- Confirm excluded/deferred/appendix-only logia still appear in the appendix and digital companion.
- Confirm paper books do not contain internal repo paths.
- Confirm digital companion intentionally preserves repo paths.

## Safe Fixes Performed

Updated stale documentation that still described the English output as incomplete and the digital companion as a small source-map proof. The active docs now reflect:

- Ukrainian full proof: 118 pages;
- English full proof: 177 pages with full 114-logion appendix;
- digital companion PDF proof: 16 pages;
- browsable HTML companion exists.

Files updated:

- `README.md`
- `project/publication-remediation-plan-2026-07-18.md`
- `project/project-map.md`
- `project/full-book-assembly-typesetting-pipeline-v0.1.md`

## Release-Candidate Blockers

The project is not yet a release candidate because:

1. final production typesetting has not been compiled in Typst/LaTeX/professional layout;
2. final human copyedit of Ukrainian and English books has not been completed;
3. final public-source redistribution review for downloadable snapshots has not been completed;
4. final release manifest/checksums should be generated after production typography and copyedit are frozen.

## Next Recommended Step

Build a Typst production pilot from the current generated Markdown/TSV sources. The pilot should compile at least the Ukrainian clean reader plus a representative appendix section, then the English equivalent. If Typst cannot be installed or used, prepare a professional handoff package instead.
