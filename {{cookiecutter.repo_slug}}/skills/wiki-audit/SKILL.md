---
name: wiki-audit
description: Audit the wiki for structural issues, provenance gaps, stale claims, weak links, and missing integrations.
---

# Wiki Audit Skill

Use this skill when the user wants a health check or maintenance review.

## Audit targets

- structure
- source hygiene
- evidence trails
- link health
- duplication
- integration gaps
- staleness
- unresolved questions

## Output

Record findings in `wiki/logs/audits.md` with severity, affected page or path, and a clear recommended action.

## Defaults

Unless the user explicitly says otherwise:

- run a general audit
- prioritize provenance, unsupported claims, broken links, duplication, and integration gaps
- record findings in `wiki/logs/audits.md`
- use severity levels and concrete recommended actions

The user should only need to ask for an audit or specify a narrower focus.
