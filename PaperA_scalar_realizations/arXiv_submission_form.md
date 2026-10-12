# arXiv submission draft — Paper A (narrative and priority review, 2026-10-12)

Revision: paperA-general-preprint-2026-10-12-proof-audit. Local preparation draft.

## 1. Title

Affine companion groups in characteristic two: scalar realizations and density

## 2. Authors

Baohua Li (Independent Researcher; People's Republic of China)

## 3. Comments (draft)

Theorem 5.24 retains the quadratic double-order count and proves
both exact orders for every s>=2. Proposition 5.25 gives a trace-one
subfamily with conductor four. The complete partition is: s=2..32
by exact field certificates, s=33..113 by exact divisor upper bounds
and the four-point estimate, and s>=114 by a uniform odd-integer bound.
The special subfamily is empty at s=3,5; it is not claimed to work
in every dimension. Its linear count is separate from the quadratic
full-family count. The proof is outside the Lean formalization.

The exact-order pair is a standard (t-1)-primitive pair.
The reciprocal-trace/Frobenius change of variable is attributed to
Cohen (2003), Section 4. The contribution presented here is the
effective count on the specific norm fibers and its companion-group
application. Specific priority is unconfirmed; the latest literature
comparison records the full-text coverage explicitly.

Lean scope: function-level triality, field-Singer generation,
and a conditional tau-collapse interface. No Lean rerun was performed
for this editorial revision. Classical curve bounds and exact certificates
are paper-proof dependencies; they are not claimed as formally verified.

## 4. Subject class (draft)

Primary: math.NT (Number Theory). Cross-list: math.GR (Group Theory), math.CO (Combinatorics).

## 5. Abstract (paste exactly)

We study scalar realizations of affine companion groups in characteristic two. For q=2^n, d | q-1, and k=(q-1)/d, we give an exact Möbius formula and an explicit error for the number of a satisfying a, 1+a in C_d and <a,1+a>=C_d. At the quartic norm boundary t=2^s, s>=2, and d=(t+1)(t^2+1), the full-family joint-generation count is |R_d|=theta_2(d)(t+1)^2+O(t^(3/2) 2^omega(d)), where theta_2(d)=product over p|d of (1-p^(-2)). Each norm fiber has O(t) points. On every nonexceptional fiber, we give an explicit O(t) main term with a norm-dependent coefficient and a square-root-scale error; exceptional fibers are bounded separately. Exact local averaging over all t+1 fibers yields the quadratic full-family main term. The number D_d of slopes with ord(a)=ord(1+a)=d obeys D_d~(phi(d)/d)^2(t+1)^2, with an explicit error, and is positive for every s>=2. This exact-order pair is a standard (t-1)-primitive-pair object; we do not claim its first formulation. Our contribution is the norm-fiber density analysis, its companion-group interpretation, and the all-dimensional existence proof. We also determine affine generation criteria and prove the optimal uniform index exponent 1/4; further sections treat spread statistics and a nonlinear example generating A_16. Lean checks only the stated triality and field-Singer results; the density and existence arguments use classical curve bounds and exact arithmetic.
## 6. License (draft)

arXiv.org perpetual, non-exclusive license.

## 7. Source and preparation

- Source: PaperA_revised.tex, in the existing desktop editor.
- Source, both abstracts and both local forms are synchronized.
- Certificates and reproducibility records: PaperA_revised_sha256.json.
- Literature comparison: PaperA_Submission_Narrative_and_Priority_Audit.md.
- Built-in compilation and file checks: Submission_Narrative_Final_Audit.json.

No separate PDF export or visual page inspection is claimed for this
revision. This is a local preparation draft; no external submission,
repository update or archival deposit has been performed.
Earlier local forms, including historical platform notes, are retained
in backups/before_submission_narrative/.
