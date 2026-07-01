# How JARVIS works (process, assumptions, limitations)

Source: Peleg, Rasin, Yahav, *"Generating Tests by Example"*, VMCAI 2018 (extended version).
PDF: `/Users/joaichberger/Downloads/vmcai2018-jarvis-extended.pdf`. Bib key: `peleg_2018_jarvis`.

This note documents JARVIS *on its own terms* — what it does and what it assumes/cannot do.
No comparison with our paper's claims here (that is a separate pass). Line/section/figure
references point into the JARVIS PDF.

The measured Teralizer-vs-JARVIS comparison (Table-2 head-to-head, budget elasticity, breadth,
soundness) lives in the code repo:
`test-generalization-dev/docs/plans/2026-06-30-jarvis-comparison.md`.

> Caveat: the PDF is two-column; text extraction interleaved some paragraphs out of order.
> The reconstruction below is cross-checked against the formal definitions (Def. 1–5),
> Figs. 1–5, and the section headers, which extracted cleanly.

---

## 1. Identity and goal

- **JARVIS** = *Junit Abstracted for Robust Validation In Scalacheck* (line 51).
- **Goal**: take an *existing* JUnit suite and synthesize property-based tests (PBTs) from
  **repetitive** unit tests — tests that run the same code with different constant values
  (lines 13, 25, 77).
- **Central idea**: over-approximate the concrete constants of structurally-similar tests with
  an *abstraction* from an abstract domain, then emit a value generator that samples that
  abstraction (lines 11, 29).
- A synthesized PBT = parametric test body + reused oracle (assertion) + value generator
  (lines 25, 207–209).

## 2. Input / output / toolchain

- **Input**: JUnit test suites written in **Java** (line 513). The unit-under-test (UUT) source
  is *not* required — see black-box assumption below.
- **Output**: **ScalaCheck** PBTs in **Scala** (lines 511–513). Scala↔Java interop lets the
  generated property mimic the original Java trace.
- **Toolchain**: Polyglot compiler [39] + ScalaGen [6] translate Java traces → Scala;
  template instantiation is aided by the **Z3** SMT solver [17] (lines 513). Safe-Generalization
  in interval domains can use Hydra [38] (line 377). Coverage measured with JaCoCo [1] (line 610).

## 3. Pipeline

### Step 1 — Extract test traces
A **test trace** is a sequence of (not necessarily adjacent) statements that can be executed
sequentially and **ends with exactly one tested assertion** (line 227). Each `assert*` call
yields its own trace; multi-assertion tests are sliced into one-assertion traces (lines 241,
642–694 Fig. 3 example).

### Step 2 — Parameterize (trace → parameterized test)
Constants are replaced by uninterpreted **parameters of the same type as the constant**
(lines 103, 245). Rules:
- If the **same constant appears more than once**, all occurrences become the **same parameter**
  → an *equality constraint* is preserved (line 245, 99–103).
- Specific assertions (`assertTrue`/`assertFalse`) collapse to a generic `assert`; the expected
  outcome is stripped into a separate label `res ∈ {+, −}` (lines 245, 249).
- Example: `assertTrue(Precision.equals(153.0,153.0,.0625))` →
  `pt1 = assert(Precision.equals(x,x,y))`, `type(x)=type(y)=double`,
  mapping `{x↦153.0, y↦.0625, res↦+}` (line 103).
- **Parameter mapping** `f` (Def. 1, line 253): maps each parameter to a constant of the same
  type, plus `res → {+,−}`; reproduces the original concrete trace. A suite = set of
  parameterized tests, each carrying a set of mappings `F = {f1..fn}` (line 257).

### Step 3 — Group into scenarios
A **scenario** (Def. 2, line 281) is the set of parameterized tests executing the **same
statement sequence**, differing only by parameters. The scenario "code" is that shared sequence
with parameter info discarded. **Method-overloading information is kept** (not discarded), so
overloads stay in separate scenarios (line 285).

### Step 4 — Build the generality DAG (`⊑`)
Within a scenario, define subsumption on the **sequence of parameter uses** `params(pt)`
(Def. 3, line 291). `pt1 ⊑ pt2` ("pt1 is a subtest of pt2") iff for all positions i,j
(Def. 4, line 295):
1. **Type**: `type(x1_i) ⊑ type(x2_i)` — standard subtyping / implicit conversion
   (`int ⊑ double`, `String ⊑ Object`, `ArrayList ⊑ List`) (lines 129, 295).
2. **Equality**: every equality constraint in `pt2` (a parameter repeated across positions) is
   also present in `pt1` — i.e. going *up* the order relaxes constraints (lines 129, 297).

