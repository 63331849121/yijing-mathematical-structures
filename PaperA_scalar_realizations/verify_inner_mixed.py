"""Exact finite checks accompanying the mixed-character proof.

Checks s=2..32 double-order certificates and all norm fibers for s=2..6.
The analytic proof is not inferred from these finite checks.
"""
from pathlib import Path
from math import gcd, prod
from fractions import Fraction
from collections import defaultdict
import hashlib
import json

from verify_inner_critical import (
    BinaryField, TowerField, check_primes, check_row, intersection_degree,
)

ROOT = Path(__file__).resolve().parent


def theta(n, primes):
    return prod((Fraction(p-1, p) for p in primes), start=Fraction(1))


def theta2(n, primes):
    return prod((Fraction(p*p-1, p*p) for p in primes), start=Fraction(1))


def check_double(row, old, prove):
    s = row['s']
    t, A, B = 1 << s, (1 << s)+1, (1 << (2*s))+1
    d = A*B
    pa, pb = set(old['A_factors']), set(old['B_factors'])
    assert prod(old['A_factors']) == A and prod(old['B_factors']) == B
    assert set(row['prime_factors']) == pa | pb
    assert all(prove(p) for p in pa | pb)
    E = BinaryField(int(row['E_modulus_hex'], 16))
    assert E.n == 2*s
    E.check_irreducible()
    b, w, c = (int(row[k+'_hex'], 16) for k in ('b', 'w', 'c'))
    assert all(0 < k < E.size for k in (b, w, c))
    assert c == 1 ^ b ^ w
    assert E.power(b, A) == E.power(w, A) == 1
    assert all(E.power(b, A//p) != 1 and E.power(w, A//p) != 1 for p in pa)
    assert E.power(b, row['w_exponent']) == w
    assert gcd(row['w_exponent'], A) == 1
    tr = E.mul(b, E.power(c, E.size-3))
    assert E.trace(tr) == row['absolute_trace'] == 1
    L = TowerField(E, b, c)
    roots = [(0, 1), (1, 1)]
    residues = []
    for a in roots:
        assert L.power(a, d) == (1, 0)
        values = {str(p): L.power(a, d//p) for p in sorted(pa | pb)}
        assert all(z != (1, 0) for z in values.values())
        residues.append({p: [hex(z[0]), hex(z[1])] for p, z in values.items()})
    assert L.power(roots[0], B) == (b, 0)
    assert L.power(roots[1], B) == (w, 0)
    # Evaluate the two corrected Lang functions at the certificate point.
    # The ambient field has t^4 elements, so inverse(z)=z^(t^4-2).
    inv = lambda z: L.power(z, t**4-2)
    a, one_plus_a = roots
    y = L.power(a, t)
    one_plus_y = (y[0] ^ 1, y[1])
    r0 = L.mul(a, y)
    r0_plus = L.mul(one_plus_a, one_plus_y)
    assert r0 == L.power(a, A)
    assert r0_plus == L.power(one_plus_a, A)
    g1 = L.mul((E.power(b, E.size-2), 0),
               L.mul(L.power(y, t-1), inv(L.power(a, A))))
    g2 = L.mul((E.power(w, t), 0),
               L.mul(L.power(one_plus_y, t-1), inv(L.power(one_plus_a, A))))
    assert g1 == inv(L.power(r0, 2))
    assert g2 == inv(L.power(r0_plus, 2))
    return {'s': s, 'irreducible': True, 'absolute_trace': 1,
            'both_exact_order': d, 'a_power_d_over_p': residues[0],
            'one_plus_a_power_d_over_p': residues[1]}


def small_fibers(old, prove):
    E, L = check_row(old, prove)
    s = old['s']
    t, A, B = 1 << s, (1 << s)+1, (1 << (2*s))+1
    d = A*B
    pa, pb = set(old['A_factors']), set(old['B_factors'])
    logs = {}
    x, y = 1, 0
    for j in range(d):
        z = x | (y << E.n)
        assert z not in logs
        logs[z] = j
        x, y = E.mul(L.b, y), x ^ E.mul(L.c, y)
    assert (x, y) == (1, 0)
    fibers = defaultdict(list)
    for z, j in logs.items():
        if z ^ 1 in logs:
            fibers[j % A].append((j, logs[z ^ 1]))
    thetaA, thetaB = theta(A, pa), theta(B, pb)
    theta2A, theta2B = theta2(A, pa), theta2(B, pb)
    WA, WB = 2**len(pa), 2**len(pb)
    HA = prod((Fraction(p+2, p+1) for p in pa), start=Fraction(1))
    lambdas = []
    lambda2 = []
    records = []
    for j in range(A):
        data = fibers[j]
        J = [p for p in pa if j % p == 0]
        lam = prod((Fraction(p-1, p) for p in J), start=Fraction(1))
        lambdas.append(lam)
        lambda2.append(lam * 2**len(J))
        Rb = sum(gcd(d, h, k) == 1 for h, k in data)
        Db = sum(gcd(h, d) == gcd(k, d) == 1 for h, k in data)
        good = 3*j % A != 0
        assert len(data) <= 2*A
        if good:
            assert (len(data)-A)**2 <= 4*t
            c = lam*theta2B
            assert (Rb-c*A)**2 <= t*(c*(8*2**len(J)*WB-6))**2
            if gcd(j, A) == 1:
                cc = thetaA*thetaB**2
                assert (Db-cc*A)**2 <= t*(cc*(8*WA*WB**2-6))**2
        if gcd(j, A) != 1:
            assert Db == 0
        # Chinese remaindering separates the two generation conditions.
        for h, k in data:
            assert h % A == j
            assert (gcd(d, h, k) == 1) == (gcd(A, j, k) == gcd(B, h, k) == 1)
        records.append({'norm_index': j, 'good_eight_boundary_model': good,
                        'primitive_norm': gcd(j, A) == 1,
                        'J_b': sorted(J), 'lambda_A': str(lam),
                        'population': len(data), 'R_d_b': Rb, 'D_d_b': Db})
    assert sum(lambdas) == A*theta2A
    assert sum(lambda2) == A*theta2A*HA
    T, R, D = (sum(row[k] for row in records) for k in ('population', 'R_d_b', 'D_d_b'))
    assert T == intersection_degree(d)
    cR = theta2A*theta2B
    # Bound a*sqrt(t)+b via the slightly weaker squared bound with sqrt(t)>=1.
    assert (R-cR*A*A)**2 <= t*(cR*A*(8*HA*WB-6)+2*gcd(3,A)*A)**2
    cD = (thetaA*thetaB)**2
    assert (D-cD*A*A)**2 <= t*(cD*A*(8*WA*WB**2-6))**2
    expected = [(24,24,8),(86,72,24),(240,240,208),(1214,960,240),(4104,3960,1992)]
    assert (T,R,D) == expected[s-2]
    return {'s': s, 't': t, 'T_d': T, 'R_d': R, 'D_d': D, 'fibers': records,
            'sum_lambda': str(sum(lambdas)), 'sum_lambda_2J': str(sum(lambda2))}


def check_inertia_arithmetic():
    for s in range(2, 201):
        t = 1 << s
        A, B = t+1, t*t+1
        assert gcd(A, B) == gcd(t-1, B) == 1
        # determinant of the two B-inertia vectors (-A,-1),(-A,-t)
        assert gcd(A*(t-1), B) == 1
    return {'integer_parameter_checks': [2, 200],
            'universal_identity': 'A(t-1)=B-2, hence gcd(A(t-1),B)=1'}


def main():
    if not __debug__:
        raise RuntimeError('Exact verification requires assertions; do not use -O.')
    old = json.loads((ROOT/'inner_critical_certificates.json').read_text(encoding='utf-8'))
    new = json.loads((ROOT/'inner_double_order_certificates.json').read_text(encoding='utf-8'))
    assert new['range'] == [2,32]
    assert [r['s'] for r in new['certificates']] == list(range(2,33))
    original = {r['s']: r for r in old['certificates']}
    prove = check_primes(old['prime_certificates'])
    verified = []
    for row in new['certificates']:
        verified.append(check_double(row, original[row['s']], prove))
        print(f"s={row['s']}: both exact orders and norm certificates verified.", flush=True)
    counts = [small_fibers(original[s], prove) for s in range(2,7)]
    result = {'double_certificate_range': [2,32], 'number_of_certificates': len(verified),
              'double_certificate_sha256': hashlib.sha256((ROOT/'inner_double_order_certificates.json').read_bytes()).hexdigest(),
              'all_norm_fiber_count_range': [2,6], 'exact_small_counts': counts,
              'double_certificates': verified, 'inertia_integer_checks': check_inertia_arithmetic(),
              'scope': 'Finite exact arithmetic only; does not prove the analytic character bound or all-dimensional double existence.'}
    out = ROOT/'inner_mixed_verification.json'
    if out.exists():
        assert json.loads(out.read_text(encoding='utf-8')) == result
    else:
        out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('Verified double-order certificates for s=2..32 and all norm fibers for s=2..6.',flush=True)
    print(json.dumps([{'s': r['s'],'R_d':r['R_d'],'D_d':r['D_d']} for r in counts]))


if __name__ == '__main__':
    main()
