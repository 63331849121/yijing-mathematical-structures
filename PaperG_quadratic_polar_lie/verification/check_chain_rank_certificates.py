"""Independently replay the exact central-extension rank certificates.

This imports no generator or solver code. Matrices are checked over GF(2)
by SymPy, equations are rebuilt from the stored quadratic maps, and all
degree-four equations are checked against every advertised kernel vector.
"""
from pathlib import Path
import json
import hashlib
from itertools import combinations
from sympy import Matrix,GF
from sympy.polys.matrices import DomainMatrix

HERE=Path(__file__).resolve().parent/'chain_rank_certificates'


def rank_GF2(vectors,width):
    if not vectors:return 0
    matrix=Matrix([[(v >> i)&1 for i in range(width)] for v in vectors])
    return DomainMatrix.from_Matrix(matrix).convert_to(GF(2)).rank()


def omega(v,m):
    low=v & ((1 << m)-1)
    high=v >> m
    return high|((low^high) << m)


if __name__=='__main__':
    records=[]
    for entry in json.loads((HERE/'manifest.json').read_text(encoding='utf-8')):
        data=(HERE/entry['file']).read_bytes()
        assert hashlib.sha256(data).hexdigest()==entry['sha256']
        cert=json.loads(data)
        n=cert['n']
        masks=cert['quadratic_input_masks']
        coefficients=cert['quadratic_map_coefficients']
        m=len(masks)
        width=2*m
        def equation(x,bit):
            fx=0
            for t,c in zip(masks,coefficients):
                if (x & t)==t:fx ^= c
            a=b=0
            for i,t in enumerate(masks):
                if (fx & t)==t:a |= 1 << i
                if (x & t)==t:b |= 1 << i
            return ((a^b)|(b << m)) if bit==0 else (b|(a << m))
        selected=[]
        for record in cert['independent_equations']:
            row=int(record['row_hex'],16)
            assert row==equation(record['point'],record['output_bit'])
            selected.append(row)
        assert rank_GF2(selected,width)==cert['claimed_rank']
        kernel=[int(v,16) for v in cert['kernel_basis_hex']]
        assert rank_GF2(kernel,width)==len(kernel)
        assert cert['claimed_rank']+len(kernel)==width
        equation_count=0
        for k in range(1,5):
            for indices in combinations(range(n),k):
                x=sum(1 << i for i in indices)
                for bit in range(2):
                    row=equation(x,bit)
                    assert all((row & v).bit_count()%2==0 for v in kernel)
                    equation_count+=1
        cob=[int(v,16) for v in cert['coboundary_vectors_hex']]
        rebuilt=[]
        for j in range(n):
            v=0
            for i,(t,c) in enumerate(zip(masks,coefficients)):
                value=((c >> j)&1) ^ (2 if t==(1 << j) else 0)
                v |= (value & 1) << i
                v |= ((value >> 1)&1) << (m+i)
            rebuilt.extend((v,omega(v,m)))
        assert cob==rebuilt
        assert rank_GF2(cob,width)==cert['coboundary_rank']
        extended=list(cob)
        for rep in cert['named_quotient_basis']:
            v=int(rep['vector_hex'],16)
            extended.extend((v,omega(v,m)))
        assert rank_GF2(extended,width)==len(kernel)
        assert rank_GF2(kernel+extended,width)==len(kernel)
        row={'n':n,'status':'PASS','independent_engine':'SymPy DomainMatrix over GF(2)',
             'equations_reconstructed_and_checked':equation_count,
             'rank':cert['claimed_rank'],'kernel_dimension':len(kernel),
             'extension_quotient_F4_dimension':cert['quadratic_extension_quotient_F4_dimension']}
        records.append(row)
        print(json.dumps(row),flush=True)
    (HERE/'independent_check_results.json').write_text(json.dumps(
        {'status':'PASS','not_Lean_formalization':True,'records':records},indent=2),encoding='utf-8')
