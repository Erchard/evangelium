# Дорожня карта завершення проєкту

Статус: оновлена робоча дорожня карта v0.3, 2026-07-18.

## Мета

Довести проєкт до публікаційно придатного результату:

- чистий український текст реконструкції найдавнішого досяжного євангелія висловів;
- український повний коментований додаток до всіх 114 логій;
- коптський шар свідків;
- грецький шар із чітким розрізненням extant Greek і `Greek retroversion, hypothetical`;
- англійський читацький текст;
- англомовний evidence dossier;
- прозора таблиця рішень для кожної логії або підодиниці;
- бібліографія, права, джерельна ієрархія і методологічний вступ.

## Поточна оцінка стану

Орієнтовна готовність: 74-76%.

Це вже не початковий корпусний етап. Найскладніший хаос знято: корпус покритий повністю, є метод, є чистий reader, є багатомовні шари для поточної реконструкції, є evidence dossier і є каркас повного 114-логійного додатку.

Водночас проект ще не готовий до публікації, бо багато матеріалу існує як робочий каркас, а не як фінально аргументований коментар або академічний апарат.

## Що вже зроблено

| Напрям | Поточний стан |
| --- | --- |
| Структура проєкту | Є |
| Специфікація кінцевого продукту | Є |
| Принцип clean reader first | Є |
| Принцип повного додатку до 114 логій | Є |
| Повний робочий коптський текст | Є |
| P.Oxy. 1 / 654 / 655 у локальному корпусі | Є |
| Метод і рубрика оцінювання | Є |
| Еталонна картка | Logion 2 |
| Приклад картки для складеної логії | Logion 6 |
| Картки 114 логій | Є |
| Вирівнювання якості всіх карток | Є, 114/114 мають `Gold-level status check v0.2` |
| Пʼятиджерельний апарат у картках | Є, 114/114 мають `Five-source original-language apparatus v0.1`; canonical Greek заповнено для 81 картки; pending P.Oxy. XML extraction gap закрито |
| Читацьке тлумачення в картках | Є, 114/114 мають окремий український розділ із простим сенсом, можливими прочитаннями, реконструкційним значенням і застереженням |
| Чистий український reader | 37 логій / ядер |
| Англійський reader | Є для 37 логій / ядер |
| Коптський шар | Є для 37 логій / ядер |
| Грецький шар | Є для 37 логій / ядер; confidence audit v0.1 оновлено |
| Паралельне видання | 37 рядків поточного reader |
| Evidence dossier | Робочий v1.3 |
| Print/digital publication architecture | Є, v0.1 |
| Повний додаток до 114 логій | Є для всіх 114; усі секції мають читацьке пояснення; Logia 1-60 уже редакційно консолідовані, Logia 61-114 ще потребують інтеграції card-derived blocks і усунення дублювань |
| Structural QA baseline | Є: `tools/qa_crosscheck.py` перевіряє 114 карток, 114 appendix-секцій, синхронізацію clean-reader шарів і точні appendix anchors |
| Cluster-control notes | Розпочато; living/dead/world, beatitudes, seek/find, family-renunciation і fire/kingdom passes v0.1 виконано |
| Inclusion decisions table | Є як робоча таблиця; all-114 publication decision table v0.1 створено як головний контрольний документ перед appendix/dossier polish |
| Open-task prompt queue | Є: `project/open-task-prompt-queue-2026-07-18.md`; поточний `NEXT` - appendix editorial consolidation Logia 61-70 |

## Поточний склад clean reader

У чистому українському тексті зараз 37 логій або ядер:

1, 2, 3, 4, 5, 6, 9, 10, 16, 20, 22, 25, 26, 31, 32, 33, 34, 35, 36, 39, 41, 45A, 46A, 47B, 54, 63, 72, 73, 86, 89, 91A, 95, 96, 99, 100, 103A, 107.

Цей список не є фінальним. Його можуть змінити high-candidate deepening passes.

## Основні прогалини

