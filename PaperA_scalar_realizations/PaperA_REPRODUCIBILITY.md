# Paper A: reproduction guide for the revised source

This guide accompanies `PaperA_revised.tex` and the files in this directory.
The Python checks use only the standard library. Run them with ordinary Python
and do not use `-O`, because the verifiers contain assertions.

```text
python reproduce_paperA.py
```

The driver checks `PaperA_revised_sha256.json`, runs all finite verifiers,
regenerates the machine-readable coordinate, certificate, standard-spread,
and nonlinear-companion data, then checks the manifest again.

| Script | Coverage |
|---|---|
| verify_inner_double_all.py | 31 double certificates s=2..32 with Lucas proofs; all 81 omega bounds s=33..113; uniform constant; diagonal enumeration s=2..6 |
| `verify_inner_mixed.py` | Both exact orders in all 31 double certificates s=2..32; corrected Lang functions at those points; all norm-fiber counts, exact density averages and bounds s=2..6 |
| `verify_inner_symmetry.py` | Four-torsion and Lang multiplier at all 31 certificate points s=2..32; exhaustive primitive-norm fibers and integer character distributions s=2..6 |
| `verify_inner_critical.py` | Independent exact field-tower, recursive Lucas primality, norm and order certificates for every s=2..32; independent subgroup / polynomial-gcd counts for s=2..6; exact effective constant |
| `verify_scalar_depth.py` | Quantitative counts and polynomial/Frobenius classification for even n=2..14; all norm-descent parameters r=2..8; quarter-power polynomial certificates s=1..5 and independent subfield enumeration s=1..4; direct graph certificates on 4 and 16 vertices; regenerates `scalar_depth_results.json` |
| `verify_scalar_realization.py` | All multiplicative subgroup orders in even dimensions 2 through 14; compares polynomial gcds with explicit field enumeration, audits the Jacobi bounds and the explicit index-three witness, and regenerates `scalar_realization_results.json` |
| `verify_paperA_structure.py` | Coordinate bases, cycle types, group orders, polynomial data, basis orderings, and the finite tau-collapse checks |
| `verify_k1_29.py` | The 29 trace-one primitive-element certificates used in Appendix B |
| `verify_complete_mapping_orbits.py` | Affine complete mappings through dimension four and all four-dimensional spreads and orientations |
| `verify_affine_groups_and_conjugacy.py` | Direct group closures, action criteria, four-dimensional conjugacy classes, and signed Burnside counts |
| `verify_standard_spread_orbits.py` | Standard-spread orientation orbits and stabilizers for dimensions four and six; regenerates `standard_spread_results.json` |
| `verify_nonlinear_companions.py` | The explicit 16-point companion triple, its three-cycle certificate, and translated-fixed identities; regenerates `nonlinear_companion_results.json` |
| `export_paperA_data.py` | Regenerates the coordinate tables and the 29 certificate rows by reusing the structural and certificate verifiers |

The Python driver does not build the Lean project. The supplied `lean/`
directory records its source files, toolchain, dependency lock, and checked
environment. The scope and limits of those formal checks are stated in the
manuscript's computational appendix.

The finite computations check the stated finite cases. They do not replace the
paper proofs of results asserted for arbitrary dimensions.

The fixed-index existence theorem and the exact index-three threshold have
complete paper proofs. The latter uses one explicit degree-eight field
certificate and analytic inequalities for all higher even dimensions.
`abstract_en.txt`, `abstract_zh.txt`, and both submission forms are synchronized
with the saved revised source. The forms are local drafts; no submission is
performed by this driver. The built-in editor compiles the current source for
preview; a separate PDF export and visual page review are not claimed here.
`PaperA_scalar_update.diff` records the preceding scalar-realization update
against its own preceding source. Older archives in the recovery directory
are historical snapshots; the current version is identified by
`PaperA_revised_sha256.json`.

## Critical-index revision (2026-10-12)

