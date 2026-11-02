"""Exact fixed-support fifth norm and reflection defect, all integer parameters."""
from itertools import product,permutations
from collections import Counter,defaultdict
from pathlib import Path
from math import gcd
from functools import reduce,lru_cache
import json

BASE=Path(__file__).resolve().parent

def gf16(a,b):
    r=0
    while b:
        if b&1:r^=a
        b>>=1;a<<=1
        if a&16:a^=0x13
    return r
MUL=tuple(tuple(gf16(a,b) for b in range(16)) for a in range(16))
Z=[1]
for _ in range(4):Z.append(gf16(Z[-1],8))
assert gf16(Z[-1],8)==1 and len(set(Z))==5

def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def parity(ts):
    r=set()
    for e in ts:
        if e in r:r.remove(e)
        else:r.add(e)
    return r
def pmul(a,b):return parity(add(e,f) for e in a for f in b)

@lru_cache(None)
def norm_form():
    p={(0,0,0,0,0):1}
    for s in range(5):
        r=defaultdict(int)
        for e,c in p.items():
            for t in range(5):
                v=list(e);v[t]+=1
                r[tuple(v)]^=MUL[c][Z[(s*t)%5]]
        p={e:c for e,c in r.items() if c}
    assert all(c==1 for c in p.values())
    # Independent determinant expansion of the circulant multiplication matrix.
    terms=[]
    for perm in permutations(range(5)):
        powers=[0]*5
        for row,col in enumerate(perm):powers[(col-row)%5]+=1
        terms.append(tuple(powers))
    assert set(p)==parity(terms)
    return tuple(sorted(p))

P={(0,0,0,0),(2,0,0,1),
   (0,1,0,0),(0,1,0,1),(0,0,1,0),(0,0,1,1),
   (2,-1,0,-1),(2,-1,0,0),(2,0,-1,-1),(2,0,-1,0)}

@lru_cache(None)
def defect(r):
    cs=[set() for _ in range(5)]
    for e in P:cs[(sum(e[t]*r[t] for t in range(3))+e[3])%5].add(e)
    powers=[]
    for s in cs:
        vals=[{(0,0,0,0)}]
        for _ in range(5):vals.append(pmul(vals[-1],s))
        powers.append(vals)
    norm=set()
    for e in norm_form():
        term={(0,0,0,0)}
        for t,a in enumerate(e):term=pmul(term,powers[t][a])
        norm ^= term
    top=(10,0,0,5)
    out=parity([sub(top,e) for e in norm]+[add(e,(0,0,0,5)) for e in norm]+
               [(0,0,0,0),(0,0,0,5),(10,0,0,5),(10,0,0,10)])
    return tuple(sorted(out))

def gap_bases(r):return [r[1] or 5,(r[2]-r[1])%5 or 5,(r[0]-r[2])%5 or 5]
def gap_exponent(e,r):
    a,b,c=gap_bases(r)
    return (5*(e[0]+e[1]+e[2]),5*(e[0]+e[2]),5*e[0],
            e[0]*(a+b+c)+e[1]*a+e[2]*(a+b)+e[3])

def no_collision(d):
    co=d[:3];target=-d[3];g=reduce(gcd,map(abs,co),0)
    if not g:return 'constant' if target else None
    if target%g:return 'gcd'
    if any(x>0 for x in co) and any(x<0 for x in co):return None
    if any(x<0 for x in co):co=tuple(-x for x in co);target=-target
    if target<0:return 'sign'
    reachable=[True]+[False]*target
    for t in range(1,target+1):reachable[t]=any(x and t>=x and reachable[t-x] for x in co)
    return 'coin' if not reachable[target] else None

def branch(es,t,positive):
    ts=[]
    for e in es:
        v=list(e)
        if positive:v[3]+=v[t]
        else:v[t]=0
        ts.append(tuple(v))
    return tuple(sorted(parity(ts)))

def diagnose(es,remaining=(1,2,0),path=()):
    if not es:return [dict(kind='zero',path=path,support=0)]
    for e in es:
        if all(no_collision(sub(e,f)) for f in es if e!=f):
            return [dict(kind='nonzero',path=path,support=len(es),witness=e)]
    if not remaining:return [dict(kind='unresolved',path=path,support=len(es),exponents=es)]
    t=remaining[0]
    return (diagnose(branch(es,t,False),remaining[1:],path+((t,'0'),))+
            diagnose(branch(es,t,True),remaining[1:],path+((t,'+'),)))

def main():
    print('norm form monomials',len(norm_form()),norm_form(),flush=True)
    rows=[];stats=Counter()
    for r in product(range(5),repeat=3):
        es=tuple(sorted(gap_exponent(e,r) for e in defect(r)))
        leaves=diagnose(es)
        stats.update(row['kind'] for row in leaves)
        rows.append(dict(residue=r,bases=gap_bases(r),root_terms=len(es),leaves=leaves))
        if any(v['kind']!='nonzero' for v in leaves):
            print('special',r,[(v['kind'],v['path'],v['support']) for v in leaves if v['kind']!='nonzero'],flush=True)
    out=dict(norm_form=norm_form(),summary=dict(stats),rows=rows)
    (BASE/'quintic_support_diagnosis.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
    print('SUMMARY',dict(stats),flush=True)

if __name__=='__main__':main()
