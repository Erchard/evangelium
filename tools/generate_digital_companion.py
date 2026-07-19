#!/usr/bin/env python3
"""Generate the EUAGELIA digital scholarly companion.

The paper books deliberately hide repository paths. This companion does the
opposite: it preserves the full research map so the reconstruction can be
audited logion by logion.
"""

from __future__ import annotations

import csv
import hashlib
import re
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output/digital-scholarly-companion"

MATRIX = ROOT / "corpus/tables/logia-workflow-matrix.md"
DECISION_TABLE = ROOT / "reconstruction/earliest-sayings-gospel/all-114-publication-decision-table-v0.1.md"

CORE_ARTIFACTS = [
    "README.md",
    "LICENSE.md",
    "project/final-product-specification.md",
    "project/print-and-digital-publication-architecture.md",
    "project/rights-and-citation-policy.md",
    "project/source-reproducibility-note.md",
    "project/open-task-prompt-queue-2026-07-18.md",
    "project/project-completion-roadmap.md",
    "project/digital-scholarly-companion-expansion-v0.1.md",
    "project/ide-codex-digital-companion-browsable-html-v0.1-prompt.md",
    "project/digital-companion-browsable-html-v0.1.md",
    "project/ide-codex-final-production-typesetting-copyedit-gate-v0.1-prompt.md",
    "corpus/tables/logia-workflow-matrix.md",
    "reconstruction/earliest-sayings-gospel/all-114-publication-decision-table-v0.1.md",
    "reconstruction/earliest-sayings-gospel/reconstructed-gospel-uk.md",
    "reconstruction/earliest-sayings-gospel/reconstructed-gospel-en.md",
    "reconstruction/earliest-sayings-gospel/reconstructed-gospel-coptic.md",
    "reconstruction/earliest-sayings-gospel/reconstructed-gospel-greek.md",
    "reconstruction/earliest-sayings-gospel/reconstructed-gospel-ar-quranic-register.md",
    "reconstruction/earliest-sayings-gospel/parallel-edition.md",
    "reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-uk.md",
    "reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-en.md",
    "reconstruction/earliest-sayings-gospel/evidence-dossier-en.md",
    "bibliography/bibliography-working.md",
    "bibliography/source-rights-register.md",
    "output/uk-paper-book/euagelia-uk-full-proof.pdf",
    "output/en-paper-book/euagelia-en-full-proof.pdf",
]

AUDIT_PATTERNS = [
    "project/*audit*.md",
    "project/*pass*.md",
    "project/*qa*.md",
    "project/*verify*.md",
    "reconstruction/earliest-sayings-gospel/*audit*.md",
    "reconstruction/earliest-sayings-gospel/*pass*.md",
    "reconstruction/earliest-sayings-gospel/*review*.md",
    "reconstruction/earliest-sayings-gospel/*rationale*.md",
    "corpus/cards/*audit*.md",
]


@dataclass(frozen=True)
class LogionRow:
    number: int
    card: str
    evidence_notes: list[str]
    controls: list[str]
    decision: str
    reader_text: str
    greek_status: str
    current_status: str
    next_action: str


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def parse_markdown_table(path: Path) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    headers: list[str] | None = None
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells):
            continue
        if headers is None:
            headers = cells
            continue
        if headers and len(cells) == len(headers):
            rows.append(dict(zip(headers, cells)))
    return rows


def logion_number_from_filename(path: Path) -> int | None:
    match = re.search(r"logion-(\d{3})", path.name)
    return int(match.group(1)) if match else None


def collect_evidence_notes(number: int) -> list[str]:
    notes_dir = ROOT / "reconstruction/earliest-sayings-gospel/notes"
    direct = sorted(notes_dir.glob(f"logion-{number:03d}-*"))
    if number in {65, 66}:
        direct += sorted(notes_dir.glob("logion-065-066-*"))
    return [rel(path) for path in sorted(set(direct))]


def control_matches_number(path: Path, number: int) -> bool:
    name = path.name
    if re.search(rf"logion-{number:03d}\b", name):
        return True
    for match in re.finditer(r"logia-([0-9-]+)-", name):
        values = [int(value) for value in match.group(1).split("-") if value.isdigit()]
        if number in values:
            return True
    return False