This yields a **DAG**, not a tree: two tests can be incomparable, and their least upper bound
may not exist among real tests (Example 1, lines 317–321: `ArrayList ⊑ List` but `Set` is
incomparable to `List`).

### Step 5 — Pick abstraction candidates (unification rule)
**Abstraction candidates** (Def. 5, line 329) = the **roots/maxima** of the `⊑` DAG, each bundled
with the parameter mappings of every test reachable beneath it. Critical rule: JARVIS only
abstracts over parameterized tests that **exist "in the wild"** — it will **not invent a
synthetic least-upper-bound** (e.g. a `Collection<String>` test that never appears) just to
merge `List` and `Set` data (lines 321–333). Rationale: (a) it would force generating values for
a type with no concrete samples, and (b) it would merge genuinely different behaviors
(e.g. `Set.add` vs `List.add`) (line 325).
Net effect: maximal *safe* reuse of examples, no over-unification.

### Step 6 — Abstract the data via Safe Generalization
For each candidate, split its mappings by `res` into positives `C+` and negatives `C−`
(lines 337, 347–369). Use **Safe Generalization** [44] (the authors' own D3 / data-driven
disjunctive abstraction, VMCAI 2016) to find:
- `A+` covering **all** positives while excluding **all** negatives, and
- `A−` covering all negatives while excluding all positives (lines 141, 363).

Safe Generalization guarantees (line 359): (1) Abstraction — `A'` ⊇ everything `A` abstracts;
(2) Separation — no counterexample is abstracted by `A'`; (3) Precision — generalization derives
only from elements of `A`.
**Cross-candidate counterexamples**: when a scenario has several candidates, each positive set
must be separated from **all** negative points in the scenario (and vice versa); `C+cex` pulls in
negatives from sibling candidates to tighten separation (lines 143, 365–373).
Exact SG is expensive — doubly-exponential in some domains (line 389) — so JARVIS uses a
**relaxed SG relation** `SG(C, Ccex)`: rather than synthesizing over all abstractions, it
**tests a fixed set of given abstractions** and relaxes the precision requirement so small
example sets still admit a result (lines 389–391).

### Step 7 — Abstraction templates (the library)
JARVIS carries a **library of abstraction templates**, e.g. `|x−y| ≤ z`, `x ∈ [a,b]`,
`|a*x−y| ≤ b` (lines 393, 397). For each template:
- Instantiate it; numeric parameters (a,b) are chosen from the samples, aided by Z3 (line 397).
- Templates are instantiated **in pairs** (one for `A+`, one for `A−`).
- Selection uses a **predefined ranking** — unlike FlashFill [51], which *learns* its ranking,
  JARVIS's ranking is **fixed/hand-set** and applies to all instantiations that hold for all
  samples; the highest-ranked valid `(A+, A−)` pair wins (lines 393–397).
- The library and ranking are **manually extensible** per project/domain (line 399).
- Abstractions are deliberately **conservative / over-approximating** (line 401): they guarantee
  the original cases are included, but may also admit inputs that *fail* the PBT (false alarms).

### Step 8 — Sample the abstraction (generate generators)
Treat the developer's chosen constants as a **weighted sample** of the true precondition region;
preserve them (line 421). For each `pt`, emit a sampling component over each abstraction it
contributed to, **AND-ing the pt's own constraints** into the sampled region — e.g. sampling
`|x−y| ≤ z ∧ x = y` so the equality special-case keeps non-negligible probability (lines
427–431). Output is ScalaCheck `Gen` code (`Gen.choose`, `Gen.oneOf`, `Gen.posNum`,
`Arbitrary.arbitrary[Double].map(Math.abs)`, `.suchThat(...)`; Figs. 2, 4, 5). Two properties per
parameterized test: a **positive** one (assertion expected to hold) and a **negative** one
(negated assertion), differing only in the generator (lines 363, 179, Fig. 2).
**Sampling guarantee** (Claim, lines 435, 507): requires a scenario with **|T| ≥ 2** test traces;
then each trace is used in an abstraction and gets a generator.

## 4. Evaluation (for context)

- Hierarchy/unification study over **12 Apache Commons** projects (Table 1, lines 437–505).
- Coverage metrics: **instruction coverage (IC)** + **parameter value coverage (PVC)** [48],
  chosen specifically because they permit **black-box** synthesis — "the library's code need not
  even compile, as long as the tests do" (lines 535, 565).
