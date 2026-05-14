---
name: wiki-ingest
description: Turn raw source material into structured source summaries for the wiki.
---

# Wiki Ingest Skill

Use this skill when the user wants material from `raw/` or `inbox/` turned into a reusable source-summary page in `wiki/sources/`.

## Workflow

1. Identify the source type.
2. Preserve provenance.
3. Use the most specific matching template in `templates/`.
4. Create or update the source-summary page.
5. Extract durable facts, claims, definitions, examples, limitations, entities, and open questions.
6. Record suggested integration targets instead of broad synthesis.
7. Append a short maintenance log entry.

## Quality bar

- Never invent provenance.
- Keep the summary dense and reusable.
- Preserve uncertainty explicitly.
- Prefer evidence anchors over vague descriptions.
