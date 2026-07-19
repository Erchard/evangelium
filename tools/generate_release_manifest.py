#!/usr/bin/env python3
"""Generate a release-candidate manifest for current EUAGELIA artifacts."""

from __future__ import annotations

import hashlib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output/release-candidate-manifest-v1.0-rc1.tsv"

ARTIFACTS = [
    "README.md",
    "LICENSE.md",
    "project/project-completion-roadmap.md",
    "project/publication-remediation-plan-2026-07-18.md",
    "project/final-product-specification.md",
    "project/final-production-typesetting-copyedit-gate-v0.1.md",
    "project/typst-production-pilot-v0.1.md",
    "project/release-candidate-audit-v1.0-rc1.md",
    "output/uk-paper-book/book-source-uk-full.md",
    "output/uk-paper-book/euagelia-uk-full-proof.pdf",
    "output/en-paper-book/book-source-en-full.md",
    "output/en-paper-book/euagelia-en-full-proof.pdf",
    "output/digital-scholarly-companion/companion-source-full.md",
    "output/digital-scholarly-companion/euagelia-digital-companion-full-proof.pdf",
    "output/digital-scholarly-companion/html/index.html",
    "output/digital-scholarly-companion/logion-cross-reference-index.tsv",
    "output/digital-scholarly-companion/source-witness-inventory.tsv",
    "output/digital-scholarly-companion/artifact-checksums.tsv",
    "output/digital-scholarly-companion/audit-trail-index.tsv",
    "output/production-typst/README.md",
    "output/production-typst/euagelia-template.typ",
    "output/production-typst/uk-pilot.typ",
    "output/production-typst/en-pilot.typ",
    "output/production-typst/production-handoff-checklist.md",
    "output/production-typst/production-pilot-manifest.tsv",
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    rows = ["artifact\texists\tbytes\tsha256"]
    for item in ARTIFACTS:
        path = ROOT / item
        if path.exists():
            rows.append(f"{item}\tYES\t{path.stat().st_size}\t{sha256(path)}")
        else:
            rows.append(f"{item}\tNO\t0\t")
    OUT.write_text("\n".join(rows) + "\n", encoding="utf-8")
    print(OUT.relative_to(ROOT))


if __name__ == "__main__":
    main()
