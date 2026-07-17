# IDE Codex Prompt: High-Candidate Deepening Sprint A

## Project Goal

The project reconstructs the earliest recoverable sayings-gospel layer preserved in the Gospel of Thomas tradition. The clean reader must include only responsibly supported early material, while the full appendix must explain all 114 logia, including excluded and uncertain ones.

## Current Need

The publication roadmap identifies a first high-candidate package of uncertain logia that could affect the final clean reconstruction:

- Logion 44
- Logion 46
- Logion 55
- Logion 57
- Logion 76
- Logion 78
- Logion 79

These logia currently have primary cards but lack sufficient evidence notes and control files.

## Task

Deepen this first high-candidate package without changing the clean reader.

## Required Work

1. Create evidence notes for Logia 44, 46, 55, 57, 76, 78, and 79.
2. Create focused synoptic/control files for the same logia.
3. For each logion, decide whether it is:
   - a possible `INCLUDE_WITH_MARKER` candidate;
   - still `UNCERTAIN`;
   - better treated as `DEFER`.
4. If a logion is composite, separate possible early core from likely secondary expansion.
5. Update `inclusion-decisions-table.md` with these seven logia.
6. Update `logia-workflow-matrix.md` to show that evidence notes and controls now exist.
7. Update the collection log.

## Quality Rules

- Do not change `reconstructed-gospel-uk.md`.
- Do not add any of these logia to the clean reader in this task.
- Do not claim extant Greek Thomas witnesses where there are none.
- Any Greek form for these seven logia must remain `Greek retroversion, hypothetical`.
- Keep conclusions cautious and reversible.

## Expected Output

New evidence notes:

- `notes/logion-044-evidence-en.md`
- `notes/logion-046-evidence-en.md`
- `notes/logion-055-evidence-en.md`
- `notes/logion-057-evidence-en.md`
- `notes/logion-076-evidence-en.md`
- `notes/logion-078-evidence-en.md`
- `notes/logion-079-evidence-en.md`

New control files:

- `04_Synoptic_Parallels/logion-044-blasphemy-spirit-controls.md`
- `04_Synoptic_Parallels/logion-046-john-least-kingdom-controls.md`
- `04_Synoptic_Parallels/logion-055-discipleship-cross-controls.md`
- `04_Synoptic_Parallels/logion-057-weeds-controls.md`
- `04_Synoptic_Parallels/logion-076-pearl-treasure-controls.md`
- `04_Synoptic_Parallels/logion-078-wilderness-reed-controls.md`
- `04_Synoptic_Parallels/logion-079-womb-word-controls.md`

## Verification

After editing, verify:

- all seven evidence notes exist;
- all seven control files exist;
- workflow matrix marks evidence notes as `YES`;
- clean Ukrainian reader is untouched.
