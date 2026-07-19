#!/usr/bin/env python3
"""Render full-length EUAGELIA proof PDFs from assembled Markdown sources."""

from __future__ import annotations

import argparse
import hashlib
import html
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


ROOT = Path(__file__).resolve().parents[1]
PYTHON_RUNTIME = "/Users/arseny/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3"
FONT_CANDIDATES = [
    Path("/System/Library/Fonts/Supplemental/Times New Roman.ttf"),
    Path("/System/Library/Fonts/Times.ttc"),
    Path("/System/Library/Fonts/Supplemental/Georgia.ttf"),
]
FONT_BOLD_CANDIDATES = [
    Path("/System/Library/Fonts/Supplemental/Times New Roman Bold.ttf"),
    Path("/System/Library/Fonts/Supplemental/Georgia Bold.ttf"),
]
COPTIC_FONT_CANDIDATES = [
    Path("/System/Library/Fonts/Supplemental/NotoSansCoptic-Regular.ttf"),
    Path("/System/Library/Fonts/Supplemental/Arial Unicode.ttf"),
    Path("/Library/Fonts/Arial Unicode.ttf"),
]
GREEK_FONT_CANDIDATES = [
    Path("/System/Library/Fonts/Supplemental/Times New Roman.ttf"),
    Path("/System/Library/Fonts/Times.ttc"),
    Path("/System/Library/Fonts/Supplemental/Georgia.ttf"),
]


@dataclass(frozen=True)
class Job:
    label: str
    title: str
    source: Path
    output_base: Path


JOBS = [
    Job(
        "uk",
        "EUAGELIA Ukrainian Full Book Proof",
        ROOT / "output/uk-paper-book/book-source-uk-full.md",
        ROOT / "output/uk-paper-book/euagelia-uk-full-proof",
    ),
    Job(
        "en",
        "EUAGELIA English Full Book Proof",
        ROOT / "output/en-paper-book/book-source-en-full.md",
        ROOT / "output/en-paper-book/euagelia-en-full-proof",
    ),
    Job(
        "digital",
        "EUAGELIA Digital Scholarly Companion Full Proof",
        ROOT / "output/digital-scholarly-companion/companion-source-full.md",
        ROOT / "output/digital-scholarly-companion/euagelia-digital-companion-full-proof",
    ),
]


def find_font() -> Path:
    for candidate in FONT_CANDIDATES:
        if candidate.exists():
            return candidate
    raise SystemExit("No Unicode TTF font found.")


def find_bold_font() -> Path | None:
    for candidate in FONT_BOLD_CANDIDATES:
        if candidate.exists():
            return candidate
    return None


def find_coptic_font() -> Path:
    for candidate in COPTIC_FONT_CANDIDATES:
        if candidate.exists():
            return candidate
    raise SystemExit("No Coptic-capable TTF font found.")


def find_greek_font() -> Path:
    for candidate in GREEK_FONT_CANDIDATES:
        if candidate.exists():
            return candidate
    raise SystemExit("No Greek-capable TTF font found.")


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def inline_pdf(value: str) -> str:
    value = value.replace("⟨", "(").replace("⟩", ")")
    is_coptic = bool(re.search(r"[\u2C80-\u2CFF]", value))
    if is_coptic:
        # The source keeps scholarly supralinear/working marks; the print proof
        # drops unsupported combining marks so the Coptic line does not render
        # as a field of boxes.
        value = value.replace("\\`", "").replace("`", "").replace("_", "")
        value = re.sub(r"[\u0300-\u036F]", "", value)
    escaped = html.escape(value)
    escaped = re.sub(r"`([^`]+)`", r"<font name='EUAGELIA'>\1</font>", escaped)
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"\1", escaped)
    escaped = re.sub(r"\*([^*]+)\*", r"<i>\1</i>", escaped)
    if is_coptic:
        escaped = f"<font name='EUAGELIA-Coptic'>{escaped}</font>"
    elif re.search(r"[\u0370-\u03FF\u1F00-\u1FFF\u27E8\u27E9]", value):
        escaped = f"<font name='EUAGELIA-Greek'>{escaped}</font>"
    return escaped


