# Workspace: "Human Map, Agent Hands"

This is the working folder for the essay. The leading underscore keeps Jekyll
from publishing it. The full project brief (purpose, hard rules, section plan)
is the pasted context in the session that started this work. Its key rules
are repeated here:

- Never invent anecdotes, incidents, numbers, quotes, or people. Use `[ADD: ...]`.
- Mark unverified external claims `[VERIFY: ...]` and track them in
  `references/to-verify.md`.
- No company cost figures. Do not name products, vendors, internal projects,
  or people. Do not name the regulator in the compliance story.
- Do not claim that roles will disappear. The author's claims are his experience.
- License: CC BY 4.0.

## Layout

- `essay/`: one file per section (00 is the title and index).
- `diagrams/`: Mermaid sources. Inline them into the post as ```` ```mermaid ```` blocks.
  The post needs `mermaid: true` in its front matter (see `_layouts/posts.htmls`).
- `references/to-verify.md`: sources to check before publishing.
- Refined sections end with a `<!-- REVIEW NOTES -->` block that marks the parts
  needing deeper thought. Strip these blocks when assembling the post.

## Decisions so far

- The section drafts named in the brief were not found, so all 13 sections were
  drafted from scratch from the brief (2026-10-31).
- Diagrams are in Mermaid (2026-10-31).
- Post path: `_posts/2026-MM-DD-Human-Map-Agent-Hands.md`. Front matter style:
  `layout: posts`, `title`, `tags`, `desc: TLDR. ...`.

## Building the pages

From the blog root:

    python3 _essay-human-map/build.py _essay-human-map .

This writes the cover to `_drafts/Human-Map-Agent-Hands.md` and one page per
chapter to `human-map-agent-hands/`. Never edit those generated files by hand;
edit `essay/` and `diagrams/`, then rebuild. To preview locally, run
`bundle exec jekyll serve --drafts` with the local config renamed to a `.yml`
file.
