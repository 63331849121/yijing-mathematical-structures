"""Independent checks for Paper A (Python 3, standard library only).

Run: python verify_paperA_structure.py
The checks cover the displayed coordinate bases, exact group orders,
characteristic polynomials, 720 basis orderings, tau-collapse data,
the scalar-affine F-orbits over F64, nonzero-translation conjugacy,
and the CRT indexing convention.
They do not establish the infinite PTE theorem or recheck Lean proofs.
"""

from itertools import permutations
from collections import Counter, deque
import json


def coord_table(basis):
    n = len(basis)
    out = [None] * (1 << n)
    for c in range(1 << n):
        x = 0
        for i, g in enumerate(basis):
            if c & (1 << (n-1-i)):
                x ^= g
        if out[x] is not None:
            raise ValueError('Dependent basis')
        out[x] = c
    return out

def inverse(p):
    if len(set(p)) != len(p):
        return None
    out = [0] * len(p)
    for i,x in enumerate(p):
        out[x] = i
    return out

def triple(basis):
    c = coord_table(basis)
    mask = len(c)-1
    t = [mask ^ x for x in c]
    d = inverse([i ^ x for i,x in enumerate(t)])
    k = inverse([i ^ x for i,x in enumerate(d)]) if d else None
    return t,d,k

def cycles(p):
    done = set()
    lengths = []
    for i in range(len(p)):
        if i in done:
            continue
        j = i
        size = 0
        while j not in done:
            done.add(j)
            j = p[j]
            size += 1
        lengths.append(size)
    return sorted(lengths)

def mul_poly(a,b):
    r = 0
    while b:
        if b & 1: r ^= a
        a <<= 1
        b >>= 1
    return r

def charpoly(p):
    n = (len(p)-1).bit_length()
    cols = [p[1 << (n-1-i)] ^ p[0] for i in range(n)]
    entries = [[((cols[j] >> (n-1-i)) & 1) ^ (2 if i==j else 0)
                for j in range(n)] for i in range(n)]
    result = 0
    for perm in permutations(range(n)):
        term = 1
        for i,j in enumerate(perm):
            if entries[i][j] == 0:
                term = 0
                break
            term = mul_poly(term, entries[i][j])
        result ^= term
    return hex(result)

def group_order(t,d):
    n = (len(t)-1).bit_length()
    identity = tuple(1 << (n-1-i) for i in range(n)) + (0,)
    seen = {identity}
    q = deque([identity])
    generators = [(p,[x ^ p[0] for x in p]) for p in (t,d)]
    while q:
        state = q.popleft()
        for full,linear in generators:
            new = tuple(linear[x] for x in state[:-1]) + (full[state[-1]],)
            if new not in seen:
                seen.add(new)
                q.append(new)
    return len(seen)

def poly_rem(a,m):
    while a.bit_length() >= m.bit_length():
        a ^= m << (a.bit_length()-m.bit_length())
    return a

def gf_mul(a,b,m):
    return poly_rem(mul_poly(a,b),m)

def gf_pow(a,e,m):
    r = 1
    while e:
        if e & 1: r = gf_mul(r,a,m)
        a = gf_mul(a,a,m)
        e >>= 1
    return r

def order(a,m):
    r = 1
    for e in range(1,(1 << (m.bit_length()-1))):
        r = gf_mul(r,a,m)
        if r == 1: return e
    return None

def Fpair(a,c,m):
    inv = gf_pow(a^1,(1 << (m.bit_length()-1))-2,m)
    return inv, gf_mul(inv,c,m)

result = {}
bases = [(1,3),(1,2,5,13),(63,33,18,49,1,21),(134,136,241,71,34,65,3,143)]
for k,b in enumerate(bases,1):
    t,d,K = triple(b)
    result[f'basis_k{k}'] = {
        'cycle_types':[cycles(p) for p in (t,d,K)],
        'fixed_points':[[i for i,x in enumerate(p) if i==x] for p in (t,d,K)],
        'offsets':[p[0] for p in (t,d,K)],
        'group_order':group_order(t,d),
        'charpolys':[charpoly(p) for p in (t,d,K)],
        'F3':inverse([i ^ x for i,x in enumerate(K)])==t,
    }

