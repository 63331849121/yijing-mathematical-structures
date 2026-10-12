"""Regenerate Paper A's machine-readable coordinate and PTE data.

Python 3.12, standard library only. This reuses the original verifiers;
it is an export routine, not a separate independent arithmetic implementation.
Run from any directory: python export_paperA_data.py
"""

from collections import Counter
from contextlib import redirect_stdout
import csv
import io
from itertools import permutations
import json
from pathlib import Path
import runpy


def main():
    folder = Path(__file__).resolve().parent
    capture = io.StringIO()
    with redirect_stdout(capture):
        structural = runpy.run_path(str(folder / 'verify_paperA_structure.py'))
    assert capture.getvalue().rstrip().endswith('All structural checks passed.')
    (folder / 'structural_results.json').write_text(
        json.dumps(structural['result'], indent=2) + '\n', encoding='utf-8')

    triple = structural['triple']
    cycles = structural['cycles']
    basis = (63, 33, 18, 49, 1, 21)
    t, d, kmap = triple(basis)
    with (folder / 'TDK_values_64.csv').open('w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['x', 'T_x', 'D_x', 'K_x'])
        writer.writerows((x, t[x], d[x], kmap[x]) for x in range(64))

    stats = Counter()
    with (folder / 'basis_orderings_720.csv').open('w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['index', 'g1', 'g2', 'g3', 'g4', 'g5', 'g6',
                         'D_defined', 'K_defined', 'T_cycles', 'D_cycles', 'K_cycles',
                         'T_fixed', 'D_fixed', 'K_fixed', 'exact_Singer_triple'])
        for index, ordering in enumerate(permutations(basis), 1):
            t, d, kmap = triple(ordering)
            defined = d is not None
            exact = (defined and kmap is not None and cycles(t) == [1, 63]
                     and cycles(d) == [1, 63] and cycles(kmap) == [1] + [9]*7)
            stats['D_defined' if defined else 'D_undefined'] += 1
            if defined and cycles(t) == [1, 63]:
                stats['T_Singer_and_D_defined'] += 1
            if exact:
                stats['exact_triple'] += 1
            maps = (t, d, kmap)
            cycle_fields = ['' if p is None else json.dumps(cycles(p)) for p in maps]
            fixed_fields = ['' if p is None else json.dumps(
                [x for x, value in enumerate(p) if x == value]) for p in maps]
            writer.writerow([index, *ordering, int(defined), int(kmap is not None),
                             *cycle_fields, *fixed_fields, int(exact)])
    assert stats == dict(D_undefined=572, D_defined=148,
                         T_Singer_and_D_defined=54, exact_triple=9)

    certificate = runpy.run_path(str(folder / 'verify_k1_29.py'))
    rows = []
    for k in range(1, 30):
        modulus, a, prime_count = certificate['verify_one'](k)
        rows.append(dict(k=k, field_modulus_hex=hex(modulus), a_hex=hex(a),
                         extension_polynomial='t^2+t+a', root=[0, 1],
                         relative_trace=1, exact_order=2**(2*k)-1,
                         factorization=certificate['FACTORS'][k],
                         distinct_prime_count=prime_count))
    (folder / 'pte_certificates_k1_29.json').write_text(
        json.dumps(dict(encoding='binary polynomial coefficients, low bit constant term',
                        verified=True, certificates=rows), indent=2) + '\n', encoding='utf-8')
    print('All structural checks passed.')
    print('All certificates verified.')
    print('Exported 64 coordinate rows, 720 basis orderings, and 29 PTE certificates.')


if __name__ == '__main__':
    main()
