"""Independent symbolic checks at delicate interfaces of the general proof.

This is an exact algebraic control, not Lean and not a replacement for the
written all-parameter arguments. It imports none of the construction probes.
Coefficients are F4, omega=2; the operator indeterminate N is truncated by N^3.
"""
from itertools import product
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent


def mul4(a, b):
    value = 0
    for j in range(2):
        if b & (1 << j):
            value ^= a << j
    if value & 4:
        value ^= 7  # omega^2+omega+1
    return value


def add(*terms):
    out = {}
    for term in terms:
        for key, value in term.items():
            out[key] = out.get(key, 0) ^ value
            if out[key] == 0:
                del out[key]
    return out


def scale(a, value):
    return {key: mul4(a, coefficient) for key, coefficient in value.items()
            if mul4(a, coefficient)}


def shift(value, k=1, nilpotency=3):
    return {(degree+k, symbol): coefficient
            for (degree, symbol), coefficient in value.items()
            if degree+k < nilpotency}


def q(symbol):
    return {(0, symbol): 1}


def power4(x, n):
    value = 1
    for _ in range(n):
        value = mul4(value, x)
    return value


def anf_coordinate_coefficients(exponents):
    """F4-valued binary ANF for a reduced F4 monomial."""
    width = 2*len(exponents)
    values = []
    for bits in range(1 << width):
        value = 1
        for i, exponent in enumerate(exponents):
            value = mul4(value, power4((bits >> (2*i)) & 3, exponent))
        values.append(value)
    for i in range(width):
        for bits in range(1 << width):
            if bits & (1 << i):
                values[bits] ^= values[bits ^ (1 << i)]
    return values


def rank4(rows):
    pivots = {}
    for source in rows:
        row = list(source)
        for p in sorted(pivots):
            if row[p]:
                a = row[p]
                row = [x ^ mul4(a, y) for x, y in zip(row, pivots[p])]
        p = next((i for i, x in enumerate(row) if x), None)
        if p is not None:
            inverse = next(a for a in (1, 2, 3) if mul4(a, row[p]) == 1)
            pivots[p] = [mul4(inverse, x) for x in row]
    return len(pivots)


def main():
    omega, omega2 = 2, 3
    assert mul4(omega, omega) == omega2 and omega ^ omega2 == 1

    Q, q0, q1 = q("Q"), q("q0"), q("q1")
    # q0=NQ+omega*N^2*q1; q1=omega*N*q0+omega^2*N^2*Q.
    q1_expression = add(scale(omega, shift(q0)), scale(omega2, shift(Q, 2)))
    q0_after_substitution = add(shift(Q), scale(omega, shift(q1_expression, 2)))
    assert q0_after_substitution == shift(Q)
    q0_solution = shift(Q)
    q1_solution = add(scale(omega, shift(q0_solution)), scale(omega2, shift(Q, 2)))
    assert q1_solution == shift(Q, 2)
    residuals = [
        add(q0_solution, shift(Q), scale(omega, shift(q1_solution, 2))),
        add(q1_solution, scale(omega, shift(q0_solution)), scale(omega2, shift(Q, 2))),
        add(scale(omega, shift(q1_solution)), scale(omega2, shift(q0_solution, 2))),
    ]
    assert not any(residuals)

    # The complete intertwining equation has the form
    # (1+P)(CQ+Qprime+ta)+P*ts=0. Work modulo P^2=0.
    CQ, ta, ts = q("CQ"), q("ta"), q("ts")
    Qprime = add(CQ, ta, shift(ts, nilpotency=2))
    difference = add(CQ, Qprime, ta)
    intertwining = add(difference, shift(difference, nilpotency=2),
                      shift(ts, nilpotency=2))
    assert not intertwining
    # Multiplication by 1+P is its own inverse: no condition was lost.
    abstract = q("abstract")
    twice = add(abstract, shift(abstract, nilpotency=2))
    twice = add(twice, shift(twice, nilpotency=2))
    assert twice == abstract

    # The reduced monomial basis is compatible with the binary degree
    # filtration. Tensor independence is the written all-arity argument.
    filtration = []
    for arity in (1, 2, 3):
        rows_by_degree = {}
        for exponents in product(range(4), repeat=arity):
            coefficients = anf_coordinate_coefficients(exponents)
            expected = sum(e.bit_count() for e in exponents)
            actual = max((bits.bit_count() for bits, a in enumerate(coefficients) if a), default=-1)
            assert actual == expected
            rows_by_degree.setdefault(expected, []).append(
                [a if bits.bit_count() == expected else 0
                 for bits, a in enumerate(coefficients)])
        ranks = {degree: rank4(rows) for degree, rows in rows_by_degree.items()}
        assert all(ranks[d] == len(rows) for d, rows in rows_by_degree.items())
        filtration.append({"arity": arity, "monomial_count": 4**arity,
                           "leading_term_ranks": ranks,
                           "all_leading_terms_independent_in_each_degree": True})

    bad_patterns = [(3, 1), (1, 3), (2, 1, 1), (1, 2, 1), (1, 1, 2)]
    assert all(max(i.bit_count() for i, a in enumerate(anf_coordinate_coefficients(p)) if a) == 3
               for p in bad_patterns)
    # Check the two scalar-lift cancellations without changing conventions.
    assert omega ^ 1 ^ omega2 == 0
    assert omega ^ omega2 == 1

    result = {
        "status": "PASS",
        "scope": "Formal F4 operator identities and exact binary-degree leading terms",
        "weight_equation_residuals": [len(r) for r in residuals],
        "necessity_elimination_has_unique_q0_q1": True,
        "morphism_intertwining_residual_terms": len(intertwining),
        "morphism_inverse_factor_verified": True,
        "reduced_monomial_filtration": filtration,
        "degree_three_patterns_checked": bad_patterns,
        "scalar_lift_and_shear_conventions_verified": True,
        "limitations": [
            "Not a Lean formalization",
            "Does not by itself prove the preliminary orbit-matrix operator theorem",
            "The all-arity tensor-basis argument and intrinsic-image step remain written proofs",
            "Does not certify global originality or replace independent professional review",
        ],
    }
    (ROOT / "metabelian_symbolic_interface_audit.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()
