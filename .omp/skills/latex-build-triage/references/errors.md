# Common LaTeX build errors

| Log message | Cause | Fix |
|---|---|---|
| `LaTeX Warning: There were undefined references.` | Label/cite defined later or missing | Rebuild once; if it persists, grep the `\label`/cite key |
| `LaTeX Warning: Citation 'X' undefined` | Key not in `main.bib` or bib not rebuilt | Add/clean the entry (`skill://formatting-bibtex-entries`); rerun bibtex/latexmk |
| `! Missing $ inserted.` | Math char (`_`, `^`, `\alpha`) in text mode | Wrap in `$...$` or escape `\_` |
| `! Runaway argument?` | Unbalanced `{}` or missing `}` | Find the file:line; balance braces |
| `! Undefined control sequence.` | Unknown macro / missing package | Define the macro in `main.tex` or add `\usepackage` |
| `Overfull \hbox (NNpt too wide)` | Line too long / unbreakable | Rephrase, add `\-`, or accept if small; report only |
| `! File 'X' not found.` | Wrong `\input`/`\includegraphics` path | Use a repo-relative path under `sections/`/`figures/` |
