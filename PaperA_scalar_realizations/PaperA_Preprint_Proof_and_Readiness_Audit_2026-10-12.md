# Paper A: general article preprint proof and readiness audit

Revision: paperA-general-preprint-2026-10-12-proof-audit
Date: 2026-10-12

## Master document

The existing PaperA_revised.tex remains the master source and retains
\documentclass[11pt]{article}. No journal-specific class, replacement source,
external submission, or separate PDF was created. Journal formatting can be
handled later in a separate copy if a target journal is chosen.

## 1. Scoped proof audit

This pass concentrated on the new central chain: the mixed-character estimate,
local averaging and joint-generation density, the double full-order count, and
the trace-one construction used for all-dimensional existence.

- The mixed-character proof uses the actual descended Lang functions and the
  eight-row valuation table. The two inertia vectors at (0,1) and (0,b^{-1})
  now explicitly generate Z/A x Z/B x Z/B: their difference generates the
  third B-factor, and a combination with the first vector has order AB in the
  first two factors. This closes the geometric-connectedness explanation.
- The tame rank-one conductor is the number of active boundary rows, between
  one and eight for a nontrivial character. The genus-one character bound then
  gives 8 sqrt(t). The proof does not assume that all eight points ramify.
- In the diagonal four-point cover, the valuations are plus or minus 2 in the
  A-coordinate and plus or minus 2 or 2t in the B-coordinate. The coprimality
  checks gcd(2,A)=gcd(2t,B)=1 and gcd(A,B)=1 show that every nontrivial
  character ramifies at all four points; its conductor is exactly four.
- The local averaging identities were checked from the probability
  Pr(p divides j)=1/p for a uniform exponent j. They give the stated
  theta_2(A) and theta_2(A)H(A) averages. In particular, the fixed-fiber
  coefficient is norm-dependent, while summing over t+1 parameters gives
  the full-family quadratic main term.
- The double full-order sieve coefficients and the main term
  theta(d)^2(t+1)^2 were checked against the stated primitive indicators.
  The trace-one construction correctly ties the two orders by
  1+a=a^(t^2). The all-s proof is partitioned into exact field certificates
  for 2<=s<=32, exact divisor bounds for 33<=s<=113, and a uniform analytic
  bound for s>=114. The trace-one subfamily is not asserted positive at s=3,5.

No arithmetic inconsistency was found in this scoped recheck. This is not a
line-by-line reproof of every older structural result in the article, nor an
external referee report. The analytic conclusions depend on the cited
Lang/Kummer construction and curve character bounds; these are classical
inputs, while the source supplies the problem-specific geometric and
conductor checks.

## 2. Narrative and novelty boundary

The abstract now leads with scalar realization density, separates the O(t)
fixed-fiber scale from the O(t^2) full-family count, and says that the explicit
fixed-fiber formula applies to nonexceptional fibers while exceptional fibers
are handled separately. The introduction names the norm-fiber estimate and
its exact local averaging as the quantitative contribution.

The manuscript continues to identify the adjacent exact-order pair as a
standard (t-1)-primitive-pair object and does not claim priority for first
formulating or counting it. It also attributes the reciprocal-trace/Frobenius
construction, Hachenberger's ambient geometry, and the classical Lang, Weil,
Kummer, and primitive-indicator tools. The novelty claim is limited to the
specific norm-fiber density analysis and its scalar affine-companion
interpretation. A finite literature search cannot prove originality; this
pass makes no such claim.

## 3. Reproducibility

The complete 13-step reproduction driver passed after the final source and
abstract edits. It verified the manifest, reran the supplied finite
certificates and verifiers, regenerated the listed data, and confirmed that
the regenerated files match their hashes. In particular, the all-dimensional
closure verifier checked 31 exact-order certificates for s=2..32, all 81
divisor-bound entries for s=33..113, and the uniform tail constant. These
computations verify finite arithmetic inputs; the universal statements still
depend on the written proofs.

The desktop editor's built-in compiler successfully compiled the saved master.
The driver does not build Lean; Lean sources and their stated scope remain
separate. No Lean rerun is claimed.

## 4. Remaining work before a journal submission

The general article/preprint version is now a coherent master. Before
submission, choose a target journal and adapt only a separate copy to that
journal's class, length, bibliography style, and submission metadata. A final
reference-metadata check and a complete manuscript-wide proof read remain
appropriate. No journal-specific compliance or external expert review is
claimed by this pass.
