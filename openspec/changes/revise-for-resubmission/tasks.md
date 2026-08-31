## 1. Establish Paper-Local Execution and the Baseline

- [x] 1.1 Clone `glockyco/Teralizer-Paper` outside `projects/`, or verify that the standalone clone is clean and points to the canonical GitHub paper repository
- [x] 1.2 Read the current paper repository guidance, identify the canonical GitHub and GitLab remotes, inspect both CI workflows, and record their effective build, bibliography, style, and PDF-inspection commands
- [x] 1.3 Scaffold `revise-for-resubmission` through OpenSpec in the standalone paper clone before any manuscript edit
- [x] 1.4 Transfer the approved proposal, specification, design, and tasks through the paper-local OpenSpec workflow and store all later traceability controls under that change workspace
- [x] 1.5 Validate the paper-local change, mark tasks 1.1--1.5 complete in its task artifact, and designate it as the only owner of manuscript execution progress
- [x] 1.6 Stop implementation tracking in this source change and resume application from the validated paper-local change without marking later source tasks complete
- [x] 1.7 Create a dedicated resubmission branch and verify the rejected manuscript commit is reachable from the branch history
- [x] 1.8 Run the effective local commands for both CI workflows on the unmodified branch and record the successful baseline PDF checksum and page count
- [x] 1.9 Verify `glockyco/Teralizer`, the thesis paper submodule, and all repositories under `projects/` are unchanged before any manuscript edit
- [x] 1.10 Record that no remote will be pushed and no remote CI result will be claimed without explicit operator authorization

## 2. Build the Traceability Controls

- [x] 2.1 Create the section-level backport manifest under the paper-local change workspace with `PORT`, `ADAPT`, `KEEP-PAPER`, `DROP`, and `VERIFY` decisions for all 54 audited changed paths
- [x] 2.2 Add every Senior Associate Editor and reviewer concern to a response matrix under the paper-local change workspace and verify each decision-letter paragraph has a row
- [x] 2.3 Map each empirical paper claim to a registered report, provenance entry, generated artifact, or preserved run source in the paper-local evidence map and flag every evidence gap
- [x] 2.4 Record the section correspondence under the paper-local change workspace and verify every rejected-paper section has an intended source strategy
- [x] 2.5 Add each design reference formulation to the paper-local formulation register with its manuscript, cover-letter, or prior-review-response destination and a `USE`, `ADAPT`, or `OMIT` disposition
- [x] 2.6 Commit the verified baseline, paper-local planning artifacts, and traceability controls before publication integration begins
- [x] 2.7 Complete a separate Teralizer OpenSpec change that publishes table-body fragments with `\linewidth`, leaves its worktree unchanged during publication, and records a separate thesis-wrapper migration; keep paper publication blocked until this interface is available
- [x] 2.8 After the fragment interface is available, add every required RQ0--RQ6 artifact key and destination to the paper's `publish.toml`, run Teralizer's complete-report publication command against preserved evidence, and verify all dependencies, fragment destinations, row anchors, aggregate macros, figure PDFs, and unchanged source-repository state without starting an experiment
- [x] 2.9 Create manuscript-owned wrappers for every generated table fragment consumed by the current manuscript, preserve paper-specific captions, labels, placement, sizing, and local style, import the aggregate macro file unchanged, and verify that the ACM manuscript builds without an alias, value mapping, or manual artifact substitute
- [x] 2.10 Commit the verified publication interface and paper-owned wrappers with no scientific manuscript changes
- [ ] 2.11 Revise the existing backport manifest so `PORT`, `ADAPT`, and `VERIFY` enforce thesis-first fidelity, add its deferred-candidate register, record the proposed `ORIGINAL`/`INITIAL` and mutation-round clarification there, and verify each existing disposition permits only necessary standalone adaptation

## 3. Port Concepts and the End-to-End Approach

