# HC615: complete observed-message reconstruction

One fixed monoalphabetic substitution accounts for all **220 printed cipher glyphs**, **32 red segments**, and **8 source lines**, without changing the frozen source or adding exceptions. This is the local complete-message result. External historical-cryptology review and comparison with an original course answer remain pending.

## Exact ASCII output

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

This is the unchanged solver output in the original line layout. Its 220 letters contain no recovered accents, punctuation or capitalisation. The machine-readable [plaintext](../data/solution/PLAINTEXT_ASCII.txt), [key](../data/solution/OBSERVED_GLYPH_KEY.json), [source transcript](../data/source/DEFAULT_WORDS.json), and [forward certificate](../data/solution/EXACT_FORWARD_CERTIFICATE.json) are included.

## The complete observed key

Visual labels are transcription mnemonics, not exact font identifications. The distinct low/raised marks, single/double horizontal marks, and serif numeral/narrow stem are retained. Inspect their occurrence coordinates against the [original image](https://api.hcportal.eu/media/1762/14161684790141.jpg).

| Opaque glyph ID | Visual mnemonic | ASCII plaintext letter | Observed occurrences |
|---|---|---|---:|
| C001 | `0` | **g** | 3 |
| C002 | `1` | **z** | 4 |
| C003 | `2` | **j** | 6 |
| C004 | `3` | **u** | 9 |
| C005 | `4` | **i** | 23 |
| C006 | `5` | **d** | 7 |
| C007 | `6` | **o** | 18 |
| C008 | `7` | **a** | 21 |
| C009 | `8` | **l** | 9 |
| C010 | `X` | **t** | 9 |
| C011 | `QMARK` | **v** | 9 |
| C012 | `POUND` | **y** | 5 |
| C013 | `ORNATE` | **c** | 8 |
| C014 | `SECTION` | **h** | 4 |
| C015 | `H1` | **s** | 16 |
| C016 | `H2` | **e** | 17 |
| C017 | `SLASH` | **r** | 16 |
| C018 | `PERCENT` | **n** | 13 |
| C019 | `PLUS` | **m** | 5 |
| C020 | `LOWDOT` | **k** | 7 |
| C021 | `UPPER` | **b** | 4 |
| C022 | `VSTEM` | **p** | 7 |

The counts sum to 220. Historical cipher signs for **f, q, w, x are UNKNOWN** because those letters do not occur. The solver's four unused completion slots do not establish any additional historical signs.

## Editorial reading and meaning

One possible accent and punctuation restoration is:

> Vysílají na Ostravsko nejlepší pracovníky. Chrudimská Transporta vyslala devět soudruhů na jednoroční brigádu. Jsou mezi nimi členové celozávodního výboru organisace. Sami se přihlásili. Ostrava potřebuje brigádníky, kteří mají zkušenosti z politické práce.

This is a modern reading layer, not a claim about original typography. ASCII `chrudimska` also allows **pracovníky Chrudimska. Transporta…**, referring to workers of the Chrudim region before a sentence break. Both interpretations retain exactly the same decoded letters. The spelling `organisace` is preserved; changing it to modern `organizace` would change a cipher letter.

In English: the passage describes sending excellent workers to the Ostrava region. Transporta sent nine comrades on a one-year work brigade. Members of an organisation's plant-wide committee were among them. They volunteered. Ostrava needed brigade workers with experience in political work. The organisation is not identified as a specific party or trade union.

中文释义：他们把最优秀的工作人员派往俄斯特拉发地区。Transporta 派出九位同志，参加为期一年的劳动支援。其中有该组织全厂委员会的成员，他们主动报名。俄斯特拉发需要具有政治工作经验的劳动支援人员。`chrudimska` 的断句与重音有两种解释，不能由密文本身唯一确定。

## Forward check

```sh
python3 scripts/verify_solution.py
python3 scripts/fetch_sources.py --archive-image
python3 scripts/verify_solution.py --require-source-image
```

The first command checks the included evidence offline. The last additionally checks the downloaded scan's SHA-256. Both regenerate symbolic glyph IDs and source layout, not JPEG pixels or printer fonts. A scan hash verifies file identity; checking the visual transcription still requires human inspection.

See [methods](METHODS.md), [claim boundaries](CLAIMS.md), [source provenance](PROVENANCE.md), and [review status](PUBLICATION_STATUS.md).
