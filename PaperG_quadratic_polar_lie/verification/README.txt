Exact verification files for the manuscript
===========================================

Requirements: Python 3 and SymPy. Only the rank-certificate checker requires
SymPy. The other two programs use the Python standard library.

Run from this directory:

  python check_chain_rank_certificates.py
  python audit_metabelian_symbolic_interfaces.py
  python manuscript_transcription_checks.py

All three should report PASS. They write their exact results in JSON files
in this directory (or in chain_rank_certificates for the first checker).

The seven central-extension equation ranks are:
  n = 4, 6, 8, 10, 12, 14, 16
  ranks = 14, 30, 58, 92, 132, 184, 244
  quotient F4 dimensions = 1, 2, 1, 1, 2, 1, 0.

The manifest authenticates the seven original input certificates by SHA-256.
The first program independently rebuilds every equation from the stored map,
checks the full degree-four kernel, and proves both bounds on every rank.
It imports no certificate-generator code.

The second program checks the scalar-weight elimination, inverse factors in
the morphism formula, the scalar-lift shear conventions, and leading-degree
independence for the reduced monomial interfaces.

The third program ties the displayed seven-coordinate formula to all seven
certificates, checks the functional equation by exact degree-four recovery,
recomputes all reported lower central and center dimensions, and checks the
explicit automorphisms and projective actions in the two two-dimensional
extension quotients. Its low-weight points are exhaustive for the stated
degree bounds; they are not random samples.

These programs are exact algebraic controls. The general all-parameter
proofs are in the manuscript. No Lean formalization is claimed.
