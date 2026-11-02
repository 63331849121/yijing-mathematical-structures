"""Verify sufficiency, exact zero counts, factor identities, and numerical controls."""
if not __debug__:
    raise RuntimeError('Run without -O: this proof checker requires Python assertions.')

from pathlib import Path
from collections import defaultdict
from itertools import product
import json
import check_quintic_classification as independent

BASE=Path(__file__).resolve().parent

def gf_mul(a,b):
    result=0
    for _ in range(4):
        if b&1:result^=a
        b>>=1;a<<=1
        if a&16:a^=0x13
    return result
Z=[1]
for _ in range(4):Z.append(gf_mul(Z[-1],8))

def pmul(a,b):
    z=0
    while b:
        if b&1:z^=a
        b>>=1;a<<=1
    return z
def remainder(a,p):
    while a.bit_length()>=p.bit_length():a^=p<<(a.bit_length()-p.bit_length())
    return a
def power(a,m,p):
    z=1
    while m:
        if m&1:z=remainder(pmul(z,a),p)
        a=remainder(pmul(a,a),p);m>>=1
    return z
def pgcd(a,b):
    while b:a,b=b,remainder(a,b)
    return a
def primes(n):
    ans=[];t=2
    while t*t<=n:
        if n%t==0:
            ans.append(t)
            while n%t==0:n//=t
        t+=1
    if n>1:ans.append(n)
    return ans
