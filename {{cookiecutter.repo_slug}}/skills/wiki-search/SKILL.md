---
name: wiki-search
description: Search the wiki first, answer from it when possible, and report coverage honestly.
---

# Wiki Search Skill

Use this skill when the user asks what the wiki says, asks for prior work, or wants a source-backed answer.

## Search order

1. `wiki/index.md`
2. `wiki/synthesis/`
3. `wiki/projects/`
4. `wiki/concepts/`
5. `wiki/decisions/`
6. `wiki/sources/`
7. `raw/` only if the wiki is missing, stale, or needs verification

## Output

Provide:

- a direct answer
- relevant page links
- a source trail when available
- a confidence rating: `Strong`, `Moderate`, `Weak`, or `Missing`
- the main gap, if one exists
