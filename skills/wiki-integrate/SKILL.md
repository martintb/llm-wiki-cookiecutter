---
name: wiki-integrate
description: Integrate source summaries into the broader LLM Wiki by updating concept pages, synthesis pages, project pages, decisions, questions, and indexes. Use summaries, not raw source documents, as the primary input.
---

# Wiki Integrate Skill

Use this skill when the user asks to integrate, synthesize, connect, merge, update the wiki, build concept pages, create synthesis pages, or incorporate source summaries into broader wiki knowledge.

This skill consumes source-summary pages from `wiki/sources/`. It should generally avoid reading raw source material unless needed to verify a detail or resolve ambiguity.

## Core principle

`wiki-ingest` turns raw sources into structured source summaries.

`wiki-integrate` turns source summaries into durable knowledge.

Do not use raw documents as the primary input unless the relevant source summary is missing, incomplete, or suspected to be wrong.

## Expected directories

- `wiki/sources/` — source summaries to integrate
- `wiki/concepts/` — concepts, methods, theories, techniques
- `wiki/projects/` — projects, programs, collaborations, proposals
- `wiki/synthesis/` — cross-source synthesis and higher-level analysis
- `wiki/people/` — people and their relevance
- `wiki/organizations/` — organizations and their relevance
- `wiki/instruments/` — instruments, platforms, beamlines, facilities
- `wiki/datasets/` — datasets and data products
- `wiki/decisions/` — durable decisions and rationale
- `wiki/questions/` — open questions
- `wiki/index.md` — navigation
- `wiki/logs/maintenance.md` — change log
- `templates/` or `/template/` — optional templates

## Template lookup

Before creating new pages, look for applicable templates.

Search these locations, in this order:

1. `/template/`
2. `/templates/`
3. `template/`
4. `templates/`
5. `wiki/templates/`

Suggested template names:

- `concept.md`
- `synthesis.md`
- `project.md`
- `person.md`
- `organization.md`
- `instrument.md`
- `dataset.md`
- `decision.md`
- `question.md`

Use a matching template if available. If none exists, use the default templates in this skill.

## Integration workflow

### 1. Identify source summaries

Read the relevant pages under `wiki/sources/`.

Do not start from `raw/` unless necessary.

For multi-source integration, first make a list of source summaries being integrated.

### 2. Determine integration targets

For each source summary, identify whether it should update:

- existing concept pages
- existing project pages
- existing synthesis pages
- people pages
- organization pages
- instrument pages
- dataset pages
- decision pages
- open-question pages
- the main index

Prefer updating existing pages over creating new ones.

Create new pages only when the idea is durable, recurring, or central enough to deserve a stable page.

### 3. Merge, do not duplicate

Before creating a new page, search the wiki for:

- exact title
- aliases
- abbreviations
- plural/singular variants
- related terminology

Example:

- `AFL`
- `Autonomous Formulation Lab`
- `autonomous formulation`
- `self-driving lab`

If a relevant page exists, update it instead of creating a duplicate.

### 4. Preserve evidence trails

When adding information to concept, project, or synthesis pages, link back to source-summary pages.

Use a section such as:

```markdown
## Source trail

- `[[source-page]]` — what this source contributes.
```

Where specific claims are important, include page numbers, section names, or source anchors when available from the source summary.

### 5. Separate claim types

Distinguish:

- source-supported facts
- interpretation
- implications for the user’s work
- unresolved questions
- contradictions
- outdated or superseded claims

Use sections such as:

```markdown
## Known

## Inferred

## Implications

## Open questions

## Contradictions and tensions
```

### 6. Write synthesis

Create or update synthesis pages when multiple source summaries point to a broader pattern.

Good synthesis pages answer questions like:

- What is the main argument across these sources?
- Where do the sources agree?
- Where do they disagree?
- What changed over time?
- What is the practical implication?
- What does this suggest for experiments, software, proposals, or strategy?

### 7. Update navigation

Update `wiki/index.md` only for durable, high-value pages.

Do not turn the index into a complete file list.

### 8. Update open questions

For unresolved issues:

- update an existing page under `wiki/questions/`, or
- create a new question page if the question is durable and likely to recur.

For resolved questions, mark them as resolved and link to the page that resolved them.

### 9. Log the integration

Append to `wiki/logs/maintenance.md`:

- source summaries integrated
- pages created
- pages updated
- pages merged or deprecated
- unresolved issues
- raw sources consulted, if any

## Default concept-page template

```markdown
---
title:
type: concept
status: active
created:
updated:
aliases: []
tags: []
source_refs: []
related: []
---

# Title

## Summary

A concise explanation of the concept.

## Why it matters

Explain why this concept is useful or recurring.

## Known

Source-supported points.

## Inferred

Interpretations or implications derived from multiple sources.

## Examples

Concrete examples.

## Relevance to the user’s work

How this connects to research, software, experiments, proposals, strategy, or writing.

## Related concepts

- `[[related-page]]` — relationship.

## Source trail

- `[[source-summary-page]]` — contribution.

## Open questions

- Question 1

## Maintenance notes

- Notes about merges, uncertainty, or future updates.
```

## Default synthesis-page template

```markdown
---
title:
type: synthesis
status: active
created:
updated:
source_refs: []
tags: []
related: []
---

# Title

## Executive summary

Short answer or synthesis.

## Sources integrated

- `[[source-summary-page]]` — contribution.
- `[[source-summary-page]]` — contribution.

## Main synthesis

Explain the cross-source pattern.

## Points of agreement

- Point 1
- Point 2

## Points of disagreement or tension

- Tension 1
- Tension 2

## Implications

### Measurement implications

- Implication for measurement, characterization, data quality, or uncertainty.

### Agent/action implications

- Implication for autonomous agents, workflows, software, decision-making, or experiment planning.

### Programmatic implications

- Implication for proposals, collaborations, strategy, or institutional planning.

## Gaps and open questions

- Question 1
- Question 2

## Related pages

- `[[concept-page]]`
- `[[project-page]]`
- `[[question-page]]`

## Maintenance notes

- Notes about scope and future updates.
```

## Default project-page template

```markdown
---
title:
type: project
status: active
created:
updated:
aliases: []
tags: []
source_refs: []
related: []
---

# Title

## Summary

Short project summary.

## Goals

- Goal 1
- Goal 2

## Current understanding

What the wiki currently knows.

## Relevant sources

- `[[source-summary-page]]` — contribution.

## Related concepts

- `[[concept-page]]`

## Decisions

- `[[decision-page]]`

## Open questions

- `[[question-page]]`

## Next actions

- Action 1
- Action 2

## Maintenance notes

- Notes.
```

## Integration discipline

Avoid these mistakes:

- summarizing raw files again instead of using source summaries
- creating many shallow concept pages
- duplicating existing pages under slightly different names
- flattening uncertainty into confident claims
- burying contradictions
- updating many pages without logging changes
- treating the index as a dumping ground
- copying long passages from source summaries into concept pages

## Output expectations

At the end of an integration operation, report:

- source-summary pages used
- pages created
- pages updated
- pages merged or deprecated
- unresolved questions
- any raw sources consulted for verification

Do not paste full page contents into chat unless the user asks.
