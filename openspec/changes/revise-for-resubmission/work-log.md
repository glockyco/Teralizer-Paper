# Revision work log

## Workspace baseline

- Manuscript repository: `/Users/glockyco/src/github.com/glockyco/Teralizer-Paper`
- GitHub remote: `git@github.com:glockyco/Teralizer-Paper.git`
- GitLab remote: `https://git-isys.aau.at/serg/johann-glock/test-generalization-paper.git`
- Initial branch: `main`
- Initial worktree: clean
- Source and evidence repository: `/Users/glockyco/src/github.com/glockyco/test-generalization`
- Read-only thesis paper submodule: `/Users/glockyco/src/github.com/glockyco/phd-thesis/projects/teralizer-paper`

The GitLab remote is registered as `gitlab`. Its first read-only fetch could not authenticate because terminal credential prompts are disabled. Do not claim that both remotes contain the same commit until an authenticated fetch verifies them. Do not push either remote without explicit operator authorization.

## Repository commands

Both CI workflows build `main.tex` with this effective command:

```bash
latexmk -pdf -interaction=nonstopmode -file-line-error main.tex
```

The `latexmk` build owns bibliography processing for `main.bib` and `main.bbl`. Use these focused local checks:

```bash
chktex main.tex
texcount -1 main.tex
latexmk -c
```

After each coherent revision, build the manuscript and inspect `main.pdf` as a rendered document. Check references, tables, figures, clipping, and page layout. Do not commit routine build artifacts. The paper guidance permits `main.pdf` only for releases.

## OpenSpec execution ownership

The paper-local change `revise-for-resubmission` owns manuscript execution and task progress. The source change in `glockyco/Teralizer` remains a planning and evidence record. Do not mark later source tasks complete for work performed here.

## Verified baseline

- Resubmission branch: `revise-for-resubmission`
- Branch point: `b72728a0571d182f4673f957033c330c77775b83`
- Rejected manuscript revision: `68b491e3708eb2d50a30fabbd75cf13d61a5e187`
- Ancestry check: the rejected manuscript revision is an ancestor of the branch point
- GitHub workflow command: successful
- GitLab workflow command: successful; the identical command found `main.pdf` up to date
- Baseline PDF SHA-256: `e4752f9a0c5b68e8ca7fb10a3e12d3f4be79fe82031bd0457877d533bacae740`
- Baseline page count: 49

The source and evidence repository and its registered submodules were clean after the execution handoff commit. The thesis worktree retained its pre-existing untracked `projects/teralizer-paper/tosem-decision.txt`; all other recursively registered thesis submodules were clean. No manuscript source had been edited when these states were checked.

## Remote authorization gate

No remote will be pushed, and no GitHub or GitLab CI result will be claimed, without explicit operator authorization. Local execution of the CI commands is not remote CI evidence.

## Generated evidence publication

- Teralizer publication command: `PAPER_OUT=/Users/glockyco/src/github.com/glockyco/Teralizer-Paper scripts/publish-analysis.sh`
- Published set: 34 LaTeX artifacts, 33 CSV exports, and 5 figure PDFs declared in `publish.toml`
- Existing manuscript tables migrated to 14 paper-owned wrappers; captions, labels, placement, and sizing remain in those wrappers
- Generated table bodies remain under `tables/generated/`; unpublished evidence tables have no speculative manuscript wrappers
- Aggregate evidence macros are imported unchanged from `tables/generated/macros.tex`
- Verification: all 72 declared destinations exist; 132 row anchors are unique; the 49-page ACM manuscript builds; representative table pages were inspected in the PDF
- Teralizer source worktree remained clean after publication. The thesis worktree retained its pre-existing ` M projects/teralizer-paper` state and no thesis file was edited

## Version 7 RQ6 backport

