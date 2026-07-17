# Project Quality Audit v0.1

Статус: повний аудит якості, 2026-07-17.

## Мета аудиту

Цей документ фіксує не те, що проект уже вміє, а те, що може завадити йому стати переконливою публікаційною реконструкцією найдавнішого досяжного євангелія висловів.

Фокус аудиту:

- якість джерельного шару;
- рівномірність карток логій;
- повнота evidence notes і control files;
- готовність clean reader і повного додатку;
- публікаційна безпека: метод, права, бібліографія, цитування;
- внутрішня синхронізація документації.

## Executive Assessment

Орієнтовна готовність проекту до кінцевої мети: 70-73%.

Це вже сильний робочий корпус, а не початкова збірка нотаток. Найважливіше вже зроблено: є повне покриття 114 логій картками, є clean Ukrainian reader, є концепція двошарового видання, є пʼятиджерельний апарат у картках, є коптський корпус, є P.Oxy. корпус, є SBLGNT canonical Greek controls для більшості релевантних карток.

Але проект ще не є бездоганним виданням. Головний ризик: структура випереджає доказову глибину. Тобто майже всюди вже є місце для правильного матеріалу, але не всюди цей матеріал доведено до публікаційного рівня.

## Поточні Метрики

| Напрям | Стан |
| --- | ---: |
| Картки логій | 114/114 |
| Картки з `Gold-level status check v0.2` | 114/114 |
| Картки з `Five-source original-language apparatus v0.1` | 114/114 |
| Картки з реальним локальним canonical Greek text | 81/114 |
| Картки з canonical Greek channel, але без локально виписаного Greek text | 33/114 |
| Картки з pending P.Oxy. line extraction | 8/114 |
| Evidence note у workflow matrix | 34/114 |
| Без evidence note у workflow matrix | 80/114 |
| Картки з явним повідомленням, що окремого evidence note ще немає | 58/114 |
| Картки з явним повідомленням, що окремого control file ще немає | 60/114 |
| Full appendix headings | 114/114 |
| Appendix sections still using short navigation-label wording | 83 |
| Clean Ukrainian reader | 34 логії / ядра |

Примітка: older audit files ще згадують 55 evidence notes / 59 missing. Поточна workflow matrix показує 34 `YES` і 80 `NO`, тому це треба звірити окремим evidence-file audit pass.

## Що Вже Сильне

1. **Корпус повністю покритий.** Немає логій без картки; це критично важливий фундамент.
2. **Картки вирівняні структурно.** Усі 114 мають однаковий gold-level status layer.
3. **Джерельні канали стали видимими.** У картках прямо показано P.Oxy. 1 / 654 / 655, Coptic NHC II і canonical Greek control channel.
4. **Коптський базовий текст внесено прямо в картки.** Це відповідає рішенню брати коптський текст як головний збережений witness.
5. **Clean reader уже читається як окремий текст.** 34 логії/ядра можна показувати читачеві як робочу реконструкцію без коментарів і дисклеймерів.
6. **Проект має правильну двошарову концепцію.** Спочатку чистий текст, потім повний додаток до всіх 114 логій, включно з відкинутими.
7. **Гіпотетичний грецький шар методологічно відокремлено від рукописних свідків.**

## P0 Недоліки: Критичні Для Публікаційної Якості

### 1. Evidence Depth Нерівномірний

Найбільший недолік зараз: не всі логії мають доказовий рівень, достатній для зовнішньої перевірки.

Фактичний стан:

- workflow matrix має тільки 34 `YES` у колонці `Evidence note`;
- 80 логій мають `NO`;
- 58 карток прямо кажуть, що окремого evidence note ще немає;
- 60 карток прямо кажуть, що окремого control file ще немає.

Ризик: читач або критик побачить рішення, але не завжди побачить достатньо доказів, чому логію включено, відкладено або відкинуто.

Потрібно:

- провести evidence-file audit: звірити реальні файли в `reconstruction/earliest-sayings-gospel/notes/` з workflow matrix;
- для всіх included reader logia мати окремий evidence note або section у dossier;
- для excluded/deferred high-impact logia мати не менший за якістю appendix rationale;
- для low-priority deferred logia дозволити коротший note, але не мовчання.

### 2. Pending P.Oxy. XML Extraction Все Ще Не Закрито

У 8 картках є реальний папірусний шанс, але card-level Greek extract ще не зроблено:

- P.Oxy. 1: логії 27, 28, 29, 30, 77;
- P.Oxy. 655: логії 24, 37, 38.

Ризик: перед фінальною all-114 decision table ми можемо недооцінити або переоцінити логії, для яких у нас уже є локальний TEI/XML witness, але він ще не перетворений у читабельний Greek apparatus.

