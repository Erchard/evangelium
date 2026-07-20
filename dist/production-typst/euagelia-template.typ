// EUAGELIA Typst production template pilot v0.1
// This template is intentionally conservative: book-like serif typography,
// clear hierarchy, clean text first, and print-safe apparatus.

#let euagelia_setup(lang: "en") = {
  set page(
    paper: "a5",
    margin: (inside: 18mm, outside: 14mm, top: 16mm, bottom: 18mm),
    numbering: "1",
  )
  set text(font: "Libertinus Serif", size: 11pt, lang: lang)
  set par(justify: true, leading: 0.57em)
  show heading.where(level: 1): it => {
    pagebreak(weak: true)
    set align(center)
    text(size: 17pt, weight: "regular", it.body)
  }
  show heading.where(level: 2): it => {
    block(above: 12pt, below: 7pt)[
      #text(size: 14pt, weight: "semibold", it.body)
    ]
  }
  show heading.where(level: 3): it => {
    block(above: 8pt, below: 4pt)[
      #text(size: 12pt, weight: "semibold", it.body)
    ]
  }
}

#let source_key_note = [
  EUAGELIA paper books must remain print-safe. Internal repository paths belong
  to the digital scholarly companion, not to the printed reader.
]
