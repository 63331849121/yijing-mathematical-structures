"""Independent standard-library audit: Horner substitution, no Lucas code.

This validates the new classification and exceptional certificates only;
it does not rerun or extend the existing primitive-polynomial tables.
"""
from itertools import combinations
from pathlib import Path
import json

OUT=Path(__file__).resolve().parent

def translate(f):
    a=0
    for j in range(f.bit_length()-1,-1,-1):
        a^=a<<1
        a^=(f>>j)&1
    return a

def mobius(f,n):
    xp=[1]
    for _ in range(n):xp.append(xp[-1]^(xp[-1]<<1))
    a=(f>>n)&1
    for j in range(n-1,-1,-1):
        a<<=1
        if (f>>j)&1:a^=xp[n-j]
    return a

def S(n):return (1<<(n+1))-1
def fzero(n,i,j):return S(n)^(1<<i)^(1<<j)^(1<<(n-1-i))^(1<<(n-1-j))
def pow2(v):return v>0 and v&(v-1)==0
def shape_pred(n,i,j):
    if n==14 and (i,j) in [(2,4),(2,5),(4,5)]:return True
    if i==3 and pow2(n-2) and n>=10 and j==(n-2)//2:return True
    if j==i+1 and pow2(i+2) and i+2>=4 and pow2(n-i) and n-i>i+2:return True
    return False

shapes=0
for n in range(6,65,2):
    for i,j in combinations(range(1,n//2),2):
        f=fzero(n,i,j)
        assert (mobius(f,n)==f)==shape_pred(n,i,j),(n,i,j)
        shapes+=1

def two_pred(d,a,b):
    if pow2(d+2) and pow2(a) and pow2(b):return True
    if pow2(d) and b==d-1 and pow2(a):return True
    return pow2(a+1) and pow2(b+1) and a+1>=4 and b+1>a+1 and d==a+b

twos=0
for d in range(2,97,2):
    for a,b in combinations(range(1,d),2):
        e=S(d)^(1<<a)^(1<<b)
        assert (translate(e)==e)==two_pred(d,a,b),(d,a,b)
        twos+=1

def mod(a,f):
    while a.bit_length()>=f.bit_length():a^=f<<(a.bit_length()-f.bit_length())
    return a
def gcd(a,b):
    while b:a,b=b,mod(a,b)
    return a
def square(a):return sum(((a>>j)&1)<<(2*j) for j in range(a.bit_length()))
def frob(f,n):
    a=2
    for _ in range(n):a=mod(square(a),f)
    return a

cert=[]
for degree,h in [(5,0x37),(7,0xcb)]:
    final=frob(h,degree)
    small=gcd(h,0b110)
    assert final==2 and small==1
    cert.append(dict(degree=degree,h=hex(h),x_2power_degree_mod_h=hex(final),gcd_x2_plus_x=hex(small)))

result=dict(status='PASS',method='Horner/Pascal substitutions independent of prior Lucas/submask implementation',fourzero_degrees=[6,64],fourzero_candidates=shapes,twozero_degrees=[2,96],twozero_candidates=twos,prime_degree_Rabin_certificates=cert,proof_review='All-degree proof reviewed separately; finite checks are not its completeness justification')
(OUT/'independent_review.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result,indent=2))
