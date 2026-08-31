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
