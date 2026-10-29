# Yijing Mathematical Structures

Independent research on finite-field, combinatorial, and affine structures inspired by the Yijing.

## Current preprints

### Paper A: norm-fiber densities and relative traces

**Norm-fiber densities and relative traces in characteristic two** · Baohua Li · **v21, 2026-10-29**

Effective norm-fiber estimates, uniform relative traces, complete C9/C11 exceptional
classification and affine companion groups. The main paper has 37 pages and the
supplement 40 pages. The nine-module selective Lean boundary is unchanged.

- [Main paper](PaperA_norm_fibers/main.pdf) / [supplement](PaperA_norm_fibers/supplement.pdf).
- [Research data, code and precise scope](PaperA_norm_fibers/).
- [Chinese reading guide](PaperA_norm_fibers/overview_zh.txt).
- [Versioned GitHub release](https://github.com/63331849121/yijing-mathematical-structures/releases/tag/paperA-v2026.10.29-v21) / [Zenodo DOI](https://doi.org/10.5281/zenodo.23757428).

Earlier Paper A releases and the [preceding scalar-realization archive](PaperA_scalar_realizations/) remain available.

### Earlier Paper A note: affine Singer layers and the (T,D,K) triple

**An affine Singer layer on F2^6, its (T,D,K) triple, and <T,D> = AGL(1,64)**

The note gives an explicit coordinate realization on F2^6, with
`D = (id xor T)^(-1)` and `K = (id xor D)^(-1)`. The maps have cycle types
`T = D = 1+63` and `K = 1+7x9`, satisfy `F^3 = id`, and generate
`AGL(1,64)` of order 4032. The same presentation extends to every even
dimension: `T,D` have type `1+(2^(2k)-1)` and `K` has type
`1+(2^k-1)x(2^k+1)`, with generation of `AGL(1,2^(2k))`.

The contribution is the explicit coordinate realization and the unified
presentation of the triple identities and affine group-generation proof.
The prescribed-trace existence input and character-sum method are classical:
Moreno (1989), Cohen (1990), and the equivalent square-order formulation of
Cohen (2003). Cohen--Presern (2005) also gives a self-contained treatment.
Appendix B reconstructs the even-characteristic trace-one case with a
deterministic finite certificate. No priority is claimed for that input.

**Revision: October 11, 2026 (10 pages).** The proof now takes `alpha=beta`
directly from PTE. Section 7 classifies F-orbits on scalar affine maps and
defines CRT coordinates using iteration exponents. The primitive-polynomial
checks, character-at-zero convention, contribution statement, and reference
list have also been clarified. See [revision notes](PaperA_revision_notes.md).

- [Earlier note PDF](PaperA_singer_TDK.pdf)
- [Earlier note LaTeX source](PaperA_singer_TDK.tex)
- [English abstract](abstract_en.txt) / [Chinese abstract](abstract_zh.txt)

### Paper F: four-zero tail-palindromic polynomials

**Four-zero tail-palindromic polynomials over F2: reciprocal obstructions
and quadratic-transform intersections.** Baohua Li · Research note · 12 pages.

Reciprocal obstruction and surviving-position count, complete quadratic
support intersections and a translation-invariant reducibility obstruction.
Classical invariant representations and irreducibility criteria are credited.
The general primitive-existence conjecture remains open.

- [Paper F manuscript and editable source](PaperF_fourzero/).
- [Chinese reading guide](PaperF_fourzero/overview_zh.txt).
- [Version DOI](https://doi.org/10.5281/zenodo.23764251).
- [Fixed release and verification package](https://github.com/63331849121/yijing-mathematical-structures/releases/tag/paperF-v2026.10.29).
- [Earlier deposited version](https://doi.org/10.5281/zenodo.22745836), preserved.

## Reproduce Paper A's computations

For the current paper, start with the [current source and verification package](PaperA_norm_fibers/).
The command below reproduces the retained earlier scalar-realization archive.

Requires Python 3 and its standard library only. From the repository root:

```text
python PaperA_scalar_realizations/reproduce_paperA.py
```

The driver checks the package manifest, runs the supplied finite verifiers and
exporter, then checks regenerated data against the manifest. These finite
checks do not replace proofs of statements for arbitrary dimensions. See the
[reproduction guide](PaperA_scalar_realizations/PaperA_REPRODUCIBILITY.md) for
coverage and limitations.

## Repository contents

- `PaperA_norm_fibers/`: current main paper, supplement, visual overview,
  complete sources/verification archive, citation metadata and checksums.

- `PaperA_scalar_realizations/`: general-article Paper A source, PDF, abstracts,
  finite verifiers, data, Lean sources, and audit/reproduction materials.
- `PaperA_singer_TDK.pdf` and `.tex`: earlier focused Paper A note.
- `abstract_en.txt`, `abstract_zh.txt`: abstracts for the earlier Singer note.
- `verify_paperA_structure.py`, `verify_k1_29.py`: checks for that note.
- `PaperA_revision_notes.md`: its review corrections and verification record.
- `PaperD_primitive_trace_even_detailed_supplement.pdf`, `.tex`, and
  `detailed_proof_body.tex`: detailed proof archive.
- `PaperF_fourzero/`: Paper F preprint, reproducibility scripts, and data tables.

## Scope

This repository records a broader independent study of mathematical structures
inspired by the Yijing. The mathematical papers and programs are self-contained.

## Citation

Current Paper A: Li, Baohua. (2026). *Norm-fiber densities and relative traces in characteristic two* (v21). Zenodo. [10.5281/zenodo.23757428](https://doi.org/10.5281/zenodo.23757428).

Earlier Singer-layer note: Li, Baohua. (2026). *An affine Singer layer on F2^6, its (T,D,K) triple,
and <T,D> = AGL(1,64).* [Zenodo archive](https://doi.org/10.5281/zenodo.22731492).

That DOI links to the existing archived Singer-layer note. The general-article
preprint is available in `PaperA_scalar_realizations/`; this update does not
change the archived record.

## License

- Manuscript and supplementary PDFs: CC BY 4.0.
- Code: MIT License.

## Contact

Baohua Li · Independent Researcher · 707952331@qq.com
