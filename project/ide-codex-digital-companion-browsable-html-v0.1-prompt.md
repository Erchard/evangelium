# IDE Codex Prompt: Browsable Digital Companion HTML v0.1

You are Codex working in `/Users/arseny/BOOKS/EUAGELIA`.

## Goal

Turn the expanded digital scholarly companion into a usable browsable HTML/static-site proof. The Markdown/PDF companion now preserves the apparatus, but the all-114 table is too dense for comfortable research. The next step is a digital workbench where a reader can quickly move from a logion to its card, evidence note, control files, source witnesses, decision status, and paper-book reference.

## Inputs

Use the deterministic outputs from the companion expansion pass:

- `output/digital-scholarly-companion/companion-source-full.md`
- `output/digital-scholarly-companion/logion-cross-reference-index.tsv`
- `output/digital-scholarly-companion/source-witness-inventory.tsv`
- `output/digital-scholarly-companion/artifact-checksums.tsv`
- `output/digital-scholarly-companion/audit-trail-index.tsv`
- `tools/generate_digital_companion.py`

Also use these project controls:

- `project/print-and-digital-publication-architecture.md`
- `project/rights-and-citation-policy.md`
- `project/source-reproducibility-note.md`
- `project/digital-scholarly-companion-expansion-v0.1.md`

## Tasks

1. Run baseline QA:

   ```bash
   python3 tools/qa_crosscheck.py
   ```

2. Design a static HTML companion under `output/digital-scholarly-companion/html/` with:

   - overview page;
   - filterable/searchable all-114 logion index;
   - per-logion detail panels or pages;
   - links to cards, evidence notes, control files, and source inventory rows;
   - separate sections for source witnesses, audit trail, bibliography/rights, and reproducibility;
   - clear labels distinguishing manuscript witnesses from hypothetical Greek retroversions and canonical controls.

3. Implement deterministic generation, preferably with a script such as `tools/render_digital_companion_html.py`. Do not hand-maintain a large HTML table if it can be generated from TSV.

4. Keep the result local/static and repository-friendly. Do not require a server unless absolutely necessary.

5. Verify:

   - 114 logion entries appear in the HTML;
   - filters/search work if JavaScript is used;
   - all internal links are either valid local paths or deliberately marked external/public/protected;
   - no paper-book output is changed;
   - `python3 tools/qa_crosscheck.py` still passes.

6. Update:

   - `output/digital-scholarly-companion/README.md`
   - `project/project-completion-roadmap.md`
   - `project/open-task-prompt-queue-2026-07-18.md`
   - `project/project-map.md`
   - `project/repository-structure.md`

7. Save a QA report, for example:

   - `project/digital-companion-browsable-html-v0.1.md`

## Quality Rules

- Do not alter clean-reader membership.
- Do not remove uncertainty markers.
- Keep manuscript witnesses, canonical controls, translations, and hypothetical retroversions conceptually separate.
- Make the interface helpful for a serious reader, not decorative.
- Preserve the commons/anti-ownership policy and third-party rights distinctions.

## Expected Output

- Static HTML companion proof.
- Deterministic HTML generation script.
- QA report and updated documentation.
- Next-step recommendation after the HTML companion is usable.
