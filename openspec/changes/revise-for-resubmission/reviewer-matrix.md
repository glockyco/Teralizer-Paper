# Prior-review response matrix

## Source and disposition contract

- Decision: `TOSEM-2025-1249`, 23 June 2026
- Source: `/Users/glockyco/src/github.com/glockyco/phd-thesis/projects/teralizer-paper/tosem-decision.txt`
- Submission treatment: new TOSEM submission after rejection, not an invited revision

Each concern has one response type: `accepted and revised`, `addressed by new evidence`, `partially addressed with a stated boundary`, `rebutted with mechanism and evidence`, or `not implemented, with rationale`. Final references are recorded in the prior-review response at `correspondence/prior-review-response.tex` (private submodule `glockyco/Teralizer-Paper-Correspondence`), which cites the manuscript section and page for every row.

## Concern matrix

| ID | Source | Concern | Response type | Planned response and evidence | Planned manuscript location | Final reference |
|---|---|---|---|---|---|---|
| SAE-01 | Senior Associate Editor | Extend applicability beyond numerical and pure-function-oriented scenarios. | partially addressed with a stated boundary | State the general approach, Java prototype, and evaluated domain separately. Report current type, side-effect, framework, and symbolic-execution limits; do not claim a broader implementation. | Abstract; contributions; approach; validity; conclusion | see response |
| SAE-02 | Senior Associate Editor | Compare with the JARVIS dataset. | addressed by new evidence | Add RQ0 using all twelve JARVIS projects, ten published scenarios, reconstructed revisions, and registered Teralizer results. | Background; evaluation RQ0; validity | see response |
| SAE-03 | Senior Associate Editor | Consider combining the approach with AI/LLM techniques. | partially addressed with a stated boundary | Expand adjacent LLM related work and identify a hybrid as a separate future contribution. Do not imply an implemented or evaluated integration. | Related work; discussion | see response |
| AE-01 | Associate Editor | Practical applicability is limited by symbolic execution and the low real-world success rate. | addressed by new evidence | Replace the 632-project account with RepoReapers version 7: 85 of 584 selected projects complete the pipeline, with project, test, assertion, and attempt denominators and causes. Retain explicit prototype limits. | Abstract; RQ6; discussion; validity; conclusion | see response |
| AE-02 | Associate Editor | The closest prior work needs a stronger comparison. | addressed by new evidence | Add the complete bounded JARVIS comparison and distinguish published JARVIS values from measured Teralizer values. | Background; RQ0; validity | see response |
| AE-03 | Associate Editor | Claims need tighter scope for supported program classes. | accepted and revised | Use developer-anchored, implementation-derived, path-bounded language and state prototype and evaluation restrictions in prominent framing. | Abstract; contributions; approach; validity; conclusion | see response |
| AE-04 | Associate Editor | Mutation-based evaluation lacks stronger independent validation. | not implemented, with rationale | State that no held-out-mutant or real-bug experiment was added. Explain the mutation-proxy construct limit and distinguish mutation-free generation from mutation-based reduction. | Evaluation setup; validity; prior-review response | see response |
| META3-01 | Reviewer 3 via meta-review | Completing 11 of 632 projects (1.7%) is too low for the practical claims. | addressed by new evidence | Replace the obsolete population and result with the complete version 7 lifecycle and 85-of-584 outcome; qualify applicability claims. | Abstract; RQ6; discussion; conclusion | see response |
| META3-02 | Reviewer 3 via meta-review | Use AI/LLM techniques for complex types, assertions, and project structures. | partially addressed with a stated boundary | Discuss task-specific LLM work and a possible hybrid, but retain the unevaluated-integration boundary. | Related work; discussion | see response |
| META3-03 | Reviewer 3 via meta-review | Mutation testing is used for reduction and effectiveness, creating an overfitting risk. | rebutted with mechanism and evidence | Explain that Stages 1--4 do not consume mutants and Stage 5 uses mutation effectiveness only to select a smaller retained suite. Retain the standard mutation-proxy limitation. | Approach reduction; evaluation setup; validity | see response |
| META3-04 | Reviewer 3 via meta-review | Add held-out mutants, different operators, or real bugs. | not implemented, with rationale | Report any preserved pre/post mutation comparison if available; otherwise record the evidence gap. Do not run or imply a new experiment. | Validity; prior-review response | see response |
| META3-05 | Reviewer 3 via meta-review | Assertion-exclusion percentages are inconsistent. | accepted and revised | Replace old assertion populations with version 7 generated evidence and verify that 6,905 included, 166,602 filtered, and 7,041 failed assertions total 180,548. | RQ6 tables and narrative | see response |
| META3-06 | Reviewer 3 via meta-review | “Exact specifications” overstates intended behavior. | accepted and revised | Replace universal exactness language with developer-anchored, implementation-derived, path-bounded claims. | Abstract; approach; discussion; validity; conclusion | see response |
| R1-01 | Referee 1 | Real-world completion is extremely low and restricts practical applicability. | addressed by new evidence | Present version 7 applicability and the complete-population lifecycle while retaining explicit limits and measured failure causes. | RQ6; discussion; validity | see response |
| R1-02 | Referee 1 | SPF has scalability and compatibility limits, especially loops and complex objects. | accepted and revised | State executed resource limits and unsupported symbolic domains; distinguish SPF limits from the general approach. | Background; approach; validity | see response |
| R1-03 | Referee 1 | Constraint-aware generation directly encodes only simple equality and inequality relations. | accepted and revised | Describe supported generators and path filters precisely; treat unsupported constraints and widening refusals as measured outcomes. | Approach; RQ6; validity | see response |
| R1-04 | Referee 1 | Determinism and limited side effects exclude stateful, concurrent, database, and external-dependency scenarios. | partially addressed with a stated boundary | State the current prototype and evaluation restrictions without generalizing them into a universal approach limit. | Approach; evaluation setup; validity | see response |
| R1-05 | Referee 1 | Extend with advanced static or interprocedural analysis, loop invariants, or property synthesis. | not implemented, with rationale | Position these as future work; no unevaluated extension enters the current method or contribution list. | Discussion; related work | see response |
| R2-01 | Referee 2 | Experimental results show limited effectiveness and only marginal gains. | accepted and revised | Report breadth, effectiveness, retained-suite size, runtime, processing efficiency, and applicability as separate results with their denominators. Avoid one aggregate effectiveness claim. | Evaluation RQ0--RQ6; discussion | see response |
| R2-02 | Referee 2 | The implementation largely reconfirms known symbolic-execution limitations. | partially addressed with a stated boundary | Lead with the developer-anchored test-generalization contribution and use the evaluation to delimit the prototype, not to claim symbolic-execution novelty. | Contributions; approach; discussion | see response |
| R2-03 | Referee 2 | Teralizer handles mainly simple, local, numeric cases and misses strings, arrays, and objects. | partially addressed with a stated boundary | Describe actual scalar, string, array, object, and framework support from executable declarations and measured outcomes; avoid the stale numeric-only shorthand where inaccurate. | Approach; evaluation setup; validity | see response |
| R2-04 | Referee 2 | A restricted prototype result could be mis-cited as a general limit of semantics-based generalization. | accepted and revised | Distinguish the general approach, Java prototype, controlled evaluation, inherited JARVIS benchmark, and real-world evaluation everywhere scope is summarized. | Abstract; contributions; discussion; conclusion | see response |
| R2-05 | Referee 2 | The approach lacks an abstract account of concepts and algorithms. | accepted and revised | Add core concepts, formal units and relations, and an end-to-end algorithm before implementation details. | Approach concepts and algorithm | see response |
| R2-06 | Referee 2 | Java-oriented presentation conflicts with the language-independent approach claim. | accepted and revised | Separate language-agnostic concepts from Java/JUnit/jqwik prototype operations and evaluation restrictions. | Contributions; approach; validity | see response |
| R2-07 | Referee 2 major 1 | JARVIS comparison should use its public Apache Commons benchmark despite the unavailable implementation. | addressed by new evidence | Run no JARVIS code; compare published JARVIS scenarios with measured Teralizer results on the inherited twelve-project benchmark and document reconstruction limits. | RQ0; validity | see response |
| R2-08 | Referee 2 major 2 | Define key terms and algorithms formally or drop language independence. | accepted and revised | Define assertion-to-MUT unit, MUT call, specification, partition, oracle, and failure result; add the end-to-end algorithm and retain a bounded language-agnostic claim. | Approach concepts and algorithm | see response |
| R2-09 | Referee 2 major 3 | Supported input and program structures are not scoped in the abstract, contributions, or conclusion. | accepted and revised | Add compact scope qualifiers to all prominent framing after the detailed method and evaluation stabilize. | Abstract; contributions; conclusion | see response |
| R3-01 | Referee 3 | Connect LLM-based property-test generation, specification inference, and oracle work more thoroughly. | accepted and revised | Discuss each technique with the adjacent task it addresses. Describe a Teralizer hybrid only as future work. | Related work; discussion | see response |
| R3-02 | Referee 3 | The manuscript is lengthy and should combine RQs and remove redundancy. | partially addressed with a stated boundary | Remove genuine repetition after scientific content stabilizes. Retain distinct RQs because they measure different contracts and denominators. | Whole manuscript; prior-review response | see response |
| R3-03 | Referee 3 | Reduction and final effectiveness use mutation testing, so the result may depend on the same metric. | rebutted with mechanism and evidence | Explain the stage boundary and reduction invariant; report existing pre/post evidence if preserved and retain the mutation-proxy threat. | Approach; RQ3--RQ4; validity | see response |
| R3-04 | Referee 3 | Generated oracles may reproduce current implementation behavior rather than intended behavior. | accepted and revised | Anchor intent in developer-authored tests and describe oracles as implementation-derived and path-bounded; retain this construct limitation. | Approach; discussion; validity | see response |
| R3-05 | Referee 3 | Add a clearer comparison with JARVIS even if its implementation is unavailable. | addressed by new evidence | Add RQ0 and preserve comparability, reconstruction, and unavailable-implementation limitations beside the result. | RQ0; validity | see response |
| R3-06 | Referee 3 | Add held-out mutants or real bugs such as Defects4J. | not implemented, with rationale | State this validation boundary explicitly. The revision corrects and broadens existing evidence but does not start a new experiment. | Validity; prior-review response | see response |

