#!/usr/bin/env python3
"""HC615 offline glyph-identity certificate. No solver, network or image decoder.

Offline verifies the frozen manually audited transcript. Strict mode additionally
checks opt-in-fetched original image bytes; neither mode automatically recognizes
historical glyphs from pixels. Archive pixels are not distributed in this repo.
"""
from pathlib import Path
from collections import Counter
import argparse, json, sys
from common import ROOT, sha, load, check_inputs_manifest, read_model, audit_result

def reencrypt(plaintext,observed_key,source,occurrences):
    mapping=observed_key['glyph_to_plaintext_letter']
    observed={g for w in source['words'] for g in w['glyph_ids']}
    if set(mapping)!=observed or observed!=set(f'C{i:03d}' for i in range(1,23)):
        raise ValueError('Key must contain exactly the22 actually observed source glyph IDs')
    letters=list(mapping.values())
    if any(len(c)!=1 or c not in 'abcdefghijklmnopqrstuvwxyz' for c in letters) or len(set(letters))!=22:
        raise ValueError('Observed mapping must be injective lowercase singleletter substitution')
    inverse={p:g for g,p in mapping.items()}
    if any(c not in 'abcdefghijklmnopqrstuvwxyz ' for c in plaintext):
        raise ValueError('ASCII plaintext only; no automatic accent/punctuation restoration')
    if any(c!=' ' and c not in inverse for c in plaintext):
        raise ValueError('Plaintext contains a letter with UNKNOWN, unobserved source glyph')
    plain_words=plaintext.split(' ')
    if any(not w for w in plain_words) or len(plain_words)!=len(source['words']):
        raise ValueError('Must reproduce the32 registered source segments exactly')
    by_id={o['occurrence_id']:o for o in occurrences}
    if len(by_id)!=len(occurrences) or len(occurrences)!=220:
        raise ValueError('Expected220 unique source occurrence records')
    ledger=[];segments=[];used=[];line_counts=Counter();plain_offset=0
    for source_word,plain_word in zip(source['words'],plain_words):
        generated=[inverse[p] for p in plain_word]
        if generated!=source_word['glyph_ids']:
            raise ValueError('Forward encryption differs at '+source_word['segment_id'])
        if len(generated)!=len(source_word['occurrence_ids']):
            raise ValueError('Missing or extra source occurrences')
        line=source_word['line']
        for pos,(p,g,oid,visual) in enumerate(zip(plain_word,generated,source_word['occurrence_ids'],source_word['visual_labels']),1):
            o=by_id[oid]
            if (o['glyph_id'],o['raw_visual_label'],o['line'],o['segment_id'],o['position_in_segment'])!=(g,visual,line,source_word['segment_id'],pos):
                raise ValueError('Occurrence identity/coordinate source disagreement at '+oid)
            line_counts[line]+=1
            if o['position_in_line']!=line_counts[line]:raise ValueError('Original lineorder differs')
            if o['lacuna'] is not False:raise ValueError('Unexpected unaccounted lacuna')
            ledger.append({'occurrence_id':oid,'line':line,'segment_id':source_word['segment_id'],
              'position_in_segment':pos,'position_in_line':o['position_in_line'],'plaintext_offset0':plain_offset+pos-1,
              'plaintext_letter':p,'reencrypted_glyph_id':g,'original_glyph_id':o['glyph_id'],'match':True,
              'raw_visual_label':visual,'source_bbox':o['source_bbox'],'source_center_x':o['source_center_x'],
              'source_image':o['source_image'],'source_sha256':o['source_sha256'],
              'source_font_candidates':o['font_candidates'],'source_uncertainty':o['uncertainty'],
              'source_red_underline_observed':o['red_underline_observed']})
            used.append(oid)
        segments.append({'segment_id':source_word['segment_id'],'line':line,'segment_in_line':source_word['segment_in_line'],
          'plaintext_ascii':plain_word,'reencrypted_glyph_ids':generated,'source_glyph_ids':source_word['glyph_ids'],
          'source_visual_labels':source_word['visual_labels'],'source_bbox':source_word['source_bbox'],
          'red_annotation_bounds_x_approx':source_word['red_annotation_bounds_x_approx'],
          'word_boundary_is_hypothesis':source_word['word_boundary_is_hypothesis'],'match':True})
        plain_offset+=len(plain_word)+1
    if used!=[o['occurrence_id'] for o in occurrences] or used!=[f'O{i:04d}'for i in range(1,221)]:
        raise ValueError('Original occurrenceorder not exactly accounted for')
    lines=[]
    for line in sorted(line_counts):
        sw=[s for s in segments if s['line']==line]
        lines.append({'line':line,'plaintext_ascii':' '.join(s['plaintext_ascii']for s in sw),
          'cipher_glyph_id_segments':[s['reencrypted_glyph_ids']for s in sw],
          'source_visual_label_segments':[s['source_visual_labels']for s in sw],
          'glyphs':line_counts[line],'source_segments':len(sw)})
    return {'version':'HC615_EXACT_FORWARD_CERTIFICATE_v1','mechanism':'One global observed22symbol substitution, source word/line layout retained',
      'plaintext_ascii':plaintext,'glyphs':len(ledger),'segments':len(segments),'lines':len(lines),'all220_source_glyphs_match':True,
      'all32_source_segments_match':True,'all8_source_lines_match':True,'glyph_substitutions_or_deletions':0,
      'nulls':0,'per_position_exceptions':0,'source_alternative_selection':False,
      'unobserved_plaintext_letters':[{'letter':p,'source_glyph':'UNKNOWN'} for p in sorted(set('abcdefghijklmnopqrstuvwxyz')-set(inverse))],
      'pixel_regeneration_claim':False,'accounting_level':'Exact original source glyph identities and occurrencecoordinates, not synthesis of historic inkpixels',
      'line_segments':lines,'segments_with_source':segments,'occurrence_accounting':ledger}

