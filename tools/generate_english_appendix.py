#!/usr/bin/env python3
"""Generate the first complete English 114-logion commentary appendix.

The generator is intentionally conservative. It builds a print-safe English
appendix from the frozen all-114 decision table and the frozen English clean
reader. It does not change the reconstruction; it creates the missing English
paper-facing commentary layer that can later receive a literary copyedit.
"""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DECISIONS = ROOT / "reconstruction/earliest-sayings-gospel/all-114-publication-decision-table-v0.1.md"
EN_CLEAN = ROOT / "reconstruction/earliest-sayings-gospel/reconstructed-gospel-en.md"
OUT = ROOT / "reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-en.md"


STATUS_LABELS = {
    "READER_INCLUDE_MARKED": "included in the clean reconstruction with an apparatus marker",
    "APPENDIX_ONLY_STABLE": "kept in the appendix as important but not printed in the clean reconstruction",
    "APPENDIX_ONLY_UNCERTAIN": "kept in the appendix as unresolved material",
    "DEFER_TO_CLUSTER": "deferred to a thematic or source cluster before any future reader decision",
    "DEFER_TO_CLUSTER_BEFORE_READER_DECISION": "deferred to cluster review before any reader decision",
    "PROMOTE_TO_CONTROLLED_READER_CANDIDATE_PASS": "promoted for a controlled reader-candidate review",
    "EXCLUDE_AS_SECONDARY": "excluded from the earliest reconstructed reader as secondary",
    "NEEDS_EVIDENCE_BEFORE_FINAL": "requires evidence work before final publication",
    "APPENDIX_ONLY_STABLE; full logion appendix-only": "kept in the appendix as important but not printed in the clean reconstruction",
}


SPECIAL_MEANINGS = {
    "1": "This opening saying functions like a doorway into the whole collection. It tells the reader that the sayings are not merely to be stored in memory; they have to be interpreted. The promise of not tasting death is therefore best read as a claim about life opened by understanding, not as a simple promise of biological escape.",
    "2": "This saying describes searching as a process that unsettles the seeker. Finding does not immediately produce calm; it produces shock, amazement, and a new stance before reality. That is why the final verbs matter so much for reconstruction.",
    "3": "This logion rejects the idea that the kingdom is a faraway location. It turns the question inward and outward at once: the decisive recognition concerns the self, the world, and one's relation to the living Father.",
    "6": "The clean reader preserves only the short ethical core: do not lie, and do not do what you hate. The surrounding ritual and question-answer frame is left in the appendix because it is more compositionally complex.",
    "21": "This is a composite watchfulness and harvest text. Its thief motif is important for understanding Logion 103, but the full logion gathers several images into one larger Thomasine composition.",
    "45": "The reconstructed reader uses the fruit-tree core. The heart-treasure material is important, but the project keeps it in the appendix because the full logion combines related but separable moral images.",
    "63": "This is the rich-fool warning: a person plans future abundance, but death arrives before the plan can be enjoyed. The saying is powerful, but its closeness to Luke means the apparatus has to keep dependence risk visible.",
    "90": "This is one of the attractive non-reader cases. Its invitation to rest is beautiful and theologically rich, but the wording is so close to Matthew 11:28-30 that this edition keeps it outside the earliest reconstructed text.",
    "103": "Only the brief thief/watchfulness core is printed in the clean reader. The fuller Thomasine form remains appendix material because it expands the image into a wider scene of preparation and defense.",
    "104": "This saying has strong Gospel parallels around fasting and the bridegroom, but the Thomasine version is tied to ritual and bridal-chamber language. That makes it too entangled for clean extraction in this edition.",
    "114": "This final scene is the clearest exclusion case. It stages Mary, Peter, and gender transformation in a way that looks like later community-boundary discourse rather than an early sayings-gospel unit.",
}


