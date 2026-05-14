---
name: wiki-search
description: Search and read the wiki first, answer from it when possible, and report coverage honestly.
---

# Wiki Search Skill

Use this skill when the user asks what the wiki says, asks for prior knowledge, or wants a source-backed answer.

## Search order

For broad questions, prefer:

1. `wiki/index.md`
2. `wiki/synthesis/`
3. `wiki/projects/`
4. `wiki/concepts/`
5. `wiki/decisions/`
6. `wiki/sources/`
7. `raw/` only when the wiki is missing, stale, or needs verification

## Output

Answer with:

- a direct answer
- the most relevant page links
- a source trail when available
- a confidence rating: `Strong`, `Moderate`, `Weak`, or `Missing`
- the main gap, if one exists

## Quality bar

- Do not claim the wiki contains something you did not find.
- Say clearly when coverage is weak or missing.
- Suggest `wiki-ingest`, `wiki-integrate`, or `wiki-audit` when the question exposes a durable gap.
