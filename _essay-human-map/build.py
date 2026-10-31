"""Build the essay as a cover post plus one page per chapter.

usage: assemble.py <workspace> <blog root>
"""
import pathlib, re, sys

ws = pathlib.Path(sys.argv[1])
root = pathlib.Path(sys.argv[2])
BOOK = "human-map-agent-hands"
HOME = f"/{BOOK}/"
TITLE = "Human Map, Agent Hands"
COVER = "/images/human-map-agent-hands-cover.jpg"
TLDR = ("TLDR. Agents make building fast and failure cheap in time. Running a "
        "platform under strict rules, maintaining it, and finding customers stay "
        "expensive. Let humans hold the map, let agents do the hands-on work, set "
        "autonomy by what a failure costs, and remember that the most valuable "
        "decision is often what not to build.")


def diagram(m):
    src = (ws / m.group(1)).read_text()
    # Drop "%%" comments but keep "%%{init...}%%" directives.
    src = "\n".join(l for l in src.splitlines()
                    if not (l.startswith("%%") and not l.startswith("%%{")))
    # raw: Mermaid syntax such as {{hexagon}} would otherwise be eaten by Liquid.
    return "{% raw %}\n```mermaid\n" + src.strip() + "\n```\n{% endraw %}"


def mark(m):
    cls = "ph verify" if m.group(1) == "VERIFY" else "ph"
    return f'<mark class="{cls}">{m.group(0)}</mark>'


chapters = []
for f in sorted((ws / "essay").glob("[0-9][0-9]-*.md")):
    if f.name.startswith("00-"):
        continue
    t = f.read_text()
    t = re.sub(r"<!-- REVIEW NOTES.*?-->\s*", "", t, flags=re.S)
    heading, body = t.split("\n", 1)
    title = heading.lstrip("# ").strip()
    has_diagram = "[DIAGRAM:" in body
    body = re.sub(r"\[DIAGRAM: (diagrams/[^\]]+)\]", diagram, body)
    body = re.sub(r"\[(ADD|VERIFY):[^\]]*\]", mark, body, flags=re.S)
    chapters.append((f.stem, title, has_diagram, body.strip()))

def url(i):
    return f"{{{{ '/{BOOK}/{chapters[i - 1][0]}/' | relative_url }}}}"


def link_refs(body, idx):
    """Link "chapter N", "chapters N, M, and K", and "the previous chapter"."""
    def ref(m):
        nums = [int(n) for n in re.findall(r"\d+", m.group(0))]
        if not all(1 <= n <= len(chapters) for n in nums):
            return m.group(0)
        if len(nums) == 1:
            return f"[{m.group(0)}]({url(nums[0])})"
        return re.sub(r"\d+", lambda d: f"[{d.group(0)}]({url(int(d.group(0)))})", m.group(0))

    body = re.sub(r"\b[Cc]hapters?\s+\d+(?:(?:,\s*|,?\s+and\s+)\d+)*", ref, body)
    if idx > 1:
        body = re.sub(r"\bprevious\s+chapter\b",
                      lambda m: f"[{m.group(0)}]({url(idx - 1)})", body)
    return body


chapters = [(s, t, d, link_refs(b, i)) for i, (s, t, d, b) in enumerate(chapters, 1)]

out_dir = root / BOOK
out_dir.mkdir(exist_ok=True)
for old in out_dir.glob("[0-9][0-9]-*.md"):
    old.unlink()

n = len(chapters)
for idx, (slug, title, has_diagram, body) in enumerate(chapters, 1):
    fm = [
        "---",
        "layout: chapter",
        f'title: "{title}"',
        f'desc: "{TITLE} · Chapter {idx} of {n}"',
        f"book: {BOOK}",
        f"book_home: {HOME}",
        f"chapter: {idx}",
        f"permalink: /{BOOK}/{slug}/",
        f"image: {COVER}",
    ]
    if has_diagram:
        fm.append("mermaid: true")
    fm.append("---")
    (out_dir / f"{slug}.md").write_text("\n".join(fm) + "\n\n" + body + "\n")

toc = "\n".join(
    f"- [{title}]({{{{ '/{BOOK}/{slug}/' | relative_url }}}})"
    for slug, title, _, _ in chapters
)
first = chapters[0][0]
cover = f"""---
layout: posts
title: "{TITLE}"
tags: AI agents engineering fintech SDLC
desc: "{TLDR}"
permalink: {HOME}
image: {COVER}
---

<style>
mark.ph {{ background: #fff3b0; padding: 0 .2em; }}
</style>

*Agents made building cheap. Owning, running, and choosing what to build are
still ours.*

![A hand drawing a boundary line on a map divided into green, amber, and red zones, with many small builders at work in the green zone and fewer in the amber zone]({{{{ '{COVER}' | relative_url }}}})

**[Start reading &rarr;]({{{{ '/{BOOK}/{first}/' | relative_url }}}})**

## Contents

{toc}

---

*This essay is licensed under [Creative Commons Attribution 4.0
(CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).*
"""
(root / "_drafts" / "Human-Map-Agent-Hands.md").write_text(cover)
words = sum(len(b.split()) for *_, b in chapters)
print(f"{n} chapters, {words} words, cover + pages in {out_dir}")
