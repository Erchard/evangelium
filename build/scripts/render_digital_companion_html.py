#!/usr/bin/env python3
"""Render a static browsable HTML companion from generated TSV indexes."""

from __future__ import annotations

import csv
import html
import json
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
COMPANION = ROOT / "dist/digital-scholarly-companion"
HTML_DIR = COMPANION / "html"


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def rel_to_html(path: str) -> str:
    return "../../../" + path


def esc(value: str) -> str:
    return html.escape(value or "", quote=True)


def strip_ticks(value: str) -> str:
    return (value or "").replace("`", "")


def split_paths(value: str) -> list[str]:
    return [part.strip() for part in (value or "").split(";") if part.strip()]


def link_path(path: str, label: str | None = None) -> str:
    label = label or path
    return f'<a href="{esc(rel_to_html(path))}"><code>{esc(label)}</code></a>'


def short_path(path: str) -> str:
    return path.split("/")[-1]


def decision_family(decision: str, reader: str) -> str:
    plain = strip_ticks(decision)
    if reader == "YES":
        return "reader"
    if "EXCLUDE_AS_SECONDARY" in plain:
        return "excluded"
    if "DEFER" in plain:
        return "deferred"
    if "UNCERTAIN" in plain:
        return "uncertain"
    if "APPENDIX_ONLY" in plain or "KEEP_APPENDIX_ONLY" in plain:
        return "appendix"
    return "other"


def witness_groups(greek_status: str, controls: str) -> list[tuple[str, str]]:
    status = greek_status.lower()
    groups = [("coptic", "Coptic NHC II,2")]
    if "654" in status:
        groups.append(("poxy654", "P.Oxy. 654"))
    if "655" in status:
        groups.append(("poxy655", "P.Oxy. 655"))
    if "p.oxy. 1" in status or "p.oxy.1" in status:
        groups.append(("poxy1", "P.Oxy. 1"))
    if "5575" in status:
        groups.append(("poxy5575", "P.Oxy. 5575 control"))
    if "retroversion" in status:
        groups.append(("retroversion", "Greek retroversion policy"))
    if controls:
        groups.append(("canonical", "Canonical/control files"))
    seen: set[str] = set()
    result = []
    for key, label in groups:
        if key not in seen:
            seen.add(key)
            result.append((key, label))
    return result


def source_group_id(category: str, path: str) -> str:
    text = (category + " " + path).lower()
    if "coptic" in text:
        return "coptic"
    if "654" in text:
        return "poxy654"
    if "655" in text:
        return "poxy655"
    if "poxy1" in text or "poxy-1" in text or "p.oxy. 1" in text:
        return "poxy1"
    if "5575" in text:
        return "poxy5575"
    if "canonical" in text or "sblgnt" in text:
        return "canonical"
    if "translation" in text:
        return "translation"
    return "general"


def badge(text: str, class_name: str) -> str:
    return f'<span class="badge {class_name}">{esc(text)}</span>'


def render_link_list(paths: list[str], empty: str) -> str:
    if not paths:
        return f'<span class="muted">{esc(empty)}</span>'
    return "<ul>" + "".join(f"<li>{link_path(path, short_path(path))}</li>" for path in paths) + "</ul>"


