# Publish the prepared repository

This guide is for the real repository owner. The package itself has not been uploaded. The public ZIP contains one `hc615/` directory; the separate Git bundle preserves a prepared release commit/tag.

## From the ZIP

Extract the public ZIP, enter `hc615/`, and run:

```sh
python3 scripts/verify_release.py
python3 scripts/verify_solution.py
python3 -m unittest discover -s tests -v
git init -b main
git add .
git commit -m "HC615 v1.0.0: complete observed-message reconstruction"
git tag v1.0.0
```

Use your real configured Git identity. Create an empty GitHub repository called `hc615` (or your chosen name), then use the exact remote URL GitHub provides. The optional `gh` route is:

```sh
gh repo create hc615 --public --source=. --remote=origin --push
git push origin v1.0.0
```

Those commands publish externally and should be run only when you intend to publish. No fake owner or remote address is embedded in the package. Recommended description: **Complete 220-symbol Czech reconstruction of HC Portal 615: fixed key, zero edits, reproducible verifier. External historical review pending.**

## From the Git bundle

```sh
git clone /path/to/HC615_GITHUB_RELEASE_v1.0.0.bundle hc615
cd hc615
python3 scripts/verify_release.py
python3 scripts/verify_solution.py
```

Replace `/path/to/…` with the real downloaded bundle location. The prepared commit uses a clearly labelled release identity; it is not an assertion of the researcher's legal name or affiliation.

## Release contents and settings

The English `README.md` is GitHub's default landing page and links three translations. The workflow covers Linux, macOS and Windows with Python 3.9/3.12. Issue forms distinguish source critique, cryptanalysis and reproduction problems. The DOI/repository fields intentionally remain absent until they exist.

Keep the three licence scopes and upstream attribution. Do not upload the separately labelled **PRIVATE RESEARCH ARCHIVE**, raw archive scan/crops, cached corpus, private email drafts or compiled local binaries. Optional downloads and builds belong in ignored directories. The public package already contains what is needed for offline evidence verification.

After publication, enter the real repository URL in `CITATION.cff` and press copy, and record the publication date in [PUBLICATION_STATUS.md](PUBLICATION_STATUS.md). Update external-review status only with an actual reviewer reply.