1. Найбільша поточна прогалина - повний 114-логійний додаток уже синхронізований із картковим читацьким шаром 114/114, але ще не доведений до єдиного print-safe публікаційного формату: треба прибрати дублювання, вирівняти стиль, додати бібліографічні привʼязки й відділити друковані посилання від digital-only paths.
2. Cluster-control notes для deferred-груп суттєво просунуті: living/dead/world, beatitudes, seek/find, family-renunciation і fire/kingdom уже виконано, але wealth/renunciation ще треба закрити.
3. Evidence dossier ще не є публікаційним академічним документом.
4. Паперова й цифрова архітектура тепер зафіксована: наступні редакційні проходи мають писатися print-safe, щоб українська й англійська книги не залежали від клікабельних repo links.
5. Canonical Greek control layer суттєво покращено: 81 картка має SBLGNT Greek controls, 33 не мають локально виписаного canonical Greek text через відсутність явного reference або відсутність потреби в синоптичному контролі.
6. Pending P.Oxy. XML extraction gap закрито для логій 24, 27, 28, 29, 30, 37, 38 і 77; тепер потрібна звірка цих витягів з академічними виданнями.
7. All-114 publication decision table v0.1 покриває всі 114 логій; після Package B evidence-rationale pass `NEEDS_EVIDENCE_BEFORE_FINAL` зведено до 0; пʼять cluster-control груп уже мають контрольні документи.
8. Greek retroversion layer має confidence audit v0.1, але перед публікацією потрібна фінальна редакція й перевірка проти академічних видань.
9. Bibliography / rights / citation policy існують як принципи, але ще не як фінальний апарат.
10. Методологічний вступ для читача і англомовний methodological introduction ще треба написати.
11. Probability-pressure review виконано. Logion 1 frame-status review також виконано. Split-core / high-early pressure Review C і controlled reader-candidate pass 46A/91A виконано: 46A та 91A додано до clean reader як марковані ядра, 90 лишено appendix-only.
12. Thief/watchfulness cluster-control для Logia 21/103 виконано: 103A додано до clean reader як марковане ядро; повні Logia 21 і 103 лишаються appendix-only.

Поточні технічні борги після technical-debt closure pass закрито на рівні структурного контролю: `python3 tools/qa_crosscheck.py` проходить і має запускатися перед/після великих редакційних пакетів.

## Фаза 1. High-Candidate Deepening

Мета: поглибити логії, які ще можуть змінити склад реконструкції.

Перший список, Sprint A, уже має evidence/control pass:

- 44, 46, 55, 57, 76, 78, 79;

Ці логії залишаються поза clean reader, але тепер мають evidence notes і control files.

Другий список, Sprint B, уже має evidence/control pass:

- 86, 89, 90, 93, 94, 95, 96;

Третій список, Sprint C, уже має evidence/control pass:

- 99, 100, 103, 107, 109, 113.

Вихідні критерії:

- для кожної логії є evidence note або чітке обґрунтування, чому вона не потрібна;
- створено або оновлено synoptic/control files;
- рішення `INCLUDE_WITH_MARKER`, `UNCERTAIN`, `DEFER` або `EXCLUDE_AS_SECONDARY` уточнене;
- якщо є можливе раннє ядро, воно відділене від пізнішого розгортання.

## Фаза 2. Evidence and Control Gap Closure

Мета: закрити розрив між картками, evidence notes і control files.

Вихідні критерії:

- кожна включена логія має evidence note;
- кожна high-candidate невключена логія має evidence note або documented reason for no note;
- кожна логія зі strong synoptic control має окремий control file або посилання на cluster file;
- workflow matrix, card-quality audit і appendix skeleton не суперечать одне одному.

Стан після evidence-rationale packages: усі 114 карток мають однаковий поточний status block; evidence/control inventory виконано, direct evidence-note coverage піднято до 91 логії, а `NEEDS_EVIDENCE_BEFORE_FINAL` у all-114 publication decision table зведено до 0.

## Фаза 3. Final Decision Audit

Мета: сформувати остаточну таблицю рішень.

Файл:

- `reconstruction/earliest-sayings-gospel/inclusion-decisions-table.md`

Вихідні критерії:

- покрито всі 114 логій або підодиниці;
- вказано decision, confidence, main reason, evidence file, reader status;
- для часткових логій окремо позначено раннє ядро і повну форму;
- `Greek retroversion, hypothetical` не змішується з extant Greek witness.

## Фаза 4. Clean Reader Finalization

Мета: після high-candidate deepening зафіксувати фінальний склад чистої реконструкції.

Вихідні критерії:

- чистий український текст містить тільки пронумеровані логії;
- немає дисклеймерів, квадратних дужок, статусів і коментарів;
- нумерація збігається із загальноприйнятим Євангелієм від Фоми;
- усі рішення про невключення винесені в додаток і evidence dossier.

## Фаза 5. Full 114-Logion Commentary Expansion

Мета: перетворити `full-logion-commentary-appendix-uk.md` з каркаса на справжній читацький додаток.

