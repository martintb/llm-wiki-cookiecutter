---
name: wiki-ingest
description: Turn raw source material into structured source summaries for the LLM Wiki.
---

# Wiki Ingest Skill

Use this skill when the user wants material from `raw/` or `inbox/` turned into a reusable page in `wiki/sources/`.

## Goal

Produce a source summary with:

- provenance
- concise summary
- key claims
- evidence anchors
- notable entities
- relevant wiki links
- suggested follow-up pages for later integration

## Workflow

1. Identify the source type.
2. Preserve provenance without inventing missing details.
3. Use the most specific matching template in `templates/`.
4. Create or update the source-summary page.
5. Extract durable facts, definitions, examples, limitations, and open questions.
6. Record suggested integration targets instead of broad synthesis.
7. Append a short entry to `wiki/logs/maintenance.md`.

## Quality bar

- Keep summaries dense and reusable.
- Preserve uncertainty explicitly.
- Prefer concrete evidence anchors over vague prose.
- Treat raw material as evidence, not as a place to rewrite.
