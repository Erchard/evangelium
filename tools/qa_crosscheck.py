#!/usr/bin/env python3
"""Project consistency checks for EUAGELIA logion files."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_ALL = list(range(1, 115))
EXPECTED_READER = [
    1, 2, 3, 4, 5, 6, 9, 10, 16, 20, 22, 25, 26, 31, 32, 33, 34,
    35, 36, 39, 41, 45, 46, 47, 54, 63, 72, 73, 86, 89, 91, 95, 96, 99, 100, 103, 107,
]


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def parse_headings(text: str, pattern: str) -> list[int]:
    return [int(value) for value in re.findall(pattern, text, re.M)]


def normalized(text: str) -> str:
    text = re.sub(r"(?m)^>\s?", "", text)
    text = text.replace("ʼ", "'").replace("’", "'")
    text = text.replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", text).strip()


def parse_uk_clean() -> dict[int, str]:
    text = read("reconstruction/earliest-sayings-gospel/reconstructed-gospel-uk.md")
    result: dict[int, str] = {}
    for match in re.finditer(r"^## (\d+)\n\n(.*?)(?=^## \d+\n|\Z)", text, re.S | re.M):
        result[int(match.group(1))] = match.group(2).strip()
    return result


def parse_reader_file(rel: str, pattern: str) -> list[int]:
    return parse_headings(read(rel), pattern)


def parse_parallel_reader() -> list[int]:
    return [
        int(value)
        for value in re.findall(
            r"^\| Logion (\d+) \|",
            read("reconstruction/earliest-sayings-gospel/parallel-edition.md"),
            re.M,
        )
    ]


def parse_workflow_reader_yes() -> list[int]:
    result: list[int] = []
    for line in read("corpus/tables/logia-workflow-matrix.md").splitlines():
        if not re.match(r"^\|\s*\d+\s*\|", line):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) >= 5 and cells[4] == "YES":
            result.append(int(cells[0]))
    return result


def parse_all114_reader_marked() -> list[int]:
    text = read("reconstruction/earliest-sayings-gospel/all-114-publication-decision-table-v0.1.md")
    start = text.index("## Full All-114 Publication Decision Table")
    table = text[start:]
    result: list[int] = []
    for line in table.splitlines():
        match = re.match(r"^\|\s*(\d+)\s*\|", line)
        if not match:
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) >= 3 and cells[2] == "`READER_INCLUDE_MARKED`":
            result.append(int(cells[0]))
    return result


def appendix_blocks() -> dict[int, str]:
    text = read("reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-uk.md")
    matches = list(re.finditer(r"^## Логія (\d+)\b", text, re.M))
    result: dict[int, str] = {}
    for index, match in enumerate(matches):
        start = match.start()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        result[int(match.group(1))] = text[start:end]
    return result


def main() -> int:
    errors: list[str] = []

    cards = sorted((ROOT / "corpus/cards").glob("logion-*.md"))
    card_nums: list[int] = []
    for card in cards:
        match = re.match(r"logion-(\d{3})\.md$", card.name)
        if not match:
            continue
        number = int(match.group(1))
        card_nums.append(number)
        heading = re.search(r"^# Logion (\d+)\b", card.read_text(encoding="utf-8"), re.M)
        if not heading or int(heading.group(1)) != number:
            fail(errors, f"Card heading mismatch: {card.relative_to(ROOT)}")

    if card_nums != EXPECTED_ALL:
        fail(errors, f"Card file set mismatch: {card_nums}")

    blocks = appendix_blocks()
    app_nums = list(blocks)
    if app_nums != EXPECTED_ALL:
        fail(errors, f"Appendix heading sequence mismatch: {app_nums}")

    app_text = read("reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-uk.md")
    if app_text.count("### Джерела й контрольні файли") != 114:
        fail(errors, "Appendix source/control section count is not 114")
    if app_text.count("### Статус у реконструкції") != 114:
        fail(errors, "Appendix status section count is not 114")

    uk_clean = parse_uk_clean()
    reader_sets = {
        "uk": list(uk_clean),
        "en": parse_reader_file(
            "reconstruction/earliest-sayings-gospel/reconstructed-gospel-en.md",
            r"^## Logion (\d+)\b",
        ),
        "greek": parse_reader_file(
            "reconstruction/earliest-sayings-gospel/reconstructed-gospel-greek.md",
            r"^## Logion (\d+)\b",
        ),
        "coptic": parse_reader_file(
            "reconstruction/earliest-sayings-gospel/reconstructed-gospel-coptic.md",
            r"^## Logion (\d+)\b",
        ),
        "arabic": parse_reader_file(
            "reconstruction/earliest-sayings-gospel/reconstructed-gospel-ar-quranic-register.md",
            r"^## قول (\d+)\b",
        ),
        "uk_apparatus": parse_reader_file(
            "reconstruction/earliest-sayings-gospel/reconstructed-gospel-uk-apparatus.md",
            r"^## Логія (\d+)\b",
        ),
        "parallel": parse_parallel_reader(),
        "workflow": parse_workflow_reader_yes(),
        "all114": parse_all114_reader_marked(),
    }

    for name, nums in reader_sets.items():
        if nums != EXPECTED_READER:
            fail(errors, f"Reader set mismatch for {name}: {nums}")

    for number, clean_text in uk_clean.items():
        block = blocks.get(number, "")
        if "Чистий текст реконструкції" not in block:
            fail(errors, f"Missing clean-text anchor in appendix Logion {number}")
        if normalized(clean_text) not in normalized(block):
            fail(errors, f"Clean Ukrainian text not found in appendix Logion {number}")
        status_area = block.split("### Про що ця логія", 1)[0].split("### Що це за матеріал", 1)[0]
        if not any(
            marker in status_area
            for marker in [
                "У чистому тексті",
                "Частково в чистому тексті",
                "Reader status: У чистому тексті",
            ]
        ):
            fail(errors, f"Appendix Logion {number} does not mark reader inclusion")

    for number, block in blocks.items():
        if number in uk_clean:
            continue
        status_area = block.split("### Про що ця логія", 1)[0].split("### Що це за матеріал", 1)[0]
        if any(
            marker in status_area
            for marker in [
                "У чистому тексті",
                "Частково в чистому тексті",
                "Reader status: У чистому тексті",
            ]
        ):
            fail(errors, f"Non-reader appendix Logion {number} is marked as included")

    if errors:
        print("QA crosscheck FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("QA crosscheck OK")
    print("- card files: 114/114")
    print("- appendix sections: 114/114")
    print("- appendix source/control sections: 114/114")
    print("- reader sets: 37/37 synchronized across language layers and control tables")
    print("- clean-text anchors: present for all clean-reader logia")
    return 0


if __name__ == "__main__":
    sys.exit(main())
