# HC615

## A Cold War-era cipher. 220 symbols. One reproducible reading.

![HC615: 220 symbols, 22 glyph classes, one fixed substitution, and a complete Czech reading](assets/hero.svg)

**English** · [简体中文](README.zh-CN.md) · [Čeština](README.cs.md) · [日本語](README.ja.md)

**Author:** Zijian Zeng, PhD · **Repository:** [hc615-cold-war-cipher-decoded](https://github.com/ArtificialZeng/hc615-cold-war-cipher-decoded) · **Release:** v1.0.2

An archival cryptogram catalogued **“Not solved”** now has a complete, auditable Czech reconstruction: **one fixed substitution explains all 220 observed symbols, with zero edits, nulls, or positional exceptions.** This repository lets you check that result yourself.

**220 symbols · 22 distinct glyph classes · 32 source segments · 8 lines · 0 mismatches**

The source is a **cryptanalysis-course exercise, dated circa 1952 in the HC Portal catalogue**, held by the Czech *Archiv bezpečnostních složek*. Its full reading concerns workers being sent to the Ostrava region; Transporta sent nine comrades on a one-year work brigade. Every letter of the recovered message participates in the same reversible key.

**Status, prepared 2026-10-05:** complete observed-message recovery and local verification passed. The public catalogue was still marked “Not solved” at our last access. External expert confirmation and comparison with an original course answer sheet remain pending. No claim of worldwide priority is made. [Read the exact claim boundaries](docs/CLAIMS.md).

## Verify it in seconds

With Python 3.9 or newer, from this repository's root:

```sh
python3 scripts/verify_solution.py
```

This offline, standard-library check compares the plaintext, the 22-entry key, and the archived glyph transcription; checks the stored hashes and search outputs; and accounts for **220/220 symbols, 32/32 segments, and 8/8 lines**. It uses the included Czech statistical cache to recheck saved scores. No external AI service, new model training, or new search is needed.

To obtain the original source image and additionally require its recorded SHA-256:

```sh
python3 scripts/fetch_sources.py --archive-image
python3 scripts/verify_solution.py --require-source-image
```

The scan is downloaded to an ignored cache. A matching file hash establishes the image's identity; human inspection is still needed to check the transcription's glyph distinctions. Archival image redistribution rights have not been established, so the source pixels are obtained from the original provider rather than bundled here.

## The complete reading

The following is the **unchanged solver output**, arranged in the source's eight lines. Accents, capitals, and punctuation are not recovered source typography.

```text
vysilaji na ostravsko nejlepsi
pracovniky chrudimska transporta
vyslala devet soudruhu na jednorocni
brigadu jsou mezi nimi clenove
celozavodniho vyboru organisace
sami se prihlasili ostrava potrebuje
brigadniky kteri maji zkusenosti z
politicke prace
```

In English: the message describes sending excellent workers to the Ostrava region. Transporta sent nine comrades on a one-year brigade, including members of an organisation's plant-wide committee. They volunteered. Ostrava needed brigade workers with experience in political work.

ASCII `chrudimska` permits two editorial readings: **Chrudimská Transporta**, describing the company, or **pracovníky Chrudimska**, describing workers from the Chrudim region before a sentence break. The cipher letters do not distinguish those accents or punctuation. The historical spelling **`organisace`** is retained.

Read the [exact plaintext](data/solution/PLAINTEXT_ASCII.txt), [observed key](data/solution/OBSERVED_GLYPH_KEY.json), and [provenance record](docs/PROVENANCE.md).

## How the result was obtained

1. **Freeze the evidence.** Transcribe the original image before language inference, preserve look-alike symbols as separate classes, and record each occurrence's source coordinates. Treat the red divisions as an explicit word-boundary hypothesis.
2. **Calibrate the solver.** Six matched Czech synthetic substitution controls, with answer keys hidden during inference, achieved **99.6708% mean letter recovery**. This measures software performance on those controls, not the target's probability of being correct.
3. **Run one registered target attack.** A classical bijective-substitution solver used a pinned Czech quadgram model, seed **615499**, and **16 × 32768** move attempts. All 16 stored restarts yielded the same whole text and the same mapping on the 22 observed classes.
4. **Try to falsify the answer.** Separate AI-agent and code audits checked the source, full Czech reading, input integrity, every saved target score, and all 220 forward-encoded symbols. No outside academic endorsement is implied by those checks.

No plaintext was manufactured by an LLM and substituted for the solver's output. The mechanism is classical monoalphabetic substitution; the contribution is a transparent recovery and reproducible evidence package. [Methods, configuration, controls, and limits](docs/METHODS.md).

Optional full search reproduction requires a C++17 compiler:

```sh
python3 scripts/reproduce.py --controls
python3 scripts/reproduce.py --target
python3 -m unittest discover -s tests -v
```

The registered seeds and budgets are preserved. Compiler and C++ standard-library differences can affect random-search trajectories; byte-identical optimiser output across platforms is not promised. The fixed-key offline verifier does not depend on that search.

## Original source and independent review

- [HC Portal record 615](https://api.hcportal.eu/api/cryptograms/615), titled **“Unsolved cryptogram in 11 210”**.
- [Original scan](https://api.hcportal.eu/media/1762/14161684790141.jpg).
- Archive reference supplied by the catalogue: **Archiv bezpečnostních složek · ZSGS · box BF388a · 27-19/6-099**.
- [HC Portal coordinators and relevant experts, with public contact sources](docs/EXPERT_CONTACTS.md).

The observed message is fully accounted for. The historical cipher signs for unused **f, q, w, x** remain **UNKNOWN**. Accents, punctuation, the original article source, sender, recipient, and original course key have not been independently recovered. Sixteen agreeing restarts do not prove mathematical uniqueness or global first discovery.

For a reviewer, the decisive question is simple: **does this one fixed key explain the complete source, and does the resulting whole Czech text make sense?** The repository preserves the evidence needed to challenge both parts.

## Reuse and citation

Code, project-authored narrative, and third-party linguistic data have distinct licences; see [provenance and attribution](docs/PROVENANCE.md). The included Czech model and optional upstream corpus retain **CC BY-NC-SA 4.0** conditions. The source scan and upstream corpus downloads are kept outside versioned files.

Use [CITATION.cff](CITATION.cff) when citing this release. For public descriptions, use the checked language in [CLAIMS.md](docs/CLAIMS.md) and the actual publication state in [PUBLICATION_STATUS.md](docs/PUBLICATION_STATUS.md).

**Read it. Re-encode it. Check every symbol.**

## Illustrated press kit

The [Chinese technology feature in Word](press/HC615_冷战档案密码_科技报道图文稿.docx) includes five original figures and the full reading. [Four-language press drafts and social copy](press/README.md) are ready for review; external expert confirmation remains pending.
