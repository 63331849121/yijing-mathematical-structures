"""Independent full audit of the historical Paper F counts and first witnesses.

Requires python-flint==0.9.0 (FLINT 3.6.0). No original search routine is imported.
Data factor lists are untrusted inputs: prove each listed factor prime and divide
each 2**n-1 completely, recovering every prime-power multiplicity.
"""
import argparse
from collections import Counter
import hashlib
from itertools import combinations
import json
from math import comb
from pathlib import Path
import sys
import time

parser = argparse.ArgumentParser()
parser.add_argument('--data', type=Path, required=True)
parser.add_argument('--out', type=Path, default=Path(__file__).resolve().parent)
parser.add_argument('--deps', type=Path)
args = parser.parse_args()
if args.deps:
    sys.path.insert(0, str(args.deps.resolve()))
import flint
from flint import fmpz, fmpz_mod_poly_ctx, nmod_poly

R = fmpz_mod_poly_ctx(2)
X = nmod_poly([0, 1], 2)
ONE = nmod_poly([1], 2)


def dump(name, obj):
    args.out.mkdir(parents=True, exist_ok=True)
    (args.out / name).write_text(json.dumps(obj, indent=2), encoding='utf-8')


def load(name):
    return json.loads((args.data / name).read_text(encoding='utf-8'))


def polynomial(n, i, j):
    # Construct coefficients directly, independently of the old bit-string code.
    coeffs = [1] * (n + 1)
    for a in (i, j, n - 1 - i, n - 1 - j):
        coeffs[a] = 0
    assert sum(c == 0 for c in coeffs[:-1]) == 4
    assert coeffs[:-1] == list(reversed(coeffs[:-1]))
    return coeffs


