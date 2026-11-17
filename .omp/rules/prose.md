---
description: Writing rules for the paper's LaTeX sources
globs:
  - "sections/**/*.tex"
  - "main.tex"
---

# Paper prose

- Write tool and dataset names with their macros from `main.tex`, such as `\ToolTeralizer` and `\DatasetEqBench`, never as plain text.
- Name the source of every number from the evaluation in a `% Source:` comment above the sentence.
- Use active voice for contributions ("We show ..."). Passive voice is fine for methodology.
- State what the evidence shows ("the data indicates"), not beliefs ("we believe"). Avoid "clearly", "obviously" and marketing adjectives, and claim no more than the data supports, such as "proves" or "demonstrates" for a trend.
- Present a result as its evidence, then its mechanism, then its implication.
- Attach a citation only to a claim it supports specifically, not to its topic.
- Map every contribution claimed in the introduction to a subsection of the evaluation, and keep each number consistent across sections.
- Integrate references to tables and figures into the sentence instead of opening a sentence with a bare "Table X".
- Use a non-breaking space (`~`) before citations (`word~\cite{x}`), in inline enumerations (`(i)~...`) and between a number and its unit (`3~hours`).
- Keep the abstract between 200 and 250 words.
