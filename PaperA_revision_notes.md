# Paper A revision — October 11, 2026

Title: *An affine Singer layer on F2^6, its (T,D,K) triple, and <T,D> = AGL(1,64)*

## Corrections

1. **Theorem 6.3:** take alpha=beta directly from the prescribed-trace primitive element. The identity beta^q=1+beta gives both primitive slopes; kappa=beta^(q-1) has order q+1. In the tau-collapse remark, gamma belongs to the norm-one subgroup of the extension, while tau belongs to the subfield.
2. **Proposition 7.1:** classify F-orbits on the Q(Q-2) scalar affine maps over Q=2^(2k): two fixed maps and (Q(Q-2)-2)/3 three-element orbits. For nonzero constant term, all orbits have length three.
3. **CRT:** define theta(j)=T^j(63). CRT applies to iteration exponents; labels 63 and 0 correspond to exponents 0 and 62, respectively.
4. **Contribution and references:** describe the explicit coordinate realization and unified affine presentation; add Cohen--Presern (2005) and retain full attribution of the classical existence theorem and character-sum approach.
5. **Self-contained details:** add the irreducibility and exact-order certificate for p_T; extend multiplicative characters by chi(0)=0 and account for the zero-trace fiber; clarify the Fourier character index.
6. **Presentation:** correct the Appendix B equation tag to B.1, fix the revision date, hide hyperlink borders, and keep the tau-data heading with its table.
7. **Synchronization:** update English and Chinese abstracts, local submission forms, metadata, proof ledger, and core proof note. The main theorem numbers remain 6.2 and 6.3; Proposition 7.1 is added. The PDF is now 10 pages.

## Verification

- Final LaTeX source compiled in two passes. The final log contains no LaTeX warnings, undefined references, overfull boxes, or underfull boxes.
- All 10 rendered PDF pages were visually inspected; no clipping or overlapping content was found.
- English and Chinese abstract blocks match their local submission forms exactly.
- The 29 certificate rows extracted from the final PDF match the verifier's data.
- `python verify_k1_29.py`: all 29 certificates passed.
- `python verify_paperA_structure.py`: all structural checks passed, including group orders 12, 240, 4032, 65280; the 720-ordering counts 572, 148, 54, 9; and the F64 counts 3968 maps, two fixed maps, 1322 three-element orbits.
- The finite-certificate verifier is unchanged. Its SHA-256 is `042CE7F74EDFF13ADE5C6285E42CB3D15491FC25C65B99BC670D256047EE8D9F`.
- The full Lean project was not rebuilt for this revision. The analytic PTE proof and finite certificate remain outside the stated Lean formalization scope.

The corrections preserve the principal existence and group-generation results. This revision addresses the mathematical and presentation issues in the October 11 review and is ready as an updated preprint. The contribution statement does not assert a new prescribed-trace existence theorem.

## Archive status

The existing Zenodo DOI, 10.5281/zenodo.22731492, identifies the previously archived record. This revision updates GitHub and the author's local submission package; it does not update Zenodo, arXiv, or ChinaXiv platform records.
