from __future__ import annotations

import argparse
import filecmp
import re
import shutil
import sys
from datetime import date
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
WIKI_ROOT = REPO_ROOT / "wiki"
SKILLS_ROOT = REPO_ROOT / "skills"
SKILL_TARGETS = [
    REPO_ROOT / ".agents" / "skills",
    REPO_ROOT / ".claude" / "skills",
    REPO_ROOT / ".gemini" / "skills",
]
REQUIRED_DIRS = [
    REPO_ROOT / "raw",
    REPO_ROOT / "inbox",
    REPO_ROOT / "templates",
    REPO_ROOT / "wiki",
    WIKI_ROOT / "sources",
    WIKI_ROOT / "concepts",
    WIKI_ROOT / "people",
    WIKI_ROOT / "organizations",
    WIKI_ROOT / "projects",
    WIKI_ROOT / "datasets",
    WIKI_ROOT / "decisions",
    WIKI_ROOT / "synthesis",
    WIKI_ROOT / "questions",
    WIKI_ROOT / "logs",
]
REQUIRED_FILES = [
    REPO_ROOT / "AGENTS.md",
    REPO_ROOT / "CLAUDE.md",
    REPO_ROOT / "GEMINI.md",
    REPO_ROOT / "README.md",
    WIKI_ROOT / "index.md",
    WIKI_ROOT / "logs" / "maintenance.md",
    WIKI_ROOT / "logs" / "audits.md",
]
PAGE_TYPE_TO_DIR = {
    "source": WIKI_ROOT / "sources",
    "concept": WIKI_ROOT / "concepts",
    "person": WIKI_ROOT / "people",
    "organization": WIKI_ROOT / "organizations",
    "project": WIKI_ROOT / "projects",
    "dataset": WIKI_ROOT / "datasets",
    "decision": WIKI_ROOT / "decisions",
    "synthesis": WIKI_ROOT / "synthesis",
    "question": WIKI_ROOT / "questions",
}
PAGE_TYPE_TO_TEMPLATE = {
    "source": "source.md",
    "concept": "concept.md",
    "person": "person.md",
    "organization": "organization.md",
    "project": "project.md",
    "dataset": "dataset.md",
    "decision": "decision.md",
    "synthesis": "synthesis.md",
    "question": "question.md",
}
ALLOWED_TYPES = set(PAGE_TYPE_TO_DIR) | {"log"}
ALLOWED_STATUSES = {"seed", "active", "stable", "stale", "deprecated"}
FRONTMATTER_REQUIRED = {"title", "type", "status", "created", "updated", "source_refs", "tags"}
IGNORED_NAMES = {"__pycache__", ".DS_Store"}
PLACEHOLDER_LINK_PREFIXES = (
    "related-",
    "source-summary",
    "concept-",
    "project-",
    "decision-",
    "question-",
    "person-",
    "organization-",
    "dataset-",
    "book-",
)
PLACEHOLDER_LINK_NAMES = {
    "page",
    "sources",
    "concepts",
    "projects",
    "synthesis",
    "decisions",
    "questions",
    "maintenance",
    "audits",
}


def slugify(text: str) -> str:
    value = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return re.sub(r"-{2,}", "-", value)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def parse_frontmatter(path: Path) -> tuple[dict[str, str], list[str]]:
    text = read_text(path)
    lines = text.splitlines()
    if len(lines) < 3 or lines[0].strip() != "---":
        raise ValueError("missing frontmatter")
    data: dict[str, str] = {}
    index = 1
    while index < len(lines):
        line = lines[index]
        if line.strip() == "---":
            return data, lines[index + 1 :]
        if ":" in line:
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip()
        index += 1
    raise ValueError("unterminated frontmatter")


def render_template(template_name: str, *, title: str) -> str:
    template_path = REPO_ROOT / "templates" / template_name
    if not template_path.exists():
        raise SystemExit(f"missing template: {template_path}")
    rendered = read_text(template_path)
    today = str(date.today())
    rendered = rendered.replace("__TITLE__", title)
    rendered = rendered.replace("__DATE__", today)
    return rendered


def new_page(args: argparse.Namespace) -> int:
    title = args.title.strip()
    slug = args.slug or slugify(title)
    if not slug:
        raise SystemExit("unable to derive slug from title")
    page_type = args.type
    target_dir = PAGE_TYPE_TO_DIR[page_type]
    target_path = target_dir / f"{slug}.md"
    if target_path.exists():
        raise SystemExit(f"page already exists: {target_path}")
    content = render_template(PAGE_TYPE_TO_TEMPLATE[page_type], title=title)
    write_text(target_path, content)
    print(target_path.relative_to(REPO_ROOT))
    return 0


