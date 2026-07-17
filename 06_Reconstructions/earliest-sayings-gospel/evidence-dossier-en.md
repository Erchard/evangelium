# Evidence Dossier

Status: working evidence dossier v1.3.

## Aim

This dossier supports a reconstruction of the earliest recoverable layer of the sayings gospel tradition preserved in the Gospel of Thomas. The goal is not to reproduce the complete Coptic Gospel of Thomas, but to distinguish probable early material from possible later expansions, redactional developments, and uncertain textual layers.

## Method

Each unit is evaluated independently. A unit may be a complete logion or a smaller layer within a logion.

The reconstruction distinguishes:

- reconstructed early core;
- extant Coptic witness;
- extant Greek witness;
- hypothetical Greek retroversion;
- possible expansion;
- secondary redaction;
- unresolved textual problem.

The decision categories are:

- `INCLUDE`
- `INCLUDE_WITH_MARKER`
- `UNCERTAIN`
- `EXCLUDE_AS_SECONDARY`
- `DEFER`

## Source Hierarchy

1. Manuscript facsimiles and extant witnesses.
2. DCLP / Papyri.info TEI XML for Greek papyri.
3. Open Coptic transcriptions checked against facsimiles.
4. Explicitly marked Greek retroversions from Coptic where a Greek Vorlage or Greek circulation is historically probable.
5. Academic editions where available and lawfully citable.
6. Modern translations only as controls, not as primary evidence.

## Greek Retroversion Policy

Absence of an extant Greek witness does not mean that a Greek form never existed. For Coptic-only units, the project should attempt a cautious Greek retroversion when the evidence suggests that a Greek Vorlage or Greek circulation is historically probable.

Such retroversions must be clearly labeled `Greek retroversion, hypothetical`. They are not manuscript witnesses and must not be weighed as equivalent to P.Oxy. 1, 654, 655, or any other extant Greek source.

Each retroversion should record a confidence level:

- `high`: strong Coptic-to-Greek recoverability and strong external controls;
- `medium`: plausible Greek form with some controls but unresolved alternatives;
- `low`: tentative aid for comparison only.

## Rights and Citation Policy

Protected modern translations are not used as the base text. Public domain or open texts may be used with source attribution. Licensed editions such as Brill / Layton should be used for verification when available, but not reproduced in full without rights clearance.

## Current Block Summary

The current reconstructed reader block covers 31 logia or cores: 1-6 ethical core, 9-10 cores, 16 core, 20, 22 core, 25-26, 31-36, 39, 41, 54, 72-73, 86, 89, 95-96, 99-100, and 107 as marked sayings. Logia 7, 8, 11, 23, 27, 37, 38, 44, 46, 55, 57, 76, 78, 79, 90, 93, 94, 103, 109, and 113 have evidence notes, cards, or cluster checks, but they are not included in the main reconstructed text because their current decision is `UNCERTAIN`, split-core pending, or too duplicative.

## Logion 1 Summary

Decision: `INCLUDE_WITH_MARKER`

Logion 1 is retained as a marked collection frame:

> Whoever finds the interpretation of these words will not taste death.

Reason: it is integral to the transmitted Greek/Coptic frame of the collection, but its function is hermeneutical and collection-level. It should not be treated as an independently secure earliest Jesus saying without further evidence.

Evidence note: `notes/logion-001-evidence-en.md`.

## Logion 2 Summary

Decision: `INCLUDE_WITH_MARKER`

The search/find core is included as a likely early or shared traditional motif:

> Let the one who seeks not stop seeking until they find.

The following sequence is retained with a marker:

> When they find, they will be disturbed; when disturbed, they will be amazed; and they will reign.

Reason: Matthew 7:7 and Luke 11:9 preserve a search/find motif, but Thomas 2 does not reproduce the full synoptic triad "ask / seek / knock." Thomas expands the search/find motif into a distinctive sequence of disturbance, amazement, reigning, and possibly rest.

Evidence note: `notes/logion-002-evidence-en.md`.

## Logion 3 Summary

Decision: `INCLUDE_WITH_MARKER`

The kingdom core is included:

> Do not seek the kingdom as a place in heaven or in the sea. The kingdom is within you and outside you.

The self-knowledge continuation is retained with a marker because it is more distinctively Thomasine and textually complex.

Synoptic evidence table: `04_Synoptic_Parallels/logion-003-luke-17-kingdom.md`.

The strongest synoptic contact is Luke 17:21, especially `ἐντὸς ὑμῶν`. The comparison supports a shared non-localized kingdom motif, but Thomas has distinctive features: heaven/sea, outside-you, and self-knowledge. Direct literary dependence is not established.

