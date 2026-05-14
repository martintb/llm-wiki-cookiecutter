---
name: wiki-audit
description: Audit the wiki for structural issues, provenance gaps, stale claims, weak links, and missing integrations.
---

# Wiki Audit Skill

Use this skill when the user wants the wiki reviewed for health, integrity, or maintenance gaps.

## Audit targets

- structure
- source hygiene
- evidence trails
- link health
- duplication
- integration gaps
- staleness
- unresolved questions

## Workflow

1. Check the directory structure and seed files.
2. Review source hygiene and provenance.
3. Check wikilinks, orphans, and duplicate pages.
4. Look for unsupported claims and missing source trails.
5. Identify source summaries that were never integrated.
6. Record findings in `wiki/logs/audits.md`.

## Severity

Use:

- `Critical`
- `High`
- `Medium`
- `Low`

## Quality bar

- Findings should be concrete and actionable.
- Prefer file or page references over vague observations.
- Focus on correctness, provenance, and maintainability before cosmetics.
