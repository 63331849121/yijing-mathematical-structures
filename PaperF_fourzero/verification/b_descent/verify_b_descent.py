"""Bounded independent checks for the explicit B-family descent.

Standard-library Python only.  Coefficient at x^j is bit j.
No irreducibility search or factorization is performed.  The all-parameter
identity is justified separately by the written telescoping proof.
"""

from pathlib import Path
import hashlib
import json


HERE = Path(__file__).resolve().parent
HISTORICAL = HERE.parent / "rational_transform/classification_audit.json"


def mul(a, b):
    out = 0
    while b:
        if b & 1:
            out ^= a
        a <<= 1
        b >>= 1
    return out


def compose(a, b):
    out = 0
    for j in range(a.bit_length() - 1, -1, -1):
        out = mul(out, b) ^ ((a >> j) & 1)
    return out


def reverse(a, degree):
    return sum(((a >> j) & 1) << (degree - j) for j in range(degree + 1))


def family(r):
    q = 1 << (r - 1)
    n = 2 * q + 2
    zeros = (3, q, q + 1, 2 * q - 2)
    assert len(set(zeros)) == 4
    assert set(zeros) == {3, q, n - 1 - 3, n - 1 - q}
    out = (1 << (n + 1)) - 1
    for j in zeros:
        out ^= 1 << j
    return out


def closed_descent(r):
    q = 1 << (r - 1)
    bracket = 1 << q
    for t in range(2, r - 1):
        bracket ^= 1 << (q - (1 << t) + 1)
    return 0b111 ^ bracket ^ (bracket << 1)


def homogeneous_horner(h):
    """Evaluate D^m h(N/D), N=X^2, D=X+1, using Horner."""
    m = h.bit_length() - 1
    out = 1
    denominator_power = 1
    for j in range(m - 1, -1, -1):
        denominator_power ^= denominator_power << 1
        out <<= 2
        if (h >> j) & 1:
            out ^= denominator_power
    return out


def descend_by_elimination(f, m):
    """Recover h from f using distinct leading degrees of its basis images."""
    powers = [1]
    for _ in range(m):
        powers.append(powers[-1] ^ (powers[-1] << 1))
    residual = f
    h = 0
    for j in range(m, -1, -1):
        # The image of x^j is X^(2j)(X+1)^(m-j), of degree m+j.
        if (residual >> (m + j)) & 1:
            h ^= 1 << j
            residual ^= powers[m - j] << (2 * j)
    assert residual == 0
    return h


def run():
    history = json.loads(HISTORICAL.read_text(encoding="utf-8"))
    expected = {row["r"]: row["h"] for row in history["remaining_family_diagnostic"]}
    rows = []
    for r in range(3, 11):
        q = 1 << (r - 1)
        m = q + 1
        h = closed_descent(r)
        f = family(r)
        assert h.bit_length() - 1 == m
        assert h & 0b111 == 0b111
        assert h.bit_count() == 2 * r - 1
        assert homogeneous_horner(h) == f
        assert descend_by_elimination(f, m) == h
        assert h == int(expected[r], 16)

        trace = sum(1 << (1 << i) for i in range(r - 1))
        frev = reverse(h, m) << 1
        frev_rhs = (0b111 << q) ^ mul(0b11, trace ^ 0b100)
        assert frev == frev_rhs
        # L(s+s^2)=s+s^q, checked by generic polynomial composition.
        assert compose(trace, 0b110) == (1 << 1) ^ (1 << q)
        # The exponent reversal verifies the Laurent-polynomial proof identity.
        left = compose(frev, 0b110)
        assert left.bit_length() - 1 == 2 * q + 4
        cleared = reverse(left, 2 * q + 4)
        assert cleared == (f ^ (f << 1))
        rows.append({
            "R": r, "q": q, "output_degree": 2 * q + 2,
            "descent_degree": m, "h_hex": hex(h),
            "empty_sum": r == 3,
            "checks": ["homogeneous Horner transform", "triangular inverse",
                       "historical descent equality", "degree and low coefficients",
                       "reverse partial-trace identity", "trace telescoping",
                       "cleared-denominator identity"]
        })
    summary = {
        "status": "PASS", "range": "3 <= R <= 10", "cases": len(rows),
        "factorization_or_irreducibility_tests": 0,
        "all_parameter_basis": "Written algebraic telescoping proof; finite checks are supplementary.",
        "priority_claim": "None. Mathematical correctness is not global novelty certification.",
        "historical_input": str(HISTORICAL),
        "historical_sha256": hashlib.sha256(HISTORICAL.read_bytes()).hexdigest(),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "rows": rows,
    }
    (HERE / "b_descent_audit.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": summary["status"], "cases": len(rows),
                      "range": summary["range"], "factorization_tests": 0}))


if __name__ == "__main__":
    run()