Evidence note: `notes/logion-003-evidence-en.md`.

## Logion 4 Summary

Decision: `INCLUDE_WITH_MARKER`

The first/last formula is included:

> Many who are first will become last, and the last first.

The seven-day child image and final becoming-one motif are retained only with a marker.

Synoptic evidence table: `04_Synoptic_Parallels/logion-004-first-last.md`.

The first/last core has strong formulaic parallels in Mark 10:31 and Matthew 19:30, with additional parallels in Matthew 20:16 and Luke 13:30. The broader Thomasine frame has no direct synoptic support.

Evidence note: `notes/logion-004-evidence-en.md`.

## Logion 5 Summary

Decision: `INCLUDE_WITH_MARKER`

The hidden/revealed maxim is included:

> Nothing is hidden that will not become manifest.

The "before your face" command is retained with a marker as a possible Thomasine wisdom frame.

Synoptic evidence table: `04_Synoptic_Parallels/logion-005-hidden-revealed.md`.

The hidden/revealed core has strong synoptic support, especially Luke 8:17, Matthew 10:26, and Luke 12:2. Mark 4:22 preserves the same motif in a different formulation. The "before your face" command remains marked.

Evidence note: `notes/logion-005-evidence-en.md`.

## Logion 6 Summary

Decision: `INCLUDE_WITH_MARKER` for the short ethical core; full Logion 6 remains `UNCERTAIN`.

Marked reader text:

> Do not lie, and do not do what you hate.

Reason: the extant logion combines ritual-practice questions, ethical instruction, and a hidden/revealed motif. The full unit remains a complex ritual-ethics composition and should not be added as a whole.

The short ethical core, however, has a stronger independent profile. The second clause is closely controlled by Tobit 4:15 (`καὶ ὃ μισεῖς, μηδενὶ ποιήσῃς`). The prohibition of lying has strong Jewish and early-Christian controls, especially Leviticus 19:11 and Colossians 3:9. Matthew 7:12 and Luke 6:31 preserve the positive Golden Rule form, while Didache 1:2 gives an early Christian reciprocity control closer to the negative form.

The marker remains necessary because P.Oxy. 654 is lacunose at the key phrase and the core is embedded in a complex Thomasine ritual-practice unit.

Evidence note: `notes/logion-006-evidence-en.md`.

Cluster note: `notes/ritual-ethics-cluster-006-014-027-104-en.md`.

Synoptic and early-Christian control table: `04_Synoptic_Parallels/logion-006-matthew-6-ritual-practice.md`.

Ethical-core table: `04_Synoptic_Parallels/logion-006-ethical-core.md`.

## Ritual-Ethics Cluster Summary

The control cluster covers Thomas 6, 14, 27, and 104.

Current decisions:

| Logion | Decision | Reason |
| --- | --- | --- |
| 6 | ethical core `INCLUDE_WITH_MARKER`; full logion `UNCERTAIN` | The short core has strong Jewish and early-Christian ethical controls, but the full unit is compositionally complex. |
| 14 | `DEFER` | Control unit for ritual critique, mission, food, and speech-defilement; no loaded Greek Oxyrhynchus witness. |
| 27 | `UNCERTAIN` | Complete Coptic, strong P.Oxy. 1 Greek witness, and P.Oxy. 5575 control; still excluded from the reader because it spiritualizes ritual practice and has only thematic synoptic controls. |
| 104 | `DEFER` | Strong bridegroom-fasting controls in Mark/Matthew/Luke, but no loaded Greek Oxyrhynchus witness. |

Conclusion: the full Thomas 6 composition should not be added to the main reconstructed text. The short ethical core may be added with a marker. Logion 27 has been separately deepened and moved from `DEFER` to `UNCERTAIN`, but it remains outside the reader text.

## Logion 7 Summary

Decision: `UNCERTAIN`.

Reason: the lion/human saying is symbolically dense, has no direct synoptic parallel entered at this stage, and the Greek witness is mostly reconstructed. Wider ancient parallels must be researched before inclusion.

Evidence note: `notes/logion-007-evidence-en.md`.

## Logion 8 Summary

Decision: `UNCERTAIN`.

Possible candidate:

> A wise fisher chose one large good fish from many small fish.

Reason: Thomas 8 is compact and may preserve an independent parable. Matthew 13:47-48 provides a thematic net/fish/sorting control, but the structures differ too sharply for reader inclusion. Matthew's parable concerns the kingdom and sorting good from bad; Thomas concerns a wise fisher choosing one large good fish from many small fish. No loaded Greek Thomas witness preserves Logion 8.

