# IDE Codex Master Prompt: EUAGELIA Final 100% Execution Pass

You are Codex working in `/Users/arseny/BOOKS/EUAGELIA`.

This prompt supersedes narrow one-off prompts for the remaining publication work. Its purpose is to move EUAGELIA from a proof-complete scholarly package to a final, reader-ready, print-ready, and digitally auditable publication package.

## 1. Final Goal

Finish EUAGELIA as a reconstruction of the earliest reachable layer of a sayings gospel tradition associated with the Gospel of Thomas.

The project must not become a normal full translation of the Gospel of Thomas. It must present:

- a clean Ukrainian reconstructed reader text;
- a clean English reconstructed reader text;
- a clean reconstructed Greek text layer;
- Coptic and Greek source layers in the appendix;
- commentary for all 114 logia, including rejected logia;
- an English scholarly evidence dossier;
- print-ready Ukrainian and English books;
- a richer digital scholarly companion.

The reader-facing books must feel like real books, not internal research dumps.

## 2. Non-Negotiable Reader Principles

For the Ukrainian and English paper books:

- Begin with the clean reconstructed text, not with disclaimers, statuses, or methodology.
- The clean Ukrainian text uses the standard Thomas logion numbers for reference.
- The clean Greek reconstructed text appears after the Ukrainian clean text and before the commentary appendix.
- The clean Greek reconstructed text must have no numbering, no brackets, no footnotes, no apparatus marks, and no disclaimers.
- The commentary appendix may discuss uncertainty, source status, rejected material, and reconstruction choices, but in plain human language.
- Every one of the 114 logia must appear in the appendix, whether included, partly included, deferred, uncertain, or rejected.

## 3. Reader-Facing Language Rules

The target reader is an ordinary thoughtful Christian reader. Do not mention that target audience inside the book.

Avoid academic or internal-project jargon in the paper books, especially:

- `clean reader`;
- `appendix-only`;
- `marker`;
- `with marker`;
- `status`;
- `profile`;
- `control`;
- `controlled`;
- `synoptic`;
- `synoptics`;
- `Thomasine` / `томине` unless it is explained simply;
- `retroversion` in Ukrainian paper-facing prose;
- repository paths;
- local working text notes;
- DCLP/XML implementation details;
- square-bracket technical explanations in reader-facing sections.

Use plain equivalents:

- "основний текст" only when necessary, otherwise "реконструкція";
- "додаток";
- "пояснене застереження";
- "паралель у Матвія, Марка або Луки";
- "канонічні Євангелія";
- "схожі місця";
- "підстави для датування";
- "грецьке свідчення";
- "коптська версія";
- "ймовірна грецька форма" when explaining reconstructed Greek in Ukrainian.

Do not write sentences such as "для звичайного церковного читача..." in the book. Use that only as an internal editorial standard.

## 4. Typography Rules

Current ReportLab PDFs are proof artifacts. The final production path should move toward Typst or XeLaTeX, unless there is a documented reason not to.

For all generated paper PDFs:

- Use a minimal serif font system.
- Avoid decorative fonts and mixed font clutter.
- Body text in logion cards must be at least 14 pt in ReportLab proofs or equivalent readable size in final production layout.
- Commentary subheadings may be bold.
- Do not use bold for logion numbers in the clean reconstructed text.
- Do not use bold for arbitrary emphasis inside normal paragraphs.
- Avoid overusing italics.
- Tables may be slightly smaller, but must remain readable.
- Greek and Coptic text must render without boxes, broken glyphs, or missing characters.
- Clean Ukrainian two-column text should be justified only if spacing remains humane; otherwise solve properly with hyphenation or revise the layout.
- Do not fake professional typography with brittle hacks.

## 5. Required Current Inputs

Before making changes, inspect the current state of:

- `README.md`
- `project/project-completion-plan-2026-07-19.md`
- `project/project-map.md`
- `project/repository-structure.md`
- `project/final-product-specification.md`
- `project/project-quality-audit-v0.1.md`
- `project/publication-gap-audit-v0.2.md`
- `output/uk-paper-book/book-source-uk-full.md`
- `output/en-paper-book/book-source-en-full.md`
- `output/digital-scholarly-companion/companion-source-full.md`
- `tools/assemble_full_book_sources.py`
- `tools/render_full_book_proofs.py`
- `tools/build_typst_production_pilot.py`
- `tools/qa_crosscheck.py`

Also inspect representative rendered pages from:

- `output/uk-paper-book/euagelia-uk-full-proof.pdf`
- `output/en-paper-book/euagelia-en-full-proof.pdf`
- `output/digital-scholarly-companion/euagelia-digital-companion-full-proof.pdf`

Use rendered PNG inspection for visual checks, not text extraction alone.

## 6. Execution Plan

Work in this order.

### Phase 1. Baseline Audit

Run:

```bash
python3 tools/qa_crosscheck.py
```

Then audit current paper-facing text for:

- technical jargon;
- accidental bold;
- unreadable font sizes;
- broken Greek/Coptic glyphs;
- duplicated headings;
- stale version/program-like labels;
- source-path leakage;
- inconsistent logion numbering;
- mismatch between inclusion decisions and probability/date assessments.

