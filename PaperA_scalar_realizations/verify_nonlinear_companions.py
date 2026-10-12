"""Finite certificates for Paper A's nonlinear companion-group results.

The alternating-group equality is proved in the paper using the certified
three-cycle and anchored-cycle identities. This program does not enumerate A16.
Only Python's standard library is used; no search or random seed is needed.
"""
from collections import deque
from pathlib import Path
import json

F = (1,5,12,3,11,7,15,10,2,14,9,13,0,8,6,4)

def compose(a,b):
    return tuple(a[b[x]] for x in range(len(a)))

def inverse(a):
    if sorted(a)!=list(range(len(a))):
        raise ValueError('Expected a permutation.')
    b=[0]*len(a)
    for x,y in enumerate(a): b[y]=x
    return tuple(b)

def rotate(f):
    return inverse(tuple(x^f[x] for x in range(len(f))))

def cycles(f):
    seen=set();result=[]
    for x in range(len(f)):
        if x in seen:continue
        cycle=[];y=x
        while y not in seen:
            seen.add(y);cycle.append(y);y=f[y]
        result.append(cycle)
    return sorted(result,key=lambda c:(len(c),c))

def power(f,k):
    result=tuple(range(len(f)))
    while k:
        if k&1:result=compose(result,f)
        f=compose(f,f);k>>=1
    return result

def orbit(generators,seed,action):
    seen={seed};pending=deque([seed])
    while pending:
        current=pending.popleft()
        for g in generators:
            image=action(g,current)
            if image not in seen:
                seen.add(image);pending.append(image)
    return seen

def example():
    g=rotate(F);k=rotate(g)
    expected_g=(3,0,5,10,1,13,11,9,14,6,8,15,12,7,2,4)
    assert g==expected_g and rotate(k)==F
    assert all(sorted(map(len,cycles(h)))==[1,15] for h in (F,g,k))
    assert F[1^2] != (F[1]^F[2]^F[0])
    w=compose(compose(F,F),g);s=power(w,35)
    assert cycles(s)==[[1],[2],[4],[5],[6],[7],[8],[9],[10],[11],[12],[13],[15],[0,14,3]]
    assert len(orbit((F,g),0,lambda h,x:h[x]))==16
    assert len(orbit((F,g),(0,1),lambda h,p:(h[p[0]],h[p[1]])))==16*15
    anchored=[]
    supports={3}
    for j in range(15):
        conjugate=compose(compose(power(F,j),s),inverse(power(F,j)))
        nontrivial=[c for c in cycles(conjugate) if len(c)>1]
        assert len(nontrivial)==1 and len(nontrivial[0])==3 and 3 in nontrivial[0]
        supports.update(nontrivial[0]);anchored.append(nontrivial[0])
    assert supports==set(range(16))
    # Directly check the two elementary identities used by the graph proof.
    def three(p,a,b):
        result=list(range(16))
        result[p],result[a],result[b]=a,b,p
        return tuple(result)
    u,v=three(3,0,1),three(3,2,4)
    comm=compose(compose(compose(u,v),inverse(u)),inverse(v))
    assert comm==three(3,0,2)
    u,v=three(3,0,1),three(3,1,2)
    assert compose(compose(u,v),inverse(u))==three(0,3,2)
    assert compose(u,v)==three(0,1,2)
    return dict(f=list(F),F_f=list(g),F2_f=list(k),
        f_cycles=cycles(F),F_f_cycles=cycles(g),F2_f_cycles=cycles(k),
        word='f^2 o F(f), right-to-left composition',word_cycles=cycles(w),
        word_exponent=35,three_cycle=cycles(s),anchored_conjugates=anchored,
        point_orbit_size=16,ordered_distinct_pair_orbit_size=240,
        nonlinear_witness=dict(x=1,y=2,lhs=F[3],rhs=F[1]^F[2]^F[0]),
        group_proof='Elementary anchored-three-cycle graph argument in the manuscript; no A16 enumeration.')

def translated_fixed_checks():
    # This finite support includes all standard four-dimensional orientations
    # and every supplied six-dimensional standard-spread representative.
    import verify_standard_spread_orbits as standard
    data=json.loads((Path(__file__).resolve().parent/'standard_spread_results.json').read_text())
    summaries=[]
    for block in data['results']:
        m=block['m'];q=4**m
        scales,points,index=standard.setup(m)
        if m==2:
            maps=[standard.orient_map(mask,m,scales,index) for mask in range(2**len(points))]
        else:
            maps=[r['mapping'] for r in block['orbits']]
        cases=0
        for mapping in maps:
            f0=tuple(mapping)
            assert rotate(f0)==f0
            for b in range(1,q):
                tau=tuple(x^b for x in range(q))
                f=compose(tau,f0);g=rotate(f);k=rotate(g)
                assert g==compose(f0,tau)
                assert k==compose(compose(tau,f0),tau)
                assert compose(g,f)==compose(f0,f0)
                line={0,b,f0[b],f0[f0[b]]}
                assert len(line)==4
                assert orbit((f,g),0,lambda h,x:h[x])==line
                assert all((x^y) in line for x in line for y in line)
                cases+=1
        summaries.append(dict(n=2*m,fixed_maps_examined=len(maps),nonzero_translation_cases=cases,
                              scope='all standard orientations' if m==2 else 'all 80 standard-spread representatives'))
    return summaries

def main():
    if not __debug__:
        raise RuntimeError('Run ordinary Python without -O.')
    result=dict(example=example(),translated_fixed_support=translated_fixed_checks())
    path=Path(__file__).resolve().parent/'nonlinear_companion_results.json'
    path.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print('Certified the nonlinear 1+15 triple and its anchored three-cycle.')
    print('Translated-fixed support:',result['translated_fixed_support'])
    print('All nonlinear-companion certificates passed.')

if __name__=='__main__':
    main()