Evidence note: `notes/logion-008-evidence-en.md`.

Synoptic evidence table: `04_Synoptic_Parallels/logia-008-020-022-high-candidate-controls.md`.

Reconstruction implication: do not add Logion 8 to the main reader text yet.

## Logion 9 Summary

Decision: sower core `INCLUDE_WITH_MARKER`; full Logion 9 `UNCERTAIN`.

Included marked core:

> A sower went out to sow. Some seed fell on the road, some on rock, some among thorns, and some on good earth; only the good earth bore fruit.

Reason: Thomas 9 has strong synoptic controls in Mark 4:3-9, Matthew 13:3-9, and Luke 8:5-8, and it preserves the parable without the allegorical interpretation found in Mark 4:13-20, Matthew 13:18-23, and Luke 8:11-15. This supports printing the short non-allegorical core with a marker. However, no loaded Greek Oxyrhynchus witness preserves Thomas 9, and the direction of dependence remains unresolved. Distinctive Thomas details, especially the worm, fruit upward to heaven, and the `60 / 120` yield, remain outside the reader text.

Evidence note: `notes/logion-009-evidence-en.md`.

Synoptic evidence tables: `04_Synoptic_Parallels/logion-009-sower.md`; `04_Synoptic_Parallels/logion-009-sower-core-final-controls.md`.

Reconstruction implication: add only the short marked sower core to the main reader text. Any Greek form must be labeled `Greek retroversion, hypothetical`.

## Logion 10 Summary

Decision: fire-casting core `INCLUDE_WITH_MARKER`; full Logion 10 `UNCERTAIN`.

Included marked core:

> I cast fire upon the world.

Reason: Thomas 10 has a strong synoptic control in Luke 12:49, where Jesus says that he came to cast fire upon the earth. The short fire-casting core is compact and plausibly belongs to an early crisis/apocalyptic sayings tradition. However, no loaded Greek Oxyrhynchus witness preserves Thomas 10, and the Thomas continuation, "I am watching/guarding it until it blazes," differs from Luke and may be Thomasine symbolic reshaping. Thomas 16 and Thomas 82 show that fire is also part of Thomas's internal symbolic vocabulary.

Evidence note: `notes/logion-010-evidence-en.md`.

Synoptic evidence table: `04_Synoptic_Parallels/logion-010-fire-luke-control.md`.

Reconstruction implication: add only the short marked fire-casting core to the main reader text. Keep the watching/blazing continuation in the apparatus. Any Greek form must be labeled `Greek retroversion, hypothetical`.

## Logion 11 Summary

Decision: `UNCERTAIN`.

Strongest possible subunit:

> This heaven will pass away, and the one above it will pass away.

Reason: the heaven-passing motif has partial synoptic controls in Mark 13:31, Matthew 24:35, and Luke 21:33. However, the synoptic formula is "heaven and earth will pass away, but my words will not pass away," while Thomas 11 has "this heaven and the one above it" and lacks the enduring-words contrast. The rest of Thomas 11 combines dead/living paradox, eating what is dead, light language, and one/two anthropology. These belong more naturally to Thomasine symbolic development than to a secure earliest sayings layer.

Evidence note: `notes/logion-011-evidence-en.md`.

Synoptic evidence table: `04_Synoptic_Parallels/logion-011-heaven-passing-controls.md`.

Reconstruction implication: do not add Logion 11 to the main reader text yet. Any Greek form must be labeled `Greek retroversion, hypothetical`.

## Logion 16 Summary

Decision: division/household core `INCLUDE_WITH_MARKER`; full Logion 16 `UNCERTAIN`.

Included marked core:

> I did not come to bring peace, but division; a household will be divided.

Reason: Thomas 16 has strong synoptic controls in Matthew 10:34-36 and especially Luke 12:51-53. Luke is the closest structural control because of the five-in-one-house and three-against-two / two-against-three pattern. Matthew is important because Thomas includes the sword motif. However, Thomas also combines fire, sword, war, a Luke-like household structure, and a final `monachos` closure. This makes the extant form likely harmonized, developed, or Thomasine-redacted.

Evidence note: `notes/logion-016-evidence-en.md`.

Synoptic evidence table: `04_Synoptic_Parallels/logion-016-division-family.md`.

Reconstruction implication: include only the marked short division/household core in the main reader text. Do not include the fire/sword/war sequence or the monachos ending. Any Greek form must be labeled `Greek retroversion, hypothetical`.

