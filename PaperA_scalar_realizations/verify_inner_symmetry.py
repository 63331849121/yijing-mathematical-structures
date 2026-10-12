"""Exact finite checks for the norm-fiber four-torsion and trace multiplier.

This reuses the audited field arithmetic, not the certificate finder. The
universal geometric identities have separate paper proofs; these checks cover
only the explicitly reported finite cases. No floating-point character sums
are used: invariance of their integer multiplicity distributions is checked.
"""
from collections import Counter, defaultdict
from math import gcd
from pathlib import Path
import json

from verify_inner_critical import check_primes, check_row

ROOT = Path(__file__).resolve().parent


def check_geometry(row, E, L):
    s = row['s']
    t, A, B = 1 << s, (1 << s) + 1, (1 << (2 * s)) + 1
    d = A * B
    one, a = (1, 0), (0, 1)
    b = (L.b, 0)
    u = (E.power(L.b, (A + 1) // 2), 0)
    mul, power = L.mul, L.power
    inv = lambda z: power(z, (1 << (4 * s)) - 2)
    div = lambda z, w: mul(z, inv(w))
    add = lambda z, w: (z[0] ^ w[0], z[1] ^ w[1])
    assert power(u, 2) == b and power(u, A) == one and power(u, B) == b
    x, y = a, power(a, t)
    rho_x, rho_y = inv(y), div(x, b)
    assert rho_y == power(rho_x, t)
    assert rho_x == power(a, (-t) % d)
    assert power(rho_x, B) == b
    assert power(add(one, rho_x), d) == one
    cycle = [a]
    for _ in range(3):
        cycle.append(power(cycle[-1], (-t) % d))
    assert len(set(cycle)) == 4
    assert power(cycle[-1], (-t) % d) == a
    assert all(power(z, d // p) != one
               for z in cycle for p in set(row['A_factors'] + row['B_factors']))
    product = mul(mul(add(x, one), add(x, b)),
                  mul(add(y, one), add(y, inv(b))))
    assert product == mul(x, y)
    # The split Frobenius fixes this K-point. Its action on the Lang fiber
    # is multiplication by x/u, which is an element of the constant kernel V.
    Fx, Fy = div(b, power(y, t)), power(x, t)
    assert (Fx, Fy) == (x, y)
    v = div(x, u)
    assert power(v, B) == one
    h = div(power(y, t), x)
    hF = div(power(Fy, t), Fx)
    assert hF == mul(power(v, B), h)
    h_rho = div(power(rho_y, t), rho_x)
    assert h_rho == mul(power(mul(u, y), B), inv(power(h, t)))
    rho2_x, rho2_y = div(b, x), div(inv(b), y)
    assert div(power(rho2_y, t), rho2_x) == inv(h)
    assert div(rho_x, u) == power(v, (-t) % B)
    return {'s': s, 'four_distinct_iterates': True,
            'rational_frobenius_and_deck_multiplier': True,
            'rho_kummer_identities': True, 'primitive_order_preserved': True}


def check_small_fibers(row, E, L, expected):
    s = row['s']
    t, A, B = 1 << s, (1 << s) + 1, (1 << (2 * s)) + 1
    d, n = A * B, E.n
    x, y, logs = 1, 0, {}
    for j in range(d):
        packed = x | (y << n)
        assert packed not in logs
        logs[packed] = j
        x, y = E.mul(L.b, y), x ^ E.mul(L.c, y)
    assert (x, y) == (1, 0)
    candidates = {j for packed, j in logs.items()
                  if packed ^ 1 in logs and gcd(j, A) == 1}
    fibers, prim, distribution = Counter(), Counter(), defaultdict(Counter)
    inverse_two = pow(2, -1, A)
    for j in candidates:
        jj = (-t * j) % d
        assert jj in candidates and j % A == jj % A
        orbit = {j, jj, (t * t * j) % d, (-t * t * t * j) % d}
        assert len(orbit) == 4 and all(z in candidates for z in orbit)
        assert gcd(j, d) == gcd(jj, d)
        norm_index = j % A
        fibers[norm_index] += 1
        prim[norm_index] += int(gcd(j, d) == 1)
        u_exponent = (B * inverse_two * norm_index) % d
        v_exponent = (j - u_exponent) % d
        assert v_exponent % A == 0
        distribution[norm_index][v_exponent // A] += 1
    assert sum(prim.values()) == expected['primitive_slope_count']
    assert len(fibers) == sum(gcd(j, A) == 1 for j in range(A))
    for norm_index, count in fibers.items():
        assert count % 4 == prim[norm_index] % 4 == 0
        freq = distribution[norm_index]
        assert Counter({(-t * j) % B: m for j, m in freq.items()}) == freq
        assert Counter({(-j) % B: m for j, m in freq.items()}) == freq
    # These are all nontrivial characters of the cyclic group V, represented
    # by their exact integer exponent modulo B, including imprimitive ones.
    for k in range(1, B):
        assert len({k, (-t * k) % B, (-k) % B, (t * k) % B}) == 4
    return {'s': s, 'primitive_norm_fibers_checked': len(fibers),
            'candidate_points_checked': len(candidates),
            'primitive_points_checked': sum(prim.values()),
            'all_four_cycles_free': True,
            'all_fiber_and_primitive_counts_divisible_by_four': True,
            'integer_character_distributions_invariant': True,
            'nontrivial_character_orbits_checked': (B - 1) // 4,
            'fiber_counts': {str(k): [fibers[k], prim[k]] for k in sorted(fibers)}}


def main():
    if not __debug__:
        raise RuntimeError('Use ordinary Python without -O.')
    data = json.loads((ROOT / 'inner_critical_certificates.json').read_text(encoding='utf-8'))
    assert data['range'] == [2, 32]
    assert [r['s'] for r in data['certificates']] == list(range(2, 33))
    previous = json.loads((ROOT / 'inner_critical_verification.json').read_text(encoding='utf-8'))
    small_expected = {r['s']: r for r in previous['exact_small_counts']}
    prove = check_primes(data['prime_certificates'])
    geometry, fibers = [], []
    for row in data['certificates']:
        E, L = check_row(row, prove)
        geometry.append(check_geometry(row, E, L))
        if row['s'] <= 6:
            fibers.append(check_small_fibers(row, E, L, small_expected[row['s']]))
        print(f"s={row['s']}: four-torsion identities and Lang fiber multiplier verified.", flush=True)
    result = {'certificate_geometry_range': [2, 32],
              'number_of_certificate_points_checked': 31,
              'exhaustive_primitive_norm_fiber_range': [2, 6],
              'certificate_geometry': geometry, 'small_fibers': fibers}
    output = ROOT / 'inner_symmetry_verification.json'
    if output.exists():
        assert json.loads(output.read_text(encoding='utf-8')) == result
    else:
        output.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print('Verified four-torsion / trace identities for s=2..32 and complete primitive-norm fibers for s=2..6.')
    print(json.dumps([{k: v for k, v in r.items() if k != 'fiber_counts'} for r in fibers]))


if __name__ == '__main__':
    main()
