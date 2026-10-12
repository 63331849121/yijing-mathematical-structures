"""Finite checks for the structural extension of Paper A (local v2.39).

Standard library only. Direct permutation-group closure is compared with the
proved formula for every translation at each matrix-similarity representative,
n <= 4. Linear conjugacy transports these cases to all admissible matrices.
All 1792 four-dimensional F-fixed maps are classified under all of GL(4,2).
The general statements have paper proofs; these computations support them.
"""

from collections import Counter, deque
from itertools import product
from pathlib import Path
import json

from verify_complete_mapping_orbits import inverse, line_spreads, linear_table, rotate, gl_order


def compose(f, g):
    return tuple(f[x] for x in g)


def closure(generators):
    identity = tuple(range(len(generators[0])))
    seen = {identity}
    queue = deque([identity])
    while queue:
        h = queue.popleft()
        for g in generators:
            next_h = compose(g, h)
            if next_h not in seen:
                seen.add(next_h)
                queue.append(next_h)
    return seen


def span(vectors):
    result = {0}
    for v in vectors:
        result |= {x ^ v for x in tuple(result)}
    return result


def cyclic_space(a, c, n):
    vectors = []
    for _ in range(n):
        vectors.append(c)
        c = a[c]
    return span(vectors)


def elementary_generators(n):
    q = 1 << n
    return [tuple(x ^ ((1 << i) if x & (1 << j) else 0) for x in range(q))
            for i in range(n) for j in range(n) if i != j]


def conjugacy_orbit(f, generators):
    seen = {f}
    queue = deque([f])
    while queue:
        h = queue.popleft()
        for s in generators:  # These elementary transvections are involutions.
            next_h = compose(s, compose(h, s))
            if next_h not in seen:
                seen.add(next_h)
                queue.append(next_h)
    return seen


def all_subspaces(n):
    spaces = {frozenset({0})}
    queue = deque(spaces)
    while queue:
        space = queue.popleft()
        for x in range(1 << n):
            if x not in space:
                larger = frozenset(set(space) | {y ^ x for y in space})
                if larger not in spaces:
                    spaces.add(larger)
                    queue.append(larger)
    return spaces


def primitive_direct(generators, group):
    """Find nontrivial blocks by closing equivalence relations under generators."""
    q = len(generators[0])
    if len({h[0] for h in group}) != q:
        return False
    for other in range(1, q):
        parent = list(range(q))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            x, y = find(x), find(y)
            if x == y:
                return False
            parent[y] = x
            return True

        union(0, other)
        changed = True
        while changed:
            changed = False
            for g in generators:
                for x in range(q):
                    for y in range(x):
                        if find(x) == find(y):
                            changed |= union(g[x], g[y])
        block_size = sum(find(x) == find(0) for x in range(q))
        if 1 < block_size < q:
            return False
    return True


def order(f):
    current = tuple(range(len(f)))
    count = 0
    while True:
        current = compose(f, current)
        count += 1
        if current == tuple(range(len(f))):
            return count


def affine_checks():
    result = {}
    gl4 = None
    for n in range(1, 5):
        q = 1 << n
        gl = sorted({linear_table(columns) for columns in product(range(q), repeat=n)
                     if len(set(linear_table(columns))) == q})
        assert len(gl) == gl_order(n)
        gl_with_inverse = [(s, inverse(s)) for s in gl]
        if n == 4:
            gl4 = gl_with_inverse
        valid = {a for a in gl if rotate(a) is not None}
        remaining = set(valid)
        generators = elementary_generators(n)
        subspaces = all_subspaces(n)
        cases = []
        group_order_counts = Counter()
        action_counts = Counter()
        closure_cases = 0
        while remaining:
            a = min(remaining)
            orbit = conjugacy_orbit(a, generators)
            full_orbit = {compose(s, compose(a, inv_s)) for s, inv_s in gl_with_inverse}
            assert orbit == full_orbit and orbit <= remaining
            remaining -= orbit
            b = rotate(a)
            multiplier_group = closure((a, b))
            irreducible = not any(1 < len(u) < q and {a[x] for x in u} == set(u)
                                  for u in subspaces)
            translations = []
            for c in range(q):
                f = tuple(x ^ c for x in a)
                g = rotate(f)
                assert g == tuple(x ^ b[c] for x in b)
                direct = closure((f, g))
                u = cyclic_space(a, c, n)
                predicted = {tuple(m[x] ^ v for x in range(q))
                             for m in multiplier_group for v in u}
                assert direct == predicted
                pure_translations = {h[0] for h in direct if all(h[x] == x ^ h[0] for x in range(q))}
                assert pure_translations == u
                transitive = len({h[0] for h in direct}) == q
                primitive = primitive_direct((f, g), direct)
                double = transitive and len({h[1] for h in direct if h[0] == 0}) == q - 1
                assert transitive == (len(u) == q)
                assert primitive == (c != 0 and irreducible)
                assert double == (c != 0 and irreducible and len(multiplier_group) == q - 1)
                group_order_counts[len(direct)] += len(orbit)
                action_counts['transitive'] += len(orbit) * transitive
                action_counts['primitive'] += len(orbit) * primitive
                action_counts['doubly_transitive'] += len(orbit) * double
                translations.append(dict(c=c, cyclic_dimension=len(u).bit_length()-1,
                                         group_order=len(direct), transitive=transitive,
                                         primitive=primitive, doubly_transitive=double))
                closure_cases += 1
            cases.append(dict(matrix_columns=[a[1 << i] for i in range(n)],
                matrix_conjugacy_class_size=len(orbit), order_A=order(a), order_B=order(b),
                multiplier_group_order=len(multiplier_group), irreducible=irreducible,
                translations=translations))
        assert sum(group_order_counts.values()) == q * len(valid)
        result[str(n)] = dict(admissible_matrices=len(valid), matrix_conjugacy_classes=len(cases),
            direct_closure_cases=closure_cases, affine_pairs_covered_by_linear_conjugacy=q*len(valid),
            group_order_distribution={str(k): v for k, v in sorted(group_order_counts.items())},
            action_counts=dict(action_counts), cases=cases)
    return result, gl4


