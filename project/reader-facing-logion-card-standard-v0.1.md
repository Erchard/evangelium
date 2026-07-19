# Reader-Facing Logion Card Standard v0.1

Status: active editorial standard, created 2026-07-19 after reader feedback on Logion 1.

## Purpose

Each logion card and each paper-facing appendix chapter must first serve an ordinary reader, not the internal project workflow. Technical status labels, machine decisions, audit markers, file paths, and control vocabulary belong in the lower research layer or in the digital scholarly companion.

The reader-facing order must be:

1. Coptic text.
2. Greek text, with a short note identifying the papyrus witness or explaining that the Greek is a reconstruction from Coptic/canonical controls.
3. Full Ukrainian translation of the preserved Coptic form.
4. Full English translation of the preserved Coptic form.
5. Human-readable interpretation and context.
6. Reconstruction decision in plain language: what enters the clean reconstruction, what is omitted, and why.
7. Short dating/probability conclusion with percentages and plain explanation.

## Required Section Order

### Coptic Text

Show the Coptic text directly. Give a short source note, for example:

`Source: NHC II,2, Coptic Gospel of Thomas; local working text in sources/primary_texts/...`

Do not begin with `Status`, `Decision`, `Reader status`, `Gold-level`, or internal file links.

### Greek Text

If an Oxyrhynchus witness exists, show it directly and identify the papyrus:

`Source: P.Oxy. 654, lines 3-5. Square brackets mark restored lost text.`

If no direct Greek Thomas witness exists, show the project's Greek retroversion only when it is historically plausible, and say plainly:

`No direct Greek Thomas papyrus is preserved for this logion. The Greek below is a cautious retroversion from the Coptic text, checked against canonical Greek parallels where relevant. It is not a manuscript witness.`

If no responsible Greek reconstruction has been made yet, say so briefly and do not invent one.

### Ukrainian Translation

Give the full Ukrainian translation of the preserved Coptic form, even if the clean reconstruction uses only a shorter core.

Then, when needed, add:

`In the clean reconstruction we print only: ...`

### English Translation

Give the full English translation of the preserved Coptic form, even if the clean reconstruction uses only a shorter core.

Then, when needed, add:

`Clean-reader form: ...`

### Interpretation For Ordinary Readers

Explain the logion in prose suitable for a thoughtful church reader with no textual-criticism training.

The explanation should answer:

- What is the saying trying to say?
- How might an early Jesus-follower or early Christian hear it?
- What biblical, Jewish, early Christian, or Thomasine context helps?
- What are the main possible interpretations?
- What should not be overclaimed?

Avoid phrases such as `INCLUDE_WITH_MARKER`, `DEFER_TO_CLUSTER`, `APPENDIX_ONLY_STABLE`, `Greek status`, `reader status`, `workflow`, and `audit` in the reader-facing section.

### Forbidden Reader-Facing Jargon

The paper-facing Ukrainian and English books must not use internal scholarly shorthand as if the reader already knows it.

Do not write:

- `Thomasine unity reading`;
- `clean reader`;
- `core` without explanation;
- `appendix-only`;
- `cluster-control`;
- `reader-candidate`;
- `Greek status`;
- `retroversion` without explanation;
- raw decision labels such as `INCLUDE_WITH_MARKER`, `UNCERTAIN`, `DEFER`, or `EXCLUDE`.

Use plain reader language instead:

- "у формі, збереженій в Євангелії від Фоми";
- "у чистому тексті реконструкції";
- "давнє ядро вислову";
- "цей вислів лишається тільки в додатку, бо...";
- "групова перевірка споріднених висловів";
- "обережна грецька реконструкція з коптського тексту";
- "ми включаємо / не включаємо цей вислів";
- "ми не можемо бути певні, бо...".

Every explanation must pass a simple test: a thoughtful church reader with no training in textual criticism should understand what is being claimed, what is uncertain, and why the logion did or did not enter the reconstructed text.

### What Enters The Reconstruction

State plainly:

- whether the full logion enters the clean text;
- whether only an ancient core enters;
- which words are omitted;
- why the omitted material is treated as secondary, uncertain, or only contextual.

Even when only a core is included, the full preserved Coptic-form translation must remain visible above.

### Short Dating Conclusion

End the reader-facing card with a concise estimate:

`Most likely written or shaped around ...`

Then give percentage bands. Use percentages as transparent project estimates, not as mathematical proof.

Explain the basis in plain language:

- manuscript witness;
- simplicity or complexity of form;
- relation to canonical parallels;
- signs of later community framing;
- Coptic-only versus Greek witness status.

## Research Layer

The old technical material should not be deleted if it is still needed for auditability. Instead, place it after a separator under:

`## Research Layer`

or, in Ukrainian:

`## Дослідницький шар картки`

This layer may preserve:

- machine-readable statuses;
- evidence links;
- control files;
- historical probability tables;
- gold-level status blocks;
- five-source apparatus;
- unresolved work notes.

Paper-facing books should either omit this layer or translate it into reader-friendly prose. The digital scholarly companion may preserve it in full.

## Pilot

Logion 1 has been converted to this standard in:

- `corpus/cards/logion-001.md`
- `reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-uk.md`

The next editorial pass should apply this standard to all Logia 1-114, including excluded and appendix-only logia.
