#!/usr/bin/env python3
"""Opt-in acquisition of pinned public inputs into an ignored local cache.

No archive pixels ship with this repository. Fetching establishes an exact local
copy, not redistribution permission. Hash changes fail rather than silently
replacing the research input. Only the pinned allowlisted HTTPS URLs are fetched.
"""
import argparse
import datetime
import hashlib
import json
import os
import sys
import tempfile
import urllib.request
from common import ROOT, load, sha

def fetch(name, entry):
    destination = ROOT/entry['path']
    if destination.exists():
        if destination.stat().st_size != entry['bytes'] or sha(destination) != entry['sha256']:
            raise ValueError('Existing cache does not match pinned source: '+entry['path'])
        return {'resource':name,'status':'already present, pinned hash verified','path':entry['path']}
    destination.parent.mkdir(parents=True,exist_ok=True)
    request = urllib.request.Request(entry['url'],headers={'User-Agent':'HC615-reproducibility/1.0'})
    temporary = None
    try:
        digest = hashlib.sha256(); size = 0
        with urllib.request.urlopen(request,timeout=45) as response:
            if response.status != 200: raise ValueError('Source did not return HTTP 200')
            with tempfile.NamedTemporaryFile(dir=destination.parent,delete=False) as output:
                temporary = output.name
                while True:
                    chunk = response.read(1024*1024)
                    if not chunk: break
                    size += len(chunk)
                    if size > entry['bytes']: raise ValueError('Source exceeded pinned size')
                    digest.update(chunk); output.write(chunk)
            final_url = response.geturl()
        if size != entry['bytes'] or digest.hexdigest() != entry['sha256']:
            raise ValueError('Downloaded source differs from pinned byte count/SHA-256: '+name)
        os.replace(temporary,destination); temporary = None
        receipt = {'resource':name,'url':entry['url'],'final_url':final_url,'access_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'bytes':size,'sha256':digest.hexdigest(),'status':200}
        destination.with_suffix(destination.suffix+'.receipt.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
        return receipt
    finally:
        if temporary is not None: os.unlink(temporary)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--archive-image',action='store_true')
    parser.add_argument('--language-corpus',action='store_true',help='About 74.3 MB train+dev, pinned README/license; CC BY-NC-SA 4.0')
    args = parser.parse_args()
    if not args.archive_image and not args.language_corpus: parser.error('Select --archive-image and/or --language-corpus explicitly')
    resources = load(ROOT/'config/sources.json')['resources']
    selected = (['archive_image'] if args.archive_image else []) + (['train','dev','language_readme','language_license'] if args.language_corpus else [])
    try:
        for name in selected: print(json.dumps(fetch(name,resources[name])),flush=True)
    except (ValueError,OSError) as exc:
        print('Source acquisition FAILED: '+str(exc),file=sys.stderr);return 1
    return 0
if __name__ == '__main__': sys.exit(main())
