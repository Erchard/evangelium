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
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
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
BIBLIOGRAPHY_SOURCE = ROOT / "bibliography/bibliography-working.md"
RIGHTS_SOURCE = ROOT / "bibliography/source-rights-register.md"
FONT_CANDIDATES = [
    Path("/System/Library/Fonts/Supplemental/Times New Roman.ttf"),
    Path("/System/Library/Fonts/Supplemental/Arial Unicode.ttf"),
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
    if "digital-companion" not in str(output_pdf):
        build_paper_pdf(source_text, output_pdf, title, font_name)
        return

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


def build_paper_pdf(source_text: str, output_pdf: Path, title: str, font_name: str) -> None:
    lang = "uk" if "uk-paper-book" in str(output_pdf) else "en"
    clean_title = "Чистий текст реконструкції" if lang == "uk" else "Clean Reconstructed Text"
    contents_title = "Зміст" if lang == "uk" else "Contents"
    appendix_title = "Додаток та індекси" if lang == "uk" else "Appendix And Indexes"
    note_title = "Як читати це видання" if lang == "uk" else "How To Read This Edition"
    bibliography_title = "Бібліографія і права" if lang == "uk" else "Bibliography And Rights"
    commons = (
        "Оригінальний внесок EUAGELIA призначений як спільне надбання людства; "
        "сторонні джерела зберігають власний правовий статус."
        if lang == "uk"
        else "The original EUAGELIA contribution is intended as a commons; "
        "external sources retain their own legal status."
    )

    base = ParagraphStyle(
        "PaperBase",
        fontName=font_name,
        fontSize=8.7,
        leading=10.2,
        alignment=TA_LEFT,
        spaceAfter=2.4,
    )
    justified = ParagraphStyle("PaperJustified", parent=base, alignment=TA_JUSTIFY)
    title_style = ParagraphStyle(
        "PaperTitle",
        parent=base,
        fontSize=23,
        leading=27,
        alignment=TA_CENTER,
        spaceAfter=16,
    )
    subtitle_style = ParagraphStyle(
        "PaperSubtitle",
        parent=base,
        fontSize=10.5,
        leading=13,
        alignment=TA_CENTER,
        spaceAfter=10,
    )
    section_style = ParagraphStyle(
        "PaperSection",
        parent=base,
        fontSize=12.5,
        leading=14.5,
        alignment=TA_CENTER,
        spaceBefore=7,
        spaceAfter=8,
    )
    compact = ParagraphStyle("PaperCompact", parent=base, fontSize=7.3, leading=8.35)
    small = ParagraphStyle("PaperSmall", parent=base, fontSize=6.4, leading=7.2)
    tiny = ParagraphStyle("PaperTiny", parent=base, fontSize=5.8, leading=6.5)

    clean_entries, remaining = split_clean_entries(source_text, lang)
    reader_note, table_rows, bibliography_note, rights_note = parse_paper_sections(remaining, lang)

    edition_note = (
        "Паперовий proof v0.4. Чистий текст лишається замороженим; цей прохід змінює тільки верстку, "
        "орієнтаційні сторінки, індекси та бібліографічний шар."
        if lang == "uk"
        else "Paper proof v0.4. The clean text remains frozen; this pass changes only layout, "
        "orientation pages, indexes, and bibliography apparatus."
    )
    contents_note = (
        "Сторінки можуть змінитися під час фінального набору; тому цей зміст фіксує порядок розділів, "
        "а не удає остаточну пагінацію."
        if lang == "uk"
        else "Page numbers may still change during final typesetting; this contents page fixes the order "
        "of sections without pretending to final pagination."
    )
    story: list[object] = [
        Spacer(1, 35 * mm),
        Paragraph(extract_main_title(source_text), title_style),
        Paragraph(
            "Реконструкція найдавнішого досяжного Євангелія висловів"
            if lang == "uk"
            else "A reconstruction of the earliest recoverable sayings gospel",
            subtitle_style,
        ),
        Spacer(1, 8 * mm),
        Paragraph(edition_note, subtitle_style),
        Spacer(1, 12 * mm),
        Paragraph(commons, subtitle_style),
        PageBreak(),
        Paragraph(contents_title, section_style),
        Paragraph(contents_note, justified),
        Spacer(1, 5 * mm),
        Paragraph(f"1. {clean_title}", base),
        Paragraph(f"2. {note_title}", base),
        Paragraph(f"3. {appendix_title}", base),
        Paragraph(f"4. {bibliography_title}", base),
        PageBreak(),
        Paragraph(clean_title, section_style),
    ]

    story.extend(two_column_clean_table(clean_entries, compact))
    story.append(PageBreak())
    story.append(Paragraph(note_title, section_style))
    story.extend(paragraphs_from_text(reader_note, base))
    story.append(PageBreak())
    story.append(Paragraph(appendix_title, section_style))
    story.extend(render_print_indexes(table_rows, lang, base, section_style, small, tiny, font_name))
    story.append(PageBreak())
    story.append(Paragraph(bibliography_title, section_style))
    story.extend(print_bibliography_story(lang, base, small))
    story.append(Spacer(1, 4 * mm))
    story.extend(paragraphs_from_text(final_bibliography_caution(lang, rights_note), base))

    doc = SimpleDocTemplate(
        str(output_pdf),
        pagesize=A4,
        rightMargin=11 * mm,
        leftMargin=11 * mm,
        topMargin=15 * mm,
        bottomMargin=14 * mm,
        title=title,
        author="EUAGELIA Project",
    )
    doc.build(story, onFirstPage=draw_footer, onLaterPages=draw_footer)


def extract_main_title(source_text: str) -> str:
    for line in source_text.splitlines():
        if line.startswith("# "):
            return inline_pdf(line[2:].strip())
    return "EUAGELIA"


def split_clean_entries(source_text: str, lang: str) -> tuple[list[tuple[str, list[str]]], str]:
    stop_heading = "## Як читати додаток" if lang == "uk" else "## How To Read The Appendix"
    logion_pattern = re.compile(r"^##\s+(?P<num>\d+[A-Z]?)$" if lang == "uk" else r"^##\s+Logion\s+(?P<num>\d+[A-Z]?)$")
    entries: list[tuple[str, list[str]]] = []
    current_num: str | None = None
    current_lines: list[str] = []
    remaining_start = 0
    lines = source_text.splitlines()
    in_clean = False
    for idx, line in enumerate(lines):
        if line in {"## Чистий текст реконструкції", "## Clean Reconstructed Text"}:
            in_clean = True
            continue
        if in_clean and line == stop_heading:
            if current_num is not None:
                entries.append((current_num, current_lines))
            remaining_start = idx
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
    return entries, "\n".join(lines[remaining_start:])


def parse_paper_sections(remaining: str, lang: str) -> tuple[str, list[list[str]], str, str]:
    lines = remaining.splitlines()
    table_rows: list[list[str]] = []
    reader_note: list[str] = []
    bibliography_note: list[str] = []
    rights_note: list[str] = []
    mode = "reader"
    in_table = False
    for idx, line in enumerate(lines):
        if line.startswith("## Додаток:") or line.startswith("## Print-Safe Evidence"):
            mode = "table"
            continue
        if line.startswith("## Бібліограф") or line.startswith("## Bibliography"):
            mode = "bibliography"
            in_table = False
            continue
        if line.startswith("## Примітка про права") or line.startswith("## Rights Note"):
            mode = "rights"
            in_table = False
            continue
        if mode == "table":
            if line.startswith("|"):
                cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
                if not all(re.fullmatch(r":?-{3,}:?", cell or "") for cell in cells):
                    table_rows.append(cells)
                in_table = True
            elif in_table and line.strip():
                mode = "other"
            continue
        if mode == "reader" and line.strip() and not line.startswith("## "):
            reader_note.append(line)
        elif mode == "bibliography" and line.strip() and not line.startswith("## "):
            bibliography_note.append(line)
        elif mode == "rights" and line.strip() and not line.startswith("## "):
            rights_note.append(line)
    return "\n".join(reader_note), table_rows, "\n".join(bibliography_note), "\n".join(rights_note)


def paragraphs_from_text(text: str, style: ParagraphStyle) -> list[object]:
    result: list[object] = []
    for line in text.splitlines():
        clean = line.strip()
        if not clean:
            result.append(Spacer(1, 2 * mm))
        elif clean.startswith("- "):
            result.append(Paragraph("• " + inline_pdf(clean[2:]), style))
        else:
            result.append(Paragraph(inline_pdf(clean), style))
    return result


def two_column_clean_table(entries: list[tuple[str, list[str]]], style: ParagraphStyle) -> list[object]:
    cells = []
    for number, lines in entries:
        text = " ".join(lines)
        cells.append(Paragraph(f"<b>{html.escape(number)}</b> {inline_pdf(text)}", style))
    split_at = (len(cells) + 1) // 2
    left = cells[:split_at]
    right = cells[split_at:]
    while len(right) < len(left):
        right.append(Paragraph("", style))
    rows = [[left[i], right[i]] for i in range(len(left))]
    table = Table(rows, colWidths=[(A4[0] - 30 * mm) / 2] * 2, hAlign="LEFT")
    table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 4),
                ("RIGHTPADDING", (0, 0), (-1, -1), 7),
                ("TOPPADDING", (0, 0), (-1, -1), 3),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
            ]
        )
    )
    return [table]


