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
