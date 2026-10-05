#!/usr/bin/env python3
"""Verify every prepared public-release file against its SHA-256 manifest.

A manifest detects accidental alteration; it is not an external signature or a
proof of historical truth. The scientific verifier separately checks the result.
"""
from pathlib import Path
import hashlib
import json
import sys

ROOT=Path(__file__).resolve().parents[1]

def main():
    manifest=json.loads((ROOT/'RELEASE_MANIFEST.json').read_text(encoding='utf-8'))
    for row in manifest['files']:
        rel=Path(row['path'])
        if rel.is_absolute() or '..' in rel.parts:raise ValueError('Unsafe manifest path')
        p=ROOT/rel
        if not p.is_file() or p.is_symlink():raise ValueError('Missing or linked release file: '+str(rel))
        data=p.read_bytes()
        if len(data)!=row['bytes'] or hashlib.sha256(data).hexdigest()!=row['sha256']:
            raise ValueError('Release file differs: '+str(rel))
    print(json.dumps({'status':'PASS','release':manifest['version'],'files_checked':len(manifest['files']),'external_signature_or_historical_truth_proven':False},indent=2))
    return 0

if __name__=='__main__':
    try:sys.exit(main())
    except (OSError,ValueError,KeyError) as exc:
        print('Release verification FAILED: '+str(exc),file=sys.stderr);sys.exit(1)
