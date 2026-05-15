from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path


def slugify(text: str) -> str:
    value = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return re.sub(r"-{2,}", "-", value) or "untitled"


@dataclass(frozen=True)
class Chapter:
    title: str
    start_page: int
    end_page: int


def load_manifest(path: Path) -> list[Chapter]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    items = payload["chapters"] if isinstance(payload, dict) else payload
    chapters: list[Chapter] = []
    for item in items:
        chapters.append(
            Chapter(
                title=str(item["title"]).strip(),
                start_page=int(item["start_page"]),
                end_page=int(item["end_page"]),
            )
        )
    if not chapters:
        raise SystemExit("manifest must contain at least one chapter")
    return chapters


def validate_chapters(chapters: list[Chapter], total_pages: int) -> None:
    previous_end = 0
    for index, chapter in enumerate(chapters, start=1):
        if not chapter.title:
            raise SystemExit(f"chapter {index} is missing a title")
        if chapter.start_page < 1 or chapter.end_page < 1:
            raise SystemExit(f"chapter {index} has invalid page numbers")
        if chapter.start_page > chapter.end_page:
            raise SystemExit(f"chapter {index} start_page is after end_page")
        if chapter.end_page > total_pages:
            raise SystemExit(
                f"chapter {index} ends at page {chapter.end_page}, but the PDF only has {total_pages} pages"
            )
        if chapter.start_page <= previous_end:
            raise SystemExit(
                f"chapter {index} overlaps or is out of order: page {chapter.start_page} follows page {previous_end}"
            )
        previous_end = chapter.end_page


def split_book(input_path: Path, manifest_path: Path, output_dir: Path) -> None:
    try:
        from pypdf import PdfReader, PdfWriter
    except ModuleNotFoundError as exc:
        raise SystemExit(
            "Missing dependency: install the project's PDF extras so pypdf is available."
        ) from exc

    reader = PdfReader(input_path)
    chapters = load_manifest(manifest_path)
    validate_chapters(chapters, len(reader.pages))
    output_dir.mkdir(parents=True, exist_ok=True)

    for index, chapter in enumerate(chapters, start=1):
        writer = PdfWriter()
        for page_number in range(chapter.start_page - 1, chapter.end_page):
            writer.add_page(reader.pages[page_number])
        if reader.metadata:
            writer.add_metadata(
                {
                    "/Title": chapter.title,
                    "/Source": str(input_path),
                }
            )
        filename = f"ch{index:02d}-{slugify(chapter.title)}.pdf"
        output_path = output_dir / filename
        with output_path.open("wb") as handle:
            writer.write(handle)
        print(output_path)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Split a large book PDF into chapter PDFs using a manifest of page ranges."
    )
    parser.add_argument("--input", required=True, type=Path, help="Path to full_book.pdf")
    parser.add_argument(
        "--manifest",
        required=True,
        type=Path,
        help="Path to manifest.json with 1-based inclusive page ranges",
    )
    parser.add_argument(
        "--output-dir",
        required=True,
        type=Path,
        help="Directory where chapter PDFs will be written",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    split_book(args.input, args.manifest, args.output_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
