# Yijing Mathematical Structures

Independent research on finite-field, combinatorial, and affine structures inspired by the Yijing.

## Current preprints

### Paper A: norm-fiber densities and relative traces

**Norm-fiber densities and relative traces in characteristic two** · Wencong Huang, Baohua Li · **2 November 2026**

Effective norm-fiber densities, complete support at every prescribed primitive
inner norm (including composite t^2+1), Kloosterman moments, a genus-two cubic
sieve coordinate and its Lang-twisted mixed second moment. Uniform relative
traces and the complete C9/C11 classification remain central. The main paper
has 44 pages and the supplement 45 pages. The full-order variance retains
W(A)^2; its asymptotic main term is not asserted. The fixed conductor constant
is not numerically evaluated. The retained selective Lean scope is unchanged.

- [Main paper](PaperA_norm_fibers/main.pdf) / [supplement](PaperA_norm_fibers/supplement.pdf).
- [Sources, certificates, reproduction and precise scope](PaperA_norm_fibers/).
- [Chinese reading guide](PaperA_norm_fibers/overview_zh.txt).
- [Pinned release](https://github.com/63331849121/yijing-mathematical-structures/releases/tag/paperA-v2026.11.02-v22) / [version DOI](https://doi.org/10.5281/zenodo.23880175).
- [Authorship correction and historical record](PaperA_norm_fibers/AUTHORS_CORRECTION.txt).

v22 is an archive identifier and is omitted from the formal title. Wencong
Huang contributed to the earlier versions and was omitted from their bylines;
the same Paper A DOI chain has corrected creator metadata. Historical PDFs,
archives and tags are preserved. Earlier scalar-realization sources, the old
graphical overview and TIMESTAMP.txt are dated historical artifacts; the
current text guide and SHA256SUMS.txt describe this revision. The separate
Singer note below retains its own record.

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

Complete quadratic-transform support classifications, a uniform translation
obstruction, an exact reciprocal screen, and an explicit B-family descent
(Proposition 3.5). The general primitive-existence conjecture C4 remains open.

- [Manuscript and editable source](PaperF_fourzero/).
- [Submission archive: PDF and TeX](PaperF_fourzero/PaperF_submission.zip).
- [Optional mathematical data and verification programs](PaperF_fourzero/PaperF_data_and_code.zip).
- [Version DOI](https://doi.org/10.5281/zenodo.23766722).
- [Fixed GitHub release](https://github.com/63331849121/yijing-mathematical-structures/releases/tag/paperF-v2026.10.29-r1).
- [Previous public version](https://doi.org/10.5281/zenodo.23764251), preserved.

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

Current Paper A: Huang, Wencong, and Li, Baohua. (2026). *Norm-fiber densities and relative traces in characteristic two*. Zenodo. [10.5281/zenodo.23880175](https://doi.org/10.5281/zenodo.23880175).

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

## Paper G: quadratic maps and polar Lie structure

[23-page preprint and reproducible verification](PaperG_quadratic_polar_lie/) on quadratic solutions of `f composed with f = f + id`: a complete metabelian correspondence, all-class sharp dimension bounds, and two closed classifications.

DOI: https://doi.org/10.5281/zenodo.23788043  
Fixed release: https://github.com/63331849121/yijing-mathematical-structures/releases/tag/paperG-v2026.10.30


## Current Paper G and Paper S

- [Paper G: 186-page manuscript and source](PaperG_quadratic_polar_lie/revisions/2026-11-01/)
- [Paper S: 56-page manuscript and source, updated 2 November 2026](PaperS_ideal_growth/)

These are connected independent papers; previous tagged editions remain available.

Zenodo current editions: [Paper G](https://doi.org/10.5281/zenodo.23852642) · [Paper S](https://doi.org/10.5281/zenodo.23873752).

## Frozen Paper G and independent Papers Q, E and C — 2 November 2026

- [Paper G: 209-page manuscript, source and verification](PaperG_quadratic_polar_lie/revisions/2026-11-02/) — [DOI](https://doi.org/10.5281/zenodo.23874173)
- [Paper Q: 65-page manuscript, source and verification](PaperQ_quadratic_orbit_maps/) — [DOI](https://doi.org/10.5281/zenodo.23874202)
- [Paper E: 80-page manuscript, source and verification](PaperE_extremal_growth/) — [DOI](https://doi.org/10.5281/zenodo.23874228)
- [Paper C: 28-page manuscript, source and verification](PaperC_central_depth/) — [DOI](https://doi.org/10.5281/zenodo.23874234)

G is the frozen unified collection. Q, E and C are independently readable manuscripts with separate questions and explicitly attributed shared foundations. [Version and contribution index](PaperG_research_collection_index.md). Paper S continues independently.