counts = Counter()
for b in permutations(bases[2]):
    t,d,K = triple(b)
    if d is None:
        counts['D_undefined'] += 1
        continue
    counts['D_defined'] += 1
    if cycles(t)==[1,63]:
        counts['T_Singer_and_D_defined'] += 1
    if K and cycles(t)==[1,63] and cycles(d)==[1,63] and cycles(K)==[1]+[9]*7:
        counts['exact_triple'] += 1
result['720_basis_counts'] = dict(counts)
b = list(bases[2])
b[3],b[5] = b[5],b[3]
t,d,K = triple(b)
result['swapped_4_6'] = {'fixed_T':[i for i,x in enumerate(t) if i==x], 'cycles':[cycles(p) for p in (t,d,K)]}

data = [(0x7,0x2,0x1,0x2),(0x13,0x8,0x7,0x2),(0x43,0x6,0x19,0x2c),(0x11d,0xf,0x99,0x5d)]
for k,(m,g,tau,alpha) in enumerate(data,1):
    invg = gf_pow(g,(1 << (2*k))-2,m)
    computed_tau = g ^ invg
    computed_alpha = gf_pow(g^1,(1 << (2*k))-2,m)
    result[f'tau_table_k{k}'] = {
        'data_agrees':(computed_tau,computed_alpha)==(tau,alpha),
        'orders':[order(g,m),order(tau,m),order(alpha,m),order(alpha^1,m)],
        'gamma_in_subfield':gf_pow(g,1 << k,m)==g,
    }

m = 0x43
allpairs = {(a,c) for a in range(2,64) for c in range(64)}
fixed = []
F3_ok = True
for a,c in allpairs:
    pair = a,c
    new = Fpair(a,c,m)
    if new == pair: fixed.append(pair)
    for _ in range(3): pair=Fpair(*pair,m)
    F3_ok &= pair==(a,c)
