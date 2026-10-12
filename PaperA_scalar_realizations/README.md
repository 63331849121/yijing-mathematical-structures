# Paper A: scalar realizations of affine companion groups

**Affine companion groups in characteristic two: scalar realizations and density**

This directory contains the generic `article`-class preprint, its compiled PDF,
synchronized English and Chinese abstracts, the proof/readiness audit, and the
finite computation package. The manuscript is the master source; no
journal-specific class or submission formatting is applied here.

- [PDF preprint](PaperA_revised.pdf)
- [LaTeX source](PaperA_revised.tex)
- [English abstract](abstract_en.txt) · [Chinese abstract](abstract_zh.txt)
- [Proof and readiness audit](PaperA_Preprint_Proof_and_Readiness_Audit_2026-10-12.md)
- [Reproduction guide](PaperA_REPRODUCIBILITY.md)
- [Research roadmap](Research_Roadmap.md)
- [PDF SHA-256](PaperA_pdf_sha256.txt)

## Reproduce the finite checks

Requires Python 3 and its standard library. From the repository root, run:

```text
python PaperA_scalar_realizations/reproduce_paperA.py
```

The driver checks the source-data manifest, runs the 13 supplied verifiers and
exporter, and checks the manifest again. The checks cover finite certificates
and computations. They do not replace the manuscript's proofs of uniform
statements. The driver does not build Lean; the supplied Lean files and their
scope are documented in the manuscript and reproduction guide.

The PDF was compiled from this directory's `PaperA_revised.tex` in two LaTeX
passes. It has 52 pages. Representative pages from the introduction, density
results, and appendices were visually checked after export.

## Scope and status

This is a general-article preprint, not a journal-formatted submission. Its
claims and novelty boundary are summarized in the proof/readiness audit. The
adjacent exact-order pair is identified as the standard primitive-pair object;
the manuscript's stated contribution is the norm-fiber density analysis, its
affine-companion interpretation, and the all-dimensional existence argument.
The audit is a scoped internal check, not an external referee report.
