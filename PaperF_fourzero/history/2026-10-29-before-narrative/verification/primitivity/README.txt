Install python-flint==0.9.0 in a local Python environment.
From the Paper F root directory run:
python verification/primitivity/verify_primitivity.py --data verification/primitivity/inputs --out audit_rerun
The optional --deps argument points to a directory containing an installed python-flint package.
The preserved historical inputs reproduce the 16 auxiliary-field corrections.
The corrected current count JSON is at the Paper F root. Counts and primary first pairs are unchanged.
The verifier uses FLINT rigorous integer primality decisions, not probable-prime status alone.
It exports factor multiplicities and modular order residues, not standalone prime certificates or Lean proofs.