THEME_HINTS = [
    (("search", "find", "seek", "knock"), "It belongs to the search/find family: the issue is not possession of a doctrine, but the movement from seeking toward recognition."),
    (("kingdom",), "It belongs to the kingdom-sayings field: the question is how God's reign is recognized, entered, embodied, or misunderstood."),
    (("poor", "wealth", "rich", "money", "merchant", "treasure", "pearl", "inheritance"), "It belongs to the wealth and renunciation field: the saying tests the relation between possessions, desire, loss, and freedom."),
    (("father", "mother", "brother", "family", "household"), "It belongs to the family and discipleship field: kinship language is used to redefine loyalty, identity, and belonging."),
    (("fire",), "It belongs to the fire/kingdom field: fire can signal crisis, judgment, purification, or the disruptive arrival of the message."),
    (("child", "children", "infant"), "It belongs to the child/kingdom field: smallness, origin, and receptivity become ways of speaking about entry into life."),
    (("hidden", "revealed", "light", "lamp"), "It belongs to the hidden/revealed field: the saying asks how truth moves from concealment into visibility."),
    (("body", "soul", "corpse", "flesh"), "It belongs to the body/soul field: the saying reflects on embodied life, mortality, and the risk of misreading the human person."),
    (("death", "living", "life"), "It belongs to the life/death field: the question is what kind of life overcomes ordinary death-bound existence."),
    (("thief", "watch"), "It belongs to the watchfulness field: the force of the saying lies in readiness before crisis becomes visible."),
    (("sower", "seed", "mustard", "leaven", "harvest", "vineyard", "tenants", "sheep"), "It belongs to the parable field: ordinary rural or household images are used to make a claim about recognition, growth, judgment, or loss."),
    (("mary", "peter", "woman", "male"), "It belongs to the gender/community-boundary field: the issue is not only gendered language, but the later community logic implied by the scene."),
]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def strip_paths(text: str) -> str:
    text = re.sub(r"`[^`]*(?:corpus|reconstruction|project|sources|controls|notes|output)/[^`]*`", "local research apparatus", text)
    text = re.sub(r"(?:corpus|reconstruction|project|sources|controls|notes|output)/[\w./-]+", "local research apparatus", text)
    text = text.replace("`", "")
    return text


def parse_clean_reader() -> dict[str, str]:
    text = read(EN_CLEAN)
    result: dict[str, list[str]] = {}
    current: str | None = None
    for line in text.splitlines():
        match = re.match(r"^## Logion (\d+[A-Z]?)$", line.strip())
        if match:
            current = match.group(1)
            result[current] = []
            continue
        if current and line.strip():
            result[current].append(line.strip())
    return {num: "\n\n".join(lines) for num, lines in result.items()}


def parse_decisions() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    headers: list[str] | None = None
    in_table = False
    for line in read(DECISIONS).splitlines():
        if line.startswith("| Logion | Unit | Publication Status |"):
            headers = [cell.strip() for cell in line.strip().strip("|").split("|")]
            in_table = True
            continue
        if not in_table:
            continue
        if line.startswith("| ---"):
            continue
        if not line.startswith("|"):
            if rows:
                break
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if headers and len(cells) == len(headers) and re.fullmatch(r"\d+", cells[0]):
            rows.append(dict(zip(headers, cells)))
    if len(rows) != 114:
        raise SystemExit(f"Expected 114 decision rows, found {len(rows)}")
    return rows


def clean_status(status: str) -> str:
    status = status.replace("`", "")
    if status == "DEFER_TO_CLUSTER; thief subunit control material":
        return "deferred as a full logion; the thief subunit is used as control material"
    if status.startswith("104A "):
        return "104A kept appendix-only; full logion kept appendix-only"
    return STATUS_LABELS.get(status, status)


def theme_hint(unit: str) -> str:
    lower = unit.lower()
    for words, hint in THEME_HINTS:
        if any(word in lower for word in words):
            return hint
    return "It belongs to the wider sayings tradition where brief images and aphorisms carry more weight than narrative explanation."


def source_sentence(row: dict[str, str]) -> str:
    greek = row["Greek Status"]
    if "No loaded P.Oxy" in greek:
        return "For this edition the complete Coptic witness carries the main textual burden; no loaded Oxyrhynchus Greek witness is available for this logion."
    if "retroversion" in greek.lower():
        return "The Greek layer here is a controlled hypothetical retroversion, useful for comparison but not an extant manuscript witness."
    if "partial" in greek.lower() or "lacunose" in greek.lower() or "fragment" in greek.lower():
        return "The Greek evidence gives valuable material control, but it is fragmentary or lacunose and must not be treated as a complete independent form."
    return "The logion has loaded Greek papyrus control in this edition, which gives it more than Coptic-only support while still leaving room for textual caution."