def render_remaining_paper_blocks(
    remaining: str,
    base: ParagraphStyle,
    section_style: ParagraphStyle,
    small: ParagraphStyle,
    font_name: str,
) -> list[object]:
    story: list[object] = []
    for block_type, value in parse_markdown_tables(remaining.splitlines()):
        if block_type == "table":
            story.append(compact_reference_table(value, small, font_name))
            story.append(Spacer(1, 3 * mm))
            continue
        line = value.strip()
        if not line:
            continue
        if line.startswith("## "):
            story.append(Paragraph(inline_pdf(line[3:].strip()), section_style))
        elif line.startswith("# "):
            continue
        elif line.startswith("- "):
            story.append(Paragraph("• " + inline_pdf(line[2:].strip()), base))
        else:
            story.append(Paragraph(inline_pdf(line), base))
    return story


def render_print_indexes(
    rows: list[list[str]],
    lang: str,
    base: ParagraphStyle,
    section_style: ParagraphStyle,
    small: ParagraphStyle,
    tiny: ParagraphStyle,
    font_name: str,
) -> list[object]:
    if not rows:
        return [Paragraph("No index table found.", base)]
    header, data_rows = rows[0], rows[1:]
    indexes = {name: idx for idx, name in enumerate(header)}

    def get(row: list[str], *names: str) -> str:
        for name in names:
            idx = indexes.get(name)
            if idx is not None and idx < len(row):
                return row[idx]
        return ""

    included = []
    not_included = []
    witness_groups: dict[str, list[str]] = {}
    status_groups: dict[str, list[str]] = {}
    for row in data_rows:
        num = get(row, "Логія", "Logion")
        if not num:
            continue
        status = get(row, "Статус у виданні", "Publication Status")
        decision = get(row, "Рішення", "Clean Reader")
        greek = get(row, "Грецький шар", "Greek Layer")
        material = get(row, "Матеріал", "Unit")
        clean_yes = get(row, "Clean Reader")
        is_included = (
            "У чистому тексті" in status
            or "READER_INCLUDE" in decision
            or clean_yes == "YES"
            or "Частково" in status
        )
        item = [num, compact_status(status, decision, lang), compact_greek(greek), material]
        if is_included:
            included.append(item)
        else:
            not_included.append(item)
        witness_groups.setdefault(compact_greek(greek), []).append(num)
        status_groups.setdefault(compact_status(status, decision, lang), []).append(num)

    story: list[object] = []
    story.append(Paragraph("Included Logia" if lang == "en" else "Логії у чистому тексті", section_style))
    story.append(index_table(["Logion", "Status", "Greek", "Subject"] if lang == "en" else ["Логія", "Статус", "Грецький", "Тема"], included, small, font_name))
    story.append(PageBreak())
    story.append(Paragraph("Non-Included Logia" if lang == "en" else "Логії поза чистим текстом", section_style))
    intro = (
        "These logia remain available in the appendix. The compact index below gives the lookup number, "
        "the present publication decision, and the main subject; Greek witness information is separated "
        "into the witness index."
        if lang == "en"
        else "Ці логії лишаються доступними в додатку. Стислий індекс нижче дає номер для пошуку, "
        "поточне рішення і головну тему; грецькі свідки винесено в окремий індекс."
    )
    story.append(Paragraph(intro, base))
    story.append(index_table(["Logion", "Status", "Subject"] if lang == "en" else ["Логія", "Статус", "Тема"], [[r[0], r[1], r[3]] for r in not_included], small, font_name))
    story.append(PageBreak())
    story.append(Paragraph("Witness Index" if lang == "en" else "Індекс свідків", section_style))
    witness_rows = [[key, compress_numbers(values)] for key, values in sorted(witness_groups.items())]
    story.append(index_table(["Witness / Greek Layer", "Logia"] if lang == "en" else ["Свідок / грецький шар", "Логії"], witness_rows, small, font_name))
    story.append(Spacer(1, 5 * mm))
    story.append(Paragraph("Status Index" if lang == "en" else "Індекс рішень", section_style))
    status_rows = [[key, compress_numbers(values)] for key, values in sorted(status_groups.items())]
    story.append(index_table(["Status", "Logia"] if lang == "en" else ["Статус", "Логії"], status_rows, small, font_name))
    return story