Потрібно:

- витягнути грецькі рядки з `sources/primary_texts/greek_poxy/dclp-poxy1-62838.xml`;
- витягнути грецькі рядки з `sources/primary_texts/greek_poxy/dclp-poxy655-62839.xml`;
- оновити відповідні 8 карток;
- зафіксувати, які читання є extant, lacunose, supplied або unusable.

### 3. Немає Фінальної All-114 Publication Decision Table

Є `inclusion-decisions-table.md`, `final-all-114-decision-audit-v0.1.md` і workflow matrix, але ще немає одного фінального контрольного документа, де для всіх 114 логій або підодиниць буде:

- decision;
- reader status;
- confidence;
- main reason;
- evidence note;
- Greek witness status;
- appendix status;
- reason for inclusion / exclusion / deferral.

Ризик: фінальний clean reader може виглядати як добірка хороших місць, а не як наслідок послідовного методу по всьому корпусу.

### 4. Full Appendix Є Як Каркас, Але Не Як Повний Коментар

`reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-uk.md` має 114 headings, але 83 місця ще використовують коротку навігаційну формулу на кшталт "Цей опис узято з робочого індексу логій".

Ризик: задум "дати читачеві можливість дослідити кожну логію" ще не виконаний повністю. Особливо важливо, що невключені логії теж мають отримати серйозне пояснення, інакше читач не побачить чесності відбору.

Потрібно для кожної логії:

- короткий зміст;
- джерела і текстові свідки;
- грецький статус;
- канонічні / позаканонічні / внутрішньотоміні паралелі;
- можливі тлумачення;
- що лишається непевним;
- чому включено, не включено або відкладено.

### 5. Evidence Dossier Не Готовий Як Англомовний Публікаційний Захист

Evidence dossier існує як робочий документ, але ще не є фінальною академічною аргументацією.

Потрібно:

- methodological introduction;
- source hierarchy;
- explicit uncertainty model;
- logion-by-logion evidence summaries;
- inclusion/exclusion rationale;
- bibliography;
- rights and citation policy;
- окреме пояснення, чому реконструкція не дорівнює "перекладу Фоми".

## P1 Недоліки: Високий Пріоритет

### 6. Canonical Greek Layer Частково Залежить Від Локального Cache

SBLGNT Greek controls внесені в 81 картку, але джерельний cache описано як `/tmp/euagelia-sblgnt/Matt.txt`, `/tmp/euagelia-sblgnt/Mark.txt`, `/tmp/euagelia-sblgnt/Luke.txt`.

Ризик: `/tmp` не є стабільним проектним джерелом. Через рік буде важче відтворити extraction pass.

Потрібно:

- або внести дозволений open-source SBLGNT source snapshot у `sources/primary_texts/`;
- або створити точний reproducibility note з URL, commit/hash, license і extraction script;
- оновити `sources/primary_texts/source-register.md`, щоб SYN-MATT / SYN-MARK / SYN-LUKE не виглядали як повністю "потрібно знайти", якщо SBLGNT уже використано.

### 7. Source Register Має Застарілі Рядки

`sources/primary_texts/source-register.md` уже має `SBLGNT-LOCAL`, але нижче SYN-MARK / SYN-MATT / SYN-LUKE досі кажуть `потрібно знайти`.

Це можна пояснити тим, що SYN rows означають "final chosen edition", але документ цього не пояснює достатньо явно.

Потрібно:

- розділити `working open control text` і `final publication critical edition`;
- позначити SBLGNT як current working canonical Greek control;
- позначити NA28/UBS або інше академічне видання як final verification target, без внесення захищеного тексту.

### 8. Документація Має Несинхронні Формулювання

Виявлені приклади:

- `project/publication-gap-audit-v0.1.md` має title `Publication Gap Audit v0.2`;
- `project/project-completion-roadmap.md` має дубльовану нумерацію в "Основні прогалини" - два пункти `5`;
- `project/project-completion-roadmap.md` одночасно каже, що найближча дія - pending P.Oxy. XML extraction pass, і що наступний рекомендований пакет - true all-114 publication decision table. Це логічно узгоджується тільки якщо чітко сказати: спершу P.Oxy extraction, потім decision table.
- older audits згадують 55/59 evidence-note split, тоді як поточна matrix показує 34/80.

Ризик: новий виконавець або читач документації може піти не в той наступний крок.

### 9. Prompt Sprawl Повернувся

У `project/` знову є багато історичних `ide-codex-...-prompt.md`. Частина з них виконані, частина застарілі, частина все ще корисні як журнал.

