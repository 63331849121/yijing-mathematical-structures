"""Fresh kernel check for the new dependency-free combinatorial module.

The three original mathlib files are compared with their historical hashes.
Any current-revision rerun record is checked separately, without rewriting
the historical record or pretending it describes the distributed sources.
"""
from pathlib import Path
import hashlib
import json
import re
import subprocess

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
TOOLCHAIN='leanprover/lean4:v4.31.0'


def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    installed=subprocess.run(['elan','toolchain','list'],capture_output=True,text=True,check=True)
    if TOOLCHAIN not in installed.stdout:
        raise RuntimeError('Pinned Lean toolchain is not installed; no automatic installation attempted')
    version=subprocess.run(['elan','run',TOOLCHAIN,'lean','--version'],capture_output=True,text=True,check=True)
    p=HERE/'InverseSupportGrid.lean'
    if re.search(r'\b(?:sorry|admit)\b',p.read_text(encoding='utf-8')):
        raise RuntimeError('Proof placeholder found')
    run=subprocess.run(['elan','run',TOOLCHAIN,'lean',p.name],cwd=HERE,capture_output=True,text=True)
    output=run.stdout+run.stderr
    (HERE/'lean_check.log').write_text(version.stdout+'\n'+output,encoding='utf-8')
    if run.returncode or 'error:' in output or 'warning:' in output:
        raise RuntimeError(output)
    names=['cover_inverse','mixed_corners','two_crosses_intersect_in_inverse_pair',
           'covered_inverse_support_is_pair','third_point_excludes_cover','inverse_pair_cover_iff']
    for name in names:
        expected="'PaperA.InverseSupportGrid."+name+"' does not depend on any axioms"
        if expected not in output:raise RuntimeError('Missing axiom audit: '+name)
    original=ROOT/'provenance/original_repository/PaperA_scalar_realizations/lean'
    old=json.loads((original/'checked_environment.json').read_text(encoding='utf-8'))
    hashes={}
    fresh_path=ROOT/'verification/supplement_sync_2026-10-26/original_lean_fresh_checks.json'
    fresh=json.loads(fresh_path.read_text(encoding='utf-8')) if fresh_path.exists() else None
    reruns={x['file']:x for x in fresh['files']} if fresh else {}
    for name,record in old['files'].items():
        actual=sha(original/name)
        matches=actual==record['sha256']
        rerun=reruns.get(name)
        if rerun and (rerun['source_sha256']!=actual or rerun['exit_code']!=0):
            raise RuntimeError('Current rerun record does not match distributed source: '+name)
        hashes[name]={'sha256':actual,'historical_record_sha256':record['sha256'],
            'matches_archived_success_record':matches,
            'current_revision_fresh_rerun_record_matches':bool(rerun),
            'legacy_rerun_performed_by_this_script':False}
    report={'status':'PASS','toolchain':TOOLCHAIN,'compiler':version.stdout.strip(),
        'module':'formalization/InverseSupportGrid.lean','source_sha256':sha(p),
        'fresh_lean_exit_code':run.returncode,'new_declarations_checked':names,
        'all_six_declarations_have_no_axiom_dependencies':True,'proof_placeholders_found':False,
        'imports':['Init'],'mathlib_dependency':False,
        'full_cyclic_group_CRT_interface_formalized':False,
        'finite_field_Frobenius_interface_formalized':False,
        'finite_field_certificates_checked_inside_Lean':False,
        'geometric_character_estimates_formalized':False,
        'full_Theorem_54_formalized':False,
        'original_three_files':hashes,
        'archived_mathlib_commit':old['mathlib_commit'],
        'external_human_peer_review_claimed':False}
    (HERE/'lean_check.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'PASS','new_core_lemmas':len(names),'extra_axiom_dependencies':False,
        'historical_hash_mismatches':[k for k,v in hashes.items() if not v['matches_archived_success_record']],
        'current_revision_legacy_reruns_recorded':sum(bool(v['current_revision_fresh_rerun_record_matches']) for v in hashes.values()),
        'full_Theorem_54_formalized':False}))


if __name__=='__main__':main()
