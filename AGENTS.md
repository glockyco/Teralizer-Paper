# Repository Guidelines — Teralizer Paper (ACM TOSEM)

LaTeX sources for "Teralizer: Semantics-Based Test Generalization from Conventional Unit Tests to
Property-Based Tests" (ACM `acmart`, TOSEM, options `[manuscript,screen,review]`).

## Structure
- `main.tex` — entry point; sections live in `sections/` (`\input{sections/<name>}`).
- `figures/`, `tables/` — assets (`\includegraphics{figures/<f>}`, `\input{tables/<f>}`); vector/PDF preferred.
- `data/` — CSV sources backing every number in the paper.
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

CI runs `latexmk` on **both** remotes — GitLab (`.gitlab-ci.yml`, internal AAU) and GitHub Actions
(`.github/workflows`, public). They must hold the same state; both must be green.

## Writing rules (paper-specific)
- **Every number has a data source.** Take quantitative claims from `data/*.csv`; add a
  `% Data source: <file>.csv` comment next to the value. Never fabricate or estimate numbers.
- Use the **macros** (`\ToolTeralizer`, `\DatasetEqBench`, …), never raw tool/dataset names.
- **Non-breaking spaces (`~`)**: before citations (`word~\cite{x}`), in inline enumerations
  (`(i)~...`), and between a number and its unit (`3~hours`).
- Run `chktex` after editing a `.tex` file; confirm cross-references resolve (build twice if refs changed).
- Abstract: 200–250 words.
- Don't open a sentence/paragraph with a bare `Table X`/`Figure Y`; integrate the reference.
- Bibliography: use `skill://searching-literature`, `skill://retrieving-paper-pdfs`, and
  `skill://formatting-bibtex-entries` for finding, acquiring, and formatting `main.bib`
  entries.

## Quality bars (self-check before yielding written prose)
- Every contribution claimed in the introduction maps to a results/evaluation subsection.
- A citation must support the *specific* claim it is attached to — not just the topic.
- No "proves"/"demonstrates" beyond what the data shows; numbers consistent across sections.

## Boundaries
- Never commit build artifacts (`*.aux`, `*.log`, `*.bbl`, `*.synctex.gz`, `*.out`, `*.fls`, `*.fdb_latexmk`).
  `main.pdf` only on releases, not routine commits.
- Use repo-relative paths under `figures/`/`tables/`; no absolute paths.

## Commits
Follow `skill://commit`. Short, imperative subject (e.g. "Rewrite sec:test-suite-reduction").
