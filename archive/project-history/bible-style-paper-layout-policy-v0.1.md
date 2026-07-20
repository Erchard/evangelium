# Bible-Style Paper Layout Policy v0.1

Date: 2026-07-19

## Purpose

The first technical PDF proof confirmed that rendering works, but it looked like a raw Markdown export rather than a book. The user explicitly prefers a visual language closer to mass Bible editions because that is the format most readers intuitively associate with sacred or scriptural text.

This policy records that direction for the Ukrainian and English paper books.

## Reader-Facing Principle

The clean reconstructed text should feel like a familiar printed scripture page:

- compact;
- calm;
- typographically conservative;
- easy to scan by numbered units;
- not visually academic on the first pages;
- free from apparatus marks, brackets, repository paths, hyperlinks, and technical metadata.

## Clean Text Layout

For paper books:

- use a serif typeface where available;
- use compact two-column layout for the clean reconstructed text;
- place logion numbers inline at the beginning of each unit, not as oversized headings;
- preserve conventional Gospel of Thomas numbering;
- keep the first reader-facing text free of commentary and disclaimers;
- keep headers/footers minimal.

## Apparatus Layout

The appendix and scholarly apparatus may be denser, but should not look like raw spreadsheets.

Preferred treatment:

- split large 114-logion tables into print-friendly indexes;
- use short status phrases rather than long machine-status strings where possible;
- keep full technical detail in the digital companion;
- use paper-safe labels: `NHC II,2`, `P.Oxy. 1`, `P.Oxy. 654`, `P.Oxy. 655`, `SBLGNT`, short bibliography keys.

## Digital Companion Exception

The digital companion may and should preserve:

- repository paths;
- source paths;
- URLs;
- full audit trail;
- detailed status strings;
- machine-readable tables.

## First Implementation

`tools/render_first_proofs.py` now renders paper PDFs with a first Bible-style proof mode:

- title page;
- simple contents page;
- compact two-column clean text;
- Times New Roman when available;
- compact reference table;
- no repository paths or URLs in paper PDF extracted text.

This is not final book design. It is the first proof direction.
