#!/usr/bin/env python3
"""Audit probability profiles against current clean-reader decisions."""

from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]


def read(path: str) -> str:
    return (ROOT / path).read_text()


def parse_workflow() -> dict[int, dict[str, str]]:
    rows: dict[int, dict[str, str]] = {}
    for line in read("research/tables/logia-workflow-matrix.md").splitlines():
        if not line.startswith("|") or line.startswith("| ---"):
            continue
        parts = [p.strip() for p in line.strip("|").split("|")]
        if len(parts) >= 8 and re.fullmatch(r"\d+", parts[0] or ""):
            rows[int(parts[0])] = {
                "decision": parts[3],
                "reader": parts[4],
                "status": parts[6],
                "next": parts[7],
            }
    return rows


def parse_all114() -> dict[int, dict[str, str]]:
    rows: dict[int, dict[str, str]] = {}
    for line in read("research/decisions/all-114-publication-decision-table-v0.1.md").splitlines():
        if not line.startswith("|") or line.startswith("| ---"):
            continue
        parts = [p.strip() for p in line.strip("|").split("|")]
        if len(parts) >= 10 and re.fullmatch(r"\d+", parts[0] or ""):
            rows[int(parts[0])] = {
                "unit": parts[1],
                "publication_status": parts[2],
                "clean": parts[3],
                "confidence": parts[4],
                "rationale": parts[7],
            }
    return rows


PERIODS = {
    "pre60": r"(?:До 60 року|Before 60 CE)",
    "p60_90": r"(?:60-90 роки|60-90 CE)",
    "p90_130": r"(?:90-130 роки|90-130 CE)",
    "post130": r"(?:Після 130 року|After 130 CE)",
}


def parse_probabilities(logion: int) -> dict[str, int | None]:
    text = read(f"research/logion-cards/logion-{logion:03d}.md")
    values: dict[str, int | None] = {}
    for key, label in PERIODS.items():
        matches = re.findall(label + r"\s*\|\s*(\d+)%", text)
        # The latest/gold-level profile is the last numeric profile in the card.
        values[key] = int(matches[-1]) if matches else None
    return values


def duplicate_probability_cards() -> list[int]:
    duplicates: list[int] = []
    for logion in range(1, 115):
        text = read(f"research/logion-cards/logion-{logion:03d}.md")
        current_profile_headings = re.findall(r"^### Ймовірнісний профіль\s*$", text, flags=re.MULTILINE)
        if len(current_profile_headings) > 1:
            duplicates.append(logion)
    return duplicates


def main() -> int:
    workflow = parse_workflow()
    all114 = parse_all114()

    rows = []
    for logion in range(1, 115):
        probs = parse_probabilities(logion)
        if all(value is not None for value in probs.values()):
            early = int(probs["pre60"]) + int(probs["p60_90"])
            late = int(probs["p90_130"]) + int(probs["post130"])
        else:
            early = None
            late = None
        row = {
            "logion": logion,
            **probs,
            "early": early,
            "late": late,
            **workflow.get(logion, {}),
            **all114.get(logion, {}),
        }
        rows.append(row)

    included_late = [
        r for r in rows
        if r.get("reader") == "YES"
        and r["early"] is not None
        and (int(r["late"]) >= 60 or int(r["post130"]) >= 20)
    ]
    excluded_early_60 = [
        r for r in rows
        if r.get("reader") == "NO"
        and r["early"] is not None
        and int(r["early"]) >= 60
    ]
    excluded_early_50 = [
        r for r in rows
        if r.get("reader") == "NO"
        and r["early"] is not None
        and int(r["early"]) >= 50
    ]

    print("Probability vs reader audit")
    print(f"- cards with current/latest numeric profile: {sum(r['early'] is not None for r in rows)}/114")
    print(f"- cards with duplicate current probability profiles: {len(duplicate_probability_cards())}")
    print(f"- included units with late >= 60 or post-130 >= 20: {len(included_late)}")
    for r in included_late:
        print(f"  - {r['logion']}: early={r['early']} late={r['late']} post130={r['post130']} decision={r.get('decision')}")
    print(f"- excluded units with early >= 60: {len(excluded_early_60)}")
    for r in sorted(excluded_early_60, key=lambda item: (-int(item["early"]), item["logion"])):
        print(f"  - {r['logion']}: early={r['early']} late={r['late']} decision={r.get('decision')} status={r.get('publication_status')}")
    print(f"- excluded units with early >= 50: {len(excluded_early_50)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
