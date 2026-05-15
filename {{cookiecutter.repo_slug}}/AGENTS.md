# AGENTS.md — LLM Wiki Maintainer

You are maintaining an LLM Wiki: a persistent, interlinked markdown knowledge base built from curated raw sources.

The goal is not to answer from scratch every time. The goal is to compile knowledge once, keep it current, and make future answers easier, better cited, and more synthetic.

## Directory structure

- `raw/` — immutable source material
- `inbox/` — unprocessed material
- `wiki/` — LLM-maintained markdown pages
- `wiki/index.md` — master index and navigation map
- `wiki/sources/` — one source-summary page per raw source or logical source unit
- `wiki/concepts/` — recurring concepts, methods, theories, and frameworks
- `wiki/people/` — people and their relevance
- `wiki/organizations/` — organizations and their relevance
- `wiki/projects/` — projects, programs, and initiatives
- `wiki/datasets/` — datasets and data products
- `wiki/decisions/` — durable decisions, assumptions, and rationale
- `wiki/synthesis/` — cross-source analyses and higher-level summaries
- `wiki/questions/` — durable open questions, TODOs, and uncertainties
- `wiki/logs/` — append-only maintenance and audit logs
- `templates/` — page templates used by humans and tooling
- `skills/` — canonical local workflow skills
- `.agents/skills/` — Codex-compatible skill mirror
- `.claude/skills/` — Claude Code-compatible skill mirror
- `.gemini/skills/` — Gemini-compatible skill mirror

## Wiki skill dispatch

Use the wiki skills as follows:

- `wiki-ingest` — convert raw source material into source-summary pages
- `wiki-integrate` — incorporate source summaries into concepts, synthesis, projects, decisions, questions, and other durable wiki pages
- `wiki-search` — answer questions from the wiki before falling back to raw sources
- `wiki-audit` — review wiki health, links, provenance, duplication, and integration gaps
- `wiki-slides` — create slide artifacts from integrated wiki pages when slide support is enabled
- `pdf` — handle PDF-specific extraction, OCR, splitting, merging, and output tasks
- `obsidian-markdown` — edit Obsidian-flavored Markdown correctly when Obsidian-specific syntax matters
- `obsidian-cli` — interact with a running Obsidian instance when needed
- `obsidian-bases` — create or edit `.base` files
- `json-canvas` — create or edit `.canvas` files
- `defuddle` — clean normal web pages into markdown before ingest

Important distinction:

- `wiki-ingest` reads from `raw/` or `inbox/` and writes to `wiki/sources/`
- `wiki-integrate` reads from `wiki/sources/` and writes to the broader wiki
- `wiki-search` reads the wiki to answer questions
- `wiki-audit` evaluates the wiki and records findings in `wiki/logs/audits.md`
- `pdf` prepares or produces PDFs but should not replace `wiki-ingest` or `wiki-integrate`

Do not collapse these workflows into one giant operation unless the user explicitly asks.

## Skill source of truth

Edit canonical skills in `skills/`.

The hidden harness directories are generated mirrors. If Python helpers are present, refresh them with:

```text
python -m wiki_tools sync-skills
```

Otherwise copy `skills/` into `.agents/skills/`, `.claude/skills/`, and `.gemini/skills/` manually.

## Core operating principles

1. Raw sources are the source of truth.
2. Wiki pages are synthesized working knowledge, not raw evidence.
3. Every important claim in the wiki should trace back to one or more source pages.
4. Prefer small, composable pages over long monolithic summaries.
5. Use links aggressively with Obsidian-style wikilinks: `[[page-slug]]`.
6. Flag contradictions instead of silently resolving them.
7. Preserve uncertainty with sections such as `Known`, `Inferred`, `Uncertain`, and `Open questions`.
8. Never invent citations or provenance.
9. Do not delete or overwrite prior synthesis without recording why.

## Page conventions

Each wiki page should use this frontmatter:

---
title: Human-readable title
type: source | concept | person | organization | project | dataset | decision | synthesis | question | log
status: seed | active | stable | stale | deprecated
created: YYYY-MM-DD
updated: YYYY-MM-DD
source_refs: []
tags: []
---

## Large source workflow

Large books, reports, and other long-form works should not usually be ingested as a single source page.

Preferred flow:

1. Preserve the original under `raw/books/`, `raw/reports/`, or another appropriate raw folder.
2. Split or extract logical units when useful.
3. Create one `wiki/sources/` page per logical unit.
4. Only then create or update higher-level synthesis pages.
5. Record the work in `wiki/logs/maintenance.md`.

## Obsidian compatibility

This wiki is plain Markdown first and Obsidian-friendly second.

Prefer:

- `[[wikilinks]]` for internal links
- consistent frontmatter
- sparing use of tags
- callouts when they materially improve clarity

Avoid shipping personal editor state or tool-specific clutter.
