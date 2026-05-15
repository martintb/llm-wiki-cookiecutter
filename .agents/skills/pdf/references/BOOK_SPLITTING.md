# Large Book Splitting

Use this reference when a source arrives as a single long PDF and the right first step is to break it into chapter or section files under `raw/books/`.

## Target Layout

```text
raw/books/<book-title>/
  full_book.pdf
  chapters/
    manifest.json
    ch01-introduction.pdf
    ch02-core-ideas.pdf
```

Keep `full_book.pdf` untouched. Treat the `chapters/` directory as derived raw material that still belongs with the source.

## Step 1: Check For A Text Layer

Start with a cheap inspection before you reach for OCR.

```python
from pathlib import Path
from pypdf import PdfReader

reader = PdfReader(Path("raw/books/example-book/full_book.pdf"))
for page_number in range(min(5, len(reader.pages))):
    text = reader.pages[page_number].extract_text() or ""
    print(page_number + 1, repr(text[:120]))
```

If chapter opener pages and the table of contents already return readable text, stay in the text-first path. Only escalate to OCR when extraction is blank or clearly unusable.

## Step 2: Build The Boundary Map

Preferred order of evidence:

1. PDF bookmarks or outline entries.
2. Table of contents text.
3. Visible chapter title pages.
4. A user-provided page-range list.

Use PDF page numbers, not printed page numbers, in the final manifest. If the table of contents uses printed page numbers, compute the offset once and apply it consistently.

## Step 3: OCR Only What You Need

When the document is scanned, OCR the table of contents and a few likely divider pages instead of rasterizing the entire book.

```python
from pathlib import Path

from pdf2image import convert_from_path
import pytesseract

pdf_path = Path("raw/books/example-book/full_book.pdf")
images = convert_from_path(pdf_path, first_page=3, last_page=6, dpi=300)
for index, image in enumerate(images, start=3):
    text = pytesseract.image_to_string(image)
    print(f"--- page {index} ---")
    print(text[:2000])
```

Notes:

- `pytesseract` needs the `tesseract` executable available on `PATH`.
- `pdf2image` usually needs Poppler installed so `pdftoppm` is available.
- OCR the smallest page set that answers the boundary question.

## Step 4: Write `manifest.json`

The bundled splitter script expects either a top-level list or an object with a `chapters` list. Page numbers are 1-based and inclusive.

```json
{
  "chapters": [
    {
      "title": "Introduction",
      "start_page": 9,
      "end_page": 24
    },
    {
      "title": "Core Ideas",
      "start_page": 25,
      "end_page": 57
    }
  ]
}
```

## Step 5: Split The PDF

Run the bundled script from the repo root:

```bash
python skills/pdf/scripts/split_book.py \
  --input raw/books/example-book/full_book.pdf \
  --manifest raw/books/example-book/chapters/manifest.json \
  --output-dir raw/books/example-book/chapters
```

Expected outputs:

- `raw/books/example-book/chapters/ch01-introduction.pdf`
- `raw/books/example-book/chapters/ch02-core-ideas.pdf`

## Step 6: Validate Before Ingest

Check these points before creating `wiki/sources/` pages:

- chapter count matches the manifest
- filenames follow `chNN-title.pdf`
- first and last pages of each split look correct
- page ranges do not overlap or leave accidental gaps
- OCR-derived titles were normalized carefully and not guessed

## After Splitting

For a long book, create one `wiki/sources/` page per chapter or logical section rather than one source page for the entire volume. Keep cross-chapter synthesis in `wiki/synthesis/` or another integrated page type.
