# Paper Q: structure and quadratic realization

Paper Q / version 2026-11-02.2 / 73 pages
Wencong Huang, Baohua Li
============================================================
Entry: PaperG_structure.tex. Read PaperG_structure.pdf.
Version DOI: https://doi.org/10.5281/zenodo.23882876
Fixed release: https://github.com/63331849121/yijing-mathematical-structures/releases/tag/paperQ-v2026.11.02.2
The 65-page baseline DOI 10.5281/zenodo.23874202 retains its original
authorship (Baohua Li) and files. The pre-publication 73-page local version
is also preserved separately. This release adds no mathematical change
to the reviewed 73-page integration; its title-page author/date and PDF
author metadata are updated.

Sections 11 and 13 and Appendix J contain exact central repair, half-weight
constraints, the arbitrary-tower sharp first-ascent cost over S_r, the full
F4 rank-four exception and optimal preparation. The cost is relative to the
specified bottom, not a global value of m(5). Equality uniqueness means an
extension isomorphism class over a fixed bottom, not a canonical map.

Build with a standard XeLaTeX distribution (two runs), or build.ps1. All
used TeX, fonts and verification inputs are local. No other paper or the
frozen 209-page collection is required. The author-specific offline cache
and build_offline.ps1 are excluded from the portable ZIP.

python -m pip install -r verification/requirements.txt
python -B -X utf8 verification/run_replay.py --group merge-review --output-dir replay_new
Use a new output directory. Add --temp-root with a short writable absolute
path if the system temporary directory is restricted. The targeted group
contains six invocations; all contains seven inherited plus five new tasks.
Exact scope, proof/certificate map and earlier fresh reports are in
verification/README.txt, central_repair/README.txt and INTEGRATION_REPORT.zh-CN.txt.
Finite computations complement the general written proofs.

Third-round class-six notes are deferred local research, outside the
article and this deposit. They do not enter the abstract or prove the
manuscript's main assertions. C/E are background comparisons, not new proof
inputs. e(d)-1 <= kappa(d) <= e(d) is retained.

Manuscript and original mathematical data: CC BY 4.0. Original verification
code: MIT. Bundled third-party assets retain their own licenses.
manifest.json fingerprints all portable files except itself.