## Logion 20 Summary

Decision: `INCLUDE_WITH_MARKER`

Possible early core:

> The kingdom is like a mustard seed: it is small, but it grows and gives shelter to the birds of heaven.

Reason: Thomas 20 has strong synoptic controls in Mark 4:30-32, Matthew 13:31-32, and Luke 13:18-19. The parable core is short, memorable, agrarian, and multiply attested. Thomas is especially close to Mark in the branch motif, while also sharing "kingdom of heaven" language with Matthew. The branch/tree follow-up strengthens the case that Thomas 20 is an important witness to a mobile parable tradition, but it does not prove Thomasine priority or independence. No loaded Greek Oxyrhynchus witness preserves Thomas 20, and the direction of dependence remains unresolved.

Evidence note: `notes/logion-020-evidence-en.md`.

Branch/tree follow-up: `notes/logion-020-branch-tree-commentary-check-en.md`.

Synoptic evidence table: `04_Synoptic_Parallels/logion-020-mustard-seed.md`.

Reconstruction implication: include Logion 20 in the main reader text with a marker. Any Greek form must be labeled `Greek retroversion, hypothetical`.

## Logion 22 Summary

Decision: children/kingdom core `INCLUDE_WITH_MARKER`; full logion `UNCERTAIN`.

Possible early core:

> Little children are like those who enter the kingdom.

Reason: the children-and-kingdom motif has strong synoptic controls in Mark 10:14-15, Matthew 18:3-4, Matthew 19:14, and Luke 18:16-17. Thomas 22 preserves a compact positive form at the start of the logion. However, the extant unit then expands into a long unity-of-opposites sequence: two become one, inside/outside, upper/lower, male/female, and eye/hand/foot/image replacement. This expansion is important for Thomasine theology, but it is not securely recoverable as the earliest gospel layer.

Evidence note: `notes/logion-022-evidence-en.md`.

Synoptic evidence table: `04_Synoptic_Parallels/logion-022-children-kingdom.md`.

Reconstruction implication: include only the short children/kingdom core in the main reader text with a marker. Keep the unity-of-opposites expansion in the apparatus. Any Greek form must be labeled `Greek retroversion, hypothetical`.

## Logion 25 Summary

Decision: `INCLUDE_WITH_MARKER`

Marked reader text:

> Love your brother as your own soul; guard him like the apple of your eye.

Reason: Thomas 25 is short, ethical, and strongly rooted in Jewish and synoptic love-command tradition. The core has strong controls in Leviticus 19:18, Mark 12:31, Matthew 22:39, and Luke 10:27. The apple-of-the-eye clause has biblical and wisdom controls in Deuteronomy 32:10, Psalm 17:8, and Proverbs 7:2. The saying remains marked because Thomas has "brother" rather than the broader "neighbor," because the second clause may be an expansion, and because no loaded Greek Thomas 25 witness is available.

Evidence note: `notes/logion-025-evidence-en.md`.

Synoptic and scriptural evidence table: `04_Synoptic_Parallels/logion-025-love-brother.md`.

Reconstruction implication: include Logion 25 in the Ukrainian reader text with a marker.

## Logion 26 Summary

Decision: `INCLUDE_WITH_MARKER`

Marked reader text:

> First remove the beam from your own eye; then you will see clearly to remove the speck from your brother's eye.

Reason: Thomas 26 has a strong evidence profile: complete Coptic Thomas, partial Greek P.Oxy. 1, and close parallels in Matthew 7:3-5 and Luke 6:41-42. The Greek witness preserves the final clause, corresponding to "then you will see clearly to remove the speck from your brother's eye." The saying remains marked because P.Oxy. 1 is fragmentary and the direction of dependence between Thomas and the synoptic tradition remains unresolved.

Evidence note: `notes/logion-026-evidence-en.md`.

Synoptic evidence table: `04_Synoptic_Parallels/logion-026-speck-beam.md`.

Reconstruction implication: include Logion 26 in the Ukrainian reader text with a marker.

## Logion 27 Summary

Decision: `UNCERTAIN`

Extant saying:

> If you do not fast from the world, you will not find the kingdom; if you do not sabbatize the Sabbath, you will not see the Father.

Reason: Thomas 27 is strongly attested as a transmitted saying. The Coptic text is complete, P.Oxy. 1 preserves the whole saying in Greek, and P.Oxy. 5575 gives an additional early control for related material in a mixed sayings environment. This makes Logion 27 important for the history of Thomas-like sayings in Greek.

