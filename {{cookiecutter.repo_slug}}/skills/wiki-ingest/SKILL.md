---
name: wiki-ingest
description: Turn raw source material into structured source summaries for the wiki.
---

# Wiki Ingest Skill

Use this skill when the user wants material from `raw/` or `inbox/` turned into a reusable source-summary page in `wiki/sources/`.

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
2. Preserve provenance.
3. Use the most specific matching template in `templates/`.
4. Create or update the source-summary page.
5. Extract durable facts, claims, definitions, examples, limitations, entities, and open questions.
6. Record suggested integration targets instead of broad synthesis.
7. Append a short maintenance log entry.

## Defaults

Unless the user explicitly says otherwise:

- choose the destination page path under `wiki/sources/`
- choose the best matching template automatically
- preserve provenance
- include key claims, evidence anchors, entities, and open questions
- avoid broad edits outside the source summary and maintenance log

The user should not need to specify template selection, section structure, or logging behavior.

## Quality bar

- Never invent provenance.
- Keep the summary dense and reusable.
- Preserve uncertainty explicitly.
- Prefer evidence anchors over vague descriptions.
