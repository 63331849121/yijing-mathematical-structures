# Norm-fiber densities and relative traces in characteristic two

**Baohua Li · preprint · version 2026-10-26**

- [Main paper](main.pdf), 40 pages.
- [Supplementary results](supplement.pdf), 36 pages.
- [Chinese visual overview](overview_zh.pdf), 22 pages.
- [Chinese text overview](overview_zh.txt).
- [Complete editable sources, exact certificates and verification records](source_and_verification.zip).
- [Citation metadata](CITATION.cff), [file checksums](SHA256SUMS.txt),
  and [timestamp verification notes](TIMESTAMP.txt).

The main paper studies linked elements in the binary quartic norm kernel,
joint-generation and individual exact-order densities, uniform relative
traces on the whole intermediate field, and the complete exceptional trace
groups C9 at t=8 and C11 at t=32. It also gives cyclic-convolution distribution
formulas, norm transfer, a general affine companion-group formula, and the
uniform index exponent 1/4 with a remaining logarithmic gap.

The supplement gives coordinate Singer constructions, oriented spreads,
an explicit nonlinear companion pair generating A16, further exact-order
statistics, and detailed comparisons with earlier results.

## Sources and reproducibility

Extract `source_and_verification.zip`. The directory
`PaperA_restructured_2026-10-26/` contains `main.tex`, `supplement.tex`,
the split section sources, `build.py`, `verification/`, `formalization/`,
and retained provenance. Build both mutually referencing PDFs with
`python build.py` from that directory, using a current TeX Live or MiKTeX.
The source archive's `PUBLICATION_CONTENTS.json` checks every packaged entry.

Main Appendix C and Supplementary Appendix S.B identify the exact verifiers
and their coverage. The current support reduction uses 755 representative
witnesses and 731 support-separation witnesses in its finite proof range.
Infinite ranges depend on mathematical proofs, not finite extrapolation.

For the new dependency-free Lean module, with the pinned Lean 4.31.0 toolchain
already installed, run `python formalization/verify_lean.py` from the project
directory. Six combinatorial lemmas have been checked; the geometric
estimates and the complete statements of Theorems 5.1 and 5.4 are not wholly
formalized. Three archived Lean source files were separately rerun against
their pinned dependencies; the fresh checks and precise scope are retained.

The editable visual-overview source and its rendering checks are in
`visual_overview/` inside the archive. Its renderer uses ReportLab and
Microsoft YaHei/Cambria fonts on Windows; system font files are not distributed.

## Version and citation

Release tag: `paperA-v2026.10.26`. The [release page](https://github.com/63331849121/yijing-mathematical-structures/releases/tag/paperA-v2026.10.26) identifies
the fixed Git commit and its publication time. `SHA256SUMS.txt` identifies the
exact downloadable bytes. A detached OpenTimestamps receipt, if present,
commits this checksum file; see `TIMESTAMP.txt` for pending/confirmed states.

The existing DOI `10.5281/zenodo.22731492` identifies the earlier Singer-layer
note. It is not assigned to this expanded main paper or this release.
Use the current title, version, author and release URL until a distinct
archival DOI is issued. The existing Paper F DOI is also unchanged.

## Research status and licensing

This is a research preprint with documented exact checks and scoped
formalization; it has not been externally peer reviewed. Counting objects
and general tools have classical predecessors. The paper states the specific
effective estimates and classifications it establishes, without an absolute
global-priority claim. See the introduction, Section 7 and Appendix D.

Manuscript/overview material is CC BY 4.0, code is MIT, and the bundled
font retains its separate license. See [license details](LICENSES.txt).
