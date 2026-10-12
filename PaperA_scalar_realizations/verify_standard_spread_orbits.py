"""Exact finite study of orientations of the standard F4^m spread.

The program enumerates projective matrices for Burnside, and uses a
separate generator orbit traversal on all binary orientation vectors.
It writes the supplied standard_spread_results.json deterministically.
"""
from array import array
from collections import Counter
from itertools import product
from pathlib import Path
import json
import time

MUL = ((0,0,0,0), (0,1,2,3), (0,2,3,1), (0,3,1,2))

def coordinates(v, m):
    return tuple((v >> (2*i)) & 3 for i in range(m))

def scalar(a, v, m):
    return sum(MUL[a][x] << (2*i) for i,x in enumerate(coordinates(v,m)))

def setup(m):
    q = 4**m
    scales = [[scalar(a,v,m) for v in range(q)] for a in range(4)]
    points = sorted({min(scales[a][v] for a in (1,2,3)) for v in range(1,q)})
    index = [-1]*q
    for i,v in enumerate(points):
        for a in (1,2,3):
            index[scales[a][v]] = i
    # The smallest integer representative need not have leading coordinate 1.
    return scales, points, index

def matrix_permutation(cols, point_coords, index, scales):
    images=[]
    for coords in point_coords:
        w=0
        for a,c in zip(coords,cols):
            w ^= scales[a][c]
        images.append(index[w])
    return bytes(images)

def projective_matrices(m, scales, points):
    def extend(cols, span):
        if len(cols)==m:
            yield tuple(cols)
            return
        candidates=points if not cols else range(1,4**m)
        for c in candidates:
            if c not in span:
                new_span={u ^ scales[a][c] for u in span for a in range(4)}
                yield from extend(cols+[c],new_span)
    yield from extend([],{0})

def cycle_lengths(p):
    seen=0
    lengths=[]
    for i in range(len(p)):
        if (seen>>i)&1:
            continue
        j=i
        length=0
        while not ((seen>>j)&1):
            seen |= 1<<j
            length+=1
            j=p[j]
        lengths.append(length)
    return tuple(sorted(lengths))

def weight_polynomial(lengths):
    coeff=[1]+[0]*sum(lengths)
    top=0
    for length in lengths:
        for i in range(top,-1,-1):
            coeff[i+length]+=coeff[i]
        top+=length
    return coeff

def generator_actions(m, scales, points, index):
    base=[1<<(2*i) for i in range(m)]
    matrices=[]
    matrices.append(base[1:]+base[:1])
    swap=base[:]
    swap[0],swap[1]=swap[1],swap[0]
    matrices.append(swap)
    for a in (1,2):
        shear=base[:]
        shear[1] ^= scales[a][base[0]]
        matrices.append(shear)
    diagonal=base[:]
    diagonal[0]=scales[2][base[0]]
    matrices.append(diagonal)
    point_coords=[coordinates(v,m) for v in points]
    actions=[(matrix_permutation(c,point_coords,index,scales),False) for c in matrices]
    frobenius=bytes(index[sum(MUL[x][x]<<(2*i) for i,x in enumerate(coordinates(v,m)))] for v in points)
    actions.append((frobenius,True))
    return list(dict.fromkeys(actions))

def mask_tables(p):
    length=len(p)
    blocks=[]
    for start in range(0,length,8):
        values=[0]*256
        for x in range(1,256):
            bit=(x & -x).bit_length()-1
            previous=x & (x-1)
            values[x]=values[previous] ^ (1<<p[start+bit] if start+bit<length else 0)
        blocks.append(values)
    return blocks

def orient_map(mask, m, scales, index):
    return [0]+[scales[3 if (mask>>index[v])&1 else 2][v] for v in range(1,4**m)]

