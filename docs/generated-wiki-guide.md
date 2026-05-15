# Generated Wiki Guide

This document previews the README that ships inside each rendered wiki repo.

For a concrete end-to-end usage example, also read [Workflow Example](workflow-example.md).

For Obsidian setup and packaged companion skills, also read [Obsidian Guide](obsidian.md).

## Purpose

The generated repository is a portable, markdown-first knowledge base for evidence-backed notes, source summaries, synthesis pages, decisions, and open questions.

It is structured for LLM-assisted maintenance rather than one-off chat answers.

## Root Files

- `AGENTS.md` — shared repo operating contract
- `CLAUDE.md` — Claude Code entrypoint
- `GEMINI.md` — Gemini entrypoint
- `README.md` — day-to-day wiki instructions
- `docs/obsidian.md` — Obsidian setup and companion skill guidance
- `skills/` — canonical local workflow skills
- `.agents/skills/` — Codex-installed skill mirror
- `.claude/skills/` — Claude Code-installed skill mirror
- `.gemini/skills/` — Gemini-installed skill mirror
- `templates/` — page templates for common wiki page types
- optional `wiki_tools/` — helper commands for new pages, checks, and skill syncing

## Core Directories

- `raw/` — immutable evidence
- `inbox/` — unprocessed material
- `wiki/sources/` — source summaries
- `wiki/concepts/` — reusable concepts and methods
- `wiki/people/` — people pages
- `wiki/organizations/` — organization pages
- `wiki/projects/` — project pages
- `wiki/datasets/` — dataset pages
- `wiki/decisions/` — durable decisions and rationale
- `wiki/synthesis/` — cross-source synthesis
- `wiki/questions/` — durable open questions
- `wiki/logs/` — maintenance and audit logs
- optional `slides/` — draft and final presentation artifacts

## Recommended Workflow

1. Put new evidence in `raw/` or `inbox/`.
2. Use `wiki-ingest` to create or improve `wiki/sources/` summaries.
3. Use `wiki-integrate` to update concept, synthesis, project, decision, and question pages.
4. Use `wiki-search` before answering questions from scratch.
5. Use `wiki-audit` periodically to catch gaps and structural issues.

For large books, preserve `raw/books/<book-title>/full_book.pdf`, use the local `pdf` skill to split it into `raw/books/<book-title>/chapters/ch01-<chapter-title>.pdf` style files, and then ingest those logical units instead of one giant source page.

## Optional Helper Commands

If the generated repo includes Python helpers:

```bash
python -m wiki_tools new-page --type concept --title "Example Concept"
python -m wiki_tools check --strict
python -m wiki_tools sync-skills
```

## Skill Mirrors

Edit canonical skills in `skills/`, then refresh the harness-specific mirrors:

```bash
python -m wiki_tools sync-skills
```

The hidden directories should be treated as generated installation targets.

The generated repo includes:

- core wiki workflow skills
- bundled Obsidian companion skills
- a repo-local `pdf` skill