Save or update a concise audit file under `project/`.

### Phase 2. Reader-Facing Copyedit

Review the Ukrainian appendix for all 114 logia.

For every logion, enforce this reader-facing order:

1. Coptic text.
2. Greek text, or short explanation that no Greek witness is extant and the Greek is reconstructed from Coptic.
3. Ukrainian translation of the full received Coptic logion.
4. English translation where appropriate for bilingual/digital layers.
5. Explanation in plain language: what the saying may mean, possible interpretations, context, and why it matters.
6. Reconstruction decision in plain language.
7. Short conclusion: likely date range, confidence percentage, and why.

If the reconstruction includes only an early core, still provide the full received Coptic logion translation in the appendix, then clearly explain what is included and what is not.

Rejected logia must receive the same level of reader explanation as included logia. The reader must understand why a logion was rejected, not feel that it was silently discarded.

### Phase 3. Decision Coherence

Check every logion against the decision tables:

- A logion assessed as probably late must not appear in the main reconstructed text without a clear split-core justification.
- A logion assessed as probably early but excluded must have a clear reason: duplication, weak source status, composite form, dependence risk, or unresolved cluster issue.
- Logion 1 must receive special treatment because it affects the title, opening words, and whether the text begins with a prologue or with a saying of Jesus.
- Logion 2 must preserve the short seek/find core in the main text, while later expansion remains in the appendix unless a new decision pass proves otherwise.

Do not silently change clean-reader membership. If a membership change is needed, create a named decision note and update all synchronized layers.

### Phase 4. Greek And Coptic Fidelity

Audit the Greek and Coptic layers:

- Extant Greek from P.Oxy. must be distinguished from reconstructed Greek.
- Greek reconstructed from Coptic must be clearly marked in the appendix/digital companion, but the clean Greek reader must remain visually clean.
- The clean Greek reader must have no numbering, no brackets, no explanatory notes.
- If the ancient-style original-language opening/title is discussed, base it on the actual first words of the chosen clean Greek reconstruction.
- Coptic and Greek must render correctly in proof PDFs.

### Phase 5. Professional Typesetting Path

Decide and implement the next best production path:

- Prefer Typst for a maintainable automated book pipeline.
- Use XeLaTeX only if Typst cannot handle Greek/Coptic typography, hyphenation, or print layout requirements well enough.
- Keep ReportLab as proof-generation unless it can meet final book quality.

At minimum:

- update the Typst production pilot;
- document the final production choice;
- create a checklist for Ukrainian and English final book builds;
- verify sample pages visually.

### Phase 6. Paper And Digital Separation

Maintain two publication layers:

- Paper books: clean, readable, print-safe, no clickable-link dependency, minimal source keys.
- Digital companion: full scholarly apparatus, source registers, audit trail, internal tables, methodology, detailed evidence notes, links where useful.

Do not move source-rich scholarly material out of the digital companion just to make paper books shorter.
Do not leave digital-only navigation assumptions in the paper books.

### Phase 7. Documentation And Release Freeze

Update:

- `README.md`
- `project/project-completion-plan-2026-07-19.md`
- `project/project-map.md`
- `project/repository-structure.md`
- `project/final-product-specification.md`
- `project/open-task-prompt-queue-2026-07-18.md`
- relevant audit files under `project/`

Then regenerate:

```bash
python3 tools/assemble_full_book_sources.py
python3 tools/render_full_book_proofs.py
python3 tools/build_typst_production_pilot.py
python3 tools/qa_crosscheck.py
```

If any command requires the bundled Python runtime, use the existing project pattern:

```bash
/Users/arseny/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 ...
```

## 7. Quality Gates

Do not call the project 100% complete until all are true:

- QA passes.
- All 114 logia have complete appendix sections.
- Clean Ukrainian, English, Greek, Coptic, and parallel layers are synchronized.
- Paper books contain no internal project jargon or source-path leakage.
- Greek and Coptic render visually without broken glyphs.
- Subheadings are readable and lightly emphasized.
- Bold is not overused.
- The main reconstructed text contains no late material without explicit split-core justification.
- The evidence dossier explains the method, source hierarchy, uncertainty, and major decisions.
- Rights/source policy is clear: original EUAGELIA work is intended as commons/public-use material, while third-party sources retain their own rights.
- Final release manifest and checksums are regenerated after the final PDFs are frozen.

## 8. Expected Deliverables

Produce:

- updated paper-book sources;
- updated proof PDFs;
- updated Typst/professional production package;
- updated digital companion if needed;
- updated audit and completion-plan documents;
- a short final report explaining:
  - what was fixed;
  - what was verified;
  - what remains unfinished;
  - the next concrete step toward release.

## 9. Immediate Next Best Action

Start with the highest-risk reader-facing gap:

Audit the Ukrainian paper book appendix from Logion 1 through Logion 114 for ordinary-reader clarity, over-technical wording, accidental bold, font-size problems, and decision/date coherence. Fix safe wording and generation issues immediately. For any change that would alter scholarly reconstruction membership, create a separate decision note instead of silently changing the text.
