"""Portable reproducibility helpers; Python 3.9+ standard library only."""
from pathlib import Path
import array
import hashlib
import json
import math
import sys

ROOT = Path(__file__).resolve().parents[1]
ALPHABET = 'abcdefghijklmnopqrstuvwxyz '

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def load(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))

def check_inputs_manifest():
    rows = load(ROOT/'config/engineering_inputs_manifest.json')['files']
    for row in rows:
        path = ROOT/row['path']
        if not path.is_file() or path.stat().st_size != row['bytes'] or sha(path) != row['sha256']:
            raise ValueError('Frozen engineering input hash mismatch: '+row['path'])
    return len(rows)

def read_model():
    config = load(ROOT/'config/reproduction.json')
    path = ROOT/config['model']
    if sha(path) != config['model_sha256']:
        raise ValueError('Scoring model hash mismatch')
    model = array.array('f')
    if model.itemsize != 4:
        raise ValueError('Scoring cache requires IEEE754 float32')
    model.frombytes(path.read_bytes())
    if sys.byteorder != 'little': model.byteswap()
    if len(model) != 27**4 or any(not math.isfinite(v) for v in model):
        raise ValueError('Invalid quadgram model')
    return model

def decode(code, key):
    if len(key) != 26 or sorted(key) != list(range(26)):
        raise ValueError('Non-bijective 26-slot solver key')
    if any(type(c) is not int or not 0 <= c <= 26 for c in code):
        raise ValueError('Invalid opaque solver input')
    return ''.join(' ' if c == 26 else chr(97+key[c]) for c in code)

def score(text, model):
    sequence = [ALPHABET.index(c) for c in text]
    return sum(model[((sequence[i]*27+sequence[i+1])*27+sequence[i+2])*27+sequence[i+3]] for i in range(len(sequence)-3))

def audit_result(result, code, model):
    trials = result['trials']
    if result['restarts'] != 16 or result['steps'] != 32768 or len(trials) != 16:
        raise ValueError('Archived result differs from registered search budget')
    for i, trial in enumerate(trials):
        if trial['restart'] != i or decode(code,trial['key']) != trial['plain']:
            raise ValueError('Trial rendering/key mismatch')
        if abs(score(trial['plain'],model)-trial['score']) > 1e-5:
            raise ValueError('Trial score differs from independent arithmetic')
    if decode(code,result['key']) != result['plain'] or abs(score(result['plain'],model)-result['score']) > 1e-5:
        raise ValueError('Winning candidate/key/score mismatch')
    winner = max(trials,key=lambda t:t['score'])
    if (result['key'],result['plain'],result['score']) != (winner['key'],winner['plain'],winner['score']):
        raise ValueError('Result does not equal best recorded restart')
    return len(trials)
