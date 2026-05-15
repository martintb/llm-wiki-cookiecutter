# LLM Wiki Workflow Example

This example shows a full, concrete workflow for using a generated wiki repo with an LLM agent. The emphasis here is on the kinds of prompts and requests you would give the agent, not on driving everything through Python commands.

## About The Prompt Syntax

The examples below use **Codex-style skill invocation** by naming the skill directly with a `$` prefix, for example:

```text
$wiki-ingest raw/reports/market-landscape-report.pdf
```

For other LLM harnesses, the same request can usually be written in plain language instead:

- Codex style: `$wiki-ingest raw/reports/market-landscape-report.pdf`
- Plain-language equivalent: `Ingest raw/reports/market-landscape-report.pdf.`

The intent is the same. The only difference is whether your harness supports explicit skill-style invocation syntax.

### Equivalent styles in other harnesses

- **Codex**: use the explicit skill form shown below, such as `$wiki-ingest raw/reports/market-landscape-report.pdf`.
- **Claude Code**: if your Claude Code setup exposes local skills as slash-invokable, the equivalent form is `/wiki-ingest raw/reports/market-landscape-report.pdf`. Plain-language prompting also works well because the skills are designed to activate from intent.
- **Gemini CLI**: the safest documented pattern is plain-language prompting plus `/skills list` to verify discovery.

Examples for the same task:

- Codex: `$wiki-ingest raw/reports/market-landscape-report.pdf`
- Claude Code: `/wiki-ingest raw/reports/market-landscape-report.pdf`
- Gemini CLI: `Ingest raw/reports/market-landscape-report.pdf.`

More equivalents:

- Codex: `$wiki-integrate wiki/sources/market-landscape-report.md`
- Claude Code: `/wiki-integrate wiki/sources/market-landscape-report.md`
- Gemini CLI: `Integrate wiki/sources/market-landscape-report.md into the wiki.`

- Codex: `$wiki-search What does the wiki say about the highest-priority customer segment?`
- Claude Code: `/wiki-search What does the wiki say about the highest-priority customer segment?`
- Gemini CLI: `What does the wiki say about the highest-priority customer segment?`

- Codex: `$wiki-audit Audit this wiki and summarize the highest-priority fixes.`
- Claude Code: `/wiki-audit Audit this wiki and summarize the highest-priority fixes.`
- Gemini CLI: `Audit this wiki and summarize the highest-priority fixes.`

- Codex: `$wiki-slides Create a short briefing deck about market priorities.`
- Claude Code: `/wiki-slides Create a short briefing deck about market priorities.`
- Gemini CLI: `Create a short briefing deck about market priorities.`

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
$wiki-ingest raw/reports/market-landscape-report.pdf
```

If the source is messy or not yet categorized:

```text
Review inbox/ and tell me how you would classify the files before ingesting anything.
```

## 3. Ingest The Source

You can keep the ingest request simple because template selection, provenance preservation, and maintenance logging are part of the skill:

```text
$wiki-ingest raw/reports/market-landscape-report.pdf
```

Expected result:

- a source summary in `wiki/sources/`
- a maintenance log entry
- suggested next integration targets

## 4. Integrate The Source

Once the source summary exists, ask for integration explicitly:

```text
$wiki-integrate wiki/sources/market-landscape-report.md
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
$wiki-search What does the wiki say about the highest-priority customer segment?
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
$wiki-integrate Create a concept page for Market Segmentation and integrate the relevant material from wiki/sources/market-landscape-report.md into it.
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
$wiki-audit Audit this wiki and summarize the highest-priority fixes.
```

## 9. Keep Skills Synced

If you edit canonical local skills under `skills/`, ask the agent to sync them:

```text
Sync the local skills into the installed Codex, Claude Code, and Gemini mirrors.
```

Optional command:

```bash
python -m wiki_tools sync-skills
```

This updates:

- `.agents/skills/`
- `.claude/skills/`
- `.gemini/skills/`

For Gemini CLI specifically, a useful verification step is:

```text
/skills list
```

## 10. Optional Slide Workflow

If slide support is enabled, ask for a deck derived from integrated wiki pages rather than raw sources.

Example prompt:

```text
$wiki-slides Create a short briefing deck about market priorities.
```

Equivalent examples:

- Claude Code: `/wiki-slides Create a short briefing deck about market priorities.`
- Gemini CLI: `Create a short briefing deck about market priorities.`

## 11. What Good Looks Like

After a few cycles, a healthy workflow looks like this:

- raw evidence preserved under `raw/`
- high-quality source summaries in `wiki/sources/`
- durable concepts, decisions, projects, and synthesis pages
- explicit source trails
- a maintenance log that explains what changed
- periodic audits that identify what still needs work
