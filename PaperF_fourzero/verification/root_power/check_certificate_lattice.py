"""Strict second audit: quotient-algebra norms and integral Bezout lattices.

Standard library only. No imports from the other proof programs or builders.
Norms are determinants of multiplication by P in F2[Y,z]/(z^ell+Y),
computed by subset dynamic programming. Integer solution lattices are
constructed by unimodular column operations, without rational Cramer forms.
"""
if not __debug__:
    raise RuntimeError('Run without -O: this proof checker requires Python assertions.')

from pathlib import Path
from itertools import product
from collections import Counter, defaultdict
from functools import lru_cache, reduce
from math import gcd
from heapq import heappop, heappush
import json

HERE = Path(__file__).resolve().parent
ZERO = (0, 0, 0, 0)


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def parity(terms):
    out = set()
    for t in terms:
        if t in out:
            out.remove(t)
        else:
            out.add(t)
    return out


def multiply(a, b):
    return parity(add(x, y) for x in a for y in b)


def starting_gaps(ell, residue):
    k, i, j = residue
    return (i % ell or ell, (j-i) % ell or ell, (k-j) % ell or ell)


@lru_cache(None)
def defect(ell, residue):
    a0, b0, c0 = starting_gaps(ell, residue)
    a, b, c = (ell, 0, 0, a0), (0, ell, 0, b0), (0, 0, ell, c0)
    k = add(add(a, b), c)
    i, j = a, add(a, b)
    n = add(k, k)
    top = add(n, (0, 0, 0, 1))
    deleted = (i, j, sub(sub(n, i), (0, 0, 0, 1)),
               sub(sub(n, j), (0, 0, 0, 1)))
    # Derive (1+z)f directly from the four deleted positions.
    p = parity([ZERO, top] + [e for d in deleted for e in (d, add(d, (0, 0, 0, 1)))])
    matrix = [[set() for _ in range(ell)] for _ in range(ell)]
    for col in range(ell):
        for e in p:
            assert all(v % ell == 0 for v in e[:3])
            q, r = divmod(e[3], ell)
            row = (col + r) % ell
            yexp = tuple(v//ell for v in e[:3]) + (q + (col+r)//ell,)
            matrix[row][col] ^= {yexp}
    dp = {0: {ZERO}}
    for col in range(ell):
        nxt = {}
        for mask, poly in dp.items():
            for row in range(ell):
                if not mask >> row & 1:
                    target = mask | (1 << row)
                    nxt.setdefault(target, set()).symmetric_difference_update(
                        multiply(poly, matrix[row][col]))
        dp = nxt
    q = dp[(1 << ell)-1]
    omega = parity([sub(top, e) for e in q] +
                   [add(e, (0, 0, 0, 1)) for e in q] +
                   [ZERO, (0, 0, 0, 1), top, add(top, (0, 0, 0, 1))])
    # Existing certificates use X exponents, with Y=X^ell.
    return tuple(sorted(tuple(ell*v for v in e) for e in omega))


def bezout(a, b):
    aa, bb = abs(a), abs(b)
    old_s, s, old_t, t = 1, 0, 0, 1
    while bb:
        q = aa//bb
        aa, bb = bb, aa-q*bb
        old_s, s = s, old_s-q*s
        old_t, t = t, old_t-q*t
    return aa, old_s*(1 if a >= 0 else -1), old_t*(1 if b >= 0 else -1)


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


@lru_cache(None)
def lattice(equations):
    """All integer solutions are origin + sum(t_j*basis[j]), t_j in Z."""
    origin = (0, 0, 0)
    basis = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    for equation in equations:
        co = [dot(equation[:3], v) for v in basis]
        target = -equation[3]-dot(equation[:3], origin)
        if not any(co):
            if target:
                return None
            continue
        dimension = len(basis)
        cols = [tuple(int(i == j) for i in range(dimension)) for j in range(dimension)]
        for j in range(1, dimension):
            aa, bb = co[0], co[j]
            if not aa and not bb:
                continue
            g, s, t = bezout(aa, bb)
            old0, oldj = cols[0], cols[j]
            cols[0] = tuple(s*x+t*y for x, y in zip(old0, oldj))
            cols[j] = tuple((-bb//g)*x+(aa//g)*y for x, y in zip(old0, oldj))
            co[0], co[j] = g, 0
        if co[0] < 0:
            co[0] = -co[0]
            cols[0] = tuple(-x for x in cols[0])
        g = co[0]
        assert g > 0
        if target % g:
            return None
        transformed = [tuple(sum(basis[j][r]*column[j] for j in range(dimension))
                             for r in range(3)) for column in cols]
        origin = tuple(x+(target//g)*y for x, y in zip(origin, transformed[0]))
        basis = transformed[1:]
    answer = origin, tuple(basis)
    for e in equations:
        assert dot(e[:3], origin)+e[3] == 0
        assert all(dot(e[:3], v) == 0 for v in basis)
    return answer


@lru_cache(None)
def feasible(equations):
    description = lattice(equations)
    if description is None:
        return False
    origin, basis = description
    if len(basis) == 3:
        return True
    if not basis:
        return min(origin) >= 0
    if len(basis) == 1:
        lower = upper = None
        for p, v in zip(origin, basis[0]):
            if v > 0:
                bound = -(p//v)  # ceil(-p/v), exact for signed integers
                lower = bound if lower is None else max(lower, bound)
            elif v < 0:
                bound = p//(-v)
                upper = bound if upper is None else min(upper, bound)
            elif p < 0:
                return False
        return lower is None or upper is None or lower <= upper
    assert len(basis) == 2
    row = next(e for e in equations if any(e[:3]))
    co, target = row[:3], -row[3]
    if min(co) < 0 < max(co):
        return True  # gcd solvability already proved by the lattice construction
    if min(co) < 0:
        co, target = tuple(-v for v in co), -target
    if target < 0:
        return False
    common = reduce(gcd, map(abs, co))
    assert target % common == 0
    coins = sorted({v//common for v in co if v > 0})
    target //= common
    modulus = min(coins)
    # Apéry distances: target is representable iff the shortest nonnegative
    # semigroup value in its residue modulo the least coin is <= target.
    distances = [None]*modulus
    distances[0] = 0
    heap = [(0, 0)]
    while heap:
        distance, residue = heappop(heap)
        if distance != distances[residue]:
            continue
        for coin in coins:
            nxt, value = (residue+coin) % modulus, distance+coin
            if distances[nxt] is None or value < distances[nxt]:
                distances[nxt] = value
                heappush(heap, (value, nxt))
    value = distances[target % modulus]
    return value is not None and value <= target


def signature(e, description):
    origin, basis = description
    return tuple(dot(e[:3], v) for v in basis) + (dot(e[:3], origin)+e[3],)


def support(es, description):
    groups = defaultdict(list)
    for e in es:
        groups[signature(e, description)].append(e)
    return tuple(sorted(min(g) for g in groups.values() if len(g) % 2))


def shifted(es, t, positive):
    out = []
    for e in es:
        value = list(e)
        if positive:
            value[3] += value[t]
        else:
            value[t] = 0
        out.append(tuple(value))
    return tuple(sorted(parity(out)))


def audit_cubic():
    obj = json.loads((HERE/'cubic_certificate.json').read_text(encoding='utf-8'))
    assert [tuple(r['residue']) for r in obj['roots']] == list(product(range(3), repeat=3))
    stats = Counter()

    def visit(node, es, zeros=frozenset(), used=frozenset()):
        if node['kind'] == 'split':
            t = node['variable']
            assert t in range(3) and t not in used
            visit(node['zero'], shifted(es, t, False), zeros | {t}, used | {t})
            visit(node['positive'], shifted(es, t, True), zeros, used | {t})
            return
        assert node['kind'] == 'leaf'
        assert set(es) == {tuple(e) for e in node['exponents']}
        witness = tuple(node['witness'])
        assert witness in es
        for e in es:
            if e != witness:
                assert not feasible((sub(witness, e),))
                stats['noncollision_checks'] += 1
        stats['singleton' if len(zeros) == 3 else 'unbounded'] += 1

    for root in obj['roots']:
        r = tuple(root['residue'])
        assert starting_gaps(3, r) == tuple(root['bases'])
        visit(root['tree'], defect(3, r))
    assert stats == {'noncollision_checks': 768, 'unbounded': 41, 'singleton': 1}
    return dict(stats)


def audit_quintic():
    obj = json.loads((HERE/'quintic_classification_certificate.json').read_text(encoding='utf-8'))
    assert [tuple(r['residue']) for r in obj['roots']] == list(product(range(5), repeat=3))
    nodes, seen, stats = obj['nodes'], {}, Counter()

    def visit(idx, es, eqs, residue, path):
        assert type(idx) is int and 0 <= idx < len(nodes)
        desc = lattice(eqs)
        node = nodes[idx]
        kind = node['kind']
        if kind == 'infeasible':
            assert not feasible(eqs)
            raise AssertionError('No infeasible terminal node is expected in this certificate')
        assert desc is not None and feasible(eqs)
        es = support(es, desc)
        if idx in seen:
            old_es, old_eqs, old_residue, old_path = seen[idx]
            assert (old_es, old_residue, old_path) == (es, residue, path)
            old_desc = lattice(old_eqs)
            assert all(not any(signature(e, desc)) for e in old_eqs)
            assert all(not any(signature(e, old_desc)) for e in eqs)
            return
        seen[idx] = es, eqs, residue, path
        stats[kind] += 1
        if kind == 'allowed':
            gaps = []
            choices = dict(path)
            for t, start in enumerate(starting_gaps(5, residue)):
                e = [0, 0, 0, start + (5 if choices.get(t) == '+' else 0)]
                if choices.get(t) != '0':
                    e[t] = 5
                gaps.append(tuple(e))
            a, b, c = gaps
            if node['label'] == 'degree10_exception':
                tests = [sub(e, (0, 0, 0, v)) for e, v in zip(gaps, (3, 1, 1))]
            else:
                assert node['label'] == 'arithmetic_progression'
                tests = [add(sub(x, add(y, y)), (0, 0, 0, 1)) for x, y in [(a, b), (b, c)]]
                d = signature(b, desc)
                assert all(v % 10 == 0 for v in d[:-1]) and d[-1] % 10 in (1, 9)
            assert all(not any(signature(e, desc)) for e in tests)
            return
        assert kind in ('unique', 'collision')
        witness = tuple(node['witness'])
        assert witness in es
        children = {} if kind == 'unique' else {tuple(v['partner']): v['node'] for v in node['children']}
        if kind == 'collision':
            assert len(children) == len(node['children']) and children
        for partner in es:
            if partner == witness:
                continue
            new = eqs + (sub(witness, partner),)
            exists = feasible(new)
            stats['partner_checks'] += 1
            assert exists == (partner in children)
            if exists:
                assert len(lattice(new)[1]) < len(desc[1])
                visit(children[partner], es, new, residue, path)

    for root in obj['roots']:
        r = tuple(root['residue'])
        paths = [tuple((t, c) for t, c in leaf['path']) for leaf in root['leaves']]
        for path in paths:
            assert len({t for t, _ in path}) == len(path)
            assert all(t in range(3) and c in ('0', '+') for t, c in path)
        for assignment in product(('0', '+'), repeat=3):
            assert sum(all(assignment[t] == c for t, c in path) for path in paths) == 1
        for leaf, path in zip(root['leaves'], paths):
            es, eqs = defect(5, r), ()
            for t, choice in path:
                es = shifted(es, t, choice == '+')
                if choice == '0':
                    eqs += (tuple(int(j == t) for j in range(4)),)
            visit(leaf['node'], es, eqs, r, path)
    assert len(seen) == len(nodes) == 672
    assert stats == {'unique': 540, 'collision': 127, 'allowed': 5, 'partner_checks': 28611}
    return dict(stats)


def main():
    cubic = audit_cubic()
    print('PASS: quotient-algebra cubic norm; 27 residue classes and all 768 noncollisions', flush=True)
    quintic = audit_quintic()
    print('PASS: quotient-algebra quintic norm; all 672 nodes and 28611 partner tests', flush=True)
    receipt = {'status': 'PASS', 'norm_method': 'multiplication matrix modulo z^ell+Y; subset determinant',
               'integer_method': 'unimodular Bezout lattice; Apery semigroup distances; integer line intervals',
               'other_checkers_or_generators_imported': False,
               'domain': 'all nonnegative integer gap parameters; no degree cutoff',
               'cubic': cubic, 'quintic': quintic}
    (HERE/'certificate_lattice_check_receipt.json').write_text(json.dumps(receipt, indent=2)+'\n', encoding='utf-8')


if __name__ == '__main__':
    main()
