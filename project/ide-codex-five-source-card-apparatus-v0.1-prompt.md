# Codex Prompt: Five-Source Original-Language Card Apparatus v0.1

## Mission

For every logion card, make the actual reconstruction sources visible inside the card itself, not only through links to external project files.

The project treats the original-language reconstruction as controlled by five channels:

1. P.Oxy. 1 Greek witness;
2. P.Oxy. 654 Greek witness;
3. P.Oxy. 655 Greek witness;
4. Coptic NHC II translation channel;
5. canonical Greek reconstruction/control channel.

## Required Work

1. Add a `## Five-source original-language apparatus v0.1` block to every `corpus/cards/logion-XXX.md` card.
2. The block must include all five channels for every logion.
3. For the Coptic channel, insert the actual Coptic text directly from `sources/primary_texts/coptic/linssen-thomas-coptic-unicode-working.txt`.
4. For P.Oxy. witnesses:
   - insert the Greek text directly when a card-ready Greek extract already exists;
   - state `[not preserved in P.Oxy. X]` when that papyrus does not preserve the logion;
   - state clearly when DCLP XML coverage exists but the line-level Greek extract is still pending.
5. For the canonical Greek channel:
   - insert only locally transcribed Greek text that is clearly labelled as Matthew, Mark, or Luke;
   - do not mix Thomas papyrus Greek into the canonical channel;
   - where canonical Greek is not yet locally transcribed, state that explicitly.
6. Do not treat a hypothetical Greek retroversion as a manuscript witness.
7. Do not promote or demote any logion in the clean reader during this pass.
8. Fix any old card wording that confuses “no loaded P.Oxy. witness” with “extant papyrus witness.”

## Deliverables

- 114/114 cards contain exactly one `## Five-source original-language apparatus v0.1` block.
- 114/114 cards retain exactly one `## Gold-level status check v0.2` block.
- A new audit file records what is complete and what remains missing.
- Project status documents identify the next source-critical gap.

## Quality Rule

Absence must be explicit. If a source does not preserve a logion, say so. If the text exists in XML but has not yet been extracted into a clean card-ready Greek text, say so. If canonical Greek parallels are known but not locally transcribed, say so. Do not silently imply that a reconstruction has more manuscript support than it actually has.
