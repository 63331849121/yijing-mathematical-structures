"""Construct exact tower-field certificates for the finite range s=2..32."""
from pathlib import Path
from math import gcd, prod
from functools import lru_cache
import json
import random

from verify_scalar_realization import multiply, power, polynomial_gcd, prime_factors

ROOT = Path(__file__).resolve().parent
RNG = random.Random(20261012)


def probable_prime(n):
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d, shift = n - 1, 0
    while d % 2 == 0:
        d //= 2
        shift += 1
    for a in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(shift - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def rho(n):
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return p
    while True:
        y, c, block = RNG.randrange(1, n), RNG.randrange(1, n), 64
        g, radius = 1, 1
        while g == 1:
            x = y
            for _ in range(radius):
                y = (y * y + c) % n
            step = 0
            while step < radius and g == 1:
                saved, batch = y, 1
                for _ in range(min(block, radius - step)):
                    y = (y * y + c) % n
                    batch = batch * abs(x - y) % n
                g = gcd(batch, n)
                step += block
            radius *= 2
        if g == n:
            while True:
                saved = (saved * saved + c) % n
                g = gcd(abs(x - saved), n)
                if g > 1:
                    break
        if g != n:
            return g


@lru_cache(None)
def factor(n):
    if n == 1:
        return ()
    if probable_prime(n):
        return (n,)
    p = rho(n)
    return tuple(sorted(factor(p) + factor(n // p)))


PRIME_CERTS = {'2': {'factors': [], 'witness': None}}


def certify_prime(p):
    if str(p) in PRIME_CERTS:
        return
    factors = factor(p - 1)
    for r in set(factors):
        certify_prime(r)
    assert prod(factors) == p - 1
    # Complete Lucas certificate. Probable-prime screening is not the proof.
    a = 2
    while not (pow(a, p - 1, p) == 1 and all(
            gcd(pow(a, (p - 1) // r, p) - 1, p) == 1 for r in set(factors))):
        a += 1
        assert a < p
    PRIME_CERTS[str(p)] = {'factors': list(factors), 'witness': a}


def irreducible(m, n):
    if power(2, 1 << n, m) != 2:
        return False
    return all(polynomial_gcd(m, power(2, 1 << (n // r), m) ^ 2) == 1
               for r in prime_factors(n))


def trace(a, n, m):
    answer, current = 0, a
    for _ in range(n):
        answer ^= current
        current = multiply(current, current, m)
    assert answer in (0, 1)
    return answer


def tower_multiply(z, w, b, c, m):
    x, y = z
    xx, yy = w
    v = multiply(y, yy, m)
    return (multiply(x, xx, m) ^ multiply(b, v, m),
            multiply(x, yy, m) ^ multiply(y, xx, m) ^ multiply(c, v, m))


def tower_power(z, exponent, b, c, m):
    answer = (1, 0)
    while exponent:
        if exponent & 1:
            answer = tower_multiply(answer, z, b, c, m)
        z = tower_multiply(z, z, b, c, m)
        exponent >>= 1
    return answer


def find_row(s):
    t, n = 1 << s, 2 * s
    A, B = t + 1, t * t + 1
    factors_A, factors_B = factor(A), factor(B)
    for p in set(factors_A + factors_B):
        certify_prime(p)
    low = 3
    while not irreducible((1 << n) | low, n):
        low += 2
    m = (1 << n) | low
    base = 2
    while True:
        b = power(base, t - 1, m)
        if b != 1 and all(power(b, A // p, m) != 1 for p in set(factors_A)):
            break
        base += 1
    assert power(b, A, m) == 1
    attempts = 0
    # Vary b only if the first primitive norm fiber has no certificate among
    # the examined w; exhaustive for the tiny cases and bounded thereafter.
    b0 = b
    for exponent in range(1, min(A, 32)):
        if gcd(exponent, A) != 1:
            continue
        b = power(b0, exponent, m)
        w = 1
        for j in range(min(A, 512)):
            attempts += 1
            c = 1 ^ b ^ w
            if c:
                inv_c = power(c, (1 << n) - 2, m)
                f = multiply(b, multiply(inv_c, inv_c, m), m)
                if trace(f, n, m) == 1:
                    d = A * B
                    a = (0, 1)
                    powers = {str(p): tower_power(a, d // p, b, c, m)
                              for p in sorted(set(factors_A + factors_B))}
                    if all(value != (1, 0) for value in powers.values()):
                        assert tower_power(a, d, b, c, m) == (1, 0)
                        assert tower_power((1, 1), d, b, c, m) == (1, 0)
                        assert tower_power(a, B, b, c, m) == (b, 0)
                        assert tower_power((1, 1), B, b, c, m) == (w, 0)
                        return {'s': s, 'E_modulus_hex': hex(m), 'b_hex': hex(b),
                                'w_hex': hex(w), 'c_hex': hex(c),
                                'A_factors': list(factors_A), 'B_factors': list(factors_B),
                                'trace_input_hex': hex(f), 'absolute_trace': 1,
                                'a_power_d': [1, 0], 'one_plus_a_power_d': [1, 0],
                                'a_power_d_over_p': {p: [hex(v[0]), hex(v[1])] for p, v in powers.items()},
                                'construction': {'U_base_hex': hex(b0), 'b_exponent': exponent,
                                                 'w_exponent': j, 'attempts': attempts}}
            w = multiply(w, b0, m)
    raise AssertionError(f'No certificate found for s={s}.')


def main():
    rows = []
    for s in range(2, 33):
        row = find_row(s)
        rows.append(row)
        print('s=', s, 'm=', row['E_modulus_hex'], 'b=', row['b_hex'],
              'w=', row['w_hex'], 'attempts=', row['construction']['attempts'], flush=True)
        data = {'range': [2, 32], 'representation': 'E=F2[X]/m; L=E[Z]/(Z^2+cZ+b); a=Z',
                'certificates': rows, 'prime_certificates': PRIME_CERTS}
        (ROOT / 'inner_critical_certificates.json').write_text(
            json.dumps(data, indent=2) + '\n', encoding='utf-8')
    print('Constructed all 31 finite certificates with recursive Lucas primality certificates.')


if __name__ == '__main__':
    main()
