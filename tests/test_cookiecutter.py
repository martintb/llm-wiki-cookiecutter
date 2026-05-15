from __future__ import annotations

import filecmp
import subprocess
import tempfile
import unittest
from pathlib import Path

from cookiecutter.main import cookiecutter


REPO_ROOT = Path(__file__).resolve().parent.parent
CANONICAL_SKILLS_DIR = REPO_ROOT / "skills"


class CookiecutterRenderTests(unittest.TestCase):
    def render_project(self, **extra_context: str) -> Path:
        output_dir = Path(tempfile.mkdtemp(prefix="llm-wiki-cookiecutter-"))
        config_file = output_dir / "cookiecutter-config.yaml"
        config_file.write_text(
            "\n".join(
                [
                    f"cookiecutters_dir: '{output_dir / 'cookiecutters'}'",
                    f"replay_dir: '{output_dir / 'replay'}'",
                    "default_context: {}",
                    "abbreviations: {}",
                ]
            ),
            encoding="utf-8",
        )
        project_dir = Path(
            cookiecutter(
                str(REPO_ROOT),
                no_input=True,
                output_dir=str(output_dir),
                config_file=str(config_file),
                extra_context=extra_context,
            )
        )
        return project_dir

    def compare_trees(self, left: Path, right: Path) -> bool:
        comparison = filecmp.dircmp(left, right, ignore=["__pycache__", ".DS_Store"])
        if comparison.left_only or comparison.right_only or comparison.funny_files:
            return False
        _, mismatches, errors = filecmp.cmpfiles(
            left, right, comparison.common_files, shallow=False
        )
        if mismatches or errors:
            return False
        return all(
            self.compare_trees(left / directory, right / directory)
            for directory in comparison.common_dirs
        )

    def test_default_render_and_tools(self) -> None:
        project_dir = self.render_project()
        self.assertTrue((project_dir / "AGENTS.md").exists())
        self.assertTrue((project_dir / "CLAUDE.md").exists())
        self.assertTrue((project_dir / "GEMINI.md").exists())
        self.assertTrue((project_dir / "docs" / "obsidian.md").exists())
        self.assertTrue((project_dir / "skills" / "pdf" / "SKILL.md").exists())
        self.assertTrue((project_dir / "skills" / "pdf" / "scripts" / "split_book.py").exists())
        self.assertTrue((project_dir / ".agents" / "skills").exists())
        self.assertTrue((project_dir / ".claude" / "skills").exists())
        self.assertTrue((project_dir / ".gemini" / "skills").exists())
        self.assertTrue((project_dir / "skills" / "obsidian-markdown" / "SKILL.md").exists())
        self.assertTrue((project_dir / "skills" / "obsidian-cli" / "SKILL.md").exists())
        self.assertTrue((project_dir / "skills" / "obsidian-bases" / "SKILL.md").exists())
        self.assertTrue((project_dir / "skills" / "json-canvas" / "SKILL.md").exists())
        self.assertTrue((project_dir / "skills" / "defuddle" / "SKILL.md").exists())
        self.assertTrue((project_dir / ".agents" / "skills" / "pdf" / "SKILL.md").exists())
        self.assertTrue(
            self.compare_trees(CANONICAL_SKILLS_DIR, project_dir / "skills")
        )
        self.assertTrue(
            self.compare_trees(project_dir / "skills", project_dir / ".agents" / "skills")
        )
        self.assertTrue(
            self.compare_trees(project_dir / "skills", project_dir / ".claude" / "skills")
        )
        self.assertTrue(
            self.compare_trees(project_dir / "skills", project_dir / ".gemini" / "skills")
        )

        result = subprocess.run(
            [
                "python3",
                "-m",
                "wiki_tools",
                "new-page",
                "--type",
                "concept",
                "--title",
                "Example Concept",
            ],
            cwd=project_dir,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)

        result = subprocess.run(
            ["python3", "-m", "wiki_tools", "check", "--strict"],
            cwd=project_dir,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_no_domain_specific_strings_in_generated_contract(self) -> None:
        project_dir = self.render_project()
        generated_text = (project_dir / "AGENTS.md").read_text(encoding="utf-8")
        for forbidden in ["AFL", "SAXS", "SANS", "RSoXS", "NIST", "formulation"]:
            self.assertNotIn(forbidden, generated_text)

    def test_optional_features_can_be_disabled(self) -> None:
        project_dir = self.render_project(
            include_slides="n",
            include_python_helpers="n",
        )
        self.assertFalse((project_dir / "slides").exists())
        self.assertFalse((project_dir / "wiki_tools").exists())
        self.assertFalse((project_dir / "skills" / "wiki-slides").exists())


if __name__ == "__main__":
    unittest.main()
