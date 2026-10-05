# Methods and reproduction

## Evidence before inference

The target was HC Portal 615 only. The immutable 960 × 601 source image was transcribed into occurrence-bearing rows before target language inference. Two separate AI-agent observers reviewed the source; these were internal audits, not outside academic reviewers. Each occurrence retains a glyph ID, visual mnemonic, line, segment, position, bounding box and image hash.

There are 220 printed slots, 22 visual classes, 32 red segments, and eight line lengths **27, 30, 32, 26, 29, 32, 30, 14**. The handwritten “220” was not used as a count input. All nine question-mark-like signs are printed cipher symbols, not missing-text markers. The single/double horizontal signs, low/raised marks and serif numeral/narrow stem remain distinct.

Treating red divisions as plaintext word boundaries was a declared model assumption. The source also preserves an annotations-only interpretation; no segmentation alternative was selected to improve fluency. The resulting reading accounts for the fixed 32 segment lengths.

## Czech statistical cache

The training material was `cs_pdtc-ud-train-la.conllu` from Universal Dependencies **UD_Czech-PDTC**, pinned to commit `6d206ec7d337a7f76f34ddfc82893389cabbd76d`. Only that shard was used for training, not the entire treebank. The separate development file supplied synthetic controls.

Sentence text is lowercased, NFKD-decomposed, stripped of combining accents and tokenised with `[a-z]+`. There is no j/i or u/v merge. Training contains **182,808 words in 950 documents**; development contains **316,222 words in 1,006 documents**. The 27-character alphabet is `abcdefghijklmnopqrstuvwxyz `, including space. Sentence boundaries receive a space for training.

A 27⁴ table stores little-endian IEEE-754 float32 values of the smoothed joint quadgram natural logarithm, with additive smoothing **0.05**. Scores sum overlapping four-character windows. This is an optimisation heuristic, not a posterior probability or calibrated confidence. The cache hash is `8aa157cf337f4a12eb5216999105ae8e7eaec20f2a655314f2ae0e6efadfa8fd`.

The included word counts are an audit resource. The original inference objective used quadgrams rather than LLM-written text. Derived language files and control plaintext retain upstream **CC BY-NC-SA 4.0** conditions; see [provenance](PROVENANCE.md).

## Six actual controls

Six 32-word development windows from separate documents were selected by fixed rules, with 195–250 letters and 20–24 observed classes. A complete window already present in training was excluded. Their substitution generation seeds were 615310–615315; inference seeds were 615410–615415. Answers were not passed to the solver process. Truth was read after inference.

| Control | Letters recovered | Letter accuracy | Exact words |
|---|---:|---:|---:|
| C00 | 199 / 202 | 98.5149% | 30 / 32 |
| C01 | 212 / 212 | 100% | 32 / 32 |
| C02 | 197 / 197 | 100% | 32 / 32 |
| C03 | 209 / 209 | 100% | 32 / 32 |
| C04 | 203 / 204 | 99.5098% | 31 / 32 |
| C05 | 195 / 195 | 100% | 32 / 32 |

Mean per-control letter accuracy was **99.6708%**; pooled recovery was **1215/1219 letters** and **189/192 words**. The registered gate required mean ≥95% and at least five of six ≥90%; all six cleared 90%. Errors are preserved in the released predictions, not repaired. These figures describe six matching synthetic tasks, not historical target certainty or performance across all cipher families.

The older prepared control set in the private research history was not an additional completed inference experiment. The public package includes only the six actual runs used for this gate.

## Bounded target search

The C++17 solver performs a fixed 26-slot bijective substitution search with pair swaps and a simulated-annealing schedule. Space uses a fixed index 26. Target opaque slots use only indices 0–21; unused slots 22–25 remain arbitrary. The registered target seed was **615499**, with **16 restarts × 32768 move attempts** (nominal cap 524,288). Temperature began at 6.0 with a 0.05 end floor; the exact schedule and move handling are in the source. No key/truth/reading/source title is supplied to the C++ process.

The target input has **251 positions**, including 31 fixed spaces, and 248 scored quadgram windows. The saved best score is **−2300.7876777648926**. All sixteen restart bests agree on the complete text and observed 22-class key. Their twelve distinct 26-slot keys differ only in unobserved completions. All 24 permutations of the remaining f/q/w/x values have the same target score. This is finite convergence; it proves neither global uniqueness nor statistical significance.

Configuration and budget were saved before the target run in local research history. This local ordering is not an externally timestamped preregistration. The release does not claim an independent registry or cryptographically trusted clock.

An independent parser audit found that the original v1 C++ input reader could silently stop at a nonnumeric token. Before the actual target run, v1p1 changed parsing to reject malformed tokens in full. Both historical source files are retained. The patch preserves the result on valid historical input. The target used v1p1; the six controls used valid v1 inputs. Meaningful regressions check malformed interior/trailing/fractional tokens, invalid ranges and short input.

## Verification, confidence and limits

The fixed key decrypts every occurrence consistently. Re-encryption preserves **220/220 glyphs, 32/32 red segments, 8/8 lines**, with zero edits, nulls, transpositions or positional exceptions. This combines exact structural accounting with a coherent complete Czech text. A reversible key alone would not establish a historical answer; the whole-language review and unresolved historical questions are stated separately.

The final source, language and claim reviews were performed by separate AI agents and code, not external cryptologists or native-speaking academic referees. The full candidate was not present verbatim in the pinned train/dev files; the longest shared word sequence was the ordinary three-word phrase `jsou mezi nimi`. This check does not prove absence from all model pretraining or the wider web.

Accents, capitals and punctuation are editorial. `chrudimska` has two readings described in [SOLUTION.md](SOLUTION.md). The full historical alphabet, original answer sheet, original news article, sender/recipient and global discovery priority remain unresolved.

## Run levels

All commands start from the repository root and require **Python 3.9+**. Verification uses only its standard library and included files; no external AI service, new training or new search is needed. It does load the included statistical cache to independently rescore the saved 16 target and 96 control trials.

```sh
# Offline symbolic proof, frozen hashes and archived-score replay
python3 scripts/verify_solution.py
# Optional original image identity check; human visual inspection remains necessary
python3 scripts/fetch_sources.py --archive-image
python3 scripts/verify_solution.py --require-source-image
# Meaningful tampering checks and strict C++ parser regressions
python3 -m unittest discover -s tests -v
```

Rebuild the frozen source rows from the pre-inference visual specification and hash-matched scan:

```sh
python3 scripts/rebuild_source_transcription.py
```

This reproduces manual observations mechanically; it is not OCR. It compares the rebuilt files with the recorded transcript and writes into a new ignored `build/` directory.

To rebuild the language cache and deterministic control inputs:

```sh
python3 scripts/fetch_sources.py --language-corpus
python3 scripts/build_language_model.py
python3 scripts/rebuild_controls.py
```

Optional replay of the registered searches requires a C++17 compiler on a little-endian platform:

```sh
python3 scripts/reproduce.py --controls
python3 scripts/reproduce.py --target
```

No answer file is passed to inference. Comparisons are made only after each process completes. Outputs go to a new ignored directory and do not alter recorded evidence. Different compiler/STL implementations of shuffling and random distributions may change the search trajectory even with the same seed; byte-identical stochastic search is not promised. The fixed-key certificate is independent of those trajectories. GitHub Actions is configured for three operating systems and two Python versions; remote CI has not yet been run.

The release includes source, inputs, saved trial results, model cache, controls, tests, provenance and internal audit projections. Source image pixels and raw training text are fetched from their original providers rather than mirrored here. See [publication status](PUBLICATION_STATUS.md).
