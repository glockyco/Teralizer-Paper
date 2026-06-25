---
description: BibTeX conventions for main.bib (keys, fields, formatting)
globs:
  - "main.bib"
---

# main.bib conventions

- Target file: `main.bib`.
- Keys: `author_year_keyword` (first-author surname lowercase, 4-digit year, one keyword); never
  rename an existing key without updating every `\cite{...}`.
- Format every entry per `skill://formatting-bibtex-entries` (title-casing, brace-protected
  acronyms, expanded venues, lowercase DOIs, en-dash pages, stripped DBLP cruft).
- To find/acquire a paper and its metadata, use `skill://searching-literature` (OpenAlex/Crossref
  lead) then `skill://retrieving-paper-pdfs`.