- Results: IC preserved (≥ original in every case but one); PVC up **~26× on average**, up to two
  orders of magnitude (Table 2, line 612). Two PVC regressions explained by 100-iteration
  ScalaCheck cap vs. large in-test loops (`isPrintable`, `toIntExact`, line 628).
- **Intended use vs. what the case study shows (important).** JARVIS claims **two** uses
  (line 181): (a) "find bugs that are simply **not tested for**" in the current version, and
  (b) "stave off bugs that will be added in **future changes**" (regression). The over-approximation
  is on the **input region** while the oracle is reused faithfully; its guarantee (line 401) is only
  that the **original passing cases are included** — it does **not** promise everything the generator
  samples passes. JARVIS's own **§5.1 "Handling Impreciseness"** explicitly **expects** raw output to
  sometimes fail on the source version: conservative abstractions (too-coarse — single interval vs.
  needed disjunction — or built from too-few examples) "also represent data points that will fail the
  PBT," requiring **manual intervention** (finer abstraction / more examples / hand-editing)
  (lines 401–407). So a same-version failure of *raw* output is **expected, not anomalous** — it is a
  **candidate requiring triage**, resolving to either (i) imprecision to refine away or (ii) a genuine
  latent bug. The artifact intended for **regression** use is the **accepted/refined PBT** *after*
  triage, not the raw output.