Ризик: складно зрозуміти, який prompt є головним, а які лишилися історичними.

Потрібно:

- створити `project/prompts/archived/` або інший зрозумілий архів;
- залишити в корені тільки master prompt і поточний next-step prompt;
- у `project/project-map.md` позначити архів як історію виконаних проходів.

### 10. Грецькі Ретроверсії Потребують Publication Polish

Проект правильно маркує `Greek retroversion, hypothetical`, але фінальна якість потребує:

- єдиної шкали confidence;
- звірки з коптською граматикою;
- звірки з extant Greek Thomas fragments;
- звірки з canonical Greek formulae;
- чіткого пояснення для читача, що це не рукописний текст.

### 11. Права І Цитування Ще Не Доведені До Фінального Апарату

Є source register і notes, але ще немає фінального rights/citation pass.

Ризик: проект може ненавмисно виглядати так, ніби використовує захищені сучасні переклади або critical editions як базовий публічний текст.

Потрібно:

- окремий rights and citation policy;
- окрема bibliography;
- короткий список open / public-domain / protected sources;
- правило, що захищені видання використовуються для перевірки, а не для повного відтворення.

## P2 Недоліки: Полірування І Читабельність

### 12. Український Вступ Для Читача Ще Не Написано

Clean reader має починатися без дисклеймерів, але перед або після чистого тексту потрібен reader-facing introduction у другому шарі:

- що означає "найдавніше євангеліє";
- чому це реконструкція, а не знайдений рукопис;
- чому нумерація логій лишається томиною;
- чому частина логій не включена;
- як користуватися appendix.

### 13. Clean Reader Потребує Фінального Літературного Редагування

34 логії/ядра читаються добре, але перед фіналом треба:

- уніфікувати стиль української мови;
- перевірити, чи немає надто "церковно звичних" пізніших формулювань там, де ми реконструюємо ранніший шар;
- не додавати пояснення в сам чистий текст;
- зберегти нумерацію за Gospel of Thomas.

### 14. Parallel Edition Ще Не Фінальна

Поточний multilingual/parallel layer покриває reader units, але після final all-114 decision table його треба оновити:

- українська;
- англійська;
- коптська;
- extant Greek або Greek retroversion with confidence;
- canonical parallels тільки як control, не як witness.

### 15. Автоматичні Перевірки Майже Відсутні

Проект уже достатньо великий, щоб мати прості consistency checks:

- 114 карток існують;
- кожна має five-source block;
- кожна має gold status block;
- appendix має 114 sections;
- clean reader logia збігаються зі списком у roadmap;
- workflow matrix не суперечить cards.

Це не замінює дослідження, але зменшує ризик технічних розсинхронів.

### 16. У Робочому Дереві Є `.DS_Store`

Файли `.DS_Store` знайдено в:

- `./.DS_Store`;
- `./output/.DS_Store`;
- `./reconstruction/.DS_Store`.

Вони не відстежуються git і `.gitignore` вже має `.DS_Store`, але їх варто прибрати локально, щоб не засмічувати audits/search results.

## Рекомендована Послідовність Закриття Недоліків

1. **P.Oxy. XML extraction pass.** Закрити 8 pending папірусних витягів.
2. **Documentation sync pass.** Виправити очевидні розсинхрони: roadmap numbering, publication audit filename/title, source register SBLGNT/SYN rows, evidence-note statistics.
3. **Evidence-file audit pass.** Звірити фактичні evidence notes/control files із workflow matrix.
4. **True all-114 publication decision table.** Один фінальний контрольний документ по всіх логіях і підодиницях.
5. **Full appendix expansion pass.** Пакетами перетворити 83 каркасні розділи на реальні пояснювальні коментарі.
6. **Evidence dossier publication pass.** Англомовний доказовий документ із методологією, bibliography і uncertainty model.
7. **Rights and citation pass.** Зафіксувати, що можна публікувати, що тільки цитувати коротко, що тільки використовувати для перевірки.
8. **Greek retroversion polish.** Confidence labels, wording, no-confusion rule.
9. **Final reader polish.** Український clean reader, English reader, parallel edition, introduction і editorial consistency.
10. **Consistency check scripts.** Маленькі технічні перевірки перед фінальним freeze.

## Найважливіший Наступний Крок

Найлогічніше наступне завдання: завершити **P.Oxy. XML extraction pass** для 8 карток.

Причина: перед фінальною таблицею включення/невключення треба спершу закрити прямий джерельний борг. Якщо папірусний шар ще має pending extraction, то all-114 publication decision table буде побудована на не до кінця відкритому evidence layer.

Після цього треба одразу робити documentation sync pass і true all-114 publication decision table.

