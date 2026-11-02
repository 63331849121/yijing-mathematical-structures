"""Classify all zeros of the fifth-norm reflection defect by affine collisions.

Exact rational/integer arithmetic. SMT is not used. Every zero polynomial must
cancel a chosen term with some partner; each branch raises the equality rank.
"""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache,reduce
from math import gcd,lcm,ceil,floor
from collections import defaultdict,Counter
from itertools import product
import json
import quintic_support as q

BASE=Path(__file__).resolve().parent
STATS=Counter();NODES=[];MEMO={}

@lru_cache(None)
def canonical(equations):
    a=[list(map(F,row)) for row in equations if any(row)]
    p=0
    for col in range(3):
        pivot=next((t for t in range(p,len(a)) if a[t][col]),None)
        if pivot is None:continue
        a[p],a[pivot]=a[pivot],a[p]
        divisor=a[p][col];a[p]=[v/divisor for v in a[p]]
        for t in range(len(a)):
            if t!=p and a[t][col]:
                s=a[t][col];a[t]=[v-s*w for v,w in zip(a[t],a[p])]
        p+=1
    if any(not any(row[:3]) and row[3] for row in a):return ((F(0),F(0),F(0),F(1)),)
    return tuple(tuple(row) for row in a if any(row[:3]))

def pivot(row):return next(t for t in range(3) if row[t])
def evaluate_mod(e,basis):
    v=list(map(F,e))
    for row in basis:
        t=pivot(row);s=v[t]
        if s:v=[a-s*b for a,b in zip(v,row)]
    return tuple(v)

def integer_row(row):
    denominator=lcm(*(v.denominator for v in row))
    v=[int(x*denominator) for x in row];g=reduce(gcd,map(abs,v),0)
    return tuple(x//g for x in v)

@lru_cache(None)
def feasible(basis):
    if any(not any(row[:3]) and row[3] for row in basis):return False
    rank=len(basis)
    if rank==0:return True
    if rank==1:
        row=integer_row(basis[0]);co=row[:3];target=-row[3]
        g=reduce(gcd,map(abs,co),0)
        if target%g:return False
        if any(x>0 for x in co) and any(x<0 for x in co):return True
        if any(x<0 for x in co):co=tuple(-x for x in co);target=-target
        if target<0:return False
        reached=[True]+[False]*target
        for t in range(1,target+1):reached[t]=any(x and t>=x and reached[t-x] for x in co)
        return reached[target]
    if rank==3:
        point=[F(0)]*3
        for row in basis:point[pivot(row)]=-row[3]
        return all(x>=0 and x.denominator==1 for x in point)
    assert rank==2
    free=next(t for t in range(3) if all(pivot(row)!=t for row in basis))
    slopes=[F(0)]*3;intercepts=[F(0)]*3;slopes[free]=1
    for row in basis:
        t=pivot(row);slopes[t]=-row[free];intercepts[t]=-row[3]
    low=F(0);high=None
    for a,b in zip(slopes,intercepts):
        if not a:
            if b<0:return False
        elif a>0:low=max(low,-b/a)
        else:high=min(high,-b/a) if high is not None else -b/a
    lo=ceil(low);hi=floor(high) if high is not None else None
    if hi is not None and hi<lo:return False
    period=lcm(*(x.denominator for x in slopes+intercepts))
    for r in range(period):
        if all((a*r+b).denominator==1 for a,b in zip(slopes,intercepts)):
            first=lo+(r-lo)%period
            if hi is None or first<=hi:return True
    return False

def reduce_support(es,basis):
    groups=defaultdict(list)
    for e in es:groups[evaluate_mod(e,basis)].append(e)
    return tuple(sorted(min(vals) for vals in groups.values() if len(vals)%2))

def gap_forms(r,path):
    bases=q.gap_bases(r);choices=dict(path);out=[]
    for t in range(3):
        row=[0,0,0,bases[t]]
        if choices.get(t)!='0':row[t]=5
        if choices.get(t)=='+':row[3]+=5
        out.append(tuple(row))
    return out

def allowed(r,path,basis):
    a,b,c=gap_forms(r,path)
    def equation(x,y,m):return tuple(x[t]-m*y[t]+(1 if t==3 else 0) for t in range(4))
    if tuple(r) in ((1,2,1),(3,1,2)):
        if not any(evaluate_mod(equation(a,b,2),basis)) and not any(evaluate_mod(equation(b,c,2),basis)):
            return 'arithmetic_progression'
    eqs=[tuple(row[t]-(value if t==3 else 0) for t in range(4)) for row,value in zip((a,b,c),(3,1,1))]
    if all(not any(evaluate_mod(e,basis)) for e in eqs):return 'degree10_exception'
    return None

def record(node):
    assert len(NODES)<20000,'Finite exploration node limit reached'
    idx=len(NODES);NODES.append(node);STATS[node['kind']]+=1
    return idx

def prove(es,basis,r,path,context):
    basis=canonical(basis)
    if not feasible(basis):return record(dict(kind='infeasible'))
    es=reduce_support(es,basis)
    key=(context,basis,es)
    if key in MEMO:return MEMO[key]
    accept=allowed(r,path,basis)
    if accept:
        idx=record(dict(kind='allowed',label=accept));MEMO[key]=idx;return idx
    assert es,('Unclassified zero family',r,path,basis)
    best=None;best_partners=None
    for e in es:
        partners=[]
        for f in es:
            if f==e:continue
            new=canonical(basis+(q.sub(e,f),))
            if feasible(new):partners.append(f)
            if best_partners is not None and len(partners)>len(best_partners):break
        if best_partners is None or len(partners)<len(best_partners):
            best=e;best_partners=partners
            if not partners:break
    assert best is not None
    if not best_partners:
        idx=record(dict(kind='unique',witness=best));MEMO[key]=idx;return idx
    children=[]
    for f in best_partners:
        new=canonical(basis+(q.sub(best,f),))
        assert len(new)>len(basis)
        child=prove(es,new,r,path,context)
        children.append(dict(partner=f,node=child))
    idx=record(dict(kind='collision',witness=best,children=children));MEMO[key]=idx
    return idx

def main():
    old=json.loads((BASE/'quintic_support_diagnosis.json').read_text(encoding='utf-8'))
    roots=[];context=0
    for region in old['rows']:
        r=tuple(region['residue']);leaves=[]
        for leaf in region['leaves']:
            path=tuple((t,c) for t,c in leaf['path'])
            es=tuple(sorted(q.gap_exponent(e,r) for e in q.defect(r)))
            basis=[]
            for t,c in path:
                es=q.branch(es,t,c=='+')
                if c=='0':basis.append(tuple(1 if j==t else 0 for j in range(4)))
            node=prove(es,tuple(basis),r,path,context)
            leaves.append(dict(path=path,node=node));context+=1
        roots.append(dict(residue=r,leaves=leaves))
        print('proved',r,'nodes',len(NODES),dict(STATS),flush=True)
    out=dict(theorem='N5(f) tail-palindromic iff progression d=1 or 9 mod 10, or f_(10,3,4)',
             method='affine collision cover; exact nonnegative integer feasibility, no SMT',
             roots=roots,nodes=NODES,summary=dict(STATS),node_count=len(NODES))
    (BASE/'quintic_classification_certificate.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
    print('COMPLETE',len(NODES),dict(STATS),flush=True)

if __name__=='__main__':main()
