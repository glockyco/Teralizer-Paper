---
description: Build the paper with latexmk and report only actionable diagnostics
---

Build the paper:

Run `latexmk -pdf -interaction=nonstopmode -file-line-error main.tex` (rerun once if cross-refs
changed). Then summarize from `main.log`: undefined references, multiply-defined labels, undefined
citations, and overfull `\hbox` over 10pt. Do NOT edit sources — report the actionable diagnostics
only. If a build error appears, follow `skill://latex-build-triage`.
