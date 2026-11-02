# Four-zero tail-palindromic polynomials over F2

**Four-zero tail-palindromic polynomials over F2: reciprocity and transformation boundaries**

**Wencong Huang, Baohua Li** · Version 3.0 · 18 pages · 2 November 2026

- Version DOI: https://doi.org/10.5281/zenodo.23880299
- All versions: https://doi.org/10.5281/zenodo.22745835
- Fixed GitHub release: https://github.com/63331849121/yijing-mathematical-structures/releases/tag/paperF-v2026.11.02
- [Manuscript PDF](PaperF_fourzero.pdf)
- [Self-contained LaTeX source](PaperF_fourzero.tex)
- [Required proof materials, source and data](PaperF_data_and_code.zip)
- [Complete manuscript and proof bundle](PaperF_revision_bundle.zip)

## Results

The paper retains the exact reciprocal obstruction and full-degree quadratic
transform intersection classifications. Section 4 adds a computer-assisted
classification of the cubic and quintic root-power images, counting roots
with multiplicity. No cubic image is tail-palindromic. The quintic image is
tail-palindromic exactly for the degree-10 exception or the explicit family
`(n,i,j)=(7d-1,2d-1,3d-1)`, `d=1 or 9 (mod 10)`. Its number of missing tail
coefficients is 2 or 2d, always 2 modulo 4, so it never stays in the four-zero
family. The progression is reducible for d>1. Classical generalized Graeffe
transforms, resultants and power-composition criteria are explicitly credited.

Conjecture C4 remains open. These are boundaries for specified constructions,
not an infinite-degree primitive-existence theorem.

## Proof materials and reproduction

Appendix B and `verification/root_power/` are required parts of the
computer-assisted classification proof. They cover unbounded integer
parameter regions, not a finite list of degrees. Use Python 3.10 or later
and its standard library, without `-O` or `-OO`:


cd verification/root_power
python check_cubic_formal.py
python check_quintic_classification.py
python check_quintic_branches.py
python check_certificate_lattice.py


The two certificates are `cubic_certificate.json` and
`quintic_classification_certificate.json`. The independent lattice audit
uses quotient-algebra determinants and integral Bezout lattices; it imports
neither the builders nor the other checkers. Run in a working copy to retain
the supplied receipts. No SMT solver is required.

The unchanged complete arithmetic enumeration covers 161700 candidates at
98 even degrees 6--200, with 2663 primitive polynomials. First witnesses
cover all 148 even degrees 6--300; degrees 202--300 are prefix checks.
The historical arithmetic audit alone requires `python-flint==0.9.0`:


python verification/primitivity/verify_primitivity.py --data verification/primitivity/inputs --out rerun_primitivity


Historical audit hashes and local-only statements in review reports describe
the earlier reviewed inputs and the time at which those reports were written.
The authorship correction changes the byline and PDF author metadata while
retaining the entire reviewed mathematical body. The current files are bound
by `release_manifest.json` and `SHA256SUMS.txt`. Compile the source twice with
pdflatex. The complete proof package should accompany any PDF distribution.

## Earlier versions and authorship

All versions are attributed, in order, to **Wencong Huang, Baohua Li**.
Authorship-corrected earlier files are retained under `history/`. The version
DOIs are https://doi.org/10.5281/zenodo.22745836 (1.0),
https://doi.org/10.5281/zenodo.23764251 (2.0), and
https://doi.org/10.5281/zenodo.23766722 (2.1).
Old Git commits remain provenance records; release notes identify the
authorship correction and the current corrected distribution.

Manuscript, mathematical data and reports: CC BY 4.0. Original verification
code: MIT, retaining its original copyright notice. See the license files.
Publisher full texts, private drafts and local credentials are not included.
