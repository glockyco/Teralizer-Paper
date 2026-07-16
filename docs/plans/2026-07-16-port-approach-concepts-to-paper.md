---
title: Port Approach Concepts & Algorithm Subsection to the Paper
type: plan
status: active
created: 2026-07-16
---

# Port Approach Concepts & Algorithm Subsection to the Paper

Port the thesis §5.3 restructure into the paper's Approach section to address TOSEM
reviewer #1 ("Section 3 jumps directly into instantiation/implementation without an
abstract description of concepts and algorithms; hard to separate existing techniques
from contributions; conflicts with the language-independence claim").

The approved design already exists and is built/verified in the thesis:
`~/Projects/phd-thesis/chapters/05-teralizer/03-approach.tex` (subsection
"Concepts and Algorithm", `\label{sec:teralizer-approach-concepts}`) and
`~/Projects/phd-thesis/chapters/05-teralizer/listings/alg-test-generalization.tex`.
This plan is the execution: adapt that content to the paper's conventions (ACM
`acmart`, numbered `\cite`, `\ref` not `\cref`, `listings` not `minted`, literal
"i.e."/"e.g." — the paper defines no `\ie`/`\eg`).

Build/verify command (from `AGENTS.md`):
`latexmk -pdf -interaction=nonstopmode -file-line-error main.tex` (build twice when
refs change), then `chktex` on edited files. Never commit build artifacts.

## Scope boundaries

- The paper intro (`03-approach-00-intro.tex`) ALREADY contains: the five-stage list,
  the running example (`lst:bonus-method`, `lst:original-test`), the implementation
  scope paragraph (Java 5–8, Maven/Gradle, dependency auto-injection of jqwik/PIT/
  JaCoCo — thesis P8), and the stage roadmap. Do NOT duplicate these.
- The new content is only the abstract layer the paper lacks: the problem model, the
  end-to-end algorithm, the formal input/output specification, the oracle semantics,
  the extraction/solver-free framing, the purity/domain scope, and the established-
  techniques + capability-independence demarcation.
- Keep the concepts subsection variant-agnostic (no `\VariantBaseline`/`\VariantNaive`/
  `\VariantImproved`); those belong to stage 4 (`03-approach-04-generalization.tex`).
- Non-goal: revising `figures/fig_approach.drawio` (tracked separately).

## File map

- Create `sections/03-approach-01-concepts.tex`: the "Concepts and Algorithm"
  subsection (problem model, algorithm float, formal spec, oracle, extraction scope,
  demarcation). One new `\subsection` under the existing `\section{Approach}`.
- Modify `main.tex`: add `\input{sections/03-approach-01-concepts}` between
  `03-approach-00-intro` (line 345) and `03-approach-01-test-analysis` (line 346).
- Modify `sections/03-approach-00-intro.tex`: update the closing roadmap to point to
  the concepts subsection first; align regression-framing terminology
  ("input partitions" → "execution paths" in the two running-example sentences).
- Modify `main.bib`: add the `khurshid_2003_gse` entry (copy from
  `~/Projects/phd-thesis/bibliography/references.bib`).
- Modify `sections/03-approach-03-spec-extraction.tex`,
  `sections/03-approach-04-generalization.tex`,
  `sections/03-approach-05-reduction.tex`: terminology pass replacing "path-exact"
  usages with "input/output specification" per the thesis terminology decision.

## Task 1: Add the missing bibliography entry

**Files:**
- Modify: `main.bib`

- [ ] Copy the `@inproceedings{khurshid_2003_gse, ...}` entry verbatim from
  `~/Projects/phd-thesis/bibliography/references.bib` into `main.bib`.
  Verification: `grep -c 'khurshid_2003_gse' main.bib` returns 1.

- [ ] Commit.
  Message: `bib: add Khurshid 2003 generalized symbolic execution`

## Task 2: Create the Concepts and Algorithm subsection

**Files:**
- Create: `sections/03-approach-01-concepts.tex`
- Modify: `main.tex`

Port these paragraphs from the thesis §5.3 "Concepts and Algorithm" subsection,
adapting notation to the paper (see conversion rules below):

- [ ] Problem model (thesis P1): `\subsection{Concepts and Algorithm}` with
  `\label{sec:approach-concepts}`. Define MUT and MUT call, then the three
  assertion–MUT pairs of `testCalculate` (250↔calculate(2500,1000),
  75↔calculate(1500,1000), 0↔calculate(500,1000)); close with "Each pair yields one
  generalized test."

- [ ] End-to-end algorithm (thesis P2 + `alg-test-generalization.tex`): an
  `algorithm`/`algorithmic` float `\label{alg:test-generalization}` with the same
  five-stage body (inputs `P`, `T`; sets `G`, `A`; `IdentifyMutCall`,
  `ExtractSpecification`, `CreateGeneralizedTest`; `⊥` skips; retain `g` iff
  `killed(g) ⊄ killed(T)`; remove `t` iff `assertions(t) ⊆ A`). Stage comments
  reference the paper's stage labels via `\ref` (`sec:test-assertion-analysis`,
  `sec:tested-method-identification`, `sec:specification-extraction`,
  `sec:generalized-test-creation`, `sec:test-suite-reduction`). Follow with the P2
  prose walkthrough. Point the exclusion sentence at the paper's applicability
  results (RQ5/RQ6 — resolve their `\label`s in `04-evaluation-08-rq5.tex` /
  `04-evaluation-09-rq6.tex`; if none exist, add `\label{sec:rq5}`/`\label{sec:rq6}`
  at those section heads and reference them).

