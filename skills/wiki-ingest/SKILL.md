---
name: wiki-ingest
description: Turn primary source documents into structured source summaries for the LLM Wiki. Use for book chapters, papers, webpages, reports, notes, transcripts, GitHub READMEs, slide decks, datasets, tabular exports, and other raw/ source material.
---

# Wiki Ingest Skill

Use this skill when the user asks to ingest, process, summarize, extract, clip, parse, or add a primary source to the LLM Wiki.

This skill converts raw source material into a structured source summary. It does **not** perform broad integration into the rest of the wiki except for minimal links and suggested follow-up pages.

Primary sources may include:

- book chapters
- individual papers
- webpages
- reports
- white papers
- standards
- proposals
- notes
- meeting transcripts
- slide decks
- GitHub repositories or READMEs
- manuals
- emails
- datasets or dataset descriptions
- tabular exports or data bundles such as CSV/TSV/XLS/XLSX directories
- other files under `raw/` or `inbox/`

## Core principle

Raw material is evidence. Source summaries are structured, reusable summaries. Broader synthesis belongs to `wiki-integrate`, not `wiki-ingest`.

## Expected directories

- `raw/` — immutable source material
- `inbox/` — unprocessed or triaged source material
- `wiki/sources/` — source-summary pages created by this skill
- `wiki/logs/maintenance.md` — processing log
- `templates/` or `/template/` — optional templates to prefer when available

## Template lookup

Before creating any source summary, look for applicable templates.

Search these locations, in this order:

1. `/template/`
2. `/templates/`
3. `template/`
4. `templates/`
5. `wiki/templates/`

Prefer the most specific matching template available.

Suggested template names:

- `source.md`
- `source-summary.md`
- `paper.md`
- `book-chapter.md`
- `webpage.md`
- `report.md`
- `standard.md`
- `meeting-notes.md`
- `github-repo.md`
- `slide-deck.md`
- `dataset-table.md`
- `dataset.md`

If no suitable template exists, use the default template in this skill.

Do not fail merely because no template is found. Use the default template and note that no external template was available.

## Ingest workflow

### 1. Identify source type

Determine whether the source is a:

- book chapter
- paper
- webpage
- report
- standard
- transcript
- slide deck
- GitHub repository
- dataset
- tabular dataset or dataset bundle
- miscellaneous source

If uncertain, choose `source_type: unknown` and explain the uncertainty in the summary.

### 2. Preserve source provenance

Record as much provenance as available:

- title
- author(s)
- organization
- publication venue
- publisher
- year/date
- URL
- DOI
- ISBN
- file path
- page range
- date clipped or downloaded
- snapshot or release label
- access notes
- license or copyright status, if known

Never invent missing provenance.

### 3. Create a source-summary page

Create a page under:

```text
wiki/sources/<source-slug>.md
```

For books or multi-part sources, use:

```text
wiki/sources/<book-slug>/ch01-<chapter-slug>.md
wiki/sources/<book-slug>/ch02-<chapter-slug>.md
```

For papers, use:

```text
wiki/sources/<paper-slug>.md
```

For webpages, use:

```text
wiki/sources/<webpage-slug>.md
```

### 4. Extract durable information

Extract:

- concise summary
- key claims
- definitions
- methods
- frameworks
- evidence
- examples
- assumptions
- limitations
- people
- organizations
- datasets
- instruments
- software/tools
- relevant concepts
- contradictions or tensions
- open questions
- likely wiki pages to update later

For tabular datasets, also extract:

- file inventory
- row and column counts
- schema and identifiers
- units and missing-value conventions
- snapshot or time coverage
- duplicate files or repeated exports
- obvious normalization or naming issues

### 5. Add minimal links

Add obvious wikilinks to already-known pages if possible.

Examples:

- `[[SAXS]]`
- `[[SANS]]`
- `[[autonomous-experimentation]]`
- `[[uncertainty-quantification]]`
- `[[AFL]]`

Do not create a new concept page for every term during ingestion. Instead, list candidate concepts under “Suggested wiki updates”.

### 6. Avoid premature synthesis

Do not broadly rewrite existing concept, project, or synthesis pages during ingestion unless the user explicitly asks.

