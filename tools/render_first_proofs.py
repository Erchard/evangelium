#!/usr/bin/env python3
"""Render first EUAGELIA proof artifacts from Markdown sources.

This is intentionally a small first-proof renderer, not a final book design
system. It creates HTML and PDF artifacts, keeps paper sources print-safe, and
records checksums so later proof passes can compare outputs.
"""

from __future__ import annotations

import argparse
import hashlib
import html
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    PageBreak,
    Paragraph,
    Preformatted,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
PYTHON_RUNTIME = "/Users/arseny/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3"
FONT_CANDIDATES = [
    Path("/System/Library/Fonts/Supplemental/Arial Unicode.ttf"),
    Path("/System/Library/Fonts/Supplemental/Times New Roman.ttf"),
    Path("/Library/Fonts/Arial Unicode.ttf"),
]


@dataclass(frozen=True)
class ProofJob:
    label: str
    title: str
    source: Path
    output_base: Path


JOBS = [
    ProofJob(
        label="uk",
        title="EUAGELIA Ukrainian Paper Book Proof",
        source=ROOT / "output/uk-paper-book/book-source-uk.md",
        output_base=ROOT / "output/uk-paper-book/euagelia-uk-proof",
    ),
    ProofJob(
        label="en",
        title="EUAGELIA English Paper Book Proof",
        source=ROOT / "output/en-paper-book/book-source-en.md",
        output_base=ROOT / "output/en-paper-book/euagelia-en-proof",
    ),
    ProofJob(
        label="digital",
        title="EUAGELIA Digital Scholarly Companion Proof",
        source=ROOT / "output/digital-scholarly-companion/companion-manifest.md",
        output_base=ROOT
        / "output/digital-scholarly-companion/euagelia-digital-companion-proof",
    ),
]


def find_font() -> Path:
    for candidate in FONT_CANDIDATES:
        if candidate.exists():
            return candidate
    raise SystemExit("No Unicode TTF font found for PDF proof rendering.")


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def parse_markdown_tables(lines: list[str]) -> list[object]:
    blocks: list[object] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("|") and i + 1 < len(lines) and re.match(r"^\|\s*:?-{3,}", lines[i + 1]):
            table_lines = [line, lines[i + 1]]
            i += 2
            while i < len(lines) and lines[i].startswith("|"):
                table_lines.append(lines[i])
                i += 1
            rows = []
            for table_line in table_lines:
                cells = [cell.strip() for cell in table_line.strip().strip("|").split("|")]
                if all(re.fullmatch(r":?-{3,}:?", cell or "") for cell in cells):
                    continue
                rows.append(cells)
            blocks.append(("table", rows))
            continue
        blocks.append(("line", line))
        i += 1
    return blocks


