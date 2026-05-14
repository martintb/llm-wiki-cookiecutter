# LLM Wiki Cookiecutter

`llm-wiki-cookiecutter` is a project template for standing up a portable, markdown-based knowledge wiki that can be maintained by LLM agents instead of by hand-written ad hoc notes.

The generated wiki is designed to work across the major repository-aware harnesses:

- Codex via `AGENTS.md` and `.agents/skills/`
- Claude Code via `CLAUDE.md` and `.claude/skills/`
- Gemini via `GEMINI.md` and `.gemini/skills/`

The template produces a repo with:

- a durable wiki folder structure
- page and source-summary templates
- local wiki workflow skills
- optional Python helpers for page creation, validation, and skill syncing
- optional slide directories for Marp-style deck generation

## What This Tool Generates

Each rendered repo is an LLM-maintained wiki with these operating layers:

1. `raw/` for immutable evidence
2. `wiki/` for synthesized knowledge
3. `templates/` for repeatable page structures
4. `skills/` for reusable workflows such as ingest, integrate, search, audit, and slides
5. hidden skill mirrors for Codex, Claude Code, and Gemini
6. optional `wiki_tools` helpers for operational checks

## Quick Start

Install `cookiecutter`:

```bash
python3 -m pip install cookiecutter
```

Render directly from a GitHub repository:

```bash
cookiecutter gh:<owner>/<repo>
```

Example:

```bash
cookiecutter gh:tbm/llm-wiki-cookiecutter
```

Render directly from a specific branch or tag on GitHub:

```bash
cookiecutter https://github.com/<owner>/<repo>.git --checkout <branch-or-tag>
```

If you already have the template cloned locally, render from the local path:

```bash
cookiecutter /path/to/llm-wiki-cookiecutter
```

To generate into the current directory instead of the default output location:

```bash
cookiecutter gh:<owner>/<repo> --output-dir .
```

The template will prompt for:

- project name
- repository slug
- wiki title
- maintainer name
- license
- whether to include slide scaffolding
- whether to include the Python helper tools

## Generated Wiki Preview

If you want to review the produced wiki layout and operating model before rendering anything, read [docs/generated-wiki-guide.md](/Users/tbm/software/llm-wiki-cookiecutter/docs/generated-wiki-guide.md).

That document mirrors the README shipped inside each generated wiki repo.

## Harness Compatibility

The canonical skills in this template live in `skills/`.

They are mirrored into harness-native install locations:

- `.agents/skills/`
- `.claude/skills/`
- `.gemini/skills/`

Refresh those mirrors with:

```bash
python3 scripts/sync_skills.py
```

Check for drift without rewriting files:

```bash
python3 scripts/sync_skills.py --check
```

## Developing The Template

Install the tool needed to render and test the template:

```bash
python3 -m pip install cookiecutter
```

Run the skill mirror sync:

```bash
python3 scripts/sync_skills.py
```

Run tests:

```bash
python3 -m unittest discover -s tests -v
```

The tests render a temporary project from the cookiecutter template and verify:

- expected wiki files and directories exist
- skills are mirrored into all harness-specific locations
- no copied domain-specific strings remain
- the generated `wiki_tools` commands work on a clean scaffold

## Maintainer Notes

- Edit canonical skills in `skills/`, not in hidden mirror directories.
- Keep root `AGENTS.md`, `CLAUDE.md`, and `GEMINI.md` aligned with the generated versions.
- Keep `docs/generated-wiki-guide.md` aligned with the README rendered into generated projects.
- Prefer generic examples and placeholders over domain-specific examples.
