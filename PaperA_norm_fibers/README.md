# Norm-fiber densities and relative traces in characteristic two

**Baohua Li · research preprint · v17 · 28 October 2026**

- [Main paper](main.pdf), 41 pages.
- [Supplement](supplement.pdf), 36 pages. Keep the two PDFs together for cross-document links.
- [Editable LaTeX sources](LaTeX_sources.zip).
- [Research sources, raw data, exact certificates and verification programs](source_and_verification.zip).
- [Lean sources and actual check records](formalization/) / [download the Lean package](Lean_verification.zip).
- [Precise formalization scope](formalization/INTERFACE_SCOPE.txt), [citation](CITATION.cff), [checksums](SHA256SUMS.txt).
- [Versioned release](https://github.com/63331849121/yijing-mathematical-structures/releases/tag/paperA-v2026.10.28-v17).

The main paper develops effective norm-fiber densities, uniform exact-order
relative traces over the intermediate field, the C9/C11 exceptional trace
classification, distribution formulas and affine companion groups. Classical
counting objects and general methods are credited explicitly. The supplement
contains coordinate constructions, oriented spreads and further exact checks.

## Changes in v17

The mathematical statements and raw computational logs are unchanged from the
locally checked v16 revision. The current selective Lean build checks nine
modules: 129 theorem/lemma declarations and 33 definitions. It now constructs
the rational a/gamma bijection, proves the exact-order component equivalence,
and transfers the original M_c count using named Algebra.norm and Algebra.trace
in a genuine quadratic-quadratic finite-field tower. The shifted support-count
identity and the zero trace slice are checked as well.

All declaration audits use only the standard foundations propext,
Classical.choice and Quot.sound, with no proof placeholders or additional
mathematical axioms. Concrete field certificates, fixed-generator conversion,
the full exceptional-case assembly, geometric estimates, sieve and infinite
tail remain outside the build. This is not complete Lean formalization of
Theorems 5.1/5.4 or of the paper. See the scope file for the exact assumptions.

## Reproduce

Extract source_and_verification.zip and enter PaperA_research_artifact/project/.
Start with REPRODUCE.txt. The archive's artifact_manifest.json checks every
distributed project file. The current entry points include the independent
exact field-certificate checks, raw log generation/readback, and the pinned
Lean verifier. The selected provenance subset is not a complete legacy checkout;
its historical full-repository driver is not the current entry point.

The data include 1,384,765 element records with explicit field parameters,
norms, fiber identifiers and relative traces, plus population and certificate
logs. Declared finite ranges are specified in data_deposit/README.txt. Infinite
parameter statements rely on proofs, rather than finite extrapolation. The
data retain their recorded runs; they were not relabeled as new computations.

Build the manuscript pair with python build.py using pdflatex. For the Lean
interfaces, install the pinned dependencies as described in formalization/README.txt
and run python formalization/verify_interfaces.py. Existing dependency caches
were reused for the recorded checks; a cache-free build is not claimed.

## Versions, citation and licenses

The [2026-10-26 release](https://github.com/63331849121/yijing-mathematical-structures/releases/tag/paperA-v2026.10.26)
is retained. The [Chinese visual overview from that version](overview_zh.pdf)
is a dated mathematical introduction; use the v17 scope file for current
formalization coverage. Its stated old page count/check coverage is historical.
The [old timestamp materials](history/2026-10-26/) retain their original pairing.

The earlier Singer-note DOI 10.5281/zenodo.22731492 and Paper F DOI are not
assigned to this expanded preprint. Cite the current title, author, version
and release URL. Existing manuscript CC BY 4.0, verification-code MIT and font
license notices are retained; no new dataset-specific license or DOI is asserted.
The preprint has not been externally peer reviewed. See [license details](LICENSES.txt).
