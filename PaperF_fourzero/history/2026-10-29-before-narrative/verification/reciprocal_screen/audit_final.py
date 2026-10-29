"""Final reproducible audit; supplements the bounded base probe."""
import importlib.util
import json
import math
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('factor_probe_base', ROOT/'probe_factors.py')
p = importlib.util.module_from_spec(spec)
spec.loader.exec_module(p)

def prime_factors(n):
    result = []
    q = 2
    while q*q <= n:
        if n % q == 0:
            result.append(q)
            while n % q == 0:
                n //= q
        q += 1
    if n > 1:
        result.append(n)
    return result

def factor_small(f):
    result = []
    for d in range(1, p.degree(f)//2+1):
        for g in range((1 << d) | 1, 1 << (d+1), 2):
            if d > 1 and not p.irreducible(g):
                continue
            m = 0
            while f != 1:
                q, r = p.divmod_poly(f, g)
                if r:
                    break
                f = q
                m += 1
            if m:
                result.append({'factor_hex': hex(g), 'degree': d, 'multiplicity': m})
        if f == 1:
            break
    if f != 1:
        assert p.irreducible(f)
        result.append({'factor_hex': hex(f), 'degree': p.degree(f), 'multiplicity': 1})
    return result

def main():
    p.main()
    data = json.loads((ROOT/'findings.json').read_text(encoding='utf-8'))
    for row in data['by_degree']:
        N = row['n']+1
        phi, S2 = N, N
        for q in prime_factors(N):
            phi = phi//q*(q-1)
            S2 = S2//q*(q-2)
        survivors = row['candidates']-row['nontrivial_reciprocal_obstruction']
        assert survivors == math.comb(phi//2, 2)-(S2-1)//2
        row.update(reciprocal_screen_survivors=survivors, closed_count_phi=phi,
                   closed_count_S2=S2, closed_count_verified=True)
    records = list(data['examples'].values())
    records += [x for pair in data['parity_pattern_counterexamples'].values() for x in pair]
    for rec in records:
        rec['exact_factorization'] = factor_small(int(rec['polynomial_hex'], 16))
        product = 1
        for term in rec['exact_factorization']:
            for _ in range(term['multiplicity']):
                product = p.mul(product, int(term['factor_hex'], 16))
        assert product == int(rec['polynomial_hex'], 16)
    for rec in data['unbounded_degree_factor_family']:
        a = rec['a']
        quotient = sum(1 << e for e in [2*a, a+1, a-1, a-2, 0])
        assert p.mul((1 << a)-1, quotient) == p.candidate(rec['n'], rec['i'], rec['j'])
        rec['pentanomial_quotient_hex'] = hex(quotient)
    generic_checks = 0
    for n in range(2, 22, 2):
        k = n//2
        for mask in range(1 << (k-1)):
            half = 1 | (mask << 1)
            f = 1 << n
            for i in range(k):
                if (half >> i) & 1:
                    f ^= (1 << i) | (1 << (n-1-i))
            common = p.gcd(f, p.reciprocal(f))
            assert p.divmod_poly((1 << (n+1)) ^ 1, common)[1] == 0
            assert p.gcd(common, p.derivative(common)) == 1
            generic_checks += 1
    data['all_tail_palindromic_constant_one_checks_up_to_degree_20'] = generic_checks
    data['audit_source_hashes'] = {
        name: hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
        for name in ['probe_factors.py', 'audit_final.py']}
    (ROOT/'audit_final.json').write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps({'final_audit': 'passed', 'gcd_candidates': data['totals']['all_gcd_checks'],
        'excluded_by_reciprocal_obstruction': sum(x['nontrivial_reciprocal_obstruction'] for x in data['by_degree']),
        'closed_count_degrees_checked': len(data['by_degree']),
        'generic_tail_palindromes_checked': generic_checks}, ensure_ascii=False))

if __name__ == '__main__':
    main()
