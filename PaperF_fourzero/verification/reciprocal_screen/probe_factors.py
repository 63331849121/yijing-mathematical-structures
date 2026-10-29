"""Bounded exact checks for reciprocal factors and reducibility obstructions."""
import json
import math
from pathlib import Path
from collections import Counter

OUT = Path(__file__).resolve().parent

def degree(f):
    return f.bit_length()-1

def divmod_poly(a, b):
    q = 0
    while a and degree(a) >= degree(b):
        d = degree(a)-degree(b)
        q ^= 1 << d
        a ^= b << d
    return q, a

def gcd(a, b):
    while b:
        a, b = b, divmod_poly(a, b)[1]
    return a

def mul(a, b):
    c = 0
    while b:
        if b & 1:
            c ^= a
        a <<= 1
        b >>= 1
    return c

def reciprocal(f):
    n = degree(f)
    return sum(((f >> i) & 1) << (n-i) for i in range(n+1))

def derivative(f):
    return sum(((f >> i) & 1) << (i-1) for i in range(1, degree(f)+1, 2))

def candidate(n, i, j):
    return ((1 << (n+1))-1) ^ sum(1 << e for e in [i, j, n-1-i, n-1-j])

def predicted_gcd(n, i, j):
    N, delta, R = n+1, j-i, n-1-i-j
    a, b = math.gcd(N, delta), math.gcd(N, R)
    h = math.gcd(a, b)
    numerator = mul((1 << a) ^ 1, (1 << b) ^ 1)
    denominator = mul(0b11, (1 << h) ^ 1)
    result, rem = divmod_poly(numerator, denominator)
    assert rem == 0
    return result, {'a': a, 'b': b, 'h': h}

def factor_count(f):
    """Berlekamp nullity counts distinct irreducible factors; only squarefree used."""
    n = degree(f)
    basis = {}
    column = 1
    for i in range(n):
        z = column ^ (1 << i)
        while z:
            h = degree(z)
            if h in basis:
                z ^= basis[h]
            else:
                basis[h] = z
                break
        column = divmod_poly(column << 2, f)[1]
    return n-len(basis)

def powmod(a, e, f):
    z = 1
    while e:
        if e & 1:
            z = divmod_poly(mul(z, a), f)[1]
        a = divmod_poly(mul(a, a), f)[1]
        e >>= 1
    return z

def irreducible(f):
    n = degree(f)
    h = 2
    for k in range(1, n//2+1):
        h = powmod(h, 2, f)
        if gcd(f, h ^ 2) != 1:
            return False
    return powmod(2, 1 << n, f) == 2

def main():
    counts, examples, parity_keys, parity_failures = Counter(), {}, {}, {}
    by_degree = []
    for n in range(6, 102, 2):
        local = Counter()
        for i in range(1, n//2):
            for j in range(i+1, n//2):
                f = candidate(n, i, j)
                G, parameters = predicted_gcd(n, i, j)
                actual = gcd(f, reciprocal(f))
                assert actual == G
                # The same G is exactly the cyclotomic part from x^(n+1)+1.
                assert G == gcd(f, (1 << (n+1)) ^ 1)
                assert degree(G) == parameters['a']+parameters['b']-parameters['h']-1
                assert degree(G) < n
                residual, rem = divmod_poly(f, G)
                assert rem == 0 and gcd(residual, reciprocal(residual)) == 1
                sf = gcd(f, derivative(f)) == 1
                counts['all_gcd_checks'] += 1
                local['candidates'] += 1
                local['nontrivial_reciprocal_obstruction'] += int(G != 1)
                local['not_squarefree'] += int(not sf)
                if not sf and 'not_squarefree' not in examples:
                    examples['not_squarefree'] = {'n': n, 'i': i, 'j': j,
                        'polynomial_hex': hex(f), 'derivative_gcd_hex': hex(gcd(f, derivative(f)))}
                if n <= 64 and sf:
                    r = factor_count(f)
                    counts['squarefree_parity_checks'] += 1
                    if n <= 24:
                        assert (r == 1) == irreducible(f)
                        counts['berlekamp_rabin_crosschecks'] += 1
                    if G == 1:
                        rec = {'n': n, 'i': i, 'j': j, 'polynomial_hex': hex(f),
                               'distinct_irreducible_factors': r}
                        if r > 1 and 'no_reciprocal_obstruction_but_reducible' not in examples:
                            examples['no_reciprocal_obstruction_but_reducible'] = rec
                        if r % 2 and r > 1 and 'passes_parity_but_reducible' not in examples:
                            examples['passes_parity_but_reducible'] = rec
                        key = (n, i % 8, j % 8)
                        if key in parity_keys and parity_keys[key]['distinct_irreducible_factors'] % 2 != r % 2:
                            parity_failures.setdefault('same_n_and_zero_positions_mod_8',
                                                      [parity_keys[key], rec])
                        else:
                            parity_keys.setdefault(key, rec)
        by_degree.append({'n': n, **dict(local)})
    # Display a scalable obstruction with factors of unbounded degree.
    family = []
    for a in [3, 5, 7, 11, 21, 35]:
        n, i, j = 3*a-1, a-2, a
        f = candidate(n, i, j)
        G, params = predicted_gcd(n, i, j)
        expected = (1 << a)-1  # 1+x+...+x^(a-1)
        assert params['a'] == 1 and params['b'] == a and G == expected
        assert divmod_poly(f, expected)[1] == 0
        family.append({'a': a, 'n': n, 'i': i, 'j': j, 'forced_factor_degree': a-1})
    result = {'scope': {'reciprocal_gcd_all_even_degrees': [6, 100],
                        'squarefree_factor_parity_max_degree': 64,
                        'independent_irreducibility_crosscheck_max_degree': 24},
              'totals': dict(counts), 'by_degree': by_degree,
              'examples': examples, 'parity_pattern_counterexamples': parity_failures,
              'unbounded_degree_factor_family': family}
    (OUT/'findings.json').write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps({k: v for k, v in result.items() if k != 'by_degree'}, ensure_ascii=False))

if __name__ == '__main__':
    main()
