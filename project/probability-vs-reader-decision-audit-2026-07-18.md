# Probability vs Reader Decision Audit

Date: 2026-07-18

## Purpose

This audit checks a specific risk: a logion may have a high probability of later composition while still appearing in the clean reader, or a logion may have a high early-probability profile while being excluded from the clean reader.

This is not a simple arithmetic inclusion rule. A logion can be early by motif but excluded because:

- the preserved Thomas form is composite;
- the early element is already represented by a stronger clean-reader logion;
- the text has high dependence risk on Matthew, Luke, or another known control;
- the early core has not been safely separated from a later frame;
- there is no extant Greek Thomas witness and no strong external control.

Still, this audit is important because the reader-facing project must not appear arbitrary.

## Method

Reusable script:

- `tools/probability_reader_audit.py`

Command:

```bash
python3 tools/probability_reader_audit.py
```

The script compares:

- latest / gold-level numeric probability profile in `corpus/cards/logion-001.md` through `corpus/cards/logion-114.md`;
- `Reader text` value in `corpus/tables/logia-workflow-matrix.md`;
- publication status in `reconstruction/earliest-sayings-gospel/all-114-publication-decision-table-v0.1.md`.

The audit uses:

- early score = `До 60 року` + `60-90 роки`;
- late score = `90-130 роки` + `Після 130 року`.

## Summary

- Cards with current/latest numeric probability profile: 114/114.
- Cards with duplicate current probability profiles: 0.
- Included clean-reader units with late score >= 60 or post-130 score >= 20: 1.
- Excluded units with early score >= 60: 10.
- Excluded units with early score >= 50: 20.

## Main Finding 1: Included Unit With High Late Score

| Logion | Reader | Early | Late | Post-130 | Current decision | Audit judgment |
| ---: | --- | ---: | ---: | ---: | --- | --- |
| 1 | YES | 35 | 65 | 20 | `INCLUDE_WITH_MARKER` | Needs explicit final review. |

### Logion 1

This is the only current clean-reader unit where the latest probability profile itself still leans late.

This may be defensible because Logion 1 functions as a collection-frame / interpretation promise and is preserved in P.Oxy. 654. But it is not the same kind of material as a short independent saying of Jesus. If the final product is marketed as "the earliest sayings gospel," the reader may reasonably ask why a likely collection-frame saying appears in the clean text.

Current recommendation:

- Keep Logion 1 in the clean reader only as a marked prologue / collection-frame unit.
- The card now contains `Probability / reader-decision rationale v0.1`.
- Final freeze still must decide whether the printed book wants this as numbered clean text or as a marked prologue in the front matter.

## Main Finding 2: Excluded Units With Early Score >= 60

These are not automatic mistakes. They are the main review list where appendix/dossier must explain non-inclusion especially clearly.

| Logion | Early | Late | Current decision | Publication status | Why exclusion may still be justified |
| ---: | ---: | ---: | --- | --- | --- |
| 94 | 70 | 30 | `KEEP_APPENDIX_ONLY_FOR_NOW` | `APPENDIX_ONLY_STABLE` | Strong seek/ask/knock tradition, but currently redundant with Logion 2 as the selected seek/find representative. |
| 90 | 65 | 35 | `KEEP_APPENDIX_ONLY_FOR_NOW` | `APPENDIX_ONLY_STABLE` | Matt 11:28-30 control is strong, but dependence and wording need deeper review. |
| 93 | 65 | 35 | `UNCERTAIN` | `APPENDIX_ONLY_STABLE` | Matt 7:6 / secrecy motif is strong but may be one-source or dependent. |
| 64 | 60 | 40 | 64A/64B `KEEP_APPENDIX_ONLY_FOR_NOW` | `APPENDIX_ONLY_STABLE` | Banquet core plausible, but long/dependence-risky and currently not clean as a reader unit. |
| 76 | 60 | 40 | `KEEP_APPENDIX_ONLY_FOR_NOW` | `APPENDIX_ONLY_STABLE` | Pearl/treasure cores plausible, but need Matthew-only parable/treasure cluster decision. |
| 78 | 60 | 40 | `KEEP_APPENDIX_ONLY_FOR_NOW` | `APPENDIX_ONLY_STABLE` | John-tradition control strong, but not clean as a free-standing reader unit. |
| 79 | 60 | 40 | `KEEP_APPENDIX_ONLY_FOR_NOW` | `APPENDIX_ONLY_STABLE` | Hearing/keeping core overlaps current reader and remains embedded in a composite unit. |
| 104 | 60 | 40 | 104A bridegroom-fasting core `APPENDIX_ONLY_STABLE`; full logion appendix-only | 104A `APPENDIX_ONLY_STABLE`; full logion appendix-only | Follow-up completed: strong bridegroom-fasting motif, but no extant Greek Thomas witness and Thomas ritual/bridal-chamber frame remains too entangled for clean-reader extraction. |
| 109 | 60 | 40 | `KEEP_APPENDIX_ONLY_FOR_NOW` | `APPENDIX_ONLY_STABLE` | Hidden-treasure image is interesting but Matthew-only control and expansion remain risky. |
| 113 | 60 | 40 | `KEEP_APPENDIX_ONLY_FOR_NOW` | `APPENDIX_ONLY_STABLE` | Kingdom-not-observed core is already represented more strongly by Logion 3. |

Current recommendation:

- Do not promote these automatically.
- Card-level `Probability / reader-decision rationale v0.1` blocks have now been added to Logia 64, 76, 78, 79, 90, 93, 94, 104, 109, and 113.
- The full appendix and evidence dossier still need final prose polish so these rationales are visible to non-specialist readers.

## Main Finding 3: Excluded Units With Early Score >= 50

The broader watchlist is:

- 21, 55, 57, 64, 65, 66, 68, 69, 76, 78, 79, 90, 92, 93, 94, 101, 104, 109, 111, 113.

These should not drive immediate reader expansion by themselves. They should drive review priority.

## Main Finding 4: Superseded Historical Probability Profiles

The previous audit found 24 cards with more than one numeric probability table:

- 1, 2, 3, 4, 5, 6, 7, 9, 16, 20, 22, 23, 25, 26, 27, 31, 32, 33, 34, 35, 36, 37, 38, 39.

This documentation risk has been remediated at the card level. Older/local probability tables in these cards are now explicitly labeled as `superseded historical probability table`, while the current profile remains the lower `### Ймовірнісний профіль` block.

Important example preserved for method:

- Logion 6 initially appears suspicious if the first old profile is read: late score 65, post-130 score 25.
- But the current/latest gold-level profile is early score 65, late score 35, post-130 score 10.
- Therefore Logion 6 is not currently a reader/probability contradiction; its older tables must be read as superseded historical profiles.

Current recommendation:

- Maintain the distinction between historical/local probability notes and the current profile.
- For split-core logia, separate probability for full logion from probability for included core.

## Conclusion

No mass accidental inversion was found.

After final clean-reader freeze, the remaining probability-related work belongs to book production and proofing:

1. Polish the appendix/dossier presentation of the probability-vs-reader principle for non-specialist readers.
2. Replace remaining generic early-core placeholders with logion-specific layer models.
3. During final book layout, decide whether Logion 1 is printed as numbered clean text or as a visually distinct prologue/front-matter unit while retaining lookup number 1.