- [ ] Formal input/output specification (thesis P3): the `(pc, out)` pair over
  generalizable parameters `x_1,…,x_n` with the two enumerated properties
  ((i) `pc` holds iff same execution path as the seed call; (ii) `m(x̄)=out(x̄)` on
  the partition), the "input partition" definition, and the good-performance instance
  (`pc = sales/2 < target ∧ sales ≥ target`, `out = sales/20`).

- [ ] Oracle semantics (thesis P4): `out` becomes the oracle; a regression anywhere
  in the partition fails the generalized test once a sampled input exposes it, versus
  the single seed point; the boundary-mutation instance.

- [ ] Extraction framing (thesis P5): single-path symbolic analysis executes
  concretely and tracks symbolic values from the MUT call; one path, no backtracking
  or constraint solving.

- [ ] Scope (thesis P6): purity requirement (deterministic, side-effect-free,
  parameter-dependent) and the numeric/boolean domain restriction, with the
  partial-generalization / exclusion consequence.

- [ ] Demarcation (thesis P7): the five stages build on established techniques
  (`cadar_2013_symbolic`, `baldoni_2018_survey`, `pasareanu_2013_symbolic`); the
  purity/domain restrictions stem from the employed analysis, not the approach —
  properties (i)/(ii) do not prescribe how specifications are obtained — with
  `amadini_2021_string_survey` and `khurshid_2003_gse` as directions that would relax
  them. Do NOT re-list the Java toolchain already named in the intro's auto-injection
  paragraph; reference it rather than repeat it.

Conversion rules (thesis → paper):
- `\cref{X}` / `\crefrange{..}` → `Section~\ref{X}` / `Algorithm~\ref{X}` (match the
  intro's existing `Section~\ref{...}` style).
- `\ie` / `\eg` → literal "i.e." / "e.g.".
- Listing refs `\cref{lst:...}` → `Listing~\ref{lst:...}` (labels `lst:bonus-method`,
  `lst:original-test` already exist in the intro).
- Enumerate properties with `(i)`/`(ii)` labels as in the thesis.
- Drop thesis-only `\cite{replicationpackage_teralizer}` / `meszaros_2007_xunit`
  duplication — `meszaros_2007_xunit` sits on the unit-test-anatomy sentence only.

- [ ] Wire `\input{sections/03-approach-01-concepts}` into `main.tex` immediately
  after `\input{sections/03-approach-00-intro}` (line 345).

- [ ] Build: `latexmk -pdf -interaction=nonstopmode -file-line-error main.tex` (twice).
  Verification: `grep -c 'undefined' main.log` returns 0 and the Approach section
  renders the new subsection before "Test and Assertion Analysis".
  Expected: no undefined references (`alg:test-generalization`, `sec:approach-concepts`,
  the five stage labels, and both listing labels all resolve).

- [ ] `chktex sections/03-approach-01-concepts.tex` — no new warning classes beyond
  those already present in the sibling approach files.

- [ ] Commit.
  Message: `feat(approach): add concepts and algorithm subsection`

## Task 3: Update the intro roadmap and align terminology

**Files:**
- Modify: `sections/03-approach-00-intro.tex`

- [ ] Update the closing roadmap so it introduces the concepts subsection first
  (mirroring the thesis: the concepts subsection defines the model and overall
  algorithm, independent of language/toolchain, then the stage subsections describe
  the Java instantiation), keeping the existing per-stage `Section~\ref` sentences.

- [ ] Align regression-framing terminology: in the two running-example sentences,
  change "regressions that affect other inputs in the same partitions" and "encode
  the intended behavior for all inputs in the covered input partitions" to the
  execution-path phrasing used in the thesis intro ("...other inputs that follow the
  same execution paths" / "...for all inputs that follow the covered execution paths
  instead of individual input/output examples").

- [ ] Build twice; verify `grep -c 'undefined' main.log` returns 0 and the roadmap
  references resolve.

- [ ] Commit.
  Message: `revise(approach): point roadmap at concepts subsection; align terminology`

## Task 4: Terminology pass on the stage sections

**Files:**
- Modify: `sections/03-approach-03-spec-extraction.tex`
- Modify: `sections/03-approach-04-generalization.tex`
- Modify: `sections/03-approach-05-reduction.tex`

- [ ] Replace "path-exact specification"/"path-exact" wording with "input/output
  specification" (reserve "path-exact" only where a precision contrast is explicitly
  intended, per the thesis terminology decision). Locate sites:
  `grep -rn 'path-exact' sections/03-approach-*.tex`.

- [ ] Build twice; verify `grep -c 'undefined' main.log` returns 0.

- [ ] Commit.
  Message: `revise(approach): standardize on "input/output specification"`

## Task 5: Final verification

- [ ] Full clean build: `latexmk -C && latexmk -pdf -interaction=nonstopmode -file-line-error main.tex` (twice).
  Expected: exit 0; `grep -c 'undefined' main.log` returns 0; `main.log` shows no new
  overfull warnings introduced by the concepts subsection beyond pre-existing ones.

- [ ] Reviewer-response check: the Approach section now opens with an abstract concepts
  layer (model + Algorithm~\ref{alg:test-generalization} + formal `(pc,out)` spec)
  before the Java stage subsections, and the demarcation paragraph separates
  established techniques from the approach. Confirm by reading the rendered
  Approach section start in `main.pdf`.

- [ ] On completion, run `omp-plans complete 2026-07-16-port-approach-concepts-to-paper`.