def compact_status(status: str, decision: str, lang: str) -> str:
    text = f"{status} {decision}"
    if lang == "uk":
        if "EXCLUDE_AS_SECONDARY" in text or "вторин" in text:
            return "виключено як вторинне"
        if "У чистому тексті" in status or "READER_INCLUDE" in text or "INCLUDE_WITH_MARKER" in text or "Частково" in status:
            return "у чистому тексті"
        if "DEFER" in text or "відклад" in status:
            return "відкладено"
        if "KEEP_APPENDIX" in text or "APPENDIX_ONLY" in text:
            return "тільки додаток"
        if "UNCERTAIN" in text or "непевн" in status:
            return "не включено"
        return status or decision
    if "EXCLUDE_AS_SECONDARY" in text:
        return "excluded as secondary"
    if "READER_INCLUDE" in text or "INCLUDE_WITH_MARKER" in text:
        return "in clean text"
    if "DEFER" in text:
        return "deferred"
    if "UNCERTAIN" in text or "APPENDIX_ONLY" in text or "KEEP_APPENDIX" in text:
        return "appendix only"
    return status or decision


def compact_greek(value: str) -> str:
    if not value:
        return "no Greek witness"
    replacements = {
        "Greek retroversion, hypothetical": "Greek retroversion",
        "No loaded P.Oxy. witness": "no P.Oxy. witness",
        "No loaded P.Oxy witness": "no P.Oxy. witness",
    }
    return replacements.get(value, value)