def build() -> str:
    logia = read_tsv(COMPANION / "logion-cross-reference-index.tsv")
    sources = read_tsv(COMPANION / "source-witness-inventory.tsv")
    audits = read_tsv(COMPANION / "audit-trail-index.tsv")
    artifacts = read_tsv(COMPANION / "artifact-checksums.tsv")

    families = Counter(decision_family(row["decision"], row["reader_text"]) for row in logia)
    greek_statuses = Counter(row["greek_status"] or "Not recorded" for row in logia)
    source_groups = Counter(source_group_id(row["category"], row["path"]) for row in sources)

    logia_json = json.dumps(
        [
            {
                "n": row["logion"],
                "reader": row["reader_text"],
                "decision": strip_ticks(row["decision"]),
                "family": decision_family(row["decision"], row["reader_text"]),
                "greek": row["greek_status"],
                "status": row["current_status"],
                "next": row["next_action"],
                "search": " ".join(row.values()).lower(),
            }
            for row in logia
        ],
        ensure_ascii=False,
    )

    logion_rows = []
    for row in logia:
        evidence = split_paths(row["evidence_notes"])
        controls = split_paths(row["controls"])
        family = decision_family(row["decision"], row["reader_text"])
        witness_links = " ".join(
            f'<a class="pill-link" href="#source-{key}">{esc(label)}</a>'
            for key, label in witness_groups(row["greek_status"], row["controls"])
        )
        logion_rows.append(
            f"""
            <details class="logion" data-logion="{esc(row['logion'])}" data-reader="{esc(row['reader_text'])}" data-family="{esc(family)}" data-greek="{esc(row['greek_status'])}">
              <summary>
                <span class="logion-number">Logion {esc(row['logion'])}</span>
                {badge('reader' if row['reader_text'] == 'YES' else 'appendix', 'reader' if row['reader_text'] == 'YES' else 'appendix')}
                {badge(strip_ticks(row['decision']) or 'See matrix', family)}
                <span class="greek">{esc(row['greek_status'] or 'Greek status not recorded')}</span>
              </summary>
              <div class="detail-grid">
                <section>
                  <h3>Core Links</h3>
                  <p>{link_path(row['card'], 'card')}</p>
                  <p>{link_path('book/appendix/commentary-uk.md', 'Ukrainian appendix')}</p>
                  <p>{link_path('book/appendix/commentary-en.md', 'English appendix')}</p>
                </section>
                <section>
                  <h3>Evidence Notes</h3>
                  {render_link_list(evidence, 'No direct evidence note recorded')}
                </section>
                <section>
                  <h3>Control Files</h3>
                  {render_link_list(controls, 'No direct control file recorded')}
                </section>
                <section>
                  <h3>Witness Channels</h3>
                  <p>{witness_links}</p>
                  <p class="small"><b>Current status:</b> {esc(row['current_status'] or 'Not recorded')}</p>
                  <p class="small"><b>Next action:</b> {esc(row['next_action'] or 'Not recorded')}</p>
                </section>
              </div>
            </details>
            """
        )

    source_sections = []
    for group in ["coptic", "poxy1", "poxy654", "poxy655", "poxy5575", "canonical", "translation", "general"]:
        group_rows = [row for row in sources if source_group_id(row["category"], row["path"]) == group]
        if not group_rows:
            continue
        title = {
            "coptic": "Coptic / NHC II,2",
            "poxy1": "Greek P.Oxy. 1",
            "poxy654": "Greek P.Oxy. 654",
            "poxy655": "Greek P.Oxy. 655",
            "poxy5575": "Greek P.Oxy. 5575 Control",
            "canonical": "Canonical Greek Controls",
            "translation": "Translation Controls",
            "general": "General Source Corpus",
        }[group]
        rows = "\n".join(
            f"<tr><td>{esc(row['category'])}</td><td>{link_path(row['path'])}</td><td>{esc(row['bytes'])}</td><td><code>{esc(row['sha256'][:16])}...</code></td></tr>"
            for row in group_rows
        )
        source_sections.append(
            f"""
            <section id="source-{group}" class="source-group">
              <h3>{esc(title)} <span class="count">{len(group_rows)}</span></h3>
              <table>
                <thead><tr><th>Category</th><th>Path</th><th>Bytes</th><th>SHA256</th></tr></thead>
                <tbody>{rows}</tbody>
              </table>
            </section>
            """
        )

    audit_rows = "\n".join(
        f"<tr><td>{link_path(row['path'])}</td><td>{esc(row['title'])}</td><td>{esc(row['bytes'])}</td><td><code>{esc(row['sha256'][:16])}...</code></td></tr>"
        for row in audits
    )
    artifact_rows = "\n".join(
        f"<tr><td>{link_path(row['artifact'])}</td><td>{esc(row['bytes'])}</td><td><code>{esc(row['sha256'])}</code></td></tr>"
        for row in artifacts
    )

    css = """
    :root { color-scheme: light; --ink:#1f2328; --muted:#626a73; --line:#d7dde3; --soft:#f6f8fa; --blue:#1f5f9f; --green:#2f6f4e; --amber:#8a5a00; --red:#9b2c2c; --violet:#5f4b8b; }
    * { box-sizing: border-box; }
    body { margin: 0; font: 15px/1.48 -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; color: var(--ink); background: #fff; }
    header { border-bottom: 1px solid var(--line); padding: 22px 28px 18px; }
    h1 { margin: 0 0 6px; font-size: 24px; letter-spacing: 0; }
    h2 { margin: 30px 0 12px; font-size: 18px; letter-spacing: 0; }
    h3 { margin: 0 0 8px; font-size: 14px; letter-spacing: 0; }
    p { margin: 0 0 10px; }
    main { max-width: 1280px; margin: 0 auto; padding: 18px 24px 36px; }
    code { font-size: .92em; background: var(--soft); padding: 1px 4px; border-radius: 4px; }
    a { color: var(--blue); text-decoration-thickness: .08em; text-underline-offset: 2px; }
    .subtle { color: var(--muted); max-width: 900px; }
    .stats { display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: 10px; margin: 16px 0 20px; }
    .stat { border: 1px solid var(--line); border-radius: 6px; padding: 10px 12px; background: var(--soft); }
    .stat b { display: block; font-size: 20px; }
    .toolbar { position: sticky; top: 0; z-index: 2; display: grid; grid-template-columns: 1.6fr repeat(3, minmax(150px, .5fr)); gap: 10px; padding: 10px; margin: 0 0 14px; border: 1px solid var(--line); background: rgba(255,255,255,.96); border-radius: 6px; }
    input, select { width: 100%; border: 1px solid var(--line); border-radius: 5px; padding: 8px 9px; font: inherit; background: #fff; }
    .logion { border: 1px solid var(--line); border-radius: 6px; margin: 8px 0; background: #fff; }
    .logion[hidden] { display: none; }
    summary { cursor: pointer; display: grid; grid-template-columns: 92px 68px minmax(220px, 1fr) minmax(160px, .8fr); gap: 8px; align-items: center; padding: 9px 11px; }
    summary:hover { background: var(--soft); }
    .logion-number { font-weight: 700; }
    .greek { color: var(--muted); font-size: 13px; }
    .badge { display: inline-block; width: fit-content; max-width: 100%; border-radius: 999px; padding: 2px 8px; font-size: 12px; line-height: 1.35; border: 1px solid transparent; white-space: normal; }
    .badge.reader { color: var(--green); border-color: #9bc5aa; background: #edf7f0; }
    .badge.appendix { color: var(--violet); border-color: #c8bfdd; background: #f4f1fa; }
    .badge.deferred, .badge.uncertain { color: var(--amber); border-color: #dfc47e; background: #fff8e8; }
    .badge.excluded { color: var(--red); border-color: #dda3a3; background: #fff0f0; }
    .badge.other { color: var(--muted); border-color: var(--line); background: var(--soft); }
    .detail-grid { border-top: 1px solid var(--line); display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 14px; padding: 13px 14px 16px; }
    .detail-grid section { min-width: 0; }
    ul { margin: 0; padding-left: 18px; }
    .small { font-size: 13px; color: var(--muted); }
    .muted { color: var(--muted); }
    .pill-link { display: inline-block; border: 1px solid var(--line); border-radius: 999px; padding: 2px 7px; margin: 0 4px 5px 0; background: var(--soft); text-decoration: none; font-size: 12px; }
    table { width: 100%; border-collapse: collapse; margin: 8px 0 18px; }
    th, td { border: 1px solid var(--line); padding: 6px 7px; text-align: left; vertical-align: top; }
    th { background: var(--soft); font-weight: 650; }
    td { overflow-wrap: anywhere; }
    .count { color: var(--muted); font-weight: 400; }
    .section-nav { display: flex; flex-wrap: wrap; gap: 8px; margin: 12px 0 18px; }
    .section-nav a { border: 1px solid var(--line); border-radius: 5px; padding: 5px 8px; background: var(--soft); text-decoration: none; }
    @media (max-width: 760px) {
      main { padding: 14px; }
      header { padding: 18px 16px; }
      .toolbar { position: static; grid-template-columns: 1fr; }
      summary { grid-template-columns: 1fr; }
    }
    """

    js = f"""
    const LOGIA = {logia_json};
    const search = document.getElementById('search');
    const reader = document.getElementById('readerFilter');
    const family = document.getElementById('familyFilter');
    const greek = document.getElementById('greekFilter');
    const count = document.getElementById('visibleCount');
    function applyFilters() {{
      const q = search.value.trim().toLowerCase();
      let visible = 0;
      document.querySelectorAll('.logion').forEach((el, idx) => {{
        const data = LOGIA[idx];
        const ok = (!q || data.search.includes(q)) &&
          (!reader.value || data.reader === reader.value) &&
          (!family.value || data.family === family.value) &&
          (!greek.value || data.greek === greek.value);
        el.hidden = !ok;
        if (ok) visible++;
      }});
      count.textContent = visible;
    }}
    [search, reader, family, greek].forEach(el => el.addEventListener('input', applyFilters));
    document.getElementById('expandAll').addEventListener('click', () => document.querySelectorAll('.logion:not([hidden])').forEach(el => el.open = true));
    document.getElementById('collapseAll').addEventListener('click', () => document.querySelectorAll('.logion').forEach(el => el.open = false));
    applyFilters();
    """

    greek_options = "\n".join(f'<option value="{esc(key)}">{esc(key)} ({value})</option>' for key, value in sorted(greek_statuses.items()))

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>EUAGELIA Digital Scholarly Companion</title>
  <style>{css}</style>