def remove_children(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)
    for child in path.iterdir():
        if child.name in IGNORED_NAMES:
            continue
        if child.is_dir():
            shutil.rmtree(child)
        else:
            child.unlink()


def sync_skills(_: argparse.Namespace | None = None) -> int:
    if not SKILLS_ROOT.exists():
        raise SystemExit(f"missing canonical skill directory: {SKILLS_ROOT}")
    for target_root in SKILL_TARGETS:
        remove_children(target_root)
        for skill_dir in sorted(SKILLS_ROOT.iterdir()):
            if not skill_dir.is_dir() or skill_dir.name in IGNORED_NAMES:
                continue
            shutil.copytree(skill_dir, target_root / skill_dir.name)
    print("synced skills")
    return 0


def compare_trees(left: Path, right: Path) -> bool:
    comparison = filecmp.dircmp(left, right, ignore=list(IGNORED_NAMES))
    if comparison.left_only or comparison.right_only or comparison.funny_files:
        return False
    _, mismatches, errors = filecmp.cmpfiles(
        left, right, comparison.common_files, shallow=False
    )
    if mismatches or errors:
        return False
    return all(
        compare_trees(left / directory, right / directory)
        for directory in comparison.common_dirs
    )


def known_page_names() -> set[str]:
    names: set[str] = set()
    for page in WIKI_ROOT.rglob("*.md"):
        names.add(page.stem)
    return names


def find_wikilinks(text: str) -> list[str]:
    pattern = re.compile(r"\[\[([^\]|#]+)(?:[#|][^\]]*)?\]\]")
    return [match.group(1).split("/")[-1] for match in pattern.finditer(text)]


def is_placeholder_link(link: str) -> bool:
    return link in PLACEHOLDER_LINK_NAMES or link.startswith(PLACEHOLDER_LINK_PREFIXES)


def check(args: argparse.Namespace) -> int:
    errors: list[str] = []

    for path in REQUIRED_DIRS:
        if not path.exists():
            errors.append(f"missing required directory: {path.relative_to(REPO_ROOT)}")

    for path in REQUIRED_FILES:
        if not path.exists():
            errors.append(f"missing required file: {path.relative_to(REPO_ROOT)}")

    page_names = known_page_names()
    for page in WIKI_ROOT.rglob("*.md"):
        try:
            frontmatter, body = parse_frontmatter(page)
        except ValueError as exc:
            errors.append(f"{page.relative_to(REPO_ROOT)}: {exc}")
            continue

        missing = sorted(FRONTMATTER_REQUIRED - set(frontmatter))
        if missing:
            errors.append(
                f"{page.relative_to(REPO_ROOT)}: missing frontmatter keys {', '.join(missing)}"
            )
        page_type = frontmatter.get("type", "")
        if page_type not in ALLOWED_TYPES:
            errors.append(f"{page.relative_to(REPO_ROOT)}: invalid type '{page_type}'")
        status = frontmatter.get("status", "")
        if status not in ALLOWED_STATUSES:
            errors.append(f"{page.relative_to(REPO_ROOT)}: invalid status '{status}'")
        if page_type == "source" and "raw_source" not in frontmatter:
            errors.append(f"{page.relative_to(REPO_ROOT)}: source page missing raw_source")

        for link in find_wikilinks("\n".join(body)):
            if is_placeholder_link(link):
                continue
            if link not in page_names:
                errors.append(f"{page.relative_to(REPO_ROOT)}: broken wikilink [[{link}]]")

    if SKILLS_ROOT.exists():
        for target in SKILL_TARGETS:
            if not target.exists():
                errors.append(f"missing skill mirror: {target.relative_to(REPO_ROOT)}")
            elif not compare_trees(SKILLS_ROOT, target):
                errors.append(f"skill mirror drift: {target.relative_to(REPO_ROOT)}")

    if errors:
        stream = sys.stderr if args.strict else sys.stdout
        for error in errors:
            print(error, file=stream)
        return 1 if args.strict else 0

    print("wiki checks passed")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Helper tools for an LLM wiki repo.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    new_page_parser = subparsers.add_parser("new-page", help="Create a new wiki page from a template.")
    new_page_parser.add_argument("--type", choices=sorted(PAGE_TYPE_TO_DIR), required=True)
    new_page_parser.add_argument("--title", required=True)
    new_page_parser.add_argument("--slug")
    new_page_parser.set_defaults(func=new_page)

    check_parser = subparsers.add_parser("check", help="Validate the wiki scaffold and content.")
    check_parser.add_argument("--strict", action="store_true")
    check_parser.set_defaults(func=check)

    sync_parser = subparsers.add_parser("sync-skills", help="Sync canonical skills into hidden mirrors.")
    sync_parser.set_defaults(func=sync_skills)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)
