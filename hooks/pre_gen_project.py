from __future__ import annotations

import re
import sys


REPO_SLUG = "{{ cookiecutter.repo_slug }}"
INCLUDE_SLIDES = "{{ cookiecutter.include_slides }}"
INCLUDE_PYTHON_HELPERS = "{{ cookiecutter.include_python_helpers }}"


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", REPO_SLUG):
    fail("repo_slug must be lowercase kebab-case, using only a-z, 0-9, and hyphens")

for name, value in {
    "include_slides": INCLUDE_SLIDES,
    "include_python_helpers": INCLUDE_PYTHON_HELPERS,
}.items():
    if value not in {"y", "n"}:
        fail(f"{name} must be 'y' or 'n'")
