# AGENTS.md — LLM Wiki Maintainer

You are maintaining an LLM Wiki: a persistent, interlinked markdown knowledge base built from curated raw sources.

The goal is not to answer from scratch every time. The goal is to compile knowledge once, keep it current, and make future answers easier, better cited, and more synthetic.

## Directory structure

- `raw/` — immutable source material. Do not rewrite, summarize in place, or delete raw sources unless explicitly asked.
- `wiki/` — LLM-maintained markdown pages.
- `wiki/index.md` — master index and navigation map.
- `wiki/sources/` — one source-summary page per raw source.
- `wiki/concepts/` — concepts, theories, methods, and recurring ideas.
- `wiki/people/` — people and their relevance.
- `wiki/organizations/` — institutions, companies, agencies, facilities, consortia.
- `wiki/projects/` — projects, programs, collaborations, proposals.
- `wiki/instruments/` — instruments, beamlines, measurement platforms.
- `wiki/datasets/` — datasets and data products.
- `wiki/decisions/` — durable decisions, assumptions, and rationale.
- `wiki/synthesis/` — cross-source analyses and higher-level summaries.
- `wiki/questions/` — open questions, TODOs, uncertainties, and follow-up searches.
- `wiki/logs/` — append-only maintenance log.

## Wiki skill dispatch

Use the wiki skills as follows:

- Use `wiki-ingest` when converting raw source material into structured source-summary pages.
- Use `wiki-integrate` when incorporating source summaries into concepts, synthesis, projects, decisions, questions, and other durable wiki pages.
- Use `wiki-search` when answering questions from the wiki.
- Use `wiki-audit` when checking wiki health, links, duplication, staleness, source support, and integration gaps.

Important distinction:

- `wiki-ingest` reads primary material from `raw/` or `inbox/` and writes to `wiki/sources/`.
- `wiki-integrate` reads `wiki/sources/` and writes to the broader wiki.
- `wiki-search` reads the wiki to answer questions.
- `wiki-audit` evaluates the wiki itself and records findings in `wiki/logs/audits.md`.

Do not collapse these workflows into one giant operation unless the user explicitly asks. In general:

```text
raw source → wiki-ingest → source summary → wiki-integrate → concepts/synthesis/projects → wiki-search/wiki-audit
```

## Slide-generation workflow

The wiki can be used as source material for slide decks.

Prefer generating slides from integrated wiki pages, especially `wiki/synthesis/`, `wiki/concepts/`, and `wiki/projects/`, rather than directly from raw sources.

Recommended workflow:

1. Use `wiki-search` to identify relevant pages.
2. Create a slide brief: audience, goal, duration, desired tone, and source pages.
3. Create a slide outline before writing a full deck.
4. Generate slides as Markdown, preferably Marp-compatible `.marp.md`.
5. Keep slides visually sparse.
6. Put evidence trails, caveats, and source links in speaker notes.
7. Use source-summary pages for evidence when needed.
8. Save drafts under `slides/drafts/`.
9. Save final decks or exported files under `slides/final/`.
10. If a deck contains durable synthesis, ingest or integrate that synthesis back into the wiki.

Do not treat slides as a replacement for the wiki. Slides are presentation artifacts derived from the wiki.


## Python   

If you need Python, there should be either a python venv already loaded or a .venv in the root directory of the project which can be activated with `source .venv/bin/activate`

## Obsidian skills

This wiki is intended to be maintained as an Obsidian-compatible vault. The agent should assume that the Obsidian skills from `kepano/obsidian-skills` have been installed and should use them when relevant.

Installed / expected skills include:

- `obsidian-markdown` — use when creating or editing Obsidian-flavored Markdown, including wikilinks, embeds, callouts, frontmatter/properties, tags, and other Obsidian syntax.
- `obsidian-bases` — use when creating or editing Obsidian Bases (`.base`) for structured views, filters, summaries, formulas, and dashboards.
- `json-canvas` — use when creating or editing Obsidian Canvas / JSON Canvas files (`.canvas`) for concept maps, workflows, source graphs, and project maps.
- `obsidian-cli` — use when interacting with the vault through the Obsidian CLI, including vault inspection, plugin/theme workflows, or automation tasks.
- `defuddle` — use when ingesting webpages so that clean Markdown is extracted before summarization or wiki integration.

When editing this wiki, prefer Obsidian-native constructs where useful:

- Use `[[wikilinks]]` for internal links.
- Use aliases where helpful: `[[autonomous-formulation-lab|AFL]]`.
- Use frontmatter/properties consistently.
- Use tags sparingly and systematically.
- Use callouts for warnings, open questions, contradictions, and important notes.
- Use embeds only when they improve navigation or synthesis.
- Use Canvas files for maps of projects, source relationships, experiment workflows, and concept dependencies.
- Use Bases for dashboards such as sources by status, open questions, stale pages, proposal materials, people/organizations, and project pages.

