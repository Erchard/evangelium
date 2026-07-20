# Publication Gap Audit v0.2

Статус: робочий аудит прогалин v0.3, актуалізовано 2026-07-18.

## Мета аудиту

Цей документ відповідає на питання: що саме треба підтягнути, щоб проект став не просто робочою реконструкцією, а якісним виданням, яке можна показувати читачам і давати на зовнішню перевірку.

## Уже створені активи

| Актив | Стан |
| --- | --- |
| 114 карток логій | Є |
| Вирівнювання карток до еталонного стандарту | Є, 114/114 мають `Gold-level status check v0.2` |
| Clean Ukrainian reader | Є, 37 логій / ядер |
| English reader layer | Є для 37 логій / ядер |
| Coptic layer | Є для 37 логій / ядер |
| Greek layer | Є для 37 логій / ядер; confidence audit v0.1 оновлено |
| Parallel edition | Є, 37 рядків |
| Evidence dossier | Є, publication-facing draft v1.4; bibliography/rights/citation release layer оновлено |
| Bibliography / rights / citation / reproducibility | Release verification v0.2 виконано; protected controls обмежено |
| Ritual-ethics / bridegroom 104A | Закрито: 104A `APPENDIX_ONLY_STABLE`, clean reader без змін |
| All-114 publication decision table | Є, v0.1; `NEEDS_EVIDENCE_BEFORE_FINAL` = 0 |
| Final all-114 decision audit | Є, v0.1 |
| Full 114-logion appendix | Є для всіх 114; усі секції мають читацьке пояснення; Logia 1-114 editorially consolidated |
| Card quality audit | Є, актуальний файл `corpus/cards/card-quality-audit-v0.2.md` |
| Five-source card apparatus | Є, актуальний файл `corpus/cards/five-source-apparatus-audit-v0.1.md` |
| Print/digital publication architecture | Є, v0.1; separate Ukrainian/English paper books plus digital scholarly companion |
| Collection log | Є |

## Головні прогалини

### 1. High-candidate логії ще не закриті

Найбільший ризик: ми можемо передчасно вважати склад clean reader стабільним.

Перший пакет для поглиблення завершено як Sprint A evidence/control pass:

- 44 - blasphemy-Spirit controls;
- 46 - John the Baptist / least in kingdom;
- 55 - radical discipleship and cross;
- 57 - weeds among wheat;
- 76 - pearl / imperishable treasure;
- 78 - wilderness / reed / soft clothing;
- 79 - womb / hearing the word.

Після final high-candidate decision pass логії 86, 89, 95 і 96 увійшли до clean reader з маркером або як ядра; 90, 93 і 94 залишаються поза clean reader, але мають evidence notes і control files.

Другий пакет для поглиблення завершено як Sprint B evidence/control pass:

- 86 - foxes / birds / Son of Man homelessness;
- 89 - cup inside/outside;
- 90 - yoke and rest;
- 93 - holy things / dogs and pearls / swine;
- 94 - seek/find and knock/open;
- 95 - money, interest, and non-repayment;
- 96 - leaven parable.

Усі ці логії залишаються поза clean reader, але тепер мають evidence notes і control files.

Третій пакет для поглиблення завершено як Sprint C evidence/control pass:

- 99 - true family;
- 100 - Caesar/God tribute saying;
- 103 - thief/watchfulness;
- 107 - lost sheep;
- 109 - hidden treasure;
- 113 - kingdom not observed / not here-or-there.

Після final high-candidate decision pass логії 99, 100 і 107 увійшли до clean reader як ядра; 103, 109 і 113 залишаються поза clean reader, але мають evidence notes і control files.

Усі planned high-candidate packages A/B/C тепер мають evidence notes і control files.

### 2. Source text visibility is improved; pending P.Oxy. extracts are now closed

Усі 114 карток тепер мають `Five-source original-language apparatus v0.1`, тобто P.Oxy. 1 / 654 / 655, коптський NHC II і canonical Greek control channel видимі прямо в картці.

Canonical Greek extraction pass заповнив SBLGNT controls для 81 картки. P.Oxy. XML extraction cleanup v0.1 закрив попередній pending gap:

- `corpus/cards/poxy-xml-extraction-audit-v0.1.md`;
- P.Oxy. 1: логії 27, 28, 29, 30, 77;
- P.Oxy. 655: логії 24, 37, 38.

Наступний source-critical крок уже не extraction і не базове Greek-label polish: publication-facing Greek status нормалізовано, а bibliography/rights verification виконано. Перед публікацією лишається proof/render preparation і фінальна звірка витягів з академічними виданнями там, де будуть page-specific critical claims.

### 3. Evidence notes and control files are no longer the main blocking gap

Картки є для всіх 114 логій і всі мають gold-level status check v0.2. Evidence/control inventory і all-114 publication decision table виконані; після evidence-rationale packages `NEEDS_EVIDENCE_BEFORE_FINAL` зведено до 0.

Потрібно вже не масово створювати missing notes, а довести наявний апарат до publication quality:

- вирівняти глибину evidence dossier;
- перевірити bibliography і source provenance;
- перенести ключові аргументи в print-safe appendix prose;
- залишити повні repo paths і audit trail у digital scholarly companion.

### 4. Full appendix exists for all 114 logia and is now editorially consolidated

Файл `reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-uk.md` уже дуже корисний, але це ще не фінальний коментар.

