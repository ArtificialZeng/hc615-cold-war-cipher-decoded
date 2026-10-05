#!/usr/bin/env python3
"""Opt-in replay of the archived fixed-budget control/target searches.

Never changes stored evidence. Compiles only source code from this repository.
No truth/answer file is passed to the C++ inference process. Saved-result and
control-truth comparisons occur after process completion. Different C++ library
implementations can change stochastic trajectories; a seed is not a cross-STL
byte-reproducibility guarantee. The exact forward certificate is portable.
"""
import argparse
import datetime
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
from common import ROOT, audit_result, check_inputs_manifest, load, read_model, sha

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--controls',action='store_true')
    parser.add_argument('--target',action='store_true')
    parser.add_argument('--compiler',help='C++17 compiler command/path; defaults CXX or clang++/g++')
    parser.add_argument('--output',type=Path,help='New output directory; defaults ignored build/replay-UTC')
    args = parser.parse_args()
    if not args.controls and not args.target: parser.error('Select --controls and/or --target')
    if sys.byteorder != 'little': parser.error('Historical C++ model reader requires a little-endian platform')
    compiler = args.compiler or os.environ.get('CXX') or shutil.which('clang++') or shutil.which('g++')
    if not compiler: parser.error('Install a C++17 compiler (clang++ or g++)')
    check_inputs_manifest(); config = load(ROOT/'config/reproduction.json'); model = read_model()
    out = args.output or ROOT/('build/replay-'+datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ'))
    if out.exists(): parser.error('Output exists; choose a new directory')
    out.mkdir(parents=True)
    (out/'CONFIG.json').write_text(json.dumps(config,indent=2)+'\n',encoding='utf-8')
    version = subprocess.run([compiler,'--version'],capture_output=True,text=True,check=True)
    (out/'COMPILER_VERSION.txt').write_text(version.stdout,encoding='utf-8')
    rows = []
    for kind in (['controls'] if args.controls else [])+(['target'] if args.target else []):
        branch = config[kind]
        if sha(ROOT/branch['source']) != branch['source_sha256']: raise ValueError('Solver source differs from registered release')
        binary = out/(kind+'_solver'+('.exe' if os.name == 'nt' else ''))
        subprocess.run([compiler,'-O3','-std=c++17',str(ROOT/branch['source']),'-o',str(binary)],check=True)
        indices = range(6) if kind == 'controls' else range(1)
        for i in indices:
            name = 'C%02d'%i if kind == 'controls' else 'target'
            input_path = ROOT/(branch['inputs'][i] if kind == 'controls' else branch['input'])
            seed = branch['seeds'][i] if kind == 'controls' else branch['seed']
            result_path = out/(name+'_result.json')
            command = [str(binary.resolve()),str(ROOT/config['model']),str(input_path),str(ROOT/config['frequency_order']),str(seed),str(config['restarts']),str(config['steps_per_restart']),str(result_path.resolve())]
            completed = subprocess.run(command,capture_output=True,text=True,check=True)
            (out/(name+'_stderr.txt')).write_text(completed.stderr,encoding='utf-8')
            # Truth and saved candidate are first read only after inference.
            result = load(result_path); code = [int(x) for x in input_path.read_text().split()]
            audit_result(result,code,model)
            saved = load(ROOT/(branch['saved_results'][i] if kind == 'controls' else branch['saved_result']))
            row = {'kind':kind,'id':name,'seed':seed,'restarts':16,'steps_per_restart':32768,'score':result['score'],'matches_archived_plaintext':result['plain'] == saved['plain'],'matches_archived_full26_key':result['key'] == saved['key'],'truth_passed_to_inference':False,'result_sha256':sha(result_path)}
            if kind == 'controls':
                truth = load(ROOT/('data/controls/'+name+'_truth.json'))['plain']
                row['letter_accuracy'] = sum(a==b for a,b in zip(result['plain'],truth) if b!=' ')/sum(c!=' ' for c in truth)
            rows.append(row); print(json.dumps(row),flush=True)
    (out/'REPLAY_REPORT.json').write_text(json.dumps({'status':'FIXED_BUDGET_REPLAY_COMPLETED','runs':rows,'portability_note':config['compiler_note'],'original_evidence_modified':False},indent=2)+'\n',encoding='utf-8')
if __name__ == '__main__': main()