- [ ] 3.1 Remove the uncommitted synthesized concepts addition, port the thesis assertion-to-MUT, MUT-call, specification, partition, oracle, and failure-result definitions substantially unchanged, and verify every textual difference is a necessary paper adaptation
- [ ] 3.2 Port the thesis end-to-end algorithm listing and its explanation substantially unchanged, preserve its inputs, outputs, control flow, failure outcomes, and retention rules, and record rather than apply any implementation-driven improvement
- [ ] 3.3 Port the thesis test-and-assertion-analysis account substantially unchanged, adapt only paper labels and assembly, and record any JUnit-support, filter, collection-round, or assertion-form discrepancy as a deferred candidate
- [ ] 3.4 Port the thesis tested-method-identification account substantially unchanged and record any normalization, composite-expression, producer-selection, ranking, or unresolved-case discrepancy as a deferred candidate
- [ ] 3.5 Port the thesis specification-extraction account substantially unchanged and record any symbolic-execution, type, string, resource-limit, or failure-outcome discrepancy as a deferred candidate
- [ ] 3.6 Port the thesis generalized-test-creation account substantially unchanged and record any generator, path-filter, symbolic-oracle, original-input, widening, or exception-evidence discrepancy as a deferred candidate
- [ ] 3.7 Port the thesis test-suite-reduction account substantially unchanged and record any mutant-retention or source-assertion-removal discrepancy as a deferred candidate
- [ ] 3.8 Port the thesis algorithm and corrected examples while preserving paper-owned figure and listing presentation, and verify that presentation adaptations do not change scientific content
- [ ] 3.9 Compare the complete paper approach with the thesis source, verify every substantive thesis passage is present, and verify every departure is limited to standalone framing, labels, macros, assembly, or ACM presentation
- [ ] 3.10 Run the recorded manuscript checks, inspect the rendered approach pages, and commit the faithful approach backport as one atomic unit

## 4. Port the Evaluation Framework and RQ1--RQ5

- [ ] 4.1 Port the thesis research-question sequence with RQ0, adapt only paper numbering, labels, cross-references, and roadmap assembly, and verify the sequence remains consistent through RQ6
- [ ] 4.2 Port the thesis evaluation framework substantially unchanged, retain paper-only setup needed for a standalone account, and record any variant, budget, selection, dataset, timeout, or terminology concern as a deferred candidate
- [ ] 4.3 Connect the ported framework to the already-published controlled-study fragments and figures through generated row anchors and manuscript-owned labels, and verify the delivered files remain unedited
- [ ] 4.4 Preserve the thesis controlled-study account and measurements substantially unchanged, use equivalent generated paper macros where required by assembly, and record rather than correct any suspected stale terminology or evidence discrepancy
- [ ] 4.5 Compare the framework with the thesis source, run the recorded manuscript checks, inspect the generated assets, and commit the faithful framework backport
- [ ] 4.6 Port the thesis RQ1 and RQ2 text substantially unchanged, verify values and denominators for the deferred-review register without rewriting the port, run focused checks, inspect the result, and commit the RQ1--RQ2 backport
- [ ] 4.7 Port the thesis RQ3 text substantially unchanged, record any test-count, line-count, runtime, reduction, or terminology concern for deferred review, run focused checks, inspect the result, and commit the RQ3 backport
- [ ] 4.8 Port the thesis RQ4 text substantially unchanged, record any processing-time, mutation-cost, Pareto, or efficiency concern for deferred review, run focused checks, inspect the result, and commit the RQ4 backport
- [ ] 4.9 Port the thesis RQ5 text substantially unchanged, record any exclusion, percentage, reference, population, or interpretation concern for deferred review, run focused checks, inspect the result, and commit the RQ5 backport

## 5. Port RQ0 and the JARVIS Comparison

- [ ] 5.1 Port the thesis JARVIS background, twelve-project scope, published-data limits, revision reconstruction, ten-scenario protocol, and sampling configuration substantially unchanged, adapting only standalone cross-references and assembly
- [ ] 5.2 Select the already-published RQ0 fragments used by the thesis section, create upright and readable paper-owned wrappers only for those fragments, and verify every included cell and row anchor without changing the ported narrative; if selected evidence does not fit, stop and ask the operator
- [ ] 5.3 Port the thesis project and MUT applicability result substantially unchanged and record any provenance discrepancy as a deferred candidate
- [ ] 5.4 Port the thesis higher, lower, and missing PVC outcomes substantially unchanged and record any category or scenario discrepancy as a deferred candidate
- [ ] 5.5 Port the thesis PVC-budget and mutation-detection interpretation substantially unchanged and record any proposed clarification as a deferred candidate
- [ ] 5.6 Port the thesis JARVIS validity and comparison limits substantially unchanged and record any proposed strengthening or qualification as a deferred candidate
- [ ] 5.7 Compare the complete RQ0 section with the thesis source, run the recorded manuscript checks, inspect all RQ0 tables, and commit the faithful RQ0 package atomically

## 6. Port RQ6 with RepoReapers Version 7

