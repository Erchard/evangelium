# Final All-114 Decision Audit v0.1

Status: working audit, 2026-07-17.

## Purpose

This audit checks whether the project is ready to freeze the clean reconstructed reader. The answer is: not yet.

The current clean reader is now well supported as a working reconstruction: all 31 current reader units have cards, evidence/control support, synchronized language layers, and expanded Ukrainian appendix sections. The remaining risk is not the current reader itself, but the non-included corpus. Several non-included logia still contain possible early cores that could change the final reader if they survive a stricter split-core review.

## Current Reader Support

Current clean reader units:

1, 2, 3, 4, 5, 6, 9, 10, 16, 20, 22, 25, 26, 31, 32, 33, 34, 35, 36, 39, 41, 54, 72, 73, 86, 89, 95, 96, 99, 100, 107.

Audit result:

- Evidence notes: present for all 31 current reader units.
- Synoptic/control files: present for all reader units that need a dedicated control file, with some cluster-level files for grouped controls.
- Language layers: Ukrainian, English, Coptic, Greek, and parallel layers exist for the 31 current reader units.
- Greek policy: current Greek layer is controlled by `greek-retroversion-confidence-audit-v0.1.md`; hypothetical retroversions are not treated as witnesses.
- Full appendix: all 31 current reader units now have expanded Ukrainian reader-facing sections.

Conclusion: the current reader is defensible as a working reader. It is not yet final because the remaining 83 logia have not all received final decision-level explanation.

## Included Units That Still Need Publication Polish

These units may remain in the reader, but need final wording, bibliography, or caution notes before publication.

| Logia | Audit category | Reason |
| --- | --- | --- |
| 1-6 | `CURRENT_READER_NEEDS_PUBLICATION_POLISH` | Strong project foundations, but P.Oxy. 654 lacunae and early/Thomasine expansion boundaries need final notes. |
| 9, 10, 16, 20, 22 | `CURRENT_READER_NEEDS_PUBLICATION_POLISH` | Strong cores, but all rely on core/full-logion distinctions and hypothetical Greek for several units. |
| 25, 33, 34, 35, 41, 54, 72, 73, 86, 89, 95, 96, 99, 100, 107 | `CURRENT_READER_NEEDS_PUBLICATION_POLISH` | No loaded extant Greek Thomas witness; Greek forms must remain explicitly hypothetical. |
| 26, 31, 32, 36, 39 | `CURRENT_READER_NEEDS_PUBLICATION_POLISH` | Greek witness exists in some form, but partial, lacunose, or compositionally complex evidence must be described carefully. |
| 72 | `CURRENT_READER_NEEDS_PUBLICATION_POLISH` | Included with a stronger dependence warning than most current reader units because Luke 12 is the only strong external control. |

No current reader unit should be removed in this audit. But none should be converted from marked to unmarked inclusion before publication polish.

## Strongest Non-Included Reader Candidates

These logia could still change the final clean reader if a split-core review supports them.

| Logia | Audit category | Why they remain live |
| --- | --- | --- |
| 45 | `SPLIT_CORE_REVIEW` | Tree/fruit and treasure-heart material has strong Matt/Luke controls but the Thomas form is composite. |
| 47 | `SPLIT_CORE_REVIEW` | Two masters, new wine, and patch material have strong controls but must be separated. |
| 63 | `REOPEN_AS_STRONG_CANDIDATE` | Rich-fool core has Luke 12 control and full Coptic extraction; needs dedicated control table. |
| 64 | `SPLIT_CORE_REVIEW` | Banquet invitation core may be strong; anti-merchant ending must remain separate. |
| 65-66 | `SPLIT_CORE_REVIEW` | Tenants/rejected-stone cluster has strong controls but high allegorical and passion-tradition risk. |
| 76 | `SPLIT_CORE_REVIEW` | Pearl and imperishable treasure may contain an early core, but the Thomas form is composite. |
| 78 | `REOPEN_AS_STRONG_CANDIDATE` | Wilderness/reed/soft clothing core has strong Matt/Luke controls; final truth clause is riskier. |
| 79 | `SPLIT_CORE_REVIEW` | Hearing/keeping-word core may be viable; womb and eschatological reversal material must be separated. |
| 90 | `APPENDIX_ONLY_UNCERTAIN` for now | Yoke/rest is attractive but too close to Matthew 11 without broader control. |
| 94 | `SPLIT_CORE_REVIEW` | Seek/find/knock must be reviewed with Logia 2 and 92 to avoid duplication. |
| 103 | `SPLIT_CORE_REVIEW` | Thief/watchfulness core has controls, but Thomas's domain/kingdom wording is difficult. |
| 109 | `SPLIT_CORE_REVIEW` | Hidden treasure core has Matthean control, but Thomas's inheritance/sale/usury expansion is problematic. |
| 113 | `SPLIT_CORE_REVIEW` | Kingdom-not-observed core has Luke 17 and Logion 3 controls; duplication risk is high. |

