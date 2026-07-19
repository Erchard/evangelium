#!/usr/bin/env python3
"""Assemble full-length EUAGELIA book sources.

This creates paper-facing Markdown sources from controlled project layers. It
does not alter the frozen clean reader. Paper sources are sanitized so internal
repository paths remain in the digital companion rather than in print.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

UK_CLEAN = ROOT / "reconstruction/earliest-sayings-gospel/reconstructed-gospel-uk.md"
EN_CLEAN = ROOT / "reconstruction/earliest-sayings-gospel/reconstructed-gospel-en.md"
UK_APPENDIX = ROOT / "reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-uk.md"
EN_APPENDIX = ROOT / "reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-en.md"
EN_DOSSIER = ROOT / "reconstruction/earliest-sayings-gospel/evidence-dossier-en.md"

UK_OUT = ROOT / "output/uk-paper-book/book-source-uk-full.md"
EN_OUT = ROOT / "output/en-paper-book/book-source-en-full.md"
DIGITAL_OUT = ROOT / "output/digital-scholarly-companion/companion-source-full.md"

PAPER_STATUS_TERMS_UK = {
    "INCLUDE_WITH_MARKER": "включено з обережним маркером",
    "EXCLUDE_AS_SECONDARY": "виключено як вторинне",
    "DEFER_TO_CLUSTER": "відкладено до кластерного рішення",
    "KEEP_APPENDIX_ONLY_FOR_NOW": "залишено тільки в додатку",
    "APPENDIX_ONLY_UNCERTAIN": "тільки додаток, непевно",
    "UNCERTAIN": "непевно",
    "DEFER": "відкладено",
    "FRAME_INCLUDED_WITH_MARKER": "рамка включена з обережним маркером",
}


PRINT_BIBLIOGRAPHY_UK = """## Бібліографія і права

### Друковані ключі джерел

- NHC II,2 - коптський рукопис Євангелія від Фоми в Nag Hammadi Codex II, tractate 2.
- P.Oxy. 1; P.Oxy. 654; P.Oxy. 655 - грецькі Oxyrhynchus papyri, використані через відкритий DCLP / Papyri.info XML-шар.
- SBLGNT - відкритий грецький контроль канонічних паралелей; не свідок Фоми.
- Mattison Thomas - public-domain English translation of the Gospel of Thomas; відкритий translation-control, не база реконструкції.
- Layton; Lambdin; DeConick; Patterson / Meyer; Brill CGL; NA / UBS - захищені сучасні академічні видання й переклади; тільки контроль і цитування, не відкритий базовий текст.
- P.Oxy. 5575 - захищений контрольний матеріал для ширшої ранньої традиції висловів; не відтворюваний базовий текст.

Оригінальна реконструкція, переклади, коментарі й дослідницька архітектура EUAGELIA задумано як спільне надбання людства. Сторонні джерела, сучасні видання, переклади, факсиміле й сайти зберігають власний правовий статус.
"""


PRINT_BIBLIOGRAPHY_EN = """## Bibliography And Rights

### Print Source Keys

- NHC II,2 - the Coptic Gospel of Thomas in Nag Hammadi Codex II, tractate 2.
- P.Oxy. 1; P.Oxy. 654; P.Oxy. 655 - Greek Oxyrhynchus papyri used through the open DCLP / Papyri.info XML layer.
- SBLGNT - open Greek canonical control; not a Thomas witness.
- Mattison Thomas - public-domain English Gospel of Thomas translation; open translation control, not EUAGELIA's base text.
- Layton; Lambdin; DeConick; Patterson / Meyer; Brill CGL; NA / UBS - protected modern scholarly editions and translations; citation/control only, not reproduced as base text.
- P.Oxy. 5575 - protected control material for wider early sayings tradition; not reproduced as base text.

