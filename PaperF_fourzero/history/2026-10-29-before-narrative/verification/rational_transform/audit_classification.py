"""Exact bounded audit of a proposed all-degree shape classification.

No new primitive/existence table. Integer bits implement F_2 polynomials.
"""
from itertools import combinations
from pathlib import Path
import hashlib
import json
import sys

OUT=Path(__file__).resolve().parent
PAPER=OUT.parents[1]

def xp1pow(e):
    p=0;s=e
    while True:
        p ^= 1<<s
        if s==0:return p
        s=(s-1)&e

def S(d):return (1<<(d+1))-1
def candidate(n,i,j):return S(n)^(1<<i)^(1<<j)^(1<<(n-1-i))^(1<<(n-1-j))
def translate(p):
    result=0
    while p:
        low=p&-p; result ^= xp1pow(low.bit_length()-1);p^=low
    return result
def M(p,n):
    result=0
    while p:
        low=p&-p;j=low.bit_length()-1
        result ^= xp1pow(n-j)<<j;p^=low
    return result
def reverse(p,d):return sum(((p>>j)&1)<<(d-j) for j in range(d+1))
def derivative(p):return sum(((p>>j)&1)<<(j-1) for j in range(1,p.bit_length(),2))
def powers(limit):return [1<<a for a in range(limit.bit_length()) if (1<<a)<=limit]
def twozero_pred(d):
    out=set()
    if (d+2)&(d+1)==0:
        out.update(combinations(powers(d-1),2))
    if d>=4 and d&(d-1)==0:
        out.update(tuple(sorted((d-1,p))) for p in powers(d-1))
    if (d+2).bit_count()==2:
        bits=powers(d+2)
        bits=[p for p in bits if p&(d+2)]
        if min(bits)>=4:out.add(tuple(sorted((bits[0]-1,bits[1]-1))))
    return out

two_checks=0;two_rows=[]
for d in range(2,257,2):
    ds=translate(S(d))^S(d)
    delta=[xp1pow(a)^(1<<a) for a in range(d+1)]
    actual=set()
    for a,b in combinations(range(1,d),2):
        two_checks+=1
        if delta[a]^delta[b]==ds:actual.add((a,b))
    assert actual==twozero_pred(d),(d,actual,twozero_pred(d))
    if actual:two_rows.append(dict(d=d,pairs=sorted(actual)))

def shape_pred(n):
    out=set()
    for r in range(3,n.bit_length()):
        if n==(1<<r)+2:out.add((3,1<<(r-1)))
        for s in range(2,r):
            if n==(1<<r)+(1<<s)-2:out.add(((1<<s)-2,(1<<s)-1))
    if n==14:out.update([(2,4),(2,5),(4,5)])
    return out

shape_checks=0;direct_checks=0;bridge_checks=0;shape_rows=[]
for n in range(6,257,2):
    k=n//2
    baseline=xp1pow(n+1)^(1<<(n+1))^S(n)
    sig={i:(xp1pow(n-i)<<i)^(xp1pow(i+1)<<(n-1-i))^(1<<i)^(1<<(n-1-i)) for i in range(1,k)}
    actual=set()
    for i,j in combinations(range(1,k),2):
        shape_checks+=1
        yes=(sig[i]^sig[j]==baseline)
        if n<=64:
            f=candidate(n,i,j)
            assert yes==(M(f,n)==f)
            direct_checks+=1
            # Directly check the bridge p(x+1)=p(x) <=> M_n(f)=f.
            p=(f<<1)^(1<<(n+1))
            assert yes==(translate(p)==p)
            bridge_checks+=1
        if yes:actual.add((i,j))
    assert actual==shape_pred(n),(n,actual,shape_pred(n))
    if actual:shape_rows.append(dict(n=n,pairs=sorted(actual)))

def T(h,m):
    f=0
    for j in range(m+1):
        if (h>>j)&1:f^=xp1pow(m-j)<<(2*j)
    return f
def descend(f,n):
    m=n//2;rem=f;h=0
    for j in range(m,-1,-1):
        if (rem>>(m+j))&1:
            h^=1<<j;rem^=xp1pow(m-j)<<(2*j)
    assert rem==0 and T(h,m)==f
    return h

from flint import fmpz_mod_poly_ctx
R=fmpz_mod_poly_ctx(2)
def rp(p):return R([(p>>i)&1 for i in range(p.bit_length())])
def bits(p):return sum(int(c)<<j for j,c in enumerate(p.coeffs()))
def mul(a,b):
    c=0
    while b:
        if b&1:c^=a
        a<<=1;b>>=1
    return c

remaining=[];familyA=[]
for row in shape_rows:
    n=row['n']
    for i,j in row['pairs']:
        f=candidate(n,i,j);h=descend(f,n)
        lower=i+2;upper=n+2-lower
        if j==i+1 and lower>=4 and lower&(lower-1)==0 and upper>lower and upper&(upper-1)==0:
            assert (h>>1)&1==0
            familyA.append(dict(n=n,i=i,j=j,h1=0))
for r in range(3,11):
    n=(1<<r)+2;i=3;j=1<<(r-1)
    f=candidate(n,i,j);h=descend(f,n)
    assert (h>>1)&1
    unit,fac=rp(h).factor()
    product=int(unit)
    for q,e in fac:
        assert q.is_irreducible()
        for _ in range(int(e)):product=mul(product,bits(q))
    assert product==h
    factor_list=[dict(degree=int(q.degree()),hex=hex(bits(q)),multiplicity=int(e)) for q,e in fac]
    hi=bool(rp(h).is_irreducible())
    assert hi==bool(rp(f).is_irreducible())
    remaining.append(dict(r=r,n=n,pair=[i,j],h_degree=n//2,h=hex(h),h_irreducible=hi,h_factors=factor_list))

hashes={}
for root in [PAPER]:
    for name in ['PaperF_fourzero.tex','PaperF_fourzero.pdf']:
        p=root/name;hashes[str(p)]=hashlib.sha256(p.read_bytes()).hexdigest()
result=dict(scope='finite diagnostic supporting a separate paper proof, not a general existence proof',twozero_checks=two_checks,twozero_degrees=[2,256],twozero_rows=two_rows,shape_checks=shape_checks,shape_degrees=[6,256],direct_M_checks=direct_checks,translation_bridge_checks=bridge_checks,shape_rows=shape_rows,familyA_h1_checks=familyA,remaining_family_diagnostic=remaining,paper_hashes=hashes)
general_checks=0
for k in range(1,11):
    n=2*k;d=k-1
    for interior in range(1<<(k-1)):
        half=(interior<<1)|1
        tail=half|(reverse(half,k-1)<<k)
        f=(1<<n)|tail
        e=sum(((f>>(2*j))&1)<<j for j in range(k))
        o=reverse(e,d)
        assert f==((1<<n)^sum(((e>>j)&1)<<(2*j) for j in range(k))^sum(((o>>j)&1)<<(2*j+1) for j in range(k)))
        criterion=(translate(e)==e and e==(translate(o<<1)^(o<<1)))
        assert criterion==(M(f,n)==f)
        general_checks+=1
result['general_descent_checks']=general_checks
(OUT/'classification_audit.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k not in ['twozero_rows','shape_rows','familyA_h1_checks','paper_hashes']},indent=2))