- `sections/04-evaluation-09-rq6.tex` now contains the complete version 7 lifecycle and result account. Paper-only changes are limited to labels, references, assembly, and the registered selection provenance: 1,161 initially selected projects, 550 initial-gate exclusions, 27 projects without executed tests, and 584 eligible projects.
- The three RQ6 tables use the directly published fragments under `tables/generated/`. Their values and row anchors match the thesis tables; only paper-owned wrapper width and presentation differ.
- The complete-paper stale-claim audit found the rejected 632-project and 1.7\% result in `main.tex`, `sections/01-introduction.tex`, `sections/05-discussion.tex`, and `sections/07-conclusions.tex`. These are planned framing and synthesis destinations in tasks 7 and 8; do not remove their surrounding passages before those tasks port or adapt the complete sections.
- No RQ6 count, denominator, funnel, exclusion, widening, or provenance discrepancy required a deferred candidate.

## Discussion and validity backport

- `sections/05-discussion.tex` now follows the thesis discussion and validity account, including the RQ0 comparison, version 7 RQ6 synthesis, widening interpretation, three-part failure taxonomy, future directions, and mutation-testing validity discussion.
- Standalone adaptations are limited to paper labels and references, registered evidence macros, retained study context, and the 584-project eligibility terminology established by the published RQ6 provenance.
- The thesis cited two nonexistent bibliography keys for equivalent and subsumed mutants. The paper preserves the thesis claim and cites the registered mutation-testing survey, which covers equivalent-mutant detection and mutant-reduction strategies; the invalid keys were not imported.
- Verification: `latexmk -pdf -interaction=nonstopmode -file-line-error main.tex` and `chktex -q sections/05-discussion.tex` pass; the discussion opening and threats-to-validity pages were inspected in the rendered PDF; no overfull box was reported.

## Related-work reconciliation

- The paper retains its detailed specification-inference, LLM, test-generation, oracle-inference, and developer-study citations because the thesis delegates those surveys to other chapters. This is standalone context, not a competing scientific account.
- The thesis JARVIS comparison now points to RQ0, and its thesis-specific statement about unevaluated developer acceptance is adapted to the paper's evaluation while preserving the limitation.
- Complete source comparison found no other scientific departure or nonessential proposal requiring a deferred candidate. Label comments and non-breaking reference spaces were adapted for the ACM source.
- Verification: the complete manuscript builds, `chktex -q sections/06-related-work.tex` passes, and both related-work pages were inspected in the rendered PDF.

## Operator-approved discussion correction

- DC-004 records the duplicated `both` in the thesis discussion source. The operator approved immediate correction on 2026-08-31; `sections/05-discussion.tex` removes only the second `both`, preserving the comparison and evidence.

## Standalone framing and publication assets

- The paper retains its fuller standalone background unchanged. `sections/01-introduction.tex` now integrates the thesis scientific additions, the seven-question evaluation, the JARVIS and RepoReapers results, and a standalone contribution list and roadmap without thesis chapter framing.
- The 218-word abstract in `main.tex` and the paper-owned synthesis in `sections/07-conclusions.tex` now cover the complete RQ0--RQ6 scope. The thesis-only bridge remains omitted.
- `main.bib` and the abstract use the registered 2026 replication package and DOI `10.5281/zenodo.18242626`; the complete build reports no unresolved citations or references.
- Publication verification reran `../test-generalization/scripts/publish-analysis.sh` with this repository as `PAPER_OUT`. All 78 declared CSV, LaTeX, macro, and figure destinations were republished, and the worktree retained no generated-artifact changes, confirming byte-equivalent registered outputs.
- The complete 57-page manuscript was inspected after the framing changes. Every included table is upright and readable; no clipping, missing asset, incorrect float orientation, or factual caption conflict was found. The paper-owned listings, captions, labels, variant macros, and RQ0--RQ6 identifiers remain consistent with the manuscript assembly.
- Verification: `latexmk -pdf -interaction=nonstopmode -file-line-error main.tex` succeeds; `chktex` reports only the manuscript's recorded pre-existing warnings, including ORCID dashes, labels, and code-like text in accessibility descriptions.

## First-pass freeze

- Commit `9bef962` freezes the complete faithful backport. Every manifest row now records a final manuscript or artifact location, and the deferred register contains all four departures identified by the source, implementation, evidence, and rendered-manuscript audits.
- DC-004 is already operator-approved and applied. DC-001 through DC-003 remain undecided; no manuscript change may apply them until the operator records an explicit decision.

## Deferred-candidate verification (2026-09-04)

