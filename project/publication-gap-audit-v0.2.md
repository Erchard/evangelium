# Publication Gap Audit v0.2

Статус: робочий аудит прогалин v0.3, актуалізовано 2026-07-18.

## Мета аудиту

Цей документ відповідає на питання: що саме треба підтягнути, щоб проект став не просто робочою реконструкцією, а якісним виданням, яке можна показувати читачам і давати на зовнішню перевірку.

## Уже створені активи

| Актив | Стан |
| --- | --- |
| 114 карток логій | Є |
| Вирівнювання карток до еталонного стандарту | Є, 114/114 мають `Gold-level status check v0.2` |
| Clean Ukrainian reader | Є, 34 логії / ядра |
| English reader layer | Є для 34 логій / ядер |
| Coptic layer | Є для 34 логій / ядер |
| Greek layer | Є для 34 логій / ядер; confidence audit v0.1 оновлено |
| Parallel edition | Є, 34 рядки |
| Evidence dossier | Є, робочий v1.3; потребує publication pass |
| All-114 publication decision table | Є, v0.1; `NEEDS_EVIDENCE_BEFORE_FINAL` = 0 |
| Final all-114 decision audit | Є, v0.1 |
| Full 114-logion appendix | Є для всіх 114; усі секції мають читацьке пояснення; Logia 1-60 editorially consolidated, Logia 61-114 pending consolidation |
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

Наступний source-critical крок уже не extraction, а звірка цих витягів з академічними виданнями й перенесення уточненого Greek status у all-114 publication decision table.

### 3. Evidence notes and control files are no longer the main blocking gap

Картки є для всіх 114 логій і всі мають gold-level status check v0.2. Evidence/control inventory і all-114 publication decision table виконані; після evidence-rationale packages `NEEDS_EVIDENCE_BEFORE_FINAL` зведено до 0.

Потрібно вже не масово створювати missing notes, а довести наявний апарат до publication quality:

- вирівняти глибину evidence dossier;
- перевірити bibliography і source provenance;
- перенести ключові аргументи в print-safe appendix prose;
- залишити повні repo paths і audit trail у digital scholarly companion.

### 4. Full appendix exists for all 114 logia, but still needs editorial consolidation

Файл `reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-uk.md` уже дуже корисний, але це ще не фінальний коментар.

Він має 114/114 секцій із читацьким поясненням. Logia 1-60 уже редакційно консолідовані в цілісний коментар без окремих card-derived blocks. Logia 61-114 ще потребують такого самого проходу, тепер уже за print-safe rule: у прозі для читача не покладатися на клікабельні repo links.

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

### 6. Evidence dossier is useful, but not final

`evidence-dossier-en.md` уже має сильний каркас, але потребує publication pass:

- єдиний формат для всіх included logia;
- summary для excluded/deferred high-impact logia;
- повна бібліографія;
- methodological introduction;
- rights/citation notes;
- explicit uncertainty model.

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
| Передчасно зафіксувати 34 логії як фінальний корпус | Можна пропустити суперечності в остаточних all-114 рішеннях | All-114 publication decision table v0.1 виконано; clean-reader freeze робити тільки після appendix/evidence rationale polish |
| Гіпотетичний грецький текст сприймуть як свідок | Методологічна помилка | Greek retroversion confidence audit |
| Full appendix лишиться нерівним робочим текстом | Читач побачить шви між картками, notes і коментарем | Продовжувати print-safe editorial consolidation пакетами |
| Evidence dossier лишиться робочим | Важко захистити реконструкцію зовні | Publication pass + bibliography |
| Рішення включення не синхронізовані між файлами | Плутанина у фінальному виданні | Final decision audit |

## Рекомендований порядок наступних дій

1. Print-safe full appendix editorial consolidation, continuing with Logia 61-70.
2. Wealth/renunciation cluster-control pass.
3. Logion 114 publication-level exclusion rationale.
4. Evidence dossier publication pass.
5. Greek retroversion publication polish against academic editions.
6. Bibliography, rights, indexes, and final print/digital generation pass.

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

The most valuable immediate work is now print-safe full appendix editorial consolidation, continuing with Logia 61-70. Reviews A/B, the controlled clean-reader candidate pass, all-114 publication decision table, evidence-rationale packages, reader-interpretation sync, and print/digital architecture have stabilized the control layer; the project now needs a consistent book-ready appendix before clean-reader freeze and evidence dossier publication pass.
