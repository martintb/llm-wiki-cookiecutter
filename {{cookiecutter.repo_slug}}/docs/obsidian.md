# Obsidian Guide

This wiki is plain Markdown first and Obsidian-friendly second.

Open the repository itself as an Obsidian vault if you want backlink browsing, graph views, quick note edits, or Obsidian-native files like canvases and bases.

## Bundled Skills

This repo already includes these packaged companion skills in `skills/`:

- `obsidian-markdown`
- `obsidian-cli`
- `obsidian-bases`
- `json-canvas`
- `defuddle`
- `pdf`

Those canonical repo-local skills are mirrored into:

- `.agents/skills/`
- `.claude/skills/`
- `.gemini/skills/`

If Python helpers are enabled, refresh them with:

```bash
python -m wiki_tools sync-skills
```

## Recommended Workflow

Use the bundled skills this way:

- `pdf` for OCR, extraction, merging, splitting, and other PDF-specific work
- `wiki-ingest` after PDF preparation to create or update `wiki/sources/`
- `wiki-integrate` only after the source summary exists
- `obsidian-markdown` when editing Obsidian-flavored Markdown directly
- `obsidian-cli` when interacting with a running Obsidian instance
- `obsidian-bases` for `.base` files
- `json-canvas` for `.canvas` files
- `defuddle` when cleaning normal web pages into markdown before ingest

For large books, keep the source as `raw/books/<book-title>/full_book.pdf`, build a `chapters/manifest.json`, and split the book into `raw/books/<book-title>/chapters/ch01-<chapter-title>.pdf` style files before ingesting them.

The local `pdf` skill includes a bundled `skills/pdf/scripts/split_book.py` helper plus reference guidance for `pypdf`, `pdf2image`, and `pytesseract` when the book needs OCR-assisted chapter detection.

## Official Anthropic PDF Skill

If you want the official Anthropic `pdf` skill specifically, install it separately in your harness environment.

This repo ships its own local `pdf` skill so the generated wiki remains self-contained.
