# Yijing Mathematical Structures

Independent research on finite-field, combinatorial, and affine structures inspired by the Yijing.

## Current preprints

### Paper A: affine Singer layers and the (T,D,K) triple

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

- [Paper A PDF](PaperA_singer_TDK.pdf)
- [LaTeX source](PaperA_singer_TDK.tex)
- [English abstract](abstract_en.txt) / [Chinese abstract](abstract_zh.txt)

### Paper F: four-zero tail-palindromic primitive polynomials

**Four-zero tail-palindromic primitive polynomials: coefficient geometry,
Dickson reduction, and computational evidence.**

This preprint studies four-zero tail-palindromic candidates over F2, their
self-paired coefficient geometry, the uniform Dickson/tau reduction,
finite-pair association statistics for n=2p, and computational evidence.

[Paper F archive](https://doi.org/10.5281/zenodo.22745836) · [Files and data](PaperF_fourzero/)

## Reproduce Paper A's computations

Requires Python 3 and its standard library only.

```text
python verify_paperA_structure.py
python verify_k1_29.py
```

Expected final lines:

```text
All structural checks passed.
All certificates verified.
```

The first script independently checks the four displayed bases, exact finite
group orders, characteristic polynomials, all 720 basis orderings, the
tau-collapse examples, scalar-affine F-orbits over F64, and CRT indexing.
The second verifies every finite certificate for k=1,...,29 used in Appendix B.
These computations do not replace the paper proof for all k.
The existing Lean formalization covers the group-generation argument; the
analytic PTE proof and finite certificate are not Lean-formalized.

## Repository contents

- `PaperA_singer_TDK.pdf` and `.tex`: current Paper A preprint.
- `abstract_en.txt`, `abstract_zh.txt`: synchronized abstracts.
- `verify_paperA_structure.py`: finite structural checks.
- `verify_k1_29.py`: deterministic finite PTE certificate verifier.
- `PaperA_revision_notes.md`: review corrections and verification record.
- `PaperD_primitive_trace_even_detailed_supplement.pdf`, `.tex`, and
  `detailed_proof_body.tex`: detailed proof archive.
- `PaperF_fourzero/`: Paper F preprint, reproducibility scripts, and data tables.

## Scope

This repository records a broader independent study of mathematical structures
inspired by the Yijing. The mathematical papers and programs are self-contained.

## Citation

Li, Baohua. (2026). *An affine Singer layer on F2^6, its (T,D,K) triple,
and <T,D> = AGL(1,64).* [Zenodo archive](https://doi.org/10.5281/zenodo.22731492).

The DOI links to the existing archived record. The October 11 revision is
available in this repository; this update does not change the archived record.

## License

- Manuscript and supplementary PDFs: CC BY 4.0.
- Code: MIT License.

## Contact

Baohua Li · Independent Researcher · 707952331@qq.com
