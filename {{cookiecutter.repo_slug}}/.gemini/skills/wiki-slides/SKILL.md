---
name: wiki-slides
description: Build slide briefs, outlines, and Marp-compatible decks from integrated wiki pages.
---

# Wiki Slides Skill

Use this skill when the user wants slides derived from wiki knowledge.

## Workflow

1. Search the wiki first.
2. Build a short presentation brief.
3. Create an outline before a full draft unless the user explicitly wants a full deck immediately.
4. Draft sparse slides, usually in Marp format.
5. Put evidence trails and caveats in speaker notes rather than on slide bodies.

## Defaults

Unless the user explicitly says otherwise:

- use integrated wiki pages before raw sources
- create a brief, then an outline, then a draft
- write the draft deck under `slides/drafts/`
- keep slides sparse
- put source trails and caveats in speaker notes

The user should only need to describe the topic, audience, or goal.

## Source priority

Prefer:

1. `wiki/synthesis/`
2. `wiki/projects/`
3. `wiki/concepts/`
4. `wiki/decisions/`
5. `wiki/sources/`
6. `raw/` only when needed

## Quality bar

- Slides are communication artifacts, not wiki page dumps.
- Keep slide bodies sparse.
- Use claim-like titles when possible.
- Preserve uncertainty rather than overstating it.
