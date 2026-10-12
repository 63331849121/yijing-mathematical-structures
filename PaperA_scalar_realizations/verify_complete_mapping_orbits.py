"""Exact checks of complete-mapping orbit results in Paper A.

Python 3.12, standard library only; no random choices.
Enumerates all binary matrices for n <= 4 and all line spreads for n = 4.
Run: python verify_complete_mapping_orbits.py
The infinite-dimensional statements are established by the paper proofs.
"""

from fractions import Fraction
from itertools import product
from pathlib import Path
import json


def inverse(perm):
    if len(set(perm)) != len(perm):
        return None
    out = [0] * len(perm)
    for x, y in enumerate(perm):
        out[y] = x
    return tuple(out)


def rotate(perm):
    return inverse(tuple(x ^ y for x, y in enumerate(perm)))


def check_parastrophy(f, g, h):
    """Check the coordinate rotation, transposition, and J F J = F^2."""
    triples = {(x, y, x ^ y) for x, y in enumerate(f)}
    assert len(triples) == len(f)
    assert all(len({triple[i] for triple in triples}) == len(f)
               for i in range(3))
    assert {(z, x, y) for x, y, z in triples} == {
        (x, y, x ^ y) for x, y in enumerate(g)}
    j = inverse(f)
    assert {(y, x, z) for x, y, z in triples} == {
        (x, y, x ^ y) for x, y in enumerate(j)}
    assert inverse(j) == f
    assert inverse(rotate(j)) == h


def gl_order(n, q=2):
    result = 1
    for i in range(n):
        result *= q**n - q**i
    return result


def counts(n):
    total = gl_order(n) * sum(
        (Fraction((-1)**j * 2**(j*(j-1)//2), gl_order(j))
         for j in range(n+1)), Fraction())
    assert total.denominator == 1
    d = int(total)
    r = 0 if n % 2 else gl_order(n) // gl_order(n//2, 4)
    a = 2**n * d
    assert (a-r) % 3 == 0
    return dict(d_n=d, affine_complete_maps=a, F_fixed_affine_maps=r,
                three_element_orbits=(a-r)//3)


def linear_table(columns):
    out = [0] * (1 << len(columns))
    for x in range(1, len(out)):
        bit = x & -x
        out[x] = out[x ^ bit] ^ columns[bit.bit_length()-1]
    return tuple(out)


def check_affine(n):
    q = 1 << n
    invertible = valid = fixed = maps = 0
    fixed_linear = set()
    for cols in product(range(q), repeat=n):
        linear = linear_table(cols)
        if inverse(linear) is None:
            continue
        invertible += 1
        if rotate(linear) is None:
            continue
        valid += 1
        for c in range(q):
            f = tuple(x ^ c for x in linear)
            g = rotate(f)
            h = rotate(g)
            assert h == tuple(x ^ y for x, y in enumerate(inverse(f)))
            assert rotate(h) == f
            check_parastrophy(f, g, h)
            point = g[0]
            assert [x for x, y in enumerate(f) if x == y] == [point]
            maps += 1
            if g == f:
                fixed += 1
                assert c == 0
                assert all(linear[linear[x]] ^ linear[x] == x for x in range(q))
                fixed_linear.add(f)
    expected = counts(n)
    assert invertible == gl_order(n)
    assert valid == expected['d_n']
    assert maps == expected['affine_complete_maps']
    assert fixed == expected['F_fixed_affine_maps']
    return expected, fixed_linear


def line_spreads(n):
    q = 1 << n
    lines = sorted({tuple(sorted((a, b, a ^ b)))
                    for a in range(1, q) for b in range(a+1, q)})
    masks = [sum(1 << (x-1) for x in line) for line in lines]
    containing = {x: [i for i, line in enumerate(lines) if x in line]
                  for x in range(1, q)}
    full = (1 << (q-1))-1
    found = []

    def search(covered, chosen):
        if covered == full:
            found.append(tuple(lines[i] for i in chosen))
            return
        bit = (full ^ covered) & -(full ^ covered)
        point = bit.bit_length()
        for i in containing[point]:
            if masks[i] & covered == 0:
                search(covered | masks[i], chosen + (i,))

    search(0, ())
    return lines, found


def main():
    result = {'affine': {}}
    fixed4 = None
    for n in range(1, 5):
        row, fixed_linear = check_affine(n)
        result['affine'][str(n)] = row
        if n == 4:
            fixed4 = fixed_linear
    # Larger rows are exact evaluations of the proved formula, not enumeration.
    result['formula_rows'] = {str(n): counts(n) for n in (5, 6, 8)}
    lines, spreads = line_spreads(4)
    assert len(lines) == 35 and len(spreads) == 56
    seen = set()
    linear_count = 0
    nonlinear_witness = None
    for spread in spreads:
        for orientations in product((0, 1), repeat=len(spread)):
            f = [0] * 16
            for (a, b, c), reverse in zip(spread, orientations):
                cycle = (a, c, b) if reverse else (a, b, c)
                for i, x in enumerate(cycle):
                    f[x] = cycle[(i+1) % 3]
            f = tuple(f)
            assert f not in seen
            seen.add(f)
            assert rotate(f) == f
            check_parastrophy(f, f, f)
            assert all(f[f[x]] == x ^ f[x] for x in range(16))
            additive = all(f[x ^ y] == f[x] ^ f[y]
                           for x in range(16) for y in range(16))
            assert additive == (f in fixed4)
            linear_count += additive
            if not additive and nonlinear_witness is None:
                bad_pair = next((x, y) for x in range(16) for y in range(16)
                                if f[x ^ y] != f[x] ^ f[y])
                nonlinear_witness = dict(values=list(f), nonadditive_pair=list(bad_pair))
    assert len(seen) == 1792 and linear_count == 112
    result['spread_n4'] = dict(projective_lines=35, line_spreads=56,
        orientations_per_spread=32, F_fixed_complete_maps=1792,
        linear=112, nonlinear=1680, spreads=spreads,
        nonlinear_witness=nonlinear_witness)
    result['parastrophy_checks'] = dict(
        affine_maps_checked=sum(row['affine_complete_maps']
                                for row in result['affine'].values()),
        oriented_spread_maps_checked=len(seen),
        identities=['rho(Gamma_f)=Gamma_F(f)',
                    'sigma(Gamma_f)=Gamma_inverse(f)',
                    'J^2=id', 'JFJ=F^2'])
    target = Path(__file__).resolve().parent / 'complete_mapping_results.json'
    target.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'affine': result['affine'],
                     'spread_n4': {k: v for k, v in result['spread_n4'].items()
                                   if k not in ('spreads', 'nonlinear_witness')}}, indent=2))
    print('All complete-mapping checks passed.')


if __name__ == '__main__':
    main()
