Current selective Lean formalization, 28 October 2026

Read INTERFACE_SCOPE.txt before interpreting a successful build. The current
nine modules have 129 checked theorem/lemma declarations and 33 audited definitions; this is not full-paper formalization.

Minimal original six-lemma check (only the pinned Lean compiler is needed):
  python verify_lean.py

Full current interface check, with dependencies already installed:
  python verify_interfaces.py
To reuse an existing project with exactly the same nine dependency commits:
  python verify_interfaces.py --lake-project PATH_TO_PINNED_PROJECT
The --elan option may name the installed elan executable explicitly.

For a fresh environment, install Lean via elan, enter this folder and fetch
the dependencies described by lake-manifest.json using Lake. Typical commands:
  elan toolchain install leanprover/lean4:v4.31.0
  lake update
  lake exe cache get
  python verify_interfaces.py
These installation commands require network access and are not run automatically
by the verifier. The verifier rejects dependency/toolchain mismatches and tracked
dependency changes. It recompiles the local modules in a new scratch directory
and checks every theorem, lemma, definition and abbreviation for axiom dependencies. It does not trust old PASS
reports, nor use native_decide. interfaces_check.json and interfaces_check.log
record the actual current run. New installation/cache-free execution has not
been claimed or tested in this session.

The six original grid lemmas plus four cover branches have empty axiom audits.
The mathlib interfaces use only standard foundational axioms. They construct
the multiplicative exponent equivalence, the rational a/gamma bijection and
exact-order component equivalence. Named Algebra.norm/trace formulas transfer
the actual M_c count to the parameter and two-to-one support counts. Complete
classification, certificates and geometry remain excluded. Read INTERFACE_SCOPE.txt
for the actual field-tower hypotheses and remaining limits.

The three historical mathlib modules under provenance/original_repository/
are unchanged. Their previous independent rerun records remain separate; the
current interface verifier does not rerun or relabel them as current new work.
Machine checking, exact finite arithmetic and external peer review are separate
forms of evidence. No external human review or full formalization is claimed.
