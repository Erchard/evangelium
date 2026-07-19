# Obsolete Output Pipeline

This archive keeps the first proof renderer for audit history only.

`render_first_proofs.py` targeted the early short proof files:

- `output/uk-paper-book/book-source-uk.md`
- `output/en-paper-book/book-source-en.md`
- `output/*/euagelia-*-proof.*`

Those generated artifacts were removed on 2026-07-19 because the active publication outputs are now the full proof sources and PDFs:

- `output/uk-paper-book/book-source-uk-full.md`
- `output/uk-paper-book/euagelia-uk-full-proof.pdf`
- `output/en-paper-book/book-source-en-full.md`
- `output/en-paper-book/euagelia-en-full-proof.pdf`
- `output/digital-scholarly-companion/companion-source-full.md`
- `output/digital-scholarly-companion/euagelia-digital-companion-full-proof.pdf`

Use `tools/render_full_book_proofs.py` for current proof generation.