The reconstruction problem is different: its key formulas have only thematic, not direct, synoptic controls. Matthew 6:16-18 regulates fasting, Mark 2:18-20 and parallels treat bridegroom-fasting, and Mark 2:23-28 with parallels treat Sabbath controversy, but none independently confirms "fast from the world" or "sabbatize the Sabbath" as an early recoverable core. The saying fits the Thomas ritual-ethics cluster and probably represents symbolic or ascetic reinterpretation of ritual practice.

Evidence note: `notes/logion-027-evidence-en.md`.

Synoptic and early-control table: `04_Synoptic_Parallels/logion-027-fasting-sabbath.md`.

Reconstruction implication: do not add Logion 27 to the main reader text. Use it in the apparatus and evidence dossier as a well-attested but reconstructionally uncertain ritual-symbolic saying.

## Logion 31 Summary

Decision: `INCLUDE_WITH_MARKER`

Marked reader text:

> A prophet is not accepted in his own homeland.

Marked paired expansion:

> Nor does a physician heal those who know him.

Reason: Thomas 31 has complete Coptic Thomas, strong Greek P.Oxy. 1, and close synoptic controls in Mark 6:4, Matthew 13:57, and Luke 4:24. The prophet-in-homeland core is a short, widely attested proverbial unit. The physician clause is preserved in Thomas and P.Oxy. 1, but its external control is weaker; Luke 4:23 provides a related physician proverb in the same context, not the same saying.

Evidence note: `notes/logion-031-evidence-en.md`.

Synoptic evidence table: `04_Synoptic_Parallels/logia-031-033-poxy1-synoptic-controls.md`.

Reconstruction implication: include Logion 31 in the Ukrainian reader text with a marker; do not treat the physician clause as equally secure as the prophet core.

## Logion 32 Summary

Decision: `INCLUDE_WITH_MARKER`

Marked reader text:

> A city built and established on a high mountain can neither fall nor be hidden.

Reason: Thomas 32 has complete Coptic Thomas, strong Greek P.Oxy. 1, and a close synoptic control in Matthew 5:14. The city-on-mountain core is strong. The fuller Thomas/P.Oxy. form, with "built/established" and "cannot fall," may preserve an independent fuller version or may be an expansion.

Evidence note: `notes/logion-032-evidence-en.md`.

Synoptic evidence table: `04_Synoptic_Parallels/logia-031-033-poxy1-synoptic-controls.md`.

Reconstruction implication: include Logion 32 in the Ukrainian reader text with a marker.

## Logion 33 Summary

Decision: `INCLUDE_WITH_MARKER`

Marked reader units:

> What you hear in your ear, proclaim from your rooftops.

> No one lights a lamp and puts it under a basket or in a hidden place; it is put on a lampstand so that its light may be seen.

Reason: Thomas 33 is composite but strongly supported at the level of its two subunits. The ear/rooftop unit has strong controls in Matthew 10:27 and Luke 12:3. The lamp/lampstand unit has strong controls in Mark 4:21, Matthew 5:15, Luke 8:16, and Luke 11:33. P.Oxy. 1 preserves only the opening of Thomas 33; therefore the lamp section has no extant Greek Thomas witness in P.Oxy. 1 and should require a marked hypothetical Greek retroversion in the Greek layer.

Evidence note: `notes/logion-033-evidence-en.md`.

Synoptic evidence table: `04_Synoptic_Parallels/logia-031-033-poxy1-synoptic-controls.md`.

Reconstruction implication: include Logion 33 in the Ukrainian reader text with a split-unit marker.

## Logion 34 Summary

Decision: `INCLUDE_WITH_MARKER`

Marked reader text:

> If a blind person leads a blind person, both fall into a pit.

Reason: Thomas 34 has complete Coptic and very strong controls in Matthew 15:14 and Luke 6:39. The saying is a short portable proverb. Thomas lacks the wider Matthean polemical frame, which may preserve a compact form or may reflect abbreviation.

Greek note: no loaded extant Greek Thomas witness preserves Logion 34. Any Greek form should be labeled `Greek retroversion, hypothetical`, controlled by Matthew and Luke.

Evidence note: `notes/logion-034-evidence-en.md`.

Synoptic evidence table: `04_Synoptic_Parallels/logia-034-035-bridge-synoptic-controls.md`.

Reconstruction implication: include Logion 34 in the Ukrainian reader text with a marker.

## Logion 35 Summary

Decision: `INCLUDE_WITH_MARKER`

Marked reader text:

