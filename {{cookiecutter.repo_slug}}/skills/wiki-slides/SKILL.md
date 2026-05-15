---
name: wiki-slides
description: Build slide briefs, outlines, and decks from integrated wiki pages.
---

# Wiki Slides Skill

Use this skill when the user wants slides derived from wiki knowledge.

## Workflow

1. Search the wiki first.
2. Create a short presentation brief.
3. Build an outline before a full draft unless the user explicitly wants a full deck.
4. Draft sparse slides, usually in Marp format.
5. Put evidence trails and caveats in speaker notes.

## Defaults

Unless the user explicitly says otherwise:

- use integrated wiki pages before raw sources
- create a brief, then an outline, then a draft
- write the draft deck under `slides/drafts/`
- keep slides sparse
- put source trails and caveats in speaker notes

The user should only need to describe the topic, audience, or goal.

## Source priority

Prefer `wiki/synthesis/`, `wiki/projects/`, and `wiki/concepts/` before raw sources.
