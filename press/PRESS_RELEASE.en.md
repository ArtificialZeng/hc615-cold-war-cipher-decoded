# 220 Symbols. Zero Edits. A Cold War Cipher You Can Check Yourself.

**AI-assisted research reconstructs every symbol of HC615, an archival cryptanalysis-course exercise catalogued around 1952.**

*Proposed announcement text, prepared 5 October 2026. External specialist confirmation and an official catalogue update are pending.*

A page of digits, dots, bars and unfamiliar signs now reads as a complete Czech message. The HC615 project has recovered a single substitution key that re-encodes **all 220 observed symbols, all 32 segments and all eight source lines**, with no changed symbols, deleted symbols, nulls or position-specific exceptions. The solution, source ledger and executable verification are prepared together in a [GitHub-ready research package](../README.md).

HC Portal calls the item **“Unsolved cryptogram in 11 210.”** Its public record attributes the sheet to circa 1952 cryptanalysis-course material in the Czech Security Services Archive, `ZSGS / box BF388a, 27-19/6-099`. The record was still labelled “Not solved” at the project's 5 October 2026 check. That label describes a catalogue entry; it does not establish that nobody has ever privately read the exercise. [Original catalogue record](https://api.hcportal.eu/api/cryptograms/615).

The decoded passage describes Transporta sending **nine comrades to a one-year work brigade**, with Ostrava needing volunteers experienced in political work. The content is coherent throughout, rather than a collection of isolated English-like fragments. The exact output is Czech without accents; accents, capital letters and punctuation are supplied separately as an editorial reading. The company/region phrase `chrudimska` admits two punctuation-and-accent readings with the same underlying letters. [Complete text and key](../docs/SOLUTION.md).

The mechanical result is unusually easy to inspect: **22 observed symbol classes, one fixed table, 220 matches.** A short Python verifier checks the forward transformation and uses an included Czech statistical cache to recheck saved scores. No external AI service, new model training, or new search is needed. Readers can also compare the symbol classes directly against the [original source image](https://api.hcportal.eu/media/1762/14161684790141.jpg). The certificate proves agreement with the frozen, occurrence-bearing transcription; comparing that transcription to the scan remains a separate source check. [Reproduction instructions](../docs/METHODS.md).

The attack used classical simulated annealing and Czech character statistics in an AI-assisted research workflow. Six separate matched synthetic controls qualified the solver before the real target run. All 16 bounded restarts on the locked target converged on the same observed key and complete text. These checks support reproducibility; restart agreement is not a theorem of global uniqueness. [Methods and experiment record](../docs/METHODS.md).

The result is a **complete reconstruction of the observed message**, not a claim to have recovered a secret spy letter or invented a new cipher-breaking algorithm. The catalogue describes a teaching exercise. Four absent plaintext letters, `f/q/w/x`, have no recoverable historical symbols in this sheet. The independent internal checks used separate AI agents and executable programs, not external expert peer review. No world-first claim, institutional endorsement or official “solved” update is being announced. [Claim ledger](../docs/CLAIMS.md), [current publication and review status](../docs/PUBLICATION_STATUS.md).

The project invites HC Portal's coordinator, Czech readers and historical-cryptology researchers to inspect the evidence and identify any prior course answer or decipherment. [Verified professional contacts](../docs/EXPERT_CONTACTS.md).

**The strongest headline is also the most testable: every observed symbol has an explanation, and anyone can run the check.**
