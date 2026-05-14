# LLM Wiki Workflow Example

This example shows a full, concrete workflow for using a generated wiki repo with an LLM agent. The emphasis here is on the kinds of prompts and requests you would give the agent, not on driving everything through Python commands.

## Scenario

You have a new report called `market-landscape-report.pdf` and you want to preserve it, summarize it, connect it to the rest of the wiki, and later answer questions from it.

## 1. Create The Wiki

Render the template:

```bash
cookiecutter gh:<owner>/<repo>
cd my-llm-wiki
```

Then open the generated repo in your preferred harness.

Good first prompt:

```text
Read AGENTS.md and summarize how this wiki is supposed to work. Then inspect the repo structure and tell me whether the scaffold looks complete.
```

Optional verification command if helpers are enabled:

```bash
python -m wiki_tools check --strict
```

## 2. Add Raw Source Material

Place the source under:

```text
raw/reports/market-landscape-report.pdf
```

Then tell the agent exactly what you want:

```text
Use wiki-ingest on raw/reports/market-landscape-report.pdf. Create a source summary under wiki/sources/, preserve provenance, extract the main claims and evidence, and log the ingest in wiki/logs/maintenance.md.
```

If the source is messy or not yet categorized:

```text
Review inbox/ and tell me how you would classify the files before ingesting anything.
```

## 3. Ingest The Source

A more specific ingest prompt:

```text
Ingest raw/reports/market-landscape-report.pdf into wiki/sources/market-landscape-report.md.

Use the most appropriate template in templates/.
Preserve provenance.
Extract:
- a dense summary
- key claims
- evidence anchors
- important organizations and people
- suggested follow-up concept, project, decision, or synthesis pages

Do not broadly edit the rest of the wiki yet.
```

Expected result:

- a source summary in `wiki/sources/`
- a maintenance log entry
- suggested next integration targets

## 4. Integrate The Source

Once the source summary exists, ask for integration explicitly:

```text
Use wiki-integrate on wiki/sources/market-landscape-report.md.

Update any existing concept, project, decision, or synthesis pages that already fit.
If no suitable pages exist, create only the durable ones that are justified.
Keep source trails explicit and separate Known from Inferred.
Log all changes in wiki/logs/maintenance.md.
```

Possible outputs:

- `wiki/concepts/market-segmentation.md`
- `wiki/projects/q4-planning.md`
- `wiki/decisions/prioritize-enterprise-segment.md`
- `wiki/synthesis/market-priorities.md`

## 5. Ask Questions Against The Wiki

After ingest and integration, use the wiki as the first source of truth.

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

This should push the agent toward:

1. `wiki/synthesis/`
2. `wiki/projects/`
3. `wiki/concepts/`
4. `wiki/decisions/`
5. `wiki/sources/`

## 6. Create Follow-Up Pages Deliberately

If you want the agent to create a new page instead of deciding on its own, say so directly.

Example:

```text
Create a new concept page called "Market Segmentation" using the local concept template.
Then integrate the relevant material from wiki/sources/market-landscape-report.md into it.
Do not create any other new pages.
```

Optional helper commands, if enabled:

```bash
python -m wiki_tools new-page --type concept --title "Market Segmentation"
python -m wiki_tools new-page --type decision --title "Prioritize Enterprise Segment"
```

## 7. Record Maintenance And Review Deltas

Ask the agent to be explicit about what changed:

```text
Summarize exactly what wiki pages you updated, what new pages you created, and append a concise maintenance log entry describing the changes and any unresolved issues.
```

The maintenance log should capture:

- source processed
- summary created or updated
- pages created
- pages updated
- unresolved questions

## 8. Run A Health Check

Use both the helper check and the audit workflow when possible.

Command:

```bash
python -m wiki_tools check --strict
```

Agent prompt:

```text
Run wiki-audit on this repo and focus on:
- weak source trails
- orphan pages
- duplicate pages
- stale assumptions
- source summaries that have not yet been integrated

Record the findings in wiki/logs/audits.md and summarize the highest-priority fixes.
```

## 9. Keep Skills Synced

If you edit canonical local skills under `skills/`, ask the agent to sync them:

```text
I updated the skill definitions under skills/. Refresh the installed mirrors for Codex, Claude Code, and Gemini.
```

Optional command:

```bash
python -m wiki_tools sync-skills
```

This updates:

- `.agents/skills/`
- `.claude/skills/`
- `.gemini/skills/`

## 10. Optional Slide Workflow

If slide support is enabled, ask for a deck derived from integrated wiki pages rather than raw sources.

Example prompt:

```text
Use wiki-slides to create a short briefing deck about market priorities.

Base it on the current synthesis and project pages, not raw sources.
Create a brief first, then an outline, then a draft Marp deck in slides/drafts/.
Keep the slides sparse and put evidence trails in speaker notes.
```

## 11. What Good Looks Like

After a few cycles, a healthy workflow looks like this:

- raw evidence preserved under `raw/`
- high-quality source summaries in `wiki/sources/`
- durable concepts, decisions, projects, and synthesis pages
- explicit source trails
- a maintenance log that explains what changed
- periodic audits that identify what still needs work
