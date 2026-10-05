#!/usr/bin/env python3
"""Rebuild the unchanged quadgram model/frequencies from the pinned train file.

The generated model, word counts and frequency order inherit CC BY-NC-SA 4.0.
Target transcript/plaintext is never read. Default output is a new ignored build
directory; frozen release files are never overwritten.
"""
import argparse
import array
import collections
import json
import math
import re
import sys
import unicodedata
from pathlib import Path
from common import ROOT, ALPHABET, load, sha

def words(text):
    text = ''.join(c for c in unicodedata.normalize('NFKD',text.lower()) if not unicodedata.combining(c))
    return re.findall('[a-z]+',text)

def sentences(path):
    with Path(path).open(encoding='utf-8') as stream:
        for line in stream:
            if line.startswith('# text = '): yield line[len('# text = '):].rstrip('\r\n')

def documents(path):
    current = []; ident = None
    with Path(path).open(encoding='utf-8') as stream:
        for line in stream:
            if line.startswith('# newdoc id = '):
                if current: yield ident,current
                ident = line[len('# newdoc id = '):].rstrip('\r\n'); current = []
            elif line.startswith('# text = '): current.append(line[len('# text = '):].rstrip('\r\n'))
    if current: yield ident,current

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=ROOT/'build/language_model_rebuilt')
    args = parser.parse_args()
    resources = load(ROOT/'config/sources.json')['resources']
    train = ROOT/resources['train']['path']
    if not train.is_file() or sha(train) != resources['train']['sha256']:
        parser.error('Fetch pinned corpus first: python3 scripts/fetch_sources.py --language-corpus')
    if args.output.exists(): parser.error('Output exists; choose a new directory')
    args.output.mkdir(parents=True)
    counts = collections.Counter(); frequency = collections.Counter(); grams = collections.Counter()
    for sentence in sentences(train):
        tokens = words(sentence)
        if not tokens: continue
        text = ' '+' '.join(tokens)+' '
        counts.update(tokens); frequency.update(text)
        a = [ALPHABET.index(c) for c in text]
        for i in range(len(a)-3): grams[((a[i]*27+a[i+1])*27+a[i+2])*27+a[i+3]] += 1
    total = sum(grams.values()); smoothing = .05; denominator = total+smoothing*27**4
    model = array.array('f',(math.log((grams.get(i,0)+smoothing)/denominator) for i in range(27**4)))
    if model.itemsize != 4: raise ValueError('IEEE754 float32 required')
    if sys.byteorder != 'little': model.byteswap()
    (args.output/'quadgram27.bin').write_bytes(model.tobytes())
    (args.output/'word_counts.tsv').write_text('word\tcount\n'+''.join(w+'\t'+str(n)+'\n' for w,n in sorted(counts.items())),encoding='utf-8')
    ordered = sorted(range(26),key=lambda i:(-frequency[ALPHABET[i]],i))
    (args.output/'frequency_order.txt').write_text(' '.join(map(str,ordered))+'\n',encoding='utf-8')
    rows = []
    for name in ['quadgram27.bin','word_counts.tsv','frequency_order.txt']:
        actual = sha(args.output/name); expected = sha(ROOT/'data/model'/name)
        if actual != expected: raise ValueError('Rebuild mismatch: '+name)
        rows.append({'file':name,'sha256':actual,'matches_frozen_cache':True})
    print(json.dumps({'status':'PASS_BYTE_IDENTICAL_REBUILD','train_words':sum(counts.values()),'train_distinct_words':len(counts),'train_ngrams':total,'target_read':False,'files':rows},indent=2))
if __name__ == '__main__': main()
