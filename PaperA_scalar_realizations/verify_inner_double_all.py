"""Exact finite arithmetic for the all-dimensional double-order proof.

No certificate finder or exploratory arithmetic program is imported.
All small-prime lists are reconstructed by deterministic trial division.
Large factors in the omega certificates are never presumed prime.
"""
from pathlib import Path
from math import gcd, prod, isqrt
from fractions import Fraction
import hashlib
import json

from verify_inner_critical import check_primes, check_row
from verify_inner_mixed import check_double

ROOT = Path(__file__).resolve().parent


def primes_up_to(limit):
    return [p for p in range(2,limit+1)
            if all(p % q for q in range(2,isqrt(p)+1))]


def omega_certificate(row, s, primes, trial_bound):
    t = 1 << s
    bounds = []
    for key, number in [('A',t+1),('B',t*t+1)]:
        data = row[key]
        remaining = number
        factors = []
        for p in primes:
            if remaining % p == 0:
                exponent = 0
                while remaining % p == 0:
                    remaining //= p
                    exponent += 1
                factors.append([p,exponent])
        assert factors == data['small_factors']
        assert str(remaining) == data['remainder']
        assert prod(p**e for p,e in factors) * remaining == number
        assert all(remaining % p for p in primes)
        k = data['large_factor_count_bound']
        assert k >= 0
        assert (trial_bound+1)**k <= remaining < (trial_bound+1)**(k+1)
        assert data['omega_bound'] == len(factors)+k
        bounds.append(data['omega_bound'])
    r = sum(bounds)
    assert row['omega_d_bound'] == r
    assert gcd(t+1,t*t+1) == 1
    # sqrt(t)>=4*2^r is sufficient for the diagonal lower bound.
    assert s >= 4+2*r
    assert (1 << s) >= 16 * (1 << (2*r))
    return {'s':s,'omega_A_bound':bounds[0],'omega_B_bound':bounds[1],
            'omega_d_bound':r,'positivity_margin':s-4-2*r}


def small_diagonal(row, prove):
    E,L = check_row(row,prove)
    s = row['s']
    t,A,B = 1<<s,(1<<s)+1,(1<<(2*s))+1
    d = A*B
    pa,pb = set(row['A_factors']),set(row['B_factors'])
    assert gcd(A,B) == 1
    unit = (1,0)
    gamma_generator = L.power((0,1),A)
    assert L.power(gamma_generator,B) == unit
    assert all(L.power(gamma_generator,B//p) != unit for p in pb)
    tau_logs = {}
    b = int(row['b_hex'],16)
    w = 1
    for j in range(A):
        tau_logs[w] = j
        w = E.mul(w,b)
    assert len(tau_logs) == A and w == 1
    gamma = unit
    population = primitive = 0
    exponents = []
    for i in range(B):
        if gamma != unit:
            inverse_gamma = L.power(gamma,B-1)
            assert inverse_gamma == L.power(gamma,t*t)
            tau = (gamma[0]^inverse_gamma[0],gamma[1]^inverse_gamma[1])
            assert tau[1] == 0
            if tau[0] in tau_logs:
                population += 1
                j = tau_logs[tau[0]]
                # Check the descent coordinates and actual Lang function.
                y = L.power(gamma,t)
                h = L.mul(L.power(y,t),inverse_gamma)
                assert h == L.power(gamma,t*t-1)
                one_plus = (gamma[0]^1,gamma[1])
                w0 = L.mul(L.mul(one_plus,one_plus),inverse_gamma)
                assert w0 == tau
                assert L.power(w0,A) == unit
                if gcd(i,B) == gcd(j,A) == 1:
                    primitive += 1
                    exponents.append([i,j])
                    a = L.power(one_plus,t**4-2)
                    translated = (a[0]^1,a[1])
                    assert translated == L.power(a,t*t)
                    assert L.power(a,B) == (E.power(tau[0],E.size-2),0)
                    assert L.power(a,t*t-1) == gamma
                    for z in [a,translated]:
                        assert L.power(z,d) == unit
                        assert all(L.power(z,d//p) != unit for p in pa|pb)
        gamma = L.mul(gamma,gamma_generator)
    assert gamma == unit
    assert (population-A)**2 <= 4*t
    theta = prod((Fraction(p-1,p) for p in pa|pb),start=Fraction(1))
    W = 1 << len(pa|pb)
    error = Fraction(primitive)-theta*A
    assert error*error <= theta*theta*(4*W-2)**2*t
    return {'s':s,'norm_one_fiber_population':population,'diagonal_double_count':primitive,
            'primitive_character_main_term':str(theta*A),'order_pairs_verified':len(exponents)}


def main():
    if not __debug__:
        raise RuntimeError('Run without -O.')
    data = json.loads((ROOT/'inner_double_omega_certificates.json').read_text(encoding='utf-8'))
    assert data['prime_trial_bound'] == 4096
    assert data['analytic_cutoff'] == 114 and data['range'] == [33,113]
    primes = primes_up_to(4096)
    small = [p for p in primes if 2<p<256]
    assert len(small) == 53
    assert str(prod(small)) == data['small_prime_product']
    assert data['constant_power_of_two'] == 12
    assert 256**53 < 4096**8*prod(small)
    assert [r['s'] for r in data['rows']] == list(range(33,114))
    verified_omega = [omega_certificate(row,row['s'],primes,4096) for row in data['rows']]
    print('Verified all 81 omega bounds s=33..113 and the uniform divisor constant.',flush=True)

    old = json.loads((ROOT/'inner_critical_certificates.json').read_text(encoding='utf-8'))
    doubles = json.loads((ROOT/'inner_double_order_certificates.json').read_text(encoding='utf-8'))
    originals = {r['s']:r for r in old['certificates']}
    assert sorted(originals) == list(range(2,33))
    assert [r['s'] for r in doubles['certificates']] == list(range(2,33))
    prove = check_primes(old['prime_certificates'])
    verified_double = []
    for row in doubles['certificates']:
        verified_double.append(check_double(row,originals[row['s']],prove))
        print(f"s={row['s']}: both exact orders independently reverified.",flush=True)
    small_counts = [small_diagonal(originals[s],prove) for s in range(2,7)]
    assert [r['diagonal_double_count'] for r in small_counts if r['s'] in [3,5]] == [0,0]
    result = {'omega_bound_range':[33,113],'number_of_omega_cases':81,
              'verified_omega':verified_omega,'uniform_divisor_constant':4096,
              'uniform_analytic_range_s_at_least':114,
              'double_certificate_range':[2,32],'number_of_double_certificates':31,
              'double_certificates':verified_double,'small_diagonal_range':[2,6],
              'small_diagonal_counts':small_counts,
              'inputs_sha256':{n:hashlib.sha256((ROOT/n).read_bytes()).hexdigest() for n in
                 ['inner_double_omega_certificates.json','inner_double_order_certificates.json',
                  'inner_critical_certificates.json','verify_inner_critical.py','verify_inner_mixed.py']},
              'scope':'Finite exact arithmetic only. The infinite conclusion also requires the separately proved diagonal Lang-cover bound.'}
    output = ROOT/'inner_double_all_verification.json'
    if output.exists():
        assert json.loads(output.read_text(encoding='utf-8')) == result
    else:
        output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('All finite ranges of the double-order closure proof verified.',flush=True)
    print(json.dumps(small_counts))


if __name__ == '__main__':
    main()