def verify(require_source_image=False, plaintext_path=None, key_path=None):
    manifest_count = check_inputs_manifest()
    pp = Path(plaintext_path) if plaintext_path else ROOT/'data/solution/PLAINTEXT_ASCII.txt'
    kp = Path(key_path) if key_path else ROOT/'data/solution/OBSERVED_GLYPH_KEY.json'
    source = load(ROOT/'data/source/DEFAULT_WORDS.json')
    occurrences = [json.loads(x) for x in (ROOT/'data/source/glyph_occurrences.jsonl').read_text(encoding='utf-8').splitlines()]
    key = load(kp)
    if sha(ROOT/'data/source/DEFAULT_WORDS.json') != key['source_default_words_sha256']:
        raise ValueError('Source/key transcript hash mismatch')
    image_hash = key['source_image_sha256']
    if source['source_sha256'] != image_hash or any(o['source_sha256'] != image_hash for o in occurrences):
        raise ValueError('Mixed original image provenance')
    image_checked = False
    if require_source_image:
        image = ROOT/load(ROOT/'config/sources.json')['resources']['archive_image']['path']
        if not image.is_file():
            raise ValueError('Original image absent. First run: python3 scripts/fetch_sources.py --archive-image')
        if sha(image) != image_hash:
            raise ValueError('Original image SHA-256 mismatch; do not substitute another scan')
        image_checked = True
    text = pp.read_text(encoding='utf-8')
    if text.endswith('\n'): text = text[:-1]
    certificate = reencrypt(text, key, source, occurrences)
    expected = load(ROOT/'data/solution/EXACT_FORWARD_CERTIFICATE.json')
    if certificate != {k:v for k,v in expected.items() if k != 'input_files'}:
        raise ValueError('Generated occurrence certificate differs from frozen mathematical certificate')
    if [line['glyphs'] for line in certificate['line_segments']] != [27,30,32,26,29,32,30,14]:
        raise ValueError('Original eight-line counts differ')
    encoded = []
    for i, word in enumerate(source['words']):
        if i: encoded.append(26)
        encoded.extend(int(g[1:])-1 for g in word['glyph_ids'])
    code = [int(x) for x in (ROOT/'data/solution/INPUT.txt').read_text().split()]
    if code != encoded or len(code) != 251:
        raise ValueError('Registered solver input differs from source-only glyph encoding')
    model = read_model()
    target = load(ROOT/'data/results/target/target_result.json')
    checked_trials = audit_result(target, code, model)
    if target['plain'] != text:
        raise ValueError('Saved target candidate differs from published plaintext')
    expected_key = [ord(key['glyph_to_plaintext_letter']['C%03d'%i])-97 for i in range(1,23)]
    if any(trial['key'][:22] != expected_key for trial in target['trials']):
        raise ValueError('Observed mapping differs among archived target trials')
    control_report = load(ROOT/'data/results/controls/EVALUATION.json')
    controls = []
    for i in range(6):
        cid = 'C%02d'%i
        ci = [int(x) for x in (ROOT/('data/controls/'+cid+'_input.txt')).read_text().split()]
        result = load(ROOT/('data/results/controls/'+cid+'_result.json'))
        audit_result(result, ci, model)
        truth = load(ROOT/('data/controls/'+cid+'_truth.json'))
        letters = sum(c!=' ' for c in truth['plain'])
        correct = sum(a==b for a,b in zip(result['plain'],truth['plain']) if b!=' ')
        exact_words = sum(a==b for a,b in zip(result['plain'].split(),truth['plain'].split()))
        recorded = control_report['controls'][i]
        if len(result['plain']) != len(truth['plain']) or (letters,correct,exact_words) != (recorded['letters'],recorded['correct_letters'],recorded['correct_words']):
            raise ValueError('Saved control metrics differ from explicit truth: '+cid)
        controls.append({'id':cid,'letters':letters,'correct_letters':correct,'exact_words':exact_words})
    certificate['input_files'] = [{'path':str(p.relative_to(ROOT)) if p.is_relative_to(ROOT) else p.name,'sha256':sha(p)} for p in [pp,kp,ROOT/'data/source/DEFAULT_WORDS.json',ROOT/'data/source/glyph_occurrences.jsonl']]
    summary = {'status':'PASS','verification_level':'original image hash plus frozen glyph transcript' if image_checked else 'frozen manually audited glyph transcript (offline)',
        'glyphs':220,'source_segments':32,'source_lines':8,'observed_key_entries':22,'unknown_historical_symbols':['f','q','w','x'],
        'all220_source_glyphs_match':True,'all32_source_segments_match':True,'all8_source_lines_match':True,
        'source_image_sha256_checked':image_checked,'source_edits':0,'nulls':0,'positional_exceptions':0,
        'input_manifest_files_checked':manifest_count,'archived_target_trials_checked':checked_trials,'archived_control_trials_checked':96,
        'control_correct_letters':sum(x['correct_letters'] for x in controls),'control_total_letters':sum(x['letters'] for x in controls),
        'control_exact_words':sum(x['exact_words'] for x in controls),'control_total_words':192,
        'no_optimizer_or_network_run':True,'pixel_recognition_or_regeneration_claim':False,'global_priority_or_uniqueness_proven':False}
    return summary, certificate

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--require-source-image',action='store_true')
    ap.add_argument('--plaintext',type=Path,help='Optional explicit candidate for falsification; stored source still locked')
    ap.add_argument('--key',type=Path,help='Optional explicit observed key for falsification; source still locked')
    ap.add_argument('--output',type=Path,help='Optional new full certificate path; never overwrites')
    args=ap.parse_args()
    try:
        summary,certificate=verify(args.require_source_image,args.plaintext,args.key)
        if args.output:
            args.output.parent.mkdir(parents=True,exist_ok=True)
            with args.output.open('x',encoding='utf-8') as f:
                json.dump(certificate,f,ensure_ascii=False,indent=2);f.write('\n')
        print(json.dumps(summary,indent=2))
    except (ValueError,OSError,KeyError) as exc:
        print('Verification FAILED: '+str(exc),file=sys.stderr);return 1
    return 0
if __name__=='__main__':sys.exit(main())
