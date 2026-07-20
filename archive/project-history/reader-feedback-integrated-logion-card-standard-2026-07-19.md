# Integrated Reader Feedback Standard For Logion Cards

Status: active remediation checklist, 2026-07-19. Stage 1 structural normalization has been applied to all 114 logia in the Ukrainian appendix; stages 2-5 remain active quality work.

## Why This Exists

Reader review showed that fixes were being applied locally, especially to Logion 1, while the same defects remained in later logia. This document consolidates the reader-facing requirements that must now be applied consistently to every logion in the Ukrainian paper appendix and, later, to the English book.

## Core Reader Requirement

Each logion section must first read like a book for an ordinary thoughtful reader, not like an internal textual-criticism database.

The reader must see the text before seeing the project machinery.

## Required Order For Every Logion

1. Coptic text.
2. Greek text.
3. Ukrainian translation.
4. English translation.
5. Human explanation and possible interpretations.
6. Plain-language reconstruction decision.
7. Short dating/probability conclusion when available.

## Source Text Rules

- The Coptic text must be printed directly when available.
- The Greek text must be printed directly when an Oxyrhynchus witness exists.
- If no direct Greek Thomas witness exists, use a responsible Greek reconstruction only if the project already has one.
- If the Greek is reconstructed, say briefly and plainly that no direct Greek manuscript is preserved.
- Do not use raw file paths in the paper book.
- Do not hide rejected logia. Rejected, deferred, uncertain, and appendix-only logia must still have full reader-facing sections.

## Translation Rules

- The Ukrainian translation section must contain the full preserved logion as far as the project has it, not merely the reconstructed core.
- The Ukrainian translation section must not include commentary, status notes, warnings, or explanations.
- If only an ancient core is included in the reconstruction, explain that later under the reconstruction-decision section.
- The English translation section follows the same principle.

## Clean Text And Greek Reader Rules

- The first layer of the Ukrainian book is the numbered Ukrainian reconstruction.
- Immediately after the Ukrainian reconstruction, the book must print a clean reconstructed Greek text.
- This clean Greek text must have no logion numbers, no brackets, no apparatus, no papyrus labels, no notes, and no disclaimers.
- The detailed Greek apparatus remains separate in the scholarly layer.

## Forbidden Reader-Facing Noise

Do not place these before the reader has seen the logion text:

- `Status`
- `Decision`
- `Reader status`
- `Greek status`
- `INCLUDE_WITH_MARKER`
- `UNCERTAIN`
- `DEFER`
- `APPENDIX_ONLY`
- `clean reader`
- `clean reconstruction status`
- `shorter reader form`
- internal repository paths
- card links

## Wording Rules

Use plain Ukrainian:

- "Український переклад"
- "Англійський переклад"
- "Як це можна зрозуміти"
- "Чому включено до реконструкції"
- "Чому не включено до реконструкції"
- "Чому використано лише давнє ядро"

Avoid opaque phrases such as:

- "Томине unity reading"
- "cluster-control"
- "reader-candidate"
- "appendix-only material"
- "Greek retroversion" without explanation
- "чистий/грязний текст" language in the logion card itself.

## What Must Be Fixed In The Current Project

1. Apply the Logion 1 reader-facing order to all 114 logia, not only Logion 1.
2. Move Coptic and Greek source text to the top of every logion section where available.
3. Make every `Український переклад` block clean: translation only.
4. Remove direct technical status blocks from the reader-facing paper appendix.
5. Move discussion of included core versus excluded material below the translation.
6. Replace student-note style interpretation with readable prose over multiple passes.
7. Keep all 114 logia in the appendix, including rejected and deferred logia.

## Multi-Stage Remediation Plan

### Stage 1: Structural Normalization

Apply the required section order to all 114 logia in the Ukrainian appendix. Pull Coptic, Greek, and Ukrainian translation blocks from `corpus/cards/logion-XXX.md` where available. Remove status tables, file paths, and technical labels from the top of the reader-facing section. Rebuild the Ukrainian book and run QA.

Current result: complete for all 114 logia as a structural pass. This does not mean every translation, English rendering, interpretation, or reconstructed Greek line is final.

### Stage 2: Translation Completeness Audit

Audit each logion to confirm that the Ukrainian translation is full, not merely a reconstructed core. Where only a summary exists, mark the logion for manual translation completion and do not pretend it is finished.

### Stage 3: Interpretation Rewrite

Rewrite the interpretation section for all 114 logia in a consistent reader-friendly style. Prioritize the weakest and most mechanical sections first.

### Stage 4: Source And Greek Audit

Verify that each Greek section clearly distinguishes direct papyrus text from reconstructed Greek, while keeping the clean Greek reader free of apparatus.

### Stage 5: Final Paper QA

Regenerate the Ukrainian PDF, inspect page images, and confirm that the order is:

Ukrainian reconstruction -> clean Greek reconstruction -> all-logia appendix.
