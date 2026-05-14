---
name: wiki-search
description: Search and read the LLM Wiki to answer questions, find relevant pages, trace source support, identify gaps, and decide whether ingestion, integration, or audit is needed.
---

# Wiki Search Skill

Use this skill when the user asks a question that may be answered from the LLM Wiki, asks what the wiki says, asks to find pages, asks for prior knowledge, or asks for source-backed synthesis.

This skill helps the LLM read the wiki before answering.

## Core principle

Search the wiki first. Use raw sources only when the wiki is missing, ambiguous, or requires verification.

## Expected directories

- `wiki/index.md`
- `wiki/sources/`
- `wiki/concepts/`
- `wiki/projects/`
- `wiki/synthesis/`
- `wiki/people/`
- `wiki/organizations/`
- `wiki/instruments/`
- `wiki/datasets/`
- `wiki/decisions/`
- `wiki/questions/`
- `wiki/logs/`
- `raw/` only for verification or missing coverage

## Search workflow

### 1. Classify the user’s question

Determine whether the user wants:

- a direct answer
- a literature/source summary
- a concept explanation
- a project status
- a decision/rationale trace
- a source trail
- a list of relevant pages
- a gap analysis
- a recommendation about what to ingest or integrate next

### 2. Search the index first

Start with:

```text
wiki/index.md
```

Look for:

- canonical page names
- aliases
- major topic areas
- project pages
- synthesis pages
- source collections

### 3. Search likely page classes

Depending on the query, search:

- `wiki/synthesis/` for cross-source answers
- `wiki/concepts/` for definitions and durable ideas
- `wiki/projects/` for project-specific context
- `wiki/sources/` for evidence and source summaries
- `wiki/decisions/` for rationale
- `wiki/questions/` for unresolved issues
- `wiki/people/` and `wiki/organizations/` for entity context
- `wiki/instruments/` and `wiki/datasets/` for technical resources

### 4. Search using variants

Search for:

- exact phrase
- abbreviations
- aliases
- plural/singular variants
- common synonyms
- project names
- older terminology

Example:

For Autonomous Formulation Lab, search:

- `AFL`
- `Autonomous Formulation Lab`
- `autonomous formulation`
- `self-driving lab`
- `closed-loop formulation`

### 5. Read source trails

When a concept, project, or synthesis page cites source-summary pages, read the cited source-summary pages if the answer depends on evidence.

Prefer source-summary pages over raw sources.

### 6. Use raw sources sparingly

Read raw sources only if:

- no source summary exists
- the source summary is incomplete
- a detail must be verified
- there is a contradiction
- the user asks for page-level evidence
- the wiki may be stale

If raw sources are consulted, say so.

### 7. Assess confidence

Before answering, classify the wiki coverage:

- **Strong** — multiple relevant pages and source trails
- **Moderate** — one or more useful pages, but incomplete synthesis
- **Weak** — scattered mentions or outdated pages
- **Missing** — no useful coverage

If coverage is weak or missing, say that clearly.

### 8. Answer with links

When responding, include relevant wiki links such as:

- `[[concept-page]]`
- `[[project-page]]`
- `[[source-summary-page]]`

If the chat environment does not support wikilinks as clickable links, still include the page names.

### 9. Suggest follow-up maintenance

If the query reveals a durable gap, suggest one of:

- run `wiki-ingest` on a source
- run `wiki-integrate` on existing summaries
- create a new synthesis page
- update a concept page
- run `wiki-audit`

Do not perform maintenance unless the user asked for it or it is clearly within scope.

## Answer structure

Use this structure when appropriate:

```markdown
## Answer

Direct answer.

## What the wiki says

- `[[page]]` — relevant point.
- `[[page]]` — relevant point.

## Source trail

- `[[source-summary]]` — evidence.

## Confidence

Strong / Moderate / Weak / Missing.

## Gaps

- Missing source, unresolved question, stale page, or contradiction.

## Suggested wiki action

- Suggested ingest/integrate/audit action.
```

## Search heuristics

Prefer pages in this order when answering broad questions:

1. `wiki/synthesis/`
2. `wiki/projects/`
3. `wiki/concepts/`
4. `wiki/decisions/`
5. `wiki/sources/`
6. `raw/`

Prefer pages in this order when answering evidence questions:

1. `wiki/sources/`
2. cited raw source
3. `wiki/concepts/`
4. `wiki/synthesis/`

Prefer pages in this order when answering “what should I do?” questions:

1. `wiki/decisions/`
2. `wiki/projects/`
3. `wiki/synthesis/`
4. `wiki/questions/`
5. `wiki/concepts/`

## Gap detection

Flag a gap when:

- the wiki has no page for a recurring topic
- a concept page has no source trail
- a synthesis page relies on only one source
- source summaries exist but are not integrated
- a question appears answered in chat but not filed in the wiki
- a page refers to outdated assumptions
- multiple pages use conflicting terminology

## Output expectations

At the end of a wiki search, report the answer and the coverage quality.

Do not claim the wiki contains information unless you found it.
