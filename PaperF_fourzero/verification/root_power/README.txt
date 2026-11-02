Root-power classification: complete finite proof materials
=========================================================

These files accompany Section 4 and Appendix B of the local 2 November
2026 revision of Paper F. Here n=2k>=6 and 1<=i<j<k. No irreducibility
or squarefreeness is assumed in the cubic or quintic classification.

Required checks, using Python 3.10+ and its standard library only:

  python check_cubic_formal.py
  python check_quintic_classification.py
  python check_quintic_branches.py
  python check_certificate_lattice.py

Required input certificates:
  cubic_certificate.json
  quintic_classification_certificate.json

The cubic checker reconstructs the norm over F2, verifies the parameter
partition and all 768 uncancellable-term comparisons. The 42 terminal
regions comprise 41 unbounded regions and one point (n,i,j)=(10,1,2).
cubic_leaf_table.json is a readable auxiliary table; the checker derives
the partition from the complete certificate.

The quintic classification checker reconstructs the support by a circulant
determinant and tests nonnegative integer feasibility by exact arithmetic.
It verifies all 125 residue classes, 672 nodes and 28611 partner checks.
Every feasible zero-defect input is in the stated progression or is the
isolated degree-10 exception. The accepting regions need not be disjoint.

Do not use Python -O or -OO: all four checkers reject optimized mode.

The branch checker proves sufficiency by symbolic affine supports in a free
integer parameter, verifies the compact floor formula (24), the exact
zero counts and the factor identity. It also checks both small irreducible
inputs and their exact orders. Its 250 numerical substitutions are separate
implementation controls and do not justify the all-degree conclusions.
It imports the independent classification checker for arithmetic helpers;
neither checker imports the certificate generator.

Each program writes a *_receipt.json file. The supplied *.log files record
successful runs. The floor-formula and free-parameter factor checks are
additions to the branch checker; archived research-round originals are unchanged.

The independent lattice checker derives the feedback polynomial from the
four deleted positions and computes the norm as the determinant of
multiplication by P in F2[Y,z]/(z^ell+Y). It uses subset dynamic programming,
not the cyclic norm form. It reconstructs all integral solution lattices
by unimodular Bezout column operations, uses Apery semigroup distances at
rank one and integer interval bounds at rank two, and verifies all cubic
regions and quintic collision nodes without importing the other programs.

Optional certificate reconstruction, not needed to check the proof:
  python quintic_support.py
  python build_quintic_classification.py
Then rerun the two quintic checkers. Generation uses F16 products and
Gaussian elimination, whereas verification uses F2 determinants and
Cramer parametrization. No SMT solver is required for either final check.

quintic_support_diagnosis.json records the generator's initial regions.
All mathematical data and reports are covered by the root LICENSES.txt;
the original verification code is covered by LICENSE-code-MIT.txt.