Do not use Obsidian-specific syntax gratuitously. The wiki should remain readable as plain Markdown, but should take advantage of Obsidian features where they improve navigation, maintenance, or synthesis.

## Core operating principles

1. Raw sources are the source of truth.
2. Wiki pages are synthesized working knowledge, not raw evidence.
3. Every important claim in the wiki should trace back to one or more source pages.
4. Prefer small, composable pages over long monolithic summaries.
5. Use links aggressively with Obsidian-style wikilinks: `[[page-slug]]`.
6. Flag contradictions instead of silently resolving them.
7. Preserve uncertainty. Use sections such as “Known”, “Inferred”, “Uncertain”, and “Needs verification”.
8. When a user asks a useful question, consider whether the answer should become a new wiki page.
9. Never invent citations or sources.
10. Do not delete or overwrite prior synthesis without recording why.

## Page conventions

Each wiki page should use this frontmatter:

---
title: Human-readable title
type: source | concept | person | organization | project | instrument | dataset | decision | synthesis | question | log
status: seed | active | stable | stale | deprecated
created: YYYY-MM-DD
updated: YYYY-MM-DD
source_refs: []
tags: []
---

## Large PDF and book-ingestion workflow

Large PDFs, especially books, should not be ingested as a single source page.

For books, proceedings, reports, theses, manuals, or long PDFs:

1. Preserve the original PDF unchanged under `raw/books/` or `raw/reports/`.
2. Create a metadata note for the source.
3. Identify logical boundaries such as chapters, sections, appendices, or articles.
4. Extract or split the text into one raw markdown file per logical unit.
5. Preserve page numbers whenever possible.
6. Create one `wiki/sources/` page per chapter or logical unit.
7. Only after individual units are summarized, create a whole-source synthesis page.
8. Update concept, project, method, dataset, and synthesis pages after chapter-level processing, not before.
9. Do not create a new concept page for every term. Create concept pages only for ideas likely to recur.
10. Record all processing in `wiki/logs/maintenance.md`.

For each chapter or section, extract:

- summary
- key claims
- important definitions
- methods or frameworks
- examples and evidence
- people, organizations, datasets, instruments, and tools
- links to existing wiki pages
- possible new wiki pages
- contradictions or tensions
- open questions
- relevance to the user’s work

The original PDF and extracted raw text are evidence. The `wiki/sources/` pages are LLM-generated source summaries. The `wiki/concepts/` and `wiki/synthesis/` pages are integrated knowledge.

Use this body structure when applicable:

# Title

## Summary
Short, high-density summary.

## Key points
- Bullet points with the most reusable facts.

## Evidence
- Link to source pages or raw source references.

## Connections
- `[[related-page]]` — short explanation of relationship.

## Open questions
- Questions that remain unresolved.

## Maintenance notes
- What changed and why.

## Ingest workflow

When ingesting a new source:

1. Save or identify the raw source in `raw/`.
2. Create a source page in `wiki/sources/`.
3. Extract:
   - entities
   - concepts
   - methods
   - datasets
   - claims
   - decisions
   - uncertainties
   - contradictions
4. Update existing relevant pages.
5. Create new pages only when the concept is likely to recur.
6. Add wikilinks between old and new pages.
7. Update `wiki/index.md` if the source introduces a major topic.
8. Append a short entry to `wiki/logs/maintenance.md`.

## Query workflow

When answering a question:

1. Search the wiki first.
2. Read the most relevant source, concept, project, and synthesis pages.
3. If wiki coverage is insufficient, say so clearly.
4. Use raw sources only when needed to verify or deepen a claim.
5. Answer with links to relevant wiki pages.
6. If the answer produces durable synthesis, offer to file it under `wiki/synthesis/`.

## Audit workflow

Periodically audit the wiki for:

- orphan pages
- missing backlinks
- stale claims
- contradictory claims
- duplicate pages
- pages with no source references
- important concepts mentioned but not linked
- source pages not integrated into concept/project pages
- open questions that can now be resolved

Record audit results in `wiki/logs/audits.md`.

## Style

Write in concise technical prose. Prefer clear claims over vague summaries. Preserve caveats. Avoid hype. Distinguish source-supported facts from interpretation.

## Domain priorities

This wiki is especially intended for scientific, technical, and programmatic knowledge involving:

- autonomous materials measurement
- AFL-style autonomous formulation workflows
- SAXS, SANS, USAXS, RSoXS, scattering, and multimodal characterization
- AI/ML for experimental design and control
- virtual instruments and digital twins
- uncertainty quantification and provenance
- soft matter, formulations, surfactants, polymers, nanoparticles, LNPs
- NIST, user facilities, workshops, proposals, and collaborations