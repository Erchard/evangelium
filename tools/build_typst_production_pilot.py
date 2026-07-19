#!/usr/bin/env python3
"""Build a Typst-ready production pilot / handoff package.

Typst may not be installed in the current environment. This script therefore
creates deterministic sources and a handoff package that can be compiled by a
local Typst installation or passed to a professional typesetter.
"""

from __future__ import annotations

import hashlib
import re
import shutil
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output/production-typst"
UK_SOURCE = ROOT / "output/uk-paper-book/book-source-uk-full.md"
EN_SOURCE = ROOT / "output/en-paper-book/book-source-en-full.md"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def typst_available() -> bool:
    return shutil.which("typst") is not None


def typst_escape(text: str) -> str:
    replacements = {
        "\\": "\\\\",
        "[": "\\[",
        "]": "\\]",
        "{": "\\{",
        "}": "\\}",
        "$": "\\$",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def typst_heading(level: int, text: str) -> str:
    text = typst_escape(text.strip())
    if level <= 1:
        return f"= {text}"
    if level == 2:
        return f"== {text}"
    return f"=== {text}"


def md_to_typst(md: str) -> str:
    lines: list[str] = []
    in_code = False
    for raw in md.strip().splitlines():
        line = raw.rstrip()
        if line.startswith("```"):
            in_code = not in_code
            lines.append("```")
            continue
        if in_code:
            lines.append(line)
            continue
        if not line.strip():
            lines.append("")
            continue
        if line.startswith("# "):
            lines.append(typst_heading(1, line[2:]))
        elif line.startswith("## "):
            lines.append(typst_heading(2, line[3:]))
        elif line.startswith("### "):
            lines.append(typst_heading(3, line[4:]))
        elif line.startswith("- "):
            lines.append("- " + typst_escape(line[2:]))
        elif re.match(r"^\d+\.\s+", line):
            lines.append(typst_escape(line))
        elif line.startswith("|"):
            # Keep tables as monospaced proof text in the pilot.
            lines.append("#block(inset: 4pt, fill: rgb(\"f7f7f7\"), text(size: 7pt, `" + typst_escape(line) + "`))")
        else:
            lines.append(typst_escape(line))
    return "\n".join(lines).strip() + "\n"


def section_between(text: str, start: str, stop_candidates: list[str]) -> str:
    if start not in text:
        raise SystemExit(f"Missing section start: {start}")
    after = text.split(start, 1)[1]
    stop_positions = [after.find(stop) for stop in stop_candidates if stop in after]
    stop_positions = [pos for pos in stop_positions if pos >= 0]
    if stop_positions:
        after = after[: min(stop_positions)]
    return start + "\n" + after.strip() + "\n"


def clean_section(text: str, lang: str) -> str:
    if lang == "uk":
        return section_between(text, "## Логії Ісуса", ["## Реконструйований грецький текст", "## Як читати це видання"])
    return section_between(text, "## Clean Reconstructed Text", ["## How To Read This Edition"])


def logion_section(text: str, heading: str) -> str:
    if heading not in text:
        raise SystemExit(f"Missing heading: {heading}")
    start = text.index(heading)
    rest = text[start:]
    match = re.search(r"\n## (?!#)", rest[len(heading) :])
    if match:
        rest = rest[: len(heading) + match.start()]
    return rest.strip() + "\n"


def bibliography_section(text: str, heading: str) -> str:
    if heading not in text:
        raise SystemExit(f"Missing bibliography heading: {heading}")
    return text[text.index(heading) :].strip() + "\n"


def sample_markdown(path: Path, lang: str) -> str:
    text = path.read_text(encoding="utf-8")
    if lang == "uk":
        parts = [
            "# Реконструкція найдавнішого Євангелія висловів",
            "## Production Pilot Scope",
            "Цей файл є Typst-ready production pilot, а не повною фінальною версією. Він перевіряє дизайн: титул, чистий текст, одну включену логію, одну виключену логію і бібліографічний зразок.",
            clean_section(text, "uk"),
            logion_section(text, "## Логія 2"),
            logion_section(text, "## Логія 114"),
            bibliography_section(text, "## Бібліографія і права"),
        ]
    else:
        parts = [
            "# A Reconstruction of the Earliest Sayings Gospel",
            "## Production Pilot Scope",
            "This file is a Typst-ready production pilot, not the full final edition. It tests the design path: title, clean text, one included logion, one excluded logion, and a bibliography sample.",
            clean_section(text, "en"),
            logion_section(text, "## Logion 2"),
            logion_section(text, "## Logion 114"),
            bibliography_section(text, "## Bibliography And Rights"),
        ]
    return "\n\n".join(part.strip() for part in parts) + "\n"


def template_text() -> str:
    return r'''// EUAGELIA Typst production template pilot v0.1
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
'''


def wrap_typst(body: str, lang: str) -> str:
    return f'''#import "euagelia-template.typ": euagelia_setup, source_key_note

#euagelia_setup(lang: "{lang}")

{body}

#pagebreak()
= Production Note

#source_key_note
'''


def write_readme(compiled: bool) -> None:
    status = "compiled pilot available" if compiled else "Typst-ready handoff; Typst not installed in this environment"
    text = f"""# EUAGELIA Typst Production Pilot

Status: {status}, 2026-07-19.

## Contents

- `euagelia-template.typ` - conservative book template pilot.
- `uk-pilot.typ` - Ukrainian pilot source.
- `en-pilot.typ` - English pilot source.
- `uk-pilot-source.md` - Markdown source excerpt used for the Ukrainian pilot.
- `en-pilot-source.md` - Markdown source excerpt used for the English pilot.
- `production-handoff-checklist.md` - checklist for Typst or professional typesetting.
- `production-pilot-manifest.tsv` - file sizes and checksums.

## Compile Commands

Install Typst, then run:

```bash
typst compile output/production-typst/uk-pilot.typ output/production-typst/uk-pilot.pdf
typst compile output/production-typst/en-pilot.typ output/production-typst/en-pilot.pdf
```

## Production Rule

ReportLab PDFs in `output/uk-paper-book/`, `output/en-paper-book/`, and `output/digital-scholarly-companion/` remain proof artifacts. Final release-candidate PDFs should come from this Typst/professional production path or from an explicitly approved equivalent.
"""
    (OUT / "README.md").write_text(text, encoding="utf-8")


def write_handoff_checklist() -> None:
    text = """# Production Handoff Checklist

Status: Typst/professional handoff checklist v0.1, 2026-07-19.

## Required Design

- Clean reconstructed text appears before commentary.
- Logion numbers follow conventional Gospel of Thomas numbering.
- Commentary is visually separate from the reconstructed text.
- Paper books contain no internal repository paths.
- Source keys are print-safe: NHC II,2; P.Oxy. 1; P.Oxy. 654; P.Oxy. 655; SBLGNT; protected editions as citation/control only.
- Digital companion remains the source-rich layer for repository paths and machine-checkable apparatus.

## Pilot Sections Included

- Title/front matter.
- Full clean reader.
- Logion 2 as included/marked sample.
- Logion 114 as excluded secondary-material sample.
- Bibliography/source-key sample.

## Acceptance Criteria For Final Production PDFs

- No clipped text, broken glyphs, black squares, or overlapping elements.
- Stable page numbers, headers, margins, section breaks, and bibliography.
- Ukrainian and English books use corresponding structure.
- Final copyedit checklist is complete.
- Final paper PDFs have zero repo-path leakage.
- Final release manifest and checksums are generated after copyedit freeze.
"""
    (OUT / "production-handoff-checklist.md").write_text(text, encoding="utf-8")


def write_manifest(paths: list[Path]) -> None:
    lines = ["artifact\tbytes\tsha256"]
    for path in paths:
        if path.exists():
            lines.append(f"{rel(path)}\t{path.stat().st_size}\t{sha256(path)}")
    (OUT / "production-pilot-manifest.tsv").write_text("\n".join(lines) + "\n", encoding="utf-8")


def maybe_compile() -> list[Path]:
    if not typst_available():
        return []
    outputs = []
    for stem in ["uk-pilot", "en-pilot"]:
        src = OUT / f"{stem}.typ"
        pdf = OUT / f"{stem}.pdf"
        subprocess.run(["typst", "compile", str(src), str(pdf)], check=True)
        outputs.append(pdf)
    return outputs


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    uk_md = sample_markdown(UK_SOURCE, "uk")
    en_md = sample_markdown(EN_SOURCE, "en")
    (OUT / "uk-pilot-source.md").write_text(uk_md, encoding="utf-8")
    (OUT / "en-pilot-source.md").write_text(en_md, encoding="utf-8")
    (OUT / "euagelia-template.typ").write_text(template_text(), encoding="utf-8")
    (OUT / "uk-pilot.typ").write_text(wrap_typst(md_to_typst(uk_md), "uk"), encoding="utf-8")
    (OUT / "en-pilot.typ").write_text(wrap_typst(md_to_typst(en_md), "en"), encoding="utf-8")
    write_handoff_checklist()
    compiled = maybe_compile()
    write_readme(bool(compiled))
    manifest_paths = [
        OUT / "README.md",
        OUT / "euagelia-template.typ",
        OUT / "uk-pilot-source.md",
        OUT / "en-pilot-source.md",
        OUT / "uk-pilot.typ",
        OUT / "en-pilot.typ",
        OUT / "production-handoff-checklist.md",
        *compiled,
    ]
    write_manifest(manifest_paths)
    for path in [*manifest_paths, OUT / "production-pilot-manifest.tsv"]:
        if path.exists():
            print(rel(path))


if __name__ == "__main__":
    main()
