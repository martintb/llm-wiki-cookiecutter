---
name: pdf
description: Use this skill whenever the task involves a .pdf file or PDF-specific work such as extraction, OCR, page manipulation, form filling, generating a PDF from wiki material, or breaking a large book/report PDF into chapter files under raw/books/. Prefer Python tooling and keep the PDF step distinct from wiki ingestion and synthesis.
---

# PDF Skill

Use this skill whenever the task is about a `.pdf` file, not just when the input happens to be a PDF.

Typical triggers:

- read a report or paper stored as PDF
- extract text or tables
- OCR a scanned document
- split, merge, rotate, or reorder pages
- split a large book into chapter or section PDFs
- fill a form
- create a PDF artifact from markdown or other structured content

## Routing

Decide first what kind of job this is:

1. **Source handling**: the PDF is evidence that should usually stay under `raw/`
2. **Transformation**: the user wants pages combined, split, rotated, decrypted, or otherwise repaired
3. **Extraction**: the goal is text, tables, images, or metadata
4. **Output generation**: the user wants a new PDF produced from wiki or report content

Do not jump straight from a raw PDF to broad synthesis. If the PDF is a source, prepare it first and then hand off to `wiki-ingest`.

## Default Tool Stack

Prefer small, dependable tools with clear responsibilities:

- `pypdf` for page-level operations, metadata, merge/split, and basic extraction
- `pdfplumber` for text with layout awareness and table extraction
- `reportlab` for generating PDFs from structured content
- `pdftotext` when a command-line extractor is available and simpler than writing code
- `qpdf` for structural repairs, decryption, and page operations
- a TeX-native renderer such as Pandoc plus a LaTeX engine or Typst when the output contains equations
- OCR tooling only when extraction quality is clearly inadequate

Choose the lightest tool that can do the job well. Do not introduce a heavier stack unless the task justifies it.

## Python Dependencies

If the repo uses Python package metadata, the `pdf` extra should cover the default Python path:

- `pypdf` for splitting, merging, metadata, and quick text checks
- `pdfplumber` for layout-aware extraction and table-heavy pages
- `pdf2image` plus `Pillow` for rasterizing scanned pages before OCR
- `pytesseract` for OCR when a text layer is missing or unusable
- `reportlab` for PDF generation

`pytesseract` still requires the `tesseract` binary to be installed on the system, and `pdf2image` typically needs Poppler tools such as `pdftoppm`.

For math-heavy output generation, prefer an external renderer such as Pandoc with `tectonic`, `xelatex`, or another LaTeX-compatible engine, or Typst. Keep `reportlab` as the default only for equation-light documents unless equations are inserted as pre-rendered vector or raster assets.

## Workflow

1. Identify whether the PDF is source evidence, an intermediate artifact, or the final deliverable.
2. Preserve the original file when it is evidence.
3. Inspect the PDF before acting:
   - Is it text-based or scanned?
   - Are tables important?
   - Does page order or metadata matter?
   - Is the document encrypted or malformed?
4. Perform the narrow PDF task first.
5. Validate the result:
   - confirm page count
   - spot-check extracted text
   - call out OCR uncertainty
   - confirm output opens cleanly
6. If the PDF is source material, route the cleaned result into `wiki-ingest`.
7. If repo contents changed materially, record that work in `wiki/logs/maintenance.md`.

## Large Book Workflow

When a book-sized source arrives as one large PDF, do not usually ingest `full_book.pdf` as one giant source page. Break it into logical units first.

Preferred raw layout:

```text
raw/books/<book-title>/
  full_book.pdf
  chapters/
    manifest.json
    ch01-<chapter-title>.pdf
    ch02-<chapter-title>.pdf
```

Use this sequence:

1. Preserve the original as `raw/books/<book-title>/full_book.pdf`.
2. Check whether the PDF already has a usable text layer with `pypdf` or `pdfplumber`.
3. Derive chapter boundaries from bookmarks, the table of contents, visible divider pages, or a user-provided range list.
4. If the book is scanned, OCR only the pages you need for boundary detection first, usually the table of contents and chapter opener pages.
5. Write `raw/books/<book-title>/chapters/manifest.json` with chapter titles and page ranges.
6. Run `python skills/pdf/scripts/split_book.py --input raw/books/<book-title>/full_book.pdf --manifest raw/books/<book-title>/chapters/manifest.json --output-dir raw/books/<book-title>/chapters`.
7. Spot-check the first page of each output PDF and confirm page ranges before starting `wiki-ingest`.
8. Create one `wiki/sources/` page per chapter or section when the book is large enough that a single source page would become unwieldy.

