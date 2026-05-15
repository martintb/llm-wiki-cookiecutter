# Obsidian Guide

This template is plain Markdown first and Obsidian-friendly second.

That means generated wikis should work well in Obsidian without turning the repository into an Obsidian-only project.

## Bundled Obsidian Skills

This template vendors the most useful local skills from `kepano/obsidian-skills` directly into the repo-local `skills/` tree:

- `obsidian-markdown`
- `obsidian-cli`
- `obsidian-bases`
- `json-canvas`
- `defuddle`

Because they live in `skills/`, they are copied into:

- `.agents/skills/`
- `.claude/skills/`
- `.gemini/skills/`

via:

```bash
python3 scripts/sync_skills.py
```

Generated repos get the same packaged skills, and `python -m wiki_tools sync-skills` refreshes their mirrors the same way.

## Recommended Vault Setup

Open the generated repository itself as an Obsidian vault.

The wiki layout already fits Obsidian well:

- `[[wikilinks]]` for internal navigation
- frontmatter on every page
- small composable notes instead of large monoliths
- folder-based organization that still works outside Obsidian

Use Obsidian for:

- backlink browsing
- graph exploration
- quick note edits
- canvas and base files when they add value

## PDF Skill Guidance

This template also ships a repo-local `pdf` skill for PDF-oriented wiki work.

Use it when the task involves:

- extracting or OCRing a source PDF
- splitting, merging, or rotating PDF pages
- filling forms
- producing a PDF artifact

Recommended flow for source material:

1. Preserve the original under `raw/`.
2. Use `pdf` if extraction, OCR, or transformation is required.
3. Use `wiki-ingest` to create or update the source summary in `wiki/sources/`.
4. Use `wiki-integrate` only after the source summary exists.

## Official Anthropic PDF Skill

If you want the official Anthropic `pdf` skill specifically, install it separately in the relevant harness environment rather than treating it as a canonical repo-local skill.

That keeps this template's `skills/` directory limited to the skills the repo intends to own and sync.

## Maintainer Notes

- Keep repo-local packaged skills in `skills/`.
- If you update bundled Obsidian skills, update `skills/` first and then run `python3 scripts/sync_skills.py`.
- Prefer documentation and portable markdown conventions over shipping user-specific Obsidian state.
