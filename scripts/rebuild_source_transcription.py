#!/usr/bin/env python3
"""Rebuild source-only derived rows from frozen visual spec and fetched source image.
This mechanically reproduces prior glyph observations; it is not OCR.
No plaintext, language, candidate or optimizer is read. Frozen files are unchanged.
"""
import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path
import argparse
from common import sha, load

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'build/source_transcription_rebuilt'
SPEC = ROOT / 'data/source/manual_source_spec.json'
CLASS_ORDER = ['0','1','2','3','4','5','6','7','8','X','QMARK','POUND','ORNATE',
               'SECTION','H1','H2','SLASH','PERCENT','PLUS','LOWDOT','UPPER','VSTEM']


def write_json(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')


def pattern(seq):
    assigned = {}
    return [assigned.setdefault(x, len(assigned)) for x in seq]


def main():
    s = json.loads(SPEC.read_text())
    image_path = ROOT / load(ROOT/'config/sources.json')['resources']['archive_image']['path']
    if not image_path.is_file(): raise ValueError('Fetch source first: python3 scripts/fetch_sources.py --archive-image')
    source = image_path.read_bytes()
    OUT.mkdir(parents=True, exist_ok=False)
    assert hashlib.sha256(source).hexdigest() == s['source_sha256']
    assert set(CLASS_ORDER) == set(s['glyph_classes'])
    ids = {c: f'C{i+1:03}' for i, c in enumerate(CLASS_ORDER)}
    glyphs, words, lines = [], [], []
    for li in s['lines']:
        xcursor = 0
        line_start = len(glyphs)
        for wi, seq in enumerate(li['words'], 1):
            word_id = f'L{li["line"]:02}W{wi:02}'
            word_start = len(glyphs)
            for ti, c in enumerate(seq, 1):
                x = li['glyph_centres_x'][xcursor]
                xcursor += 1
                bbox = [round(x)-10, li['bbox'][1], round(x)+11, li['bbox'][3]]
                underlined = any(a['line'] == li['line'] and abs(a['x'] - x) < 1
                                 for a in s['observed_red_underlines'])
                glyphs.append({'occurrence_id': f'O{len(glyphs)+1:04}',
                               'glyph_id': ids[c], 'raw_visual_label': c,
                               'line': li['line'], 'red_segment': wi,
                               'segment_id': word_id, 'position_in_segment': ti,
                               'position_in_line': xcursor, 'source_bbox': bbox,
                               'source_center_x': x, 'source_image': s['source_image'],
                               'source_sha256': s['source_sha256'],
                               'font_candidates': s['glyph_classes'][c]['font_candidates'],
                               'red_underline_observed': underlined,
                               'lacuna': False,
                               'uncertainty': 'visual class stable; exact font-name uncertain'
                                    if len(s['glyph_classes'][c]['font_candidates']) > 1 else 'none at visual-class level'})
            ws = glyphs[word_start:]
            words.append({'segment_id': word_id, 'line': li['line'], 'segment_in_line': wi,
                          'word_boundary_is_hypothesis': True,
                          'glyph_ids': [g['glyph_id'] for g in ws],
                          'visual_labels': seq, 'pattern': pattern(seq),
                          'occurrence_ids': [g['occurrence_id'] for g in ws],
                          'source_bbox': [ws[0]['source_bbox'][0], li['bbox'][1],
                                          ws[-1]['source_bbox'][2], li['bbox'][3]],
                          'red_annotation_bounds_x_approx': li['red_boundary_centres_x_approx'][wi-1:wi+1]})
        assert xcursor == len(li['glyph_centres_x'])
        lines.append({'line': li['line'], 'source_bbox': li['bbox'],
                      'glyph_count': len(glyphs)-line_start, 'red_segment_count': len(li['words']),
                      'occurrence_ids': [g['occurrence_id'] for g in glyphs[line_start:]]})
    assert len(glyphs) == 220 and len(words) == 32
    (OUT / 'glyph_occurrences.jsonl').write_text(''.join(json.dumps(g, ensure_ascii=False) + '\n' for g in glyphs))
    write_json(OUT / 'DEFAULT_WORDS.json', {'schema':'HC615_default_red_segment_tokens_v1',
                'source_sha256':s['source_sha256'], 'model':'22 distinct glyph identities; red divisions treated as candidate word boundaries',
                'words':words, 'lines':lines})
    write_json(OUT / 'glyph_inventory.json', [{**s['glyph_classes'][c], 'raw_visual_label':c,
                 'glyph_id':ids[c], 'occurrence_count':sum(g['raw_visual_label']==c for g in glyphs),
                 'first_occurrence':next(g['occurrence_id'] for g in glyphs if g['raw_visual_label']==c)} for c in CLASS_ORDER])
    (OUT / 'DEFAULT_visual_labels.txt').write_text('\n'.join(' | '.join(' '.join(w) for w in li['words']) for li in s['lines'])+'\n')
    (OUT / 'DEFAULT_opaque_ids.txt').write_text('\n'.join(' | '.join(' '.join(ids[c] for c in w) for w in li['words']) for li in s['lines'])+'\n')
    freq = Counter(g['glyph_id'] for g in glyphs)
    seq = [g['glyph_id'] for g in glyphs]
    repeat_words = defaultdict(list)
    for w in words:
        repeat_words[tuple(w['glyph_ids'])].append(w['segment_id'])
    ngram_repeats = {}
    for n in range(2, 9):
        repeats = defaultdict(list)
        for i in range(len(seq)-n+1):
            repeats[tuple(seq[i:i+n])].append(glyphs[i]['occurrence_id'])
        ngram_repeats[str(n)] = [{'glyph_ids': list(k), 'start_occurrences':v}
                  for k,v in sorted(repeats.items(), key=lambda kv:(-len(kv[1]),kv[0])) if len(v)>1][:50]
    write_json(OUT / 'STRUCTURAL_COUNTS.json', {
        'glyph_occurrences':len(glyphs), 'distinct_visual_classes':len(freq),
        'lines':lines, 'red_segments':len(words), 'red_vertical_boundaries_count':sum(len(li['red_boundary_centres_x_approx']) for li in s['lines']),
        'frequency':dict(sorted(freq.items())), 'segment_length_histogram':dict(sorted(Counter(len(w['glyph_ids']) for w in words).items())),
        'index_of_coincidence':sum(v*(v-1) for v in freq.values())/(len(glyphs)*(len(glyphs)-1)),
        'repeated_complete_red_segments':[{'glyph_ids':list(k),'segments':v} for k,v in repeat_words.items() if len(v)>1],
        'ngram_repeats_2_to_8':ngram_repeats,
        'repeat_scope':'continuous printed glyph sequence across red divisions/line breaks; source coordinates retained',
        'missing_glyph_or_lacuna_events':0,
        'qmark_occurrences_are_printed_cipher_signs':sum(g['raw_visual_label']=='QMARK' for g in glyphs),
        'handwritten220_used_as_count_input':False})
    write_json(OUT / 'SOURCE_ALTERNATIVES.json', {
        'DEFAULT': {'glyph_identity_merges':[], 'glyph_identity_splits':[], 'tokenization':'220 printed slots / 22 classes / red32 segments'},
        'font_name_alternatives': {c: s['glyph_classes'][c]['font_candidates'] for c in CLASS_ORDER if len(s['glyph_classes'][c]['font_candidates'])>1},
        'font_name_alternatives_change_opaque_ids':False,
        'red_boundary_models':[{'name':'RED_DIVISIONS_WORDS','segments':32,'status':'DEFAULT inference hypothesis, not demonstrated historical plaintext spaces'},
                               {'name':'RED_DIVISIONS_ANNOTATIONS_ONLY','token_sequence_unchanged':True,'status':'source-compatible formatting alternative; solver model must be separately registered'}],
        'unapproved_merges':['VSTEM with1','H1 withH2','UPPER withLOWDOT','POUND withORNATE orSECTION'],
        'lacuna_vs_qmark':'No lacuna observed. Repeated printed QMARK is a token, never missing-data placeholder.',
        'no_fluency_based_choices':True})
    (OUT / 'source_occurrence_roundtrip_labels.txt').write_text('\n'.join(' '.join(g['raw_visual_label'] for g in glyphs if g['line']==i) for i in range(1,9))+'\n')
    expected = [[x for word in li['words'] for x in word] for li in s['lines']]
    actual = [[g['raw_visual_label'] for g in glyphs if g['line']==i] for i in range(1,9)]
    assert expected == actual
    files = [p for p in OUT.rglob('*') if p.is_file() and p.name != 'MANIFEST.json']
    write_json(OUT / 'MANIFEST.json', {'source':{'path':s['source_image'],'sha256':s['source_sha256']},
        'file_count':len(files), 'files':[{'path':str(p.relative_to(OUT)), 'bytes':p.stat().st_size,
             'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sorted(files)]})
    for name in ['DEFAULT_WORDS.json','glyph_occurrences.jsonl','glyph_inventory.json','DEFAULT_visual_labels.txt','DEFAULT_opaque_ids.txt','STRUCTURAL_COUNTS.json','SOURCE_ALTERNATIVES.json','source_occurrence_roundtrip_labels.txt']:
        if sha(OUT/name) != sha(ROOT/'data/source'/name): raise ValueError('Rebuilt transcript differs: '+name)
    print(json.dumps({'status':'PASS_BYTE_IDENTICAL_SOURCE_REBUILD','glyphs':len(glyphs),'classes':len(freq),'red_segments':len(words),
                      'line_lengths':[l['glyph_count'] for l in lines]}))


if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=OUT)
    OUT=parser.parse_args().output
    main()
