Translation-branch audit, 29 October 2026

Current written results: PaperF_fourzero.tex Lemma 3.5, Proposition 3.6,
Theorem 3.7 and Corollary 3.8. All-degree validity relies on the proofs.
proof_review.txt: independent mathematical review.
manuscript_review.txt: review of the final source and correction checks.
literature_review.txt: exact classical coverage and remaining access limits.
verify_translation.py: portable Python 3.10+ standard-library verifier.
audit_summary.json: bounded computational output, scope and exact factors.
Run: python verification/translation/verify_translation.py --out audit_rerun_translation
The script refuses -O because its checks use assertions.
compile_report.json, compile_pass1/2.txt and desktop_compile_result.json:
current final-source compilation records. 13 rendered pages were checked.

Files prefixed exploration_ preserve the pre-integration research record;
their historical statements that the manuscript was not yet modified,
and their historical source hashes, refer to that earlier stage.
The four-zero and general-tail computations are diagnostics, not Lean
proofs. The embedded factors were found in an earlier FLINT calculation;
this portable run independently checks irreducibility certificates and
exact products. It does not invoke a factorization library.


Same-day primary-source supplement: agou_original/ contains the completed
Agou 1977 original-text audit. Earlier missing-full-text statements in
dated reviews describe the earlier stage and are superseded by this
supplement. The third-party original PDF is kept privately in the research
workspace and is not bundled in the distributable paper package.