def markdown_to_html(text: str, title: str) -> str:
    lines = text.splitlines()
    body: list[str] = []
    in_list = False
    for block_type, value in parse_markdown_tables(lines):
        if block_type == "table":
            if in_list:
                body.append("</ul>")
                in_list = False
            rows = value
            body.append("<table>")
            for row_index, row in enumerate(rows):
                tag = "th" if row_index == 0 else "td"
                body.append("<tr>" + "".join(f"<{tag}>{inline_html(c)}</{tag}>" for c in row) + "</tr>")
            body.append("</table>")
            continue

        line = value
        if not line.strip():
            if in_list:
                body.append("</ul>")
                in_list = False
            continue
        if line.startswith("# "):
            close_list(body, in_list)
            in_list = False
            body.append(f"<h1>{inline_html(line[2:].strip())}</h1>")
        elif line.startswith("## "):
            close_list(body, in_list)
            in_list = False
            body.append(f"<h2>{inline_html(line[3:].strip())}</h2>")
        elif line.startswith("### "):
            close_list(body, in_list)
            in_list = False
            body.append(f"<h3>{inline_html(line[4:].strip())}</h3>")
        elif line.startswith("- "):
            if not in_list:
                body.append("<ul>")
                in_list = True
            body.append(f"<li>{inline_html(line[2:].strip())}</li>")
        else:
            if in_list:
                body.append("</ul>")
                in_list = False
            body.append(f"<p>{inline_html(line.strip())}</p>")
    if in_list:
        body.append("</ul>")

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{html.escape(title)}</title>
<style>
body {{ font-family: "Arial Unicode MS", "Times New Roman", serif; margin: 2.2rem auto; max-width: 980px; line-height: 1.45; color: #111; }}
h1 {{ text-align: center; font-size: 2rem; margin: 0 0 1.8rem; }}
h2 {{ font-size: 1.35rem; margin: 1.6rem 0 .7rem; border-bottom: 1px solid #bbb; padding-bottom: .25rem; }}
h3 {{ font-size: 1.05rem; margin: 1.1rem 0 .4rem; }}
p {{ margin: .45rem 0; }}
table {{ border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: .72rem; }}
th, td {{ border: 1px solid #bbb; padding: .25rem .3rem; vertical-align: top; }}
th {{ background: #f1f1f1; }}
code {{ font-family: ui-monospace, Menlo, Consolas, monospace; font-size: .92em; }}
@page {{ margin: 22mm 18mm; }}
</style>
</head>
<body>
{chr(10).join(body)}
</body>
</html>
"""


def close_list(body: list[str], in_list: bool) -> None:
    if in_list:
        body.append("</ul>")


def inline_html(value: str) -> str:
    escaped = html.escape(value)
    escaped = re.sub(r"`([^`]+)`", r"<code>\1</code>", escaped)
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", escaped)
    escaped = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", escaped)
    return escaped


def inline_pdf(value: str) -> str:
    escaped = html.escape(value)
    escaped = re.sub(r"`([^`]+)`", r"<font name='EUAGELIA'>\1</font>", escaped)
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", escaped)
    escaped = re.sub(r"\*([^*]+)\*", r"<i>\1</i>", escaped)
    return escaped


def build_pdf(source_text: str, output_pdf: Path, title: str, font_name: str) -> None:
    styles = getSampleStyleSheet()
    base = ParagraphStyle(
        "EUAGELIA",
        parent=styles["BodyText"],
        fontName=font_name,
        fontSize=10,
        leading=13,
        alignment=TA_LEFT,
        spaceAfter=5,
    )
    h1 = ParagraphStyle(
        "EUAGELIA-H1",
        parent=base,
        fontSize=18,
        leading=22,
        alignment=TA_CENTER,
        spaceBefore=8,
        spaceAfter=18,
    )
    h2 = ParagraphStyle(
        "EUAGELIA-H2",
        parent=base,
        fontSize=14,
        leading=17,
        spaceBefore=14,
        spaceAfter=8,
    )
    h3 = ParagraphStyle(
        "EUAGELIA-H3",
        parent=base,
        fontSize=12,
        leading=15,
        spaceBefore=10,
        spaceAfter=5,
    )
    small = ParagraphStyle("EUAGELIA-Small", parent=base, fontSize=6, leading=7)
    mono = ParagraphStyle("EUAGELIA-Mono", parent=base, fontName=font_name, fontSize=8, leading=10)

    provenance = (
        f"First proof generated from {rel(output_pdf.with_suffix('.source.md'))}"
        if "digital-companion" in str(output_pdf)
        else "First paper proof generated from controlled print source"
    )
    story: list[object] = [
        Paragraph(title, h1),
        Paragraph(provenance, small),
        Spacer(1, 6 * mm),
    ]

    for block_type, value in parse_markdown_tables(source_text.splitlines()):
        if block_type == "table":
            rows = value
            if not rows:
                continue
            col_count = max(len(row) for row in rows)
            normalized = [row + [""] * (col_count - len(row)) for row in rows]
            width = A4[0] - 30 * mm
            col_width = width / max(col_count, 1)
            data = [
                [Paragraph(inline_pdf(cell), small) for cell in row]
                for row in normalized
            ]
            table = Table(data, colWidths=[col_width] * col_count, repeatRows=1)
            table.setStyle(
                TableStyle(
                    [
                        ("FONTNAME", (0, 0), (-1, -1), font_name),
                        ("BACKGROUND", (0, 0), (-1, 0), colors.whitesmoke),
                        ("GRID", (0, 0), (-1, -1), 0.25, colors.lightgrey),
                        ("VALIGN", (0, 0), (-1, -1), "TOP"),
                        ("LEFTPADDING", (0, 0), (-1, -1), 2),
                        ("RIGHTPADDING", (0, 0), (-1, -1), 2),
                        ("TOPPADDING", (0, 0), (-1, -1), 2),
                        ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
                    ]
                )
            )
            story.append(table)
            story.append(Spacer(1, 4 * mm))
            continue

        line = value
        stripped = line.strip()
        if not stripped:
            story.append(Spacer(1, 2 * mm))
        elif line.startswith("# "):
            story.append(Paragraph(inline_pdf(line[2:].strip()), h1))
        elif line.startswith("## "):
            text = line[3:].strip()
            if text in {"Чистий текст реконструкції", "Clean Reconstructed Text"}:
                story.append(PageBreak())
            story.append(Paragraph(inline_pdf(text), h2))
        elif line.startswith("### "):
            story.append(Paragraph(inline_pdf(line[4:].strip()), h3))
        elif line.startswith("- "):
            story.append(Paragraph("• " + inline_pdf(line[2:].strip()), base))
        elif line.startswith("```"):
            continue
        elif line.startswith("> "):
            story.append(Paragraph(inline_pdf(line[2:].strip()), mono))
        else:
            story.append(Paragraph(inline_pdf(stripped), base))

    doc = SimpleDocTemplate(
        str(output_pdf),
        pagesize=A4,
        rightMargin=15 * mm,
        leftMargin=15 * mm,
        topMargin=17 * mm,
        bottomMargin=17 * mm,
        title=title,
        author="EUAGELIA Project",
    )
    doc.build(story, onFirstPage=draw_footer, onLaterPages=draw_footer)


def draw_footer(canvas, doc) -> None:  # noqa: ANN001
    canvas.saveState()
    canvas.setFont("EUAGELIA", 8)
    canvas.drawCentredString(A4[0] / 2, 9 * mm, f"Proof v0.1 - page {doc.page}")
    canvas.restoreState()


def render_job(job: ProofJob, font_name: str) -> list[Path]:
    source_text = job.source.read_text(encoding="utf-8")
    html_path = job.output_base.with_suffix(".html")
    pdf_path = job.output_base.with_suffix(".pdf")
    copied_source = job.output_base.with_suffix(".source.md")
    html_path.write_text(markdown_to_html(source_text, job.title), encoding="utf-8")
    copied_source.write_text(source_text, encoding="utf-8")
    build_pdf(source_text, pdf_path, job.title, font_name)
    return [html_path, pdf_path, copied_source]


def write_manifest(paths: Iterable[Path], log_path: Path, font_path: Path) -> None:
    now = datetime.now(timezone.utc).isoformat()
    lines = [
        "# EUAGELIA First Proof Render Log",
        "",
        f"Generated UTC: {now}",
        f"Python runtime: {PYTHON_RUNTIME}",
        f"Font: {font_path}",
        "",
        "| Artifact | Bytes | SHA256 |",
        "| --- | ---: | --- |",
    ]
    for path in paths:
        lines.append(f"| `{rel(path)}` | {path.stat().st_size} | `{sha256(path)}` |")
    log_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--only", choices=["uk", "en", "digital"], help="Render one job only.")
    args = parser.parse_args()

    font_path = find_font()
    pdfmetrics.registerFont(TTFont("EUAGELIA", str(font_path)))

    selected_jobs = [job for job in JOBS if args.only in {None, job.label}]
    outputs: list[Path] = []
    for job in selected_jobs:
        job.output_base.parent.mkdir(parents=True, exist_ok=True)
        outputs.extend(render_job(job, "EUAGELIA"))
    log_path = ROOT / "output/render-log-first-proofs-v0.1.md"
    write_manifest(outputs, log_path, font_path)
    print(f"Rendered {len(outputs)} artifacts")
    print(rel(log_path))


if __name__ == "__main__":
    main()