Після print/digital publication architecture v0.1 кожен appendix pass має дотримуватися print-safe правил: у прозі для читача використовувати номери логій, witness labels, canonical references і bibliography keys; внутрішні repo paths тримати в окремому source/control шарі, який може бути автоматично вилучений або трансформований для друку.

Кожна логія має отримати:

- короткий зміст;
- джерела;
- грецький статус;
- канонічні, позаканонічні або внутрішньотоміні паралелі;
- можливі тлумачення;
- що лишається непевним;
- чому включено або не включено;
- посилання на картку й evidence note.

## Фаза 6. Greek Retroversion Confidence Audit

Мета: перевірити всі місця, де грецький текст не збережений, але реконструюється.

Вихідні критерії:

- кожна ретроверсія має маркер `Greek retroversion, hypothetical`;
- кожна має confidence: `high`, `medium`, `low`;
- вказано підстави: коптська граматика, грецькі запозичення, синоптичні формули, семітизми або інші контролі;
- жодна ретроверсія не використовується як рукописний свідок.

## Фаза 7. Publication Evidence Dossier

Мета: довести `evidence-dossier-en.md` до рівня зовнішньої перевірки.

Вихідні критерії:

- методологічний вступ;
- source hierarchy;
- rights and citation policy;
- logion-by-logion evidence summaries;
- inclusion/exclusion rationale;
- synoptic and non-synoptic parallels;
- bibliography;
- uncertainty and alternative reconstructions.

## Фаза 8. Bibliography, Rights, and Citation Pass

Мета: зробити проект безпечним для поширення.

Потрібно:

- окрема бібліографія;
- перелік використаних онлайн-джерел і локальних snapshots;
- чітке позначення public domain / open / protected materials;
- перевірка, що жоден захищений сучасний переклад не є базовим текстом;
- правила короткого цитування сучасних видань.

## Фаза 9. Final Reader and Editorial Pass

Мета: зробити видання читабельним і переконливим.

Потрібно:

- український вступ для читача;
- англомовний methodological introduction;
- фінальна редакція українського clean reader;
- фінальна редакція full appendix;
- фінальна редакція parallel edition;
- перевірка термінології між українським, англійським, коптським і грецьким шарами.

## Найближча дія

Найважливіша наступна редакційна дія за актуальною prompt queue: print-safe full appendix editorial consolidation для Logia 61-70. Найважливіша pre-freeze змістова дія після цього: wealth/renunciation cluster-control. Evidence dossier publication pass лишається наступним великим публікаційним кроком після цих пакетів.

Перед початком і після завершення пакета запускати:

```bash
python3 tools/qa_crosscheck.py
```

Виконані пакети:

- Logia 86, 89, 95, 96, 99, 100, 107.
- Logia 1, 2, 3, 4, 5, 6.
- Logia 9, 10, 16, 20, 22.
- Logia 25, 26, 31, 32, 33.
- Logia 34, 35, 36, 39, 41.
- Logia 54, 72, 73.
- Logia 51-60.

Виконано також:

- Final all-114 decision audit.
- Split-core decision review A: Logia 45, 47, 63, 64, 65-66.

Наступний рекомендований пакет:

- Cluster-control note для wealth/renunciation групи.

Причина: Controlled clean-reader candidate pass уже виконано і додав тільки 45A, 47B та 63. Gold-level card normalization v0.2 і five-source apparatus v0.1 виконано для 114/114 карток. Canonical Greek extraction pass виконано для 81 картки. Pending P.Oxy. XML extraction gap закрито; evidence/control inventory виконано; all-114 publication decision table v0.1 створено; P1 evidence-rationale packages виконано; living/dead/world, beatitudes, seek/find, family-renunciation і fire/kingdom cluster-control passes виконано. Тепер слабке місце - wealth/renunciation cluster-control, Logion 114 exclusion rationale і публікаційна редактура appendix/dossier.

Після reader-interpretation expansion v0.1 і full-appendix reader-interpretation sync v0.1 усі 114 карток і всі 114 appendix-секцій мають читацький шар. Editorial consolidation виконано для Logia 1-60. Усі 37 clean-reader одиниць мають точний `Чистий текст реконструкції` anchor у full appendix. Наступний якісний крок за `project/open-task-prompt-queue-2026-07-18.md` - продовжити вирівнювання appendix пакетом Logia 61-70, прибираючи дублювання між старими розгорнутими секціями й новим синхронізованим блоком, а потім перейти до wealth/renunciation cluster-control.

Цей наступний пакет має вже виконувати нове print-safe правило: не покладатися на клікабельні посилання як єдиний апарат, а давати друковані відповідники для кожного важливого джерельного або паралельного посилання.
