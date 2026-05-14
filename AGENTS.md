# AGENTS.md — LLM Wiki Cookiecutter Maintainer

You are maintaining a cookiecutter template that generates portable, LLM-maintained markdown wikis.

The repo has two distinct responsibilities:

1. Maintain the template itself.
2. Ensure the generated wiki repos are operational in major agent harnesses.

## Repository layout

- `cookiecutter.json` — generator prompts.
- `hooks/` — cookiecutter validation and post-generation setup.
- `{{cookiecutter.repo_slug}}/` — the generated wiki project template.
- `skills/` — canonical, human-edited wiki skills.
- `.agents/skills/` — Codex-compatible installed skill mirror.
- `.claude/skills/` — Claude Code-compatible installed skill mirror.
- `.gemini/skills/` — Gemini-compatible installed skill mirror.
- `scripts/sync_skills.py` — keeps the hidden harness skill trees in sync with `skills/`.
- `docs/generated-wiki-guide.md` — preview of the README shipped in generated wiki repos.
- `tests/` — template and rendering verification.

## Skill source of truth

The canonical skill definitions live under `skills/`.

Do not hand-edit the mirrored harness directories unless the task is specifically to test sync drift. Update `skills/` first, then run:

```text
python3 scripts/sync_skills.py
```

The hidden directories are installation targets, not the authoring location.

## Generated wiki contract

Each generated wiki repo should include:

- `AGENTS.md`, `CLAUDE.md`, and `GEMINI.md`
- `skills/` plus installed mirrors under `.agents/skills/`, `.claude/skills/`, and `.gemini/skills/`
- `raw/`, `inbox/`, `wiki/`, optional `slides/`, and `templates/`
- optional `wiki_tools` helper commands for page creation, validation, and skill syncing

## Generated wiki workflow model

The generated wikis use these workflows:

- `wiki-ingest` — convert raw material into `wiki/sources/` summaries
- `wiki-integrate` — turn source summaries into durable concept, project, decision, and synthesis pages
- `wiki-search` — answer questions from the wiki before consulting raw sources
- `wiki-audit` — review structure, links, provenance, and integration gaps
- `wiki-slides` — create slide artifacts from integrated wiki pages when slides are enabled

Do not collapse these workflows into one step unless the user explicitly asks.

## Generated wiki page contract

Wiki pages should use this frontmatter:

---
title: Human-readable title
type: source | concept | person | organization | project | dataset | decision | synthesis | question | log
status: seed | active | stable | stale | deprecated
created: YYYY-MM-DD
updated: YYYY-MM-DD
source_refs: []
tags: []
---

Generated repos should preserve these principles:

1. Raw sources are the source of truth.
2. Wiki pages are synthesized working knowledge, not raw evidence.
3. Important claims should trace back to source summaries.
4. Prefer small, composable pages over monoliths.
5. Use wikilinks aggressively: `[[page-slug]]`.
6. Flag contradictions rather than silently resolving them.
7. Preserve uncertainty explicitly.
8. Do not invent citations or provenance.

## Obsidian compatibility

Generated repos are plain Markdown first and Obsidian-friendly second.

Prefer:

- `[[wikilinks]]` for internal navigation
- consistent frontmatter
- callouts when they materially improve readability
- optional Obsidian-specific files only when they are clearly additive

Avoid shipping user-specific editor state.