def verdict(n, i, j, primes, certificate=False):
    coeffs = polynomial(n, i, j)
    # Separate explicit irreducibility test, absent from the historical code.
    if not R(coeffs).is_irreducible():
        return 'R', None
    f = nmod_poly(coeffs, 2)
    M = (1 << n) - 1
    assert X.pow_mod(M, f) == ONE
    residues = {}
    for p in primes:
        a = X.pow_mod(M // p, f)
        if a == ONE:
            return 'I', {'order_divisor': str(p)}
        if certificate:
            residues[str(p)] = hex(sum(int(c) << d for d, c in enumerate(a.coeffs())))
    if certificate:
        return 'P', {'n': n, 'i': i, 'j': j,
                     'polynomial_hex': hex(sum(c << d for d, c in enumerate(coeffs))),
                     'irreducible': True, 'full_power_is_one': True,
                     'proper_order_test_residues': residues}
    return 'P', None


def pure_mod(a, f):
    while a.bit_length() >= f.bit_length():
        a ^= f << (a.bit_length() - f.bit_length())
    return a


def pure_mul(a, b, f):
    # Unreduced carryless product, then long division: different from old code.
    out = 0
    while b:
        if b & 1:
            out ^= a
        a <<= 1
        b >>= 1
    return pure_mod(out, f)


def pure_pow(a, exponent, f):
    out = 1
    for bit in bin(exponent)[2:]:
        out = pure_mul(out, out, f)
        if bit == '1':
            out = pure_mul(out, a, f)
    return out


def pure_gcd(a, b):
    while b:
        a, b = b, pure_mod(a, b)
    return a


def small_factors(m):
    out = []
    p = 2
    while p * p <= m:
        if m % p == 0:
            out.append(p)
            while m % p == 0:
                m //= p
        p += 1
    if m > 1:
        out.append(m)
    return out


def pure_verdict(n, i, j, primes):
    coeffs = polynomial(n, i, j)
    f = sum(c << d for d, c in enumerate(coeffs))
    frob = [2]
    for _ in range(n):
        frob.append(pure_mul(frob[-1], frob[-1], f))
    if frob[n] != 2 or any(pure_gcd(frob[n // q] ^ 2, f) != 1 for q in small_factors(n)):
        return 'R'
    assert pure_pow(2, (1 << n) - 1, f) == 1
    if any(pure_pow(2, ((1 << n) - 1) // p, f) == 1 for p in primes):
        return 'I'
    return 'P'


def main():
    start = time.time()
    factor_text = (args.data / '_fourzero_factors_6_300.txt').read_text(encoding='utf-8')
    factors = {int(n): [int(p) for p in s.split(',')]
               for n, s in (line.split(':') for line in factor_text.splitlines() if line.strip())}
    assert set(factors) == set(range(6, 301, 2))
    primes = sorted({p for row in factors.values() for p in row})
    prime_records = []
    for p in primes:
        # fmpz_is_prime is a proof-producing decision procedure, not BPSW-only.
        assert fmpz(p).is_prime() == 1, ('nonprime_factor', p)
        prime_records.append({'p': str(p), 'bits': p.bit_length(), 'flint_is_prime': True})
    factorizations = []
    for n, row in sorted(factors.items()):
        assert row == sorted(set(row))
        residual = (1 << n) - 1
        powers = []
        for p in row:
            assert residual % p == 0
            e = 0
            while residual % p == 0:
                residual //= p
                e += 1
            powers.append({'p': str(p), 'e': e})
        assert residual == 1, ('incomplete_factorization', n, residual)
        factorizations.append({'n': n, 'prime_powers': powers, 'residual': '1'})
    cache = load('_factordb_2n_minus_1_cache.json')
    for n, row in cache.items():
        if int(n) in factors:
            assert sorted(set(row)) == factors[int(n)]
    dump('factor_audit.json', {'python_flint': flint.__version__,
        'flint': flint.__FLINT_VERSION__, 'test': 'fmpz_is_prime (rigorous)',
        'unique_proven_primes': len(primes), 'prime_records': prime_records,
        'factorizations': factorizations})
    print(f'factor audit PASS: {len(primes)} primes, {len(factors)} complete factorizations', flush=True)

    old = load('_四零回文本原计数_6到200.json')
    assert [row['n'] for row in old] == list(range(6, 201, 2))
    counts = []
    witnesses = []
    all_verdicts = []
    total_cases = 0
    total_primitive = 0
    pure_checks = 0
    metadata_corrections = []
    corrected_old = []
    for row in old:
        n = row['n']
        clock = time.time()
        successful = []
        status = []
        for i, j in combinations(range(1, n // 2), 2):
            label, _ = verdict(n, i, j, factors[n])
            if n <= 24:
                assert pure_verdict(n, i, j, factors[n]) == label
                pure_checks += 1
            status.append(label)
            if label == 'P':
                successful.append([i, j])
        assert len(status) == comb(n // 2 - 1, 2) == row['leaves']
        assert len(successful) == row['primitive'], ('count_mismatch', n, len(successful), row)
        assert successful[0] == [row['first_i'], row['first_j']]
        first_i1 = next((j for i, j in successful if i == 1), None)
        if first_i1 != row['first_j_i1']:
            metadata_corrections.append({'n': n, 'field': 'first_j_i1',
                                         'old': row['first_j_i1'], 'corrected': first_i1,
                                         'count_unchanged': True, 'first_pair_unchanged': True})
        corrected_old.append(dict(row, first_j_i1=first_i1))
        assert abs(len(successful) / len(status) - row['ratio']) <= 0.00000051
        _, cert = verdict(n, *successful[0], factors[n], certificate=True)
        witnesses.append(cert)
        counts.append({'n': n, 'candidates': len(status), 'primitive': len(successful),
                       'irreducible': status.count('I') + status.count('P'),
                       'first': successful[0], 'first_j_i1': first_i1,
                       'primitive_pairs': successful, 'matches_historical': True,
                       'seconds': round(time.time() - clock, 3)})
        all_verdicts.append({'n': n, 'order': 'lexicographic i,j',
                             'legend': 'R=reducible,I=irreducible nonprimitive,P=primitive',
                             'verdicts': ''.join(status)})
        total_cases += len(status)
        total_primitive += len(successful)
        dump('counts_6_200.json', counts)
        print(f'n={n}: {len(successful)} primitive / {len(status)} candidates; PASS; {time.time()-clock:.2f}s', flush=True)
    assert total_cases == 161700 and total_primitive == 2663
    dump('candidate_verdicts_6_200.json', all_verdicts)
    dump('corrected_historical_counts_6_200.json', corrected_old)

    extended = load('_四零首解_202到250.json') + load('_四零首解_252到300.json')
    assert [row['n'] for row in extended] == list(range(202, 301, 2))
    extended_results = []
    extended_cases = 0
    for row in extended:
        n = row['n']
        tested = 0
        labels = []
        first = None
        for i, j in combinations(range(1, n // 2), 2):
            label, cert = verdict(n, i, j, factors[n], certificate=True)
            labels.append(label)
            tested += 1
            if label == 'P':
                first = [i, j]
                witnesses.append(cert)
                break
        assert first == row['found'], ('first_mismatch', n, first, row)
        assert tested == row['tested'], ('tested_mismatch', n, tested, row)
        extended_results.append({'n': n, 'first': first, 'tested': tested,
                                 'preceding_verdicts_including_first': ''.join(labels),
                                 'matches_historical': True})
        extended_cases += tested
        dump('first_solutions_202_300.json', extended_results)
        print(f'n={n}: first {first} after {tested}; PASS', flush=True)
    dump('first_witness_certificates_6_300.json', witnesses)
    input_files = ['_fourzero_factors_6_300.txt', '_factordb_2n_minus_1_cache.json',
                   '_四零回文本原计数_6到200.json', '_四零首解_202到250.json', '_四零首解_252到300.json']
    summary = {'status': 'PASS', 'python_flint': flint.__version__, 'flint': flint.__FLINT_VERSION__,
               'factor_degrees': 148, 'unique_proven_prime_factors': len(primes),
               'largest_prime_bits': max(primes).bit_length(),
               'complete_count_degrees': 98, 'complete_candidates': total_cases,
               'primitive_total_6_200': total_primitive,
               'pure_python_crosscheck_candidates_n_le_24': pure_checks,
               'extended_first_degrees': 50, 'extended_tested_candidates': extended_cases,
               'witness_certificates': len(witnesses),
               'metadata_corrections': metadata_corrections,
               'seconds': round(time.time() - start, 3),
               'input_sha256': {name: hashlib.sha256((args.data/name).read_bytes()).hexdigest() for name in input_files},
               'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
               'limitations': ['Finite computations do not prove existence in all even degrees.',
                               'FLINT proof decisions are software results, not exported primality certificates or Lean proofs.',
                               'No claim of a new primitivity test or search-complexity improvement.']}
    dump('summary.json', summary)
    print(json.dumps(summary, indent=2), flush=True)


if __name__ == '__main__':
    main()