- Each open candidate was checked against the implementation, git history, and the stored `project.configuration` of every run database (`postgres_dev`, `postgres_jarvis_census`, `postgres_jarvis_scoreboard`, `postgres_reporeapers_rq6_v7`).
- DC-001: the controlled-study reduction uses `ORIGINAL` as its baseline; a direct query reproduces the published `tab-tests-per-project` "Added" values. The manuscript rule already matches the implementation. Recommendation: reject.
- DC-002: all reported controlled, census, and v7 runs recorded a 10-second JPF budget; the scoreboard run recorded 30 seconds. The manuscript says 60 seconds in Section 3 and 10 seconds "in every processing run" in Section 4. Recommendation: approve with the corrected values.
- DC-003: unambiguous listing defect. Recommendation: approve.
- DC-005 (new): `\TzRealworldGeneralizationsFinalUsable` (1,435) counts generalized tests whose Stage-5 PIT run completed, not tests retained by the reduction criterion. The criterion retains 19 tests in 13 projects. The manuscript presents 1,435 as the reduced-suite content in five locations. Recommendation: approve; requires a registered analysis metric before any manuscript edit.
- No manuscript file changed during this verification.

## Post-port improvement review (2026-09-04)

- Operator decisions: DC-001 rejected; DC-002 approved in simplified form (10 s in Section 3 prose and listing only); DC-003 approved; DC-005 approved as wording only.
- The scoreboard run's 30 s JPF budget never bound: all 18 `EXECUTE_JPF` tasks succeeded, maximum runtime 0.46 s. Section 4 was left unchanged.
- Applied to the paper: `sections/03-approach-03-spec-extraction.tex`, `sections/03-approach-04-generalization.tex`, `sections/04-evaluation-09-rq6.tex`, `sections/05-discussion.tex`, `sections/01-introduction.tex`, `sections/07-conclusions.tex`, and the abstract in `main.tex`. The 1,435 / 85 applicability figures are unchanged; only the "reduction leaves" and "reduced suites contain" framing was replaced.
- Applied the same corrections to the thesis chapter (`chapters/05-teralizer/03-approach.tex`, `04-evaluation-rq6.tex`, `05-discussion.tex`, `listings/lst-jpf-config.tex`, `listings/lst-generalized-test.tex`).
- Verification: both documents build without unresolved references; `chktex` counts unchanged from baseline; the thesis style check reports 0 blocking; all affected pages were inspected in both rendered PDFs with no layout defects.

## Framing revision (DC-006, 2026-09-06)

- Operator-directed framing pass. Seven drafts were reviewed read-only by four persona subagents with unbiased briefs. All four independently flagged the same defects, and the drafts were corrected before application. Edit 6 (related work) was withdrawn because the existing sentence was already correct.
- Applied to the paper: background two-decision paragraph, 3.1 selection sentence, introduction complementarity, 5.1 bound by construction, 5.3 third deployment strategy, 5.4 oracle account linked to the regression purpose, conclusion, and four consistency fixes. Abstract unchanged except "path-specific" to "path-exact".
- Verification: complete build with no unresolved references, `chktex` counts identical to baseline for every touched section, all eight affected pages inspected in the rendered PDF with no layout defect.

## Submission correspondence

- Submission letters must not enter the public paper repository. Created the private repository `glockyco/Teralizer-Paper-Correspondence` and mounted it as the submodule `correspondence/`.
- `cover-letter.tex` identifies TOSEM-2025-1249 as the rejected predecessor and summarizes six substantive changes without implying an invited revision.
- `prior-review-response.tex` answers every row of the reviewer matrix with one of five response types and cites final section and page numbers. Every manuscript claim cited in the response was verified against the section source before the letters were built.
- Verification: both letters build with `latexmk`, contain no semicolons, and were inspected page by page. One orphaned heading was fixed with `needspace`.

## GitLab retirement (2026-10-05)

