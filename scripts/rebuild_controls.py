#!/usr/bin/env python3
"""Rebuild the six pre-inference matched controls from pinned dev documents.

The historically selected windows, keys and seeds are deterministic. Truth files
inherit CC BY-NC-SA 4.0. This script does not run inference or read the target.
"""
import argparse
import json
import random
from pathlib import Path
from build_language_model import words, sentences, documents
from common import ROOT, ALPHABET, load, sha

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=ROOT/'build/controls_rebuilt')
    args = parser.parse_args()
    resources = load(ROOT/'config/sources.json')['resources']
    train = ROOT/resources['train']['path']; dev = ROOT/resources['dev']['path']
    for name,path in [('train',train),('dev',dev)]:
        if not path.is_file() or sha(path) != resources[name]['sha256']:
            parser.error('Fetch pinned corpus first: python3 scripts/fetch_sources.py --language-corpus')
    if args.output.exists(): parser.error('Output exists; choose a new directory')
    args.output.mkdir(parents=True)
    training = '\n'.join(' '.join(words(s)) for s in sentences(train))
    selected = []
    for document_id, text_sentences in documents(dev):
        all_words = words(' '.join(text_sentences))
        for start in range(0,max(0,len(all_words)-31),32):
            sample = all_words[start:start+32]
            letters = sum(map(len,sample)); classes = len(set(''.join(sample)))
            if not 195 <= letters <= 250 or not 20 <= classes <= 24: continue
            plain = ' '.join(sample)
            if plain in training: continue
            ci = len(selected); seed = 615310+ci
            key = list(range(26)); random.Random(seed).shuffle(key)
            code = [26 if c == ' ' else key[ALPHABET.index(c)] for c in plain]
            cid = 'C%02d'%ci
            (args.output/(cid+'_input.txt')).write_text(' '.join(map(str,code))+'\n',encoding='utf-8')
            truth = {'plain':plain,'forward_key':key,'document_id':document_id,'word_offset':start,'generation_seed':seed,'letters':letters,'classes':classes}
            (args.output/(cid+'_truth.json')).write_text(json.dumps(truth,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
            for suffix in ['input.txt','truth.json']:
                name = cid+'_'+suffix
                if sha(args.output/name) != sha(ROOT/'data/controls'/name):
                    raise ValueError('Rebuilt control differs from historical frozen input: '+name)
            selected.append({'id':cid,'document_id':document_id,'word_offset':start,'seed':seed,'letters':letters,'matches_frozen_files':True})
            break
        if len(selected) == 6: break
    if len(selected) != 6 or len({c['document_id'] for c in selected}) != 6:
        raise ValueError('Six distinct dev documents required')
    print(json.dumps({'status':'PASS_BYTE_IDENTICAL_CONTROLS_REBUILD','target_read':False,'inference_run':False,'controls':selected},indent=2))
if __name__ == '__main__': main()
