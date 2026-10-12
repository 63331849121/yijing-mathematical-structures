"""Reproduce Paper A's finite computations from the standard library.

Run with ordinary Python (without -O): python reproduce_paperA.py
The manifest covers this revised source, its verifiers, data, and Lean inputs.
"""

from pathlib import Path
import hashlib
import json
import subprocess
import sys


ROOT = Path(__file__).resolve().parent
MANIFEST = ROOT / 'PaperA_revised_sha256.json'
REVISION = 'paperA-general-preprint-2026-10-12-proof-audit'
CHECKS = (
    ('verify_inner_double_all.py', 'All finite ranges of the double-order closure proof verified.'),
    ('verify_inner_mixed.py', 'Verified double-order certificates for s=2..32 and all norm fibers for s=2..6.'),
    ('verify_inner_symmetry.py', 'Verified four-torsion / trace identities for s=2..32 and complete primitive-norm fibers for s=2..6.'),
    ('verify_inner_critical.py', 'Verified all 31 cases; independent subgroup / polynomial-gcd counts agree for s=2..6.'),
    ('verify_scalar_depth.py', 'All scalar-depth certificates passed.'),
    ('verify_scalar_realization.py',
     'All scalar-realization certificates passed.'),
    ('verify_standard_spread_orbits.py',
     'All standard-spread orbit computations passed.'),
    ('verify_nonlinear_companions.py',
     'All nonlinear-companion certificates passed.'),
    ('verify_paperA_structure.py', 'All structural checks passed.'),
    ('verify_k1_29.py', 'All certificates verified.'),
    ('verify_complete_mapping_orbits.py',
     'All complete-mapping checks passed.'),
    ('verify_affine_groups_and_conjugacy.py',
     'All affine-group and conjugacy checks passed.'),
    ('export_paperA_data.py',
     'Exported 64 coordinate rows, 720 basis orderings, and 29 PTE certificates.'),
)


def check_hashes():
    manifest = json.loads(MANIFEST.read_text(encoding='utf-8'))
    if manifest['revision'] != REVISION:
        raise ValueError(f'Expected the {REVISION} manifest.')
    for name, expected in manifest['files'].items():
        path = (ROOT / name).resolve()
        if not path.is_relative_to(ROOT):
            raise ValueError(f'Path escapes the ancillary directory: {name}')
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual != expected:
            raise ValueError(f'SHA-256 mismatch: {name}')
    return len(manifest['files'])


def main():
    if not __debug__:
        raise RuntimeError('Use ordinary Python without -O; checks require assertions.')
    count = check_hashes()
    print(f'Checked SHA-256 for {count} source and ancillary files.', flush=True)
    for name, final_message in CHECKS:
        print(f'Running {name} ...', flush=True)
        run = subprocess.run([sys.executable, str(ROOT / name)], cwd=ROOT,
                             capture_output=True, text=True,
                             encoding='utf-8', errors='replace')
        if run.returncode != 0 or final_message not in run.stdout:
            raise RuntimeError(f'{name} failed.\n{run.stdout}\n{run.stderr}')
        print(final_message, flush=True)
    check_hashes()
    print('All finite computations reproduced; regenerated data match the manifest.')
    print('Lean sources are supplied separately; no Lean build is run by this driver.')


if __name__ == '__main__':
    main()
