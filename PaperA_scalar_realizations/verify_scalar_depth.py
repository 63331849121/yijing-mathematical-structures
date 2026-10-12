"""Finite arithmetic certificates for the quantitative and norm-descent results.

These checks audit explicitly stated finite ranges. General results use the
manuscript's paper proofs, not extrapolation from this file.
"""

from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from math import gcd, prod
from pathlib import Path
import json

from verify_scalar_realization import (
    MODULI, check_irreducible, divisors, field_logs, intersection_degree,
    multiply, polynomial_gcd, power, prime_factors, squarefree_products,
    translated_power,
)


ROOT = Path(__file__).resolve().parent


@lru_cache(None)
def intersection_polynomial(e):
    return polynomial_gcd((1 << e) ^ 1, translated_power(e) ^ 1)


@lru_cache(None)
def T(e):
    return intersection_polynomial(e).bit_length() - 1


def R(d):
    return sum(sign * T(d // h)
               for h, sign in squarefree_products(prime_factors(d)))


def binary_product(a, b):
    out = 0
    while b:
        if b & 1:
            out ^= a
        a <<= 1
        b >>= 1
    return out


def exact_quotient(a, b):
    quotient = 0
    while a and a.bit_length() >= b.bit_length():
        shift = a.bit_length() - b.bit_length()
        quotient ^= 1 << shift
        a ^= b << shift
    assert a == 0, 'Polynomial division was not exact.'
    return quotient


def realization_polynomial(d):
    # All G_e are squarefree. The lcm encodes the union of maximal
    # subgroup root sets, so division retains exactly joint generators.
    union = 1
    for p in prime_factors(d):
        g = intersection_polynomial(d // p)
        union = binary_product(exact_quotient(union, polynomial_gcd(union, g)), g)
    return exact_quotient(intersection_polynomial(d), union)


def order_two(d):
    a, n = 2 % d, 1
    while a != 1:
        a = (2 * a) % d
        n += 1
    return n


def b(index):
    return Fraction((index - 1) * (index - 2), index * index)


def orbit_polynomial(orbit, modulus):
    coefficients = [1]
    for a in orbit:
        next_coefficients = [0] * (len(coefficients) + 1)
        for i, value in enumerate(coefficients):
            next_coefficients[i] ^= multiply(value, a, modulus)
            next_coefficients[i + 1] ^= value
        coefficients = next_coefficients
    assert all(c in (0, 1) for c in coefficients)
    return sum(c << i for i, c in enumerate(coefficients))


def check_quantitative_and_classes():
    dimensions = []
    for n, modulus in MODULI.items():
        q, M = 1 << n, (1 << n) - 1
        check_irreducible(modulus, n)
        _, logs, powers = field_logs(q, modulus)
        entries = []
        for d in divisors(M):
            if d == 1:
                continue
            k = M // d
            primes = prime_factors(d)
            theta1 = prod(Fraction(p - 1, p) for p in primes)
            theta2 = prod(Fraction(p * p - 1, p * p) for p in primes)
            center = Fraction(q + 1, k * k) * theta2 - Fraction(3, k) * theta1
            coefficient = sum(b(k * h) for h, _ in squarefree_products(primes))
            product_expression = (2 ** len(primes)
                                  - Fraction(3, k) * prod(Fraction(p + 1, p) for p in primes)
                                  + Fraction(2, k * k) * prod(Fraction(p * p + 1, p * p) for p in primes))
            assert coefficient == product_expression
            assert 0 <= coefficient <= 2 ** len(primes)
            good = [a for a in powers[::k] if a != 1 and logs[a ^ 1] % k == 0]
            realized = {a for a in good if M // gcd(M, logs[a], logs[a ^ 1]) == d}
            assert len(good) == T(d) and len(realized) == R(d)
            assert abs(R(d) - center) <= coefficient * (1 << (n // 2))
            assert theta2 > Fraction(3, 4)
            if d > 3:
                assert len(realized) % 6 == 0
                remaining = set(realized)
                ratio_orbits = 0
                while remaining:
                    a = min(remaining)
                    inv_a, inv_b = power(a, q - 2, modulus), power(a ^ 1, q - 2, modulus)
                    orbit = {a, a ^ 1, inv_a, inv_b,
                             multiply(a, inv_b, modulus), multiply(a ^ 1, inv_a, modulus)}
                    assert len(orbit) == 6 and orbit <= remaining
                    remaining -= orbit
                    ratio_orbits += 1
                assert ratio_orbits * 6 == len(realized)

            if order_two(d) == n:
                remaining = set(realized)
                frobenius_orbits = []
                encoded = 1
                while remaining:
                    a, orbit = min(remaining), []
                    current = a
                    while current not in orbit:
                        orbit.append(current)
                        current = multiply(current, current, modulus)
                    assert current == a and len(orbit) == n
                    assert set(orbit) <= remaining
                    remaining -= set(orbit)
                    encoded = binary_product(encoded, orbit_polynomial(orbit, modulus))
                    frobenius_orbits.append(orbit)
                classifier = realization_polynomial(d)
                assert classifier == encoded
                assert classifier.bit_length() - 1 == len(realized)
                entries.append({'d': d, 'k': k, 'T_d': T(d), 'R_d': R(d),
                                'linear_map_classes': len(frobenius_orbits),
                                'main_term': str(center), 'error_coefficient': str(coefficient)})
        dimensions.append({'n': n, 'all_divisors_checked': len(divisors(M)),
                           'primitive_orders': entries})
        print(f'Quantitative count, polynomial classifier and ratio orbits: n={n}', flush=True)
    return dimensions


def check_descent():
    rows = []
    for r in range(2, 9):
        for s in divisors(r):
            if s == r:
                continue
            for u in divisors((1 << s) - 1):
                d = u * ((1 << r) + 1)
                g = u if (r // s) % 2 == 0 else u * ((1 << s) + 1)
                assert g == gcd(d, (1 << (2 * s)) - 1) and g < d
                assert intersection_polynomial(d) == intersection_polynomial(g)
                assert R(d) == 0 and order_two(d) == 2 * r
                rows.append({'r': r, 's': s, 'u': u, 'd': d, 'g': g, 'T_d': T(d)})
    return rows


def check_quarter_power():
    rows = []
    field_moduli = {4: 0x13, 8: 0x11B, 12: 0x1009, 16: 0x1002B}
    for s in range(1, 6):
        t, n = 1 << s, 4 * s
        q, k, d = t ** 4, t + 1, (t - 1) * (t * t + 1)
        assert k * d == q - 1
        assert intersection_polynomial(d) == intersection_polynomial(t - 1)
        assert T(d) == t - 2 and R(d) == 0 and order_two(d) == n
        row = {'s': s, 'n': n, 'q': q, 'k': k, 'd': d, 'T_d': T(d), 'R_d': R(d)}
        if n in field_moduli:
            modulus = field_moduli[n]
            check_irreducible(modulus, n)
            _, logs, powers = field_logs(q, modulus)
            good = {a for a in powers[::k] if a != 1 and logs[a ^ 1] % k == 0}
            subfield = set(powers[::(q - 1) // (t - 1)]) | {0}
            assert good == subfield - {0, 1}
            assert all(power(a, t, modulus) == a for a in subfield)
            assert all((q - 1) // gcd(q - 1, logs[a], logs[a ^ 1]) < d for a in good)
            row['independent_field_enumeration'] = True
            row['modulus_hex'] = hex(modulus)
        rows.append(row)
        print(f'Quarter-power obstruction: s={s}, d={d}, T_d={T(d)}, R_d=0', flush=True)
    return rows


def check_small_graphs():
    rows = []
    for n in (2, 4):
        q, modulus = 1 << n, MODULI[n]
        _, logs, powers = field_logs(q, modulus)
        for d in divisors(q - 1):
            if d == 1:
                continue
            connection = set(powers[::(q - 1) // d])
            triangles = []
            generated = []
            for x, y, z in combinations(range(q), 3):
                if not {x ^ y, x ^ z, y ^ z} <= connection:
                    continue
                triangles.append((x, y, z))
                a = multiply(z ^ x, power(y ^ x, q - 2, modulus), modulus)
                if (q - 1) // gcd(q - 1, logs[a], logs[a ^ 1]) == d:
                    generated.append((x, y, z))
            assert len(triangles) == q * d * T(d) // 6
            assert 6 * len(generated) == q * d * R(d)
            if d > 3:
                for triangle in generated:
                    stabilizers = []
                    target = frozenset(triangle)
                    for a in connection:
                        for c in range(q):
                            if frozenset(multiply(a, x, modulus) ^ c for x in triangle) == target:
                                stabilizers.append((a, c))
                    assert stabilizers == [(1, 0)]
            rows.append({'n': n, 'd': d, 'triangles': len(triangles),
                         'generating_triangles': len(generated),
                         'free_affine_action_checked': d > 3})
    return rows


def main():
    if not __debug__:
        raise RuntimeError('Use ordinary Python without -O.')
    dimensions = check_quantitative_and_classes()
    descent = check_descent()
    quarter = check_quarter_power()
    graphs = check_small_graphs()
    # The uniform range is a paper proof; these are arithmetic endpoint audits.
    assert (Fraction(16, 12) - 1) * 256 - 1 > 0
    data = {'scope': {'quantitative_and_classes': 'All d|2^n-1, even n=2..14',
                      'norm_descent': '2<=r<=8, every proper s|r, every u|2^s-1',
                      'quarter_polynomials': 's=1..5', 'quarter_field_enumeration': 's=1..4',
                      'direct_graphs': 'All subgroup orders on 4 and 16 vertices'},
            'dimensions': dimensions, 'norm_descent': descent,
            'quarter_power': quarter, 'direct_graphs': graphs}
    (ROOT / 'scalar_depth_results.json').write_text(
        json.dumps(data, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print('All scalar-depth certificates passed.')


if __name__ == '__main__':
    main()