The split outputs should follow the filename contract `ch01-<chapter-title>.pdf`, `ch02-<chapter-title>.pdf`, and so on even when the source uses parts, sections, or appendices.

Read `references/BOOK_SPLITTING.md` when the task is specifically about chapterizing a large book.

## Extraction Guidance

### Text-heavy PDFs

Start with `pypdf` or `pdftotext`. If the extracted text is garbled, missing columns, or obviously loses structure, escalate to `pdfplumber`.

### Table-heavy PDFs

Prefer `pdfplumber`. Return tables in a structured form when possible instead of flattening everything into prose.

### Scanned PDFs

Assume OCR output is imperfect. Preserve the original PDF, create a searchable or extracted derivative, and explicitly note where OCR confidence is weak.

For large books, use `pdf2image` and `pytesseract` selectively:

- OCR the table of contents to recover chapter titles and printed page numbers.
- OCR suspected chapter opener pages when bookmarks are absent.
- Do not OCR every page just to split the document unless there is no better boundary signal.

### Equation-heavy PDFs

If equations matter, prioritize notation fidelity over convenience.

- Do not assume plain text extraction preserves mathematical meaning.
- Prefer preserving the original PDF or page images when the goal is to retain exact notation.
- If you must extract equations into editable text, normalize them into standard LaTeX math delimiters and verify the result against the source.
- Flag ambiguous glyphs explicitly, especially minus versus en dash, `x` versus `\times`, superscripts, subscripts, primes, and Greek letters.

## Output Generation

When generating a new PDF:

- keep the editable source material as the system of record
- treat the PDF as a publication artifact, not the canonical editable format
- prefer deterministic layout over decorative complexity
- avoid Unicode superscript and subscript glyph tricks if the rendering stack is known to be fragile

When the output includes equations:

- Prefer a math-native pipeline such as Markdown or LaTeX rendered through Pandoc plus a LaTeX engine, or Typst.
- Use `reportlab` directly only when the document has no meaningful equations, or when each equation is inserted as a verified rendered asset.
- Keep equation source in standard LaTeX form rather than visually similar Unicode substitutions.
- Preserve display math, inline math, matrices, fractions, radicals, aligned equations, and numbered equations as semantic math, not hand-positioned text.

Minimum validation for equation-bearing PDFs:

- visually inspect every page containing equations
- confirm inline and display math are distinct and legible
- check fractions, superscripts, subscripts, radicals, matrices, and alignment
- verify line wrapping does not break equations incorrectly
- compare a sample of rendered equations against the editable source and the intended notation

If you cannot guarantee equation fidelity with the available toolchain, say so and recommend a TeX-native rendering path instead of shipping a silently degraded PDF.

## Wiki-Specific Rules

- Keep source PDFs under `raw/` whenever they are evidence.
- Keep book chapter derivatives under `raw/books/<book-title>/chapters/`.
- Do not replace `wiki-ingest` with ad hoc PDF summarization.
- Do not replace `wiki-integrate` with extraction output.
- If a user asks about what a PDF says, extraction is only preparation; the reusable knowledge belongs in `wiki/sources/`.
- For long books, prefer one source page per chapter or logical section over one page for the entire book.

## Defaults

Unless the user says otherwise:

- preserve the original source PDF
- prefer lossless transformations
- keep page order intact
- preserve provenance and metadata where practical
- describe extraction failures honestly
- make the smallest change that satisfies the request

## Good Outcome

A good PDF task leaves behind one of these:

- a repaired or transformed PDF that matches the requested operation
- clean extracted text or tables with caveats when needed
- a generated PDF plus its editable source
- a prepared source document ready for `wiki-ingest`
- for books, `full_book.pdf`, `chapters/manifest.json`, and validated `chapters/ch01-<title>.pdf` style outputs
