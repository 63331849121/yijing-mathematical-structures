"""Independent exact verification of the finite part of the inner critical theorem.

No third-party library, probable-prime test, or import from the certificate
finder is used. All reported finite equalities are exact integer arithmetic.
"""
from pathlib import Path
from math import gcd, prod, isqrt
from functools import lru_cache
from collections import Counter
import json

ROOT = Path(__file__).resolve().parent


def small_primes(n):
    result = []
    for p in range(2, n + 1):
        if all(p % r for r in result if r * r <= p):
            result.append(p)
    return result


def poly_mod(f, g):
    while f and f.bit_length() >= g.bit_length():
        f ^= g << (f.bit_length() - g.bit_length())
    return f


def poly_gcd(f, g):
    while g:
        f, g = g, poly_mod(f, g)
    return f


class BinaryField:
    def __init__(self, modulus):
        self.modulus = modulus
        self.n = modulus.bit_length() - 1
        self.size = 1 << self.n

    def mul(self, a, b):
        # Reduce after every shift, independently of the finder's full product.
        z = 0
        while b:
            if b & 1:
                z ^= a
            b >>= 1
            a <<= 1
            if a & self.size:
                a ^= self.modulus
        return z

    def power(self, a, k):
        # Left-to-right powering (the finder uses right-to-left powering).
        z = 1
        for digit in bin(k)[2:]:
            z = self.mul(z, z)
            if digit == '1':
                z = self.mul(z, a)
        return z

    def trace(self, a):
        z, v = 0, a
        for _ in range(self.n):
            z ^= v
            v = self.mul(v, v)
        assert z in (0, 1)
        return z

    def check_irreducible(self):
        assert self.modulus & 1
        v, frobenius = 2, {0: 2}
        for j in range(1, self.n + 1):
            v = self.mul(v, v)
            frobenius[j] = v
        assert frobenius[self.n] == 2
        for r in small_primes(self.n):
            if self.n % r == 0:
                assert poly_gcd(self.modulus, frobenius[self.n // r] ^ 2) == 1


class TowerField:
    def __init__(self, base, b, c):
        self.base, self.b, self.c = base, b, c

    def mul(self, z, w):
        x, y = z
        xx, yy = w
        m = self.base.mul
        p0, p2 = m(x, xx), m(y, yy)
        # Karatsuba convolution, followed by Z^2 = cZ+b.
        p1 = m(x ^ y, xx ^ yy) ^ p0 ^ p2
        return (p0 ^ m(self.b, p2), p1 ^ m(self.c, p2))

    def power(self, a, k):
        z = (1, 0)
        for digit in bin(k)[2:]:
            z = self.mul(z, z)
            if digit == '1':
                z = self.mul(z, a)
        return z


def check_primes(certificates):
    @lru_cache(None)
    def prove(p):
        if p == 2:
            assert certificates['2'] == {'factors': [], 'witness': None}
            return True
        assert p > 2 and p % 2 == 1
        row = certificates[str(p)]
        factors, a = row['factors'], row['witness']
        assert factors and prod(factors) == p - 1
        assert all(2 <= r < p and prove(r) for r in factors)
        assert 1 < a < p and pow(a, p - 1, p) == 1
        assert all(gcd(pow(a, (p - 1) // r, p) - 1, p) == 1 for r in set(factors))
        return True

    for p in certificates:
        assert prove(int(p))
    return prove


def check_row(row, prove):
    s = row['s']
    t, A, B = 1 << s, (1 << s) + 1, (1 << (2 * s)) + 1
    d = A * B
    assert prod(row['A_factors']) == A and prod(row['B_factors']) == B
    factors = set(row['A_factors'] + row['B_factors'])
    assert all(prove(p) for p in factors)
    E = BinaryField(int(row['E_modulus_hex'], 16))
    assert E.n == 2 * s
    E.check_irreducible()
    b, w, c = [int(row[key + '_hex'], 16) for key in ('b', 'w', 'c')]
    assert 0 < b < E.size and 0 < w < E.size and 0 < c < E.size
    assert c == 1 ^ b ^ w
    assert E.power(b, A) == E.power(w, A) == 1
    assert all(E.power(b, A // p) != 1 for p in set(row['A_factors']))
    trace_input = E.mul(b, E.power(c, E.size - 3))
    assert trace_input == int(row['trace_input_hex'], 16)
    assert E.trace(trace_input) == row['absolute_trace'] == 1
    L = TowerField(E, b, c)
    a = (0, 1)
    assert L.power(a, d) == tuple(row['a_power_d']) == (1, 0)
    assert L.power((1, 1), d) == tuple(row['one_plus_a_power_d']) == (1, 0)
    assert L.power(a, B) == (b, 0)
    assert L.power((1, 1), B) == (w, 0)
    stored = row['a_power_d_over_p']
    assert set(stored) == {str(p) for p in factors}
    for p in factors:
        value = L.power(a, d // p)
        assert value == tuple(int(v, 16) for v in stored[str(p)])
        assert value != (1, 0)
    return E, L


def intersection_degree(e):
    # Build (X+1)^e by multiplying the sparse Frobenius factors 1+X^(2^j).
    polynomial = 1
    for j, digit in enumerate(reversed(bin(e)[2:])):
        if digit == '1':
            polynomial ^= polynomial << (1 << j)
    return poly_gcd((1 << e) ^ 1, polynomial ^ 1).bit_length() - 1


def exact_counts(row, E, L):
    s, n = row['s'], E.n
    t, A, B = 1 << s, (1 << s) + 1, (1 << (2 * s)) + 1
    d, b, c = A * B, L.b, L.c
    x, y, logs = 1, 0, {}
    for j in range(d):
        packed = x | (y << n)
        assert packed not in logs
        logs[packed] = j
        x, y = E.mul(b, y), x ^ E.mul(c, y)
    assert (x, y) == (1, 0)
    bp = [1]
    for _ in range(A - 1):
        bp.append(E.mul(bp[-1], b))
    pairs = [(z, j, logs[z ^ 1]) for z, j in logs.items() if z ^ 1 in logs]
    T = len(pairs)
    R = sum(gcd(d, j, k) == 1 for _, j, k in pairs)
    P = sum(gcd(d, j) == 1 for _, j, _ in pairs)
    assert T == intersection_degree(d)
    products = [(1, 1)]
    for p in set(row['A_factors'] + row['B_factors']):
        products += [(h * p, -sign) for h, sign in products[:]]
    assert R == sum(sign * intersection_degree(d // h) for h, sign in products)
    fibers = Counter(j % A for _, j, _ in pairs)
    for j in range(A):
        if gcd(j, A) == 1:
            assert (fibers[j] - (t + 1)) ** 2 <= 4 * t
    degenerate = sum((1 ^ bp[j % A] ^ bp[k % A]) == 0 for _, j, k in pairs)
    assert degenerate == (2 if s % 2 else 0)
    diagonal = [(j, k) for _, j, k in pairs if j % A == k % A]
    return {'s': s, 't': t, 'd': d, 'T_d': T, 'R_d': R, 'primitive_slope_count': P,
            'degenerate_subfield_elements': degenerate,
            'diagonal_candidates': len(diagonal),
            'diagonal_realizing': sum(gcd(d, j, k) == 1 for j, k in diagonal),
            'primitive_norm_fiber_min': min(fibers[j] for j in range(A) if gcd(j, A) == 1),
            'primitive_norm_fiber_max': max(fibers[j] for j in range(A) if gcd(j, A) == 1)}


def check_effective_constant():
    primes = [p for p in small_primes(255) if p % 4 == 1]
    assert primes == [5, 13, 17, 29, 37, 41, 53, 61, 73, 89, 97, 101,
                      109, 113, 137, 149, 157, 173, 181, 193, 197, 229, 233, 241]
    assert 256 ** len(primes) < 32 ** 8 * prod(primes)
    # W(B) < 32 B^(1/8); s>=33 gives t^4 > 256^8 (t^2+1).
    t = 1 << 33
    assert t ** 4 > 256 ** 8 * (t * t + 1)
    return {'small_primes_1_mod_4': primes,
            'constant_eighth_power_numerator': str(256 ** len(primes)),
            'constant_eighth_power_denominator': str(prod(primes)),
            'constant_less_than': 32, 'analytic_range_s_at_least': 33}


def main():
    if not __debug__:
        raise RuntimeError('Run without -O; exact verification requires assertions.')
    data = json.loads((ROOT / 'inner_critical_certificates.json').read_text(encoding='utf-8'))
    assert data['range'] == [2, 32]
    assert [row['s'] for row in data['certificates']] == list(range(2, 33))
    prove = check_primes(data['prime_certificates'])
    counts = []
    expected = [(24, 24), (86, 72), (240, 240), (1214, 960), (4104, 3960)]
    for row in data['certificates']:
        E, L = check_row(row, prove)
        if row['s'] <= 6:
            result = exact_counts(row, E, L)
            assert (result['T_d'], result['R_d']) == expected[row['s'] - 2]
            counts.append(result)
        print(f"s={row['s']}: exact irreducibility, primality, norm and order certificates verified.", flush=True)
    result = {'finite_range_verified': [2, 32], 'number_of_certificates': 31,
              'recursive_primality_certificates': len(data['prime_certificates']),
              'exact_small_counts': counts, 'effective_constant': check_effective_constant()}
    output = ROOT / 'inner_critical_verification.json'
    if output.exists():
        assert json.loads(output.read_text(encoding='utf-8')) == result
    else:
        output.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print('Verified all 31 cases; independent subgroup / polynomial-gcd counts agree for s=2..6.')
    print(json.dumps(counts, ensure_ascii=False))


if __name__ == '__main__':
    main()