- [ ] 6.1 Port the thesis version 7 population and selection account substantially unchanged, including the 584 selected projects, 550 initial-gate exclusions, and 27 projects without executed tests
- [ ] 6.2 Port the thesis project lifecycle and stage-entry account substantially unchanged and record any project-funnel discrepancy as a deferred candidate
- [ ] 6.3 Select the already-published RQ6 fragments used by the thesis section, create upright and readable paper-owned wrappers only for those fragments, and verify every included cell and row anchor without changing the ported narrative; if selected evidence does not fit, stop and ask the operator
- [ ] 6.4 Port the thesis test-level account substantially unchanged and record any population discrepancy as a deferred candidate
- [ ] 6.5 Port the thesis assertion-level account substantially unchanged and record any count or denominator discrepancy as a deferred candidate
- [ ] 6.6 Port the thesis generalization lifecycle, widening, emission, validation, reduction, and final-test account substantially unchanged and record any discrepancy as a deferred candidate
- [ ] 6.7 Port the thesis 85-of-584, 14.6%, and final-generalized-test result substantially unchanged and record any definition or provenance discrepancy as a deferred candidate
- [ ] 6.8 Port the thesis failure interpretation and three-part cause taxonomy substantially unchanged and record any mechanism-classification concern as a deferred candidate
- [ ] 6.9 Port the thesis version 7 provenance, manual-review boundaries, evidence gaps, and validity discussion substantially unchanged
- [ ] 6.10 Search the complete paper for remnants of the rejected RQ6 account, remove only passages superseded by the ported thesis section, and record any ambiguous historical occurrence for deferred review
- [ ] 6.11 Compare the complete RQ6 section with the thesis source, run the recorded manuscript checks, inspect every RQ6 table and page, and commit the faithful version 7 package atomically

## 7. Port Discussion, Validity, and Related Work

- [ ] 7.1 Port the thesis discussion substantially unchanged and retain paper-only context only where the thesis relies on other chapters
- [ ] 7.2 Port the thesis validity account substantially unchanged and retain the standalone paper's necessary study context without adding new qualifications during the backport
- [ ] 7.3 Port the thesis explanation of mutation-independent Stages 1--4 and mutation-based Stage 5 substantially unchanged, and defer any proposed implementation clarification
- [ ] 7.4 Port the thesis exactness and intent language substantially unchanged, and defer any proposed reformulation even when it appears more precise
- [ ] 7.5 Port the thesis distinctions among approach, prototype, RQ0, RQ1--RQ5, and RQ6 substantially unchanged, adapting only references required by the standalone structure
- [ ] 7.6 Port the thesis RQ0, version 7, widening, failure-mechanism, and prototype-restriction synthesis substantially unchanged
- [ ] 7.7 Port the thesis LLM discussion substantially unchanged and retain additional paper-related work only where a standalone reader requires it
- [ ] 7.8 Port the thesis mutation-proxy and construct-validity discussion substantially unchanged and record any proposed addition or removal as a deferred candidate
- [ ] 7.9 Preserve all distinct thesis methods, results, research questions, and validity conditions, and do not make cosmetic or page-length edits during the backport
- [ ] 7.10 Compare the discussion, validity, and related-work sections with the thesis source and record every nonessential proposed departure in the deferred-candidate register
- [ ] 7.11 Run the recorded manuscript checks, inspect the ported discussion and related-work pages, and commit the faithful synthesis backport atomically

## 8. Adapt Paper-Level Framing and Publication Assets

- [ ] 8.1 Preserve the standalone paper's fuller background and integrate only thesis scientific additions that remain meaningful outside the monograph, adapting cross-references without importing the thesis's reduced-background structure
- [ ] 8.2 Adapt the paper introduction, contribution list, and roadmap to the fully ported body, using thesis content where applicable and changing only what the standalone genre and added RQ0 or RQ6 material require
- [ ] 8.3 Adapt the abstract to the fully ported results and scope while preserving thesis formulations where they fit the standalone paper
- [ ] 8.4 Adapt the standalone conclusion to the fully ported thesis content, retain the paper conclusion structure, and omit the thesis bridge
- [ ] 8.5 Port required bibliography additions, adapt citation keys and artifact URLs, update the replication-package DOI, and verify all citations resolve without rewriting cited claims
- [ ] 8.6 Audit the complete paper `publish.toml`, aggregate macro import, generated table-body fragments and figure PDFs, manuscript-owned wrappers, listings, captions, labels, variant names, and RQ identifiers; verify every included table is upright and readable, every analysis-owned artifact is direct and unedited, and every factual caption claim is recorded for deferred review if it conflicts with the thesis; if evidence does not fit, stop and ask the operator before any remedy
- [ ] 8.7 Verify that every planned thesis passage is present or has a necessary recorded disposition, run the manuscript checks, inspect the complete rendered paper, and commit the framing and publication-asset adaptation atomically

