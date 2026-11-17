# Teralizer paper

LaTeX sources of the paper "Teralizer: Semantics-Based Test Generalization from Conventional Unit Tests to Property-Based Tests", set with `acmart`.

This repository is public. Correspondence, reviews and the plans that answer them, including the OpenSpec changes, belong in the private submodule `correspondence/`, because they must not appear in the public history. `git submodule update --init` fetches it only for accounts with access.

## Paper

- `main.tex` holds the preamble, the tool and dataset macros and the order of the files in `sections/`.
- `.omp/rules/prose.md` holds the writing rules for `main.tex` and `sections/`, and `.omp/rules/bib.md` the rules for `main.bib`.
- Find, retrieve and verify cited papers and their BibTeX metadata with `skill://research-evidence`.

## Numbers

- The analysis of the Teralizer repository generates the files that `publish.toml` declares, among them `tables/generated/macros.tex`, the tables in `tables/generated/`, the CSV files in `data/generated/` and several figures. Regenerate them with `PAPER_OUT=<this repository> scripts/publish-analysis.sh` in the Teralizer repository, and never edit them by hand, because the next run overwrites them.
- Write a number from the evaluation with its `\Tz...` macro from `tables/generated/macros.tex`, because the macro follows the data when the analysis changes.
- Where no generated macro or table holds a number, name its source in a `% Source:` comment above the sentence, such as the analysis command that computes it. Never estimate a number.

## Build

- Build with `latexmk -pdf -interaction=nonstopmode -file-line-error main.tex`. CI runs the same build on every push and pull request.
- Run `chktex` on each changed `.tex` file, and build twice when labels or references changed.
- `python arxiv/build.py` prepares the arXiv upload in `build/arxiv/`. It strips comments, because arXiv publishes the sources, and ships the compiled bibliography, so that arXiv uses exactly the references of the local build. It fails unless pdfLaTeX alone reproduces the text of the normal PDF.

## Commits

Follow `skill://commit-policy`. `commitlint.config.js` lists the permitted types, such as `revise` and `bib`.
