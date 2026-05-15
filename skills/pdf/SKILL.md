---
name: pdf
description: Use this skill whenever the task involves a .pdf file or PDF-specific work such as extraction, OCR, page manipulation, form filling, or generating a PDF from wiki material. Prefer Python tooling and keep the PDF step distinct from wiki ingestion and synthesis.
---

# PDF Skill

Use this skill whenever the task is about a `.pdf` file, not just when the input happens to be a PDF.

Typical triggers:

- read a report or paper stored as PDF
- extract text or tables
- OCR a scanned document
- split, merge, rotate, or reorder pages
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
- OCR tooling only when extraction quality is clearly inadequate

Choose the lightest tool that can do the job well. Do not introduce a heavier stack unless the task justifies it.

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

## Extraction Guidance

### Text-heavy PDFs

Start with `pypdf` or `pdftotext`. If the extracted text is garbled, missing columns, or obviously loses structure, escalate to `pdfplumber`.

### Table-heavy PDFs

Prefer `pdfplumber`. Return tables in a structured form when possible instead of flattening everything into prose.

### Scanned PDFs

Assume OCR output is imperfect. Preserve the original PDF, create a searchable or extracted derivative, and explicitly note where OCR confidence is weak.

## Output Generation

When generating a new PDF:

- keep the editable source material as the system of record
- treat the PDF as a publication artifact, not the canonical editable format
- prefer deterministic layout over decorative complexity
- avoid Unicode superscript and subscript glyph tricks if the rendering stack is known to be fragile

## Wiki-Specific Rules

- Keep source PDFs under `raw/` whenever they are evidence.
- Do not replace `wiki-ingest` with ad hoc PDF summarization.
- Do not replace `wiki-integrate` with extraction output.
- If a user asks about what a PDF says, extraction is only preparation; the reusable knowledge belongs in `wiki/sources/`.

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
