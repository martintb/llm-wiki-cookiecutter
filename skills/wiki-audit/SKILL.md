---
name: wiki-audit
description: Audit the LLM Wiki for orphan pages, stale claims, missing source trails, unintegrated summaries, contradictions, duplicate pages, weak links, unresolved questions, and structural problems.
---

# Wiki Audit Skill

Use this skill when the user asks to audit, lint, clean up, health-check, review, organize, maintain, improve, or evaluate the LLM Wiki.

This skill follows the general LLM-wiki maintenance pattern described by Karpathy and related implementations: the wiki should be searchable, linked, source-backed, non-duplicative, and continuously improved as new sources and answers accumulate.

## Core principle

The wiki is only useful if it is maintained. Audit for structure, provenance, contradictions, staleness, duplication, and integration gaps.

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
- `raw/`
- `inbox/`
- `templates/` or `/template/`

## Template lookup

Before creating an audit report, look for templates in:

1. `/template/`
2. `/templates/`
3. `template/`
4. `templates/`
5. `wiki/templates/`

Suggested template names:

- `audit.md`
- `wiki-audit.md`
- `maintenance-audit.md`

If no template exists, use the default audit template in this skill.

## Audit modes

Use the mode requested by the user. If no mode is specified, perform a general audit.

### 1. General audit

Check overall wiki health.

### 2. Source audit

Focus on source summaries, raw source coverage, and unintegrated sources.

### 3. Link audit

Focus on wikilinks, backlinks, orphans, duplicate pages, and index structure.

### 4. Concept audit

Focus on concept pages, aliases, duplicate terminology, and unsupported claims.

### 5. Project audit

Focus on project pages, decisions, open questions, and source support.

### 6. Staleness audit

Focus on outdated pages, old assumptions, and superseded claims.

### 7. Question audit

Focus on unresolved questions, resolved-but-unmarked questions, and questions that should become synthesis pages.

## Audit checklist

### Structure

- Does `wiki/index.md` provide useful navigation?
- Are major areas represented?
- Are folders used consistently?
- Are pages in the right place?
- Are there pages that should be split?
- Are there pages that should be merged?

### Source hygiene

- Are raw sources preserved?
- Does each source summary link to its raw source?
- Are source summaries missing metadata?
- Are there raw sources without source summaries?
- Are there source summaries that were never integrated?
- Are source summaries too shallow to be useful?

### Evidence trails

- Do concept, project, and synthesis pages cite source-summary pages?
- Are important claims unsupported?
- Are source trails specific enough?
- Are page numbers, sections, figure numbers, or anchors preserved where available?

### Link health

- Are there orphan pages with no inbound links?
- Are there dead wikilinks?
- Are important pages missing backlinks?
- Are there pages with no outbound links?
- Are aliases needed?
- Are redirects or merge notes needed?

### Duplication

Look for duplicate or near-duplicate pages caused by:

- abbreviations
- plural/singular variants
- renamed projects
- synonyms
- old terminology
- overlapping concepts

Examples:

- `AFL` vs `Autonomous Formulation Lab`
- `self-driving labs` vs `autonomous laboratories`
- `uncertainty propagation` vs `uncertainty quantification`

### Integration gaps

- Are there source summaries that should update concept pages?
- Are there multiple source summaries that call for a synthesis page?
- Are there repeated concepts with no concept page?
- Are there open questions that should be promoted?
- Are chat answers or decisions missing from the wiki?

### Contradictions and tensions

- Do sources disagree?
- Do older pages conflict with newer pages?
- Are contradictions explicitly marked?
- Are superseded claims labeled as superseded?
- Are uncertain claims presented too confidently?

### Staleness

- Are pages marked `stable` that should be `stale`?
- Are project pages outdated?
- Are source pages based on old versions?
- Are decisions still valid?
- Are open questions already answered elsewhere?

### Template compliance

- Do pages have frontmatter?
- Are required fields present?
- Are page types consistent?
- Are statuses consistent?
- Are tags useful rather than noisy?
- Are source refs formatted consistently?

### Obsidian compatibility

- Are wikilinks valid?
- Are aliases used where helpful?
- Are embeds used appropriately?
- Are callouts used where they improve readability?
- Are Bases or Canvas files needed for dashboards or maps?

## Severity levels

Use these severity levels:

- **Critical** — undermines correctness or trustworthiness
- **High** — significantly reduces usefulness or discoverability
- **Medium** — worth fixing during maintenance
- **Low** — cosmetic or optional improvement

## Default audit report template

Create or update:

```text
wiki/logs/audits.md
```

Use this format:

```markdown
# Wiki audits

## Audit — YYYY-MM-DD

### Scope

Describe what was audited.

### Summary

Brief summary of wiki health.

### Overall assessment

- Structure:
- Source hygiene:
- Evidence trails:
- Link health:
- Integration:
- Staleness:
- Obsidian compatibility:

### Issues found

| Severity | Area | Page / path | Issue | Recommended action |
|---|---|---|---|---|
| High | Source hygiene | `wiki/sources/example.md` | Missing raw source link | Add `raw_source` frontmatter and provenance section |

### Orphan pages

- `[[page]]` — recommended action.

### Dead or ambiguous links

- `[[missing-page]]` — appears in X pages; create, rename, or relink.

### Duplicate or merge candidates

- `[[page-a]]` and `[[page-b]]` — recommended merge direction.

### Unintegrated source summaries

- `[[source-summary]]` — should update `[[concept]]` or `[[synthesis]]`.

### Unsupported or weakly supported claims

- `[[page]]` — claim needing source trail.

### Contradictions or tensions

- `[[page-a]]` vs `[[page-b]]` — describe tension.

### Stale pages

- `[[page]]` — reason it may be stale.

### Suggested new pages

- `[[new-page]]` — reason.

### Suggested synthesis pages

- `[[synthesis-page]]` — sources that motivate it.

### Suggested template improvements

- Template or field improvement.

### Changes made during audit

- Change 1
- Change 2

### Changes deferred

- Deferred item and reason.

### Recommended next actions

1. Highest-priority action.
2. Second action.
3. Third action.
```

## Audit behavior

When performing an audit:

1. Prefer reporting first over making sweeping edits.
2. Make safe, mechanical fixes if requested:
   - broken links
   - missing backlinks
   - status updates
   - obvious aliases
   - maintenance-log entries
3. Do not merge, delete, or deprecate pages without clear rationale.
4. Preserve audit findings even after fixing issues.
5. If the audit reveals many issues, prioritize the highest-impact fixes.

## Output expectations

At the end of an audit, report:

- audit scope
- number and type of issues found
- most important fixes
- pages created or changed
- deferred decisions

Do not paste the entire audit log into chat unless the user asks.