</head>
<body>
  <header>
    <h1>EUAGELIA Digital Scholarly Companion</h1>
    <p class="subtle">Static research workbench for the reconstruction: all 114 logia, reader decisions, manuscript/control status, evidence notes, source inventory, checksums, and audit trail.</p>
  </header>
  <main>
    <nav class="section-nav" aria-label="Sections">
      <a href="#logia">Logia</a>
      <a href="#sources">Sources</a>
      <a href="#audit">Audit Trail</a>
      <a href="#rights">Rights</a>
      <a href="#reproducibility">Reproducibility</a>
    </nav>

    <section class="stats" aria-label="Companion summary">
      <div class="stat"><b>114</b>Logion entries</div>
      <div class="stat"><b>{families.get('reader', 0)}</b>Clean-reader units</div>
      <div class="stat"><b>{len(sources)}</b>Source files indexed</div>
      <div class="stat"><b>{len(audits)}</b>Audit/pass files indexed</div>
    </section>

    <section id="logia">
      <h2>All-114 Logion Index</h2>
      <p class="subtle">Search across logion number, decision, Greek status, file paths, and next-action notes. Reader inclusion means the logion or marked core appears in the clean reconstruction, not that uncertainty has disappeared.</p>
      <div class="toolbar">
        <input id="search" type="search" placeholder="Search logia, sources, decisions, controls...">
        <select id="readerFilter"><option value="">Reader: all</option><option value="YES">Reader: yes</option><option value="NO">Reader: no</option></select>
        <select id="familyFilter"><option value="">Decision family: all</option><option value="reader">Reader</option><option value="appendix">Appendix only</option><option value="uncertain">Uncertain</option><option value="deferred">Deferred</option><option value="excluded">Excluded</option><option value="other">Other</option></select>
        <select id="greekFilter"><option value="">Greek status: all</option>{greek_options}</select>
      </div>
      <p class="small">Showing <span id="visibleCount">114</span> logia. <button id="expandAll" type="button">Expand visible</button> <button id="collapseAll" type="button">Collapse all</button></p>
      {''.join(logion_rows)}
    </section>

    <section id="sources">
      <h2>Source Witness Inventory</h2>
      <p class="subtle">Manuscript witnesses, source snapshots, translations, and control files are grouped by function. Canonical Greek controls are not Thomas witnesses; hypothetical Greek retroversions are publication reconstructions, not manuscripts.</p>
      {''.join(source_sections)}
    </section>

    <section id="audit">
      <h2>Audit Trail</h2>
      <table>
        <thead><tr><th>Path</th><th>Title</th><th>Bytes</th><th>SHA256</th></tr></thead>
        <tbody>{audit_rows}</tbody>
      </table>
    </section>

    <section id="rights">
      <h2>Bibliography, Rights, And Commons Policy</h2>
      <p>{link_path('book/bibliography/bibliography-working.md', 'Working bibliography')}</p>
      <p>{link_path('book/bibliography/source-rights-register.md', 'Source rights register')}</p>
      <p>{link_path('project/rights-and-citation-policy.md', 'Rights and citation policy')}</p>
      <p>{link_path('project/commons-dedication-and-use-policy.md', 'Commons / anti-ownership policy')}</p>
    </section>

    <section id="reproducibility">
      <h2>Reproducibility</h2>
      <ol>
        <li>Run <code>python3 build/scripts/qa_crosscheck.py</code>.</li>
        <li>Regenerate companion data with <code>python3 build/scripts/generate_digital_companion.py</code>.</li>
        <li>Regenerate this HTML with <code>python3 build/scripts/render_digital_companion_html.py</code>.</li>
        <li>Render proofs with <code>python3 build/scripts/render_full_book_proofs.py</code>.</li>
      </ol>
      <h3>Core Artifact Checksums</h3>
      <table>
        <thead><tr><th>Artifact</th><th>Bytes</th><th>SHA256</th></tr></thead>
        <tbody>{artifact_rows}</tbody>
      </table>
    </section>
  </main>
  <script>{js}</script>
</body>
</html>
"""


def main() -> None:
    HTML_DIR.mkdir(parents=True, exist_ok=True)
    index = HTML_DIR / "index.html"
    index.write_text(build(), encoding="utf-8")
    print(index.relative_to(ROOT))


if __name__ == "__main__":
    main()