Review A completed: split-core review for Logia 45, 47, 63, 64, 65-66 now exists in `split-core-decision-review-a-v0.1.md`.

Review B completed: split-core review for Logia 76, 78, 79, 94, 103, 109, 113 now exists in `split-core-decision-review-b-v0.1.md`.

Current next package: controlled clean-reader candidate pass for the promoted cores from Reviews A and B.

Reason: Reviews A and B identified candidate cores for a later reader pass but did not edit the clean reader. The next pass should decide which, if any, genuinely belong in the clean reconstruction without creating duplication or lowering the evidentiary threshold.

## Appendix-Only or Deferred Material

These logia should remain outside the clean reader unless later research changes the evidence profile. They still need good appendix explanation.

| Logia | Audit category | Main reason |
| --- | --- | --- |
| 7, 8, 11, 17, 18, 21, 23, 28, 30, 38, 40, 42, 48, 51, 58, 62, 68, 69, 81, 82, 91, 92, 93, 97, 101, 111 | `APPENDIX_ONLY_UNCERTAIN` | Interesting material, but insufficiently controlled, too composite, or better handled as uncertain appendix material at this stage. |
| 14, 15, 19, 24, 27, 29, 37, 43, 49, 50, 53, 56, 59, 60, 61, 67, 70, 71, 74, 75, 77, 80, 83, 84, 85, 87, 88, 98, 102, 104, 105, 106, 108, 110, 112 | `CLUSTER_DEFER` or `LIKELY_SECONDARY_OR_FRAME` | Needs thematic cluster explanation more than reader promotion. |
| 114 | `EXCLUDE_AS_SECONDARY` | Strong exclusion example: late gender/transformation frame, not an early sayings core. |

## Stale or Inconsistent Files

The audit found three types of stale state:

1. `full-corpus-classification-v0.1.md` is historically useful but no longer current. It still treats several now-included reader units as `HIGH_PRIORITY_DEEPENING`.
2. `corpus/tables/logia-workflow-matrix.md` contained stale `Needs multilingual sync` notes for reader units 86, 89, 95, 96, 99, 100, and 107.
3. `inclusion-decisions-table.md` is useful but not a true all-114 final table. It omits many low-priority or deferred logia as individual rows and should not be treated as the final publication control table.

## Publication Gate

The project should not freeze the final clean reader until:

1. controlled clean-reader candidate pass is completed for the promoted cores from split-core reviews A/B;
2. `inclusion-decisions-table.md` is replaced or upgraded into a true all-114 publication decision table;
3. full appendix sections for excluded/deferred/uncertain logia are expanded beyond skeleton level;
4. evidence dossier receives a publication pass with bibliography and rights/citation policy.

## Next Work Package

Reviews A and B have been completed. Next prompt should perform:

**Controlled Clean-Reader Candidate Pass: promoted cores from Reviews A/B**

Required outputs:

- reader-candidate evaluation for 45A/45B, 47B, 63, 64A, 76A/76B, 78A, 79A, and 103A;
- explicit duplication/dependence warnings;
- update clean reader only if a candidate clearly improves the reconstruction;
- update workflow matrix and publication gap audit;
- keep Greek retroversions labeled hypothetical unless an extant Greek witness is loaded.