The original EUAGELIA reconstruction, translations, commentary, and research architecture are intended as a commons. External witnesses, modern editions, translations, facsimiles, and websites retain their own legal status.
"""


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8").strip()


def localize_paper_statuses_uk(line: str) -> str:
    line = line.replace("Reader status:", "Статус у читацькому виданні:")
    line = line.replace("Greek witness status:", "Грецьке свідчення:")
    line = line.replace("Publication status:", "Статус публікації:")
    for code, label in PAPER_STATUS_TERMS_UK.items():
        line = re.sub(rf"`?{re.escape(code)}`?", label, line)
    return line


def sanitize_paper_text(text: str, lang: str = "en") -> str:
    text = re.sub(r"`[^`]*(?:corpus|reconstruction|project|sources|controls|notes|output)/[^`]*`", "", text)
    text = re.sub(r"\s+\n", "\n", text)
    lines = []
    for line in text.splitlines():
        stripped = line.strip()
        if re.search(r"(?:corpus|reconstruction|project|sources|controls|notes|output)/", stripped):
            continue
        if stripped.startswith("Evidence note:"):
            continue
        if stripped.startswith("Status:"):
            continue
        if "publication-facing draft" in stripped:
            continue
        if stripped.startswith("Synoptic/control files:"):
            continue
        if stripped.startswith("Cluster/context notes:"):
            continue
        if "Картка:" in stripped or stripped.startswith("Card:"):
            continue
        if stripped.startswith("- окремий synoptic/control file"):
            continue
        if stripped.startswith("- окремий cluster/context note"):
            continue
        line = line.rstrip()
        if lang == "uk":
            line = localize_paper_statuses_uk(line)
        lines.append(line)
    return "\n".join(lines).strip()


def extract_uk_appendix_for_paper() -> str:
    text = read(UK_APPENDIX)
    marker = "## Коментарний каркас за логіями"
    if marker not in text:
        raise SystemExit(f"Cannot find {marker!r} in {UK_APPENDIX}")
    body = text.split(marker, 1)[1].strip()
    body = remove_sections(body, {"### Джерела й контрольні файли", "### Що треба допрацювати"})
    body = sanitize_paper_text(body, lang="uk")
    return "### Повний коментований додаток до 114 логій\n\n" + body


def extract_en_appendix_for_paper() -> str:
    if not EN_APPENDIX.exists():
        return ""
    text = sanitize_paper_text(read(EN_APPENDIX), lang="en")
    return "### Full 114-Logion Commentary Appendix\n\n" + text


def remove_sections(text: str, headings_to_remove: set[str]) -> str:
    lines = text.splitlines()
    result: list[str] = []
    skip = False
    for line in lines:
        if line.startswith("### "):
            skip = line.strip() in headings_to_remove
            if skip:
                continue
        elif line.startswith("## "):
            skip = False
        if not skip:
            result.append(line.rstrip())
    return "\n".join(result)


def normalize_clean_headings(clean: str, lang: str) -> str:
    if lang == "uk":
        return clean
    return clean


def assemble_uk() -> str:
    return "\n\n".join(
        [
            "# Реконструкція найдавнішого Євангелія висловів",
            "## Чистий текст реконструкції",
            normalize_clean_headings(read(UK_CLEAN), "uk"),
            "## Як читати це видання",
            (
                "Перший читацький шар - це тільки чистий реконструйований текст. "
                "Номери логій збережено за загальноприйнятою нумерацією Євангелія від Фоми, "
                "щоб читач міг легко перейти до відповідного розділу додатка. "
                "Коментар не є частиною самого реконструйованого тексту."
            ),
            extract_uk_appendix_for_paper(),
            PRINT_BIBLIOGRAPHY_UK.strip(),
        ]
    ) + "\n"


def assemble_en() -> str:
    dossier = sanitize_paper_text(read(EN_DOSSIER), lang="en")
    appendix = extract_en_appendix_for_paper()
    appendix_or_note = appendix or (
        "### Evidence Dossier And Methodological Defense\n\n"
        + dossier
    )
    return "\n\n".join(
        [
            "# A Reconstruction of the Earliest Sayings Gospel",
            "## Clean Reconstructed Text",
            normalize_clean_headings(read(EN_CLEAN), "en"),
            "## How To Read This Edition",
            (
                "The first reader-facing layer is the clean reconstructed text only. "
                "The logion numbers follow the conventional Gospel of Thomas numbering. "
                "The commentary appendix covers all 114 logia so readers can compare included, uncertain, deferred, appendix-only, and excluded material without relying on clickable links."
            ),
            appendix_or_note,
            "### Evidence Dossier And Methodological Defense",
            dossier,
            PRINT_BIBLIOGRAPHY_EN.strip(),
        ]
    ) + "\n"


def assemble_digital() -> str:
    sections = [
        "# EUAGELIA Digital Scholarly Companion Source",
        "",
        "This source preserves the full apparatus map for digital use. Repository paths are allowed here by design.",
        "",
        "## Paper Outputs",
        "",
        "- output/uk-paper-book/book-source-uk-full.md",
        "- output/en-paper-book/book-source-en-full.md",
        "- output/uk-paper-book/euagelia-uk-full-proof.pdf",
        "- output/en-paper-book/euagelia-en-full-proof.pdf",
        "",
        "## Core Corpus",
        "",
        "- corpus/cards/",
        "- corpus/tables/logia-workflow-matrix.md",
        "- reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-uk.md",
        "- reconstruction/earliest-sayings-gospel/evidence-dossier-en.md",
        "",
        "## Language Layers",
        "",
        "- reconstruction/earliest-sayings-gospel/reconstructed-gospel-uk.md",
        "- reconstruction/earliest-sayings-gospel/reconstructed-gospel-en.md",
        "- reconstruction/earliest-sayings-gospel/reconstructed-gospel-coptic.md",
        "- reconstruction/earliest-sayings-gospel/reconstructed-gospel-greek.md",
        "- reconstruction/earliest-sayings-gospel/parallel-edition.md",
        "",
        "## Rights And Bibliography",
        "",
        "- bibliography/bibliography-working.md",
        "- bibliography/source-rights-register.md",
        "- project/rights-and-citation-policy.md",
        "- project/source-reproducibility-note.md",
    ]
    return "\n".join(sections) + "\n"


def main() -> None:
    UK_OUT.parent.mkdir(parents=True, exist_ok=True)
    EN_OUT.parent.mkdir(parents=True, exist_ok=True)
    DIGITAL_OUT.parent.mkdir(parents=True, exist_ok=True)
    UK_OUT.write_text(assemble_uk(), encoding="utf-8")
    EN_OUT.write_text(assemble_en(), encoding="utf-8")
    sys.path.insert(0, str(ROOT / "tools"))
    try:
        from generate_digital_companion import main as generate_digital_companion
    except Exception:
        DIGITAL_OUT.write_text(assemble_digital(), encoding="utf-8")
    else:
        generate_digital_companion()
    for path in (UK_OUT, EN_OUT, DIGITAL_OUT):
        print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