- Access to the AAU GitLab instance `git-isys.aau.at` has ended. The `gitlab` remote was removed from the macbook-pro and korolev clones, and `.gitlab-ci.yml` was deleted. GitHub Actions is the only CI.
- The proposal, design, setup and remote-readiness scenarios, and open tasks 11.2, 11.9, and 11.10 now name only the GitHub remote. Earlier entries that mention GitLab describe the state at that time.
- `revise-for-resubmission` is shared between the macbook-pro and korolev clones over SSH and has not been pushed to GitHub, which holds only `main`.
- `AGENTS.md` and `.omp/rules/bib.md` now cite the installed `research-evidence` and `commit-policy` skills instead of the retired literature, PDF, BibTeX, and commit skills.

## Thesis RQ6 follow-up (2026-10-05)

- Ported thesis commit `a2700ca` (`revise(ch5): refine RQ6 exclusion wording`, 2026-09-15), which postdates the backport audit. The Stage 3 and Stage 4 project counts now refer to remaining projects, and the widening-refusal sentence is split in two. The paper keeps its own `Section~\ref{sec:generalized-test-creation}` reference.
- Verification: the complete build has no unresolved references and stays at 59 pages, the `chktex` count for `sections/04-evaluation-09-rq6.tex` is unchanged, and the affected page 43 was inspected in the rendered PDF.

## Decision letter (2026-10-05)

- The TOSEM-2025-1249 decision letter existed only as an untracked file in the macbook-pro thesis worktree, so the reviewer matrix could cite it only by a machine-specific absolute path. It is now versioned in the private correspondence repository as `correspondence/tosem-2025-1249-decision.txt`, and the reviewer matrix cites that path. The untracked copies were removed from the macbook-pro and korolev thesis worktrees.

## Discussion fidelity correction (2026-10-05)

- A sentence-level audit compared the manuscript with every thesis chapter at five commits from 2026-08-30 to 2026-09-15 and with the rejected manuscript. Outside commit `846ab3e` (`docs(discussion): update synthesis and validity`), every number, citation key, and reworded sentence traces to a source or an approved candidate.
- Commit `846ab3e` had rewritten parts of the discussion instead of porting them. Section 5.4 claimed code reviews, stage-wise manual inspection, and repeated experiments where the thesis states single runs per configuration. It also added a conclusion-validity paragraph with unsourced counts (10,436 original tests, 2,763 retained generalized tests) and nonexistent regression models, an equivalent-mutant exclusion step the implementation does not perform, a misquoted equivalent-mutant rate, and inaccurate EqBench and RepoReapers descriptions. Sections 5.1 and 5.3 contained an unsupported significance claim, an altered causal explanation, a mislabeled FuzzChick citation, a "substantially reduce" claim, and a continuous-integration deployment strategy.
- These passages now follow the thesis text. The remaining differences from the thesis are reference styles, the paper's "eligible" project term, and the DC-006 statement that the RQ1 and RQ2 mutation scores are measured before any test is removed.
- Applied DC-007, which corrects two operation-count ranges in RQ2 to match the generated table.
- Verification: the complete build has no unresolved references and is 58 pages, `chktex` reports no warnings for `sections/05-discussion.tex`, and pages 47--53 were inspected in the rendered PDF.

## RQ2 statistics correction (2026-10-05)

- Applied DC-008: the RQ2 complexity and utilization ranges and the discussion's utilization range now match the generated table. The same corrections, DC-007, and the DC-006 statement on when mutation testing runs were applied to the thesis.
- The DC-006 statement matches the implementation: the reduction phase runs PIT on the `ORIGINAL`, `INITIAL`, and complete generalized suites, and no PIT run follows test removal (`PipelinePhase.REDUCTION`).
- Verification: the complete build has no unresolved references and is 58 pages, `chktex` counts are unchanged, and the revised RQ2 page 29 was inspected in the rendered PDF.

## Approach corrections (2026-10-05)

- Applied DC-009 to the paper and the thesis: the constraint-encoding example now numbers parameters from 1, as Algorithm 2 does.
- Applied DC-010 to the paper only: Section 3.6 states that Stage 5 is optional and what skipping it costs and saves.
- Verification: the complete build has no unresolved references and is 58 pages, `chktex` counts are unchanged, the new paragraph ending fills 89% of the text width, and pages 16--18 were inspected in the rendered PDF. Pages after 18 are unchanged.
