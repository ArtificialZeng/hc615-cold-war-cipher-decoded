# An auditable Czech reconstruction of HC Portal cryptogram 615

**Prepared research note — 5 October 2026.** Project contributor label pending individual author metadata. No outside peer review or original answer-sheet confirmation is claimed.

## Abstract

HC Portal 615 catalogues a cryptanalysis-course cryptogram dated approximately 1952, held by the Czech Security Services Archive. A frozen source transcription contains 220 printed glyphs in 22 visual classes, 32 red segments and eight lines. A bounded classical substitution solver, calibrated on six separate Czech development-document controls, recovered a coherent complete Czech message. One fixed 22-class key regenerates every observed glyph and the source layout with zero edits, nulls or positional exceptions. The release provides source coordinates, retained uncertainty, an exact symbolic forward certificate, pinned language statistics, recorded search outputs and portable verification code. The result is complete observed-message recovery; historical typography, four unobserved alphabet signs, global priority and external expert confirmation remain unresolved.

## Source and procedure

The official catalogue gives archive reference **ZSGS, box BF388a, 27-19/6-099**, title “Unsolved cryptogram in 11 210”, approximate date 1952, and solution state “Not solved”. These are catalogue attributions, not a statement that no prior teacher or researcher had an answer. The transcription was frozen before inference and separately reviewed internally. The red divisions were explicitly assumed to represent word boundaries.

Czech joint quadgram statistics were built from one pinned UD_Czech-PDTC training shard. Six development-document windows were enciphered by random bijective substitutions; truth was withheld from the solver. The actual controls recovered 1215/1219 letters and 189/192 words, with mean per-control letter accuracy 99.6708%. This is a matching-task software calibration, not the target's posterior probability.

The target solver used seed 615499 with 16 restarts of 32768 move attempts. The stored bests agreed on the full text and observed 22-entry key. All scores were recomputed independently. An input-parser repair preceded the target run and is preserved as v1p1. No extra target budget, per-position rule, source editing or post-hoc LLM-generated replacement text was used.

## Result

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

The passage concerns Transporta sending nine comrades to a one-year work brigade in the Ostrava region, including members of an organisation's plant-wide committee who volunteered. The final clause requests brigade workers with political-work experience. The complete key and symbol counts appear in [SOLUTION.md](SOLUTION.md).

Forward encoding matches 220/220 occurrences, 32/32 segments and 8/8 lines. This is exact symbolic accounting against frozen visual classes and source coordinates, not recreation of the JPEG pixels. The mechanism is historically ordinary monoalphabetic substitution; the contribution is this transparent reading and its reproducible evidence trail, not a new general cipher-solving algorithm.

## Limitations and review questions

The source is a course exercise rather than a demonstrated secret diplomatic or operational message. Accents, punctuation and capitalisation are editorial. ASCII `chrudimska` permits both the adjectival *Chrudimská Transporta* and a genitive phrase *pracovníky Chrudimska* with different punctuation. Historical `organisace` is kept unchanged. Cipher signs for unused f/q/w/x remain UNKNOWN.

Sixteen matching restart bests do not establish global uniqueness or a calibrated significance level. Internal AI-agent/code audits are not independent outside academic peer review. An original course key, earlier reading or source article has not been found. The priority claim is therefore deliberately limited: a locally checked full observed-message reconstruction of a catalogue record currently labelled unsolved at the recorded access.

External reviewers are invited to challenge glyph distinctions, whole-text Czech coherence, the scope of exactness and earlier-answer provenance. The official coordinator can establish whether a catalogue update is appropriate.

## References and reproducibility

1. Eugen Antal / HC Portal. [“Unsolved cryptogram in 11 210”, record 615](https://api.hcportal.eu/api/cryptograms/615); [original scan](https://api.hcportal.eu/media/1762/14161684790141.jpg). Accessed 2026-10-05. Archival original: Archiv bezpečnostních složek, ZSGS, box BF388a, 27-19/6-099.
2. Archiv bezpečnostních složek. [Fonds guide](https://www.abscr.cz/pruvodce-po-fondech-sbirkach/pruvodce-po-fondech-a-sbirkach-e/). Background for ZSGS; exact exercise dating not independently confirmed here.
3. Universal Dependencies. [UD_Czech-PDTC, pinned commit 6d206ec7…](https://github.com/UniversalDependencies/UD_Czech-PDTC/tree/6d206ec7d337a7f76f34ddfc82893389cabbd76d). PDT-C 2.0 / Charles University provenance and CC BY-NC-SA 4.0 terms in the upstream README.
4. Ústav pro jazyk český. [Slovník spisovného jazyka českého: organizace/organisace](https://ssjc.ujc.cas.cz/search.php?heslo=organizace&hsubstr=no). Post-decoding spelling context.

Run `python3 scripts/verify_solution.py` from the repository root. [METHODS.md](METHODS.md) documents inputs, rebuilding and optional search replay. [PROVENANCE.md](PROVENANCE.md) separates source rights and preserved evidence. [CLAIMS.md](CLAIMS.md) and [PUBLICATION_STATUS.md](PUBLICATION_STATUS.md) define public-facing scope.
