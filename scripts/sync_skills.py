from __future__ import annotations

import argparse
import filecmp
import shutil
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
SOURCE_ROOT = REPO_ROOT / "skills"
TEMPLATE_ROOT = REPO_ROOT / "{{cookiecutter.repo_slug}}"
TARGET_ROOTS = [
    REPO_ROOT / ".agents" / "skills",
    REPO_ROOT / ".claude" / "skills",
    REPO_ROOT / ".gemini" / "skills",
]
TEMPLATE_TARGET_ROOTS = [
    TEMPLATE_ROOT / "skills",
    TEMPLATE_ROOT / ".agents" / "skills",
    TEMPLATE_ROOT / ".claude" / "skills",
    TEMPLATE_ROOT / ".gemini" / "skills",
]
IGNORED_NAMES = {"__pycache__", ".DS_Store"}


def skill_directories(root: Path) -> list[Path]:
    if not root.exists():
        return []
    return sorted(
        path for path in root.iterdir() if path.is_dir() and path.name not in IGNORED_NAMES
    )


def remove_children(path: Path) -> None:
    if not path.exists():
        path.mkdir(parents=True, exist_ok=True)
        return
    for child in path.iterdir():
        if child.name in IGNORED_NAMES:
            continue
        if child.is_dir():
            shutil.rmtree(child)
        else:
            child.unlink()


def sync_targets(source_root: Path, target_roots: list[Path]) -> None:
    for target_root in target_roots:
        target_root.mkdir(parents=True, exist_ok=True)
        remove_children(target_root)
        for skill_dir in skill_directories(source_root):
            shutil.copytree(skill_dir, target_root / skill_dir.name)


def sync() -> None:
    if not SOURCE_ROOT.exists():
        raise SystemExit(f"missing canonical skill directory: {SOURCE_ROOT}")
    sync_targets(SOURCE_ROOT, TARGET_ROOTS)
    sync_targets(SOURCE_ROOT, TEMPLATE_TARGET_ROOTS)


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


def check() -> int:
    if not SOURCE_ROOT.exists():
        print(f"missing canonical skill directory: {SOURCE_ROOT}", file=sys.stderr)
        return 1
    for target_root in TARGET_ROOTS + TEMPLATE_TARGET_ROOTS:
        if not target_root.exists():
            print(f"missing mirror directory: {target_root}", file=sys.stderr)
            return 1
        if not compare_trees(SOURCE_ROOT, target_root):
            print(f"skill mirror drift detected in {target_root}", file=sys.stderr)
            return 1
    print("skill mirrors are in sync")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync repo-local wiki skills into harness mirrors.")
    parser.add_argument("--check", action="store_true", help="Check for mirror drift without copying.")
    args = parser.parse_args()
    if args.check:
        return check()
    sync()
    print(
        "synced canonical skills into repo mirrors and the generated project template"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
