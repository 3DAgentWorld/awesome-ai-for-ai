"""Render the README catalog from the companion site's paper data."""

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BEGIN = "<!-- BEGIN PAPER CATALOG -->"
END = "<!-- END PAPER CATALOG -->"
ROLES = (
    ("Training experience", "Training experience"),
    ("Evaluation feedback", "Evaluation feedback"),
    ("System changes", "System changes"),
    ("Retained improvement", "Retained improvement"),
    ("Related work & evidence", "Related work and evidence"),
    ("Boundary case", "Boundary cases"),
)
CORPUS = {"main": "Main", "supplement": "Supplement", "both": "Main + supplement"}


def paper_table(papers):
    rows = ["| Paper | Venue | Corpus | Code |", "| --- | --- | --- | --- |"]
    for paper in papers:
        title = re.sub(r"([\\|`*_\[\]<>])", r"\\\1", paper["title"])
        code = " · ".join(
            f"[{'Code' if len(paper['code_urls']) == 1 else f'Code {n}'}]({url})"
            for n, url in enumerate(paper["code_urls"], 1)
        )
        rows.append(
            f"| [{title}]({paper['paper_url']}) | {paper['venue']} {paper['year']} | "
            f"{CORPUS[paper['corpus']]} | {code} |"
        )
    return "\n".join(rows)


def main():
    source = (ROOT / "js" / "papers-data.js").read_text(encoding="utf-8")
    _, data = source.split("window.AI4AI_PAPERS = ", 1)
    papers, _ = json.JSONDecoder().raw_decode(data)
    grouped = {role: [] for role, _ in ROLES}
    for paper in papers:
        grouped[paper["survey_role"]].append(paper)

    index = ["| Browse by survey role | Papers |", "| --- | ---: |"]
    for role, heading in ROLES:
        anchor = heading.lower().replace(" ", "-")
        index.append(f"| [{heading}](#{anchor}) | {len(grouped[role])} |")

    with_code = sum(bool(paper["code_urls"]) for paper in papers)
    sections = ["## Papers", f"**{len(papers)} papers** · {with_code} with code", "\n".join(index)]
    for role, heading in ROLES:
        entries = grouped[role]
        sections.extend([
            f"### {heading}",
            f"<details>\n<summary>Show {len(entries)} papers</summary>\n\n"
            f"{paper_table(entries)}\n\n</details>",
            "[Back to paper index](#papers)",
        ])

    readme = ROOT / "README.md"
    before, catalog = readme.read_text(encoding="utf-8").split(BEGIN, 1)
    _, after = catalog.split(END, 1)
    rendered = "\n\n".join(sections)
    readme.write_text(f"{before}{BEGIN}\n\n{rendered}\n\n{END}{after}", encoding="utf-8")


if __name__ == "__main__":
    main()
