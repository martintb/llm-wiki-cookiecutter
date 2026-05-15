# Workflow Example

This example shows a practical workflow for using the wiki with an LLM agent. It focuses on the prompts and requests you would give the agent, with helper commands treated as optional support.

## About The Prompt Syntax

The examples below use **Codex-style skill invocation** by naming the skill directly with a `$` prefix, for example:

```text
$wiki-ingest raw/reports/market-landscape-report.pdf
```

If your harness does not use explicit skill syntax, translate the same request into plain language:

- Codex style: `$wiki-ingest raw/reports/market-landscape-report.pdf`
- Plain-language equivalent: `Ingest raw/reports/market-landscape-report.pdf.`

The requested action is the same either way.

### Equivalent styles in other harnesses

- **Codex**: use the explicit skill form shown below, such as `$wiki-ingest raw/reports/market-landscape-report.pdf`.
- **Claude Code**: if your Claude Code setup exposes local skills as slash-invokable, the equivalent form is `/wiki-ingest raw/reports/market-landscape-report.pdf`. Plain-language prompting also works well because the skills are designed to activate from intent.
- **Gemini CLI**: the safest documented pattern is plain-language prompting plus `/skills list` to confirm the skill was discovered.

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

If you use Obsidian, opening the repo as a vault is a good way to verify placement and later inspect backlinks on the generated source-summary page.

## 3. Ask The Agent To Ingest It

Example prompt:

```text
$wiki-ingest raw/reports/market-landscape-report.pdf
```

If the PDF is scanned or needs PDF-specific handling first, ask for the `pdf` skill explicitly:

```text
Use the pdf skill to OCR raw/reports/market-landscape-report.pdf if needed, preserve the original, and then ingest it into wiki/sources/.
```

Expected result:

- a new source summary
- a maintenance log entry
- suggested next integration targets

## 4. Ask The Agent To Integrate It

Once the source summary exists:

```text
$wiki-integrate wiki/sources/market-landscape-report.md
```

Possible outputs:

- `wiki/concepts/market-segmentation.md`
- `wiki/projects/q4-planning.md`
- `wiki/decisions/prioritize-enterprise-segment.md`
- `wiki/synthesis/market-priorities.md`

## 5. Create A Specific New Page When Needed

If you want the agent to create a specific new page:

```text
$wiki-integrate Create a concept page for Market Segmentation and integrate the relevant material from wiki/sources/market-landscape-report.md into it.
```

Optional helper command:

```bash
python -m wiki_tools new-page --type concept --title "Market Segmentation"
```

## 6. Ask Questions Against The Wiki

Example prompt:

```text
$wiki-search What does the wiki say about the highest-priority customer segment?
```

## 7. Ask For An Audit

Prompt:

```text
$wiki-audit Audit this wiki and summarize the highest-priority fixes.
```

Optional helper command:

```bash
python -m wiki_tools check --strict
```

## 8. Keep Skills Synced

If you edit canonical local skills under `skills/`, tell the agent:

```text
Sync the local skills into the installed Codex, Claude Code, and Gemini mirrors.
```

Optional helper command:

```bash
python -m wiki_tools sync-skills
```

For Gemini CLI specifically, a useful verification step is:

```text
/skills list
```

The repo-local skill set also includes Obsidian companion skills such as `obsidian-markdown`, `obsidian-cli`, `obsidian-bases`, `json-canvas`, and `defuddle`.

## 9. Optional Slides

If slide support is enabled, ask for slides like this:

```text
$wiki-slides Create a short briefing deck about market priorities.
```

Equivalent examples:

- Claude Code: `/wiki-slides Create a short briefing deck about market priorities.`
- Gemini CLI: `Create a short briefing deck about market priorities.`

## 10. Healthy End State

After a few cycles, the repo should have:

- raw evidence preserved under `raw/`
- source summaries under `wiki/sources/`
- durable integrated pages under `wiki/concepts/`, `wiki/projects/`, `wiki/decisions/`, and `wiki/synthesis/`
- explicit maintenance and audit logs
- synced local skills for the main harnesses
