# P.Oxy. XML Extraction Audit v0.1

Статус: виконаний source-critical cleanup pass, 2026-07-17.

## Мета

Цей прохід закрив видимий card-level борг `pending local line extraction` для P.Oxy. 1 і P.Oxy. 655 у восьми картках логій.

Головний принцип: XML-витяг має робити джерельний шар чеснішим, а не створювати ілюзію певності. Тому extant letters, lacunae, supplied text і невпевнені ототожнення залишено видимими.

## Source Files

- `sources/primary_texts/greek_poxy/dclp-poxy1-62838.xml`
- `sources/primary_texts/greek_poxy/dclp-poxy655-62839.xml`

Обидва файли походять із DCLP / Papyri.info TEI/EpiDoc XML і в source register позначені як умовно перевірені відкриті робочі джерела.

## Updated Cards

| Logion | Papyrus | Result | Use Policy |
| ---: | --- | --- | --- |
| 24 | P.Oxy. 655 | Pending marker removed; no card-ready Greek witness to the Coptic light saying was found. | Do not cite P.Oxy. 655 as direct Greek support for Logion 24; keep only as uncertain catalogue-level association. |
| 27 | P.Oxy. 1 | Greek extract added from verso lines 5-11. | Direct Greek manuscript support for fasting-from-world / Sabbath-Sabbath unit. |
| 28 | P.Oxy. 1 | Partial Greek extract added from verso lines 11-21. | Direct but incomplete support for incarnation/world/drunkenness/blind-heart core. |
| 29 | P.Oxy. 1 | Tiny final-fragment extract added from recto line 1. | Minimal support for the final poverty clause only. |
| 30 | P.Oxy. 1 | Damaged Greek extract added from recto lines 2-6. | Direct but textually complex support for the three/one divine-presence unit; keep separate from 77b. |
| 37 | P.Oxy. 655 | Greek extract added from column i lines 17-23. | Direct support for the shorter appearance/undressing core only. |
| 38 | P.Oxy. 655 | Heavily restored Greek extract added from column ii lines 2-11. | Fragmentary control for seek/not-find saying; most continuity is supplied. |
| 77 | P.Oxy. 1 | Greek extract added from recto lines 6-9. | Direct support only for the stone/wood presence unit, not for full Logion 77. |

## Extraction Notes

### P.Oxy. 1

The DCLP title identifies the text as Thomas 26-30, 77b, 31-33. The relevant pending cards were 27, 28, 29, 30 and 77.

- Logion 27 is the strongest of this set: the fasting/Sabbath unit is continuous enough for card-level citation.
- Logion 28 is meaningful but incomplete: it preserves the world/flesh/drunkenness/blind-heart core, but the ending is lost or damaged.
- Logion 29 has only a tiny overlap, apparently the final poverty phrase.
- Logion 30 is damaged and compositionally complex because the text moves directly into the 77b stone/wood unit.
- Logion 77 is attested only for the 77b stone/wood unit, not for the whole Coptic logion.

### P.Oxy. 655

The DCLP title identifies the text as Thomas 24(?), 36-39. The pending cards were 24, 37 and 38.

- Logion 24 remains uncertain: the XML does not provide a responsible line-level Greek equivalent of the Coptic light/person-of-light saying.
- Logion 37 has a clear shorter Greek form of the question and undressing answer.
- Logion 38 is present but heavily restored; cite it only as fragmentary/reconstructed.

## Methodological Policy

- Square brackets in card extracts mark supplied/lost text or damaged continuity.
- The extracts are working card-level transcriptions, not final critical editions.
- DCLP normalized forms may be used for readability when the XML places original forms in `<orig>` and normalized forms in `<reg>` or lemma text.
- No Greek extract from this pass should be promoted into the clean reader by itself.
- Any inclusion/exclusion decision must still pass through the all-114 publication decision table.

## Remaining Source-Critical Work

The specific `pending local line extraction` gap is now closed for the eight targeted cards.

Remaining source-critical work is different in kind:

1. verify the extracts against Grenfell & Hunt / Attridge / Layton or another academic control;
2. decide how much of P.Oxy. 655 Logion 38 should be treated as extant vs supplied;
3. create a dedicated evidence note for Thomas 24(?) / P.Oxy. 655;
4. carry the updated Greek status into the true all-114 publication decision table.

