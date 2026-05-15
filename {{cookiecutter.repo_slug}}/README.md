# {{cookiecutter.wiki_title}}

`{{cookiecutter.wiki_title}}` is an LLM-maintained markdown wiki for accumulating evidence, source summaries, concepts, projects, decisions, synthesis, and open questions over time.

This repo is designed to work with major repository-aware harnesses:

- Codex via `AGENTS.md` and `.agents/skills/`
- Claude Code via `CLAUDE.md` and `.claude/skills/`
- Gemini via `GEMINI.md` and `.gemini/skills/`

It also opens cleanly as an Obsidian vault.

## Directory Map

- `raw/` — immutable evidence and source material
- `inbox/` — unprocessed material waiting for triage
- `wiki/sources/` — source summaries
- `wiki/concepts/` — recurring concepts and methods
- `wiki/people/` — people pages
- `wiki/organizations/` — organization pages
- `wiki/projects/` — project pages
- `wiki/datasets/` — dataset pages
- `wiki/decisions/` — durable decisions and rationale
- `wiki/synthesis/` — higher-level cross-source synthesis
- `wiki/questions/` — durable open questions
- `wiki/logs/` — maintenance and audit logs
- `templates/` — page templates
- `skills/` — canonical local workflow skills

## Recommended Workflow

1. Put new evidence in `raw/` or `inbox/`.
2. Use `wiki-ingest` to create or improve `wiki/sources/` summaries.
3. Use `wiki-integrate` to update concept, synthesis, project, decision, and question pages.
4. Use `wiki-search` before answering from scratch.
5. Use `wiki-audit` periodically to catch structural or provenance issues.

For a full step-by-step example, read [docs/workflow-example.md](docs/workflow-example.md).

For Obsidian setup and bundled companion skills, read [docs/obsidian.md](docs/obsidian.md).

## Harness Files And Skills

The repo ships with three harness entrypoints:

- `AGENTS.md`
- `CLAUDE.md`
- `GEMINI.md`

The canonical skill source is `skills/`.

That includes the wiki workflow skills, bundled Obsidian companion skills, and the repo-local `pdf` skill.

Installed skill mirrors live at:

- `.agents/skills/`
- `.claude/skills/`
- `.gemini/skills/`

If Python helpers are enabled, refresh those mirrors with:

```bash
python -m wiki_tools sync-skills
```

## Optional Helper Commands

If this repo was generated with Python helpers enabled, these commands are available:

```bash
python -m wiki_tools new-page --type concept --title "Example Concept"
python -m wiki_tools check --strict
python -m wiki_tools sync-skills
```

`new-page` creates a page from `templates/` in the canonical wiki folder for that page type.

`check` verifies:

- required files and directories
- frontmatter shape
- allowed page types and statuses
- broken wikilinks
- skill mirror drift across harness directories

## Page Types

Supported page types:

- `source`
- `concept`
- `person`
- `organization`
- `project`
- `dataset`
- `decision`
- `synthesis`
- `question`
- `log`

## Slides

{% if cookiecutter.include_slides == "y" %}
Slide support is enabled.

Use:

- `slides/drafts/` for working decks
- `slides/final/` for final decks or exports
- `slides/assets/` for images and diagrams

The `wiki-slides` skill should prefer integrated wiki pages over raw sources.
{% else %}
Slide support was disabled when this repo was generated.
{% endif %}

## Maintainer Notes

- Preserve raw sources.
- Keep source trails explicit.
- Prefer updating an existing page over creating a duplicate.
- Record maintenance work in `wiki/logs/maintenance.md`.
