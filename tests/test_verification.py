"""Falsification regressions: source/key tampering, unknown letters, strict input."""
from pathlib import Path
import copy
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
import common
from verify_solution import reencrypt, verify

class ForwardVerificationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.plain = (ROOT/'data/solution/PLAINTEXT_ASCII.txt').read_text(encoding='utf-8').rstrip('\n')
        cls.key = common.load(ROOT/'data/solution/OBSERVED_GLYPH_KEY.json')
        cls.source = common.load(ROOT/'data/source/DEFAULT_WORDS.json')
        cls.occurrences = [json.loads(x) for x in (ROOT/'data/source/glyph_occurrences.jsonl').read_text(encoding='utf-8').splitlines()]

    def test_complete_certificate_and_saved_search_arithmetic(self):
        summary, certificate = verify()
        self.assertEqual((summary['glyphs'],summary['source_segments'],summary['source_lines']),(220,32,8))
        self.assertEqual(summary['archived_control_trials_checked'],96)
        self.assertEqual(summary['archived_target_trials_checked'],16)
        self.assertEqual((summary['control_correct_letters'],summary['control_total_letters']),(1215,1219))
        self.assertEqual((summary['control_exact_words'],summary['control_total_words']),(189,192))
        self.assertFalse(summary['source_image_sha256_checked'])
        self.assertEqual([x['letter'] for x in certificate['unobserved_plaintext_letters']],['f','q','w','x'])

    def test_one_wrong_letter_rejected(self):
        altered = 'a'+self.plain[1:]
        with self.assertRaisesRegex(ValueError,'Forward encryption differs'):
            reencrypt(altered,self.key,self.source,self.occurrences)

    def test_unobserved_letter_cannot_invent_historical_glyph(self):
        with self.assertRaisesRegex(ValueError,'UNKNOWN'):
            reencrypt('f'+self.plain[1:],self.key,self.source,self.occurrences)

    def test_linguistic_restoration_not_silently_encoded(self):
        with self.assertRaisesRegex(ValueError,'ASCII plaintext only'):
            reencrypt('výsilají'+self.plain[8:],self.key,self.source,self.occurrences)

    def test_invented_23rd_glyph_rejected(self):
        key = copy.deepcopy(self.key); key['glyph_to_plaintext_letter']['C023'] = 'f'
        with self.assertRaisesRegex(ValueError,'exactly the22'):
            reencrypt(self.plain,key,self.source,self.occurrences)

    def test_noninjective_key_rejected(self):
        key = copy.deepcopy(self.key); key['glyph_to_plaintext_letter']['C001'] = key['glyph_to_plaintext_letter']['C002']
        with self.assertRaisesRegex(ValueError,'injective'):
            reencrypt(self.plain,key,self.source,self.occurrences)

    def test_changed_source_occurrence_identity_rejected(self):
        occurrences = copy.deepcopy(self.occurrences); occurrences[0]['glyph_id'] = 'C001'
        with self.assertRaisesRegex(ValueError,'Occurrence identity'):
            reencrypt(self.plain,self.key,self.source,occurrences)

    def test_deleted_source_occurrence_rejected(self):
        with self.assertRaisesRegex(ValueError,'220 unique'):
            reencrypt(self.plain,self.key,self.source,self.occurrences[:-1])

    def test_added_segment_boundary_rejected(self):
        with self.assertRaisesRegex(ValueError,'32 registered'):
            reencrypt(self.plain.replace('vysilaji','vysi laji',1),self.key,self.source,self.occurrences)

    def test_frozen_source_file_hash_tampering_detected(self):
        with tempfile.TemporaryDirectory() as temporary:
            copied = Path(temporary)/'repo'
            shutil.copytree(ROOT,copied,ignore=shutil.ignore_patterns('build','upstream_cache','__pycache__','.git'))
            source = copied/'data/source/DEFAULT_WORDS.json'
            source.write_bytes(source.read_bytes()+b' ')
            with patch.object(common,'ROOT',copied):
                with self.assertRaisesRegex(ValueError,'Frozen engineering input hash mismatch'):
                    common.check_inputs_manifest()

    def test_strict_mode_requires_exact_source_image_not_network_fallback(self):
        image = ROOT/common.load(ROOT/'config/sources.json')['resources']['archive_image']['path']
        if image.exists():
            self.assertTrue(verify(require_source_image=True)[0]['source_image_sha256_checked'])
        else:
            with self.assertRaisesRegex(ValueError,'Original image absent'):
                verify(require_source_image=True)

class StrictCppInputRegressionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        compiler = shutil.which('clang++') or shutil.which('g++')
        if compiler is None: raise unittest.SkipTest('No C++17 compiler; offline forward checks still run')
        if sys.byteorder != 'little': raise unittest.SkipTest('Historical C++ reader requires little endian')
        cls.temporary = tempfile.TemporaryDirectory()
        cls.directory = Path(cls.temporary.name)
        cls.binary = cls.directory/('strict_solver.exe' if sys.platform == 'win32' else 'strict_solver')
        subprocess.run([compiler,'-O1','-std=c++17',str(ROOT/'src/mono_substitution_sa_v1p1.cpp'),'-o',str(cls.binary)],check=True,capture_output=True,text=True)

    @classmethod
    def tearDownClass(cls):
        if hasattr(cls,'temporary'): cls.temporary.cleanup()

    def run_toy(self,name,text):
        input_path = self.directory/(name+'.txt'); result_path = self.directory/(name+'.json')
        input_path.write_text(text,encoding='utf-8')
        command = [str(self.binary),str(ROOT/'data/model/quadgram27.bin'),str(input_path),str(ROOT/'data/model/frequency_order.txt'),'1','1','1',str(result_path)]
        return subprocess.run(command,capture_output=True,text=True),result_path

    def test_tiny_valid_input_is_accepted(self):
        completed,path = self.run_toy('valid','0 1 2 3 26\n')
        self.assertEqual(completed.returncode,0,completed.stderr)
        result = common.load(path)
        self.assertEqual(result['seed'],1)
        self.assertEqual(len(result['plain']),5)
        self.assertEqual(sorted(result['key']),list(range(26)))

    def test_malformed_input_is_rejected_without_partial_cipher_output(self):
        cases = {'middle':'0 1 nonsense 2 3\n','trailing':'0 1 2 3 junk\n','fraction':'0 1 2 3.0\n','range':'0 1 2 27\n','short':'0 1 2\n'}
        for name,text in cases.items():
            with self.subTest(name=name):
                completed,path = self.run_toy(name,text)
                self.assertNotEqual(completed.returncode,0)
                self.assertFalse(path.exists(),'Malformed input must not be silently truncated to a valid prefix')

if __name__ == '__main__': unittest.main()
