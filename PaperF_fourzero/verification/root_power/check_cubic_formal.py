"""Independent exact checker. Does not import the builder, old rounds, or Z3.

Symbolic norm is recomputed with the F2 cubic formula, while the builder uses
three factors over F4. All exponent-collision refutations are checked locally.
"""
if not __debug__:
    raise RuntimeError('Run without -O: this proof checker requires Python assertions.')

from pathlib import Path
from itertools import product
from collections import Counter
from math import gcd
from functools import reduce
import json

BASE=Path(__file__).resolve().parent

def xor_terms(terms):
    p=set()
    for e in terms:
        e=tuple(e)
        if e in p:p.remove(e)
        else:p.add(e)
    return p

def add(e,f):return tuple(a+b for a,b in zip(e,f))
def sub(e,f):return tuple(a-b for a,b in zip(e,f))
def pmul(a,b):return xor_terms(add(e,f) for e in a for f in b)

def independent_defect(r):
    p={(0,0,0,0),(2,0,0,1),
       (0,1,0,0),(0,1,0,1),(0,0,1,0),(0,0,1,1),
       (2,-1,0,-1),(2,-1,0,0),(2,0,-1,-1),(2,0,-1,0)}
    cs=[set() for _ in range(3)]
    for e in p:cs[(sum(e[t]*r[t] for t in range(3))+e[3])%3].add(e)
    cubes=[pmul(pmul(s,s),s) for s in cs]
    norm=cubes[0]^cubes[1]^cubes[2]^pmul(cs[0],pmul(cs[1],cs[2]))
    top=(6,0,0,3)
    defect=xor_terms([sub(top,e) for e in norm]+[add(e,(0,0,0,3)) for e in norm]+
                     [(0,0,0,0),(0,0,0,3),(6,0,0,3),(6,0,0,6)])
    a=r[1] or 3;b=(r[2]-r[1])%3 or 3;c=(r[0]-r[2])%3 or 3
    def change(e):
        return (3*(e[0]+e[1]+e[2]),3*(e[0]+e[2]),3*e[0],
                e[0]*(a+b+c)+e[1]*a+e[2]*(a+b)+e[3])
    return xor_terms(change(e) for e in defect),(a,b,c)

def verify_no_collision(proof,d):
    assert tuple(proof['difference'])==d
    v=d[:3];t=-d[3];kind=proof['kind']
    if kind=='constant':assert all(x==0 for x in v) and t!=0
    elif kind=='gcd':
        g=reduce(gcd,map(abs,v),0)
        assert g==proof['gcd'] and g>0 and t%g!=0
    elif kind in ('sign','coin'):
        assert not(any(x>0 for x in v) and any(x<0 for x in v))
        if any(x<0 for x in v):v=tuple(-x for x in v);t=-t
        assert all(x>=0 for x in v)
        if kind=='sign':assert t<0
        else:
            assert t>=0 and t==proof['target']
            coins=sorted(set(x for x in v if x));assert coins==proof['coins']
            reached={0}
            for k in range(t+1):
                if k in reached:
                    reached.update(k+c for c in coins if k+c<=t)
            assert sorted(reached)==proof['reachable'] and t not in reached
    else:raise AssertionError(kind)

def visit(node,expected,stats,depth=0,zero_variables=frozenset(),used=frozenset(),domains=None):
    if node['kind']=='leaf':
        es=[tuple(e) for e in node['exponents']]
        assert len(es)==len(set(es)) and set(es)==expected
        w=tuple(node['witness']);assert w in expected
        others=[e for e in es if e!=w]
        assert len(others)==len(node['noncollision'])
        for e,proof in zip(others,node['noncollision']):
            verify_no_collision(proof,sub(w,e));stats[proof['kind']]+=1
        stats['leaves']+=1;stats['depth_'+str(depth)]+=1
        assert domains is not None
        domains['unbounded' if len(zero_variables)<3 else 'singleton']+=1
        return
    assert node['kind']=='split'
    t=node['variable'];assert t in range(3)
    assert t not in used
    left=[];right=[]
    for e in expected:
        a=list(e);a[t]=0;left.append(tuple(a))
        a=list(e);a[3]+=a[t];right.append(tuple(a))
    # These disjoint branches cover all nonnegative integers: variable=0 or >=1.
    visit(node['zero'],xor_terms(left),stats,depth+1,zero_variables|{t},used|{t},domains)
    visit(node['positive'],xor_terms(right),stats,depth+1,zero_variables,used|{t},domains)

def main():
    obj=json.loads((BASE/'cubic_certificate.json').read_text(encoding='utf-8'))
    rs=[tuple(root['residue']) for root in obj['roots']]
    assert rs==list(product(range(3),repeat=3))
    stats=Counter()
    domains=Counter()
    for root in obj['roots']:
        expected,bases=independent_defect(root['residue'])
        assert list(bases)==root['bases']
        visit(root['tree'],expected,stats,domains=domains)
    assert dict(stats)==obj['summary'] and stats['leaves']==42
    assert domains==dict(unbounded=41,singleton=1)
    out=dict(status='PASS',independent_norm='F2 cubic formula; no F4 code imported',
             parameter_domain='all integer k>=3, 1<=i<j<k; no upper bound',
             certificate_checks=dict(stats),parameter_regions=dict(domains),SMT_used_by_checker=False)
    (BASE/'cubic_formal_check_receipt.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
    print('PASS: independent norm expansion, 27 residues / 41 unbounded regions + 1 singleton')
    print('PASS: every unique coefficient checked by constant, gcd, sign or finite coin refutation')
    print('PASS: standard-library-only checker; no SMT oracle; no bound on n')

if __name__=='__main__':main()
