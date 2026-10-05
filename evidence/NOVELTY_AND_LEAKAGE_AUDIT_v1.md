# Public projection of NOVELTY_AND_LEAKAGE_AUDIT_v1.md

Internal AI-agent/code record, not outside peer review. This labelled projection redacts private paths and excludes source-image pixels. Earlier pending verdicts are preserved. Original hashes are in ORIGINAL_EVIDENCE_INDEX.json; historic paths need not exist in this public layout.

---

# HC615 bounded novelty / supplied-answer audit v1

**No supplied full answer or complete train/dev plaintext match was detected in
the audited inputs.** The defensible novelty statement is that this project
reconstructed a complete candidate from a public catalogue item currently
labelled Not solved. This audit cannot establish the first-ever reading, exclude
private prior decipherments, or identify the original article/edition from which
this cryptanalysis-course exercise may have been taken. It is separate from the
root's cryptanalytic solution and exact-regeneration verification gates.

The audited candidate is the32-word/220-letter ASCII stream in
`experiments/czech_bijective_target_v1p1/target_result.json`. No candidate was
generated or fitted here. This review reads the frozen candidate, source and
pinned licensed corpora only; it runs no solver, new language training, key
optimization or target-dependent word insertion.

The [official615 API](https://api.hcportal.eu/api/cryptograms/615) was anonymously
re-read on2026-10-05. It returned HTTP200 and exactly the same1,623 bytes as the
initial retained record, SHA-256
`f4373a538729747fe6593f47e5c6bf72911afec66d0c4d6ce90dddb2b1747f57`.
It explicitly labels language/category/sender/recipient Unknown and solution
Not solved, has`cipher_key_id=null`, and contains only one image item in its
datagroups. Its description merely calls the item an unsolved cryptogram; no
plaintext, cipher alphabet or worked solution is attached to this record.
The actual original image was inspected during this agent's independent
source transcription: eight printed cipher lines with red divisions and pen
annotations, with no visible plaintext or key table. Source hash remains
`712891e2f5019509798a750d4a92318910333b623ee583ae39ea5d86a7b1d4e6`.
This finding concerns the public record/image actually supplied, not all possible
archive holdings, hidden/private attachments or historical course answer sheets.

Both actual pinned UD corpus files were hash-verified against the pre-target
language manifest, repository commit`6d206ec7d337a7f76f34ddfc82893389cabbd76d`.
The original CC BY-NC-SA4.0 license and acquisition records remain retained.
The read-only comparison uses the model's explicit NFKD/lowercase/combining-mark
removal/ASCII-word normalization. It searches the whole candidate and the longest
exact consecutive candidate word run through **all**`# text` sentences, including
adjacent sentence boundaries within each document. It does not conflate different
documents or treat shared ordinary words as leakage.
An additional accent-normalized scan of every raw line, including non-text
comments/metadata, found no whole-candidate line either.

| File | Audited documents / words | Complete32-word match | Longest consecutive candidate span |
|---|---|---:|---:|
| `cs_pdtc-ud-train-la.conllu` | 950 /182,808 | 0 | 3 words |
| `cs_pdtc-ud-dev.conllu` | 1006 /316,222 | 0 | 3 words |

The longest match in both is the ordinary normalized phrase`jsou mezi nimi`,
candidate word offsets13–15 (zero-based). Training has one occurrence at
`ln95040-074`, raw source line131950; validation has four at`wsj0082-001`,
`wsj2443-001`, `lnd91301-075` and`mf920901-022`. Exact source lines/word offsets
are in`data/derived/novelty_audit_v1/AUDIT.json`. Eleven distinct candidate words
do not appear at all as training words; six do not appear in validation.
Those absences are supplementary observations, not a requirement for independent
decoding. Expected letter n-grams and ordinary vocabulary overlap are the purpose
of language-model training and are not an already supplied answer.

The existing public
[cyphersolver tree snapshot](https://api.github.com/repos/dbourdeau/cyphersolver/git/trees/a43993754e2edd5bdc159bb5859a3d3ff78b7d98?recursive=1)
was read without modifying its scout copy or downloading the repository. It has
13,486 entries and`truncated=false`. A bounded path-name scan for
`615|11.?210|stb|course|1952|transport|chrud` produced six incidental matches:
a1706 key's DECODE R615, a1754 key's D1952, three Louis1615 paths and a1736 file's
D1615. None names HC615, this course item, the supplied archive reference or the
candidate sentence. This is only a **path inventory** audit. It does not establish
that no generic file contains relevant data, that ignored images do not exist,
or that other commits/repositories have no decipherment.

Exactly four public search queries were issued in one batch:

1. `"Unsolved cryptogram" "11 210"`
2. `"HC615" cryptogram`
3. `"Vysílají na Ostravsko nejlepší pracovníky Chrudimska"`
4. `"Transporta vyslala devět soudruhů"`

Accented forms in the last two are discovery-query hypotheses, not observed
original orthography or a verified historical headline. The returned batch
provided only unrelated HC615 product/datasheet/manual name collisions, with no
relevant primary historical page or existing matching decipherment. No irrelevant
page was treated as an authority or downloaded. Full tool-returned search text,
query list, returned URLs, access date and SHA-256 are retained in
`data/raw/novelty_audit_v1/`; that text is not claimed to be raw HTTP page bytes.
The one relevant primary record is the directly re-read official API above.
Search indexing limits, unindexed historical newspaper OCR, other spelling and
undigitised course materials remain unexamined. Absence from these four queries
does **not** imply global novelty.

Permissible reporting: “Using the locked public source transcript and calibrated
substitution solver, we reconstructed a complete candidate for HC615, whose
public catalogue was still labelled Not solved when checked on2026-10-05. The
candidate was not present in the supplied pinned train/dev text.” Exact
regeneration/coherence/cipher-family support must be established by the separate
cryptanalytic audit before upgrading that candidate to a solved status.

Unsupported reporting: “first decipherment ever,” “no one previously solved
this,” a named original1952 author/article/date, an entirely new cryptanalytic
method, or an exhaustive no-contamination guarantee. LLM pretraining contents
were not audited; this source/corpus review cannot make that claim. No people
were contacted and no protected course/archive answer source was requested.

Reproduce the local portion with`python3 scripts/audit_novelty_leakage_v1.py`.
It uses no network or inference and writes only its own audit output. The
`NOVELTY_AND_LEAKAGE_AUDIT_v1_MANIFEST.json` receipt freezes all owned outputs
plus hashes of read-only inputs. State, checkpoints, source transcript, language
models, target candidate and Git were not modified.
