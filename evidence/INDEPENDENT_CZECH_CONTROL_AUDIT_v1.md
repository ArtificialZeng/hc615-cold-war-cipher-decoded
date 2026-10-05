# Public projection of INDEPENDENT_CZECH_CONTROL_AUDIT_v1.md

Internal AI-agent/code record, not outside peer review. This labelled projection redacts private paths and excludes source-image pixels. Earlier pending verdicts are preserved. Original hashes are in ORIGINAL_EVIDENCE_INDEX.json; historic paths need not exist in this public layout.

---

# Independent Czech substitution-control audit

**PASS for matched-model calibration and software accounting only.** Independently recomputed6winning outputs and all96restart outputs. Mean letteraccuracy=0.9967077590;6/6≥0.90, above the locked≥0.95mean/5of6gate. Micro letters=1215/1219; exact words=189/192. No target was read or inferred; no search was rerun.

The entire27^4float32 scorearray was independently rebuilt from pinned licensed train data byte-exact. Base27 index endpoints are0 and531440; all finite. Every scorer uses exactly length−3overlapping windows, with boundaryspace26 fixed. The score is a sum of smoothed jointquadgram logweights, an optimization heuristic rather than normalized whole-text likelihood or historicalkey posterior.

All96restart keys and6winning keys are permutations and support exact forward/inverse roundtrip. Synthetic forwardkey maps plaintext→cipherlabel; solver key maps cipherlabel→plaintext. Fixed seeds regenerate all6original cipherinputs. The16×32768attempt cap per case is respected in source/output; a selfswap consumes one attempt. Trainingfrequency initialization and every letterpair swap/restart preserve bijection. Unused3–5keylabels per control are unidentifiable and are not included in a supposed fullkeyrecovery score.

C++ accepts only model, opaqueinteger cipherinput, frequencyorder, seed, restart/step counts and outputpath. It neither accepts truth nor opens any sourceplaintext. The wrapper reads truth only after inference for metrics. All6windows exactly match the registered32word heldoutdevsource windows, all source documents differ from train IDs, and no whole-window repetition exists in train even across sentence boundaries. Official pinned Gitblob hashes were recomputed for train/dev/license/README. Some source documents/windows overlap never-inferred prepared v1artifacts; the available record does not demonstrate completely new documents relative to every preparation or rule out unrecorded runs.

There are4 lettererrors:3inC00,1inC04; all exact offsets/words are retained inJSON. A false spelling may outrank trueplaintext. Sixmodern Czech synthetic passages do not establish targetlanguage, wordboundaries, glyphgrouping, historicalorthography or cipherfamily. Candidate roundtrip alone is automatic under any fixedbijection and cannot prove authenticity.

One provenance gap is nonblocking here: originalconfig/runner omit a separate frequencyorder SHAcheck. The current order was independently reconstructed from traincounts and matches; this audit seals its currenthash without editing the preregistered config. Config andmanifest exactly match frozen copies. Declaredtimestamps are consistent but not independently trusted timestamps.

Machine observations and input/output hashes: `reports/INDEPENDENT_CZECH_CONTROL_AUDIT_v1.json`. Reproduction script: `scripts/independent_czech_control_audit_v1.py` (creates append-only outputs; does not run inference). Existing experiment/state/Git files were not changed.
