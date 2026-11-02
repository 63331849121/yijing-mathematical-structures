"""Independent classification checker: circulant determinant + Cramer parametrization.

No imports from generators, old rounds, SymPy, or SMT. Builder uses F16 and
Gaussian elimination; this checker uses F2 determinant terms and small minors.
"""
if not __debug__:
    raise RuntimeError('Run without -O: this proof checker requires Python assertions.')

from pathlib import Path
from itertools import product,permutations,combinations
from fractions import Fraction as F
from functools import lru_cache,reduce
from math import gcd,lcm,ceil,floor
from collections import defaultdict,Counter
import json

BASE=Path(__file__).resolve().parent
COUNTS=Counter();CHECKED={}

def parity(terms):
    out=set()
    for t in terms:
        if t in out:out.remove(t)
        else:out.add(t)
    return out
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def minus(a,b):return tuple(x-y for x,y in zip(a,b))
def pmul(a,b):return parity(add(e,f) for e in a for f in b)

@lru_cache(None)
def fifth_form():
    terms=[]
    for perm in permutations(range(5)):
        e=[0]*5
        for row in range(5):e[(perm[row]-row)%5]+=1
        terms.append(tuple(e))
    return tuple(sorted(parity(terms)))

@lru_cache(None)
def raw_defect(r):
    P={(0,0,0,0),(2,0,0,1),(0,1,0,0),(0,1,0,1),(0,0,1,0),(0,0,1,1),
       (2,-1,0,-1),(2,-1,0,0),(2,0,-1,-1),(2,0,-1,0)}
    parts=[set() for _ in range(5)]
    for e in P:parts[(sum(e[t]*r[t] for t in range(3))+e[3])%5].add(e)
    norm=set()
    for monomial in fifth_form():
        term={(0,0,0,0)}
        for j,m in enumerate(monomial):
            # Compute each power afresh, independently of the builder's power table.
            for _ in range(m):term=pmul(term,parts[j])
        norm ^= term
    top=(10,0,0,5)
    return parity([minus(top,e) for e in norm]+[add(e,(0,0,0,5)) for e in norm]+
                  [(0,0,0,0),(0,0,0,5),(10,0,0,5),(10,0,0,10)])

def bases(r):return (r[1] or 5,(r[2]-r[1])%5 or 5,(r[0]-r[2])%5 or 5)
def to_gaps(e,r):
    a,b,c=bases(r)
    return (5*(e[0]+e[1]+e[2]),5*(e[0]+e[2]),5*e[0],
            e[0]*(a+b+c)+e[1]*a+e[2]*(a+b)+e[3])

def determinant(a):
    if not a:return F(1)
    if len(a)==1:return F(a[0][0])
    return sum(((-1)**j)*a[0][j]*determinant([row[:j]+row[j+1:] for row in a[1:]]) for j in range(len(a)))

@lru_cache(None)
def system(equations):
    """Return all real solutions x_j=sum(coeff[j,t]*free_t)+constant[j]."""
    equations=tuple(tuple(map(F,e)) for e in equations)
    nrows=len(equations);rank=0;pivots=();selected=();matrix=[]
    for size in range(min(3,nrows),0,-1):
        found=False
        for cols in combinations(range(3),size):
            for rows in combinations(range(nrows),size):
                candidate=[[equations[i][j] for j in cols] for i in rows]
                if determinant(candidate):
                    rank=size;pivots=cols;selected=rows;matrix=candidate;found=True;break
            if found:break
        if found:break
    free=tuple(j for j in range(3) if j not in pivots)
    forms=[[F(0)]*4 for _ in range(3)]
    for j in free:forms[j][j]=1
    if rank:
        det=determinant(matrix)
        for h,j in enumerate(pivots):
            for t in list(free)+[3]:
                rhs=[-equations[i][t] for i in selected]
                replaced=[row[:] for row in matrix]
                for i in range(rank):replaced[i][h]=rhs[i]
                forms[j][t]=determinant(replaced)/det
    bad=False
    for e in equations:
        co=[sum(e[j]*forms[j][t] for j in range(3)) for t in range(3)]
        const=e[3]+sum(e[j]*forms[j][3] for j in range(3))
        assert not any(co),'Coefficient rank or Cramer implementation is inconsistent'
        if const:bad=True
    return rank,free,tuple(tuple(row) for row in forms),bad

def reduce_expression(e,description):
    rank,free,forms,bad=description;assert not bad
    return tuple(sum(F(e[j])*forms[j][t] for j in range(3))+(F(e[3]) if t==3 else 0) for t in range(4))

@lru_cache(None)
def integer_feasible(equations):
    rank,free,forms,bad=system(equations)
    if bad:return False
    if rank==0:return True
    if rank==1:
        row=next(e for e in equations if any(e[:3]));co=row[:3];target=-row[3]
        assert all(F(x).denominator==1 for x in row)
        co=tuple(map(int,co));target=int(target)
        common=reduce(gcd,map(abs,co),0)
        if target%common:return False
        if min(co)<0<max(co):return True
        if min(co)<0:co=tuple(-x for x in co);target=-target
        if target<0:return False
        reachable={0}
        for t in range(target+1):
            if t in reachable:reachable.update(t+c for c in co if c>0 and t+c<=target)
        return target in reachable
    if rank==3:return all(row[3]>=0 and row[3].denominator==1 for row in forms)
    assert rank==2 and len(free)==1
    t=free[0];lower=F(0);upper=None
    for row in forms:
        a,b=row[t],row[3]
        if a>0:lower=max(lower,-b/a)
        elif a<0:upper=-b/a if upper is None else min(upper,-b/a)
        elif b<0:return False
    low=ceil(lower);high=floor(upper) if upper is not None else None
    if high is not None and low>high:return False
    period=lcm(*(v.denominator for row in forms for v in (row[t],row[3])))
    COUNTS['largest_line_period']=max(COUNTS['largest_line_period'],period)
    for residue in range(period):
        if all((row[t]*residue+row[3]).denominator==1 for row in forms):
            first=low+(residue-low)%period
            if high is None or first<=high:return True
    return False