def index_table(headers: list[str], rows: list[list[str]], style: ParagraphStyle, font_name: str) -> Table:
    data = [[Paragraph(inline_pdf(cell), style) for cell in headers]]
    data.extend([[Paragraph(inline_pdf(cell), style) for cell in row] for row in rows])
    width = A4[0] - 22 * mm
    if len(headers) == 4:
        col_widths = [15 * mm, 33 * mm, 39 * mm, width - 87 * mm]
    elif len(headers) == 3:
        col_widths = [15 * mm, 36 * mm, width - 51 * mm]
    elif len(headers) == 2:
        col_widths = [42 * mm, width - 42 * mm]
    else:
        col_widths = [width / len(headers)] * len(headers)
    table = Table(data, colWidths=col_widths, repeatRows=1)
    table.setStyle(
        TableStyle(
            [
                ("FONTNAME", (0, 0), (-1, -1), font_name),
                ("BACKGROUND", (0, 0), (-1, 0), colors.whitesmoke),
                ("GRID", (0, 0), (-1, -1), 0.2, colors.lightgrey),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 2),
                ("RIGHTPADDING", (0, 0), (-1, -1), 2),
                ("TOPPADDING", (0, 0), (-1, -1), 1.5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 1.5),
            ]
        )
    )
    return table


