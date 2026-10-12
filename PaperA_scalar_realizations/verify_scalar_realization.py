"""Check finite scalar-realization counts by two independent methods.

Polynomial gcds over F2 are compared with explicit multiplicative-subgroup
enumeration in finite fields. The general theorems have paper proofs.
"""

from fractions import Fraction
from math import gcd
from pathlib import Path
import json


ROOT = Path(__file__).resolve().parent
MODULI = {2: 0x7, 4: 0x13, 6: 0x43, 8: 0x11B,
          10: 0x409, 12: 0x1009, 14: 0x4021}
EXPECTED = {4: (0, 0), 6: (8, 0), 8: (24, 24),
            10: (120, 90), 12: (440, 396), 14: (1848, 1722)}


def prime_factors(value):
    out = []
    p = 2
    while p * p <= value:
        if value % p == 0:
            out.append(p)
            while value % p == 0:
                value //= p
        p += 1
    if value > 1:
        out.append(value)
    return out


def divisors(value):
    return [e for e in range(1, value + 1) if value % e == 0]


def polynomial_remainder(a, b):
    while a.bit_length() >= b.bit_length():
        a ^= b << (a.bit_length() - b.bit_length())
    return a


def polynomial_gcd(a, b):
    while b:
        a, b = b, polynomial_remainder(a, b)
    return a


def translated_power(e):
    """(t+1)^e via Lucas's theorem, as a binary coefficient vector."""
    result = 0
    submask = e
    while True:
        result ^= 1 << submask
        if submask == 0:
            return result
        submask = (submask - 1) & e


def intersection_degree(e):
    common = polynomial_gcd((1 << e) ^ 1, translated_power(e) ^ 1)
    return common.bit_length() - 1


def multiply(a, b, modulus):
    """Carryless product followed by polynomial reduction."""
    product = 0
    while b:
        if b & 1:
            product ^= a
        b >>= 1
        a <<= 1
    return polynomial_remainder(product, modulus)


def power(a, exponent, modulus):
    result = 1
    while exponent:
        if exponent & 1:
            result = multiply(result, a, modulus)
        a = multiply(a, a, modulus)
        exponent >>= 1
    return result


def check_irreducible(modulus, n):
    assert modulus.bit_length() - 1 == n
    assert power(2, 1 << n, modulus) == 2
    for p in prime_factors(n):
        reduced = power(2, 1 << (n // p), modulus) ^ 2
        assert polynomial_gcd(modulus, reduced) == 1


def field_logs(q, modulus):
    primes = prime_factors(q - 1)
    generator = next(a for a in range(2, q)
                     if all(power(a, (q - 1) // p, modulus) != 1
                            for p in primes))
    logs = [-1] * q
    powers = []
    a = 1
    for j in range(q - 1):
        assert logs[a] == -1
        logs[a] = j
        powers.append(a)
        a = multiply(a, generator, modulus)
    assert a == 1 and all(logs[a] >= 0 for a in range(1, q))
    return generator, logs, powers


def squarefree_products(primes):
    values = [(1, 1)]
    for p in primes:
        values += [(h * p, -sign) for h, sign in values[:]]
    return values


def check_dimension(n, modulus):
    q = 1 << n
    M = q - 1
    root_q = 1 << (n // 2)
    check_irreducible(modulus, n)
    generator, logs, powers = field_logs(q, modulus)
    entries = {}
    for d in divisors(M):
        k = M // d
        candidates = powers[::k]
        good = [a for a in candidates if a != 1 and logs[a ^ 1] % k == 0]
        realized = [a for a in good
                    if M // gcd(M, logs[a], logs[a ^ 1]) == d]
        T = intersection_degree(d)
        assert T == len(good)
        b_k = Fraction((k - 1) * (k - 2), k * k)
        center = Fraction(q + 1 - 3 * k, k * k)
        assert abs(T - center) <= b_k * root_q
        primes = prime_factors(d)
        inverse_count = sum(sign * intersection_degree(d // h)
                            for h, sign in squarefree_products(primes))
        assert inverse_count == len(realized)
        if d > 1:
            lower = (Fraction(q, k * k)
                     * (1 - sum(Fraction(1, p * p) for p in primes))
                     - Fraction(3 * k - 1, k * k)
                     - (len(primes) + b_k) * root_q)
            uniform = (Fraction(3 * q, 4 * k * k)
                       - Fraction(3 * k - 1, k * k)
                       - (len(primes) + b_k) * root_q)
            assert len(realized) >= lower and len(realized) > uniform
        entries[d] = {'T': T, 'R': len(realized)}

    if n == 2:
        return None
    d = M // 3
    assert (entries[d]['T'], entries[d]['R']) == EXPECTED[n]
    uniform = (Fraction(q, 12) - Fraction(8, 9)
               - (len(prime_factors(d)) + Fraction(2, 9)) * root_q)
    return {'n': n, 'q': q, 'd': d, 'modulus_hex': hex(modulus),
            'field_generator_hex': hex(generator),
            'T_d': entries[d]['T'], 'R_d': entries[d]['R'],
            'number_of_realizing_maps': M * entries[d]['R'],
            'uniform_lower_bound': str(uniform),
            'checked_divisor_counts': {str(e): entries[e] for e in divisors(d)}}


def main():
    if not __debug__:
        raise RuntimeError('Use Python without -O: this verifier uses assertions.')
    rows = [row for n, modulus in MODULI.items()
            if (row := check_dimension(n, modulus)) is not None]
    m = 0x11B
    a = 0x2E
    assert power(2, 16, m) == 0x5E
    assert power(2, 256, m) == 2
    assert polynomial_gcd(m, 0x5E ^ 2) == 1
    assert power(a, 85, m) == power(a ^ 1, 85, m) == 1
    assert power(a, 5, m) == 0xAB
    assert power(a, 17, m) == 0xED
    assert a != 1 and a ^ 1 != 0
    # The analytic threshold at n=14 and its step-by-two monotonicity
    # are proved in the manuscript; these exact values audit its arithmetic.
    assert (Fraction(1 << 14, 12) - Fraction(8, 9)
            - Fraction(86, 9) * (1 << 7)) == Fraction(424, 3)
    assert (Fraction(1 << 10, 12) - Fraction(8, 9)
            - Fraction(20, 9) * (1 << 5)) == Fraction(40, 3)
    assert (Fraction(1 << 12, 12) - Fraction(8, 9)
            - Fraction(38, 9) * (1 << 6)) == Fraction(632, 9)
    data = {'scope': 'Even dimensions n=2,4,6,8,10,12,14; all d dividing 2^n-1',
            'methods': ['F2 polynomial gcd', 'explicit finite-field subgroup enumeration'],
            'index_three': rows,
            'n8_witness': {'modulus_hex': hex(m), 'slope_hex': hex(a),
                           'a_power_5_hex': hex(0xAB), 'a_power_17_hex': hex(0xED),
                           'a_power_85': 1, 'one_plus_a_power_85': 1}}
    (ROOT / 'scalar_realization_results.json').write_text(
        json.dumps(data, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    for row in rows:
        print(f"n={row['n']}: d={row['d']}, T_d={row['T_d']}, R_d={row['R_d']}")
    print('All scalar-realization certificates passed.')


if __name__ == '__main__':
    main()