def obligation_sentence(text: str) -> str:
    text = strip_paths(text).strip()
    replacements = {
        "Explain included core, excluded/full-form material, Greek status, and uncertainty marker.": "The appendix therefore separates the printed core from the fuller received form and keeps the Greek status visible.",
        "Explain why tradition is important but appendix-only under current model.": "The appendix therefore explains why the tradition matters even though it is not printed in the clean reconstruction.",
        "Explain why the tradition is important but appendix-only as a full logion under current model.": "The appendix therefore explains why the tradition matters while the full logion remains outside the clean reconstruction.",
        "Use appendix to explain source state, interpretive range, and reason for non-inclusion.": "The appendix therefore gives the source state, interpretive range, and reason for non-inclusion.",
        "Use new Package A evidence rationale to explain non-inclusion; keep full discussion in appendix.": "The appendix therefore keeps the evidence rationale visible and treats non-inclusion as an argued decision.",
        "Use new Package B evidence rationale to explain non-inclusion; keep full discussion in appendix.": "The appendix therefore keeps the evidence rationale visible and treats non-inclusion as an argued decision.",
        "Keep appendix-only while documenting partial \"not taste death\" formula control.": "The appendix therefore preserves the partial deathlessness control without promoting the whole logion.",
        "Explain the four subunits and why the full form is not printed.": "The appendix therefore distinguishes the subunits and explains why the full form is not printed.",
        "Explain why possible early family-renunciation core remains apparatus material and full logion is not printed.": "The appendix therefore keeps the possible early family-renunciation core as apparatus material rather than clean text.",
        "Explain why possible reversal wisdom remains apparatus material and full logion is not printed.": "The appendix therefore keeps possible reversal wisdom as apparatus material rather than clean text.",
        "Explain why thematic control through Logion 10/Luke 12:49 is not enough for clean-reader promotion.": "The appendix therefore explains why thematic fire control is not enough for clean-reader promotion.",
        "Explain why strong tradition can remain appendix-only when already represented by a stronger reader unit.": "The appendix therefore explains why a strong tradition can remain appendix-only when the motif is already represented by a stronger reader unit.",
        "Explain why Logion 2 is included while 92 and 94 remain appendix-only.": "The appendix therefore explains why Logion 2 represents the search/find motif in the clean reader while Logia 92 and 94 remain appendix-only.",
        "Explain why the core is strong but the full form is not printed.": "The appendix therefore explains why the short core is strong while the full received form remains outside the clean reader.",
        "Explain why this beatitude is included while related beatitudes remain appendix-only.": "The appendix therefore explains why this beatitude is printed while related beatitudes remain appendix-only.",
        "Explain why the full dialogue frame is not included.": "The appendix therefore separates the recognition-of-time core from the fuller dialogue frame.",
        "Explain included short core, excluded full-form material, no extant Greek Thomas witness, and relation to Logion 21.": "The appendix therefore separates the short watchfulness core from the fuller Thomasine expansion and relates it to Logion 21.",
        "Explain strong synoptic control, dependence risk, and Thomasine ritual/bridal-chamber risk.": "The appendix therefore names both the strong synoptic control and the dependence or ritual-frame risk.",
        "Split controlled heaven/earth formula from weaker deathlessness/world-unworthy material in appendix.": "The appendix therefore separates the more controlled heaven/earth formula from weaker deathlessness and world-unworthy material.",
        "Use as transparent exclusion case with full rationale.": "The appendix therefore uses this logion as a transparent case study in exclusion.",
    }
    return replacements.get(text, text)


def what_about(row: dict[str, str]) -> str:
    num = row["Logion"]
    if num in SPECIAL_MEANINGS:
        return SPECIAL_MEANINGS[num]
    unit = row["Unit"]
    return (
        f"This section concerns the {unit}. "
        f"{theme_hint(unit)} "
        "For a paper reader, the first question is simple: what does this saying ask a person to notice, practice, reject, or reinterpret?"
    )


