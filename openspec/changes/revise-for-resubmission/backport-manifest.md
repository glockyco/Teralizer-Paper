# Backport manifest

## Audit boundary

- Thesis import commit: `037fa62` (`write(ch5): import Teralizer paper sections 2-6 verbatim`)
- Comparison: `git diff --name-status 037fa62..HEAD -- chapters/05-teralizer chapters/05-teralizer.tex`
- Audited paths: 54
- Source repository: `/Users/glockyco/src/github.com/glockyco/phd-thesis`
- Paper repository: `/Users/glockyco/src/github.com/glockyco/Teralizer-Paper`

Decisions apply to scientific content, not raw files. `PORT` means transfer substantive content. `ADAPT` means preserve the scientific change but rewrite it for the standalone ACM paper. `KEEP-PAPER` means retain the paper version unless later evidence identifies a defect. `DROP` means do not transfer the thesis-only or stale artifact. `VERIFY` means compare the thesis change with evidence and the paper, then record a more specific disposition before final verification.

| # | Thesis status | Changed path | Decision | Paper destination and rationale |
|---:|:---:|---|---|---|
| 1 | M | `chapters/05-teralizer.tex` | DROP | Thesis chapter assembly and source note; `main.tex` remains paper-owned. |
| 2 | A | `chapters/05-teralizer/01-overview.tex` | ADAPT | Use substantive motivation, contribution, and roadmap changes in `sections/01-introduction.tex`; remove thesis framing and bridge references. |
| 3 | M | `chapters/05-teralizer/02-background.tex` | PORT | Reconcile current terminology and JARVIS background into `sections/02-background.tex`. |
| 4 | M | `chapters/05-teralizer/03-approach.tex` | PORT | Primary source for concepts, formal definitions, current stages, algorithm, widening, and reduction semantics. |
| 5 | M | `chapters/05-teralizer/04-evaluation-intro.tex` | PORT | Update the paper evaluation framework and insert RQ0 while preserving standalone setup detail. |
| 6 | A | `chapters/05-teralizer/04-evaluation-rq0.tex` | PORT | Add a new paper RQ0 section with the complete JARVIS comparison and its limitations. |
| 7 | M | `chapters/05-teralizer/04-evaluation-rq1.tex` | VERIFY | Audit terminology, explanations, and values against generated controlled-study evidence before adapting `sections/04-evaluation-04-rq1.tex`. |
| 8 | M | `chapters/05-teralizer/04-evaluation-rq2.tex` | VERIFY | Audit substantive clarifications and measurements before adapting `sections/04-evaluation-05-rq2.tex`. |
| 9 | M | `chapters/05-teralizer/04-evaluation-rq3.tex` | VERIFY | Audit counts, reduction semantics, and runtime claims before adapting `sections/04-evaluation-06-rq3.tex`. |
| 10 | M | `chapters/05-teralizer/04-evaluation-rq4.tex` | VERIFY | Audit processing and mutation-testing costs before adapting `sections/04-evaluation-07-rq4.tex`. |
| 11 | M | `chapters/05-teralizer/04-evaluation-rq5.tex` | VERIFY | Audit controlled-population failure terminology before adapting `sections/04-evaluation-08-rq5.tex`. |
| 12 | M | `chapters/05-teralizer/04-evaluation-rq6.tex` | PORT | Replace `sections/04-evaluation-09-rq6.tex` atomically with the version 7 population, lifecycle, outcomes, and causes. |
| 13 | M | `chapters/05-teralizer/05-discussion.tex` | ADAPT | Port evidence-backed implications and limitations while retaining paper-specific standalone synthesis. |
| 14 | M | `chapters/05-teralizer/06-related-work.tex` | ADAPT | Port substantive comparison and LLM positioning; retain complete paper context and citations. |
| 15 | A | `chapters/05-teralizer/07-bridge.tex` | DROP | Thesis-only bridge; the paper keeps a standalone conclusion. |
| 16 | A | `chapters/05-teralizer/data/rq0-breadth-summary.csv` | DROP | Do not copy thesis data; publish the registered RQ0 artifact from Teralizer. |
| 17 | A | `chapters/05-teralizer/data/rq0-pvc-budget.csv` | DROP | Do not copy thesis data; publish the registered RQ0 artifact from Teralizer. |
| 18 | A | `chapters/05-teralizer/data/rq0-table2-comparison.csv` | DROP | Do not copy thesis data; publish the registered RQ0 artifact from Teralizer. |
| 19 | M | `chapters/05-teralizer/figures/fig-teralizer-runtimes.tex` | VERIFY | Compare factual caption content with the report; keep paper-owned wrapper, sizing, placement, label, and accessibility text. |
| 20 | M | `chapters/05-teralizer/figures/fig-test-runtime-differences.tex` | VERIFY | Compare factual caption content with the report; keep paper-owned wrapper, sizing, placement, label, and accessibility text. |
| 21 | M | `chapters/05-teralizer/listings/alg-constraint-encoding.tex` | VERIFY | Retain only if still needed after the end-to-end algorithm is added; adapt listing style to ACM conventions. |
| 22 | A | `chapters/05-teralizer/listings/alg-test-generalization.tex` | PORT | Add the current end-to-end algorithm as a paper-owned ACM listing. |
| 23 | M | `chapters/05-teralizer/listings/lst-baseline-supplier.tex` | KEEP-PAPER | Thesis changes only float placement, color token, and list caption; retain the paper-owned presentation. |
| 24 | M | `chapters/05-teralizer/listings/lst-bonus-method.tex` | KEEP-PAPER | Thesis changes only whitespace, float placement, color token, and list caption; retain the paper-owned presentation. |
| 25 | M | `chapters/05-teralizer/listings/lst-extracted-specs.tex` | VERIFY | Port corrected specifications; adapt presentation and labels to the paper. |
| 26 | M | `chapters/05-teralizer/listings/lst-generalized-test.tex` | VERIFY | Port corrected generated-test content; adapt presentation and labels to the paper. |
| 27 | M | `chapters/05-teralizer/listings/lst-improved-supplier.tex` | KEEP-PAPER | Thesis changes only whitespace, float placement, color token, and list caption; retain the paper-owned presentation. |
| 28 | M | `chapters/05-teralizer/listings/lst-instrumented-test.tex` | VERIFY | Port substantive instrumentation corrections; retain paper-owned presentation. |
| 29 | M | `chapters/05-teralizer/listings/lst-java-input-encoding.tex` | VERIFY | Port encoding corrections that match the current implementation. |
| 30 | M | `chapters/05-teralizer/listings/lst-java-output-encoding.tex` | VERIFY | Port encoding corrections that match the current implementation. |
| 31 | M | `chapters/05-teralizer/listings/lst-jpf-config.tex` | VERIFY | Port configuration corrections that match executable declarations. |
| 32 | M | `chapters/05-teralizer/listings/lst-naive-supplier.tex` | KEEP-PAPER | Thesis changes only float placement, color token, and list caption; retain the paper-owned presentation. |
| 33 | M | `chapters/05-teralizer/listings/lst-original-test.tex` | VERIFY | Port corrected source-test content; retain paper-owned presentation. |
| 34 | M | `chapters/05-teralizer/listings/lst-test-params-class.tex` | VERIFY | Port parameter-encoding corrections that match the current implementation. |
| 35 | A | `chapters/05-teralizer/publish.toml` | ADAPT | Create a paper-local publication declaration with paper destinations and all required RQ0--RQ6 artifact keys. |
| 36 | A | `chapters/05-teralizer/tables/macros.tex` | DROP | Do not copy the thesis aggregate file; import the aggregate generated for the paper consumer unchanged. |
| 37 | A | `chapters/05-teralizer/tables/rq0-breadth-summary.tex` | DROP | Regenerate and publish directly from the registered RQ0 report. |
| 38 | A | `chapters/05-teralizer/tables/rq0-pvc-budget.tex` | DROP | Regenerate and publish directly from the registered RQ0 report. |
| 39 | A | `chapters/05-teralizer/tables/rq0-table2-comparison.tex` | DROP | Regenerate and publish directly from the registered RQ0 report. |
| 40 | M | `chapters/05-teralizer/tables/tab-dataset-statistics.tex` | VERIFY | Compare with the controlled-study report and publish the authoritative table for the paper. |
| 41 | M | `chapters/05-teralizer/tables/tab-detections-per-mutator.tex` | VERIFY | Compare with the controlled-study report and publish the authoritative table for the paper. |
| 42 | M | `chapters/05-teralizer/tables/tab-exclusions-breakdown-extended.tex` | DROP | Replace with a directly published version 7 RQ6 artifact; do not copy the thesis table. |
| 43 | M | `chapters/05-teralizer/tables/tab-exclusions-breakdown.tex` | DROP | Replace with a directly published version 7 RQ6 artifact; do not copy the thesis table. |
| 44 | M | `chapters/05-teralizer/tables/tab-exclusions-filtering-extended.tex` | DROP | Replace with a directly published version 7 RQ6 artifact; do not copy the thesis table. |
| 45 | M | `chapters/05-teralizer/tables/tab-exclusions-filtering.tex` | DROP | Replace with a directly published version 7 RQ6 artifact; do not copy the thesis table. |
| 46 | M | `chapters/05-teralizer/tables/tab-lines-per-project.tex` | VERIFY | Compare with controlled-study evidence and publish or retain the authoritative paper table. |
| 47 | D | `chapters/05-teralizer/tables/tab-mutants-per-project.tex` | PORT | Remove the stale paper table if the current RQ structure and generated assets no longer consume it. |
| 48 | M | `chapters/05-teralizer/tables/tab-mutation-detection-comparison.tex` | VERIFY | Compare with controlled-study evidence and publish or retain the authoritative paper table. |
| 49 | M | `chapters/05-teralizer/tables/tab-pareto-commons.tex` | VERIFY | Preserve measured values; reconcile terminology and generated ownership. |
| 50 | M | `chapters/05-teralizer/tables/tab-pareto-eqbench.tex` | VERIFY | Preserve measured values; reconcile terminology and generated ownership. |
| 51 | M | `chapters/05-teralizer/tables/tab-pit-mutators.tex` | VERIFY | Compare with controlled-study evidence and current mutator terminology. |
| 52 | M | `chapters/05-teralizer/tables/tab-processing-failures.tex` | DROP | Replace with a directly published version 7 processing-failure artifact. |
| 53 | M | `chapters/05-teralizer/tables/tab-runtime-per-project.tex` | VERIFY | Compare with controlled-study evidence and publish or retain the authoritative paper table. |
| 54 | M | `chapters/05-teralizer/tables/tab-tests-per-project.tex` | VERIFY | Compare with controlled-study evidence and publish or retain the authoritative paper table. |

## Completeness check

The table contains one row for every path returned by the audit command. `VERIFY`, `PORT`, and `ADAPT` rows remain open until their final manuscript source location and evidence disposition are recorded during the corresponding revision task.
