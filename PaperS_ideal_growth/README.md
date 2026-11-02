# Sharp ideal growth of metabelian restricted Lie algebras

Baohua Li. Preprint, **56 pages**. Version **2026-11-02**.

- [Manuscript](PaperS.pdf)
- [Editable LaTeX, exact verification, and reading guide](PaperS_draft_and_source.zip)
- Version DOI: https://doi.org/10.5281/zenodo.23873752
- All-version DOI: https://doi.org/10.5281/zenodo.23852660
- Fixed GitHub release: https://github.com/63331849121/yijing-mathematical-structures/releases/tag/paperS-v2026.11.02
- Previous public version: https://doi.org/10.5281/zenodo.23852662

## Results in this revision

Sharp fixed-rank growth and the rank-two logarithmic correction; typical
restricted quotient layers and classical Hall partition laws; matching
whole-p-nilpotence rarity through six generators and conditional ordinary
nilpotence failure exponents in ranks three through six.

The new proofs combine Betti-controlled generator-weighted extension
packets, near-extremal shadows and filtered tails, and adaptive polynomial
graph planes over the original finite field. An all-rank small-away
sector is included; the remaining higher-rank large-away comparison is open.

Fine probability laws use uniform ideals. Coarse isomorphism-type growth
does not by itself imply the same fine uniform-type probabilities.

## Source and verification

The archive has main entry `PaperS/PaperS.tex`. Use a standard TeX
distribution, for example `latexmk -xelatex PaperS.tex` inside `PaperS/`.
Run `python verification/run_new_results.py --output-dir NEW_EMPTY_DIRECTORY`
inside that directory to replay the ten selected checks; `--adaptive-only`
runs the five new entry points. Fresh reports and detailed coverage are supplied.
The full earlier verification suite was not rerun in this revision.

This is a manuscript/source snapshot for the version above. Publication
receipts beside this archive record the server checksums after upload.
Independent professional review and a focused priority audit of the new
tools remain pending; no proof-assistant certification is claimed.

Manuscript and original mathematical data: CC BY 4.0. Original verification
code: MIT. Bundled third-party font assets retain their own licenses.
