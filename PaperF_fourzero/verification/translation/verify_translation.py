#!/usr/bin/env python3
"""Independent bounded checks for the translation branch of Paper F.

Requires Python 3.10+ and only its standard library. Run without -O:
    python verify_translation.py
    python verify_translation.py --out audit_rerun

The default output is audit_summary.json beside this script. An explicit
--out selects another output directory. No manuscript, external data file,
network service, FLINT installation or machine-specific path is required.

Factor certificates below were exported from the previously stored FLINT
factorizations in the 2026-10-29 exploration audit. This verifier does not
factor polynomials or rerun that software: it independently validates every
listed factor with the Rabin criterion and multiplies the factors back.
The finite checks support separate written proofs; they do not establish
all-degree existence, global priority, or Lean formalization.
"""
from pathlib import Path
from itertools import combinations, product
from collections import Counter
import argparse
import hashlib
import json
import platform

if not __debug__:
    raise SystemExit("Verification requires assertions; run Python without -O or -OO.")

def mul(a, b):
    r = 0
    while b:
        if b & 1:
            r ^= a
        a <<= 1
        b >>= 1
    return r

def rem(a, b):
    assert b
    while a.bit_length() >= b.bit_length():
        a ^= b << (a.bit_length() - b.bit_length())
    return a

def gcd(a, b):
    while b:
        a, b = b, rem(a, b)
    return a

def power(a, e):
    r = 1
    while e:
        if e & 1:
            r = mul(r, a)
        a = mul(a, a)
        e >>= 1
    return r

def prime_divisors(n):
    ans = []
    p = 2
    while p*p <= n:
        if n % p == 0:
            ans.append(p)
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        ans.append(n)
    return ans

