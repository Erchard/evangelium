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
GREEK_CLEAN = ROOT / "reconstruction/earliest-sayings-gospel/reconstructed-gospel-greek-clean.md"
GREEK_MAJUSCULE_CLEAN = ROOT / "reconstruction/earliest-sayings-gospel/reconstructed-gospel-greek-majuscule-clean.md"
UK_APPENDIX = ROOT / "reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-uk.md"
EN_APPENDIX = ROOT / "reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-en.md"
EN_DOSSIER = ROOT / "reconstruction/earliest-sayings-gospel/evidence-dossier-en.md"

UK_OUT = ROOT / "output/uk-paper-book/book-source-uk-full.md"
EN_OUT = ROOT / "output/en-paper-book/book-source-en-full.md"
DIGITAL_OUT = ROOT / "output/digital-scholarly-companion/companion-source-full.md"
UK_READER_HEADING = "## Логії Ісуса"

PAPER_STATUS_TERMS_UK = {
    "INCLUDE_WITH_MARKER": "включено обережно",
    "EXCLUDE_AS_SECONDARY": "виключено як вторинне",
    "DEFER_TO_CLUSTER": "відкладено до кластерного рішення",
    "KEEP_APPENDIX_ONLY_FOR_NOW": "залишено тільки в додатку",
    "APPENDIX_ONLY_UNCERTAIN": "тільки додаток, непевно",
    "UNCERTAIN": "непевно",
    "DEFER": "відкладено",
    "FRAME_INCLUDED_WITH_MARKER": "рамка включена обережно",
}


