# Resubmission questions

Use these questions when bringing the thesis revisions into the paper:

- Which constraints does IMPROVED's by-construction input generation fail to represent most often, and which could it support with modest effort?
- Would evaluating 500 or 1000 tries with mutation scores make the limits of parameter value coverage clearer?
- Does earlier work use mutation testing to identify focal methods? How many target projects lack mutation data, and for how many could it be collected?
- Can the additional experiments reuse the collected data and rerun only generalization?

The IMPROVED generators remain limited. Distinguish supported constraints from constraints that still need filtering when discussing applicability.

For the comparison with JARVIS, use the published-results comparison in `sections/04-evaluation-03-rq0.tex` and the limitations in [the JARVIS process notes](jarvis-process.md). Its unavailable implementation and template library prevent a direct rerun, its templates can overapproximate and underapproximate, it requires multiple existing tests, and generated tests can lose coverage. Treat a possible increase in failures at larger sampling budgets as a question to investigate, not a measured result.