def why_decision(row: dict[str, str]) -> str:
    status = row["Publication Status"].replace("`", "")
    rationale = strip_paths(row["Primary Rationale"])
    obligation = obligation_sentence(row["Appendix Obligation"])
    if "READER_INCLUDE_MARKED" in status:
        return (
            f"The project prints this unit because it has enough early-profile value to represent part of the reconstructed sayings gospel. "
            f"It is still marked because the received Thomasine form, the Greek evidence, or the relation to parallels remains complicated. {rationale} {obligation}"
        )
    if "EXCLUDE_AS_SECONDARY" in status:
        return (
            f"The project excludes this logion from the clean reconstruction because it most likely belongs to a later interpretive or community-shaping layer. "
            f"It is still discussed fully because exclusion must be argued, not hidden. {rationale} {obligation}"
        )
    if "APPENDIX_ONLY_STABLE" in status:
        return (
            f"The project keeps this logion in the appendix because it is meaningful and controlled, but not strong enough to stand in the main reconstructed text for this edition. "
            f"In other words, it matters for understanding the tradition even though it is not counted as part of the earliest recoverable layer. {rationale} {obligation}"
        )
    if "APPENDIX_ONLY_UNCERTAIN" in status:
        return (
            f"The project keeps this logion outside the clean text because the early element, if present, cannot yet be separated securely from transmission history or later interpretation. "
            f"The appendix preserves the question rather than forcing a premature decision. {rationale} {obligation}"
        )
    return (
        f"The project defers this logion because it is best judged together with related sayings, source controls, or thematic clusters. "
        f"Deferral is not dismissal; it means the evidence is not yet clean enough for a stronger reader decision. {rationale} {obligation}"
    )


def text_layer(row: dict[str, str], clean_reader: dict[str, str]) -> str:
    num = row["Logion"]
    unit = row["Unit"]
    if row["Clean Reader"] == "YES":
        key = num
        if num == "45":
            key = "45"
        elif num == "46":
            key = "46"
        elif num == "47":
            key = "47"
        elif num == "91":
            key = "91"
        elif num == "103":
            key = "103"
        text = clean_reader.get(key)
        if text:
            quoted = "\n>\n> ".join(text.split("\n\n"))
            return (
                "This logion, or a controlled core within it, is printed in the clean English reconstruction:\n\n"
                f"> {quoted}\n\n"
                f"The printed unit is the project's current reconstruction of the {unit}. The appendix must still be read with the marker: inclusion does not mean that every word of the received Thomasine form is equally early."
            )
    return (
        "No clean-reader text is printed for this logion in the current English reconstruction. "
        "The logion remains visible here so that readers can see the evidence, the interpretive value, and the reason why it was not allowed into the main reconstructed text."
    )


def reader_interpretation(row: dict[str, str]) -> str:
    status = row["Publication Status"].replace("`", "")
    unit = row["Unit"]
    rationale = strip_paths(row["Primary Rationale"])
    confidence = row["Confidence"]
    if "READER_INCLUDE_MARKED" in status:
        return (
            f"In plain terms, this section treats the {unit} as a real candidate for the earliest reachable sayings-gospel layer, but not as an unmarked certainty. "
            f"The reader should first ask what experience the saying names, then ask how much of the received form can bear historical weight. "
            f"The current confidence level is {confidence}. {rationale}"
        )
    if "EXCLUDE_AS_SECONDARY" in status:
        return (
            f"This logion is important precisely because it shows a boundary of the reconstruction. "
            f"It may reveal later theological, communal, or editorial development, but the present project does not treat it as part of the earliest reconstructed sayings-gospel. "
            f"The current confidence level is {confidence}. {rationale}"
        )
    if "APPENDIX_ONLY_STABLE" in status:
        return (
            f"This logion is stable enough to discuss, but not strong enough to print in the clean reconstruction. "
            f"It may preserve an important Thomasine tradition, a later adaptation of an early motif, or a useful control for another logion. "
            f"The current confidence level is {confidence}. {rationale}"
        )
    if "APPENDIX_ONLY_UNCERTAIN" in status:
        return (
            f"This logion remains open. It may contain an early element, but the present evidence does not yet let us separate early core, transmission history, and later interpretation with enough confidence. "
            f"The current confidence level is {confidence}. {rationale}"
        )
    return (
        f"This logion is best read in relation to a wider cluster before any stronger reader decision is made. "
        f"It is not being hidden or discarded; it is held in the appendix so the reader can follow the unresolved evidence. "
        f"The current confidence level is {confidence}. {rationale}"
    )