> No one can enter the strong man's house and plunder it unless he first binds the strong man.

Reason: Thomas 35 has complete Coptic and strong controls in Mark 3:27 and Matthew 12:29. Luke 11:21-22 is a related but more developed form. The short strong-man image is therefore promising, though its original rhetorical setting remains unresolved.

Greek note: no loaded extant Greek Thomas witness preserves Logion 35. Any Greek form should be labeled `Greek retroversion, hypothetical`, controlled primarily by Mark and Matthew.

Evidence note: `notes/logion-035-evidence-en.md`.

Synoptic evidence table: `04_Synoptic_Parallels/logia-034-035-bridge-synoptic-controls.md`.

Reconstruction implication: include Logion 35 in the Ukrainian reader text with a marker.

## Logion 36 Summary

Decision: `INCLUDE_WITH_MARKER`

Marked reader text:

> Do not be anxious from morning until evening and from evening until morning about what you will wear.

Reason: Thomas 36 has a complete short Coptic form, an extant Greek P.Oxy. 655 witness, and strong controls in Matthew 6:25-34 and Luke 12:22-31. P.Oxy. 5575 gives an additional early control for related material in a mixed sayings environment.

The marker remains necessary because the Coptic Thomas form is short and focused on clothing, while P.Oxy. 655, Matthew/Luke, and P.Oxy. 5575 point to a broader and textually fluid complex involving food, clothing, lilies, and divine provision. Therefore the reader should print only the short anti-anxiety / clothing core.

Evidence note: `notes/logion-036-evidence-en.md`.

Synoptic evidence table: `04_Synoptic_Parallels/logia-036-039-poxy655-synoptic-controls.md`.

Reconstruction implication: include Logion 36 in the Ukrainian reader text with a marker; keep the fuller food/lilies complex in the apparatus.

## Logion 39 Summary

Decision: `INCLUDE_WITH_MARKER`

Marked reader units:

> The scribes and Pharisees took the key(s) of knowledge; they did not enter, and they did not allow those entering to enter.

> Be wise as serpents and pure as doves.

Reason: Thomas 39 has complete Coptic, Greek P.Oxy. 655, and strong synoptic controls. Luke 11:52 is especially close for the key of knowledge, not entering, and obstructing others. Matthew 23:13 gives a parallel polemical structure. Matthew 10:16 closely controls the serpent/dove saying.

The marker remains necessary because the transmitted Thomas form is composite. The two sayings should be printed as split marked units, not as one unmarked primitive composition.

Evidence note: `notes/logion-039-evidence-en.md`.

Synoptic evidence table: `04_Synoptic_Parallels/logia-036-039-poxy655-synoptic-controls.md`.

Reconstruction implication: include Logion 39 in the Ukrainian reader text with split-unit markers.

## Logion 41 Summary

Decision: `INCLUDE_WITH_MARKER`

Marked reader text:

> Whoever has will be given more; whoever does not have will lose even the little that they have.

Reason: Thomas 41 preserves a compact has/given formula with very strong synoptic controls in Mark 4:25, Matthew 13:12, Matthew 25:29, Luke 8:18, and Luke 19:26. The saying is short, aphoristic, portable, and broadly attested across different synoptic contexts. This makes it a strong candidate for early circulating tradition.

The marker remains necessary because no loaded extant Greek Thomas witness preserves Logion 41, because Thomas has distinctive "in hand" and "little" wording, and because standalone transmission may reflect either early oral form or later extraction from parabolic contexts.

Greek note: no loaded extant Greek Thomas witness preserves Logion 41. Any Greek form must be labeled `Greek retroversion, hypothetical`.

Evidence note: `notes/logion-041-evidence-en.md`.

Synoptic evidence table: `04_Synoptic_Parallels/logion-041-has-given-controls.md`.

Reconstruction implication: include Logion 41 in the Ukrainian reader text with a marker; do not treat the hypothetical Greek retroversion as manuscript evidence.

## Logion 54 Summary

Decision: `INCLUDE_WITH_MARKER`

Marked reader text:

> Blessed are the poor, for the kingdom of heaven belongs to you.

Reason: Thomas 54 is one of the shortest and strongest beatitude candidates in the current reconstruction. Luke 6:20 closely controls the direct address to the poor and the "yours" form, while Matthew 5:3 controls the kingdom-of-heaven wording. The compact poor/kingdom beatitude plausibly belongs to an early shared beatitude tradition.

