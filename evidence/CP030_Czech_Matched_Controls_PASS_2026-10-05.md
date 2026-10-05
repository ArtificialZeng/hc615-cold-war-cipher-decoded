# Public projection of CP030_Czech_Matched_Controls_PASS_2026-10-05.md

Internal AI-agent/code record, not outside peer review. This labelled projection redacts private paths and excludes source-image pixels. Earlier pending verdicts are preserved. Original hashes are in ORIGINAL_EVIDENCE_INDEX.json; historic paths need not exist in this public layout.

---

# CP030 — matched Czech substitution controls PASS

Six actual independent dev-document windows, each 32 words and 195–212 letters, were encrypted with random fixed substitution and inferred without their truth files. Mean letter accuracy 0.9967077590111953 exceeds the locked 0.95 gate; all six exceed 0.90 versus required five. Micro accuracy is 1215/1219 letters and exact words 189/192. Older prepared v1 controls were not inferred and are not counted as additional tests.

Pinned UD_Czech-PDTC commit6d206ec7d337a7f76f34ddfc82893389cabbd76d supplies 182808 training words from 950 documents. Actual dev documents are disjoint from train IDs, and no complete evaluated dev window occurs in train. The 27^4 little-endian float32 joint-quadgram model, fixed-space convention and training frequency order were independently rebuilt byte-exact. CC BY-NC-SA4.0 source/license and download receipts are retained. Modern Czech calibration does not establish the unknown target's language or family.

The independent auditor recomputed all96 stored restart outputs, six winners and their bijective forward/inverse mappings without new optimization or reading the target. Qualification parameters are 16 restarts ×32768 steps per case, seeds615410–615415. Truth was read by the wrapper only after each inference completed. Sum of overlapping joint quadgram weights is an optimization heuristic, not text likelihood or posterior confidence.

A parser defect that could silently truncate after a noninteger was corrected before actual target inference in v1p1. Five saved input regression cases and the byte-identical repaired C00 run establish valid-input equivalence; this is not a new search strategy or another independent calibration. The original configuration's omitted separate frequency-order hash is disclosed and sealed by independent reconstruction plus the target v1p1 config. Original code/binary/results remain intact.

See reports/INDEPENDENT_CZECH_CONTROL_AUDIT_v1.md and INDEPENDENT_CZECH_STRICT_INPUT_OVERLAY_v1p1.md. This checkpoint seal is recorded after the actual target result; no independently trusted preregistration timestamp is asserted. PASS qualifies this matched-model software experiment, not the target solution. Immediately integrate CP040/CP050; no additional search budget is required.
