# Codex Prompt: Canonical Greek Extraction Pass v0.1

## Mission

Fill the `canonical Greek reconstruction/control channel` inside logion cards with actual Greek text from the local SBLGNT cache wherever the project already gives explicit Matthew, Mark, or Luke references.

This is the logical next step after `Five-source original-language apparatus v0.1`, because that pass made the gap visible: most cards had a canonical channel, but not the actual Greek canonical text.

## Source Corpus

Use only the local SBLGNT cache:

- `/tmp/euagelia-sblgnt/Matt.txt`
- `/tmp/euagelia-sblgnt/Mark.txt`
- `/tmp/euagelia-sblgnt/Luke.txt`

Treat SBLGNT as an open working Greek control text, not as the final critical edition for publication.

## Required Work

1. Read all `corpus/cards/logion-XXX.md` files.
2. Extract explicit Matthew/Mark/Luke references already present in the cards.
3. Normalize references such as:
   - `Мт 7:7`
   - `Мк 4:22`
   - `Лк 11:9`
   - `Matthew 8:20`
   - `Mark 12:13-17`
   - `Luke 20:20-26`
4. Pull the corresponding Greek verse text from the local SBLGNT files.
5. Update only the `### 5. Canonical Greek reconstruction/control channel` section inside each card’s `Five-source original-language apparatus v0.1` block.
6. Do not insert canonical Greek text into the P.Oxy. channels.
7. Do not treat canonical Greek as a Thomas manuscript witness.
8. Do not change inclusion decisions or clean-reader text.
9. If no explicit canonical reference can be safely extracted, keep the channel as a visible gap.

## Output Format Inside Each Card

Use a compact list:

```markdown
Local Greek canonical/control text currently transcribed:
- Matthew 7:7: `...`
- Luke 11:9: `...`
```

For multi-verse ranges, keep the reference and combine the verses in canonical order.

## Audit Deliverables

Create or update an audit file recording:

- how many cards now have canonical Greek text in the channel;
- how many remain pending;
- how many canonical references were extracted;
- any limitations and next steps.

## Quality Rules

- Prefer absence over false precision.
- Extract only explicit references already present in the project.
- Avoid guessing parallels.
- Keep SBLGNT attribution visible in the audit and source register.
- Leave publication-level verification against NA28/UBS/Layton/etc. for a later pass.