The marker remains necessary because Thomas appears to stand between Lukan and Matthean forms: "poor" is closer to Luke, while "kingdom of heaven" is closer to Matthew. This may reflect shared tradition, secondary harmonization, Coptic transmission, or Thomasine wording. Direction of dependence remains unresolved.

Greek note: no loaded extant Greek Thomas witness preserves Logion 54. Any Greek form must be labeled `Greek retroversion, hypothetical`.

Evidence note: `notes/logion-054-evidence-en.md`.

Synoptic evidence table: `04_Synoptic_Parallels/logion-054-blessed-poor-controls.md`.

Reconstruction implication: include Logion 54 in the Ukrainian reader text with a marker; a shorter early core may be "Blessed are the poor, for yours is the kingdom."

## Logion 72 Summary

Decision: `INCLUDE_WITH_MARKER`

Marked reader text:

> A man asked Jesus to make his brothers divide the father's property with him. Jesus refused the role of divider and asked, "Am I a divider?"

Reason: Thomas 72 and Luke 12:13-15 share a distinctive inheritance-dispute scene. In both, a man asks Jesus to intervene in a family inheritance matter, and Jesus refuses the role of judge or divider. The scene is concrete, socially plausible, and not dependent on later ecclesial doctrine. Thomas preserves a compact version that may represent an extracted or shorter refusal saying.

The marker remains necessary because Luke is the only major synoptic control currently entered, and literary direction remains unresolved. Luke may expand a short refusal saying into an anti-greed discourse, or Thomas may abbreviate Luke's scene.

Greek note: no loaded extant Greek Thomas witness preserves Logion 72. Any Greek form must be labeled `Greek retroversion, hypothetical`.

Evidence note: `notes/logion-072-evidence-en.md`.

Synoptic evidence table: `04_Synoptic_Parallels/logion-072-inheritance-dispute-controls.md`.

Reconstruction implication: include Logion 72 in the Ukrainian reader text with a marker; keep Luke-dependence as an explicit warning in the apparatus.

## Logion 73 Summary

Decision: `INCLUDE_WITH_MARKER`

Marked reader text:

> The harvest is great, but the workers are few. Ask the Lord to send workers into the harvest.

Reason: Thomas 73 preserves the short harvest/workers formula also known from Matthew 9:37-38 and Luke 10:2. The saying is compact, memorable, and mission-oriented, with weak Thomasine secondary markers. Its broad early mission setting makes it a strong candidate for circulating Jesus-tradition, even though its precise Sitz im Leben remains open.

The marker remains necessary because no loaded extant Greek Thomas witness preserves Logion 73, and the wording of "Lord" / "Lord of the harvest" requires careful Greek retroversion control.

Greek note: no loaded extant Greek Thomas witness preserves Logion 73. Any Greek form must be labeled `Greek retroversion, hypothetical`.

Evidence note: `notes/logion-073-evidence-en.md`.

Synoptic evidence table: `04_Synoptic_Parallels/logion-073-harvest-workers-controls.md`.

Reconstruction implication: include Logion 73 in the Ukrainian reader text with a marker; use the Matthew/Luke control table to refine any later Greek retroversion.

## Thomas Unity / Monachos Cluster Summary

Decision rule: unity / monachos language should be treated as a Thomasine theological marker unless it is supported by independent controls.

Cluster note: `notes/thomas-unity-monachos-cluster-en.md`.

Relevant logia: 4, 11, 16, 22, 23, 37, 49, 75, 106, with Logion 30 as a Greek P.Oxy. 1 control.

Implication for Logion 22: the children/kingdom core remains promising, but the "make the two one" expansion should remain in the apparatus.

Implication for Logion 23: the logion is now `UNCERTAIN`; it should not enter the reader text. Its "one from a thousand / two from ten thousand / stand as one" pattern may reflect Thomasine elect/solitary identity language rather than a secure earliest saying.

Next test case: Logion 16, because it has a strong synoptic division core plus a probable Thomasine monachos ending.

## Logion 86 Summary

Decision: `INCLUDE_WITH_MARKER`

Marked reader text:

> Foxes have holes, birds have nests, but the Son of Man has nowhere to lay his head.

Reason: the aphoristic core is strongly controlled by Matthew 8:20 and Luke 9:58. Thomas preserves the saying outside the narrative following context, which may reflect a sayings-collection form or secondary decontextualization.

Greek note: no loaded extant Greek Thomas witness preserves Logion 86. Any Greek form must be labeled `Greek retroversion, hypothetical`.

Evidence note: `notes/logion-086-evidence-en.md`.

Synoptic evidence table: `04_Synoptic_Parallels/logion-086-foxes-birds-son-of-man-controls.md`.