def split_clean_entries(lines: list[str], lang: str) -> tuple[list[tuple[str, list[str]]], int]:
    start_heading = "## Логії Ісуса" if lang == "uk" else "## Clean Reconstructed Text"
    stop_heading = "## Як читати це видання" if lang == "uk" else "## How To Read This Edition"
    logion_pattern = re.compile(r"^##\s+(?P<num>\d+[A-Z]?)$" if lang == "uk" else r"^##\s+Logion\s+(?P<num>\d+[A-Z]?)$")
    entries: list[tuple[str, list[str]]] = []
    in_clean = False
    current_num: str | None = None
    current_lines: list[str] = []
    stop_index = 0
    for idx, line in enumerate(lines):
        if line == start_heading:
            in_clean = True
            continue
        if in_clean and (line == stop_heading or (line.startswith("## ") and not logion_pattern.match(line))):
            if current_num is not None:
                entries.append((current_num, current_lines))
            stop_index = idx
            break
        if not in_clean:
            continue
        match = logion_pattern.match(line)
        if match:
            if current_num is not None:
                entries.append((current_num, current_lines))
            current_num = match.group("num")
            current_lines = []
        elif current_num is not None and line.strip():
            current_lines.append(line.strip())
    return entries, stop_index


def clean_entry_weight(text: str, chars_per_line: int) -> float:
    lines = max(1, (len(text) + chars_per_line - 1) // chars_per_line)
    return lines + 0.75


def clean_column(entries: list[tuple[str, list[str]]], style: ParagraphStyle) -> list[object]:
    flowables: list[object] = []
    for num, lines in entries:
        flowables.append(Paragraph(f"{html.escape(num)} {inline_pdf(' '.join(lines))}", style))
        flowables.append(Spacer(1, 1.25 * mm))
    return flowables


def split_clean_pages(entries: list[tuple[str, list[str]]], lang: str) -> list[tuple[list[tuple[str, list[str]]], list[tuple[str, list[str]]]]]:
    chars_per_line = 34 if lang == "uk" else 38
    column_capacity = 43.0 if lang == "uk" else 45.0
    pages = []
    index = 0
    while index < len(entries):
        remaining = entries[index:]
        remaining_weight = sum(clean_entry_weight(" ".join(entry[1]), chars_per_line) for entry in remaining)
        if len(remaining) > 3 and remaining_weight <= column_capacity:
            target = remaining_weight / 2
            left: list[tuple[str, list[str]]] = []
            left_weight = 0.0
            split_at = 0
            for split_at, entry in enumerate(remaining):
                weight = clean_entry_weight(" ".join(entry[1]), chars_per_line)
                if left and left_weight + weight > target:
                    break
                left.append(entry)
                left_weight += weight
            else:
                split_at = len(remaining)
            pages.append((left, remaining[split_at:]))
            break

        columns = []
        for _ in range(2):
            used = 0.0
            column: list[tuple[str, list[str]]] = []
            while index < len(entries):
                text = " ".join(entries[index][1])
                weight = clean_entry_weight(text, chars_per_line)
                if column and used + weight > column_capacity:
                    break
                column.append(entries[index])
                used += weight
                index += 1
            columns.append(column)
        left, right = columns
        pages.append((left, right))
    return pages


def clean_column_table(
    left_entries: list[tuple[str, list[str]]],
    right_entries: list[tuple[str, list[str]]],
    style: ParagraphStyle,
) -> Table:
    width = (A4[0] - 32 * mm) / 2
    table = Table([[clean_column(left_entries, style), clean_column(right_entries, style)]], colWidths=[width, width])
    table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 4),
                ("RIGHTPADDING", (0, 0), (-1, -1), 9),
                ("TOPPADDING", (0, 0), (-1, -1), 2),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
            ]
        )
    )
    return table


def clean_text_story(entries: list[tuple[str, list[str]]], style: ParagraphStyle, lang: str) -> list[object]:
    story: list[object] = []
    for page_index, (left_entries, right_entries) in enumerate(split_clean_pages(entries, lang)):
        if page_index:
            story.append(PageBreak())
        story.append(clean_column_table(left_entries, right_entries, style))
    return story


def markdown_blocks(lines: list[str]):
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
            yield ("table", rows)
            continue
        yield ("line", line)
        i += 1