- **Bug findings (Section 9)** are this triage path landing on outcome (ii): same-version
  over-approximation failures, validated case-by-case — **MATH-1256 failed automatically**, **MATH-785
  needed manual generator refinement**. This is **not** the regression mechanism (that
  is what the accepted PBT provides afterward), and **not** a version-to-version comparison (JARVIS
  never diffs versions). Both bugs were found by running JARVIS on a **single old version** where the
  bug was present-but-uncaught ("the version before the bug was fixed", line 638), and the generated
  PBT fails on **that same version**:
  - **MATH-1256** (Interval bounds, `IntervalTest` from **release 3.5**, fixed in 3.6): the over-broad
    generator samples intervals with **lower > upper** (a region the original 2 valid-interval tests
    never covered); the faithful oracle then fails. This turned out to be a **real latent invariant
    violation** (the constructor never validates lower ≤ upper → negative size), found **automatically**
    — bug occupies ~50% of the space, "failed, on average, on the second value generated"
    (lines 624, 712, 716, 734).
  - **MATH-785** (ContinuedFraction underflow, `FDistributionTest` from **3.0**): the over-approximation
    `|0·int1 − double1| ≤ 0.999` was too coarse, so "values causing a **false positive** are far more
    likely" (line 744); the automatic run falsified on `(2147483647, −0.56…)` — a false positive
    (line 750). Only after **manually** bounding `int1` to lower positive values and `double1` near 1
    did the **real** `NoBracketingException` appear, on the same 3.0 version (lines 742–754).
  - Separately, a **copy-paste bug in the *test code*** of Commons-Lang `isPrintable` was noticed via an
    abstraction/coverage inconsistency and fixed (PR #230, line 630) — a *test* bug, not a production
    regression.
- **Net:** JARVIS's bug-finding evidence = manually triaged over-approximation failures on the same
  version, not a sound regression-detection result. The forward-looking regression use (b) is a
  motivating claim, not what §9 demonstrates.

## 5. Assumptions

- **A1 — Repetition exists.** The whole approach hinges on suites containing structurally
  identical tests differing only in constants; a scenario needs **≥2 traces** to generalize
  (lines 77, 435). Singleton scenarios "provide no generalization" (line 261).
- **A2 — Black-box / test-code-only.** JARVIS reads only the **test code**, never the UUT
  internals; it has **no access to program branches, predicates, or paths** (lines 543, 565).
  The input region is *guessed from constant examples*, not derived from program semantics.
- **A3 — Original assertions are ground truth.** The oracle is reused verbatim and `res` labels
  come from `assertTrue`/`assertFalse`; correctness of the original test is assumed (line 814).
- **A4 — Equality intent is syntactic.** "Same constant at two positions ⇒ intended equality
  constraint" (lines 99, 245). Purely lexical — no semantic check that the equality is meaningful.
- **A5 — Constants carry the generalization; structure is fixed.** Only constants become
  parameters; call structure / object construction stays fixed. JARVIS generalizes **values, not
  structure** (line 103, 245).
- **A6 — Java→Scala/ScalaCheck translatability.** Every trace must translate cleanly through
  Polyglot + ScalaGen and run under ScalaCheck (line 513).
- **A7 — Re-execution with fresh values is meaningful.** Implicitly assumes traces are
  deterministic enough that resampling explores comparable behavior; stateful / environment-
  dependent tests are not addressed. *(inferred — not stated)*

## 6. Limitations

### Explicitly acknowledged in the paper
- **L1 — Template-bounded expressiveness.** The inferred property must be expressible as one of
  the **predefined templates**. The best available template can be **too conservative**, admitting
  inputs that fail the PBT (false positives) (lines 401–403). Concrete failure: a single interval
  where the data needs a **disjunctive** abstraction (a set of intervals) (line 403).
- **L2 — Predefined, manual ranking.** Ranking of templates is hand-set (not learned); extending
  the library or retuning the ranking for a new domain is **manual effort** (lines 395, 399).
- **L3 — Few-examples imprecision.** Generalizing from very few samples (e.g. 2) leaves large room
  for error; the abstraction may be too coarse → false positives, or under-constrained. Remedy is
  **manual**: provide a finer abstraction, more examples, or hand-edit the test (lines 405–407).
- **L4 — Human-in-the-loop for hard cases.** The MATH-785 bug was found **only after manually
  rewriting the generator** (bounding `int1`, tightening `double1` near 1) (lines 742–800). So
  output is not reliably "drop-in" on imprecise scenarios.
- **L5 — Needs negative examples to constrain.** Tight separation depends on counterexamples;
  with only positives (and few of them) the positive abstraction balloons (line 139).
- **L6 — `Double.NaN` (and special float values) not abstracted/sampled.** `testMinMaxDouble`
  *lost* instruction coverage because JARVIS "does not abstract or create generators that can
  sample `Double.NaN`," which exercises a separate code path (line 632). A concrete **type-support
  gap**.
- **L7 — Iteration cap vs. in-test loops.** ScalaCheck's default 100 runs can *under*-cover a unit
  test whose body loops over many values (lines 628).

### Inferred / implicit (grounded in the paper, not stated as limitations)
- **L8 — Numeric/char-primitive bias (type support).** [INFERENCE] Every template shown is
  **arithmetic/interval** (`|x−y|≤z`, `x∈[a,b]`, `|a*x−y|≤b`); the SG machinery cited is for
  **interval** domains (Hydra); and **every** evaluated parameter space in Table 2 is `char`,
  `int`, or `double`/`double2`/`double3` (lines 393, 377, 571–608). No template family, generator,
  or evaluated case covers **strings (with structure), collections' contents, or user-defined
  object parameters**. Strong implication: JARVIS is effectively confined to **numeric (+ char)
  primitive parameters** where linear-arithmetic / interval templates apply. (The `List/Set`
  example concerns the *type hierarchy* of the receiver, not generating object *values*.)
- **L9 — Generator must exist for the parameter type.** [INFERENCE] Sampling relies on ScalaCheck
  `Arbitrary.arbitrary[T]` / `Gen.choose[T]` over an abstract region; for arbitrary user-defined
  `T` there is no shown mechanism to build such a region or generator. Reinforces L8.
- **L10 — One assertion per trace; no multi-assertion / stateful-sequence properties.**
  [INFERENCE] A trace ends in a single assertion (line 227); interrelated assertions are split.
  Properties spanning multiple coupled assertions or long stateful sequences are not generalized
  as a unit.
- **L11 — No cross-incomparable-type generalization.** By the unification rule (Step 5) tests over
  incomparable types (e.g. `List` vs `Set`) are never abstracted together, even when a meaningful
  common property exists — conservative, but misses generalizations whose LUB is absent from the
  suite (lines 321–333).
- **L12 — Spurious or missed equality constraints.** [INFERENCE] Because equality detection is
  lexical (A4), two coincidentally-equal constants force a (possibly unintended) equality
  sub-test, while an intended equality expressed via different literals is missed.
- **L13 — Scalability of exact SG.** Exact Safe Generalization is doubly-exponential in some
  domains; JARVIS sidesteps this only by **testing a fixed template set** rather than truly
  synthesizing abstractions — which is the root cause of L1 (lines 389–391).
- **L14 — Bug-finding rests on triage, not a sound automatic regression mechanism.** [INFERENCE + §4]
  JARVIS's demonstrated discoveries (§9) come from **triaging same-version over-approximation
  failures** — which §5.1 itself frames as *imprecision* — **not** from the cross-version regression
  use it is pitched on (line 181b). Deciding real-bug vs. false-positive is a **human** step
  (MATH-1256 failed automatically but still needed validation; MATH-785 was a false positive until
  manually refined). So the bug-finding evidence is weaker and more manual than a sound
  regression-detection result. Consolidates the evaluation-strength angle of L1/L3/L4; full argument
  in §4.
