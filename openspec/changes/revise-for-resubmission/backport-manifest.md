# Backport manifest

## Audit boundary

- Thesis import commit: `037fa62` (`write(ch5): import Teralizer paper sections 2-6 verbatim`)
- Comparison: `git diff --name-status 037fa62..HEAD -- chapters/05-teralizer chapters/05-teralizer.tex`
- Audited paths: 54
- Source repository: `/Users/glockyco/src/github.com/glockyco/phd-thesis`
- Paper repository: `/Users/glockyco/src/github.com/glockyco/Teralizer-Paper`

Decisions apply to scientific content, not raw files. `PORT` preserves the thesis wording, explanation, formalization, and order substantially unchanged. It permits only necessary label, macro, assembly, generated-asset, or ACM-presentation changes. `ADAPT` preserves the thesis scientific content and changes only the minimum text required for standalone framing or retained paper context. `KEEP-PAPER` retains standalone material that the thesis omits. `DROP` excludes thesis-only framing, monograph cross-references, layout-only changes, or stale artifacts. `VERIFY` preserves the thesis content during Pass 1 and records a possible discrepancy or material improvement for explicit operator review after the complete backport. It does not authorize a manuscript change during Pass 1.

| # | Thesis status | Changed path | Decision | Paper destination and rationale |
|---:|:---:|---|---|---|
| 1 | M | `chapters/05-teralizer.tex` | DROP | Thesis chapter assembly and source note; `main.tex` remains paper-owned. |
| 2 | A | `chapters/05-teralizer/01-overview.tex` | ADAPT | Preserve the thesis scientific additions in `sections/01-introduction.tex`; remove chapter framing and adapt only the standalone roadmap and cross-references. |
| 3 | M | `chapters/05-teralizer/02-background.tex` | PORT | Port the thesis terminology and JARVIS background substantially unchanged into `sections/02-background.tex`; adapt only labels, macros, and paper assembly. |
| 4 | M | `chapters/05-teralizer/03-approach.tex` | PORT | Port the thesis concepts, formal definitions, stages, algorithm, widening account, and reduction semantics substantially unchanged. |
| 5 | M | `chapters/05-teralizer/04-evaluation-intro.tex` | PORT | Port the thesis evaluation framework and RQ0 integration substantially unchanged; retain paper setup that the thesis obtains from other chapters. |
| 6 | A | `chapters/05-teralizer/04-evaluation-rq0.tex` | PORT | Port the complete thesis JARVIS comparison and its limitations substantially unchanged into a new paper RQ0 section. |
| 7 | M | `chapters/05-teralizer/04-evaluation-rq1.tex` | VERIFY | Port the thesis RQ1 text unchanged during Pass 1; record any terminology, explanation, or value concern for deferred review. |
| 8 | M | `chapters/05-teralizer/04-evaluation-rq2.tex` | VERIFY | Port the thesis RQ2 text unchanged during Pass 1; record any explanation or measurement concern for deferred review. |
| 9 | M | `chapters/05-teralizer/04-evaluation-rq3.tex` | VERIFY | Port the thesis RQ3 text unchanged during Pass 1; record any count, reduction, runtime, or terminology concern for deferred review. |
| 10 | M | `chapters/05-teralizer/04-evaluation-rq4.tex` | VERIFY | Port the thesis RQ4 text unchanged during Pass 1; record any processing-cost or mutation-cost concern for deferred review. |
| 11 | M | `chapters/05-teralizer/04-evaluation-rq5.tex` | VERIFY | Port the thesis RQ5 text unchanged during Pass 1; record any controlled-population or failure-terminology concern for deferred review. |
| 12 | M | `chapters/05-teralizer/04-evaluation-rq6.tex` | PORT | Ported the complete thesis version 7 population, lifecycle, outcomes, and causes substantially unchanged into `sections/04-evaluation-09-rq6.tex`; adapted only paper labels, references, assembly, and the registered population provenance. |
| 13 | M | `chapters/05-teralizer/05-discussion.tex` | ADAPT | Preserve the thesis implications and limitations; adapt only context supplied by other thesis chapters and retain necessary standalone synthesis. |
| 14 | M | `chapters/05-teralizer/06-related-work.tex` | ADAPT | Preserve the thesis comparisons and LLM positioning; adapt only monograph cross-references and retain paper context and citations that the thesis omits. |
| 15 | A | `chapters/05-teralizer/07-bridge.tex` | DROP | Thesis-only bridge; the paper keeps a standalone conclusion. |
| 16 | A | `chapters/05-teralizer/data/rq0-breadth-summary.csv` | DROP | Do not copy thesis data; publish the registered RQ0 artifact from Teralizer. |
| 17 | A | `chapters/05-teralizer/data/rq0-pvc-budget.csv` | DROP | Do not copy thesis data; publish the registered RQ0 artifact from Teralizer. |
| 18 | A | `chapters/05-teralizer/data/rq0-table2-comparison.csv` | DROP | Do not copy thesis data; publish the registered RQ0 artifact from Teralizer. |
| 19 | M | `chapters/05-teralizer/figures/fig-teralizer-runtimes.tex` | VERIFY | Preserve the thesis factual caption content during Pass 1; record any report conflict for deferred review and keep the paper-owned wrapper, sizing, placement, label, and accessibility text. |
| 20 | M | `chapters/05-teralizer/figures/fig-test-runtime-differences.tex` | VERIFY | Preserve the thesis factual caption content during Pass 1; record any report conflict for deferred review and keep the paper-owned wrapper, sizing, placement, label, and accessibility text. |
| 21 | M | `chapters/05-teralizer/listings/alg-constraint-encoding.tex` | VERIFY | Retain the existing paper listing during Pass 1; record its possible removal after the thesis end-to-end algorithm is present and adapt only its ACM presentation if retained. |
| 22 | A | `chapters/05-teralizer/listings/alg-test-generalization.tex` | PORT | Port the thesis end-to-end algorithm substantially unchanged as a paper-owned ACM listing. |
| 23 | M | `chapters/05-teralizer/listings/lst-baseline-supplier.tex` | KEEP-PAPER | Thesis changes only float placement, color token, and list caption; retain the paper-owned presentation. |
| 24 | M | `chapters/05-teralizer/listings/lst-bonus-method.tex` | KEEP-PAPER | Thesis changes only whitespace, float placement, color token, and list caption; retain the paper-owned presentation. |
| 25 | M | `chapters/05-teralizer/listings/lst-extracted-specs.tex` | VERIFY | Port the thesis specifications unchanged during Pass 1; adapt only paper presentation and labels, and record any content concern for deferred review. |
| 26 | M | `chapters/05-teralizer/listings/lst-generalized-test.tex` | VERIFY | Port the thesis generated-test content unchanged during Pass 1; adapt only paper presentation and labels, and record any content concern for deferred review. |
| 27 | M | `chapters/05-teralizer/listings/lst-improved-supplier.tex` | KEEP-PAPER | Thesis changes only whitespace, float placement, color token, and list caption; retain the paper-owned presentation. |
| 28 | M | `chapters/05-teralizer/listings/lst-instrumented-test.tex` | VERIFY | Port the corrected thesis instrumentation content during Pass 1 and retain the paper-owned presentation. The thesis source now includes the previously missing closing `Driver` class brace. |
| 29 | M | `chapters/05-teralizer/listings/lst-java-input-encoding.tex` | VERIFY | Port the thesis input encoding unchanged during Pass 1; record any implementation discrepancy for deferred review. |
| 30 | M | `chapters/05-teralizer/listings/lst-java-output-encoding.tex` | VERIFY | Port the thesis output encoding unchanged during Pass 1; record any implementation discrepancy for deferred review. |
| 31 | M | `chapters/05-teralizer/listings/lst-jpf-config.tex` | VERIFY | Port the thesis configuration unchanged during Pass 1; record any executable-declaration discrepancy for deferred review. |
| 32 | M | `chapters/05-teralizer/listings/lst-naive-supplier.tex` | KEEP-PAPER | Thesis changes only float placement, color token, and list caption; retain the paper-owned presentation. |
| 33 | M | `chapters/05-teralizer/listings/lst-original-test.tex` | VERIFY | Port the thesis source-test content unchanged during Pass 1; retain paper-owned presentation and record any content concern for deferred review. |
| 34 | M | `chapters/05-teralizer/listings/lst-test-params-class.tex` | VERIFY | Port the thesis parameter encoding unchanged during Pass 1; record any implementation discrepancy for deferred review. |
| 35 | A | `chapters/05-teralizer/publish.toml` | ADAPT | Create a paper-local publication declaration with paper destinations and all required RQ0--RQ6 artifact keys. |
| 36 | A | `chapters/05-teralizer/tables/macros.tex` | DROP | Do not copy the thesis aggregate file; import the aggregate generated for the paper consumer unchanged. |
| 37 | A | `chapters/05-teralizer/tables/rq0-breadth-summary.tex` | DROP | Regenerate and publish directly from the registered RQ0 report. |
| 38 | A | `chapters/05-teralizer/tables/rq0-pvc-budget.tex` | DROP | Regenerate and publish directly from the registered RQ0 report. |
| 39 | A | `chapters/05-teralizer/tables/rq0-table2-comparison.tex` | DROP | Regenerate and publish directly from the registered RQ0 report. |
| 40 | M | `chapters/05-teralizer/tables/tab-dataset-statistics.tex` | VERIFY | Use the published controlled-study fragment; preserve the thesis narrative during Pass 1 and record any value or terminology conflict for deferred review. |
| 41 | M | `chapters/05-teralizer/tables/tab-detections-per-mutator.tex` | VERIFY | Use the published controlled-study fragment; preserve the thesis narrative during Pass 1 and record any value or terminology conflict for deferred review. |
| 42 | M | `chapters/05-teralizer/tables/tab-exclusions-breakdown-extended.tex` | DROP | Replaced with the directly published version 7 fragment at `tables/generated/tab-exclusions-breakdown-extended.tex` and paper-owned wrapper at `tables/tab-exclusions-breakdown-extended.tex`; did not copy the thesis table. |
| 43 | M | `chapters/05-teralizer/tables/tab-exclusions-breakdown.tex` | DROP | Replaced with the directly published controlled-study fragment at `tables/generated/tab-exclusions-breakdown.tex`; did not copy the thesis table. |
| 44 | M | `chapters/05-teralizer/tables/tab-exclusions-filtering-extended.tex` | DROP | Replaced with the directly published version 7 fragment at `tables/generated/tab-exclusions-filtering-extended.tex` and paper-owned wrapper at `tables/tab-exclusions-filtering-extended.tex`; did not copy the thesis table. |
| 45 | M | `chapters/05-teralizer/tables/tab-exclusions-filtering.tex` | DROP | Replace with a directly published version 7 RQ6 artifact; do not copy the thesis table. |
| 46 | M | `chapters/05-teralizer/tables/tab-lines-per-project.tex` | VERIFY | Use the published controlled-study fragment or retained paper table; preserve the thesis narrative and record any evidence conflict for deferred review. |
| 47 | D | `chapters/05-teralizer/tables/tab-mutants-per-project.tex` | PORT | Port the thesis deletion when the corresponding thesis narrative no longer consumes this table; do not infer another presentation change. |
| 48 | M | `chapters/05-teralizer/tables/tab-mutation-detection-comparison.tex` | VERIFY | Use the published controlled-study fragment or retained paper table; preserve the thesis narrative and record any evidence conflict for deferred review. |
| 49 | M | `chapters/05-teralizer/tables/tab-pareto-commons.tex` | VERIFY | Preserve the thesis narrative during Pass 1 and use the published fragment; record any terminology or value conflict for deferred review. |
| 50 | M | `chapters/05-teralizer/tables/tab-pareto-eqbench.tex` | VERIFY | Preserve the thesis narrative during Pass 1 and use the published fragment; record any terminology or value conflict for deferred review. |
| 51 | M | `chapters/05-teralizer/tables/tab-pit-mutators.tex` | VERIFY | Preserve the thesis narrative during Pass 1 and use the published fragment; record any mutator-terminology conflict for deferred review. |
| 52 | M | `chapters/05-teralizer/tables/tab-processing-failures.tex` | DROP | Replaced with the directly published version 7 fragment at `tables/generated/tab-processing-failures.tex` and paper-owned wrapper at `tables/tab-processing-failures.tex`. |
| 53 | M | `chapters/05-teralizer/tables/tab-runtime-per-project.tex` | VERIFY | Use the published controlled-study fragment or retained paper table; preserve the thesis narrative and record any evidence conflict for deferred review. |
| 54 | M | `chapters/05-teralizer/tables/tab-tests-per-project.tex` | VERIFY | Use the published controlled-study fragment or retained paper table; preserve the thesis narrative and record any evidence conflict for deferred review. |

