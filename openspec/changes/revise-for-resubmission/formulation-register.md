# Reference formulation register

`USE` retains the scientific distinction with only local grammatical changes. `ADAPT` changes wording, notation, or emphasis for the destination while preserving the distinction. `OMIT` excludes a formulation that is optional, misleading, unsupported, or superseded. Final source locations are filled during manuscript and correspondence revisions.

| ID | Design formulation | Destination | Disposition | Required treatment | Final source location |
|---|---|---|---|---|---|
| MUT-01 | Mutation analysis does not guide specification extraction or generalized-test creation; Stage 5 only reduces the candidate suite. | Manuscript approach and validity | USE | Preserve the stage boundary, retained-suite benefit, and processing-cost distinction. | TBD |
| MUT-02 | Mutants do not influence created tests; held-out mutants would test reduction transfer, not creation feedback. | Prior-review response | USE | Lead with the mechanism before acknowledging the construct-validity limit. | TBD |
| MUT-03 | Teralizer could omit Stage 5 and retain every generated PBT. | Manuscript discussion | ADAPT | Use only if the reduction trade-off needs clarification; do not present it as an evaluated variant. | TBD |
| MUT-04 | Formal invariant `K_M(T ∪ G') = K_M(T ∪ G)`. | Manuscript reduction section | USE | Define `T`, `G`, `G'`, and `M`; verify the rule against the implementation. | TBD |
| MUT-05 | Mutation score is an imperfect proxy for real-fault detection. | Manuscript validity and prior-review response | USE | State operator scope; do not imply independent real-bug validation. | TBD |
| ORACLE-01 | Teralizer constructs developer-anchored, implementation-derived oracles. | Manuscript approach and contributions | USE | Retain both developer evidence and implementation derivation. | TBD |
| ORACLE-02 | The oracle is path-exact under model, purity, and widening assumptions, not proof of an unstated external specification. | Manuscript approach and validity | USE | Keep assumptions beside exactness; avoid universal “exact specification.” | TBD |
| ORACLE-03 | Developer assertions provide seed oracle evidence; implementation semantics generalize beyond seeds. | Manuscript discussion and prior-review response | ADAPT | Use to distinguish Teralizer from implementation-only oracle inference. | TBD |
| ORACLE-04 | “The result does not establish intended behavior.” | All destinations | OMIT | This standalone sentence erases developer-written oracle evidence; use ORACLE-01--03 instead. | N/A |
| SCOPE-01 | The approach is not inherently Java-specific; the prototype inherits Java, framework, type, purity, and project restrictions. | Manuscript contributions, approach, validity | USE | Separate approach and prototype without claiming unsupported portability. | TBD |
| SCOPE-02 | RQ1--RQ5 reuse one controlled EqBench and Apache Commons population. | Evaluation framework and RQ5 | USE | State that RQ5 analyzes failures within the shared population. | TBD |
| SCOPE-03 | RQ6 follows selected real-world projects through exclusions, failures, and refusals. | Evaluation framework, RQ6, validity | USE | Preserve measured unsuccessful and unsupported outcomes. | TBD |
| SCOPE-04 | Compact effectiveness, efficiency, and applicability evaluation sentence. | Abstract | ADAPT | Add only after all RQ claims stabilize; use compact controlled/real-world distinction. | TBD |
| SCOPE-05 | Contributions split into approach, Java prototype, and empirical evaluation. | Introduction and conclusion | USE | Keep prototype separate from the general method. | TBD |
| SCOPE-06 | Across 584 selected RepoReapers projects, the prototype completes all stages for 85 projects. | Conclusion | ADAPT | Correct “selected” to the final population terminology required by provenance; retain unsupported and failed outcomes in scope. | TBD |
| SCOPE-07 | “We evaluate the approach on the pure-method and data-type fragment supported by the current analyses.” | Abstract and complete-evaluation summaries | OMIT | This falsely narrows RQ6 and collapses controlled and real-world designs. | N/A |
| JARVIS-01 | Teralizer produces tests for 9 projects and 337 MUTs versus published JARVIS results for 2 projects and 9 MUTs. | RQ0 result, abstract, conclusion | USE | Attribute JARVIS values as published and Teralizer values as measured. | TBD |
| JARVIS-02 | Results show broader measured applicability but are not an executable head-to-head reproduction. | RQ0 interpretation and validity | USE | Retain unavailable-implementation and revision-reconstruction limits beside the result. | TBD |
| JARVIS-03 | PVC outcomes are four higher, three lower, and three missing; PVC measures diversity, not fault effectiveness. | RQ0 result and validity | USE | Verify scenario categories and avoid a JARVIS effectiveness claim. | TBD |
| JARVIS-04 | “Statistically significantly better.” | All destinations | OMIT | No registered statistical test supports this phrase. | N/A |
| JARVIS-05 | Universal state-of-the-art ranking. | All destinations | OMIT | The comparison is bounded to the shared benchmark and published scenarios. | N/A |
| RQ6-01 | Historical 11-of-632 versus current 85-of-584 account. | Prior-review response | ADAPT | Use to explain revision scope, not as a paired empirical improvement. | TBD |
| RQ6-02 | Different selections and pipeline semantics prevent a paired before-and-after comparison. | Manuscript validity and prior-review response | USE | Keep this limitation with any historical comparison. | TBD |
| RQ6-03 | Balanced synthesis combines 9-of-12 JARVIS and 85-of-584 RepoReapers results while retaining practical limits. | Discussion and conclusion | ADAPT | Ensure each population and comparison limit remains explicit. | TBD |
| RQ6-04 | “Applicability improved from 1.7% to 14.6% on the same corpus.” | All destinations | OMIT | The populations and pipeline semantics differ. | N/A |
| LLM-01 | LLM work addresses adjacent specification, generation, and oracle tasks; Teralizer supplies path evidence and refusal behavior. | Related work | ADAPT | Discuss each cited system in its actual task category; do not invent an LLM test-generalization class. | `sections/06-related-work.tex` (Specification Inference; Test Generation and Developer Perspective) |
| LLM-02 | A hybrid could propose assertions, abstractions, or models and validate checkable parts with tests and path evidence. | Discussion future work | USE | State that the integration is unimplemented and unvalidated. | TBD |
| LENGTH-01 | Condense genuine redundancy while retaining distinct research questions. | Prior-review response | USE | Explain that the RQs use different measures, designs, and populations. | TBD |
| LENGTH-02 | Promise wholesale condensation or combined RQs. | Cover letter and prior-review response | OMIT | The revised structure retains distinct RQs where scientifically necessary. | N/A |
| VALID-01 | No held-out-mutant or real-bug experiment was added; clarify stage boundary and mutation-proxy limitation. | Prior-review response and validity | USE | Do not describe preserved mutation score or PVC as independent validation. | TBD |
| VALID-02 | Preserved mutation-score or PVC evidence constitutes independent validation. | All destinations | OMIT | Neither evidence source is independent real-bug or held-out-mutant validation. | N/A |

## Reconciliation rule

Every `USE` or `ADAPT` row must receive a final manuscript or prior-review-response location. Any material wording change must preserve the “Required treatment” column and be recorded in `backport-manifest.md`. `OMIT` rows remain explicit guards against recurring reviewer-sensitive misstatements.