The output of this skill should be a high-quality source summary that can later be consumed by `wiki-integrate`.

### 7. Log the ingest

Append to `wiki/logs/maintenance.md`:

- source processed
- source-summary page created
- source type
- raw source path
- unresolved issues
- suggested integration targets

## Default source-summary template

Use this template if no better template is available under `/template` or equivalent template directories.

```markdown
---
title:
type: source
source_type:
status: active
created:
updated:
source_refs: []
raw_source:
url:
doi:
isbn:
authors: []
organizations: []
published:
clipped:
page_range:
tags: []
related: []
---

# Title

## Provenance

- Raw source:
- URL:
- DOI / ISBN:
- Author(s):
- Organization(s):
- Publication / venue:
- Date:
- Page range:
- Access / license notes:

## Summary

A concise summary of the source.

## Key claims

- Claim 1
- Claim 2
- Claim 3

## Important definitions

- **Term** — definition.

## Methods, frameworks, or models

- Method or framework and why it matters.

## Evidence and examples

- Example or evidence item.
- Include page numbers, section names, figure numbers, or quotation anchors when available.

## Assumptions and limitations

- Assumption or limitation.

## Entities

### People

- Person — relevance.

### Organizations

- Organization — relevance.

### Instruments, datasets, software, or tools

- Entity — relevance.

## Connections to existing wiki pages

- `[[page]]` — relationship.

## Suggested wiki updates

These are suggested targets for `wiki-integrate`.

- `[[concept-page]]` — what should be added or updated.
- `[[project-page]]` — what should be added or updated.
- `[[synthesis-page]]` — possible synthesis need.

## Contradictions or tensions

- Tension or contradiction with source/context, if any.

## Open questions

- Question 1
- Question 2

## Relevance to the user’s work

Explain why this source may matter for the user’s research, writing, proposals, software, experiments, strategy, or planning.

## Processing notes

- Template used:
- Ingested by:
- Date:
- Issues encountered:
```

## Special handling: tabular datasets

For CSV/TSV/XLS/XLSX files or `raw/data/` bundles:

- Treat the dataset bundle as the source when multiple files describe the same release.
- Record the component files explicitly rather than pretending one file is the whole source.
- Preserve schema details: column names, identifiers, units, missing-value markers, and change-log semantics.
- Capture structural facts that matter later: row counts, duplicate exports, snapshot labels, and whether files are machine-readable or presentation-oriented.
- Distinguish source-supported observations from inferred cleanup recommendations.
- Do not normalize or rewrite the raw data during ingest; record cleanup issues under limitations or data-quality notes instead.
- If a supporting PDF or README explains the dataset, include it in provenance and use it to interpret the tables.

Recommended sections for a table-oriented source summary:

- `## Dataset structure`
- `### Table inventory`
- `### Schema notes`
- `### Coverage`
- `## Data quality and normalization issues`

## Special handling: book chapters

For a book, proceedings volume, report, thesis, or long PDF, do not create one giant source summary.

Use one source-summary page per chapter or logical unit.

Each chapter page should include:

- chapter title
- chapter number
- page range
- chapter-specific summary
- key claims
- definitions
- methods
- examples
- open questions
- suggested integration targets

After all chapters are ingested, create or update a book-level source index, but leave cross-chapter synthesis to `wiki-integrate`.

## Special handling: webpages

For clipped webpages:

- Preserve the original URL.
- Preserve the clipping date.
- Distinguish extracted page content from any AI-generated summary.
- Do not treat Web Clipper AI summaries as authoritative.
- Use highlights as evidence pointers, not as the entire source.

## Special handling: papers

For papers, extract:

- research question
- contribution
- methods
- dataset/system/materials
- key results
- figures/tables worth revisiting
- limitations
- relation to prior work
- relation to the user’s work
- possible follow-up citations

## Special handling: GitHub repositories

For repositories, extract:

- repo purpose
- installation/use pattern
- key files
- maturity
- license, if available
- maintenance status, if available
- relation to the wiki or user’s tools
- whether it should be tested, forked, watched, or ignored

## Output expectations

At the end of an ingest operation, report:

- source-summary page created
- raw source used
- template used
- important open questions
- suggested next integration targets

Do not dump the entire source summary into chat unless the user asks.