## Logion 89 Summary

Decision: `INCLUDE_WITH_MARKER`

Marked reader text:

> Why do you clean the outside of the cup? Do you not understand that the one who made the inside also made the outside?

Reason: Luke 11:39-40 strongly controls the maker-of-inside/outside argument, while Matthew 23:25-26 controls the cup and inside/outside motif. The reader prints the compact critique, but the Luke-dependence warning remains.

Greek note: no loaded extant Greek Thomas witness preserves Logion 89. Any Greek form must be labeled `Greek retroversion, hypothetical`.

Evidence note: `notes/logion-089-evidence-en.md`.

Synoptic evidence table: `04_Synoptic_Parallels/logion-089-cup-inside-outside-controls.md`.

## Logion 95 Summary

Decision: `INCLUDE_WITH_MARKER`

Marked reader text:

> If you have money, do not lend at interest; give to the one from whom you do not expect to receive it back.

Reason: the saying combines Jewish anti-usury tradition with the radical non-repayment motif controlled by Luke 6:34-35. It is ethically coherent with the reconstruction, especially Logion 6, but remains marked because the Coptic opening is damaged and the combination may be secondary.

Greek note: no loaded extant Greek Thomas witness preserves Logion 95. Any Greek form must be labeled `Greek retroversion, hypothetical`.

Evidence note: `notes/logion-095-evidence-en.md`.

Synoptic/control table: `04_Synoptic_Parallels/logion-095-money-lending-controls.md`.

## Logion 96 Summary

Decision: leaven core `INCLUDE_WITH_MARKER`; full Logion 96 `UNCERTAIN`.

Marked reader text:

> The kingdom is like a woman who took a little leaven and hid it in dough.

Reason: the leaven parable core is strongly controlled by Matthew 13:33 and Luke 13:20-21. The Thomas-specific Father frame, large-loaves result, and hearing formula remain outside the clean reader.

Greek note: no loaded extant Greek Thomas witness preserves Logion 96. Any Greek form must be labeled `Greek retroversion, hypothetical`.

Evidence note: `notes/logion-096-evidence-en.md`.

Synoptic evidence table: `04_Synoptic_Parallels/logion-096-leaven-controls.md`.

## Logion 99 Summary

Decision: true-family core `INCLUDE_WITH_MARKER`; full Logion 99 `UNCERTAIN`.

Marked reader text:

> Those who do the Father's will are my brothers and my mother.

Reason: Mark 3:31-35, Matthew 12:46-50, and Luke 8:19-21 strongly control the true-family core. The family-outside narrative frame and Thomas's kingdom-of-the-Father ending remain outside the clean reader.

Greek note: no loaded extant Greek Thomas witness preserves Logion 99. Any Greek form must be labeled `Greek retroversion, hypothetical`.

Evidence note: `notes/logion-099-evidence-en.md`.

Synoptic evidence table: `04_Synoptic_Parallels/logion-099-true-family-controls.md`.

## Logion 100 Summary

Decision: Caesar/God core `INCLUDE_WITH_MARKER`; full Logion 100 `UNCERTAIN`.

Marked reader text:

> Give Caesar what belongs to Caesar, and God what belongs to God.

Reason: the Caesar/God core is strongly controlled by Mark 12:13-17, Matthew 22:15-22, and Luke 20:20-26. The Thomas-specific third clause, "give me what is mine," remains outside the clean reader.

Greek note: no loaded extant Greek Thomas witness preserves Logion 100. Any Greek form must be labeled `Greek retroversion, hypothetical`.

Evidence note: `notes/logion-100-evidence-en.md`.

Synoptic evidence table: `04_Synoptic_Parallels/logion-100-caesar-god-controls.md`.

## Logion 107 Summary

Decision: lost-sheep core `INCLUDE_WITH_MARKER`; full Logion 107 `UNCERTAIN`.

Marked reader text:

> A shepherd had one hundred sheep. One of them went astray; he left the ninety-nine and searched for it until he found it.

Reason: the lost-sheep parable core is strongly controlled by Matthew 18:12-14 and Luke 15:3-7. Thomas's "largest sheep" and "I love you more" elements likely reshape the parable around the singular one and remain outside the clean reader.

Greek note: no loaded extant Greek Thomas witness preserves Logion 107. Any Greek form must be labeled `Greek retroversion, hypothetical`.

Evidence note: `notes/logion-107-evidence-en.md`.

Synoptic evidence table: `04_Synoptic_Parallels/logion-107-lost-sheep-controls.md`.