def orbit_traversal(m, scales, points, index, pgl_order):
    length=len(points)
    full=(1<<length)-1
    actions=generator_actions(m,scales,points,index)
    lookup=[(mask_tables(p), full if flip else 0) for p,flip in actions]
    visited=bytearray(1<<length)
    orbits=[]
    for seed in range(1<<length):
        if visited[seed]:
            continue
        queue=array('I',[seed])
        visited[seed]=1
        pos=0
        representative=seed
        min_weight=min(seed.bit_count(),length-seed.bit_count())
        while pos<len(queue):
            current=queue[pos]
            if current.bit_count()==min_weight:
                representative=min(representative,current) if representative.bit_count()==min_weight else current
            pos+=1
            for blocks,flip in lookup:
                transformed=flip
                for block_index,table in enumerate(blocks):
                    transformed ^= table[(current>>(8*block_index))&255]
                if not visited[transformed]:
                    visited[transformed]=1
                    queue.append(transformed)
        size=len(queue)
        if (2*pgl_order)%size:
            raise ArithmeticError('Orbit size does not divide the effective action order.')
        orbits.append(dict(representative_mask=representative,
            reversed_line_indices=[i for i in range(length) if (representative>>i)&1],
            min_weight=min_weight, orientation_orbit_size=size,
            projective_stabilizer_order=2*pgl_order//size,
            full_linear_stabilizer_order=6*pgl_order//size,
            mapping=orient_map(representative,m,scales,index)))
    return sorted(orbits,key=lambda x:(x['min_weight'],x['representative_mask']))

def study(m):
    started=time.monotonic()
    scales,points,index=setup(m)
    point_coords=[coordinates(v,m) for v in points]
    signatures=Counter()
    pgl_order=0
    for cols in projective_matrices(m,scales,points):
        p=matrix_permutation(cols,point_coords,index,scales)
        signatures[cycle_lengths(p)]+=1
        pgl_order+=1
    length=len(points)
    numerator=sum(count*2**len(sig) for sig,count in signatures.items())
    if numerator % (2*pgl_order):
        raise ArithmeticError('Signed Burnside average is nonintegral.')
    weight_sums=[0]*(length+1)
    for sig,count in signatures.items():
        for i,coefficient in enumerate(weight_polynomial(sig)):
            weight_sums[i]+=count*coefficient
    classes_by_weight=[value//pgl_order for value in weight_sums[:(length+1)//2]]
    if any(value % pgl_order for value in weight_sums):
        raise ArithmeticError('Weight orbit average is nonintegral.')
    orbits=orbit_traversal(m,scales,points,index,pgl_order)
    orbit_weight_counts=Counter(x['min_weight'] for x in orbits)
    if len(orbits)!=numerator//(2*pgl_order) or sum(x['orientation_orbit_size'] for x in orbits)!=2**length:
        raise ArithmeticError('Independent orbit and Burnside computations disagree.')
    if [orbit_weight_counts[r] for r in range((length+1)//2)]!=classes_by_weight:
        raise ArithmeticError('Weight profiles disagree.')
    binary_gl_order=1
    for i in range(2*m): binary_gl_order*=(2**(2*m)-2**i)
    for orbit in orbits:
        orbit['full_GL_conjugacy_class_size']=binary_gl_order//orbit['full_linear_stabilizer_order']
    result=dict(m=m,n=2*m,line_count=length,orientation_count=2**length,
        gl_order=3*pgl_order,spread_stabilizer_order=6*pgl_order,
        projective_action_order=pgl_order,burnside_numerator_projective=numerator,
        conjugacy_class_count=len(orbits),classes_by_min_weight=classes_by_weight,
        stabilizer_order_histogram=dict(sorted(Counter(x['full_linear_stabilizer_order'] for x in orbits).items())),
        minimal_C3_class_count=sum(x['full_linear_stabilizer_order']==3 for x in orbits),
        minimal_C3_orientation_count=sum(x['orientation_orbit_size'] for x in orbits if x['full_linear_stabilizer_order']==3),
        projective_cycle_signatures=[dict(cycle_lengths=list(sig),multiplicity=count) for sig,count in sorted(signatures.items())],
        point_representatives=points,orbits=orbits)
    print(json.dumps({k:result[k] for k in ('m','line_count','conjugacy_class_count','classes_by_min_weight','stabilizer_order_histogram','minimal_C3_class_count')})+f' ({time.monotonic()-started:.2f}s)',flush=True)
    return result

if __name__=='__main__':
    root=Path(__file__).resolve().parent
    results=dict(field='F2[w]/(w^2+w+1)',coordinate_encoding='base-four little-endian; w=2',scope='standard Desarguesian spread only',results=[study(2),study(3)])
    (root/'standard_spread_results.json').write_text(json.dumps(results,indent=2)+'\n',encoding='utf-8')
    print('All standard-spread orbit computations passed.')
