# Workflow Example

This example shows a practical workflow for using the wiki with an LLM agent. It focuses on the prompts and requests you would give the agent, with helper commands treated as optional support.

## 1. Verify The Scaffold

Start by telling the agent:

```text
Read AGENTS.md and summarize how this wiki is intended to work. Then inspect the repo structure and tell me whether anything important is missing.
```

Optional command if helpers are enabled:

```bash
python -m wiki_tools check --strict
```

## 2. Add A Raw Source

Suppose you have:

```text
raw/reports/market-landscape-report.pdf
```

If it is not yet categorized, place it in `inbox/` first.

## 3. Ask The Agent To Ingest It

Example prompt:

```text
Use wiki-ingest on raw/reports/market-landscape-report.pdf.

Create a source summary in wiki/sources/.
Preserve provenance.
Extract the main claims, evidence, important entities, and suggested follow-up pages.
Log the ingest in wiki/logs/maintenance.md.
Do not broadly edit the rest of the wiki yet.
```

Expected result:

- a new source summary
- a maintenance log entry
- suggested next integration targets

## 4. Ask The Agent To Integrate It

Once the source summary exists:

```text
Use wiki-integrate on wiki/sources/market-landscape-report.md.

Update existing pages where possible.
Create new pages only if they are durable and justified.
Keep source trails explicit and separate Known from Inferred.
Log all changes in wiki/logs/maintenance.md.
```

Possible outputs:

- `wiki/concepts/market-segmentation.md`
- `wiki/projects/q4-planning.md`
- `wiki/decisions/prioritize-enterprise-segment.md`
- `wiki/synthesis/market-priorities.md`

## 5. Create A Specific New Page When Needed

If you want the agent to create a specific new page:

```text
Create a new concept page called "Market Segmentation" using the local concept template.
Then integrate the relevant material from wiki/sources/market-landscape-report.md into it.
Do not create any other new pages.
```

Optional helper command:

```bash
python -m wiki_tools new-page --type concept --title "Market Segmentation"
```

## 6. Ask Questions Against The Wiki

Example prompt:

```text
Use wiki-search to answer this question from the current wiki: What does the wiki say about the highest-priority customer segment?

Search the wiki first.
Use raw sources only if the wiki is missing, stale, or contradictory.
Answer with:
- the direct answer
- relevant page links
- the source trail
- confidence level
- the most important gap, if any
```

## 7. Ask For An Audit

Prompt:

```text
Run wiki-audit on this repo and focus on:
- weak source trails
- orphan pages
- duplicate pages
- stale assumptions
- source summaries that have not yet been integrated

Record the findings in wiki/logs/audits.md and summarize the highest-priority fixes.
```

Optional helper command:

```bash
python -m wiki_tools check --strict
```

## 8. Keep Skills Synced

If you edit canonical local skills under `skills/`, tell the agent:

```text
I updated the skill definitions under skills/. Refresh the installed mirrors for Codex, Claude Code, and Gemini.
```

Optional helper command:

```bash
python -m wiki_tools sync-skills
```

## 9. Optional Slides

If slide support is enabled, ask for slides like this:

```text
Use wiki-slides to create a short briefing deck about market priorities.

Base it on the current synthesis and project pages, not raw sources.
Create a brief first, then an outline, then a draft deck in slides/drafts/.
Keep the slides sparse and put evidence trails in speaker notes.
```

## 10. Healthy End State

After a few cycles, the repo should have:

- raw evidence preserved under `raw/`
- source summaries under `wiki/sources/`
- durable integrated pages under `wiki/concepts/`, `wiki/projects/`, `wiki/decisions/`, and `wiki/synthesis/`
- explicit maintenance and audit logs
- synced local skills for the main harnesses