result['F_scalar_affine_F64']={'count':len(allpairs),'fixed':fixed,'three_cycles':(len(allpairs)-len(fixed))//3,'F3':F3_ok}

tau=0x29
invtau=gf_pow(tau,62,m)
trace=0
r=invtau
for _ in range(6):
    trace ^= r
    r=gf_mul(r,r,m)
# Quadratic extension by z^2+tau*z+1; pair denotes u+v*z.
def exmul(x,y):
    u,v=x; U,V=y
    vv=gf_mul(v,V,m)
    return gf_mul(u,U,m)^vv, gf_mul(u,V,m)^gf_mul(v,U,m)^gf_mul(tau,vv,m)
r=(1,0)
root_order=None
for e in range(1,66):
    r=exmul(r,(0,1))
    if r==(1,0):
        root_order=e
        break
result['k6_counterexample']={'tau_order':order(tau,m),'trace_inverse':trace,'root_order':root_order}

t,d,K=triple(bases[2])
result['numeric_CRT']={'T_63':t[63],'T_0':t[0],'orbit_has_0_and_63':cycles(t)==[1,63] and t[0]==63,'same_residue':0%63==63%63}

# Polynomial irreducibility and order certificate used in Proposition 3.3.
def poly_gcd(a,b):
    while b:
        a,b=b,poly_rem(a,b)
    return a

p=0x6d
assert gf_pow(2,64,p)==2
assert p & 1 == 1 and p.bit_count() % 2 == 1  # p(0)=p(1)=1
assert poly_gcd(p, 0b110)==1  # t^2+t
assert poly_gcd(p,gf_pow(2,8,p)^2)==1
assert poly_gcd(p,gf_pow(2,4,p)^2)==1
assert [gf_pow(2,n,p) for n in (63,21,9)]==[1,0x17,0x6]

expected_groups=(12,240,4032,65280)
expected_polys=(['0x7','0x7','0x7'],['0x13','0x19','0x1f'],
                ['0x6d','0x5b','0x49'],['0x169','0x12d','0x139'])
expected_fixed=([[1],[2],[3]],[[3],[11],[15]],
                [[38],[41],[63]],[[16],[87],[255]])
for k in range(1,5):
    row=result[f'basis_k{k}']
    assert row['group_order']==expected_groups[k-1]
    assert row['fixed_points']==expected_fixed[k-1]
    assert row['charpolys']==expected_polys[k-1]
    assert row['F3']
    assert row['cycle_types']==[[1,(1<<(2*k))-1]]*2+[[1]+[(1<<k)+1]*((1<<k)-1)]
    taurow=result[f'tau_table_k{k}']
    assert taurow['data_agrees'] and not taurow['gamma_in_subfield']
    assert taurow['orders']==[(1<<k)+1,(1<<k)-1,(1<<(2*k))-1,(1<<(2*k))-1]
assert result['720_basis_counts']==dict(D_undefined=572,D_defined=148,
    T_Singer_and_D_defined=54,exact_triple=9)
assert result['swapped_4_6']==dict(fixed_T=[11],cycles=[[1,63],[1,21,21,21],[1,63]])
assert result['F_scalar_affine_F64']==dict(count=3968,fixed=[(58,0),(59,0)],three_cycles=1322,F3=True) or (
    result['F_scalar_affine_F64']['count']==3968 and
    set(result['F_scalar_affine_F64']['fixed'])=={(58,0),(59,0)} and
    result['F_scalar_affine_F64']['three_cycles']==1322 and
    result['F_scalar_affine_F64']['F3'])
assert result['k6_counterexample']==dict(tau_order=63,trace_inverse=1,root_order=13)

t,d,K=triple(bases[2])
orbit=[]
x=63
for _ in range(63):
    orbit.append(x)
    x=t[x]
assert x==63 and len(set(orbit))==63 and 38 not in orbit
assert orbit[0]==63 and orbit[62]==0 and (62%7,62%9)==(6,8)
result['CRT_exponents']={'word_63':0,'word_0':62,'word_0_CRT':[6,8]}
# Check every nonzero b for every PTE slope over F64.
m = 0x43
pte_slopes = [a for a in range(2,64) if order(a,m)==63 and gf_pow(a,8,m)^a==1]
assert len(pte_slopes)==6
checked = 0
for a in pte_slopes:
    one_pairs = [(a,1)]
    for _ in range(2):
        one_pairs.append(Fpair(*one_pairs[-1],m))
    assert Fpair(*one_pairs[-1],m)==one_pairs[0]
    for b in range(1,64):
        pairs = [(a,b)]
        for _ in range(2):
            pairs.append(Fpair(*pairs[-1],m))
        assert Fpair(*pairs[-1],m)==pairs[0]
        expected = [gf_mul(b,gf_pow(a^1,62,m),m), gf_mul(b,gf_pow(a,62,m),m), b]
        invb = gf_pow(b,62,m)
        for i, ((s,c),(s1,c1)) in enumerate(zip(pairs,one_pairs)):
            perm = [gf_mul(s,x,m)^c for x in range(64)]
            assert [x for x in range(64) if perm[x]==x]==[expected[i]]
            assert cycles(perm)==([1,63] if i<2 else [1]+[9]*7)
            for x in range(64):
                conjugate = gf_mul(b,gf_mul(s1,gf_mul(invb,x,m),m)^c1,m)
                assert conjugate==perm[x]
        checked += 1
result['nonzero_translation_F64'] = {'PTE_slopes':len(pte_slopes),
    'nonzero_b_per_slope':63,'triples_checked':checked,
    'fixed_points_cycles_and_conjugacy':True}
assert checked==378

print(json.dumps(result,ensure_ascii=False,indent=2))
print('All structural checks passed.')