def collect_controls(number: int) -> list[str]:
    controls_dir = ROOT / "controls/synoptic-parallels"
    return [rel(path) for path in sorted(controls_dir.glob("*.md")) if control_matches_number(path, number)]


def collect_cluster_notes() -> list[str]:
    notes_dir = ROOT / "reconstruction/earliest-sayings-gospel/notes"
    return [rel(path) for path in sorted(notes_dir.glob("*cluster*.md"))]


def collect_decision_by_logion() -> dict[int, str]:
    decisions: dict[int, str] = {}
    for row in parse_markdown_table(DECISION_TABLE):
        key = row.get("Logion") or row.get("Unit") or ""
        match = re.search(r"\d+", key)
        if not match:
            continue
        number = int(match.group(0))
        status = row.get("Publication status") or row.get("Decision") or ""
        if status:
            decisions[number] = status
    return decisions


def collect_logion_rows() -> list[LogionRow]:
    decisions = collect_decision_by_logion()
    matrix_rows = parse_markdown_table(MATRIX)
    rows: list[LogionRow] = []
    for number in range(1, 115):
        matrix = next((row for row in matrix_rows if row.get("Logion") == str(number)), {})
        card = ROOT / f"corpus/cards/logion-{number:03d}.md"
        rows.append(
            LogionRow(
                number=number,
                card=rel(card),
                evidence_notes=collect_evidence_notes(number),
                controls=collect_controls(number),
                decision=decisions.get(number) or matrix.get("Decision", ""),
                reader_text=matrix.get("Reader text", ""),
                greek_status=matrix.get("Greek witness status", ""),
                current_status=matrix.get("Current status", ""),
                next_action=matrix.get("Next action", ""),
            )
        )
    return rows


def source_category(path: Path) -> str:
    text = rel(path)
    if "/coptic/" in text:
        return "Coptic / NHC II,2"
    if "/greek_poxy/" in text:
        if "poxy1" in text.lower() or "poxy-1" in text.lower():
            return "Greek P.Oxy. 1"
        if "654" in text:
            return "Greek P.Oxy. 654"
        if "655" in text:
            return "Greek P.Oxy. 655"
        if "5575" in text:
            return "Greek P.Oxy. 5575 control"
        return "Greek Oxyrhynchus"
    if "/translations/" in text:
        return "Translation control"
    if "/notes/" in text:
        return "Source verification notes"
    if "canonical" in text.lower() or "sblgnt" in text.lower():
        return "Canonical Greek control"
    return "Source corpus general"


def collect_source_inventory() -> list[tuple[str, str, int, str]]:
    paths = sorted((ROOT / "sources/primary_texts").rglob("*"))
    rows: list[tuple[str, str, int, str]] = []
    for path in paths:
        if path.is_file():
            rows.append((source_category(path), rel(path), path.stat().st_size, sha256(path)))
    return rows


def collect_audit_trail() -> list[tuple[str, str, int, str]]:
    paths: set[Path] = set()
    for pattern in AUDIT_PATTERNS:
        paths.update(ROOT.glob(pattern))
    rows = []
    for path in sorted(paths):
        if path.is_file():
            rows.append((rel(path), path.stat().st_size, sha256(path), path.read_text(encoding="utf-8", errors="ignore").splitlines()[0] if path.suffix == ".md" else ""))
    return rows