PRINT_BIBLIOGRAPHY_UK = """## Бібліографія і права

### Друковані ключі джерел

- NHC II,2 - коптський рукопис Євангелія від Фоми в Nag Hammadi Codex II, tractate 2.
- P.Oxy. 1; P.Oxy. 654; P.Oxy. 655 - грецькі оксиринхські папіруси, використані через відкритий папірусний каталог DCLP / Papyri.info.
- SBLGNT - відкритий грецький контроль канонічних паралелей; не свідок Фоми.
- Mattison Thomas - відкритий англійський переклад Євангелія від Фоми; допоміжна перевірка змісту, не база реконструкції.
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
    text = re.sub(r";?\s*локальний робочий текст:\s*`[^`]+`", "", text)
    text = re.sub(r";?\s*[ув] проекті використано локальний робочий текст\s*`[^`]+`", "", text)
    text = re.sub(r";?\s*[ув] проекті використано локальний робочий текст\s*(?:`[^`]+`)?\s*\.{0,2}", "", text)
    text = re.sub(r";?\s*локальний робочий текст\s*(?:`[^`]+`)?\s*\.{0,2}", "", text)
    text = re.sub(r"`[^`]*(?:corpus|reconstruction|project|sources|controls|notes|output)/[^`]*`", "", text)
    if lang == "uk":
        text = normalize_uk_reader_caution_language(text)
    text = re.sub(r"\s+\n", "\n", text)
    lines = []
    for line in text.splitlines():
        stripped = line.strip()
        if re.search(r"(?:corpus|reconstruction|project|sources|controls|notes|output)/", stripped):
            continue
        if stripped.startswith("Evidence note:"):
            continue
        if stripped.startswith("- Reader status:"):
            continue
        if stripped.startswith("- Confidence:"):
            continue
        if stripped.startswith("Before final publication"):
            continue
        if stripped.startswith("Current clean-reader unit:"):
            continue
        if stripped.startswith("Review:"):
            continue
        if stripped.startswith("Synoptic controls:"):
            continue
        if stripped.startswith("Synoptic/control file:"):
            continue
        if "DCLP XML" in stripped:
            continue
        if "квадратні дужки позначають" in stripped:
            continue
        if "square brackets mark" in stripped:
            continue
        if "supplied lost text" in stripped:
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
        if lang == "en":
            line = normalize_en_reader_caution_language(line)
        lines.append(line)
    return "\n".join(lines).strip()


def normalize_en_reader_caution_language(text: str) -> str:
    replacements = {
        "clean reader": "main text",
        "Clean reader": "Main text",
        "clean-reader": "main-text",
        "appendix-only": "appendix only",
        "project's current reconstruction": "this edition's current reconstruction",
        "The project prints this unit because": "This edition includes this unit because",
        "The project keeps this logion in the appendix because": "This edition keeps this logion in the appendix because",
        "The project defers this logion because": "This edition defers this logion because",
        "the project's": "this edition's",
        "The project": "This edition",
        "the project": "this edition",
        "The appendix must still be read with the marker: inclusion does not mean that every word of the received Thomasine form is equally early.": "The commentary therefore explains that inclusion does not make every word of the received Thomasine form equally early.",
        "It is still marked because": "The caution remains because",
        "marked core": "cautiously included core",
        "marked expansion": "cautious expansion",
        "marked units": "cautiously included units",
        "marked unit": "cautiously included unit",
        "marked because": "treated cautiously because",
        "with an apparatus marker": "with an explanatory caution in the commentary",
        "with marker": "with caution",
        "the marker": "the caution",
        "marked": "cautious",
        "marker": "caution",
        "source file": "source witness",
        "repo path": "repository path",
        "DCLP XML": "DCLP / Papyri.info catalog",
        "working text": "working transcription",
        "INCLUDE_WITH_MARKER": "included with caution",
        "UNCERTAIN": "uncertain",
        "DEFER_TO_CLUSTER": "deferred to cluster review",
        "KEEP_APPENDIX_ONLY_FOR_NOW": "kept in the appendix",
        "APPENDIX_ONLY_STABLE": "kept in the appendix with a stable rationale",
        "APPENDIX_ONLY_UNCERTAIN": "kept in the appendix as uncertain",
        "DEFER": "deferred",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def normalize_uk_reader_caution_language(text: str) -> str:
    """Replace internal marker/status language with reader-facing wording."""
    replacements = {
        "Логію включено з маркером, бо": "Логію включено до реконструкції обережно, бо",
        "Логія включена з маркером, бо": "Логію включено до реконструкції обережно, бо",
        "Коротке ядро включено з маркером, бо": "Коротке ядро включено до реконструкції обережно, бо",
        "Коротке ядро включене з маркером, бо": "Коротке ядро включено до реконструкції обережно, бо",
        "Етичне ядро включено з маркером, бо": "Етичне ядро включено до реконструкції обережно, бо",
        "Саме тому логія включена з маркером.": "Саме тому логію включено до реконструкції обережно.",
        "Саме тому логія включена тільки з маркером.": "Саме тому логію включено до реконструкції лише обережно.",
        "логія включена з маркером": "логію включено до реконструкції обережно",
        "логію включено з маркером": "логію включено до реконструкції обережно",
        "включене з маркером": "включене до реконструкції обережно",
        "включено з маркером": "включено до реконструкції обережно",
        "входить до реконструкції з маркером": "входить до реконструкції обережно",
        "входить до clean reader з маркером": "входить до основного тексту обережно",
        "з маркером у другому шарі": "із поясненням у додатку",
        "до реконструкції з маркером": "до реконструкції обережно",
        "друкувати з маркером": "друкувати з поясненим застереженням",
        "з обережним маркером": "з поясненим застереженням",
        "з чітким маркером непевності": "з чітким поясненням непевності",
        "композиційного маркера": "пояснення складеної будови",
        "маркованим ядром": "обережно відділеним ядром",
        "марковане ядро": "обережно відділене ядро",
        "марковане.": "обережне.",
        "маркера і відкритого пояснення": "застереження і відкритого пояснення",
        "маркер потрібен": "потрібне застереження",
        "маркер обов'язковий": "застереження обов'язкове",
        "маркером обережності": "ознакою, що потрібна обережність",
        "має маркер": "потребує поясненого застереження",
        "Маркер потрібен": "Застереження потрібне",
        "з застереженняом": "із застереженням",
        "коптському робочому тексті": "коптській версії",
        "локальна коптська робоча транскрипція": "коптська транскрипція",
        "потребує повторної звірки з XML і виданнями": "потребує повторної звірки з папірусною транскрипцією і друкованими виданнями",
        "DCLP TEI": "папірусний каталог",
        "DCLP / Papyri.info XML-шар": "відкритий папірусний каталог DCLP / Papyri.info",
        "у проекті": "у цьому виданні",
        "У проекті": "У цьому виданні",
        "для проекту": "для цього видання",
        "Для проекту": "Для цього видання",
        "проект вважає": "це видання вважає",
        "проект відповідально включає": "це видання відповідально включає",
        "проект включає": "це видання включає",
        "проект не виключає": "це видання не виключає",
        "проект не друкує": "це видання не друкує",
        "проект лишає": "це видання лишає",
        "проект залишає": "це видання залишає",
        "нашому проекті": "цьому виданні",
        "цьому проекті": "цьому виданні",
        "clean reader": "основний текст",
        "Clean reader": "Основний текст",
        "appendix-only": "лише для додатку",
        "APPENDIX_ONLY": "лише для додатку",
        "Review C": "попередній контрольний перегляд",
        "high early pressure": "сильний ранній потенціал",
        "evidence profile dominated by": "доказовий профіль переважно залежить від",
        "collectional doublet": "збірковий дублет",
        "collection-memory expansion": "збіркове розширення пам'яті",
        "parable memory": "пам'ять про притчу",
        "kingdom-of-Father ending": "завершення про царство Отця",
        "lamp unit": "підодиниця про лампу",
        "composite форма": "складена форма",
        "Greek свідка": "грецького свідка",
        "Greek контроль": "грецький контроль",
        "canonical Greek контроль": "канонічний грецький контроль",
        "canonical Greek": "канонічний грецький",
        "synoptic контроль": "синоптичний контроль",
        "direct synoptic": "прямий синоптичний",
        "evidence note": "доказова примітка",
        "Evidence note": "Доказова примітка",
        "publication apparatus": "друкований апарат",
        "print edition": "друкованому виданні",
        "scriptural-anthropological reflection": "біблійно-антропологічним роздумом",
        "scriptural interpretation": "біблійне тлумачення",
        "scriptural reflection": "біблійний роздум",
        "scriptural Greek": "грецький текст біблійної цитати",
        "synoptic tenants tradition": "синоптичної традиції про виноградарів",
        "one-source Matthean контроль": "контроль лише через Матвія",
        "direct control": "прямого контролю",
        "anti-usury law": "заборона лихварства",
        "radical generosity": "радикальна щедрість",
        "bridal-chamber": "шлюбної кімнати",
        "bridal chamber": "шлюбна кімната",
        "broad bridal/door thematic control": "широкою тематичною паралеллю про весільну кімнату і двері",
        "Маркер все одно потрібен": "Застереження все одно потрібне",
        "Рішення рішення відкладене": "Рішення відкладене",
        "Через це це видання": "Через це видання",
        "у нашій реконструкції": "у цій реконструкції",
        "У нас немає": "Немає",
        "у проекті немає": "немає",
        "У проекті немає": "Немає",
        "для цієї логії в проекті немає": "для цієї логії немає",
        "Для звичайного церковного читача тут важливо ": "Тут важливо ",
        "Для звичайного читача це ": "Це ",
        "Для сучасного читача ": "Сьогодні ",
        "Для паперового читача головні ": "Головні ",
        "Для читача головна думка може виглядати так: ": "Головна думка така: ",
        "Для читача головний сенс такий: ": "Головний сенс такий: ",
        "Для читача головний сенс простий: ": "Головний сенс простий: ",
        "Для читача головна сила притчі ": "Головна сила притчі ",
        "Для читача головне питання: ": "Головне питання: ",
        "Для читача тут важливо ": "Тут важливо ",
        "Для читача важливо ": "Важливо ",
        "Для читача сенс досить прозорий: ": "Сенс досить прозорий: ",
        "Для читача це може звучати як ": "Це може звучати як ",
        "Для читача це може бути ": "Це може бути ",
        "Для читача це ": "Це ",
        "Для читача її можна сприйняти як ": "Її можна сприйняти як ",
        "Для читача логія може звучати як ": "Логія може звучати як ",
        "Для читача логія може виглядати як ": "Логія може виглядати як ",
        "Для читача вислів може звучати як ": "Вислів може звучати як ",
        "Для читача вислів може бути ": "Вислів може бути ",
        "Для читача ця логія цінна тому, що ": "Ця логія цінна тим, що ",
        "Для читача коротке ядро дуже просте: ": "Коротке ядро дуже просте: ",
        "Для читача вона звучить сильно саме тому, що ": "Вона звучить сильно саме тому, що ",
        "Для читача її варто читати поруч із ": "Її варто читати поруч із ",
        "залишити читачеві чесний вибір": "залишити чесний вибір",
        "допомогти читачеві побачити": "допомогти побачити",
        "не дає читачеві прямої моралі": "не дає прямої моралі",
        "дає читачеві прозору картину": "дає прозору картину",
        "маркери -": "ознаки -",
        "маркери": "ознаки",
        "маркера": "застереження",
        "маркер": "застереження",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def extract_uk_appendix_for_paper() -> str:
    text = read(UK_APPENDIX)
    marker = "## Коментарний каркас за логіями"
    if marker not in text:
        raise SystemExit(f"Cannot find {marker!r} in {UK_APPENDIX}")
    body = text.split(marker, 1)[1].strip()
    body = remove_sections(body, {"### Джерела й контрольні файли", "### Що треба допрацювати"})
    body = remove_incomplete_english_translation_slots(body)
    body = sanitize_paper_text(body, lang="uk")
    return "## Повний коментований додаток до 114 логій\n\n" + body


def extract_en_appendix_for_paper() -> str:
    if not EN_APPENDIX.exists():
        return ""
    text = sanitize_paper_text(read(EN_APPENDIX), lang="en")
    return "## Full 114-Logion Commentary Appendix\n\n" + text


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


def remove_incomplete_english_translation_slots(text: str) -> str:
    """Keep print clean until the dedicated all-114 English translation pass is done."""
    lines = text.splitlines()
    result: list[str] = []
    index = 0
    placeholder = "English translation for this logion is scheduled"
    while index < len(lines):
        line = lines[index]
        if line.strip() == "### Англійський переклад":
            section: list[str] = [line]
            index += 1
            while index < len(lines) and not lines[index].startswith("### ") and not lines[index].startswith("## "):
                section.append(lines[index])
                index += 1
            if placeholder in "\n".join(section):
                continue
            result.extend(section)
            continue
        result.append(line)
        index += 1
    return "\n".join(result)


def normalize_clean_headings(clean: str, lang: str) -> str:
    if lang == "uk":
        return clean
    return clean


def clean_greek_reader_for_paper() -> str:
    text = read(GREEK_MAJUSCULE_CLEAN)
    text = re.sub(r"^# .+?\n+", "", text)
    return text.strip()


def assemble_uk() -> str:
    return "\n\n".join(
        [
            "# Реконструкція найдавнішого Євангелія висловів",
            UK_READER_HEADING,
            normalize_clean_headings(read(UK_CLEAN), "uk"),
            "## Реконструйований грецький текст",
            clean_greek_reader_for_paper(),
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
                "The commentary appendix covers all 114 logia so readers can compare included, uncertain, deferred, appendix only, and excluded material without relying on clickable links."
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
        "- reconstruction/earliest-sayings-gospel/reconstructed-gospel-greek-clean.md",
        "- reconstruction/earliest-sayings-gospel/reconstructed-gospel-greek-majuscule-clean.md",
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