def compress_numbers(values: list[str]) -> str:
    parsed: list[tuple[int, str]] = []
    leftovers: list[str] = []
    for value in values:
        match = re.fullmatch(r"(\d+)([A-Z]?)", value)
        if match:
            parsed.append((int(match.group(1)), match.group(2)))
        else:
            leftovers.append(value)
    parsed.sort(key=lambda item: (item[0], item[1]))
    ranges: list[str] = []
    numeric = [number for number, suffix in parsed if not suffix]
    suffixed = [f"{number}{suffix}" for number, suffix in parsed if suffix]
    start: int | None = None
    prev: int | None = None
    for number in numeric:
        if start is None:
            start = prev = number
            continue
        if prev is not None and number == prev + 1:
            prev = number
            continue
        ranges.append(format_range(start, prev))
        start = prev = number
    if start is not None:
        ranges.append(format_range(start, prev))
    return ", ".join(ranges + suffixed + leftovers)


def format_range(start: int, end: int | None) -> str:
    if end is None or end == start:
        return str(start)
    if end == start + 1:
        return f"{start}, {end}"
    return f"{start}-{end}"


def print_bibliography_story(lang: str, base: ParagraphStyle, small: ParagraphStyle) -> list[object]:
    source_status = extract_bibliography_status()
    if lang == "uk":
        entries = [
            "<b>NHC II,2</b>. Коптський рукопис Євангелія від Фоми в Nag Hammadi Codex II, tractate 2. Базовий збережений коптський свідок; фінальні точні читання потребують звірки з facsimile або критичним виданням.",
            "<b>P.Oxy. 1; P.Oxy. 654; P.Oxy. 655</b>. Грецькі Oxyrhynchus papyri, використані через відкритий DCLP / Papyri.info XML-шар з attribution до Digital Corpus of Literary Papyri.",
            "<b>SBLGNT</b>. Society of Biblical Literature Greek New Testament, використано тільки як відкритий грецький контроль канонічних паралелей, не як свідок Фоми.",
            "<b>Mattison Thomas</b>. Mark M. Mattison, public-domain English translation of the Gospel of Thomas; використано як відкритий translation-control, не як база реконструкції.",
            "<b>Layton; Lambdin; DeConick; Patterson / Meyer; Brill CGL; NA / UBS</b>. Захищені сучасні академічні видання і переклади; у поточному паперовому proof вони лишаються тільки цитатно-контрольними і не відтворюються як базовий текст.",
            "<b>P.Oxy. 5575</b>. Fish, Wallace, and Holmes, \"5575. Sayings of Jesus,\" in The Oxyrhynchus Papyri 87. Захищений контрольний матеріал; не використовується як відтворюваний базовий текст.",
        ]
        heading = "Друковані ключі джерел"
        status_line = "Стан бібліографічного шару: release verification v0.2; джерела розділено на відкриті, первинні свідки, захищені лише для контролю і не використані в поточній редакції."
    else:
        entries = [
            "<b>NHC II,2</b>. The Coptic Gospel of Thomas in Nag Hammadi Codex II, tractate 2. Base preserved Coptic witness; final precise readings still require facsimile or critical-edition checking.",
            "<b>P.Oxy. 1; P.Oxy. 654; P.Oxy. 655</b>. Greek Oxyrhynchus papyri used through the open DCLP / Papyri.info XML layer with attribution to the Digital Corpus of Literary Papyri.",
            "<b>SBLGNT</b>. Society of Biblical Literature Greek New Testament, used only as open Greek canonical control, not as a Thomas witness.",
            "<b>Mattison Thomas</b>. Mark M. Mattison's public-domain English Gospel of Thomas translation; used as open translation control, not as EUAGELIA's base text.",
            "<b>Layton; Lambdin; DeConick; Patterson / Meyer; Brill CGL; NA / UBS</b>. Protected modern scholarly editions and translations; in this proof they remain citation/control-only and are not reproduced as base text.",
            "<b>P.Oxy. 5575</b>. Fish, Wallace, and Holmes, \"5575. Sayings of Jesus,\" in The Oxyrhynchus Papyri 87. Protected control material; not used as reproduced base text.",
        ]
        heading = "Print Source Keys"
        status_line = f"Bibliography layer status: {source_status}."
    story: list[object] = [Paragraph(heading, base), Paragraph(status_line, small)]
    for entry in entries:
        story.append(Paragraph(entry, small))
    return story


