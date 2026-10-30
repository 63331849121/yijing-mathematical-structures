"""Exact checks tying the manuscript's coordinates to the rank certificates.

No certificate-generator code is imported. Low-weight evaluation is exhaustive
for the relevant binary degree bounds, not a probabilistic sample.
"""
from itertools import combinations, product
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent


def mul(a, b):
    c = 0
    for j in range(2):
        if b & (1 << j):
            c ^= a << j
    return c ^ 7 if c & 4 else c


MUL = [[mul(a, b) for b in range(4)] for a in range(4)]


def chain(v):
    a, b, c, d, e, h, r, s = v + [0] * (8-len(v))
    m = lambda x, y: MUL[x][y]
    sq = lambda x: m(x, x)
    out = [m(2, x) for x in (a, b, c, d, e, h, r, s)]
    out[2] ^= m(a, b)
    out[3] ^= m(a, c) ^ m(sq(a), b)
    out[4] ^= m(b, c) ^ m(a, sq(b))
    out[5] ^= m(a, e) ^ m(b, d)
    out[6] ^= m(a, sq(c)) ^ m(sq(a), e) ^ m(a, h) ^ m(c, d)
    out[7] ^= m(b, sq(c)) ^ m(sq(b), d) ^ m(b, h) ^ m(c, e)
    return out[:len(v)]


def unpack(x, n):
    return [(x >> (2*i)) & 3 for i in range(n//2)]


def pack(v):
    return sum(x << (2*i) for i, x in enumerate(v))


def points(n, degree):
    yield 0
    for k in range(1, min(n, degree)+1):
        for indices in combinations(range(n), k):
            yield sum(1 << i for i in indices)


def basis(rows):
    pivots = {}
    for row in rows:
        while row:
            p = row.bit_length()-1
            if p not in pivots:
                pivots[p] = row
                break
            row ^= pivots[p]
    return list(pivots.values())


def bracket(table, x, y):
    out = 0
    for i in range(len(table)):
        if (x >> i) & 1:
            for j in range(len(table)):
                if (y >> j) & 1:
                    out ^= table[i][j]
    return out


def q_pair(v):
    a, b, c = v[:3]
    m = lambda x, y: MUL[x][y]
    if len(v) == 3:
        return m(a,c)^m(m(a,a),b), m(b,c)^m(a,m(b,b))
    d, e, h = v[3:6]
    return (m(a,m(c,c))^m(m(a,a),e)^m(a,h)^m(c,d),
            m(b,m(c,c))^m(m(b,b),d)^m(b,h)^m(c,e))


if __name__ == '__main__':
    records = []
    invariants = {
        4: (4,[4,0],0), 6: (2,[6,2,0],0),
        8: (2,[8,4,2,0],0), 10: (4,[10,6,4,0],0),
        12: (2,[12,8,6,2,0],0),
        14: (2,[14,10,8,4,2,0],2),
        16: (4,[16,12,10,6,4,0],4)
    }
    for n in invariants:
        cert = json.loads((ROOT/'chain_rank_certificates'/f'n{n}_rank_certificate.json').read_text())
        def G(x):
            return pack(chain(unpack(x,n)))
        def stored_G(x):
            out = 0
            for mask, coefficient in zip(cert['quadratic_input_masks'],cert['quadratic_map_coefficients']):
                if (x & mask) == mask:
                    out ^= coefficient
            return out
        assert all(G(x) == stored_G(x) for x in points(n,2))
        assert all(G(G(x)) == (G(x)^x) for x in points(n,4))
        table = [[G((1<<i)^(1<<j))^G(1<<i)^G(1<<j) for j in range(n)] for i in range(n)]
        B = lambda x,y: bracket(table,x,y)
        for i,j,k in combinations(range(n),3):
            a,b,c = 1<<i,1<<j,1<<k
            assert B(a,B(b,c))^B(b,B(c,a))^B(c,B(a,b)) == 0
        for i,j,k,l in combinations(range(n),4):
            a,b,c,d = 1<<i,1<<j,1<<k,1<<l
            assert B(B(a,b),B(c,d))^B(B(a,c),B(b,d))^B(B(a,d),B(b,c)) == 0
        derived = basis(table[i][j] for i in range(n) for j in range(i))
        series = [n,len(derived)]
        current = derived
        while current:
            current = basis(B(1<<i,v) for i in range(n) for v in current)
            series.append(len(current))
        center_rows = [sum(((table[i][j]>>k)&1)<<i for i in range(n))
                       for j in range(n) for k in range(n)]
        center = n-len(basis(center_rows))
        second = len(basis(B(x,y) for x in derived for y in derived))
        expected_center, expected_series, expected_second = invariants[n]
        assert (center,series,second) == (expected_center,expected_series,expected_second)
        records.append({'n':n,'status':'PASS','center_dimension':center,
                        'lower_central_dimensions':series,'second_derived_dimension':second,
                        'formula_matches_certificate':True})

    orbit_records = []
    for n in (6,12):
        for kind in ('swap','shear','diagonal2','diagonal3'):
            lam = int(kind[-1]) if kind.startswith('diagonal') else 1
            def S(v):
                out = v[:]
                a,b,c = v[:3]
                if kind == 'swap':
                    out[0],out[1] = b,a
                    if n == 12:
                        out[3],out[4] = v[4],v[3]
                elif kind == 'shear':
                    out[0] = a^b
                    out[2] = c^MUL[b][b]
                    if n == 12:
                        out[3] = v[3]^v[4]
                else:
                    out[0],out[2] = MUL[lam][a],MUL[lam][c]
                    if n == 12:
                        out[3] = MUL[MUL[lam][lam]][v[3]]
                        out[4] = MUL[lam][v[4]]
                        out[5] = MUL[MUL[lam][lam]][v[5]]
                return out
            for x in points(n,2):
                v = unpack(x,n)
                assert S(chain(v)) == chain(S(v))
                u,w = q_pair(v)
                if kind == 'swap':
                    expected = w,u
                elif kind == 'shear':
                    if n == 6:
                        expected = u^w,w
                    else:
                        a,b = v[:2]
                        expected = u^w^MUL[a][b]^MUL[b][b],w^MUL[b][b]
                elif n == 6:
                    expected = MUL[MUL[lam][lam]][u],MUL[lam][w]
                else:
                    expected = u,MUL[MUL[lam][lam]][w]
                assert q_pair(S(v)) == expected
            orbit_records.append({'n':n,'automorphism':kind,'status':'PASS'})
    result = {'status':'PASS','chain_records':records,'projective_orbit_records':orbit_records,
              'method':'Exact degree-two or degree-four Boolean coefficient recovery',
              'not_Lean_formalization':True}
    (ROOT/'manuscript_transcription_checks.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(result))
