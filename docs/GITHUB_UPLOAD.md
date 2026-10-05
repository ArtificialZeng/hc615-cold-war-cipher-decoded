# Maintain the HC615 GitHub repository

The actual repository is [ArtificialZeng/hc615-cold-war-cipher-decoded](https://github.com/ArtificialZeng/hc615-cold-war-cipher-decoded). Public author: Zijian Zeng, PhD. Release v1.0.1 updates publication metadata; the original v1.0.0 package and all frozen scientific evidence are retained.

## Obtain and verify the public files

After the initial upload is available:

```sh
git clone https://github.com/ArtificialZeng/hc615-cold-war-cipher-decoded.git
cd hc615-cold-war-cipher-decoded
python3 scripts/verify_release.py
python3 scripts/verify_solution.py
python3 -m unittest discover -s tests -v
```

The English `README.md` is GitHub's default landing page and links Chinese, Czech and Japanese versions. The repository includes a Linux/macOS/Windows verification workflow; check its actual run result before announcing CI success.

## Make an evidence-preserving update

Use a branch and a descriptive commit. Preserve frozen source transcripts, original results, keys and certificates; put corrected or newly reviewed scientific evidence in new versioned files. Regenerate the release manifest after any documented payload change, excluding the manifest itself, Git metadata and ignored build/cache files. Then run both verifiers and applicable regression tests.

Record repository publication and external-review status in [PUBLICATION_STATUS.md](PUBLICATION_STATUS.md) only after the corresponding upload or reply is actually observed. Do not replace a pending-review statement with endorsement based on outreach alone. The coordinator inquiry has been acknowledged; substantive assessment remains pending.

## Keep the public package separate

Keep the three licence scopes and upstream attribution. Do not upload the separately labelled **PRIVATE RESEARCH ARCHIVE**, raw archival scan/crops, raw cached language corpus, private correspondence or compiled local binaries. Optional acquisition and builds belong in ignored directories. The public package already contains what is needed for offline evidence verification.

Use the actual repository URL in citations and press copy. Do not add a fictitious DOI, affiliation, original course answer or expert quotation. The visually checked Word feature remains its original artifact; publication metadata is supplied in the current editable press files and documentation.