def rabin(f):
    n = f.bit_length()-1
    if n < 1:
        return False
    x = rem(2, f)
    h = x
    tests = {n//p for p in prime_divisors(n)}
    for j in range(1, n+1):
        h = rem(mul(h, h), f)
        if j in tests and gcd(f, h ^ x) != 1:
            return False
    return h == x

def S(d):
    return (1 << (d+1))-1

def candidate(n, i, j):
    return S(n) ^ (1 << i) ^ (1 << j) ^ (1 << (n-1-i)) ^ (1 << (n-1-j))

def translate_horner(f):
    r = 0
    for j in range(f.bit_length()-1, -1, -1):
        r = (r << 1) ^ r ^ ((f >> j) & 1)
    return r

def reverse(f, d):
    return sum(((f >> j) & 1) << (d-j) for j in range(d+1))

def compose(f, g):
    r = 0
    for j in range(f.bit_length()-1, -1, -1):
        r = mul(r, g) ^ ((f >> j) & 1)
    return r

def descend(f):
    n = f.bit_length()-1
    assert n % 2 == 0
    m = n//2
    basis = [power(6, j) for j in range(m+1)]  # x^2+x = 0b110
    rest, h = f, 0
    for j in range(m, -1, -1):
        if (rest >> (2*j)) & 1:
            rest ^= basis[j]
            h ^= 1 << j
    assert rest == 0
    assert compose(h, 6) == f
    return h

# Integer bits encode coefficients in F_2[x]; hexadecimal is not integer factorization.
FACTOR_CERTIFICATES = {
    (14, 3, 4): {'f': '0x79e7', 'h': '0xa3', 'f_factors': [('0x7', 1), ('0x1321', 1)], 'h_factors': [('0x3', 1), ('0x61', 1)]},
    (30, 5, 9): {'f': '0x7eeffddf', 'h': '0x91eb', 'f_factors': [('0x1333', 1), ('0x77fe5', 1)], 'h_factors': [('0x67', 1), ('0x3b5', 1)]},
    (30, 5, 12): {'f': '0x7efdefdf', 'h': '0x97eb', 'f_factors': [('0x6d', 1), ('0x17b7c0b', 1)], 'h_factors': [('0xd', 1), ('0x1e2f', 1)]},
    (30, 9, 12): {'f': '0x7fededff', 'h': '0x868b', 'f_factors': [('0xd5', 1), ('0xbf', 1), ('0x17b', 2)], 'h_factors': [('0x1f', 2), ('0xa7', 1)]},
}

def main(output_dir):
    EXPECTED = {(14, 3, 4), (30, 5, 9), (30, 5, 12), (30, 9, 12)}
    counts = Counter()
    found = set()
    for n in range(6, 257, 2):
        # Pascal recurrence (x+1)^j, not the Lucas submask implementation.
        powers = [1]
        for j in range(n):
            powers.append((powers[-1] << 1) ^ powers[-1])
        ds = 0
        for p in powers:
            ds ^= p
        ds ^= S(n)
        sig = {
            i: powers[i] ^ powers[n-1-i] ^ (1 << i) ^ (1 << (n-1-i))
            for i in range(1, n//2)
        }
        for i, j in combinations(range(1, n//2), 2):
            counts['fourzero_candidates_6_to_256'] += 1
            yes = (sig[i] ^ sig[j]) == ds
            assert yes == ((n, i, j) in EXPECTED), (n, i, j)
            if n <= 64:
                f = candidate(n, i, j)
                assert yes == (translate_horner(f) == f)
                counts['direct_horner_candidates_6_to_64'] += 1
            if yes:
                found.add((n, i, j))
    assert found == EXPECTED

    # Arbitrary tail palindromes, not just four-zero shapes.
    for k in range(1, 11):
        n, d = 2*k, k-1
        for inner in range(1 << (k-1)):
            half = (inner << 1) | 1
            f = (1 << n) | half | (reverse(half, k-1) << k)
            e = sum(((f >> (2*j)) & 1) << j for j in range(k))
            o = reverse(e, d)
            a = (1 << k) ^ e
            direct = translate_horner(f) == f
            descent = translate_horner(o) == o and (translate_horner(a) ^ a) == o
            assert direct == descent
            counts['general_tail_palindromes_2_to_20'] += 1
            if direct:
                assert (n+2) & (n+1) == 0
                counts['general_translation_invariant'] += 1
                h = descend(f)
                if n >= 6:
                    zeros = n - (f ^ (1 << n)).bit_count()
                    assert zeros % 2 == 0
                    s = zeros//2
                    assert ((h >> (k-1)) & 1) == (s % 2)
                    counts['zero_parity_bridge_checks'] += 1
                    if s % 2 == 0:
                        assert not rabin(f)
                        counts['zero_multiple_of_four_reducibility_checks'] += 1

    # Check every binary rational map represented by coprime nonzero g,h, maxdegree2.
    map_counts = Counter()
    for g, h in product(range(1, 8), repeat=2):
        if max(g.bit_length(), h.bit_length()) != 3 or gcd(g, h) != 1:
            continue
        g0, g1, g2 = [(g >> j) & 1 for j in range(3)]
        h0, h1, h2 = [(h >> j) & 1 for j in range(3)]
        a = (g2 & h1) ^ (g1 & h2)
        b = (g0 & h2) ^ (g2 & h0)
        c = (g1 & h0) ^ (g0 & h1)
        assert (b ^ (a & c)) == 1
        inseparable = (g1 == h1 == 0)
        assert inseparable == (a == c == 0)
        branch = 'inseparable' if inseparable else str((a, b, c))
        assert inseparable or (a, b, c) in {(1, 0, 1), (0, 1, 1), (1, 1, 0)}
        map_counts[branch] += 1
        for m in range(2, 5):
            for low in range(1 << m):
                H = (1 << m) | low
                F = 0
                for j in range(m+1):
                    if (H >> j) & 1:
                        F ^= mul(power(g, j), power(h, m-j))
                drop = F.bit_length()-1 < 2*m
                predicted_drop = h2 == 1 and rem(H, 2 ^ g2) == 0
                assert drop == predicted_drop
                if rabin(H):
                    assert not drop
                counts['quadratic_map_input_checks'] += 1
                if drop:
                    continue
                if inseparable:
                    assert all(((F >> j) & 1) == 0 for j in range(1, 2*m+1, 2))
                elif (a, b, c) == (1, 0, 1):
                    assert reverse(F, 2*m) == F
                elif (a, b, c) == (0, 1, 1):
                    assert translate_horner(F) == F
                else:
                    M = 0
                    for j in range(2*m+1):
                        if (F >> j) & 1:
                            M ^= power(3, 2*m-j) << j
                    assert M == F
                counts['full_degree_invariance_checks'] += 1

    # Finite Artin-Schreier criterion cross-check, not a replacement for the proof.
    for m in range(2, 9):
        for low in range(1 << m):
            h = (1 << m) | low
            assert rabin(compose(h, 6)) == (rabin(h) and bool((h >> (m-1)) & 1))
            counts['AS_criterion_degrees_2_to_8'] += 1


    rows = []
    for n, i, j in sorted(EXPECTED):
        f, m = candidate(n, i, j), n//2
        h = descend(f)
        cert = FACTOR_CERTIFICATES[(n, i, j)]
        assert f == int(cert['f'], 16)
        assert h == int(cert['h'], 16)
        assert not ((h >> (m-1)) & 1)
        assert not rabin(f)
        factor_lists = {}
        for name, polynomial in [('f', f), ('h', h)]:
            restored = 1
            factors = []
            for encoded, multiplicity in cert[name + '_factors']:
                q = int(encoded, 16)
                assert multiplicity >= 1
                assert rabin(q)
                counts['irreducible_factor_certificates'] += 1
                restored = mul(restored, power(q, multiplicity))
                factors.append({'hex': encoded, 'degree': q.bit_length()-1,
                                'multiplicity': multiplicity})
            assert restored == polynomial
            counts['factor_products_verified'] += 1
            factor_lists[name + '_factors'] = factors
        rows.append({'n': n, 'i': i, 'j': j, 'f_hex': hex(f), 'h_hex': hex(h),
                     'h_exponents': [q for q in range(m, -1, -1) if (h >> q) & 1],
                     'h_subleading': 0, 'f_irreducible': False, **factor_lists})

    expected_counts = {
        'fourzero_candidates_6_to_256': 341376,
        'direct_horner_candidates_6_to_64': 4960,
        'general_tail_palindromes_2_to_20': 1023,
        'quadratic_map_input_checks': 672,
        'full_degree_invariance_checks': 448,
        'AS_criterion_degrees_2_to_8': 508,
        'factor_products_verified': 8,
        'irreducible_factor_certificates': 17,
    }
    for key, expected in expected_counts.items():
        assert counts[key] == expected, (key, counts[key], expected)
    assert sum(map_counts.values()) == 24
    assert set(map_counts.values()) == {6}
    result = {
        'status': 'PASS',
        'scope': 'Bounded computational checks; all-degree statements rely on the separate paper proofs.',
        'software': {'python': platform.python_version(),
                     'implementation': platform.python_implementation(),
                     'dependencies': 'Python standard library only'},
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'factor_certificate_provenance': {
            'origin': 'Stored FLINT factorization records from the translation exploration audit dated 2026-10-29.',
            'operation_in_this_run': 'Independent bit-arithmetic Rabin checks and exact product reconstruction; no factorization software was run.',
            'embedded_certificates': True,
        },
        'counts': dict(counts),
        'quadratic_maps_total': sum(map_counts.values()),
        'quadratic_maps_by_branch': dict(map_counts),
        'four_translation_shapes': rows,
        'limitations': ['Finite checks do not prove the all-degree classification.',
                        'No new primitive-existence search is performed.',
                        'No Lean verification or global-priority claim.'],
    }
    output_dir.mkdir(parents=True, exist_ok=True)
    output = output_dir / 'audit_summary.json'
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({key: result[key] for key in ('status', 'counts', 'quadratic_maps_total')}, indent=2))
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, default=Path(__file__).resolve().parent,
                        help='Output directory for audit_summary.json (default: directory of this script).')
    args = parser.parse_args()
    main(args.out)
