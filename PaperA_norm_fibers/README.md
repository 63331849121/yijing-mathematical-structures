# Norm-fiber densities and relative traces in characteristic two

Wencong Huang; Baohua Li | research preprint | 2 November 2026

- [Main paper](main.pdf): 45 pages. [Supplement](supplement.pdf): 45 pages.
- [Version DOI](https://doi.org/10.5281/zenodo.23880175); [all versions](https://doi.org/10.5281/zenodo.23721669).
- [Pinned GitHub release](https://github.com/63331849121/yijing-mathematical-structures/releases/tag/paperN-v2026.11.02-v22).
- [Chinese reading guide](overview_zh.txt), [citation](CITATION.cff), [authorship correction](AUTHORS_CORRECTION.txt).
- [Editable LaTeX](LaTeX_sources.zip); [sources and verification](source_and_verification.zip).
- [Raw research data](https://github.com/63331849121/yijing-mathematical-structures/releases/download/paperN-v2026.11.02-v22/research_data.zip).
- [Retained selective Lean sources](Lean_verification.zip); [replay instructions](REPRODUCE.txt).
- [Checksums](SHA256SUMS.txt) and [licenses](LICENSES.txt).

This general revision adds complete support on prescribed primitive inner
norms for all s>=2, including composite t^2+1, and distribution results across
those norms. The latter include the exact Kloosterman formula, unsieved
variance, the cubic genus-two reduction, a mixed second moment excluding all
relevant rank-one Lang twists, and the refined 8M-12 full-order error.

The mixed constant is defined by a fixed conductor and is not numerically
evaluated. The full-order variance bound retains W(A)^2; it has no asserted
asymptotic main term. The old selective Lean scope is retained; no Lean proof
of these new geometric or all-parameter results is claimed. Internal
independent proof checks are not external journal peer review.

To reproduce, extract source_and_verification.zip and research_data.zip into
the same directory. The second archive supplies data_deposit/; it preserves
the earlier raw data. LaTeX_sources.zip is the smaller editable manuscript
package. Research sources exclude browser caches, internal review notes,
third-party research PDFs and historical rendered-page images.

Paper A is the earlier focused Singer note solely by Baohua Li (DOI
10.5281/zenodo.22731492). This norm-fiber article is Paper N, jointly by
Wencong Huang and Baohua Li. Its canonical directory is PaperN_norm_fibers/;
PaperA_norm_fibers/ is a compatibility path for earlier naming. See the
authorship note for the exact boundary.

The formal title omits internal version labels. Release metadata identifies
v22. Earlier Paper N DOI files and tags are preserved. The corrected historical
author metadata and current byline are explained in AUTHORS_CORRECTION.txt.
The distinct Singer note keeps its own citation and DOI. Manuscripts are
CC BY 4.0; code and Lean are MIT; fonts keep their supplied licenses.