def render_markdown_tail(lines: list[str], styles: dict[str, ParagraphStyle], font_name: str) -> list[object]:
    story: list[object] = []
    for block_type, value in markdown_blocks(lines):
        if block_type == "table":
            rows = value
            if rows:
                col_count = max(len(row) for row in rows)
                width = A4[0] - 32 * mm
                data = []
                for row in rows:
                    row = row + [""] * (col_count - len(row))
                    data.append([Paragraph(inline_pdf(cell), styles["tiny"]) for cell in row])
                table = Table(data, colWidths=[width / col_count] * col_count, repeatRows=1)
                table.setStyle(
                    TableStyle(
                        [
                            ("FONTNAME", (0, 0), (-1, -1), font_name),
                            ("BACKGROUND", (0, 0), (-1, 0), colors.whitesmoke),
                            ("GRID", (0, 0), (-1, -1), 0.18, colors.lightgrey),
                            ("VALIGN", (0, 0), (-1, -1), "TOP"),
                            ("LEFTPADDING", (0, 0), (-1, -1), 1.5),
                            ("RIGHTPADDING", (0, 0), (-1, -1), 1.5),
                            ("TOPPADDING", (0, 0), (-1, -1), 1),
                            ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
                        ]
                    )
                )
                story.append(table)
            continue
        line = value.strip()
        if not line:
            story.append(Spacer(1, 1.5 * mm))
        elif line == ">":
            story.append(Spacer(1, 1.5 * mm))
        elif line.startswith("# "):
            story.append(PageBreak())
            story.append(Paragraph(inline_pdf(line[2:]), styles["h1"]))
        elif line.startswith("## "):
            story.append(PageBreak())
            story.append(Paragraph(inline_pdf(line[3:]), styles["h2"]))
        elif line.startswith("### "):
            story.append(Paragraph(f"<b>{inline_pdf(line[4:])}</b>", styles["h3"]))
        elif line.startswith("- "):
            story.append(Paragraph("• " + inline_pdf(line[2:]), styles["base"]))
        elif re.match(r"^\d+\.\s+", line):
            story.append(Paragraph(inline_pdf(line), styles["base"]))
        elif line.startswith("> "):
            story.append(Paragraph(inline_pdf(line[2:]), styles["quote"]))
        else:
            story.append(Paragraph(inline_pdf(line), styles["base"]))
    return story


def build_pdf(source_text: str, output_pdf: Path, title: str, font_name: str, lang: str) -> None:
    sample = getSampleStyleSheet()
    base = ParagraphStyle("Base", parent=sample["BodyText"], fontName=font_name, fontSize=14, leading=17.4, alignment=TA_LEFT, spaceAfter=4.8)
    styles = {
        "base": base,
        "clean": ParagraphStyle("Clean", parent=base, fontSize=14, leading=17.0, alignment=TA_JUSTIFY, spaceAfter=2.2),
        "title": ParagraphStyle("Title", parent=base, fontSize=22, leading=26, alignment=TA_CENTER, spaceAfter=16),
        "subtitle": ParagraphStyle("Subtitle", parent=base, fontSize=14, leading=17.4, alignment=TA_CENTER, spaceAfter=8),
        "h1": ParagraphStyle("H1", parent=base, fontSize=19, leading=23, alignment=TA_CENTER, spaceBefore=7, spaceAfter=11),
        "h2": ParagraphStyle("H2", parent=base, fontSize=17, leading=21, alignment=TA_CENTER, spaceBefore=7, spaceAfter=10),
        "h3": ParagraphStyle("H3", parent=base, fontSize=15, leading=18.5, spaceBefore=8, spaceAfter=5),
        "quote": ParagraphStyle("Quote", parent=base, leftIndent=8 * mm, rightIndent=5 * mm, fontSize=14, leading=17.4, alignment=TA_LEFT),
        "tiny": ParagraphStyle("Tiny", parent=base, fontSize=10.8, leading=12.9),
    }
    lines = source_text.splitlines()
    heading = next((line[2:].strip() for line in lines if line.startswith("# ")), title)
    clean_entries, tail_start = split_clean_entries(lines, lang)
    if lang == "digital":
        proof_label = "Digital companion full proof v0.1"
    elif lang == "en":
        proof_label = "Working edition, July 19, 2026"
    else:
        proof_label = "Робоча редакція, 19 липня 2026"
    story: list[object] = [
        Spacer(1, 28 * mm),
        Paragraph(inline_pdf(heading), styles["title"]),
        Paragraph(proof_label, styles["subtitle"]),
    ]
    if clean_entries:
        story.extend(
            [
                PageBreak(),
                Paragraph("Clean Reconstructed Text" if lang == "en" else "Логії Ісуса", styles["h2"]),
                *clean_text_story(clean_entries, styles["clean"], lang),
            ]
        )
    if tail_start:
        story.extend(render_markdown_tail(lines[tail_start:], styles, font_name))
    elif not clean_entries:
        story.extend(render_markdown_tail(lines[1:], styles, font_name))
    doc = SimpleDocTemplate(
        str(output_pdf),
        pagesize=A4,
        rightMargin=12 * mm,
        leftMargin=12 * mm,
        topMargin=15 * mm,
        bottomMargin=14 * mm,
        title=title,
        author="EUAGELIA Project",
    )
    doc.build(story, onFirstPage=draw_footer, onLaterPages=draw_footer)


