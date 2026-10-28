"""Fresh Lean kernel checks of the selective support interfaces.

Use an already installed Lake project with the exact dependency manifest.
No network install or historical successful result is substituted for a run.
The original three archived modules are outside this check.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent
TOOLCHAIN = 'leanprover/lean4:v4.31.0'
MODULES = ['InverseSupportGrid', 'SupportCoverBranches',
           'CyclicSupport', 'ReciprocalTraceSupport', 'MultiplicativeSupport',
           'ReciprocalTraceCounting', 'NormOneSupportBridge',
           'RelativeTraceTransfer', 'NamedNormTraceTransfer']
STANDARD_AXIOMS = {'propext', 'Classical.choice', 'Quot.sound'}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def without_comments(text):
    # Lean has nested block comments. Preserve newlines for declaration scanning.
    out, i, depth = [], 0, 0
    while i < len(text):
        if text.startswith('/-', i):
            depth += 1; i += 2
        elif depth and text.startswith('-/', i):
            depth -= 1; i += 2
        elif depth:
            if text[i] == '\n': out.append('\n')
            i += 1
        elif text.startswith('--', i):
            end = text.find('\n', i)
            i = len(text) if end < 0 else end
        else:
            out.append(text[i]); i += 1
    if depth: raise RuntimeError('Unclosed block comment')
    return ''.join(out)


def main():
    if '--emit-lean-env' in sys.argv:
        print(json.dumps({k: os.environ.get(k, '') for k in
                          ['LEAN_PATH', 'LEAN_SRC_PATH']}))
        return
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--lake-project', type=Path, default=HERE)
    parser.add_argument('--elan', default=shutil.which('elan') or 'elan')
    args = parser.parse_args()
    project = args.lake_project.resolve()
    expected = json.loads((HERE/'lake-manifest.json').read_text(encoding='utf-8'))
    actual = json.loads((project/'lake-manifest.json').read_text(encoding='utf-8'))
    pins = {r['name']: r['rev'] for r in expected['packages']}
    if pins != {r['name']: r['rev'] for r in actual['packages']}:
        raise RuntimeError('Dependency manifest differs from pinned environment')
    if (project/'lean-toolchain').read_text().strip() != TOOLCHAIN:
        raise RuntimeError('Toolchain mismatch')
    dependency_checks = []
    for name, rev in pins.items():
        path = project/'.lake/packages'/name
        run = subprocess.run(['git', '-C', str(path), 'rev-parse', 'HEAD'],
                             capture_output=True, text=True, check=True)
        if run.stdout.strip() != rev:
            raise RuntimeError('Dependency checkout mismatch: '+name)
        dirty = subprocess.run(['git', '-C', str(path), 'status', '--porcelain',
                                '--untracked-files=no'], capture_output=True,
                               text=True, check=True)
        if dirty.stdout.strip():
            raise RuntimeError('Tracked dependency modifications: '+name)
        dependency_checks.append({'name': name, 'commit': rev,
                                  'tracked_checkout_clean': True})
    elan = [args.elan, 'run', TOOLCHAIN]
    version = subprocess.run(elan+['lean', '--version'], capture_output=True,
                             text=True, check=True).stdout.strip()
    env_run = subprocess.run(elan+['lake', 'env', sys.executable,
        str(Path(__file__).resolve()), '--emit-lean-env'], cwd=project,
        capture_output=True, text=True, check=True)
    lean_env = json.loads(env_run.stdout)
    declarations = []
    proof_declarations = []
    definitions = []
    sources = []
    logs = [version]
    # Keep scratch files inside the explicitly selected workspace project.
    # TemporaryDirectory cleans only this freshly created, validated child.
    with tempfile.TemporaryDirectory(prefix='.paperA-lean-interfaces-', dir=project) as temp:
        scratch = Path(temp)
        if scratch.resolve().parent != project:
            raise RuntimeError('Scratch directory escaped the selected project')
        env = os.environ.copy()
        env.update(lean_env)
        env['LEAN_PATH'] = str(scratch)+os.pathsep+lean_env['LEAN_PATH']
        for module in MODULES:
            src = HERE/(module+'.lean')
            code = without_comments(src.read_text(encoding='utf-8'))
            if re.search(r'\b(?:sorry|admit|native_decide)\b', code):
                raise RuntimeError('Forbidden proof placeholder/native tactic: '+module)
            if re.search(r'^\s*(?:axiom|constant)\s', code, re.M):
                raise RuntimeError('New axiom/constant declaration: '+module)
            namespaces = re.findall(r'^namespace\s+([\w.]+)\s*$', code, re.M)
            if len(namespaces) != 1:
                raise RuntimeError('Declaration audit needs one explicit namespace: '+module)
            names = re.findall(r'^\s*(?:theorem|lemma)\s+(\w+)', code, re.M)
            defs = re.findall(r'^\s*(?:noncomputable\s+)?(?:def|abbrev)\s+(\w+)', code, re.M)
            proof_declarations.extend(namespaces[0]+'.'+name for name in names)
            definitions.extend(namespaces[0]+'.'+name for name in defs)
            declarations.extend(namespaces[0]+'.'+name for name in names+defs)
            shutil.copyfile(src, scratch/src.name)
            run = subprocess.run(elan+['lean', '-o', module+'.olean', src.name],
                cwd=scratch, env=env, capture_output=True, text=True)
            output = run.stdout+run.stderr
            logs.append('\n===== '+module+' =====\n'+output)
            if run.returncode or re.search(r'\b(?:error|warning):', output):
                (HERE/'interfaces_check.log').write_text('\n'.join(logs),encoding='utf-8')
                raise RuntimeError('Lean failed: '+module+'\n'+output)
            sources.append({'module': module, 'sha256': sha(src),
                'proof_declarations': names, 'definitions': defs,
                'fresh_exit_code': run.returncode,
                'imports': re.findall(r'^import\s+(.+)$', code, re.M)})
        audit = '\n'.join('import '+m for m in MODULES)+'\n'
        audit += '\n'.join('#print axioms '+n for n in declarations)+'\n'
        (scratch/'Audit.lean').write_text(audit, encoding='utf-8')
        run = subprocess.run(elan+['lean', 'Audit.lean'], cwd=scratch, env=env,
                             capture_output=True, text=True)
        output = run.stdout+run.stderr
        logs.append('\n===== all-declaration axiom audit =====\n'+output)
        if run.returncode or re.search(r'\b(?:error|warning):', output):
            raise RuntimeError(output)
        audits = {}
        for name in declarations:
            if "'"+name+"' does not depend on any axioms" in output:
                axioms = []
            else:
                match = re.search(re.escape("'"+name+"' depends on axioms:")+
                                  r'\s*\[([^\]]*)\]', output)
                if not match: raise RuntimeError('Missing axiom audit: '+name)
                axioms = [a.strip() for a in match.group(1).split(',') if a.strip()]
            if set(axioms)-STANDARD_AXIOMS:
                raise RuntimeError('Unexpected axiom dependency: '+name+' '+str(axioms))
            audits[name] = axioms
    (HERE/'interfaces_check.log').write_text('\n'.join(logs), encoding='utf-8')
    report = {'status': 'PASS', 'checked_utc': datetime.now(timezone.utc).isoformat(),
        'toolchain': TOOLCHAIN, 'compiler': version, 'sources': sources,
        'declaration_count': len(declarations), 'axiom_dependencies': audits,
        'proof_declaration_count': len(proof_declarations),
        'definition_count': len(definitions),
        'standard_foundational_axioms_only': True,
        'proof_placeholders_or_new_axioms': False,
        'dependency_commits': dependency_checks,
        'dependency_archive_cache_reused': True,
        'cache_free_build_performed': False,
        'legacy_three_modules_rerun': False,
        'full_Theorem_54_formalized': False,
        'geometric_character_estimates_formalized': False,
        'finite_field_certificates_checked_inside_Lean': False,
        'multiplicative_exponent_equivalence_constructed': True,
        'finite_field_root_subgroup_cardinality_derived': True,
        'two_preimages_and_filtered_parameter_count_proved': True,
        'root_subgroup_support_and_parameter_count_connected': True,
        'original_a_to_gamma_bijection_formalized': True,
        'exact_order_component_equivalence_formalized': True,
        'named_Algebra_norm_and_trace_interface_formalized': True,
        'original_M_c_cardinality_transfer_formalized': True,
        'original_M_c_shifted_support_identity_formalized': True,
        'zero_relative_trace_population_formalized': True,
        'count_scope': 'Structural cardinality identities, including the named norm/trace population; no geometric estimate or complete evaluation/classification is claimed.',
        'full_Theorem_51_formalized': False,
        'fixed_certificate_generator_change_of_coordinates_formalized': False,
        'scope_reference': 'INTERFACE_SCOPE.txt'}
    (HERE/'interfaces_check.json').write_text(
        json.dumps(report, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'status': 'PASS', 'modules': len(MODULES),
        'declarations': len(declarations), 'standard_foundational_axioms_only': True,
        'proof_declarations': len(proof_declarations), 'definitions': len(definitions),
        'full_Theorem_54_formalized': False}))


if __name__ == '__main__':
    main()
