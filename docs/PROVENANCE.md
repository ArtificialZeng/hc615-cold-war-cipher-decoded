# Sources, hashes, attribution and licensing

## Original archival record

- Human-facing record: [HC Portal 615](https://crypto.hcportal.eu/dashboard/cryptograms/615).
- Official metadata: [record 615 API](https://api.hcportal.eu/api/cryptograms/615), title **“Unsolved cryptogram in 11 210”**; creator Eugen Antal; solution “Not solved”, language “Unknown”, no key or plaintext attached in the 2026-10-05 snapshot.
- Original scan: [image 1385](https://api.hcportal.eu/media/1762/14161684790141.jpg), 161,668 bytes, SHA-256 `712891e2f5019509798a750d4a92318910333b623ee583ae39ea5d86a7b1d4e6`.
- Catalogue source citation: **Archiv bezpečnostních složek (Security Services Archive), ZSGS, box BF388a, 27-19/6-099**, cryptanalysis-course material dated approximately 1952. Exact dating and shelfmark are attributed to HC Portal; not independently confirmed against an archival answer sheet.

The [official ABS fonds guide](https://www.abscr.cz/pruvodce-po-fondech-sbirkach/pruvodce-po-fondech-a-sbirkach-e/) explains the Zpravodajská správa Generálního štábu fonds. Its [268-page inventory](https://www.abscr.cz/data/pdf/inventar/fond-bf-zsgs.pdf) gives broader context. A bounded text search did not independently identify this exact shelfmark. These sources support the archival background, not proof of the exercise's specific date or prior solution status.

Minimum source citation: **Eugen Antal / HC Portal: “Unsolved cryptogram in 11 210”, record 615; archival original: Archiv bezpečnostních složek, ZSGS, box BF388a, 27-19/6-099.** Link both the record and original scan. Eugen Antal is the catalogue creator/coordinator, not asserted to be the 1952 author.

HC Portal's [terms and copyrights](https://hcportal.eu/terms.html), checked 2026-10-05, permit cited academic noncommercial teaching/presentation/publication use but restrict mirroring/transfer. The portal says ABS images are used with permission. It does not establish blanket public-domain or MIT rights for this scan. **No source image or crop pixels are bundled with this public repository.** `fetch_sources.py --archive-image` downloads the original into an ignored cache and checks its recorded hash. This is an acquisition option, not a grant of redistribution rights.

## Transcription and derived result

The manual pre-inference visual specification and occurrence-bearing rows preserve source coordinates and uncertainty. `DEFAULT_WORDS.json` hash: `a722fbac91cf338dc016d597799fe1f6387b9e1dd4ae79e191acb74590b22b23`. The raw scan identity, 22 classes and 220 occurrence IDs are explicit. See [source data](../data/source/DEFAULT_WORDS.json) and [solution key](../data/solution/OBSERVED_GLYPH_KEY.json).

Final original target result hash: `21e6c4c920438c102e1f45bb029d945d312b97bdc73cd3a24cd5921e7f62266a`. The original candidate-stage `cipher_solved=false` remains in that historical file; it was written before the final combined audits. The final local status is complete observed-message recovery. The earlier file is not rewritten to backdate the verdict.

[Evidence index](../evidence/ORIGINAL_EVIDENCE_INDEX.json) records original hashes separately from public projection hashes. Internal reports retain their chronological verdicts; some earlier reviews say “pending” because later checks had not happened. Public projections remove private absolute paths and explanatory image embeds whose pixels are excluded. They are explicitly not byte-identical originals. Core transcript/key/model/solver/result files preserve original bytes and are checked by `config/engineering_inputs_manifest.json`.

## Language data

Upstream: [Universal Dependencies, UD_Czech-PDTC](https://github.com/UniversalDependencies/UD_Czech-PDTC), pinned commit [6d206ec…](https://github.com/UniversalDependencies/UD_Czech-PDTC/tree/6d206ec7d337a7f76f34ddfc82893389cabbd76d). The Czech treebank is derived from **Prague Dependency Treebank – Consolidated 2.0 (PDT-C 2.0), Charles University / Institute of Formal and Applied Linguistics**. The upstream README credits conversion to Universal Dependencies by **Daniel Zeman** and documents the original creators and citation.

Relevant dataset: *Prague Dependency Treebank – Consolidated 2.0*, LINDAT/CLARIAH-CZ, [persistent dataset handle](http://hdl.handle.net/11234/1-5813). Use the full upstream README for authorship and component provenance; the release does not replace that attribution with its own ownership claim.

Train shard: 24,175,776 bytes, SHA-256 `b2683cba24c059d30505dc5678d20581ff0bf1d4b73508b1b33e163c6812a2f7`. Dev: 50,117,913 bytes, SHA-256 `73a19117ff39411b1134840c3a0383a37f5dd89a2e07b3f8c0a8821d8d37d4bc`. All acquisition URLs and checksums are pinned in [sources.json](../config/sources.json).

The included quadgram cache, word counts, frequency ranking, and control plaintext/ciphertext/results derived from upstream text retain **Creative Commons Attribution–NonCommercial–ShareAlike 4.0**. Raw train/dev text is not included; it can be fetched explicitly. Upstream README and license notices are in [LICENSES/UD_CZECH_PDTC_README.md](../LICENSES/UD_CZECH_PDTC_README.md) and [UPSTREAM_LICENSE.txt](../data/model/UPSTREAM_LICENSE.txt). Licence: [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/), [legal code](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode).

## Lexical checks

The Czech Language Institute's scholarly dictionary provides context for historical spelling and vocabulary: [organizace/organisace](https://ssjc.ujc.cas.cz/search.php?heslo=organizace&hsubstr=no), [brigáda](https://ssjc.ujc.cas.cz/search.php?heslo=brig%C3%A1da&hsubstr=no), [celozávodní](https://ssjc.ujc.cas.cz/search.php?heslo=celoz%C3%A1vodn%C3%AD&hsubstr=no). These are post-decoding lexical checks; not independent confirmation of the exact original passage.

## Scope of project licences

| Material | Licence / status |
|---|---|
| Project-authored Python/C++ code, tests and automation | MIT; see [LICENSES/MIT.txt](../LICENSES/MIT.txt). |
| Project-authored explanatory prose, original SVG artwork and original research annotations | CC BY 4.0; underlying archive text/image and third-party sources are excluded from this grant. |
| Czech language model, frequency/word statistics and corpus-derived controls/results | CC BY-NC-SA 4.0 with the upstream attribution above. |
| Recovered historical text and archival scan | Original-source status; no new blanket ownership/licensing claim. Scan pixels excluded. |
| Linked external websites, staff contacts and research papers | Their original terms; links do not imply endorsement. |

This is a mixed-licence research package, not an entirely MIT dataset. [Root licensing notice](../LICENSE) gives the same boundaries. The release does not modify upstream licence conditions.
