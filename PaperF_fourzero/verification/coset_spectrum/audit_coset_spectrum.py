"""Bounded independent checks for the Paper F contribution audit.

No historical primitive-polynomial enumeration is imported or extended.
Binary vectors are integers; first-half coordinate i is bit i.
"""
from collections import Counter, defaultdict
from itertools import combinations
from math import comb
from pathlib import Path
import hashlib
import json

OUT = Path(__file__).resolve().parent
SOURCE = Path(__file__).resolve().parents[2] / 'PaperF_fourzero.tex'


def rev(a, k):
    return int(f'{a:0{k}b}'[::-1], 2)


def parity(a):
    return a.bit_count() & 1


def canonical(w, basis):
    for b in basis:
        if w & (1 << (b.bit_length() - 1)):
            w ^= b
    return w


def kernel_basis(k):
    ans = []
    for i in range((k + 1) // 2):
        c = (1 << i) | (1 << (k - 1 - i))
        ans.append(c | (c << k))
    return sorted(ans, reverse=True)


def col(i, k):
    r = k // 2
    j = min(i, k - 1 - i)
    if k & 1 and j == r:
        return 0
    return 1 << (r - 1 if j == 0 else j - 1)


def expected_mu(k):
    r = k // 2
    out = Counter()
    if r > 1:
        out[0] = r - 1
    for a in range(r - 1):
        out[(1 << a) ^ (1 << (r - 1))] = 2
        if k & 1:
            out[1 << a] = 2
    for a, b in combinations(range(r - 1), 2):
        out[(1 << a) ^ (1 << b)] = 4
    if k & 1:
        out[1 << (r - 1)] = 1
    return out


def factor_int(a):
    ans = []
    p = 2
    while p * p <= a:
        if a % p == 0:
            ans.append(p)
            while a % p == 0:
                a //= p
        p += 1
    if a > 1:
        ans.append(a)
    return ans


def mod_poly(a, f):
    while a.bit_length() >= f.bit_length():
        a ^= f << (a.bit_length() - f.bit_length())
    return a


def gcd_poly(a, b):
    while b:
        a, b = b, mod_poly(a, b)
    return a


def mul_mod(a, b, f):
    out = 0
    top = 1 << (f.bit_length() - 1)
    while b:
        if b & 1:
            out ^= a
        a <<= 1
        if a & top:
            a ^= f
        b >>= 1
    return out


def pow_mod(a, m, f):
    out = 1
    while m:
        if m & 1:
            out = mul_mod(out, a, f)
        a = mul_mod(a, a, f)
        m >>= 1
    return out


def primitive_certificate(f, n):
    sq = [2]
    for _ in range(n):
        sq.append(mul_mod(sq[-1], sq[-1], f))
    rabin = {str(p): gcd_poly(sq[n // p] ^ 2, f)
             for p in factor_int(n)}
    irr = sq[n] == 2 and all(v == 1 for v in rabin.values())
    orders = {str(p): hex(pow_mod(2, ((1 << n) - 1) // p, f))
              for p in factor_int((1 << n) - 1)} if irr else {}
    prim = irr and all(v != '0x1' for v in orders.values())
    divisor = None
    if not irr:
        for d in range(1, n // 2 + 1):
            for q in range((1 << d) | 1, 1 << (d + 1), 2):
                if mod_poly(f, q) == 0:
                    divisor = q
                    break
            if divisor is not None:
                break
    return {'polynomial_hex': hex(f), 'degree': n,
            'irreducible': irr, 'primitive': prim,
            'rabin_gcds': rabin, 'frobenius_final': hex(sq[n]),
            'order_test_residues': orders,
            'proper_divisor_hex': hex(divisor) if divisor else None}


def main():
    pairs = 0
    rows = []
    characters = 0
    moment_checks = 0
    kernel_checks = 0
    enumerator_checks = 0
    for k in range(3, 129):
        r = k // 2
        kb = kernel_basis(k)
        J = (1 << k) - 1
        actual = Counter()
        coset_to_syn = {}
        syn_to_coset = {}
        for i, j in combinations(range(1, k), 2):
            A = J ^ (1 << i) ^ (1 << j)
            w = A | (rev(A, k) << k)
            c = canonical(w, kb)
            s = col(i, k) ^ col(j, k)
            assert coset_to_syn.setdefault(c, s) == s
            assert syn_to_coset.setdefault(s, c) == c
            # Explicitly check the group-law lift, not only the syndrome.
            wi = (J ^ (1 << i)) | (rev(J ^ (1 << i), k) << k)
            wj = (J ^ (1 << j)) | (rev(J ^ (1 << j), k) << k)
            assert canonical(w ^ wi ^ wj, kb) == 0
            actual[s] += 1
            pairs += 1
        assert actual == expected_mu(k)
        D = 1 if k == 3 else 1 + comb((k + 1) // 2, 2)
        assert len(actual) == D
        for t in range(1, 7):
            want = ((r - 1) ** t + 2 ** t * (r - 1)
                    + 4 ** t * comb(r - 1, 2))
            if k & 1:
                want += 2 ** t * (r - 1) + 1
            assert sum(v ** t for v in actual.values()) == want
            moment_checks += 1
        if k <= 20:
            L = k - 1
            cols = [col(i, k) for i in range(1, k)]
            # Every character of the r-dimensional palindrome quotient.
            for y in range(1 << r):
                t = sum(parity(y & u) for u in cols)
                S = L - 2 * t
                direct = sum(m * (-1 if parity(y & s) else 1)
                             for s, m in actual.items())
                K2 = comb(L - t, 2) - t * (L - t) + comb(t, 2)
                assert direct == (S * S - L) // 2 == K2
                characters += 1
            # Exhaust all half-tail masks, not just the weight-two shell.
            fibers = defaultdict(Counter)
            for x in range(1 << L):
                A = x << 1
                w = A | (rev(A, k) << k)
                syn = 0
                for i in range(1, k):
                    if A & (1 << i):
                        syn ^= col(i, k)
                is_kernel = canonical(w, kb) == 0
                assert is_kernel == (syn == 0) == (A == rev(A, k))
                fibers[syn][A.bit_count()] += 1
                kernel_checks += 1
            for s in range(1 << r):
                coeffs = [1]
                for a in range(r - 1):
                    factor = [0, 2] if s & (1 << a) else [1, 0, 1]
                    new = [0] * (len(coeffs) + len(factor) - 1)
                    for i, u in enumerate(coeffs):
                        for j, v in enumerate(factor):
                            new[i + j] += u * v
                    coeffs = new
                if s & (1 << (r - 1)):
                    coeffs = [0] + coeffs
                if k & 1:
                    coeffs = ([coeffs[0]] + [coeffs[i] + coeffs[i - 1]
                              for i in range(1, len(coeffs))] + [coeffs[-1]])
                assert {a: b for a, b in enumerate(coeffs) if b} == dict(fibers[s])
                enumerator_checks += 1
        rows.append({'k': k, 'n': 2 * k, 'candidate_pairs': sum(actual.values()),
                     'occupied_cosets': D, 'second_moment': sum(m*m for m in actual.values())})

    mixed = None
    # A small diagnostic, not a new primitive-count dataset.
    for n in range(6, 25, 2):
        k = n // 2
        groups = defaultdict(list)
        for i, j in combinations(range(1, k), 2):
            f = ((1 << (n + 1)) - 1) ^ (1 << i) ^ (1 << j)
            f ^= (1 << (n - 1 - i)) ^ (1 << (n - 1 - j))
            cert = primitive_certificate(f, n)
            cert['zero_half_positions'] = [i, j]
            cert['syndrome'] = col(i, k) ^ col(j, k)
            groups[cert['syndrome']].append(cert)
        for s, records in groups.items():
            yes = [a for a in records if a['primitive']]
            no = [a for a in records if not a['primitive']]
            if yes and no:
                mixed = {'n': n, 'syndrome': s, 'primitive': yes[0],
                         'nonprimitive': no[0]}
                break
        if mixed:
            break
    assert mixed is not None
    f1 = int(mixed['primitive']['polynomial_hex'], 16)
    f2 = int(mixed['nonprimitive']['polynomial_hex'], 16)
    k = mixed['n'] // 2
    delta = f1 ^ f2
    assert canonical(delta, kernel_basis(k)) == 0
    mixed['tail_difference_hex'] = hex(delta)
    mixed['difference_common_half_hex'] = hex(delta & ((1 << k) - 1))

    result = {'date': '2026-10-29', 'status': 'all_checks_passed',
              'source_sha256': hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
              'scope': {'coset_checks_k': [3, 128],
                        'candidate_pairs_checked': pairs,
                        'moments_t': [1, 6], 'moment_checks': moment_checks,
                        'all_image_characters_k': [3, 20],
                        'character_checks': characters,
                        'all_half_masks_k': [3, 20],
                        'kernel_masks_checked': kernel_checks,
                        'entire_coset_weight_enumerator_checks': enumerator_checks},
              'same_coset_different_primitivity': mixed, 'rows': rows,
              'limitations': ['Finite checks supplement algebraic proofs.',
                              'Historical n<=200 primitivity counts not audited here.',
                              'No global literature priority certification.']}
    (OUT / 'audit_results.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
    print(json.dumps({key: value for key, value in result.items() if key != 'rows'}, indent=2))


if __name__ == '__main__':
    main()
