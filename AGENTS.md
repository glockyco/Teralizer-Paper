# Repository Guidelines — Teralizer Paper (ACM TOSEM)

LaTeX sources for "Teralizer: Semantics-Based Test Generalization from Conventional Unit Tests to
Property-Based Tests" (ACM `acmart`, TOSEM, options `[manuscript,screen,review]`).

## Structure
- `main.tex` — entry point; sections live in `sections/` (`\input{sections/<name>}`).
- `figures/`, `tables/` — assets (`\includegraphics{figures/<f>}`, `\input{tables/<f>}`); vector/PDF preferred.
- `data/` — CSV exports backing paper numbers where an export exists (not every number has a CSV).
- `main.bib` → `main.bbl`. Tool/dataset macros (`\ToolTeralizer`, `\ToolSPF`, `\ToolJqwik`,
  `\DatasetEqBench`, `\DatasetCommonsDev`, …) are defined in `main.tex`.

## Commands
| Task | Command |
|---|---|
| Build PDF | `latexmk -pdf -interaction=nonstopmode -file-line-error main.tex` |
| Watch build | `latexmk -pdf -pvc main.tex` |
| Lint | `chktex main.tex` (or a single `sections/<f>.tex`) |
| Word count | `texcount -1 main.tex` |
| Clean aux | `latexmk -c` (`-C` also removes the PDF) |

CI: GitHub Actions (`.github/workflows/latex-compile.yml`) runs the same `latexmk` build on every
push and pull request; it must stay green.

Run `python arxiv/build.py` to prepare the arXiv upload under `build/arxiv/`. It strips comments because arXiv publishes sources and ships the compiled bibliography to pin it to the local build, then checks that pdfLaTeX alone reproduces the normal PDF's text and writes the submission metadata.

## Writing rules (paper-specific)
- **Every number is reproducibly sourced.** Prefer a committed `data/*.csv` export with a
  `% Data source: <file>.csv` comment. Where no CSV export exists (e.g. the JARVIS scoreboard,
  computed from the analysis DB via `jarvis_scoreboard`), cite the reproducible analysis instead
  (`% Source: <command or planning-doc slug>`). Never fabricate or estimate numbers.
- Use the **macros** (`\ToolTeralizer`, `\DatasetEqBench`, …), never raw tool/dataset names.
- **Non-breaking spaces (`~`)**: before citations (`word~\cite{x}`), in inline enumerations
  (`(i)~...`), and between a number and its unit (`3~hours`).
- Run `chktex` after editing a `.tex` file; confirm cross-references resolve (build twice if refs changed).
- Abstract: 200–250 words.
- Don't open a sentence/paragraph with a bare `Table X`/`Figure Y`; integrate the reference.
- Bibliography: use `skill://research-evidence` for finding papers, retrieving full texts, and
  verifying DOI/BibTeX metadata for `main.bib` entries.

## Quality bars (self-check before yielding written prose)
- Every contribution claimed in the introduction maps to a results/evaluation subsection.
- A citation must support the *specific* claim it is attached to — not just the topic.
- No "proves"/"demonstrates" beyond what the data shows; numbers consistent across sections.

## Boundaries
- Never commit build artifacts (`*.aux`, `*.log`, `*.bbl`, `*.synctex.gz`, `*.out`, `*.fls`, `*.fdb_latexmk`).
  `main.pdf` only on releases, not routine commits.
- Use repo-relative paths under `figures/`/`tables/`; no absolute paths.

## Commits
Follow `skill://commit-policy`; `commitlint.config.js` defines the permitted types (e.g.
`revise(rq6): tighten exclusion wording`).