## Deferred-candidate register

Pass 1 does not apply any entry in this register. After the complete backport builds, each entry requires an explicit operator decision. A rejected or undecided entry does not change the manuscript.

| ID | Status | Thesis source | Paper destination | Exact proposed change | Material benefit | Supporting evidence | Operator decision |
|---|---|---|---|---|---|---|---|
| DC-001 | OPEN | `chapters/05-teralizer/03-approach.tex` and `chapters/05-teralizer/listings/alg-test-generalization.tex` | `sections/03-approach-00-intro.tex` and `sections/03-approach-05-reduction.tex` | Keep the thesis retention equation and explanation during Pass 1. In Pass 2, consider defining `ORIGINAL` as the suite before preprocessing and `INITIAL` as the suite after shared preprocessing. Also consider explaining the two mutation-collection comparisons separately: `ORIGINAL` against `INITIAL` for original-test removal, and `INITIAL` against `INITIAL` plus generalized tests for generated-test retention. | Makes the thesis-level retention rule map explicitly to the two evaluated mutation rounds without replacing the direct scientific explanation during the backport. | `../test-generalization/src/main/java/teralizer/processing/diagnostics/GeneralizationLifecycleWriter.java`; `../test-generalization/src/main/resources/db/create-views.sql`; `../test-generalization/analysis/src/teralizer/rq1_mutation_detection.py` | PENDING; do not apply during Pass 1. |
| DC-002 | OPEN | `chapters/05-teralizer/03-approach.tex` | `sections/03-approach-03-spec-extraction.tex` | Keep the thesis statement that the default per-MUT timeout is 60~seconds during Pass 1. In Pass 2, either replace it with the current 10-second default or qualify 60~seconds as the evaluated setting if preserved run evidence records an override. | Distinguishes the current implementation default from the evaluated configuration without changing an empirical statement before its run provenance is checked. | `../test-generalization/src/main/resources/reference.conf` sets `jpf.timeout.per-assertion = 10`; the published run configuration remains to be checked. | PENDING; do not apply during Pass 1. |
| DC-003 | OPEN | `chapters/05-teralizer/listings/lst-generalized-test.tex` and `chapters/05-teralizer/listings/lst-baseline-supplier.tex` | `sections/03-approach-04-generalization.tex` | Keep the thesis identifiers during Pass 1. In Pass 2, change `BaseLineSupplier.class` to `BaselineSupplier.class` in the generalized-test listing. | Makes the case-sensitive supplier reference match the adjacent class declaration and removes an apparent Java example defect. | The generalized-test listing references `BaseLineSupplier.class`; the supplier listing declares `class BaselineSupplier`. | PENDING; do not apply during Pass 1. |

## Completeness check

The table contains one row for every path returned by the audit command. `PORT` and `ADAPT` rows remain open until their final manuscript source location is recorded. `VERIFY` rows remain open until their source location and deferred-candidate disposition are recorded. Every material proposal must appear in the deferred-candidate register before Pass 2.