def reduced_support(es,description):
    groups=defaultdict(list)
    for e in es:groups[reduce_expression(e,description)].append(e)
    return tuple(sorted(min(xs) for xs in groups.values() if len(xs)%2))

def gap_forms(r,path):
    starts=bases(r);choices=dict(path);forms=[]
    for t in range(3):
        v=[0,0,0,starts[t]]
        if choices.get(t)!='0':v[t]=5
        if choices.get(t)=='+':v[3]+=5
        forms.append(tuple(v))
    return forms

def check_allowed(label,r,path,description):
    a,b,c=gap_forms(r,path)
    if label=='arithmetic_progression':
        assert r in ((1,2,1),(3,1,2))
        for x,y in ((a,b),(b,c)):
            e=tuple(x[j]-2*y[j]+(1 if j==3 else 0) for j in range(4))
            assert not any(reduce_expression(e,description))
    else:
        assert label=='degree10_exception'
        for row,value in zip((a,b,c),(3,1,1)):
            e=tuple(row[j]-(value if j==3 else 0) for j in range(4))
            assert not any(reduce_expression(e,description))

def visit(idx,es,equations,r,path,nodes):
    description=system(equations)
    if description[3]:es=()
    else:es=reduced_support(es,description)
    signature=(es,equations,r,path)
    if idx in CHECKED:
        # A DAG node may be reached through different but equivalent equation bases.
        old=CHECKED[idx]
        assert old[0]==es and old[2:]==(r,path)
        olddesc=system(old[1])
        assert all(not any(reduce_expression(e,olddesc)) for e in equations)
        assert all(not any(reduce_expression(e,description)) for e in old[1])
        return
    CHECKED[idx]=signature
    node=nodes[idx];kind=node['kind'];COUNTS[kind]+=1
    if kind=='infeasible':assert not integer_feasible(equations);return
    assert integer_feasible(equations)
    if kind=='allowed':check_allowed(node['label'],r,path,description);return
    witness=tuple(node['witness']);assert witness in es
    children={} if kind=='unique' else {tuple(c['partner']):c['node'] for c in node['children']}
    assert kind in ('unique','collision')
    if kind=='collision':assert len(children)==len(node['children']) and children
    for partner in es:
        if partner==witness:continue
        new=equations+(minus(witness,partner),)
        exists=integer_feasible(new)
        COUNTS['partner_checks']+=1
        assert exists==(partner in children)
        if exists:
            assert system(new)[0]>description[0]
            visit(children[partner],es,new,r,path,nodes)

def check_partition(paths,used=frozenset()):
    if any(not p for p in paths):assert len(paths)==1;return
    t=paths[0][0][0];assert t in range(3) and t not in used
    assert all(p[0][0]==t and p[0][1] in ('0','+') for p in paths)
    for choice in ('0','+'):
        child=[p[1:] for p in paths if p[0][1]==choice];assert child
        check_partition(child,used|{t})

def main():
    obj=json.loads((BASE/'quintic_classification_certificate.json').read_text(encoding='utf-8'))
    roots=obj['roots'];nodes=obj['nodes']
    assert [tuple(r['residue']) for r in roots]==list(product(range(5),repeat=3))
    assert len(fifth_form())==26
    for root in roots:
        r=tuple(root['residue']);paths=[tuple((t,c) for t,c in leaf['path']) for leaf in root['leaves']]
        check_partition(paths)
        for leaf,path in zip(root['leaves'],paths):
            es=tuple(sorted(to_gaps(e,r) for e in raw_defect(r)));eqs=[]
            for t,choice in path:
                terms=[]
                for e in es:
                    v=list(e)
                    if choice=='0':v[t]=0
                    else:v[3]+=v[t]
                    terms.append(tuple(v))
                es=tuple(sorted(parity(terms)))
                if choice=='0':eqs.append(tuple(1 if j==t else 0 for j in range(4)))
            visit(leaf['node'],es,tuple(eqs),r,path,nodes)
    assert len(CHECKED)==len(nodes)==672
    for kind,number in obj['summary'].items():assert COUNTS[kind]==number
    receipt=dict(status='PASS',method='F2 circulant determinant and exact Cramer solution parametrization',
                 all_125_residue_classes=True,SMT_used=False,generator_code_imported=False,
                 counts=dict(COUNTS),all_nodes_checked=len(CHECKED),
                 conclusion='Every fifth-norm tail-palindromic input is the stated progression or degree-10 exception; sufficiency checked separately')
    (BASE/'quintic_classification_check_receipt.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
    print('PASS: all 125 residue classes, orthant partitions and 672 collision-certificate nodes')
    print('PASS: necessary classification into the arithmetic progression and degree-10 exception')
    print('PASS: independent F2 determinant + Cramer arithmetic, no generator imports or SMT')
    print(dict(COUNTS))

if __name__=='__main__':main()