def draw_footer(canvas, doc) -> None:  # noqa: ANN001
    canvas.saveState()
    canvas.setFont("EUAGELIA", 8)
    if "Digital Scholarly Companion" in doc.title:
        footer = f"EUAGELIA digital companion proof - {doc.page}"
    else:
        footer = str(doc.page)
    canvas.drawCentredString(A4[0] / 2, 8 * mm, footer)
    canvas.restoreState()


def render_job(job: Job, font_name: str) -> list[Path]:
    text = job.source.read_text(encoding="utf-8")
    pdf_path = job.output_base.with_suffix(".pdf")
    source_copy = job.output_base.with_suffix(".source.md")
    source_copy.write_text(text, encoding="utf-8")
    build_pdf(text, pdf_path, job.title, font_name, job.label)
    return [pdf_path, source_copy]


def write_manifest(paths: list[Path], font_path: Path, coptic_font_path: Path, greek_font_path: Path) -> None:
    lines = [
        "# EUAGELIA Full Book Proof Render Log",
        "",
        f"Generated UTC: {datetime.now(timezone.utc).isoformat()}",
        f"Python runtime: {PYTHON_RUNTIME}",
        f"Font: {font_path}",
        f"Coptic font: {coptic_font_path}",
        f"Greek font: {greek_font_path}",
        "",
        "| Artifact | Bytes | SHA256 |",
        "| --- | ---: | --- |",
    ]
    for path in paths:
        lines.append(f"| `{rel(path)}` | {path.stat().st_size} | `{sha256(path)}` |")
    (ROOT / "output/render-log-full-book-proofs-v0.1.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--only", choices=["uk", "en", "digital"])
    args = parser.parse_args()
    font_path = find_font()
    bold_font_path = find_bold_font()
    coptic_font_path = find_coptic_font()
    greek_font_path = find_greek_font()
    pdfmetrics.registerFont(TTFont("EUAGELIA", str(font_path)))
    if bold_font_path:
        pdfmetrics.registerFont(TTFont("EUAGELIA-Bold", str(bold_font_path)))
        pdfmetrics.registerFontFamily("EUAGELIA", normal="EUAGELIA", bold="EUAGELIA-Bold")
    pdfmetrics.registerFont(TTFont("EUAGELIA-Coptic", str(coptic_font_path)))
    pdfmetrics.registerFont(TTFont("EUAGELIA-Greek", str(greek_font_path)))
    selected = [job for job in JOBS if args.only in {None, job.label}]
    outputs: list[Path] = []
    for job in selected:
        job.output_base.parent.mkdir(parents=True, exist_ok=True)
        outputs.extend(render_job(job, "EUAGELIA"))
    write_manifest(outputs, font_path, coptic_font_path, greek_font_path)
    print(f"Rendered {len(outputs)} artifacts")
    print("output/render-log-full-book-proofs-v0.1.md")


if __name__ == "__main__":
    main()