def interpretation_options(row: dict[str, str]) -> list[str]:
    unit = row["Unit"]
    greek = row["Greek Status"]
    clean = row["Clean Reader"] == "YES"
    options = [f"Early-core reading: the {unit} may preserve a compact saying or motif that circulated before later literary framing."]
    lower = unit.lower()
    if any(word in lower for word in ["kingdom", "father", "life", "living"]):
        options.append("Theological reading: the saying may be less about institution or doctrine than about a transformed way of recognizing God, life, and the self.")
    elif any(word in lower for word in ["rich", "money", "wealth", "treasure", "pearl", "merchant"]):
        options.append("Renunciation reading: the saying may expose how possession promises security while actually binding the person to anxiety, status, or loss.")
    elif any(word in lower for word in ["family", "mother", "father", "brother", "household"]):
        options.append("Discipleship reading: the saying may redefine kinship around obedience, insight, or loyalty rather than blood relation.")
    elif any(word in lower for word in ["sower", "seed", "leaven", "mustard", "sheep", "harvest"]):
        options.append("Parabolic reading: the saying uses an ordinary image to make the reader reason from visible life toward hidden meaning.")
    elif any(word in lower for word in ["hidden", "revealed", "light", "lamp"]):
        options.append("Revelatory reading: the saying treats hiddenness as temporary and asks what sort of perception makes disclosure possible.")
    else:
        options.append("Wisdom reading: the saying may work as a compact challenge that forces the reader to rethink an ordinary assumption.")
    options.append("Editorial reading: the received Thomas form may have expanded, combined, or reframed an older unit in a way that now requires caution.")
    if not clean:
        options.append("Appendix-only reading: the logion can still illuminate the tradition even when it is not printed as part of the reconstructed main text.")
    if "No loaded P.Oxy" in greek:
        options.append("Source-caution reading: without a loaded Oxyrhynchus Greek witness, the Coptic witness carries the main textual weight for this edition.")
    elif "retroversion" in greek.lower():
        options.append("Greek-layer caution: the Greek wording used for comparison is hypothetical retroversion, not an extant manuscript witness.")
    else:
        options.append("Greek-witness reading: extant or partial Oxyrhynchus evidence gives this logion an additional material control, though fragmentary text still requires caution.")
    return options


def build_appendix() -> str:
    clean_reader = parse_clean_reader()
    rows = parse_decisions()
    lines = [
        "# Full 114-Logion Commentary Appendix",
        "",
        "## How To Use This Appendix",
        "",
        "The clean reconstructed text is the first layer of the book. This appendix is the second layer. It explains why each conventional Gospel of Thomas logion is included, marked, deferred, kept appendix-only, or excluded from the earliest reconstructed sayings-gospel.",
        "",
        "The appendix covers all 114 logia, including rejected and uncertain material. Non-inclusion is not concealment: it is part of the argument. The reader should be able to find any logion by its conventional number and see the present state of the evidence.",
        "",
        "Greek status means the status of loaded Greek Thomas papyrus evidence for this edition. A hypothetical Greek retroversion is never treated as an extant manuscript witness.",
        "",
    ]
    for row in rows:
        num = row["Logion"]
        lines.extend(
            [
                f"## Logion {num}",
                "",
                "### Reconstruction Status",
                "",
                f"- Reader status: {clean_status(row['Publication Status'])}.",
                f"- Clean reader: {'yes' if row['Clean Reader'] == 'YES' else 'no'}.",
                f"- Confidence: {row['Confidence']}.",
                f"- Greek witness status: {strip_paths(row['Greek Status'])}.",
                "",
                "### What This Saying Is About",
                "",
                what_about(row),
                "",
                "### Text In This Edition",
                "",
                text_layer(row, clean_reader),
                "",
                "### Sources And Controls",
                "",
                f"Primary source/control summary: {strip_paths(row['Evidence / Control'])}.",
                "",
                f"{source_sentence(row)} Coptic NHC II,2 remains the complete manuscript base for the received Thomas text; P.Oxy. 1, P.Oxy. 654, and P.Oxy. 655 are used where this project's loaded evidence supplies extant or partial Greek control. Canonical Greek parallels are controls, not Thomas witnesses.",
                "",
                "### Why It Is Or Is Not In The Reconstruction",
                "",
                why_decision(row),
                "",
                "### Possible Interpretations",
                "",
            ]
        )
        for idx, option in enumerate(interpretation_options(row), 1):
            lines.append(f"{idx}. {option}")
        lines.extend(
            [
                "",
                "### Uncertainty And Limits",
                "",
                f"Before final publication this logion should be read with the following limit in view: {strip_paths(row['Next Action Before Final Freeze'])}",
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    OUT.write_text(build_appendix(), encoding="utf-8")
    print(OUT.relative_to(ROOT))


if __name__ == "__main__":
    main()