Він має 114/114 секцій із читацьким поясненням. Logia 1-114 уже редакційно консолідовані в цілісний коментар без окремих card-derived blocks і без working-index prose. У прозі для читача більше не треба покладатися на клікабельні repo links як єдиний апарат.

Потрібно продовжити перетворювати решту розділів на читацький коментар:

- короткий сенс;
- джерела;
- паралелі;
- можливі тлумачення;
- непевності;
- причина включення або невключення.

### 5. Greek retroversion confidence needs final publication polish

Проект правильно маркує `Greek retroversion, hypothetical`, і створено `reconstruction/earliest-sayings-gospel/greek-retroversion-confidence-audit-v0.1.md`. Перед публікацією ще потрібно:

- звірити ретроверсії з академічними виданнями;
- вирівняти confidence labels;
- не допустити, щоб ретроверсії виглядали як рукописні свідки.

### 6. Evidence dossier is now publication-facing, but source safety is not final

`evidence-dossier-en.md` уже має publication-facing draft v1.4:

- thesis and scope;
- source hierarchy;
- reconstruction method;
- clean-reader selection principles;
- Greek witness / retroversion policy;
- probability versus reader-decision control;
- cluster summaries;
- major appendix-only and exclusion cases;
- explicit uncertainty model.

Тепер головний борг цього шару - не структура dossier, а source-safety pass:

- повна бібліографія;
- rights/citation notes;
- print-safe citation keys;
- source snapshots;
- reproducibility notes.

### 7. All-114 publication table exists, but still needs final freeze pass

All-114 publication decision table v0.1 уже існує, але перед фінальною книгою потрібен freeze pass для всіх 114 логій або підодиниць:

- decision;
- reader status;
- confidence;
- main reason;
- evidence note;
- Greek status;
- appendix status.

Final all-114 decision audit v0.1 і all-114 publication decision table v0.1 уже створено. `inclusion-decisions-table.md` лишається корисним старішим робочим документом, але головний контрольний документ тепер all-114 publication decision table.

### 8. Reader-facing introduction and print-safe framing are still missing

Потрібен український вступ, який пояснить:

- що саме реконструюється;
- чому за основу взято Фому;
- чому не всі логії входять;
- що означає "найдавніше";
- чим реконструкція відрізняється від перекладу;
- як читати clean text і appendix.

## Ризики для якості

| Ризик | Наслідок | Як зменшити |
| --- | --- | --- |
| Передчасно зафіксувати 37 логій/ядер як фінальний корпус | Можна пропустити суперечності в остаточних all-114 рішеннях | All-114 publication decision table v0.1 виконано; clean-reader freeze робити тільки після appendix/evidence rationale polish |
| Гіпотетичний грецький текст сприймуть як свідок | Методологічна помилка | Greek retroversion confidence audit |
| Full appendix лишиться нерівним робочим текстом | Закрито: Logia 1-114 editorially consolidated | Підтримувати під час фінальної верстки |
| Greek retroversion labels будуть нерівними між шарами | CLOSED: publication polish normalized Greek witness labels across the main public-facing Greek layers | Monitor during book generation proof QA |
| Print/digital proof layer лишиться неперевіреним | Важко безпечно генерувати паперову й цифрову версії | Print / digital render proof preparation before release |
| Рішення включення не синхронізовані між файлами | Плутанина у фінальному виданні | Final decision audit |

## Рекомендований порядок наступних дій

1. Generator-ready Ukrainian and English book source packages.
2. Digital scholarly companion manifest.
3. Print / digital render proof preparation and source snapshot stabilization.
4. Print/digital proof QA.

## Publication-ready criteria

### Publication-ready logion

A logion is publication-ready when it has:

- card;
- Coptic source reference;
- Greek witness status;
- decision;
- confidence;
- evidence note or explicit reason why no note is needed;
- synoptic/control references where relevant;
- reader-commentary section;
- appendix section;
- Greek retroversion confidence if applicable.

### Publication-ready clean reconstruction

The clean reconstruction is ready when:

- final included set is fixed;
- no statuses, brackets, comments, or warnings remain in the clean text;
- numbering follows the standard Gospel of Thomas numbering;
- every included unit has support in apparatus, dossier, and appendix.

### Publication-ready full appendix

The appendix is ready when all 114 logia have:

- clear explanation;
- sources and Greek status;
- parallels;
- possible interpretations;
- inclusion or exclusion rationale;
- next uncertainty, if any.

### Publication-ready evidence dossier

The dossier is ready when it can be read independently by an external reviewer and contains:

- method;
- source hierarchy;
- rights policy;
- logion-by-logion argument;
- bibliography;
- transparent uncertainty model;
- no unsupported claims about Greek witnesses.

## Practical conclusion

The project is no longer in the "build the corpus" phase. It is now in the "defend and refine the reconstruction" phase.

The most valuable immediate work is now print / digital render proof preparation. Reviews A/B/C, the controlled clean-reader candidate passes, all-114 publication decision table, evidence-rationale packages, reader-interpretation sync, print/digital architecture, full appendix consolidation, wealth/renunciation cluster-control, Logion 114 exclusion rationale, the evidence dossier publication pass, the bibliography/rights/citation/reproducibility pass, final bibliography / rights verify, the 104A follow-up, Greek retroversion publication polish, final clean-reader freeze, and generator-ready book source packages have stabilized the reader-facing, argument, source-safety, and production-source layers. The project now needs proof-level preparation before rendering and final QA.
