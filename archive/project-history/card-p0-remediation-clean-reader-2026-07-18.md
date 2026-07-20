# Card P0 Remediation: Clean-Reader Contradictions

Status: remediation pass, 2026-07-18.

## Problem

The most current card-level quality problem is not structural coverage. `tools/qa_crosscheck.py` already confirms 114 card files, 114 appendix sections, and 37 synchronized clean-reader units.

The urgent problem is internal contradiction inside cards for logia that are already printed in the clean reader. Several cards contain older working blocks saying `Reader text: NO`, `UNCERTAIN`, `Primary card v0.1`, or "not yet in the main reconstruction" even though the current workflow matrix and clean reader include a marked core.

## Fix Scope

This pass fixes the highest-impact clean-reader contradiction cards:

- 6
- 46
- 86
- 89
- 91
- 95
- 96
- 99
- 100
- 103
- 107

## Method

For each card:

1. Preserve the current clean-reader decision.
2. Clarify that only the included core is printed where the full logion remains uncertain or appendix-only.
3. Replace stale `Reader text: NO` statements in old card blocks.
4. Replace stale predecision next actions with publication-polish or apparatus-polish actions.
5. Keep `Greek retroversion, hypothetical` labels intact.
6. Do not change clean-reader membership.

## Expected Result

After this pass, these clean-reader cards should no longer tell the reader or editor that their included core is not in the clean reconstruction.

## Validation

Run:

```bash
python3 tools/qa_crosscheck.py
python3 tools/probability_reader_audit.py
git diff --check
```

Current targeted contradiction check after remediation:

| Logion | Result |
| ---: | --- |
| 6 | P0_CLEAR |
| 46 | P0_CLEAR |
| 86 | P0_CLEAR |
| 89 | P0_CLEAR |
| 91 | P0_CLEAR |
| 95 | P0_CLEAR |
| 96 | P0_CLEAR |
| 99 | P0_CLEAR |
| 100 | P0_CLEAR |
| 103 | P0_CLEAR |
| 107 | P0_CLEAR |

The project-wide exact-pattern card audit now reports:

- `READER_STATUS_CONFLICT`: 0
- `INCLUDED_TEXT_SAYS_NOT_MAIN`: 0
- `LOCAL_NOT_DECIDED`: 9
- `MISSING_PROBABILITY`: 3

## Next Step

After this P0 pass, the next logical card remediation is the `LOCAL_NOT_DECIDED` set:

- 12, 13, 15, 17, 18, 19, 24, 28, 29.
