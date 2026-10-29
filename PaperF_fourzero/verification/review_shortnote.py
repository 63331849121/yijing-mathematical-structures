"""Cross-file, archive, table and evidence-scope checks before deployment."""
import hashlib
import json
from pathlib import Path
import re
from pypdf import PdfReader

ROOT = Path('C:/Users/master/Documents/Codex/mywebsite')
S = ROOT/'output/pdf/PaperF_shortnote_2026-10-27'
checks = {}
meta = json.loads((S/'shortnote_metadata.json').read_text(encoding='utf-8'))
tex = (S/'PaperF_fourzero.tex').read_text(encoding='utf-8')
raw = re.search(r'\\begin\{abstract\}(.*?)\\end\{abstract\}', tex, re.S).group(1)
normalized = raw.replace(r'$\mathbb F_2$', 'F2')
assert ' '.join(normalized.split()) == meta['abstract_en']
assert (S/'abstract_en.txt').read_text(encoding='utf-8').strip() == meta['abstract_en']
assert (S/'abstract_zh.txt').read_text(encoding='utf-8').strip() == meta['abstract_zh']
for name in ['arXiv_submission_form.txt', 'ChinaXiv_submission_form.txt']:
    text = (S/name).read_text(encoding='utf-8')
    assert meta['title'] in text and meta['abstract_en'] in text
    assert 'pending' not in text and '待编译' not in text
assert meta['abstract_zh'] in (S/'ChinaXiv_submission_form.txt').read_text(encoding='utf-8')
checks['abstracts_and_submission_forms'] = True
labels = re.findall(r'\\label\{([^}]+)\}', tex)
refs = re.findall(r'\\(?:eqref|ref)\{([^}]+)\}', tex)
bib = re.findall(r'\\bibitem\{([^}]+)\}', tex)
used = [key for block in re.findall(r'\\cite(?:\[[^\]]*\])?\{([^}]+)\}', tex) for key in block.split(',')]
assert len(labels) == len(set(labels))
assert not set(refs) - set(labels)
assert set(bib) == set(used)
checks['references_and_citations'] = True
assert len(PdfReader(S/'PaperF_fourzero.pdf').pages) == meta['pages'] == 7
assert len(PdfReader(S/'archive/full_version_2026-10-27/PaperF_fourzero.pdf').pages) == 17
compiled = json.loads((S/'verification/compile_report.json').read_text())
assert compiled['compile_return_code'] == 0 and not compiled['warnings']
checks['compile_and_page_counts'] = True

archive = S/'archive/full_version_2026-10-27'
manifest = json.loads((S/'archive/full_version_manifest.json').read_text())
for name, digest in manifest.items():
    assert hashlib.sha256((archive/name).read_bytes()).hexdigest() == digest
assert len(manifest) == 38
assert hashlib.sha256((S/'PaperF_fourzero_zenodo.zip').read_bytes()).hexdigest() == \
       '10d4de6c38af43089349ba66f4b764b0d4ce8f2394ef2a7e7a52fd251b1f6992'
checks['complete_old_version_and_old_deposit_unchanged'] = True

v = S/'verification/primitivity'
audit = json.loads((v/'summary.json').read_text())
assert audit['status'] == 'PASS' and audit['primitive_total_6_200'] == 2663
for name, digest in audit['input_sha256'].items():
    assert hashlib.sha256((v/'inputs'/name).read_bytes()).hexdigest() == digest
assert hashlib.sha256((v/'verify_primitivity.py').read_bytes()).hexdigest() == audit['script_sha256']
old_counts = json.loads((v/'inputs/_四零回文本原计数_6到200.json').read_text(encoding='utf-8'))
current = json.loads((S/'_四零回文本原计数_6到200.json').read_text(encoding='utf-8'))
fresh = json.loads((v/'counts_6_200.json').read_text())
assert len(old_counts) == len(current) == len(fresh) == 98
edits = []
for old, new, computed in zip(old_counts, current, fresh):
    assert old['n'] == new['n'] == computed['n']
    assert old['primitive'] == new['primitive'] == computed['primitive']
    assert [old['first_i'], old['first_j']] == computed['first']
    assert new['first_j_i1'] == computed['first_j_i1']
    for key in old:
        if old[key] != new[key]:
            assert key == 'first_j_i1' and old[key] is None
            edits.append((old['n'], key))
assert len(edits) == 16
verdicts = json.loads((v/'candidate_verdicts_6_200.json').read_text())
assert sum(len(row['verdicts']) for row in verdicts) == 161700
assert sum(row['verdicts'].count('P') for row in verdicts) == 2663
for row, count in zip(verdicts, fresh):
    assert row['n'] == count['n']
    assert row['verdicts'].count('P') == count['primitive']
    assert len(row['verdicts']) == count['candidates']
by_n = {row['n']: row for row in fresh}
table = re.search(r'\\midrule(.*?)\\bottomrule', tex, re.S).group(1)
for n, candidates, primitive, i, j in re.findall(
        r'(\d+)\s*&\s*(\d+)\s*&\s*(\d+)\s*&\s*\$\((\d+),(\d+)\)\$', table):
    row = by_n[int(n)]
    assert int(candidates) == row['candidates'] and int(primitive) == row['primitive']
    assert [int(i), int(j)] == row['first']
checks['complete_counts_table_and_16_scoped_metadata_corrections'] = True
firsts = json.loads((v/'first_witness_certificates_6_300.json').read_text())
assert [row['n'] for row in firsts] == list(range(6, 301, 2))
factors = {row['n']: row['prime_powers'] for row in json.loads((v/'factor_audit.json').read_text())['factorizations']}
for row in firsts:
    assert row['irreducible'] and row['full_power_is_one']
    assert set(row['proper_order_test_residues']) == {a['p'] for a in factors[row['n']]}
    assert all(int(residue, 16) != 1 for residue in row['proper_order_test_residues'].values())
checks['all_148_first_witness_records'] = True
association = json.loads((S/'_四零回文_2p_有限配对关联.json').read_text(encoding='utf-8'))
for row in association:
    assert row['N4'] == by_n[row['n']]['primitive']
    assert row['N'] == by_n[row['n']]['candidates']
checks['retained_frequency_data_consistency'] = True
assert 'classical binary degree-two Krawtchouk' in tex
assert 'no general irreducibility criterion' in tex
assert 'Sixteen missing auxiliary' in tex
assert 'first_j_i1' in (S/'README.md').read_text(encoding='utf-8')
assert 'not exported primality' in tex
checks['classical_attribution_and_evidence_limits'] = True
report = {'status': 'PASS', 'checks': checks,
          'source_sha256': hashlib.sha256((S/'PaperF_fourzero.tex').read_bytes()).hexdigest(),
          'pdf_sha256': hashlib.sha256((S/'PaperF_fourzero.pdf').read_bytes()).hexdigest(),
          'pages': 7, 'preserved_old_pages': 17, 'preserved_old_files': 38,
          'visual_review': 'All seven rendered pages inspected; final amended page 4 inspected again.',
          'scope': 'Artifact consistency and supplied records; full arithmetic run is documented separately.'}
(S/'verification/shortnote_review.json').write_text(json.dumps(report, indent=2), encoding='utf-8')
print(json.dumps(report, indent=2))