def irreducible(p):
    n=p.bit_length()-1;z=2;tests={n//q for q in primes(n)}
    for j in range(1,n+1):
        z=remainder(pmul(z,z),p)
        if j in tests and pgcd(p,z^2)!=1:return False
    return z==2
def exact_order(p):
    assert irreducible(p);m=(1<<(p.bit_length()-1))-1
    for q in primes(m):
        while m%q==0 and power(2,m//q,p)==1:m//=q
    assert power(2,m,p)==1 and all(power(2,m//q,p)!=1 for q in primes(m))
    return m
def exact_divide(a,b):
    q=0
    while a.bit_length()>=b.bit_length():
        s=a.bit_length()-b.bit_length();q^=1<<s;a^=b<<s
    assert a==0
    return q
def candidate(n,i,j):return ((1<<(n+1))-1)^(1<<i)^(1<<j)^(1<<(n-1-i))^(1<<(n-1-j))
def reciprocal(p,n):return sum(((p>>j)&1)<<(n-j) for j in range(n+1))
def tail_palindromic(p):
    n=p.bit_length()-1;tail=p^(1<<n)
    return tail==reciprocal(tail,n-1)

def actual_norm5(p):
    """Five factors over F16, with actual integer X-exponents."""
    terms=[j for j in range(p.bit_length()) if p>>j&1]
    out={0:1}
    for s in range(5):
        new=defaultdict(int)
        for a,c in out.items():
            for b in terms:new[a+b]^=gf_mul(c,Z[(s*b)%5])
        out={e:c for e,c in new.items() if c}
    assert all(c==1 and e%5==0 for e,c in out.items())
    return sum(1<<(e//5) for e in out)

def symbolic_family_norm(residue):
    # d=10t+residue; n=7d-1, i=2d-1, j=3d-1.
    forms=[(0,0),(70,7*residue)]
    n=(70,7*residue-1);i=(20,2*residue-1);j=(30,3*residue-1)
    forms += [i,(i[0],i[1]+1),j,(j[0],j[1]+1),
              (n[0]-i[0],n[1]-i[1]-1),(n[0]-i[0],n[1]-i[1]),
              (n[0]-j[0],n[1]-j[1]-1),(n[0]-j[0],n[1]-j[1])]
    out={(0,0):1}
    for s in range(5):
        new=defaultdict(int)
        for a,c in out.items():
            for b in forms:
                assert b[0]%5==0
                new[(a[0]+b[0],a[1]+b[1])]^=gf_mul(c,Z[(s*b[1])%5])
        out={e:c for e,c in new.items() if c}
    assert all(c==1 and e[0]%5==e[1]%5==0 for e,c in out.items())
    return sorted((a//5,b//5) for a,b in out)

def parity_terms(ts):return independent.parity(ts)

def symbolic_factor_identity():
    # Laurent monomials (a,b) encode x^(a*d+b), with d a free positive integer.
    # Clear the sole geometric-sum denominator by multiplying by 1+x.
    deleted=[(a,-1) for a in (2,3,4,5)]
    left=parity_terms([(0,0),(7,0)]+[e for a,b in deleted for e in ((a,b),(a,b+1))])
    H=parity_terms([(a,0) for a in range(7)]+[(2,-1),(2,0),(4,-1),(4,0)])
    right=parity_terms((a+c,b+e) for a,b in ((0,0),(1,0)) for c,e in H)
    assert left==right
    return True

def check_family(residue):
    Q=symbolic_family_norm(residue)
    # Compact manuscript formula, with d=10t+residue.
    aset=(7,8,9,12,13,14,21,22,23,26,27,28)
    compact={(0,0),(70,7*residue)}
    for a in aset:compact.symmetric_difference_update({(2*a,(a*residue)//5)})
    for b in range(2,6):
        compact.symmetric_difference_update({(10*b,b*residue-1),(10*b,b*residue)})
    assert compact==set(Q)
    N=(70,7*residue)
    defect=parity_terms([(N[0]-a,N[1]-b) for a,b in Q]+[(a,b+1) for a,b in Q]+
                        [(0,0),(0,1),N,(N[0],N[1]+1)])
    assert not defect
    lower=1 if residue==1 else 0
    ordered=sorted(Q,key=lambda e:e[0]*lower+e[1])
    assert len(ordered)==22 and ordered[0]==(0,0) and ordered[-1]==N
    for a,b in zip(ordered,ordered[1:]):
        slope=b[0]-a[0];constant=b[1]-a[1]
        assert slope>=0 and slope*lower+constant>0
    # Coefficients of Q/(1+Y) are prefix parity of the ordered Q exponents.
    zero_count=[0,0]
    for t in range(1,len(ordered)-1,2):
        zero_count[0]+=ordered[t+1][0]-ordered[t][0]
        zero_count[1]+=ordered[t+1][1]-ordered[t][1]
    assert zero_count==[20,2*residue]
    if residue==1:
        f=candidate(6,1,2);g=actual_norm5(f)
        assert g==0x73 and tail_palindromic(g) and 6-(g^(1<<6)).bit_count()==2
    return dict(d_residue_mod10=residue,Q_support=ordered,distinct_support_for_t_at_least=lower,
                zero_count_coefficients=zero_count,reflection_defect_identically_zero=True,
                manuscript_floor_support_formula_verified=True)

def controls():
    count=0
    for r in product(range(5),repeat=3):
        starts=independent.bases(r)
        for offsets in ((0,0,0),(1,2,3)):
            a,b,c=[starts[t]+5*offsets[t] for t in range(3)]
            k=a+b+c;i=a;j=a+b;n=2*k;N=n+1
            f=candidate(n,i,j);g=actual_norm5(f);P=pmul(3,f);Q=actual_norm5(P)
            assert Q==pmul(3,g)
            actual=reciprocal(Q,N)^(Q<<1)^pmul(3,(1|(1<<N)))
            symbolic=0
            for e in independent.raw_defect(r):
                val=sum(e[t]*(k,i,j)[t] for t in range(3))+e[3]
                assert val%5==0
                symbolic^=1<<(val//5)
            assert actual==symbolic
            expected=(n==10 and i==3 and j==4) or (a==2*b-1 and b==2*c-1 and b%10 in (1,9))
            assert tail_palindromic(g)==expected
            count+=1
    points=[]
    for d in (1,9,11,19,21):
        n=7*d-1;f=candidate(n,2*d-1,3*d-1);g=actual_norm5(f)
        assert tail_palindromic(g) and n-(g^(1<<n)).bit_count()==2*d
        S=(1<<d)-1
        zS=sum(1<<(d*t) for t in range(7))
        H=zS^pmul(3,(1<<(2*d-1))^(1<<(4*d-1)))
        assert pmul(S,H)==f
        if d>1:assert remainder(f,S)==0 and remainder(g,S)==0 and not irreducible(f)
        points.append(dict(d=d,n=n,image_zero_count=2*d,proper_S_factor=(d>1)))
    small=[]
    for n,i,j,expected_g,expected_order in ((6,1,2,0x73,63),(10,3,4,0x77b,341)):
        f=candidate(n,i,j);g=actual_norm5(f)
        assert g==expected_g and irreducible(f) and irreducible(g)
        assert exact_order(f)==exact_order(g)==expected_order
        small.append(dict(n=n,input=hex(f),image=hex(g),root_order=expected_order,image_zero_count=2))
    return dict(numerical_identity_controls=count,progression_controls=points,small_irreducible_cases=small)

def main():
    assert irreducible(0x13) and len(set(Z))==5 and gf_mul(Z[-1],8)==1
    compact=[]
    for i in range(5):
        for terms in (((i,5),),((i,3),((i+1)%5,1),((i-1)%5,1)),
                      ((i,3),((i+2)%5,1),((i-2)%5,1)),
                      ((i,2),((i+1)%5,2),((i+3)%5,1)),
                      ((i,2),((i+2)%5,2),((i+1)%5,1))):
            e=[0]*5
            for j,v in terms:e[j]+=v
            compact.append(tuple(e))
    compact.append((1,1,1,1,1))
    assert parity_terms(compact)==set(independent.fifth_form())
    out=dict(status='PASS',sufficient_families=[check_family(1),check_family(9)],controls=controls(),
             general_factor_identity_symbolically_verified=symbolic_factor_identity(),
             extension_field_and_root_verified=True,
             compact_cyclic_norm_formula_verified=True,
             conclusion='All listed branches are tail-palindromic; their missing-tail counts are 2d or 2, never 4')
    (BASE/'quintic_branch_check_receipt.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
    print('PASS: both unbounded progression branches have identically zero reflection defect')
    print('PASS: exact zero counts 2d for d=1,9 mod10, and 2 for the degree-10 exception')
    print('PASS: d>1 input/output proper S-factor and complete small irreducible cases')
    print('PASS: 250 independent numerical norm/reflection controls in all residue classes')

if __name__=='__main__':main()