def fixed_map_checks(gl):
    _, spreads = line_spreads(4)
    all_maps = set()
    for spread in spreads:
        for bits in product((0, 1), repeat=5):
            f = [0] * 16
            for (a, b, c), bit in zip(spread, bits):
                cycle = (a, c, b) if bit else (a, b, c)
                for i, x in enumerate(cycle):
                    f[x] = cycle[(i+1) % 3]
            all_maps.add(tuple(f))
    assert len(all_maps) == 1792
    omega = (0, 2, 3, 1)
    base = tuple(omega[x & 3] | (omega[x >> 2] << 2) for x in range(16))
    standard = sorted({tuple(sorted((x, base[x], base[base[x]]))) for x in range(1, 16)})
    assert len(standard) == 5
    spread_set = set(standard)
    stabilizer = []
    for s, inv_s in gl:
        if {tuple(sorted(s[x] for x in line)) for line in standard} == spread_set:
            stabilizer.append((s, inv_s))
    assert len(gl) == 20160 and len(stabilizer) == 360
    records, all_orbits = [], set()
    for r, orbit_size, stabilizer_size in ((0,112,180), (1,560,36), (2,1120,18)):
        f = list(base)
        for line in standard[:r]:
            for x in line:
                f[x] = base[base[x]]
        f = tuple(f)
        assert rotate(f) == f
        orbit = {compose(s, compose(f, inv_s)) for s, inv_s in gl}
        assert orbit == conjugacy_orbit(f, elementary_generators(4))
        assert len(orbit) == orbit_size and orbit <= all_maps
        assert not (orbit & all_orbits)
        all_orbits |= orbit
        centralizer = [s for s, _ in gl if compose(s, f) == compose(f, s)]
        assert len(centralizer) == stabilizer_size
        additive = all(f[x ^ y] == f[x] ^ f[y] for x in range(16) for y in range(16))
        assert additive == (r == 0)
        records.append(dict(reversed_lines=r, representative_values=list(f),
            GL_orbit_size=orbit_size, GL_stabilizer_order=stabilizer_size,
            fixed_spread_orbit_size=orbit_size//56, linear=additive,
            GL_stabilizer_matrices=[[s[1 << i] for i in range(4)] for s in centralizer]))
    assert all_orbits == all_maps

    burnside_sum = 0
    signature_counts = Counter()
    for s, inv_s in stabilizer:
        permutation = [standard.index(tuple(sorted(s[x] for x in line))) for line in standard]
        flips = [int(s[base[line[0]]] != base[s[line[0]]]) for line in standard]
        assert len(set(flips)) == 1
        cycles, unused = [], set(range(5))
        while unused:
            start = min(unused)
            cycle, x = [], start
            while x in unused:
                unused.remove(x)
                cycle.append(x)
                x = permutation[x]
            assert x == start
            cycles.append(cycle)
        consistent = all(sum(flips[i] for i in cycle) % 2 == 0 for cycle in cycles)
        formula_count = (1 << len(cycles)) if consistent else 0
        direct_count = 0
        for bits in product((0,1), repeat=5):
            if all(bits[permutation[i]] == bits[i] ^ flips[i] for i in range(5)):
                direct_count += 1
        assert formula_count == direct_count
        burnside_sum += direct_count
        signature_counts[(tuple(sorted(len(c) for c in cycles)), flips[0], formula_count)] += 1
    assert burnside_sum == 1080 and burnside_sum // len(stabilizer) == 3
    return dict(GL_order=len(gl), standard_spread=standard,
        standard_spread_stabilizer_order=len(stabilizer), line_spreads=len(spreads),
        fixed_maps=len(all_maps), GL_conjugacy_classes=records,
        burnside_fixed_orientation_sum=burnside_sum, burnside_orientation_classes=3,
        burnside_signatures=[dict(line_cycle_lengths=list(key[0]), global_flip=key[1],
            fixed_orientations=key[2], matrices=count) for key, count in sorted(signature_counts.items())])


def main():
    assert __debug__, 'Run ordinary Python without -O.'
    affine, gl = affine_checks()
    fixed = fixed_map_checks(gl)
    result = dict(revision='local-v2.39', encoding='integer vectors; low bit first matrix columns',
        group_verification='direct permutation closure at all matrix-class representatives and every translation; complete GL conjugacy transport for n<=4',
        affine=affine, fixed_map_n4=fixed)
    target = Path(__file__).resolve().parent / 'affine_groups_and_conjugacy_results.json'
    target.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(dict(affine={n:{k:v for k,v in row.items() if k != 'cases'} for n,row in affine.items()},
        n4_GL_orbit_sizes=[r['GL_orbit_size'] for r in fixed['GL_conjugacy_classes']],
        n4_stabilizer_orders=[r['GL_stabilizer_order'] for r in fixed['GL_conjugacy_classes']],
        Burnside_orientation_classes=fixed['burnside_orientation_classes']), indent=2))
    print('All affine-group and conjugacy checks passed.')


if __name__ == '__main__':
    main()
