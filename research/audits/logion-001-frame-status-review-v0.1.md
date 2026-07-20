# Logion 1 Frame-Status Review v0.1

Status: completed pre-freeze review, 2026-07-18.

## Question

Should Logion 1 be treated as part of the reconstructed earliest sayings gospel, or as a collection frame that belongs to the Gospel of Thomas transmission but is not itself an independently secure early saying?

## Evidence Summary

Logion 1 is present in the Coptic Gospel of Thomas and has Greek control in P.Oxy. 654. This makes it textually important for the history of the Thomas collection. It is not a late Coptic-only addition.

At the same time, its function is visibly editorial. It tells the reader how to approach "these sayings" and promises life to the one who finds their interpretation. That is the language of a collection frame. The saying does not behave like an independent aphorism, parable, dispute saying, or sapiential unit.

The Greek witness is also not equally strong at every point. P.Oxy. 654 controls the transition and the presence of the frame, but much of the core wording is reconstructed in lacunae. This does not remove the logion from the tradition, but it prevents using it as a high-confidence independent early saying.

The current probability profile in `notes/logion-001-evidence-en.md` assigns the strongest pressure to 90-130 CE. That is compatible with a developed collection frame already known in Greek, but not with quietly presenting the unit as one of the most secure earliest sayings.

## Decision

Recommended final editorial status:

`FRAME_INCLUDED_WITH_MARKER`

Meaning:

- keep Logion 1 in the controlled source-layer reader for now, because the current multilingual reader, Coptic layer, Greek layer, English layer, Arabic literary layer, and parallel edition are synchronized around a 34-unit reader set;
- do not treat Logion 1 as an ordinary reconstructed saying;
- in final print generation, present Logion 1 as the opening frame or prologue to the reconstructed sayings collection, not as evidence that this exact sentence belongs to the earliest recoverable Jesus-saying core;
- keep the explanation in the apparatus, appendix, and evidence dossier, not inside the clean first reader pages.

## Why Not Remove It Now

Immediate removal from `reconstructed-gospel-uk.md` would force a synchronized update of all public language layers, the parallel edition, clean-reader counts, QA expectations, and appendix anchors. That should happen only in a dedicated clean-reader freeze/generation pass.

The cleaner move at this stage is to lock the editorial interpretation: Logion 1 is allowed to function as the reader's doorway into the collection, but it is not allowed to function as an unmarked early-saying datum.

## Print Implication

For the Ukrainian and English paper books, Logion 1 should remain visually clean on the first pages. The print edition should avoid brackets or technical labels in the main text.

The distinction belongs in the second layer:

- the apparatus should call it a collection frame;
- the full appendix should explain why it is useful and why it is marked;
- the evidence dossier should classify it separately from ordinary included sayings;
- final generation may optionally typeset it as an opening frame before the main sequence while preserving the Thomas number "1" for lookup.

## Digital Scholarly Implication

The digital companion should preserve the full evidence trail:

- Coptic NHC II witness;
- P.Oxy. 654 Greek witness and lacunae;
- probability profile;
- reason for inclusion;
- reason for marking;
- relation to collection formation and reception.

## Follow-Up Work

1. During the clean-reader freeze pass, decide the final display rule: numbered opening frame inside the clean text, or visually distinct prologue retaining the number "1".
2. During the evidence dossier publication pass, separate `FRAME_INCLUDED_WITH_MARKER` from ordinary `INCLUDE_WITH_MARKER` cases.
3. Run the next probability-pressure reviews for split-core/high-early non-reader cases, especially Logia 46, 90, 91, 103, and 104.
