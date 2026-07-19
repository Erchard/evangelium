# Project Completion Plan, 2026-07-19

Status: active completion plan after Ukrainian reader-facing proof review.

## Current Assessment

The project is approximately **99% complete as a scholarly proof package** and approximately **96-97% complete as a final publishable book package**.

The difference is important. The corpus, reconstruction logic, appendix architecture, multilingual layers, digital companion, and proof PDFs exist. What remains is not discovery work, but final publication discipline: reader-facing copyedit, professional production layout, external source/citation review, final visual QA, and release freeze.

## What Is Already Done

- 114/114 logion cards exist.
- 114/114 Ukrainian appendix sections exist.
- 114/114 English appendix sections exist.
- The main reconstructed reader set is frozen at 36 logia or reconstructed cores.
- Ukrainian, English, Coptic, Greek, Greek majuscule, Arabic literary, and parallel reader layers are synchronized for the included set.
- Ukrainian paper book source and full proof exist.
- English paper book source and full proof exist.
- Digital scholarly companion source, PDF proof, TSV indexes, checksums, and browsable HTML companion exist.
- Reader-facing cleanup now blocks technical phrases such as `DCLP XML`, `INCLUDE_WITH_MARKER`, `UNCERTAIN`, `DEFER_TO_CLUSTER`, internal "marker" language, `clean reader`, and `appendix-only` from the Ukrainian and English paper-book PDFs.
- Obsolete first-proof generated artifacts were removed from `output/`; the active proof files are now the `*-full` sources and PDFs.
- The project has a commons/public-use policy and separates original project work from third-party source rights.

## Main Remaining Gaps

### 1. Final Reader-Facing Copyedit Signoff

This is now mostly a final human signoff task rather than a missing-content task.

The Ukrainian and English paper books are structurally complete and have passed automated anti-jargon checks. A human editor still needs to read them as books and catch:

- stiff wording;
- theological ambiguity caused by phrasing rather than by evidence;
- page-level reading rhythm;
- any remaining places where the commentary feels like a memo instead of an explanation.

### 2. Logion 1, Title, And First Words

The remaining editorial decision with the largest conceptual weight is whether Logion 1 remains only in the appendix as a collection prologue or returns to the main reconstructed text as the numbered opening.

This affects:

- the ancient-style title question;
- the first words of the reconstructed original-language text;
- whether the book begins with "Jesus said..." or with a prologue about hidden sayings written by Thomas;
- how strongly the edition separates earliest sayings from later collection framing.

### 3. Production Typesetting

The current PDFs are proof artifacts. They are useful for review, but not the final print design.

The project still needs:

- a full Typst or professional-layout build for the complete Ukrainian book;
- a full Typst or professional-layout build for the complete English book;
- page-level visual QA after production compilation;
- final check of column flow, font size, justification, Greek/Coptic rendering, headings, page breaks, and bibliography/index pages.

### 4. Greek And Coptic Visual Fidelity

The Greek and Coptic layers exist, but final publication needs one last visual pass:

- no broken Greek glyphs;
- no missing Coptic combining marks where a readable alternative exists;
- no accidental bracketed apparatus in the clean Greek section;
- clear distinction between extant Greek witnesses and reconstructed Greek forms in the appendix/digital apparatus.

### 5. Source And Rights Freeze

The project has a rights policy and source keys, but final publication still needs:

- final public-source redistribution review;
- confirmation that protected modern editions are citation/control-only;
- final source snapshot list;
- final checksums after production PDFs are frozen.

### 6. Release Freeze

The final release needs:

- final version/date label suitable for a book;
- release manifest;
- frozen checksums;
- tag or release marker in git;
- short publication note explaining what is final and what remains open for future scholarly revision.

## Execution Order To Reach 100%

1. **Logion 1 / title / opening-words decision**
   Decide whether the reconstructed text begins with the Logion 1 prologue or with the first included Jesus saying. This must be settled before final typesetting.

2. **Production layout build**
   Compile or hand off complete Ukrainian and English books through the Typst/professional production path.

3. **Greek/Coptic rendering audit**
   Render representative pages from the clean Greek section and appendix source sections. Fix glyph, font, spacing, and line-breaking issues.

4. **Human copyedit signoff**
   A human reader must approve Ukrainian and English prose, especially theological phrasing, clarity of inclusion/exclusion explanations, and awkward machine-generated language.

5. **Final QA and freeze**
   Run structural QA, visual QA, source-rights review, checksum generation, manifest update, and release tagging.

## Next Action

Run the **Logion 1 / title / opening-words decision pass** next. The rest of the project can be polished technically, but this decision defines what the reconstructed book actually is when the reader opens page one.