## Paragraph coverage index

This index maps every substantive concern-bearing paragraph in the decision letter to at least one matrix row. Praise-only text, editorial metadata, disclosure answers, numeric ratings, empty responses, and repeated questionnaire summaries do not require a manuscript change.

| Decision-letter block | Paragraph or item | Matrix rows |
|---|---|---|
| Editor’s meta-review | Senior Associate Editor comment | SAE-01--SAE-03 |
| Editor’s meta-review | Associate Editor comment | AE-01--AE-04 |
| Reviewer 3 quoted by editor | Applicability and 11-of-632 paragraph | META3-01 |
| Reviewer 3 quoted by editor | AI/LLM extension paragraph | META3-02 |
| Reviewer 3 quoted by editor | Mutation-overfitting and independent-validation paragraph | META3-03--META3-04 |
| Reviewer 3 quoted by editor | Assertion percentages and exactness paragraph | META3-05--META3-06 |
| Referee 1 comments | Positive method assessment | Acknowledge; no corrective action |
| Referee 1 comments | Applicability, SPF, constraints, purity, and extension paragraph | R1-01--R1-05 |
| Referee 2 comments | Opening effectiveness paragraph | R2-01 |
| Referee 2 comments | Known technique limitations paragraph | R2-02 |
| Referee 2 comments | Restricted contribution and three-item evidence list | R2-01--R2-03 |
| Referee 2 comments | Weak boundary-study and mis-citation paragraph | R2-04 |
| Referee 2 comments | Approach organization and language-independence paragraph | R2-05--R2-06 |
| Referee 2 major comments | Major items 1--3 | R2-07--R2-09 |
| Referee 2 questionnaire | Missing empirical JARVIS comparison | R2-07 |
| Referee 3 questionnaire | Modest improvement and applicability paragraph | R2-01, R1-01 |
| Referee 3 questionnaire | Missing LLM literature | R3-01 |
| Referee 3 questionnaire | Length and redundancy | R3-02 |
| Referee 3 questionnaire | Stronger independent evaluation | R3-03, R3-06 |
| Referee 3 questionnaire | Mutation-metric reuse | R3-03 |
| Referee 3 questionnaire | Intended-behavior oracle concern | R3-04 |
| Referee 3 questionnaire | JARVIS comparison | R3-05 |
| Referee 3 questionnaire | Held-out mutants or Defects4J | R3-06 |

## Finalization rule

Before submission, replace every `TBD` with the final page, section, figure, table, or listing reference. A row may be closed only when the promised manuscript change exists or the prior-review response states the recorded limitation and rationale.
