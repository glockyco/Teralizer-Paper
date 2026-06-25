---
name: latex-build-triage
description: Build the paper with latexmk and triage compile errors/warnings. Use when a LaTeX build fails, references/citations are undefined, or the user mentions latexmk/chktex/overfull boxes.
---

# LaTeX build triage

## Build
```bash
latexmk -pdf -interaction=nonstopmode -file-line-error main.tex
```
Run twice if cross-references or citations changed (latexmk usually handles this, but undefined
refs on a single pass clear on the second).

## Triage
1. Read `main.log`; match the first error against `references/errors.md`.
2. "Undefined references"/"Citation undefined" → rebuild once; if still undefined, the label/key is
   missing or misspelled — grep `sections/` and `main.bib`.
3. "Missing $ inserted" / "Runaway argument" → find the file:line in the log, fix the math/brace.
4. Overfull/underfull `\hbox` → report only (do not auto-rewrite prose) unless asked.
5. After fixing, rebuild and confirm zero "Undefined" and zero new errors.

See `references/errors.md` for the error catalogue.