The quantitative, norm-descent, quarter-power obstruction, primitive-classification
and generating-triangle results have complete paper proofs in Section 5.
The new finite verifier audits the explicit ranges above; it does not establish
the infinite assertions by extrapolation. Existing Lean inputs are unchanged.
The literature comparison is in `Literature_Audit_scalar_realization.md`.
`PaperA_depth_update.diff` compares this revision with the immediately preceding
saved source. The older `PaperA_scalar_update.diff` describes the previous update.
That earlier revision identifier was `paperA-revised-2026-10-12-critical-index`.
Only the new finite arithmetic checks were executed for this research update;
the full reproduction driver remains available to run all supplied checks.

## Inner critical all-dimensional revision (2026-10-12)

That revision was `paperA-revised-2026-10-12-inner-critical-all`.
Theorem 5.20 proves existence at k=t-1 for every t=2^s, s>=2: the analytic
argument covers s>=33 and the exact certificates cover every s=2..32.
Theorem 5.19 gives the primitive-slope count and its error. Both use the
classical Weil curve bound; the Lang pullback and conductor-eight hypotheses
are proved in the source. These results are outside the existing Lean scope.

Run `python verify_inner_critical.py` to audit the new finite certificates.
The certificate finder is optional; verification does not import it.
`Research_Report_inner_critical.md` contains the complete Parts I-VI report.
`PaperA_inner_critical_update.diff` compares with the saved immediately
preceding source. This research turn ran the new independent finite verifier
and static document/hash checks; unchanged older verifiers were not rerun.
The complete reproduction driver now includes all ten verifier/export steps.
The current editor source compiled successfully. No separate PDF was exported.

## Explicit descent and four-torsion review merge (2026-10-12)

That revision was `paperA-revised-2026-10-12-lang-trace-four-torsion`.
Lemma 5.17 contains the explicit descended Frobenius and character trace.
Proposition 5.18 proves the four-torsion, boundary and character symmetries;
Theorems 5.19 and 5.20 are the count and all-dimensional realization results.
The character bound remains 8 sqrt(t).

Run `python verify_inner_symmetry.py` for the added finite symmetry checks.
They use the independently audited verifier's arithmetic, without importing
the certificate finder or evaluating characters in floating point. The checks
cover all 31 certificate points for s=2..32, and all primitive-norm fibers for
s=2..6. Integer multiplicity invariance verifies the character-sum symmetries
in this finite range. These checks supplement the universal paper proof.

This review turn reran verify_inner_critical.py and verify_inner_symmetry.py.
Full outputs are inner_critical_review_run.log and inner_symmetry_review_run.log;
review_verification_environment.json records Python, the platform, exit codes,
and the input/output hashes. Other older verifiers and Lean were not rerun.
The complete reproduction driver includes eleven verifier/export steps.
Review_Response_2026-10-12.md explains which review suggestions were adopted
and the limits of the literature comparison. No external expert approval or
new visual PDF audit is claimed. The existing editor compiles the saved source.

## Mixed character and density revision (2026-10-12)

Previous revision: `paperA-revised-2026-10-12-mixed-character-density`.
Proposition 5.21 proves the actual mixed Lang cover and conductor ≤8;
Corollary 5.22 classifies the norm-only two-character exceptions.
Theorem 5.23 proves both fixed-fiber and whole-family joint generation counts;
Theorem 5.24 proves double full-order asymptotics and eventual existence.
All-dimensional double full order remains open.

Run `python verify_inner_mixed.py` for the finite checks stated in the table.
The external double certificates have been copied into
`inner_double_order_certificates.json`; their input digest and all exact order
residues are in `inner_mixed_verification.json`.
This turn ran that verifier and the static source/abstract/hash audit;
older unrelated verifiers and Lean were not rerun.
The full driver now has twelve finite verifier/export steps.
Complete proof, dependencies and risks are documented in
`PaperA_Mixed_Character_Proof_and_Density.md` and the handoff ledger.
`PaperA_mixed_character_update.diff` compares with the preceding saved source.
The existing source editor is retained; no replacement source tab or separate
PDF export was created.


## Submission tightening (2026-10-12)

