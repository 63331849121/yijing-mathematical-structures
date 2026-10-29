"""Independent linear-algebra cross-checks and revision consistency checks."""
from pathlib import Path
import importlib.util
import hashlib
import json
import math
import re
from fractions import Fraction

ROOT = Path(__file__).resolve().parent.parent
V = ROOT/'verification/reciprocal_screen'
spec = importlib.util.spec_from_file_location('bounded_factor_probe',V/'probe_factors.py')
p = importlib.util.module_from_spec(spec)
spec.loader.exec_module(p)

def rank(columns):
    # Sylvester multiplication map, independent of Euclidean gcd computation.
    rows = {}
    for column in columns:
        while column:
            pivot = column.bit_length()-1
            if pivot in rows:
                column ^= rows[pivot]
            else:
                rows[pivot] = column
                break
    return len(rows)

def main():
    sylvester_checks = 0
    for n in range(6,42,2):
        for i in range(1,n//2):
            for j in range(i+1,n//2):
                f = p.candidate(n,i,j)
                fs = p.reciprocal(f)
                common, data = p.predicted_gcd(n,i,j)
                columns = [f << r for r in range(n)]+[fs << r for r in range(n)]
                assert 2*n-rank(columns) == p.degree(common)
                # Verify the exact displayed factor, not only its degree.
                assert p.divmod_poly(f,common)[1] == p.divmod_poly(fs,common)[1] == 0
                sylvester_checks += 1
    integer_checks = 0
    prime_power_examples = []
    for n in range(6,302,2):
        for i in range(1,n//2):
            A = (1 << i)+(1 << (n-1-i))
            expected = (1 << math.gcd(n//2,2*i+1))+1
            actual = math.gcd(A,(1 << n)-1)
            assert actual == expected
            if expected > 3 and len(prime_power_examples) < 5:
                prime_power_examples.append({'n':n,'i':i,'gcd':expected})
            integer_checks += 1
    pair_checks = 0
    for N in range(2,201):
        for m in range(N+1):
            mu = Fraction(m,N)
            assert Fraction(m*(m-1),N*(N-1))-mu*mu == -mu*(1-mu)/(N-1)
            pair_checks += 1
    source = (ROOT/'PaperF_fourzero.tex').read_text(encoding='utf-8')
    assert 'conj:negcorr' not in source
    assert 'negative-association signal' not in source
    assert r'\asymp 1/(p\log p)' not in source
    labels = re.findall(r'\\label\{([^}]+)\}',source)
    assert len(labels) == len(set(labels))
    refs = re.findall(r'\\(?:eqref|ref)\{([^}]+)\}',source)
    assert not (set(refs)-set(labels))
    bib = set(re.findall(r'\\bibitem\{([^}]+)\}',source))
    cites = set(x for group in re.findall(r'\\cite(?:\[[^]]*\])?\{([^}]+)\}',source)
                for x in group.split(','))
    assert cites <= bib
    data = json.loads((ROOT/'_四零回文本原计数_6到200.json').read_text(encoding='utf-8-sig'))
    assert sum(x['primitive'] for x in data) == 2663
    by_n = {x['n']:x['primitive'] for x in data}
    count_table = source[source.index(r'\label{sec:computations}'):source.index(r'\subsection{A finite-population identity}')]
    rows = re.findall(r'^(\d+) & (\d+) & (\d+) &',count_table,re.M)
    for n,candidates,primitive in rows:
        n = int(n)
        assert int(candidates) == math.comb(n//2-1,2)
        assert int(primitive) == by_n[n]
    assert len(rows) == 11
    en = (ROOT/'abstract_en.txt').read_text(encoding='utf-8').strip()
    zh = (ROOT/'abstract_zh.txt').read_text(encoding='utf-8').strip()
    assert en in (ROOT/'arXiv_submission_form.txt').read_text(encoding='utf-8')
    form = (ROOT/'ChinaXiv_submission_form.txt').read_text(encoding='utf-8')
    assert en in form and zh in form
    tex_abstract = re.search(r'\\begin\{abstract\}(.*?)\\end\{abstract\}',source,re.S)[1]
    tex_plain = tex_abstract.replace(r'\(', '').replace(r'\)', '').replace(r'\mathbb F_2','F2')
    assert ' '.join(tex_plain.split()) == ' '.join(en.split())
    result = {'status':'passed','sylvester_rank_checks':sylvester_checks,
              'integer_gcd_full_multiplicity_checks':integer_checks,
              'finite_population_fraction_checks':pair_checks,
              'sample_nontrivial_integer_gcds':prime_power_examples,
              'retained_count_table_rows_checked':len(rows),'old_count_total':2663,
              'all_labels_and_citations_resolve_in_source':True,
              'abstract_and_submission_form_consistency':True,
              'reviewed_tex_sha256':hashlib.sha256((ROOT/'PaperF_fourzero.tex').read_bytes()).hexdigest(),
              'proof_review':[
                  'Reciprocity: constant term one and even-degree tail symmetry explicit.',
                  'Binomial gcd: odd N makes S_n squarefree; use lcm, not a product with duplicate roots.',
                  'Infinite family: m odd, m>=3; both factors nonconstant and legal positions.',
                  'Position count: zero coordinates removed before a free action of order eight.',
                  'Endpoint class 1 removed with (Schemmel_2(N)-1)/2 neighbors.',
                  'Finite-population identity is universal and supplies no arithmetic dependence.',
                  'Integer gcd proof works modulo the whole gcd, preserving prime-power multiplicities.']}
    (ROOT/'verification/strict_revision_review.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(result,ensure_ascii=False))

if __name__ == '__main__':
    main()
