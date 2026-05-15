---
name: wiki-integrate
description: Integrate source summaries into broader wiki knowledge.
---

# Wiki Integrate Skill

Use this skill when the user wants `wiki/sources/` content woven into the rest of the wiki.

## Goal

Turn source summaries into better:

- concepts
- projects
- people
- organizations
- datasets
- decisions
- synthesis pages
- durable open questions

## Workflow

1. Read the relevant source summaries.
2. Search for existing pages before creating anything new.
3. Update or create durable pages with clear `Known`, `Inferred`, `Open questions`, and `Source trail` sections.
4. Preserve explicit links back to source summaries.
5. Update `wiki/index.md` only for durable, navigation-worthy pages.
6. Log the integration in `wiki/logs/maintenance.md`.

## Defaults

Unless the user explicitly says otherwise:

- update existing pages before creating new ones
- create new pages only when the topic is durable and recurring
- keep `Known`, `Inferred`, `Open questions`, and `Source trail` structure where appropriate
- update `wiki/index.md` only for durable navigation-worthy pages
- append a maintenance log entry

The user should only need to name the source summary or topic to integrate.

## Quality bar

- Prefer merging over duplicating.
- Distinguish source-supported fact from interpretation.
- Keep source trails specific.
- Record contradictions instead of smoothing them over.