def final_bibliography_caution(lang: str, rights_note: str) -> str:
    if lang == "uk":
        return "\n\n".join(
            [
                "Перед фінальною версткою цей стислий список треба перетворити на єдиний бібліографічний стиль і перевірити сторінкові посилання тільки там, де вони реально входять у друк. Захищені сучасні видання не мають ставати відкритим базовим текстом EUAGELIA.",
                rights_note,
            ]
        )
    return "\n\n".join(
        [
            "Before final typesetting this compact list should be converted into one uniform bibliography style, with page-specific references checked only where they actually enter print. Protected modern editions must not become EUAGELIA's open base text.",
            rights_note,
        ]
    )


def extract_bibliography_status() -> str:
    statuses: list[str] = []
    for path in (BIBLIOGRAPHY_SOURCE, RIGHTS_SOURCE):
        try:
            text = path.read_text(encoding="utf-8")
        except FileNotFoundError:
            continue
        for line in text.splitlines():
            if line.startswith("Status:"):
                statuses.append(line.replace("Status:", "").strip().rstrip("."))
                break
    return "; ".join(statuses) if statuses else "release verification layer present"


def compact_reference_table(rows: list[list[str]], style: ParagraphStyle, font_name: str) -> Table:
    if not rows:
        return Table([[""]])
    header = rows[0]
    keep_names = {"Логія", "Статус у виданні", "Рішення", "Грецький шар", "Logion", "Publication Status", "Clean Reader", "Greek Layer"}
    keep_indexes = [idx for idx, name in enumerate(header) if name in keep_names]
    if not keep_indexes:
        keep_indexes = list(range(min(len(header), 4)))
    compact_rows = [[row[idx] if idx < len(row) else "" for idx in keep_indexes] for row in rows]
    width = A4[0] - 24 * mm
    col_width = width / max(len(compact_rows[0]), 1)
    data = [[Paragraph(inline_pdf(cell), style) for cell in row] for row in compact_rows]
    table = Table(data, colWidths=[col_width] * len(compact_rows[0]), repeatRows=1)
    table.setStyle(
        TableStyle(
            [
                ("FONTNAME", (0, 0), (-1, -1), font_name),
                ("BACKGROUND", (0, 0), (-1, 0), colors.whitesmoke),
                ("GRID", (0, 0), (-1, -1), 0.2, colors.lightgrey),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 2),
                ("RIGHTPADDING", (0, 0), (-1, -1), 2),
                ("TOPPADDING", (0, 0), (-1, -1), 1.5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 1.5),
            ]
        )
    )
    return table


def draw_footer(canvas, doc) -> None:  # noqa: ANN001
    canvas.saveState()
    canvas.setFont("EUAGELIA", 8)
    canvas.drawCentredString(A4[0] / 2, 8 * mm, f"EUAGELIA proof - {doc.page}")
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