def write_tsv(path: Path, headers: list[str], rows: list[list[str | int]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t")
        writer.writerow(headers)
        writer.writerows(rows)


def write_machine_indexes(logia: list[LogionRow]) -> None:
    write_tsv(
        OUT / "logion-cross-reference-index.tsv",
        ["logion", "reader_text", "decision", "greek_status", "card", "evidence_notes", "controls", "current_status", "next_action"],
        [
            [
                row.number,
                row.reader_text,
                row.decision,
                row.greek_status,
                row.card,
                "; ".join(row.evidence_notes),
                "; ".join(row.controls),
                row.current_status,
                row.next_action,
            ]
            for row in logia
        ],
    )
    source_rows = collect_source_inventory()
    write_tsv(OUT / "source-witness-inventory.tsv", ["category", "path", "bytes", "sha256"], [list(row) for row in source_rows])
    checksum_paths = [ROOT / item for item in CORE_ARTIFACTS if (ROOT / item).exists()]
    write_tsv(
        OUT / "artifact-checksums.tsv",
        ["artifact", "bytes", "sha256"],
        [[rel(path), path.stat().st_size, sha256(path)] for path in checksum_paths],
    )
    audit_rows = collect_audit_trail()
    write_tsv(OUT / "audit-trail-index.tsv", ["path", "bytes", "sha256", "title"], [list(row) for row in audit_rows])


def link(path: str) -> str:
    return f"[`{path}`](../../{path})"


def compact_paths(paths: list[str], limit: int = 4) -> str:
    if not paths:
        return "None recorded"
    shown = ", ".join(link(path) for path in paths[:limit])
    if len(paths) > limit:
        shown += f", plus {len(paths) - limit} more in `logion-cross-reference-index.tsv`"
    return shown


def companion_markdown(logia: list[LogionRow]) -> str:
    reader_count = sum(1 for row in logia if row.reader_text == "YES")
    source_rows = collect_source_inventory()
    audit_rows = collect_audit_trail()
    cluster_notes = collect_cluster_notes()
    lines: list[str] = [
        "# EUAGELIA Digital Scholarly Companion",
        "",
        "Status: expanded digital scholarly companion v0.1, 2026-07-19.",
        "",
        "## How To Use This Companion",
        "",
        "This companion is the digital research layer behind the Ukrainian and English paper books. The paper books are intentionally clean and print-safe; this file intentionally preserves repository paths, evidence notes, source snapshots, control files, checksums, and audit history.",
        "",
        "For a normal reading experience, start with the paper books. For verification, start here and move logion by logion: card -> evidence note -> control files -> source witness inventory -> publication decision table.",
        "",
        "## Generated Machine Indexes",
        "",
        "- `output/digital-scholarly-companion/logion-cross-reference-index.tsv` - all 114 logia with cards, evidence notes, controls, decisions, Greek status, and next actions.",
        "- `output/digital-scholarly-companion/source-witness-inventory.tsv` - local source corpus inventory with categories and SHA256 checksums.",
        "- `output/digital-scholarly-companion/artifact-checksums.tsv` - checksums for core publication artifacts and paper proofs.",
        "- `output/digital-scholarly-companion/audit-trail-index.tsv` - major audit/pass/review files with checksums.",
        "",
        "## Clean-Reader Manifest",
        "",
        f"The frozen clean reader contains {reader_count} printed units. Reader membership is controlled by `reconstruction/earliest-sayings-gospel/final-clean-reader-freeze-v0.1.md` and synchronized by `tools/qa_crosscheck.py`.",
        "",
        "| Layer | Path | Role |",
        "| --- | --- | --- |",
        "| Ukrainian clean reader | `reconstruction/earliest-sayings-gospel/reconstructed-gospel-uk.md` | First paper-reader layer. |",
        "| English clean reader | `reconstruction/earliest-sayings-gospel/reconstructed-gospel-en.md` | English paper-reader layer. |",
        "| Coptic reader layer | `reconstruction/earliest-sayings-gospel/reconstructed-gospel-coptic.md` | Coptic source-facing layer for included units. |",
        "| Greek reader layer | `reconstruction/earliest-sayings-gospel/reconstructed-gospel-greek.md` | Extant Greek plus clearly marked hypothetical retroversions. |",
        "| Arabic literary layer | `reconstruction/earliest-sayings-gospel/reconstructed-gospel-ar-quranic-register.md` | Literary/theological reception layer, not a source witness. |",
        "| Parallel edition | `reconstruction/earliest-sayings-gospel/parallel-edition.md` | Synchronized multilingual view of the frozen reader. |",
        "",
        "## All-114 Logion Research Index",
        "",
        "Each row links the core card and the currently known evidence/control apparatus. `Reader text = YES` means the logion or a marked core appears in the clean reader; it does not mean unqualified certainty.",
        "",
        "| Logion | Reader | Decision | Greek status | Card | Evidence | Controls |",
        "| ---: | --- | --- | --- | --- | --- | --- |",
    ]
    for row in logia:
        lines.append(
            f"| {row.number} | {row.reader_text or 'NO'} | {row.decision or 'See matrix'} | {row.greek_status or 'Not recorded'} | {link(row.card)} | {compact_paths(row.evidence_notes, 2)} | {compact_paths(row.controls, 2)} |"
        )
    lines.extend(
        [
            "",
            "## Source Witness Inventory",
            "",
            f"The local source inventory currently contains {len(source_rows)} files under `sources/primary_texts/`. The full machine-readable table is `source-witness-inventory.tsv`.",
            "",
            "| Witness family | Digital role |",
            "| --- | --- |",
            "| Coptic / NHC II,2 | Main surviving complete-language witness for the Gospel of Thomas tradition used by the project. |",
            "| Greek P.Oxy. 1 | Early Greek fragmentary witness; direct Thomas witness where extant. |",
            "| Greek P.Oxy. 654 | Early Greek fragmentary witness; especially important for opening logia. |",
            "| Greek P.Oxy. 655 | Early Greek fragmentary witness; important but lacunose/uncertain in several places. |",
            "| Canonical Greek controls | Synoptic/control channel, not Thomas manuscript evidence. |",
            "| Translation controls | Open or protected translations used only according to rights/citation policy. |",
            "",
            "## Cluster And Control Notes",
            "",
            "Cluster notes prevent isolated decisions from distorting the reconstruction. They are especially important for motifs such as seek/find, family renunciation, wealth, beatitudes, living/dead/world, fire/kingdom, ritual practice, and thief/watchfulness.",
            "",
        ]
    )
    for path in cluster_notes:
        lines.append(f"- {link(path)}")
    lines.extend(
        [
            "",
            "## Bibliography, Rights, And Commons Policy",
            "",
            "- `bibliography/bibliography-working.md` - working bibliography with print keys.",
            "- `bibliography/source-rights-register.md` - source-rights status table.",
            "- `project/rights-and-citation-policy.md` - print/digital citation policy.",
            "- `project/source-reproducibility-note.md` - source reproducibility note.",
            "- `LICENSE.md` and `project/commons-dedication-and-use-policy.md` - commons / anti-ownership policy for the original EUAGELIA work.",
            "",
            "The original EUAGELIA reconstruction, translations, commentary, prompts, tables, and research architecture are intended as a commons. External witnesses, modern editions, translations, facsimiles, and websites retain their own legal status.",
            "",
            "## Audit Trail",
            "",
            f"The current audit-trail index contains {len(audit_rows)} project pass/audit/review files. Use `audit-trail-index.tsv` for checksums and exact file paths.",
            "",
            "Major publication-stage reports include:",
            "",
            "- `project/full-ukrainian-book-proof-qa-appendix-typography-v0.1.md`",
            "- `project/full-english-book-proof-qa-typography-v0.1.md`",
            "- `project/english-appendix-editorial-quality-pass-v0.1.md`",
            "- `project/full-book-assembly-typesetting-pipeline-v0.1.md`",
            "- `project/final-bibliography-rights-verify-v0.1.md`",
            "- `project/publication-remediation-plan-2026-07-18.md`",
            "",
            "## Reproducibility Checklist",
            "",
            "1. Run `python3 tools/qa_crosscheck.py`.",
            "2. Regenerate paper and companion sources with `python3 tools/assemble_full_book_sources.py` and `python3 tools/generate_digital_companion.py`.",
            "3. Render proofs with `python3 tools/render_full_book_proofs.py`.",
            "4. Compare checksums in `artifact-checksums.tsv` and `output/render-log-full-book-proofs-v0.1.md`.",
            "5. Review all changed files with `git status --short` and `git diff` before release.",
            "",
            "## Remaining Digital Work",
            "",
            "- Turn this Markdown/PDF proof into a polished HTML or static-site companion with better browsing, filters, and back-links.",
            "- Add final production checksums only after final copyedit and typesetting decisions.",
            "- Add a final external-source redistribution review before publishing downloadable source snapshots.",
        ]
    )
    return "\n".join(lines) + "\n"


def update_readme() -> None:
    text = """# Digital Scholarly Companion Package

Status: expanded companion package v0.1, 2026-07-19.

## Contents

- `companion-source-full.md` - human-readable digital research companion.
- `logion-cross-reference-index.tsv` - all 114 logia mapped to cards, evidence notes, controls, decisions, Greek status, and next actions.
- `source-witness-inventory.tsv` - local source corpus inventory with SHA256 checksums.
- `artifact-checksums.tsv` - checksums for core publication artifacts and generated paper proofs.
- `audit-trail-index.tsv` - major audit/pass/review files with checksums.
- `euagelia-digital-companion-full-proof.pdf` - PDF proof rendered from the companion source.

## Purpose

The digital companion keeps the full apparatus that paper books should not expose as raw infrastructure: file paths, evidence notes, source snapshots, control files, audit trail, bibliography, and machine-checkable cross-references.

## Still Needed

- polished browsable HTML/static-site version;
- final production checksums after final copyedit and typesetting;
- final external-source redistribution review before publishing downloadable snapshots.
"""
    (OUT / "README.md").write_text(text, encoding="utf-8")


def update_manifest(logia: list[LogionRow]) -> None:
    text = f"""# Digital Scholarly Companion Manifest

Status: expanded companion manifest v0.2, 2026-07-19.

## Purpose

The digital scholarly companion preserves the full apparatus that cannot fit cleanly into paper books: repository paths, evidence notes, source snapshots, audit trail, decision tables, checksums, and machine-checkable cross-references.

## Coverage

- Logion cross-reference rows: {len(logia)}/114.
- Clean-reader rows: {sum(1 for row in logia if row.reader_text == "YES")}.
- Evidence-note coverage: {sum(1 for row in logia if row.evidence_notes)}/114.
- Direct control-file coverage: {sum(1 for row in logia if row.controls)}/114.

## Companion Artifacts

- `output/digital-scholarly-companion/companion-source-full.md`
- `output/digital-scholarly-companion/logion-cross-reference-index.tsv`
- `output/digital-scholarly-companion/source-witness-inventory.tsv`
- `output/digital-scholarly-companion/artifact-checksums.tsv`
- `output/digital-scholarly-companion/audit-trail-index.tsv`
- `output/digital-scholarly-companion/euagelia-digital-companion-full-proof.pdf`

## Frozen Reader Source

- `reconstruction/earliest-sayings-gospel/final-clean-reader-freeze-v0.1.md`
- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-uk.md`
- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-en.md`
- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-coptic.md`
- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-greek.md`
- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-ar-quranic-register.md`
- `reconstruction/earliest-sayings-gospel/parallel-edition.md`

## Full Commentary And Decisions

- `reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-uk.md`
- `reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-en.md`
- `reconstruction/earliest-sayings-gospel/all-114-publication-decision-table-v0.1.md`
- `reconstruction/earliest-sayings-gospel/inclusion-decisions-table.md`
- `reconstruction/earliest-sayings-gospel/evidence-dossier-en.md`

## Primary Text And Witness Sources

- `sources/primary_texts/coptic/`
- `sources/primary_texts/greek_poxy/`
- `sources/primary_texts/notes/`
- `sources/primary_texts/translations/`
- `sources/primary_texts/source-register.md`

## Bibliography And Rights

- `bibliography/bibliography-working.md`
- `bibliography/source-rights-register.md`
- `project/rights-and-citation-policy.md`
- `project/source-reproducibility-note.md`

## Remaining Companion Work

1. Build a polished browsable HTML/static-site edition with filters and back-links.
2. Add final production checksums after final copyedit and typesetting.
3. Run final external-source redistribution review before publishing downloadable snapshots.
"""
    (OUT / "companion-manifest.md").write_text(text, encoding="utf-8")


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    logia = collect_logion_rows()
    if len(logia) != 114:
        raise SystemExit(f"Expected 114 logion rows, found {len(logia)}")
    write_machine_indexes(logia)
    (OUT / "companion-source-full.md").write_text(companion_markdown(logia), encoding="utf-8")
    update_manifest(logia)
    update_readme()
    print("output/digital-scholarly-companion/companion-source-full.md")
    print("output/digital-scholarly-companion/logion-cross-reference-index.tsv")
    print("output/digital-scholarly-companion/source-witness-inventory.tsv")
    print("output/digital-scholarly-companion/artifact-checksums.tsv")
    print("output/digital-scholarly-companion/audit-trail-index.tsv")


if __name__ == "__main__":
    main()