## 9. Review Deferred Substantive Improvements

- [ ] 9.1 Freeze the complete first-pass manuscript, compare every ported section with its thesis source and manifest disposition, and verify the deferred-candidate register contains every proposed nonessential substantive departure
- [ ] 9.2 Present every deferred candidate to the operator with its thesis source, exact proposed change, material benefit, and evidence, record an explicit approve or reject decision, and block manuscript changes while any candidate remains undecided
- [ ] 9.3 Apply only approved candidates, preserve thesis content for every rejected candidate, and keep each applied change traceable to its recorded decision
- [ ] 9.4 Recheck all applied candidates against affected sections, evidence, and implementation sources and verify no unapproved stylistic, terminological, formal, or scientific rewrite entered the manuscript
- [ ] 9.5 Run the recorded manuscript checks, inspect every page affected by approved candidates, and commit the post-port improvement review separately from the faithful backport commits

## 10. Prepare the TOSEM Submission Correspondence

- [ ] 10.1 Draft a concise new-submission cover letter that identifies TOSEM-2025-1249 as the rejected predecessor, summarizes the substantive revision, and does not imply an invited or requested revision
- [ ] 10.2 Draft the prior-review-response overview around the concepts and algorithm, complete JARVIS benchmark, version 7 RepoReapers evaluation, and claim clarifications and verify each headline maps to manuscript locations
- [ ] 10.3 Answer the mutation-selection concern with the stage boundary, reduction invariant, retained-suite benefit, generalization cost, mutation-proxy limitation, and any existing pre/post evidence and verify the response does not concede generation overfitting
- [ ] 10.4 Answer the applicability concerns with both the JARVIS and RepoReapers results and verify all denominators and comparison limits are explicit
- [ ] 10.5 Answer the exactness and intended-behavior concerns with the developer-anchored, implementation-derived account and verify the response matches paper terminology
- [ ] 10.6 Answer type, purity, project, and framework scope concerns and verify the response distinguishes approach limits from prototype and evaluation outcomes
- [ ] 10.7 Answer the LLM request with the expanded comparison and future direction and verify no unimplemented integration is promised
- [ ] 10.8 Answer the length request by identifying removed redundancy and retained distinct RQs and verify the tone remains factual and respectful
- [ ] 10.9 Mark independent real-bug or held-out-mutant validation as not added, explain the rationale and remaining construct limit, and verify the prior-review response does not imply such evidence exists
- [ ] 10.10 Complete the reviewer matrix with final page, section, figure, table, and listing references and verify every concern has one disposition
- [ ] 10.11 Build or render the cover letter through its declared workflow, inspect it, and commit it as a verified correspondence unit
- [ ] 10.12 Build or render the prior-review response through its declared workflow, inspect it, and commit it as a separate verified correspondence unit

## 11. Perform Submission Verification

- [ ] 11.1 Run the complete manuscript build from a clean generated state and verify the command succeeds without unresolved references or bibliography errors
- [ ] 11.2 Run the effective local commands for both paper CI workflows and the repository's complete style, spelling, hygiene, and pre-commit checks and resolve every task-owned failure
- [ ] 11.3 Compare all manuscript empirical values with the evidence map and verify each measure has its denominator and provenance owner
- [ ] 11.4 Recheck the backport manifest and deferred-candidate register, verify every `PORT`, `ADAPT`, and `VERIFY` item has a final disposition and source location, and verify no rejected or undecided candidate changed the manuscript
- [ ] 11.5 Recheck the reviewer matrix and verify every promised revision exists in the final manuscript or prior-review response
- [ ] 11.6 Inspect the complete rendered manuscript, cover letter, and prior-review response in their actual PDF surfaces and resolve layout, clipping, reference, table, and figure defects
- [ ] 11.7 Verify `Teralizer-Paper` is clean except for intended manuscript, correspondence, generated publication, and paper-local OpenSpec files and verify `Teralizer`, the thesis submodule, preserved data, and generated datasets remain unchanged
- [ ] 11.8 Create the final atomic commit for submission-only corrections and verify the full local check set passes on the committed tree
- [ ] 11.9 Report the branch as locally verified and push-ready unless the operator explicitly authorizes synchronization of both canonical remotes
- [ ] 11.10 If synchronization is explicitly authorized, push both canonical remotes, observe both CI workflows, and report their exact results
