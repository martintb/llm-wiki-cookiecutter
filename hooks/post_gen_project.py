from __future__ import annotations

import shutil
from datetime import date
from pathlib import Path


PROJECT_ROOT = Path.cwd()
INCLUDE_SLIDES = "{{ cookiecutter.include_slides }}" == "y"
INCLUDE_HELPERS = "{{ cookiecutter.include_python_helpers }}" == "y"
LICENSE_NAME = "{{ cookiecutter.license }}"
MAINTAINER_NAME = "{{ cookiecutter.maintainer_name }}"
IGNORED_NAMES = {"__pycache__", ".DS_Store"}


def ensure_directory(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)
    gitkeep = path / ".gitkeep"
    if not any(child.name not in IGNORED_NAMES for child in path.iterdir()):
        gitkeep.write_text("", encoding="utf-8")


def remove_path(path: Path) -> None:
    if not path.exists():
        return
    if path.is_dir():
        shutil.rmtree(path)
    else:
        path.unlink()


def sync_skills() -> None:
    source_root = PROJECT_ROOT / "skills"
    targets = [
        PROJECT_ROOT / ".agents" / "skills",
        PROJECT_ROOT / ".claude" / "skills",
        PROJECT_ROOT / ".gemini" / "skills",
    ]
    for target in targets:
        if target.exists():
            shutil.rmtree(target)
        target.mkdir(parents=True, exist_ok=True)
        for skill_dir in sorted(source_root.iterdir()):
            if not skill_dir.is_dir() or skill_dir.name in IGNORED_NAMES:
                continue
            shutil.copytree(skill_dir, target / skill_dir.name)


def set_seed_dates() -> None:
    today = str(date.today())
    for path in [
        PROJECT_ROOT / "wiki" / "index.md",
        PROJECT_ROOT / "wiki" / "logs" / "maintenance.md",
        PROJECT_ROOT / "wiki" / "logs" / "audits.md",
    ]:
        text = path.read_text(encoding="utf-8")
        path.write_text(text.replace("__DATE__", today), encoding="utf-8")


def write_license() -> None:
    license_path = PROJECT_ROOT / "LICENSE"
    if LICENSE_NAME == "none":
        remove_path(license_path)
        return

    year = str(date.today().year)
    if LICENSE_NAME == "MIT":
        text = f"""MIT License

Copyright (c) {year} {MAINTAINER_NAME}

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
    elif LICENSE_NAME == "Apache-2.0":
        text = f"""Apache License
Version 2.0, January 2004

Copyright {year} {MAINTAINER_NAME}

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
    elif LICENSE_NAME == "BSD-3-Clause":
        text = f"""BSD 3-Clause License

Copyright (c) {year}, {MAINTAINER_NAME}
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.
3. Neither the name of the copyright holder nor the names of its
   contributors may be used to endorse or promote products derived from
   this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""
    else:
        text = ""
    license_path.write_text(text, encoding="utf-8")


if not INCLUDE_SLIDES:
    remove_path(PROJECT_ROOT / "slides")
    remove_path(PROJECT_ROOT / "templates" / "marp.md")
    remove_path(PROJECT_ROOT / "templates" / "slide-deck.md")
    remove_path(PROJECT_ROOT / "skills" / "wiki-slides")

if not INCLUDE_HELPERS:
    remove_path(PROJECT_ROOT / "wiki_tools")

for directory in [
    PROJECT_ROOT / "inbox",
    PROJECT_ROOT / "raw" / "books",
    PROJECT_ROOT / "raw" / "papers",
    PROJECT_ROOT / "raw" / "reports",
    PROJECT_ROOT / "raw" / "web",
    PROJECT_ROOT / "raw" / "data",
    PROJECT_ROOT / "raw" / "notes",
    PROJECT_ROOT / "raw" / "misc",
    PROJECT_ROOT / "wiki" / "sources",
    PROJECT_ROOT / "wiki" / "concepts",
    PROJECT_ROOT / "wiki" / "people",
    PROJECT_ROOT / "wiki" / "organizations",
    PROJECT_ROOT / "wiki" / "projects",
    PROJECT_ROOT / "wiki" / "datasets",
    PROJECT_ROOT / "wiki" / "decisions",
    PROJECT_ROOT / "wiki" / "synthesis",
    PROJECT_ROOT / "wiki" / "questions",
    PROJECT_ROOT / "wiki" / "logs",
]:
    ensure_directory(directory)

if INCLUDE_SLIDES:
    for directory in [
        PROJECT_ROOT / "slides" / "drafts",
        PROJECT_ROOT / "slides" / "final",
        PROJECT_ROOT / "slides" / "assets",
        PROJECT_ROOT / "slides" / "templates",
    ]:
        ensure_directory(directory)

set_seed_dates()
sync_skills()
write_license()
