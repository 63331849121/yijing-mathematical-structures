# Four-zero tail-palindromic polynomials over F2

**Four-zero tail-palindromic polynomials over F2: reciprocal obstructions and quadratic-transform intersections**  
Baohua Li · Research note · 12 pages · 29 October 2026

- Version DOI: https://doi.org/10.5281/zenodo.23764251
- All versions: https://doi.org/10.5281/zenodo.22745835
- Fixed GitHub release: https://github.com/63331849121/yijing-mathematical-structures/releases/tag/paperF-v2026.10.29
- Earlier deposited manuscript: https://doi.org/10.5281/zenodo.22745836

## Results and contribution

The note determines the reciprocal common divisor of four-zero tail-palindromic
polynomials and the exact number of zero-position pairs passing this obstruction.
It classifies the intersections with full-degree binary quadratic rational
transformations. The translated Q branch has two infinite shape families and
three degree-14 exceptions. The translation-invariant branch has exactly four
outputs, (n,i,j)=(14,3,4), (30,5,9), (30,5,12), (30,9,12), all reducible.

More generally, a translation-invariant tail palindrome has n+2 a power of two;
for n at least 6 it is reducible when its number of missing tail coefficients is
divisible by four. A brief B-family descent identity records an explicit
algebraic descent. Classical reciprocal identities, invariant representations
and composition criteria are credited, including Long (1973), Agou (1977)
and Kapetanakis (2017). The family-specific content concerns their compatibility
with the prescribed support and the resulting boundary on quadratic constructions.

The general primitive-existence conjecture remains open. No infinite
irreducible family, new general irreducibility criterion, global-priority
certification, complete formalization or external peer review is claimed.

## Files and finite coverage

- `PaperF_fourzero.pdf` and `.tex`: unchanged reviewed 12-page manuscript and
  self-contained editable LaTeX source. Compile twice with pdflatex.
- `abstract_en.txt`, `abstract_zh.txt`: synchronized abstracts.
- `complete_counts_6_200.csv`: all 161700 candidates at 98 even degrees,
  recovering 2663 primitive polynomials.
- `first_solutions_6_300.csv`: first solutions at 148 even degrees 6--300.
  Degrees 202--300 are first-solution checks, not complete counts.
- `verification/`: original inputs, portable verification programs, written
  proof/attribution reviews and recorded machine outputs.
- `overview_zh.txt`: concise Chinese reading guide.
- `release_manifest.json`, `SHA256SUMS.txt`: release integrity records.

This publication step checks the hashes against the completed local review;
it does not claim to rerun the historical exhaustive arithmetic enumeration.
Earlier dates, page counts, source hashes and local-only status in historical
audit files describe the versions at which those records were produced.
The review of the actual final source is in `verification/final_submission/`.
The original publisher PDFs are not redistributed. Private submission-form
drafts and the older presentation are excluded from this public package.

## Reproduce selected checks

From this folder, with Python 3.10 or later:

```text
python verification/b_descent/verify_b_descent.py
python verification/coset_spectrum/audit_coset_spectrum.py
python verification/translation/verify_translation.py --out audit_rerun_translation
python verification/rational_transform/verify_independent.py
```

These structural checks use the standard library. The separate arithmetic
audit uses python-flint 0.9.0:

```text
python verification/primitivity/verify_primitivity.py --data verification/primitivity/inputs --out audit_rerun_primitivity
```

The stored order audit checks 148 factorizations and 484 distinct prime factors.
Its rigorous software decisions are not exported independent primality
certificates or Lean proofs. Finite checks do not prove all-degree existence.

## License

Manuscript, mathematical data and reports retain CC BY 4.0 terms.
Original verification code retains the repository's MIT terms.
See `LICENSES.txt` and `LICENSE-code-MIT.txt`. Third-party dependencies
and publisher full texts are not bundled.