Historical revision: `paperA-revised-2026-10-12-submission-tightening`. Main results 5.21–5.24 retain their
numbers. Two named auxiliary lemmas make character decomposition and
exact cyclic-group averaging explicit. The double-order analytic set is
eq:inner-double-range; all-dimensional double existence was open in that historical revision.
Abstracts, forms, and insertion fragments are synchronized.
This pass uses paper proof review and document checks. It does not rerun
the finite-arithmetic verifiers or Lean; their earlier logs retain their
original scope and identifiers. No additional finite cases are asserted.
See PaperA_Submission_Stress_Audit.md and the new source difference file.

## Historical revision: all-dimensional double full order

Identifier: paperA-revised-2026-10-12-double-full-order-closure.
Theorem 5.24 now proves both exact orders for every s>=2.
Proposition 5.25 supplies a four-point Lang bound and two primitive indicators.
The field certificates s=2..32, integer omega bounds s=33..113 and uniform
analytic tail s>=114 cover every parameter. The trace-one subfamily is empty
at s=3,5 and is only asserted positive for every s>=33.
Run python verify_inner_double_all.py without -O. It imports no finder;
small primes are reconstructed by deterministic trial division. Residuals
are never presumed prime. The independent field arithmetic and Lucas checker
are shared with the old verifiers, and every double certificate is rechecked.
The finite verifier does not alone prove the infinite result: the four-point
conductor and uniform tail have manuscript proofs.

This turn ran this relevant verifier, document/hash checks and the built-in
compiler. Records: inner_double_all_run.log, inner_double_all_verification.json,
double_all_verification_environment.json, Double_Full_Order_Final_Audit.json.
Unrelated verifiers and Lean were not rerun; the full driver now has 13 steps.
No separate PDF was exported and no replacement editor tab was opened.


## Current revision: narrative and priority review

Identifier: paperA-revised-2026-10-12-submission-narrative-priority.
Title, abstracts and both local forms now foreground affine companion
realizations, density and all-dimensional double full order.
Proposition 5.25 clarifies the torus descent and geometric irreducibility;
the mathematical bounds and parameter coverage are unchanged.
Cohen (2003), Section 4, is now explicitly credited for the reciprocal-trace
change of variable. CKR22 criteria are compared with an exact parameter dictionary.

This revision performs source/form/reference/fragment/hash checks and built-in
LaTeX compilation. It does not rerun finite-field or Lean verifiers.
The earlier exact arithmetic results retain their original source/input hashes
and run environments; the new final audit verifies that these files are unchanged.
The reproducibility entry point continues to provide the same 13 arithmetic checks.
Latest literature coverage: PaperA_Submission_Narrative_and_Priority_Audit.md.
Latest source checks: Submission_Narrative_Final_Audit.json.


## Current general-article preprint revision (2026-10-12)

The open master remains the generic article source PaperA_revised.tex;
journal-specific class files and formatting are deferred. The abstract and
both local platform forms now use the same scope: exact-order adjacent pairs
are identified as a standard primitive-pair object, while the principal
quantitative advance is the norm-fiber estimate and its exact averaging.
The text distinguishes the O(t) fixed-fiber scale from the O(t^2)
full-family count.

The mixed-character proof now lists two explicit geometric inertia vectors
that generate the full product deck group. The four-point diagonal-cover
argument records why each nontrivial character has conductor exactly four.
These clarifications do not change the constants or theorem statements.

For this revision, verify_inner_mixed.py and verify_inner_double_all.py
were rerun successfully. The former checks double-order certificates for
s=2..32 and all norm-fiber counts for s=2..6; the latter checks the 81
divisor bounds for s=33..113, the uniform tail constant, and the same finite
certificates. They check finite arithmetic only; the paper's curve and
character arguments establish the uniform results. The full 13-step
reproduction driver remains the package entry point.

The final general-article preprint revision then passed the complete
13-step reproduction driver after abstract synchronization; all regenerated
files matched the manifest. The current master also compiled successfully
with the desktop editor's built-in LaTeX compiler. The scoped mathematical
findings and limits are recorded in
PaperA_Preprint_Proof_and_Readiness_Audit_2026-10-12.md.
