# Claims the paper makes about JARVIS

JARVIS (Peleg, Rasin, Yahav, *"Generating Tests by Example"*, VMCAI 2018; bib key
`peleg_2018_jarvis`) is positioned as the closest existing tool and the only prior work
that automatically generalizes conventional unit tests (CUTs) into property-based tests (PBTs).

Source PDF: `/Users/joaichberger/Downloads/vmcai2018-jarvis-extended.pdf`

The measured comparison and all its evidence live in the code repo:
`test-generalization-dev/docs/plans/2026-06-30-jarvis-comparison.md`.

## Load-bearing claims (what the JARVIS paper must support)

| # | Claim | Cited in | Verified? |
|---|-------|----------|-----------|
| 1 | Generalizes CUTs → PBTs automatically; the only prior work to do so | `sections/01-introduction.tex:63-64` | unverified |
| 2 | Works black-box / from test code only, not program analysis | `sections/01-introduction.tex:65`, `sections/06-related-work.tex:44-45` | unverified |
| 3 | Uses predefined abstraction templates | `sections/01-introduction.tex:66`, `sections/06-related-work.tex:45` | unverified |
| 4 | Templates overapproximate, requiring multiple related tests to constrain the inferred property | `sections/01-introduction.tex:66`, `sections/06-related-work.tex:46` | unverified |
| 5 | Evaluation metric is parameter value coverage (`\cite{sampath_2008_prioritizing}`) | `sections/04-evaluation-04-rq1.tex:9-10` | unverified |
| 6 | Implementation is not publicly available | `sections/04-evaluation-04-rq1.tex:13-14` | unverified |

## Verbatim claim text

**Introduction** (`sections/01-introduction.tex:63-68`):
> To our knowledge, JARVIS is the only prior work that automatically generalizes unit
> tests into property-based tests. However, JARVIS infers properties from input-output
> examples based solely on test code, relying on predefined abstraction templates that
> yield overapproximations. In contrast, our white-box approach leverages both static and
> dynamic program analysis to extract exact specifications for the execution paths
> exercised by the original tests.

**Related Work** (`sections/06-related-work.tex:44-49`):
> JARVIS introduced automated CUT-to-PBT transformation using black-box analysis with
> predefined abstraction templates, which produces overapproximations that require
> multiple related tests to constrain. We instead use white-box symbolic analysis along
> concrete execution paths, extracting path-exact specifications that generalize oracles
> from individual input-output examples.

**Evaluation / RQ1** (`sections/04-evaluation-04-rq1.tex:9-14`):
> We use mutation score rather than parameter value coverage --- the metric employed by
> JARVIS --- because mutation testing is a stronger proxy for fault detection capability.
> Direct comparison with JARVIS is not possible as its implementation is not publicly
> available.
