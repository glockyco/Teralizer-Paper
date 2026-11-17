# Teralizer paper

LaTeX sources of the paper "Teralizer: Semantics-Based Test Generalization from Conventional Unit Tests to Property-Based Tests", set with `acmart`.

This repository is public. Correspondence, reviews and the plans that answer them belong in the private repository `glockyco/Teralizer-Paper-Correspondence`, because they must not appear in the public history.

## Paper

- `main.tex` holds the preamble, the tool and dataset macros and the order of the files in `sections/`.
- `.omp/rules/prose.md` holds the writing rules for `main.tex` and `sections/`, and `.omp/rules/bib.md` the rules for `main.bib`.
- Find, retrieve and verify cited papers and their BibTeX metadata with `skill://research-evidence`.
- Name the source of every number from the evaluation in a `% Source:` comment above the sentence, such as the analysis report of the Teralizer repository that computes it. Never estimate a number.

## Build

- Build with `latexmk -pdf -interaction=nonstopmode -file-line-error main.tex`. CI runs the same build on every push and pull request.
- Run `chktex` on each changed `.tex` file, and build twice when labels or references changed.

## Commits

Follow `skill://commit-policy`. `commitlint.config.js` lists the permitted types, such as `revise` and `bib`.
