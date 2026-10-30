# Quadratic maps satisfying f ∘ f = f + id: polar Lie structure and sharp dimension bounds

Baohua Li · Preprint · 23 pages · 30 October 2026

- DOI: https://doi.org/10.5281/zenodo.23788043
- Fixed GitHub release: https://github.com/63331849121/yijing-mathematical-structures/releases/tag/paperG-v2026.10.30
- Manuscript: `PaperG_quadratic_polar_lie.pdf`
- Complete editable source and verification: `PaperG_source_and_verification.zip`

## Structure and results

The equation ties three-cycle orbits to additive binary planes. At binary degree
two, its polar form becomes a Lie bracket. This structure gives a complete
metabelian correspondence, sharp dimension costs at every nilpotency class,
and two closed classification ranges.

For metabelian solutions, the minimum binary dimensions are 6, 8 and 12 in
classes 2, 3 and 4, then `2^c + 2c - 6` for `c >= 5`. Compatibility of the
original polar bracket with its intrinsic F4-actions is characterized by an
explicit linear system. In that subclass the minimum is `2^c + 2c - 2` for
every `c >= 2`, and at least `c - 2` inequivalent extremizers occur for
every `c >= 4`.

There are three conjugacy classes in binary dimension eight. Solvable solutions
with binary abelianization dimension four form a complete seven-class chain
in dimensions 4 through 16; the final extension quotient vanishes.

## Read and reproduce

The source ZIP unpacks into `PaperG_quadratic_polar_lie/` and contains all
eleven LaTeX source files, verification inputs, programs and their recorded
exact outputs. Select `PaperG_quadratic_polar_lie.tex` as the main file in Overleaf, or run
pdfLaTeX on that entry two or three times. The manuscript PDF is distributed
separately and is byte-identical to the reviewed 23-page revision.

Verify the original source payload before rerunning any program:

```text
python verify_public_payload.py
cd verification
python check_chain_rank_certificates.py
python audit_metabelian_symbolic_interfaces.py
python manuscript_transcription_checks.py
```

Use Python 3. Only the first verification program requires SymPy; the others
use the standard library. All three replayed successfully for this release.
The seven extension ranks are 14, 30, 58, 92, 132, 184 and 244, with quotient
F4-dimensions 1, 2, 1, 1, 2, 1 and 0. The certificates verify both rank bounds.
The coordinate checker verifies the functional equation, intrinsic dimensions
and the two projective actions. General all-parameter results use the written
proofs in the paper. Replays may update generated JSON reports; keep a pristine
copy when checking the delivered hashes.

The public payload contains the manuscript, sources and mathematical
verification. Internal author checklists, local compiler diagnostics,
editing snapshots and third-party full texts are kept separately.

## Citation and licenses

Use the DOI above or `CITATION.cff`. Manuscript and original mathematical data
are CC BY 4.0; original verification programs retain MIT terms.
See `LICENSES.txt` and `LICENSE-code-MIT.txt`.
