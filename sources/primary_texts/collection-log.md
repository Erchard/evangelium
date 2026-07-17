# Журнал збирання корпусу

## 2026-07-17, controlled clean-reader candidate pass

### Що додано

- `project/ide-codex-controlled-clean-reader-candidate-pass-prompt.md` - промпт для суворого reader-candidate pass після split-core reviews A/B.
- `reconstruction/earliest-sayings-gospel/controlled-clean-reader-candidate-pass-v0.1.md` - рішення по всіх candidate cores.

### Що оновлено

- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-uk.md`: clean reader розширено з 31 до 34 одиниць.
- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-en.md`, `reconstructed-gospel-coptic.md`, `reconstructed-gospel-greek.md`, `parallel-edition.md`: додано синхронні шари для 45A, 47B і 63.
- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-uk-apparatus.md`: додано пояснення для нових включень.
- `reconstruction/earliest-sayings-gospel/evidence-dossier-en.md`: додано summary-блоки для 45, 47 і 63 та оновлено current reader count.
- `reconstruction/earliest-sayings-gospel/greek-retroversion-confidence-audit-v0.1.md`: додано 45, 47 і 63 як `Greek retroversion, hypothetical`.
- `reconstruction/earliest-sayings-gospel/inclusion-decisions-table.md`, `corpus/tables/logia-workflow-matrix.md`, `full-logion-commentary-appendix-uk.md` і відповідні картки синхронізовано з рішеннями pass.
- Активні project/README/status документи оновлено: наступний крок тепер true all-114 publication decision table.

### Методологічне рішення

До clean reader включено тільки:

- 45A grapes/thorns core;
- 47B two-masters core;
- 63 rich-fool core.

Не включено в clean reader, але збережено в appendix-only:

- 45B heart-treasure continuation;
- 64A banquet core;
- 76A/76B pearl and treasure cores;
- 78A wilderness/reed/soft-clothing core;
- 79A hearing/keeping word core;
- 103A thief/watchfulness core.

Причина: ці одиниці цікаві, але мають сильніший ризик дублювання, залежності, контекстної прив'язаності або вторинного розгортання.

### Наступна дія

True all-114 publication decision table.

## 2026-07-17, split-core decision review B

### Що додано

- `project/ide-codex-split-core-decision-review-b-prompt.md` - промпт для split-core review B.
- `reconstruction/earliest-sayings-gospel/split-core-decision-review-b-v0.1.md` - підсумковий review по логіях 76, 78, 79, 94, 103, 109, 113.

### Що оновлено

- `reconstruction/earliest-sayings-gospel/inclusion-decisions-table.md`: додано split-core decisions для 76A/76B, 78A, 79A, 94, 103A, 109, 113.
- `corpus/tables/logia-workflow-matrix.md`: цільові логії позначено як Split-core review B v0.1.
- `corpus/cards/logion-076.md`, `logion-078.md`, `logion-079.md`, `logion-094.md`, `logion-103.md`, `logion-109.md`, `logion-113.md`: доказовий апарат синхронізовано з уже наявними evidence/control файлами.
- `README.md`, `project/project-map.md`, `project/project-completion-roadmap.md`, `project/publication-gap-audit-v0.1.md`, `project/repository-structure.md`, `project/final-product-specification.md`, `reconstruction/earliest-sayings-gospel/README.md`: наступний крок оновлено до controlled clean-reader candidate pass.

### Методологічне рішення

Clean Ukrainian reader не змінювався. Review B промотував як candidate cores лише:

- 76A pearl/merchant core;
- 76B imperishable treasure core;
- 78A wilderness/reed/soft-clothing core;
- 79A hearing/keeping word core;
- 103A thief/watchfulness core.

Logia 94, 109 і 113 залишено appendix-only for now через дублювання вже представлених мотивів або високий dependence/secondary-layer risk.

### Наступна дія

Controlled clean-reader candidate pass для ядер, промотованих у Reviews A/B.

## 2026-07-17, split-core decision review A

### Що додано

- `project/ide-codex-split-core-decision-review-a-prompt.md` - промпт для split-core review A.
- `reconstruction/earliest-sayings-gospel/split-core-decision-review-a-v0.1.md` - підсумковий review по логіях 45, 47, 63, 64, 65-66.
- Control files:
  - `controls/synoptic-parallels/logion-045-tree-fruit-heart-controls.md`
  - `controls/synoptic-parallels/logion-047-incompatibility-sayings-controls.md`
  - `controls/synoptic-parallels/logion-063-rich-fool-luke-control.md`
  - `controls/synoptic-parallels/logion-064-banquet-invitation-controls.md`
  - `controls/synoptic-parallels/logia-065-066-tenants-stone-controls.md`

### Що оновлено

- `reconstruction/earliest-sayings-gospel/inclusion-decisions-table.md`: додано split-core decisions для 45A/45B, 47B, 63, 64A/64B, 65-66.
- `corpus/tables/logia-workflow-matrix.md`: цільові логії позначено як Split-core review A v0.1.
- `reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-uk.md`: зведену таблицю синхронізовано з рішеннями Review A.
- `README.md`, `project/project-map.md`, `project/project-completion-roadmap.md`, `project/publication-gap-audit-v0.1.md`, `project/repository-structure.md`, `project/final-product-specification.md`, `reconstruction/earliest-sayings-gospel/README.md`: наступний крок оновлено до Review B.

### Методологічне рішення

Clean Ukrainian reader не змінювався. Review A не промотував повні складені логії. Натомість він визначив candidate cores для майбутнього controlled clean-reader pass:

- 45A grapes/thorns;
- 45B good/evil heart treasure;
- 47B two masters;
- 63 rich-fool core;
- 64A banquet invitation core.

Logia 65-66 залишено appendix-only for now через сильний allegorical / passion-interpretation risk.

Для всіх цільових логій немає loaded extant Greek Thomas witness; будь-яка грецька форма має лишатися `Greek retroversion, hypothetical`.

### Наступна дія

Split-core decision review B: Logia 76, 78, 79, 94, 103, 109, 113.

## 2026-07-17, final all-114 decision audit

### Що додано

- `project/ide-codex-final-all-114-decision-audit-prompt.md` - промпт для контрольного all-114 decision audit перед фіналізацією clean reader.
- `reconstruction/earliest-sayings-gospel/final-all-114-decision-audit-v0.1.md` - аудит поточного стану рішень, стабільності clean reader, сильних невключених кандидатів, застарілих файлів і наступного робочого пакета.

### Що оновлено

- `corpus/tables/logia-workflow-matrix.md`: прибрано застарілі `Needs multilingual sync` для reader units 86, 89, 95, 96, 99, 100 і 107; ці одиниці вже мають мовні шари й розгорнуті appendix-секції.
- `README.md`, `project/project-map.md`, `project/project-completion-roadmap.md`, `project/publication-gap-audit-v0.1.md`, `project/repository-structure.md`, `project/clean-text-plus-commentary-concept.md`, `reconstruction/earliest-sayings-gospel/README.md`: наступний крок оновлено з загального all-114 audit на конкретний split-core review.

### Методологічне рішення

Clean Ukrainian reader не змінювався. Аудит підтвердив, що поточні 31 reader units мають достатню робочу підтримку: cards, evidence/control support, language layers і expanded appendix commentary. Але clean reader ще не треба фіналізувати, бо кілька невключених логій можуть містити короткі ранні ядра.

### Наступна дія

Split-core decision review A: Logia 45, 47, 63, 64, 65-66.

## 2026-07-17, full appendix expansion for Logia 54, 72, 73

### Що додано

- `project/ide-codex-full-appendix-logia-054-072-073-expansion-prompt.md` - промпт для закриття останнього пакета включених clean-reader логій, які ще мали каркасний appendix-розділ.

### Що оновлено

- `reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-uk.md`: логії 54, 72 і 73 перетворено з каркасних секцій на читацькі коментарі.
- `README.md`, `project/project-map.md`, `project/project-completion-roadmap.md`, `project/final-product-specification.md`, `project/publication-gap-audit-v0.1.md`, `project/repository-structure.md`, `reconstruction/earliest-sayings-gospel/README.md`: статус full appendix оновлено з 28 розгорнутих включених секцій до всіх 31 включених одиниць поточного clean reader.

### Методологічне рішення

Чистий український reader не змінювався. Логії 54, 72 і 73 вже були включені до clean reader; цей прохід додав другий читацький шар: сенс логії, підстави включення, синоптичні контролі, можливі тлумачення, Greek retroversion status і межі впевненості.

Особливо зафіксовано:

- Logion 54 має сильну beatitude-паралель із Лукою 6:20 і Матвієм 5:3, але змішує Luke-like direct poverty і Matthew-like kingdom-of-heaven wording.
- Logion 72 лишається найобережнішою з трьох, бо має дуже близький, але одиничний контроль у Луці 12:13-15.
- Logion 73 має сильний формульний подвійний контроль у Матвія 9:37-38 і Луки 10:2.

Для всіх трьох логій немає loaded extant Greek Thomas witness; будь-яка грецька форма має лишатися `Greek retroversion, hypothetical`.

### Наступна дія

Провести final all-114 decision audit перед фіналізацією складу clean reader.

## 2026-07-17, repository structure reorganization

### Що змінено

- Стару числову структуру папок замінено на функціональну: `project/`, `sources/`, `corpus/`, `controls/`, `reconstruction/`, `research/`, `bibliography/`, `output/`, `archive/`.
- Додано навігаційний документ `project/repository-structure.md`.
- Оновлено кореневий `README.md`, `project/project-map.md`, дорожню карту й внутрішні посилання на нові шляхи.

### Методологічне рішення

Реорганізація не змінює зміст реконструкції. Вона лише робить робочий простір ближчим до фактичної логіки проекту: джерела окремо, корпус карток окремо, контролі паралелей окремо, реконструкція і читацькі тексти окремо.

### Наступна дія на той момент

Після структурного прибирання продовжити full appendix expansion для логій 54, 72, 73.

## 2026-07-17, full appendix expansion for Logia 34, 35, 36, 39, 41

### Що додано

- `project/ide-codex-full-appendix-logia-034-035-036-039-041-expansion-prompt.md` - промпт для розгортання наступного включеного пакета.

### Що оновлено

- `reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-uk.md`: логії 34, 35, 36, 39 і 41 перетворено з каркасних секцій на читацькі коментарі.
- `project/project-completion-roadmap.md`: пакет 34/35/36/39/41 позначено виконаним; наступний пакет - 54, 72, 73.
- `project/final-product-specification.md`, `project/project-map.md`, `project/publication-gap-audit-v0.1.md`, `reconstruction/earliest-sayings-gospel/README.md`: кількість розгорнутих included appendix sections оновлено з 23 до 28.

### Методологічне рішення

Чистий український reader не змінювався. У додатку уточнено, що логії 34, 35 і 41 не мають extant Greek Thomas witness, а логії 36 і 39 залежать від складного P.Oxy. 655 матеріалу з відновленнями й композиційними ризиками.

### Наступна дія

Завершити full appendix expansion для remaining included units: 54, 72, 73.

## 2026-07-17, project documentation refresh

### Що оновлено

- `project/project-map.md` - додано актуальний стислий стан проекту.
- `project/final-product-specification.md` - оновлено до v0.2 і додано current working state.
- `project/project-completion-roadmap.md` - оновлено до v0.3; готовність тепер 55-60%, full appendix більше не описується як чистий skeleton.
- `project/publication-gap-audit-v0.1.md` - оновлено зміст до v0.2: 31-unit reader, 23 expanded appendix sections, next packet 34/35/36/39/41.
- `project/clean-text-plus-commentary-concept.md` - зафіксовано, що перший тест clean text + commentary уже виконано.
- `reconstruction/earliest-sayings-gospel/README.md` - оновлено current scope до 31 логії/ядра і додано Greek audit / full appendix status.
- `reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-uk.md` - статус оновлено до v0.3.

### Поточний стан після актуалізації

- Clean Ukrainian reader має 31 логію/ядро.
- English/Coptic/Greek/parallel layers синхронізовані для 31 одиниці.
- Greek retroversion confidence audit створено.
- На цьому історичному етапі full 114-logion appendix мав каркас для всіх 114 логій і 23 розгорнуті включені секції; поточний стан оновлено до 28 у записі про пакет 34/35/36/39/41 вище.

### Наступна дія

Продовжити full appendix expansion для логій 34, 35, 36, 39, 41.

## 2026-07-17, Greek retroversion confidence audit

### Що додано

- `project/ide-codex-greek-retroversion-confidence-audit-prompt.md` - промпт для аудиту грецького шару.
- `reconstruction/earliest-sayings-gospel/greek-retroversion-confidence-audit-v0.1.md` - аудит усіх 31 одиниці current reader за категоріями Greek layer і confidence.

### Що оновлено

- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-greek.md`: статус оновлено до v0.5 і додано посилання на confidence audit.
- `project/project-completion-roadmap.md`: Greek layer більше не позначений як без audit; наступний крок - full appendix expansion для включених 31 логій/ядер.
- `project/publication-gap-audit-v0.1.md`: оновлено стан Greek layer і рекомендований порядок наступних дій.

### Методологічне рішення

Аудит розділяє:

- extant Greek witnesses;
- lacunose extant witnesses;
- partial extant witnesses;
- mixed extant-plus-retroversion units;
- `Greek retroversion, hypothetical`.

Ретроверсії не рахуються як рукописні свідки й мають бути явно позначені в будь-якому публічному виданні.

### Наступна дія

Розширити повний український додаток для включених 31 логій/ядер, щоб чистий reader мав повний читацький другий шар.

## 2026-07-17, multilingual sync for new reader additions 86, 89, 95, 96, 99, 100, 107

### Що додано

- `project/ide-codex-multilingual-sync-new-reader-additions-086-089-095-096-099-100-107-prompt.md` - промпт для синхронізації семи нових reader additions.

### Що оновлено

- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-en.md`: додано англійські тексти логій 86, 89, 95, 96, 99, 100 і 107.
- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-coptic.md`: додано коптські базові свідки для семи одиниць із нотатками про скорочене ядро.
- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-greek.md`: додано тільки позначені `Greek retroversion, hypothetical` для семи одиниць; жодна не подана як extant Greek witness.
- `reconstruction/earliest-sayings-gospel/parallel-edition.md`: додано сім рядків; parallel edition тепер покриває 31 одиницю.
- `reconstruction/earliest-sayings-gospel/evidence-dossier-en.md`: оновлено до v1.3 і додано summaries для семи нових одиниць.
- `reconstruction/earliest-sayings-gospel/reader-commentary-uk.md`: додано українські читацькі коментарі для семи нових одиниць.
- `project/project-completion-roadmap.md` і `project/publication-gap-audit-v0.1.md`: наступним кроком визначено Greek retroversion confidence audit.

### Методологічне рішення

Чистий український reader не змінювався в цьому проході. Синхронізовано другий шар довкола вже ухваленого складу з 31 логії/ядра.

### Наступна дія

Провести Greek retroversion confidence audit для поточного 31-unit reader, особливо для одиниць без extant Greek Thomas witness.

## 2026-07-17, final high-candidate decision pass

### Що додано

- `project/ide-codex-final-high-candidate-decision-pass-prompt.md` - промпт для фінального decision pass по Sprint A/B/C.
- `reconstruction/earliest-sayings-gospel/final-high-candidate-decision-pass-v0.1.md` - документ із рішеннями, промоціями, відхиленнями і cluster decisions.

### Що оновлено

- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-uk.md`: додано чисті ядра логій 86, 89, 95, 96, 99, 100 і 107.
- `reconstruction/earliest-sayings-gospel/inclusion-decisions-table.md`: сім нових одиниць переведено в `INCLUDE_WITH_MARKER` або `INCLUDE_WITH_MARKER` для core.
- `corpus/tables/logia-workflow-matrix.md`: для 86, 89, 95, 96, 99, 100 і 107 тепер `Reader text = YES`.
- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-uk-apparatus.md`: додано пояснення для семи нових reader additions.
- `project/project-completion-roadmap.md` і `project/publication-gap-audit-v0.1.md`: clean reader тепер має 31 логію/ядро; наступним кроком є multilingual synchronization pass.

### Методологічне рішення

До clean reader додано тільки короткі ядра, не повні форми з пізніми або томиними розгортаннями:

- 86 - foxes/birds/Son of Man homelessness;
- 89 - cup inside/outside;
- 95 - anti-usury / giving without return;
- 96 - leaven parable core;
- 99 - true-family core;
- 100 - Caesar/God core;
- 107 - lost-sheep core.

Логії 44, 46, 55, 57, 76, 78, 79, 90, 93, 94, 103, 109 і 113 залишаються поза clean reader, але зберігаються в appendix/evidence layer.

### Наступна дія

Синхронізувати нові reader additions у `reconstructed-gospel-en.md`, `reconstructed-gospel-coptic.md`, `reconstructed-gospel-greek.md`, `parallel-edition.md`, `evidence-dossier-en.md` і читацькому коментарі.

## 2026-07-17, high-candidate deepening sprint C

### Що додано

- `project/ide-codex-high-candidate-deepening-sprint-c-prompt.md` - промпт для фінального planned high-candidate evidence/control спринту.
- Evidence notes для логій 99, 100, 103, 107, 109 і 113.
- Synoptic/control files для логій 99, 100, 103, 107, 109 і 113.

### Що оновлено

- `corpus/tables/logia-workflow-matrix.md`: Sprint C має `Evidence note = YES`; усі шість логій залишаються `Reader text = NO`.
- `reconstruction/earliest-sayings-gospel/inclusion-decisions-table.md`: додано рішення для логій 99, 100, 103, 107, 109 і 113.
- `corpus/cards/card-quality-audit-v0.1.md`, `project/publication-gap-audit-v0.1.md` і `project/project-completion-roadmap.md`: наступним кроком тепер є final high-candidate decision pass, а не новий evidence sprint.

### Методологічне рішення

Жодна з логій Sprint C не додана до clean reader у цьому проході. Логії 99, 100, 103 і 109 позначені як split-core candidates; 107 як possible marked parable-core candidate; 113 як possible marked-core candidate, але з ризиком дублювання логії 3.

Для всіх Sprint C логій без extant Greek Thomas witness будь-який грецький шар має бути тільки `Greek retroversion, hypothetical`.

### Наступна дія

Провести final high-candidate decision pass для Sprint A/B/C: вирішити, які короткі ядра можуть увійти до clean reader, які лишаються тільки в appendix, і які потрібно відкласти як занадто залежні або вторинні.

## 2026-07-17, high-candidate deepening sprint B

### Що додано

- `project/ide-codex-high-candidate-deepening-sprint-b-prompt.md` - промпт для другого high-candidate evidence/control спринту.
- Evidence notes для логій 86, 89, 90, 93, 94, 95 і 96.
- Synoptic/control files для логій 86, 89, 90, 93, 94, 95 і 96.

### Що оновлено

- `corpus/tables/logia-workflow-matrix.md`: Sprint B має `Evidence note = YES`; усі сім логій залишаються `Reader text = NO`.
- `reconstruction/earliest-sayings-gospel/inclusion-decisions-table.md`: додано рішення для логій 86, 89, 90, 93, 94, 95 і 96.
- `corpus/cards/card-quality-audit-v0.1.md`, `project/publication-gap-audit-v0.1.md` і `project/project-completion-roadmap.md`: наступним high-candidate пакетом тепер є 99, 100, 103, 107, 109, 113.

### Методологічне рішення

Жодна з логій Sprint B не додана до clean reader у цьому проході. Найсильнішими майбутніми кандидатами виглядають 86, 89, 94, 95 і 96, але кожна потребує фінального decision pass. Логії 90 і 93 залишаються обережнішими через вузький матеєвий контроль або сильну secrecy-функцію.

Для логій без extant Greek Thomas witness будь-який грецький шар має бути тільки `Greek retroversion, hypothetical`.

### Наступна дія

Виконати high-candidate deepening sprint C для логій 99, 100, 103, 107, 109 і 113, а потім перейти до decision pass для кандидатів Sprint A/B/C.

## 2026-07-17, high-candidate deepening sprint A

- Збережено і виконано промпт: `project/ide-codex-high-candidate-deepening-sprint-a-prompt.md`.
- Створено evidence notes для Logia 44, 46, 55, 57, 76, 78, 79.
- Створено synoptic/control files: `controls/synoptic-parallels/logion-044-blasphemy-spirit-controls.md`, `logion-046-john-least-kingdom-controls.md`, `logion-055-discipleship-cross-controls.md`, `logion-057-weeds-controls.md`, `logion-076-pearl-treasure-controls.md`, `logion-078-wilderness-reed-controls.md`, `logion-079-womb-word-controls.md`.
- Оновлено `corpus/tables/logia-workflow-matrix.md`: evidence note для цих семи логій тепер `YES`.
- Оновлено `reconstruction/earliest-sayings-gospel/inclusion-decisions-table.md`: додано робочі рішення для цих семи логій.
- Оновлено `corpus/cards/card-quality-audit-v0.1.md`, `project/publication-gap-audit-v0.1.md` і `project/project-completion-roadmap.md`: наступним high-candidate пакетом тепер є 86, 89, 90, 93, 94, 95, 96.
- Жодну з цих логій не додано до clean reader; всі залишаються `UNCERTAIN`, але 46 і 78 позначені як можливі майбутні marked-core candidates, 76 і 79 як split-core candidates.
- Чистий український reader не змінювався.

## 2026-07-17, publication gap audit and roadmap refresh

- Збережено і виконано промпт: `project/ide-codex-publication-gap-audit-and-roadmap-refresh-prompt.md`.
- Оновлено дорожню карту завершення: `project/project-completion-roadmap.md`.
- Створено публікаційний аудит прогалин: `project/publication-gap-audit-v0.1.md`.
- Дорожня карта тепер відображає реальний стан: 114 карток існують, усі картки вирівняні, clean reader має 24 логії/ядра, повний додаток до 114 логій існує як skeleton.
- Зафіксовано наступні ключові робочі фази: high-candidate deepening, evidence/control gap closure, final decision audit, full appendix expansion, Greek retroversion confidence audit, evidence dossier publication pass, bibliography/rights pass, final editorial pass.
- Чистий український reader не змінювався.

## 2026-07-17, full 114-logion commentary appendix skeleton

- Збережено і виконано промпт: `project/ide-codex-full-114-logion-commentary-appendix-skeleton-prompt.md`.
- Створено робочий український каркас повного додатку: `reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-uk.md`.
- Додаток охоплює всі 114 логій: включені, частково включені, `UNCERTAIN`, `DEFER` і `EXCLUDE_AS_SECONDARY`.
- Для кожної логії додано статус у реконструкції, коротку мітку шару, причину включення/невключення, Greek witness status, evidence/control/cluster links і наступну дію.
- Оновлено `reconstruction/earliest-sayings-gospel/README.md`, щоб новий файл був частиною карти реконструкції.
- Чистий український reader не змінювався.
- Наступний якісний крок: перетворювати цей каркас на повноцінні читацькі коментарі пакетами, починаючи з включених 24 логій або з найсильніших невключених high-candidate логій.

## 2026-07-17, full appendix principle for excluded logia

- Зафіксовано важливе уточнення кінцевої мети: чистий reconstructed gospel є вибірковим текстом найдавнішого шару, але коментований додаток має охопити всі 114 логій.
- Оновлено `project/final-product-specification.md`: додано принцип повного покриття всіх логій у додатку, включно з `UNCERTAIN`, `DEFER` і `EXCLUDE_AS_SECONDARY`.
- Оновлено `project/clean-text-plus-commentary-concept.md`: розширено модель коментаря від включених логій до повного 114-логійного додатку.
- Оновлено `project/logion-card-gold-standard.md`: якісна картка тепер має готувати матеріал і для пояснення невключених логій.
- Оновлено `reconstruction/earliest-sayings-gospel/README.md`: додано Full Commentary Principle і виправлено current scope до 24 поточних логій clean reader.
- Оновлено `corpus/cards/LOGION_TEMPLATE.md`: додано поля для пояснення невключених логій у повному коментованому додатку.
- Чистий український reader не змінювався.

## 2026-07-17, logion card quality normalization

- Збережено і виконано промпт: `project/ide-codex-logion-card-quality-normalization-prompt.md`.
- Зафіксовано стандарт якості карток: `project/logion-card-gold-standard.md`.
- Формальний еталон: `corpus/cards/logion-002.md`; додатковий приклад для складених логій: `corpus/cards/logion-006.md`.
- Оновлено шаблон майбутніх карток: `corpus/cards/LOGION_TEMPLATE.md`.
- Усі 114 карток `corpus/cards/logion-*.md` отримали блок `Еталонне вирівнювання картки v0.1` з рішенням, reader status, Greek witness status, попереднім шаром, ймовірнісним профілем, evidence/control посиланнями і наступною дією.
- Створено аудит якості карток: `corpus/cards/card-quality-audit-v0.1.md`.
- Рішення про включення логій не змінювалися; чистий український reader не змінювався.
- Наступний якісний крок: поглиблювати не всі логії однаково, а спершу high-candidate картки без evidence notes/control files, які реально можуть змінити фінальний склад реконструкції.

## 2026-07-17, evidence dossier consolidation for current reader

- Збережено і виконано промпт: `project/ide-codex-evidence-dossier-current-reader-consolidation-prompt.md`.
- Оновлено `reconstruction/earliest-sayings-gospel/evidence-dossier-en.md` до робочої версії v1.2.
- Current Block Summary тепер явно включає всі 24 логії поточного clean reader: 1, 2, 3, 4, 5, 6, 9, 10, 16, 20, 22, 25, 26, 31, 32, 33, 34, 35, 36, 39, 41, 54, 72, 73.
- Додано summary-блоки для Logia 41, 54, 72, 73 з рішенням, reader text, аргументом включення, Greek witness status, evidence note і synoptic control reference.
- Для Logia 41, 54, 72, 73 явно зафіксовано: немає loaded extant Greek Thomas witness; будь-яка грецька форма має лишатися `Greek retroversion, hypothetical`.
- Чистий український reader не змінювався.
- Наступний якісний крок: створити completeness audit для всіх 24 dossier-блоків і вирівняти їх у єдиний публікаційний шаблон.

## 2026-07-17, normalized current parallel edition

- Збережено і виконано промпт: `project/ide-codex-normalize-parallel-edition-current-reader-prompt.md`.
- Нормалізовано `reconstruction/earliest-sayings-gospel/parallel-edition.md` до робочого формату v0.4.
- Таблиця тепер має 24 логійні рядки, що відповідають поточному clean Ukrainian reader.
- Українська й англійська reader-колонки очищені від старих ярликів на кшталт `[Можливе розгортання]` / `[Possible expansion]`.
- Greek Layer тепер явно розрізняє `Extant Greek`, `Partial extant Greek`, `Lacunose P.Oxy.` і `Greek retroversion, hypothetical`.
- Чистий український reader не змінювався.
- Наступний якісний крок: почати consolidation англомовного evidence dossier для всіх 24 включених логій.

## 2026-07-17, multilingual sync для решти поточного reader

- Збережено і виконано промпт: `project/ide-codex-multilingual-sync-current-reader-remainder-prompt.md`.
- Синхронізовано Logia 6, 9, 10, 16, 20, 22, 25, 26, 31, 32, 33, 34, 35, 36, 39 з англійським reader layer: `reconstruction/earliest-sayings-gospel/reconstructed-gospel-en.md`.
- Додано повні коптські base-witness sections для цих логій у `reconstruction/earliest-sayings-gospel/reconstructed-gospel-coptic.md`.
- Додано extant/partial/lacunose Greek witness або clearly marked `Greek retroversion, hypothetical` для цих логій у `reconstruction/earliest-sayings-gospel/reconstructed-gospel-greek.md`.
- Додано компактні рядки до `reconstruction/earliest-sayings-gospel/parallel-edition.md`.
- Оновлено `corpus/tables/logia-workflow-matrix.md`: ці логії позначено як `Multilingual sync v0.1`.
- Найслабші грецькі місця цього проходу: Logia 9, 10, 16, 20, 22, 25, 34, 35 мають лише гіпотетичні ретроверсії; Logion 26 має тільки частковий P.Oxy. 1; Logia 36 і 39 мають P.Oxy. 655, але сильно відновлений.
- Наступний якісний крок: вирівняти status language і clean/marked distinction у `parallel-edition.md`, а потім почати повне evidence-dossier consolidation для всіх логій, уже включених у reader.

## 2026-07-17, multilingual sync для Logia 41, 54, 72, 73

- Збережено і виконано промпт: `project/ide-codex-multilingual-sync-041-054-072-073-prompt.md`.
- Оновлено англійський reader layer: `reconstruction/earliest-sayings-gospel/reconstructed-gospel-en.md`.
- Оновлено коптський base witness layer: `reconstruction/earliest-sayings-gospel/reconstructed-gospel-coptic.md`.
- Оновлено грецький layer: `reconstruction/earliest-sayings-gospel/reconstructed-gospel-greek.md`; для Logia 41, 54, 72, 73 додано тільки `Greek retroversion, hypothetical`, не extant Greek witness.
- Оновлено `reconstruction/earliest-sayings-gospel/parallel-edition.md`: додано рядки для Logia 41, 54, 72, 73.
- Оновлено `corpus/tables/logia-workflow-matrix.md`: Logia 41, 54, 72, 73 позначено як `Multilingual sync v0.1`.
- Наступний якісний крок: підтягнути решту вже включених українських логій 6, 9, 10, 16, 20, 22, 25, 26, 31-36, 39 до англійського, коптського, грецького і parallel-edition шарів.

## 2026-07-17, clean reader pass для Logia 41, 54, 72, 73

- Збережено і виконано промпт: `project/ide-codex-clean-reader-pass-041-054-072-073-prompt.md`.
- Оновлено чистий український reader: `reconstruction/earliest-sayings-gospel/reconstructed-gospel-uk.md`.
- До чистого reader text додано Logia 41, 54, 72, 73 без статусів, квадратних дужок, маркерів і коментарів.
- Оновлено український апарат: `reconstruction/earliest-sayings-gospel/reconstructed-gospel-uk-apparatus.md`.
- Оновлено читацький коментар: `reconstruction/earliest-sayings-gospel/reader-commentary-uk.md`.
- Оновлено `corpus/tables/logia-workflow-matrix.md`: Logia 41, 54, 72, 73 позначено як `Reader pass v0.1`.
- Наступний якісний крок: синхронізувати англійський, коптський, грецький і parallel-edition шари для нового складу reader text.

## 2026-07-17, synoptic control and Coptic extraction sprint

- Збережено і виконано промпт: `project/ide-codex-synoptic-control-and-coptic-extraction-prompt.md`.
- Створено synoptic control files для Logia 41, 54, 72, 73: `controls/synoptic-parallels/logion-041-has-given-controls.md`, `controls/synoptic-parallels/logion-054-blessed-poor-controls.md`, `controls/synoptic-parallels/logion-072-inheritance-dispute-controls.md`, `controls/synoptic-parallels/logion-073-harvest-workers-controls.md`.
- Створено повний коптський extraction file для Logia 63-65: `sources/primary_texts/coptic/logia-063-065-coptic-extraction.md`.
- Оновлено `reconstruction/earliest-sayings-gospel/inclusion-decisions-table.md`: Logia 41, 54, 72, 73 переведено до `INCLUDE_WITH_MARKER`; Logia 63-65 отримали посилання на повний коптський extraction.
- Оновлено `corpus/tables/logia-workflow-matrix.md`: для Logia 41, 54, 72, 73 позначено synoptic controls; для Logia 63-65 зафіксовано Coptic extraction v0.1.
- Чистий український reader не змінювався; наступний окремий крок - контрольоване додавання 41, 54, 72, 73 у clean reader та апарат.

## 2026-07-17, evidence sprint high-priority 01

- Збережено і виконано промпт: `project/ide-codex-evidence-sprint-high-priority-01-prompt.md`.
- Створено evidence notes для першого high-priority пакета: 41, 45, 47, 54, 63, 64, 65-66, 72, 73.
- Нові файли: `notes/logion-041-evidence-en.md`, `notes/logion-045-evidence-en.md`, `notes/logion-047-evidence-en.md`, `notes/logion-054-evidence-en.md`, `notes/logion-063-evidence-en.md`, `notes/logion-064-evidence-en.md`, `notes/logion-065-066-evidence-en.md`, `notes/logion-072-evidence-en.md`, `notes/logion-073-evidence-en.md`.
- Оновлено `corpus/tables/logia-workflow-matrix.md`: для цих логій evidence note позначено як `YES`.
- Оновлено `reconstruction/earliest-sayings-gospel/inclusion-decisions-table.md` робочими рішеннями.
- Чистий український reader не змінювався. Найсильніші кандидати для майбутнього `INCLUDE_WITH_MARKER`: 41, 54, 72, 73; також перспективні 45, 47, 63, 64 після розщеплення.
- Наступний якісний крок: створити синоптичні control tables для 41, 54, 72, 73, а також повністю витягнути коптський текст для 63-65.

## 2026-07-17, повна класифікація корпусу v0.1

- Збережено і виконано промпт: `project/ide-codex-full-corpus-classification-prompt.md`.
- Створено документ `reconstruction/earliest-sayings-gospel/full-corpus-classification-v0.1.md`.
- Уперше класифіковано всі 114 логій за робочими кошиками: `CURRENT_READER_TEXT`, `HIGH_PRIORITY_DEEPENING`, `SECONDARY_PRIORITY_DEEPENING`, `CLUSTER_DEFER`, `LIKELY_SECONDARY_OR_FRAME`, `EXCLUDE_AS_SECONDARY`.
- Залишкові `NOT_DECIDED` у `corpus/tables/logia-workflow-matrix.md` замінено на робочі рішення.
- Синхронізовано ранні неповні статуси в `corpus/tables/logia-index.md`.
- Чистий український reader не змінювався; класифікація не є автоматичним включенням нових логій.
- Наступний якісний крок: evidence-note sprint для першого high-priority пакета, починаючи з 41, 45, 47, 54, 63, 64, 65-66, 72, 73.

## 2026-07-17, корпусний спринт 101-114: завершення первинного покриття

- Збережено і виконано промпт: `project/ide-codex-corpus-sprint-101-114-quality-prompt.md`.
- Створено первинні картки `corpus/cards/logion-101.md` - `corpus/cards/logion-114.md`.
- Логію 104 перетворено з контрольної картки на повну первинну корпусну картку.
- Оновлено `corpus/tables/logia-workflow-matrix.md`: у матриці більше немає логій зі статусом `NOT_STARTED`.
- Оновлено `corpus/tables/logia-index.md`: додано записи 101-114 з попередніми шарами, рішеннями й імовірнісними оцінками.
- Додатково доведено логію 14 з контрольної картки до повної первинної картки, щоб у матриці більше не лишалося `PARTIAL` корпусних прогалин.
- У завантажених P.Oxy. джерелах не знайдено extant Greek Thomas witness для логій 101-114; грецький шар для сильних кандидатів може бути тільки `Greek retroversion, hypothetical`.
- Найсильніші кандидати для майбутнього поглиблення: 101, 103, 104, 107, 109, 111, 113.
- Логії 102, 105, 106, 108, 110, 112 відкладено як polemical, birth/identity, unity, mystical-transmission, world-renunciation або body/soul clusters.
- Логія 114 отримала попереднє рішення `EXCLUDE_AS_SECONDARY` як імовірно пізній редакційний/спільнотний матеріал.
- Чистий український reader не змінювався; цей спринт завершив первинне корпусне покриття.
- Наступний якісний крок: загальна класифікація всіх 114 логій і формування списку high-candidate deepening set для evidence notes та можливого розширення реконструкції.

## 2026-07-17, корпусний спринт 81-100: первинні картки

- Виконано збережений промпт: `project/ide-codex-corpus-sprint-081-100-quality-prompt.md`.
- Створено первинні картки `corpus/cards/logion-081.md` - `corpus/cards/logion-100.md`.
- Оновлено `corpus/tables/logia-workflow-matrix.md`: логії 81-100 більше не мають статусу `NOT_STARTED`.
- Оновлено `corpus/tables/logia-index.md` попередніми шарами, рішеннями й імовірнісними оцінками для 81-100.
- У завантажених P.Oxy. джерелах не знайдено extant Greek witness для логій 81-100; для сильних синоптичних одиниць грецький шар може бути лише `Greek retroversion, hypothetical`.
- Найсильніші кандидати для майбутнього поглиблення: 86, 89, 90, 91, 92, 93, 94, 95, 96, 99, 100.
- Логії 83, 84, 85, 87, 88 і 98 відкладено як image/light, Adam/anthropology, body/soul, angelic-prophetic або violent-kingdom clusters.
- Чистий український reader не змінювався; цей спринт був корпусним, а не реконструкційним.
- Наступний якісний крок: виконати Sprint H для логій 101-114, щоб завершити первинне покриття всього корпусу.

## 2026-07-17, промпт для корпусного спринту 81-100

- Збережено якісний робочий промпт: `project/ide-codex-corpus-sprint-081-100-quality-prompt.md`.
- Промпт фіксує наступний корпусний крок: створити первинні картки для логій 81-100, перевірити коптський текст, грецький статус, паралелі, робочі переклади й попередні рішення.
- Окремо зафіксовано обмеження: не розширювати чистий український читацький текст без доказового рішення й окремого апарату.
- Оновлено `project/project-map.md`.

## 2026-07-17, очищення українського читацького тексту

- Оновлено `reconstruction/earliest-sayings-gospel/reconstructed-gospel-uk.md`: прибрано вступний статус, дисклеймери, квадратні дужки й редакційні ярлики.
- Чистий український текст тепер починається одразу з пронумерованих логій і використовує загальноприйняті номери повного Євангелія від Фоми.
- Створено окремий концептуальний документ `project/clean-reader-text-first-page-principle.md`.
- Уся інформація про статус, маркери, непевність, часткове включення і пояснення має лишатися в другому шарі: `reader-commentary-uk.md`, `reconstructed-gospel-uk-apparatus.md`, `parallel-edition.md`, `evidence-dossier-en.md`.
- Оновлено `project/clean-text-plus-commentary-concept.md`, `project/final-product-specification.md`, `project/ide-codex-master-project-prompt.md`, `project/project-map.md` і `reconstruction/earliest-sayings-gospel/README.md`.

## 2026-07-17, корпусний спринт 61-80: первинні картки

- Виконано збережений промпт: `project/ide-codex-corpus-sprint-061-080-quality-prompt.md`.
- Створено первинні картки `corpus/cards/logion-061.md` - `corpus/cards/logion-080.md`.
- Оновлено `corpus/tables/logia-workflow-matrix.md`: логії 61-80 більше не мають статусу `NOT_STARTED`.
- Оновлено `corpus/tables/logia-index.md` попередніми шарами, рішеннями й імовірнісними оцінками для 61-80.
- Новий чистий український reader не змінювався; цей спринт був корпусним, а не реконструкційним.
- Єдиний завантажений грецький контроль у цьому блоці: P.Oxy. 1 overlap для Logion 77b (`split wood / lift stone`). Для решти 61-80 немає loaded extant Greek Thomas witness.
- Найсильніші кандидати для наступного поглиблення: 63, 64, 65, 66, 68, 69, 72, 73, 76, 78, 79.
- Логії 61, 70, 71, 74, 75, 77, 80 відкладено як cluster/dialogue/Thomasine-symbolic material.
- Наступний якісний крок: або поглибити high-candidate block 63-66 / 72-79, або продовжити первинне покриття Sprint G, Logia 81-100.

## 2026-07-17, перший український читацький коментар до включених логій

- Збережено промпт: `project/ide-codex-reader-commentary-first-pass-prompt.md`.
- Виконано перший повний коментарний прохід для всіх одиниць, уже включених у `reconstruction/earliest-sayings-gospel/reconstructed-gospel-uk.md`.
- Оновлено `reconstruction/earliest-sayings-gospel/reader-commentary-uk.md`: замість шаблону створено розділи для логій 1, 2, 3, 4, 5, 6 ethical core, 9 core, 10 core, 16 core, 20, 22 core, 25, 26, 31, 32, 33, 34, 35, 36, 39.
- Коментарі подані українською й відокремлені від чистого реконструйованого тексту.
- Для кожної одиниці зафіксовано короткий сенс, джерельну базу, грецький статус, паралелі, можливі тлумачення, непевності й причину включення.
- Наступний якісний крок: зробити редакційний другий прохід по коментарях із додаванням точніших цитат першоджерел і коротких бібліографічних посилань там, де це правомірно.

## 2026-07-17, розширення фінальної моделі: український читацький коментар

- Зафіксовано нову вимогу до фінального продукту: після чистого реконструйованого тексту має йти окремий український коментар до кожної включеної логії.
- Створено окремий концептуальний документ `project/clean-text-plus-commentary-concept.md`.
- Оновлено `project/final-product-specification.md`.
- Оновлено `project/ide-codex-master-project-prompt.md`.
- Оновлено `project/project-completion-roadmap.md`.
- Оновлено `project/project-map.md`.
- Створено робочий файл `reconstruction/earliest-sayings-gospel/reader-commentary-uk.md`.
- Коментар має пояснювати походження, джерела, канонічні паралелі, можливі тлумачення, непевності й причини включення, але не має бути частиною самого реконструйованого тексту.

## 2026-07-17, корпусний спринт 40-60: первинні картки

- Виконано збережений промпт: `project/ide-codex-corpus-sprint-040-060-quality-prompt.md`.
- Створено первинні картки `corpus/cards/logion-040.md` - `corpus/cards/logion-060.md`.
- Оновлено операційну матрицю `corpus/tables/logia-workflow-matrix.md`: логії 40-60 більше не мають статусу `NOT_STARTED`.
- Оновлено індекс `corpus/tables/logia-index.md` попередніми шарами, ймовірностями й рішеннями для 40-60.
- Для логій 40-60 не знайдено завантаженого P.Oxy. грецького свідка; будь-яка грецька форма на цьому етапі має позначатися як `Greek retroversion, hypothetical`.
- Найсильніші кандидати для наступного поглиблення: 41, 44, 45, 46, 47, 54, 55, 57.
- Логії 43 і 53 відкладено як кластерні/практичні контрольні випадки; логії 49, 50, 56, 59, 60 потребують обережної перевірки як томині тематичні кластери.
- Український читацький текст не оновлювався: цей спринт мав на меті повне первинне покриття блоку, а не фінальне включення.

## 2026-07-17, розщеплення і класифікація логії 11

- Збережено промпт: `project/ide-codex-logion-011-composite-split-prompt.md`.
- Створено синоптичну таблицю: `controls/synoptic-parallels/logion-011-heaven-passing-controls.md`.
- Створено evidence note: `reconstruction/earliest-sayings-gospel/notes/logion-011-evidence-en.md`.
- Логія 11 оновлена до рішення `UNCERTAIN`.
- До українського читацького тексту не додано новий вислів; оновлено лише пояснення, що логія 11 лишається поза головним текстом.
- Найсильніша підодиниця - `це небо мине / те, що над ним, мине` - має частковий контроль у Мк 13:31, Мт 24:35, Лк 21:33, але форма Фоми відрізняється від синоптичної.
- Підодиниці про мертвих/живих, їжу мертвого, світло і один/два залишені в апараті як томина символічна композиція.

## 2026-07-17, поглиблення логії 10: вогонь на світ

- Збережено промпт: `project/ide-codex-logion-010-fire-core-deepening-prompt.md`.
- Створено синоптичну таблицю: `controls/synoptic-parallels/logion-010-fire-luke-control.md`.
- Створено evidence note: `reconstruction/earliest-sayings-gospel/notes/logion-010-evidence-en.md`.
- Логія 10 оновлена до рішення: коротке ядро `INCLUDE_WITH_MARKER`; повна логія 10 `UNCERTAIN`.
- До українського читацького тексту v1.3 додано тільки ядро: `Я кинув вогонь на світ`.
- Продовження `і пильную його, доки він не спалахне` залишено в апараті.
- Зафіксовано: для Фоми 10 немає завантаженого P.Oxy. грецького свідка; будь-яка грецька форма має бути позначена `Greek retroversion, hypothetical`.

## 2026-07-17, фіналізація короткого ядра логії 9

- Збережено промпт: `project/ide-codex-logion-009-sower-core-finalization-prompt.md`.
- Створено фінальну контрольну таблицю: `controls/synoptic-parallels/logion-009-sower-core-final-controls.md`.
- Логія 9 оновлена до рішення: коротке неалегоричне ядро `INCLUDE_WITH_MARKER`; повна логія 9 `UNCERTAIN`.
- До українського читацького тексту v1.2 додано тільки ядро: сіяч, дорога, камінь, терня, добра земля, плід.
- Деталі `черв'як`, `плід угору до неба` і `60 / 120` залишені в апараті.
- Зафіксовано: для Фоми 9 немає завантаженого P.Oxy. грецького свідка; будь-яка грецька форма має бути позначена `Greek retroversion, hypothetical`.

## 2026-07-17, поглиблення логії 9: притча про сіяча

### Що додано

- Створено `controls/synoptic-parallels/logion-009-sower.md`.
- Створено `reconstruction/earliest-sayings-gospel/notes/logion-009-evidence-en.md`.
- Оновлено `corpus/cards/logion-009.md` до поглибленої картки v0.2.
- Оновлено `corpus/tables/logia-index.md`.
- Оновлено `corpus/tables/logia-workflow-matrix.md`.
- Оновлено `reconstruction/earliest-sayings-gospel/inclusion-decisions-table.md`.
- Оновлено `reconstruction/earliest-sayings-gospel/evidence-dossier-en.md`.

### Джерела

- Thomas 9: коптський текст із `coptic/linssen-thomas-coptic-unicode-working.txt`.
- Для Thomas 9 у завантажених P.Oxy. 1, 654, 655 грецького свідчення немає.
- Синоптичний контроль: SBLGNT, Мк 4:3-9, Мт 13:3-9, Лк 8:5-8, локальний кеш `/tmp/euagelia-sblgnt`.

### Рішення

- Логія 9 піднята з `NOT_DECIDED` до `UNCERTAIN`.
- В український читацький текст її не додано.
- Можливе раннє ядро: притча про сіяча без алегоричного тлумачення.

### Наступна дія

Порівняти алегоричні тлумачення притчі в Мк 4:13-20, Мт 13:18-23 і Лк 8:11-15; окремо перевірити деталі Фоми `60 / 120` і `черв'як`.

## 2026-07-17, інфраструктура завершення проєкту

### Що додано

- Збережено магістральний промпт `project/ide-codex-project-completion-pipeline-prompt.md`.
- Створено `project/project-completion-roadmap.md` з фазами завершення, критеріями готовності логії й пакетами роботи.
- Створено `corpus/tables/logia-workflow-matrix.md` - повну операційну матрицю для 114 логій.
- Створено `project/next-sprint-logia-008-013-prompt.md` як наступний виконуваний пакет.
- Оновлено `project/project-map.md`.

### Рішення

- Не виставляти штучні рішення для неопрацьованих логій.
- Для неопрацьованих логій використовувати `NOT_STARTED`.
- Наступним корпусним кроком визначено Sprint A: логії 8-13.

### Поточний висновок

Проєкт має перейти від одиничних поглиблень до пакетної роботи по корпусу. Найближчий якісний приріст - створити первинні картки для логій 8-13 і після цього поступово закривати прогалини між уже опрацьованими P.Oxy.-кластерами.

## 2026-07-17, Sprint A: первинні картки логій 8-13

### Що додано

- Створено `corpus/cards/logion-008.md`.
- Створено `corpus/cards/logion-009.md`.
- Створено `corpus/cards/logion-010.md`.
- Створено `corpus/cards/logion-011.md`.
- Створено `corpus/cards/logion-012.md`.
- Створено `corpus/cards/logion-013.md`.
- Оновлено `corpus/tables/logia-index.md`.
- Оновлено `corpus/tables/logia-workflow-matrix.md`.

### Джерела

- Коптський текст узято з `coptic/linssen-thomas-coptic-unicode-working.txt`.
- Перевірено статус грецьких свідків за `source-register.md` і `greek_poxy/README.md`: для логій 8-13 у завантажених P.Oxy. 1, 654, 655 грецького свідчення немає.
- Контрольний переклад Mattison / Gospels.net використано лише як допоміжний контроль, не як первинну базу.

### Рішення

- Для логій 8-13 виставлено `NOT_DECIDED`, щоб не симулювати фінальну впевненість.
- Логія 9 позначена як високопріоритетна для поглиблення через сильні синоптичні паралелі притчі про сіяча.
- Логії 12-13 поки не додавати до читацької реконструкції: вони виглядають як громадовий / рамковий матеріал і потребують окремої аргументації.

### Наступна дія

Створити синоптичну таблицю для логії 9 з Мк 4, Мт 13 і Лк 8 або перейти до Sprint B для логій 15-26.

## 2026-07-17, український читацький текст v0.3

### Що додано

- Збережено промпт `project/ide-codex-uk-reader-v03-prompt.md`.
- Оновлено `reconstruction/earliest-sayings-gospel/reconstructed-gospel-uk.md` до чистішої читацької версії v0.3.
- Створено `reconstruction/earliest-sayings-gospel/reconstructed-gospel-uk-apparatus.md` з коротким українським поясненням маркерів, ядра й можливих розгортань.
- Оновлено `reconstruction/earliest-sayings-gospel/README.md`.

### Рішення

- Логії 1-5 лишаються `INCLUDE_WITH_MARKER`.
- Логії 6-7 не додано до головного українського тексту, бо вони лишаються `UNCERTAIN`.
- Технічні примітки винесено з основного читацького тексту в український апарат.

### Наступна дія

Після цього можна або розширювати читацький текст наступним блоком логій, або спершу провести швидкий первинний відбір логій 8-13 / 8-20.

## 2026-07-17, ритуально-етичний кластер логій 6, 14, 27 і 104

### Що додано

- Створено `controls/synoptic-parallels/logion-006-matthew-6-ritual-practice.md`.
- Створено контрольні картки `corpus/cards/logion-014.md`, `logion-027.md`, `logion-104.md`.
- Створено англомовну кластерну нотатку `reconstruction/earliest-sayings-gospel/notes/ritual-ethics-cluster-006-014-027-104-en.md`.
- Оновлено картку логії 6, індекс логій, evidence note, evidence dossier і таблицю включення.

### Джерела

- Коптський текст логій 14, 27 і 104 взято з локального робочого Unicode-файлу Martijn Linssen: `coptic/linssen-thomas-coptic-unicode-working.txt`.
- Грецьке свідчення логії 27 звірено з DCLP / P.Oxy. 1: `greek_poxy/dclp-poxy1-62838.xml`.
- Для логій 14 і 104 у завантажених P.Oxy. 1, 654, 655 грецького свідчення не зафіксовано.
- Синоптичні грецькі контролі взято з SBLGNT: https://github.com/Faithlife/SBLGNT.
- Didache 8 перевірено як ранньохристиянський контроль для посту й молитви: https://greekdoc.com/DOCUMENTS/early/didache.html.

### Рішення

- Логія 6 лишається `UNCERTAIN`; імовірності не змінено: 10 / 25 / 40 / 25.
- Логії 14, 27 і 104 позначено як `DEFER` і використано як контрольні одиниці для ритуально-етичного кластера.
- Головний реконструйований текст не оновлювався, бо немає нового включення.

### Наступна дія

Ізолювати коротке можливе ядро логії 6 - "не брешіть і не робіть того, що ненавидите" - і перевірити його за незалежними єврейськими, мудрісними та ранньохристиянськими етичними паралелями.

## 2026-07-17, синоптичні evidence tables для логій 3-5

### Що додано

- Створено `controls/synoptic-parallels/logion-003-luke-17-kingdom.md`.
- Створено `controls/synoptic-parallels/logion-004-first-last.md`.
- Створено `controls/synoptic-parallels/logion-005-hidden-revealed.md`.

### Джерела

- Для Фоми використано локальні коптські й грецькі робочі файли NHC II,2 і P.Oxy. 654.
- Для синоптичного грецького контролю використано SBLGNT з репозиторію Faithlife / LogosBible: https://github.com/Faithlife/SBLGNT, ліцензія CC BY 4.0.
- Це продовжує стандарт, уже застосований для логії 2.

### Рішення

- Логія 3: `INCLUDE_WITH_MARKER` лишається без зміни; Лк 17:20-21 посилює мотив не-локалізованого царства, але не доводить прямої залежності.
- Логія 4: `INCLUDE_WITH_MARKER` лишається без зміни; синоптики сильно підтримують ядро перші/останні, але не семиденного малого і не фінал "стати одним".
- Логія 5: `INCLUDE_WITH_MARKER` лишається без зміни; синоптики сильно підтримують ядро приховане/явне, але не вступ "перед твоїм обличчям".

### Оновлено

- Картки логій 3-5.
- Evidence notes логій 3-5.
- Англомовний `evidence-dossier-en.md`.

### Наступна дія

Після цього логічно або звірити ці три таблиці з академічними виданнями NA28 / UBS5 / Attridge / Layton, або перейти до блоку логій 6, 14, 27 і 104, щоб вирішити ритуально-етичний комплекс перед можливим включенням логії 6.

## 2026-07-17, масштабування еталону логії 2 на логії 1 і 3-7

### Що додано

- Створено джерельні аудити для логій 1 і 3-7 у `notes/logion-00X-source-verification.md`.
- Створено англомовні evidence notes для логій 1 і 3-7 у `reconstruction/earliest-sayings-gospel/notes/`.
- Оновлено картки логій 1 і 3-7 рішеннями, імовірностями, шаруванням і публікаційними нотатками.
- Оновлено перший реконструкційний блок логій 1-5 українською та англійською.
- Оновлено коптську базу, грецькі свідки, паралельну таблицю, таблицю включення й англомовний evidence dossier.

### Реконструкційні рішення

- Логії 1, 2, 3, 4, 5: `INCLUDE_WITH_MARKER`.
- Логії 6, 7: `UNCERTAIN`, не включено в головний реконструйований текст.

### Методологічна межа

Це робоча реконструкція v0.2, не фінальне академічне видання. Для публікації потрібна звірка з академічними виданнями, повні синоптичні таблиці й окремий пошук ширших паралелей для непаралельного матеріалу.

## 2026-07-17

### Що зроблено

- Створено структуру папок для первинних текстів:
  - `coptic`
  - `greek_poxy`
  - `synoptic_parallels`
  - `translations`
  - `notes`
- Створено план корпусу: `SOURCE_CORPUS_PLAN.md`.
- Створено реєстр джерел: `source-register.md`.
- Перевірено кілька відкритих онлайн-орієнтирів для початкового етапу.

### Перевірені онлайн-орієнтири

- Brill Coptic Gnostic Library Online: містить Nag Hammadi Codex II,2, Gospel of Thomas, стор. 32.10-51.28; ресурс заявляє наявність коптського тексту й перекладу. Статус: авторитетний, але імовірно ліцензійний.
- Gospels.net, Mark M. Mattison translation: сайт прямо зазначає, що переклад public domain і базується на коптському тексті NHC II,2. Статус: відкритий допоміжний переклад, не первинний текст.
- K. C. Hanson page: дає стислу таблицю рукописів, мов, дат, місць зберігання, діапазонів логій і синоптичних паралелей. Статус: зручний навчальний ресурс, потребує академічної звірки.
- Gnosis Archive / Gnostic Society Library: у пошуку підтверджено наявність сторінок Oxyrhynchus fragments, Lambdin translation, Thomas collection і bibliography. Пряме відкриття частини сторінок через інструмент було нестабільним. Статус: потрібно повторно перевірити вручну або іншим способом.
- Papyri.info / DCLP: сторінка P.Oxy. 654 знайдена в пошуку, але прямий доступ заблокований перевіркою. Статус: потрібно перевірити вручну.

### Що не зроблено

- Повний коптський текст не внесено.
- Повні грецькі фрагменти P.Oxy. 1, 654, 655 не внесено.
- Синоптичні паралелі не зібрано в окрему таблицю.
- Український переклад не створено.
- 114 карток логій не створено і не заповнено.

### Сумніви й обмеження

- Потрібно розділити відкриті переклади, ліцензійні академічні видання й первинні рукописні свідчення.
- Не можна використовувати сучасні переклади як основу для реконструкції без коптського/грецького тексту.
- Потрібно перевірити, які саме першодруки Grenfell & Hunt перебувають у public domain і чи можна внести їхні транскрипції.
- Потрібно визначити одне базове видання грецького Нового Завіту для синоптичних паралелей.

### Наступні дії

1. Знайти або отримати надійну коптську транскрипцію NHC II,2.
2. Знайти першодруки або надійні транскрипції P.Oxy. 1, 654, 655.
3. Окремо створити таблицю `synoptic_parallels/thomas-synoptic-parallels.md`.
4. Визначити правила цитування й авторських прав для кожного джерела.
5. Почати пробну логію з блоку 1-7, бажано з логії 1 або 2, бо цей блок має грецьке свідчення P.Oxy. 654.

## 2026-07-17, доповнення

### Що додано після перевірки папок

- У `coptic` збережено знімки Gospel-Thomas.net / Michael W. Grondin:
  - головна сторінка ресурсу;
  - індекс інтерлінійного перекладу;
  - індекс логій;
  - індекс факсиміле;
  - HTML-сторінки й GIF-зображення інтерлінійного матеріалу для логій 1-7.
- У `greek_poxy` збережено:
  - сторінку Gnosis Archive для Oxyrhynchus fragments;
  - сторінки Agraphos для P.Oxy. 1, P.Oxy. 654, P.Oxy. 655;
  - GIF-зображення грецького тексту для P.Oxy. 1, 654, 655.

### Важливе уточнення

Папки тепер не порожні й містять реальні джерельні матеріали. Проте це ще не фінальний машинний корпус:

- коптський матеріал Grondin переважно поданий як зображення інтерлінійника;
- грецький матеріал Agraphos переважно поданий як зображення грецького тексту;
- потрібна наступна ітерація: OCR або ручне перенесення в Unicode, після чого звірка з академічними виданнями.

### Найкращий наступний крок

Створити робочі транскрипції для логій 1-7:

- `coptic/logia-001-007-coptic-working.md`;
- `greek_poxy/poxy654-transcription-working.md`;
- `translations/logia-001-007-control-translations.md`.

## 2026-07-17, завантаження відкритих текстів

### Що додано

- У `coptic` завантажено відкриту Unicode-транскрипцію Martijn Linssen:
  - `linssen-thomas-unicode-transcription-snapshot.html`;
  - `linssen-thomas-coptic-unicode-working.txt`.
- У `greek_poxy` завантажено DCLP / Papyri.info TEI/EpiDoc XML з GitHub `papyri/idp.data`:
  - `dclp-poxy1-62838.xml`;
  - `dclp-poxy654-62840.xml`;
  - `dclp-poxy655-62839.xml`.
- У `notes` завантажено довідкові snapshots:
  - `gospels-net-manuscript-snapshot.html`;
  - `nasscal-poxy1-snapshot.html`;
  - `nasscal-poxy654-snapshot.html`;
  - `nasscal-poxy655-snapshot.html`.

### Статус джерел

- Коптський текст тепер є в машинному вигляді для всіх 114 логій, але має статус робочої відкритої транскрипції, яку треба звіряти з факсиміле / Grondin / Brill / Layton.
- Грецькі фрагменти тепер є в TEI/EpiDoc XML під CC BY 3.0 і можуть бути базою для першої роботи, з обов'язковою атрибуцією DCLP.
- Papyri.info напряму блокує автоматичний доступ, але raw XML доступний через GitHub.

### Наступна дія

Створити для P.Oxy. 654 окремий читабельний робочий файл з рядками, лакунами й варіантами, а потім зіставити його з коптськими логіями 1-7.

## 2026-07-17, перша пілотна ітерація

### Що створено

- `greek_poxy/poxy654-transcription-working.md` - читабельний робочий витяг P.Oxy. 654 за рядками 1-42.
- `coptic/logia-001-007-coptic-working.md` - коптський робочий блок прологу й логій 1-7.
- `notes/logia-001-007-greek-coptic-alignment.md` - перша таблиця зіставлення грецького й коптського текстів.
- `corpus/cards/logion-002.md` - перша пілотна картка логії.

### Методологічне рішення

Історичні ймовірності для логії 2 не виставлено. На цьому етапі картка фіксує тільки текстові свідчення, початковий переклад і місця, які треба перевірити. Це відповідає головній меті проєкту: не датувати логії до того, як зібраний і звірений корпус.

### Наступна дія

Звірити логію 2 за факсиміле / Grondin / DCLP XML і після цього додати контрольні переклади та синоптичні паралелі.

## 2026-07-17, виконання збереженого промпта

### Що додано

- `sources/primary_texts/translations/logia-001-007-control-translations.md` - контрольні нотатки за відкритим public domain перекладом Mark M. Mattison / Gospels.net і таблиці паралелей для логій 1-7.
- `corpus/cards/logion-001.md` - пілотна картка логії 1.
- `corpus/cards/logion-003.md` - пілотна картка логії 3.
- `corpus/cards/logion-004.md` - пілотна картка логії 4.
- `corpus/cards/logion-005.md` - пілотна картка логії 5.
- `corpus/cards/logion-006.md` - пілотна картка логії 6.
- `corpus/cards/logion-007.md` - пілотна картка логії 7.
- `corpus/tables/logia-index.md` оновлено для логій 1-7.

### Методологічне рішення

Картки 1-7 залишаються корпусним шаром: внесено коптський текст, грецький P.Oxy. 654, буквальний український переклад, контрольні переклади й початкові паралелі. Історичні ймовірності не виставлялися, щоб не змішувати збір корпусу з датувальним аналізом.

### Наступна дія

Поглибити одну логію як повний зразок методу. Найкращий кандидат - логія 2, бо вона коротка, має повний коптський текст, грецький фрагмент і чітко обмежені тематичні паралелі Мт 7:7 / Лк 11:9.

## 2026-07-17, поглиблення логії 2 як еталону

### Що додано

- `project/ide-codex-logion-002-deepening-prompt.md` - промпт для поглиблення логії 2 як першого еталону методу.
- `controls/synoptic-parallels/logion-002-matthew-luke.md` - окреме зіставлення Фоми 2 з Мт 7:7 і Лк 11:9.
- `corpus/cards/logion-002.md` оновлено до еталонної аналітичної картки v0.1.
- `corpus/tables/logia-index.md` оновлено першою робочою оцінкою для логії 2.

### Методологічне рішення

Для логії 2 вперше виставлено обережний імовірнісний розподіл: 20% до 60 року, 35% для 60-90 років, 35% для 90-130 років, 10% після 130 року. Це не остаточна дата і не оцінка всього Євангелія від Фоми, а робоча експертна оцінка саме цієї логії.

### Наступна дія

Перевірити синоптичний матеріал за обраним критичним грецьким текстом, а також окремо дослідити мотив `спокою / відпочинку` у Фоми, бо саме він є ключем до розбіжності між грецьким P.Oxy. 654 і коптським NHC II,2.

## 2026-07-17, логія 2 як відкрито перевірений стандарт

### Що додано

- `project/ide-codex-logion-002-gold-standard-prompt.md` - промпт для доведення логії 2 до відкрито перевіреного стандарту.
- `sources/primary_texts/notes/logion-002-source-verification.md` - audit trail джерельної перевірки логії 2.
- `research/methodology/logion-rating-rubric.md` - рубрика оцінювання окремої логії.
- `sources/primary_texts/coptic/facsimiles/grondin-nhc2p32-scan0001.jpg` - факсиміле NHC II p.32.
- `sources/primary_texts/coptic/facsimiles/grondin-nhc2p32-color.jpg` - кольоровий контрольний знімок сторінки 32.
- `sources/primary_texts/coptic/facsimiles/grondin-nhc2-display-32-33.jpg` - display leaf сторінок 32-33.
- `controls/synoptic-parallels/logion-002-matthew-luke.md` оновлено точними формами Мт 7:7 і Лк 11:9 за SBLGNT.
- `corpus/cards/logion-002.md` оновлено до відкрито перевіреної еталонної картки v0.2.

### Методологічне рішення

Логія 2 тепер вважається не остаточно академічно закритою, а відкрито перевіреною: локально є коптський текст, грецький DCLP XML, факсиміле сторінки, синоптична звірка й рубрика оцінювання. Повна колація з Brill / Layton лишається окремим публікаційним або ліцензійним кроком.

### Наступна дія

Масштабувати цей стандарт на логії 1 і 3-7: для кожної створити audit-файл, синоптичну / несиноптичну звірку, застосувати рубрику й лише потім виставити ймовірнісний розподіл.

## 2026-07-17, перший зразок фінальної реконструкції

### Що додано

- `project/ide-codex-build-first-reconstruction-sample-prompt.md` - промпт для створення першого зразка фінальної реконструкції.
- `reconstruction/earliest-sayings-gospel/README.md` - опис папки майбутньої реконструкції.
- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-uk.md` - український читацький шар, наразі з логією 2.
- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-coptic.md` - коптський базовий шар.
- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-greek.md` - грецький засвідчений шар.
- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-en.md` - англійський читацький шар.
- `reconstruction/earliest-sayings-gospel/parallel-edition.md` - перший паралельний рядок для логії 2.
- `reconstruction/earliest-sayings-gospel/inclusion-decisions-table.md` - перше рішення `INCLUDE_WITH_MARKER`.
- `reconstruction/earliest-sayings-gospel/evidence-dossier-en.md` - початковий англомовний доказовий корпус.
- `reconstruction/earliest-sayings-gospel/notes/logion-002-evidence-en.md` - детальна англомовна evidence note для логії 2.

### Методологічне рішення

Логія 2 перенесена в фінальний формат не як повністю очищений текст, а як перший приклад шарової реконструкції: раннє ядро `шукати / знайти` включене в основний текст, а послідовність `бути враженим / здивуватися / царювати / спочити` позначена як можливе томине розгортання.

### Наступна дія

Застосувати цей самий формат до логій 1 і 3-7, але не переносити їх у фінальну реконструкцію до створення evidence notes і рішень включення.

## 2026-07-17, Sprint B: первинні картки логій 15-25

### Що додано

- `corpus/cards/logion-015.md` - первинна картка логії 15.
- `corpus/cards/logion-016.md` - первинна картка логії 16.
- `corpus/cards/logion-017.md` - первинна картка логії 17.
- `corpus/cards/logion-018.md` - первинна картка логії 18.
- `corpus/cards/logion-019.md` - первинна картка логії 19.
- `corpus/cards/logion-020.md` - первинна картка логії 20.
- `corpus/cards/logion-021.md` - первинна картка логії 21.
- `corpus/cards/logion-022.md` - первинна картка логії 22.
- `corpus/cards/logion-023.md` - первинна картка логії 23.
- `corpus/cards/logion-024.md` - первинна картка логії 24 з окремою перевіркою P.Oxy. 655.
- `corpus/cards/logion-025.md` - первинна картка логії 25.
- `corpus/tables/logia-index.md` оновлено для логій 15-25.
- `corpus/tables/logia-workflow-matrix.md` оновлено для логій 15-25.

### Методологічне рішення

Усі логії 15-25 залишено зі статусом `NOT_DECIDED`. Логії 20, 22, 24 і 25 позначені як найперспективніші для поглиблення, але жодна не перенесена до читацької реконструкції без окремої evidence note.

Особливо важливо: P.Oxy. 655 перевірено для логії 24. Завантажений грецький файл має заголовок `gospel of Thomas 24 (?), 36-39` і фрагмент про явлення / бачення / роздягання, але не містить прямого грецького відповідника коптського світлового вислову логії 24. Тому грецький статус позначено як можливий і непевний.

### Наступна дія

Поглибити логію 20 як найкращий наступний короткий тест: створити синоптичну таблицю Thomas 20 / Mark 4:30-32 / Matthew 13:31-32 / Luke 13:18-19 і вирішити, чи є в ній раннє притчеве ядро для майбутньої реконструкції.

## 2026-07-17, поглиблення логії 20: притча про гірчичне зерно

### Що додано

- `project/ide-codex-logion-020-mustard-seed-deepening-prompt.md` - промпт для поглиблення логії 20.
- `controls/synoptic-parallels/logion-020-mustard-seed.md` - синоптична evidence table для Thomas 20 / Mark 4:30-32 / Matthew 13:31-32 / Luke 13:18-19.
- `reconstruction/earliest-sayings-gospel/notes/logion-020-evidence-en.md` - англомовна evidence note для логії 20.
- `corpus/cards/logion-020.md` оновлено до поглибленої картки v0.2.
- `corpus/tables/logia-index.md` оновлено probability assessment для логії 20.
- `corpus/tables/logia-workflow-matrix.md` оновлено статус логії 20.
- `reconstruction/earliest-sayings-gospel/inclusion-decisions-table.md` додано рішення для логії 20.
- `reconstruction/earliest-sayings-gospel/evidence-dossier-en.md` додано короткий summary логії 20.

### Методологічне рішення

Логію 20 переведено з `NOT_DECIDED` у `UNCERTAIN`. Притчеве ядро про мале гірчичне зерно, яке виростає і дає притулок птахам, має сильну підтримку в Марка, Матвія і Луки. Однак відсутній грецький свідок Thomas 20 у завантажених P.Oxy., а напрям залежності від синоптичної традиції не доведений.

### Наступна дія

Перевірити академічні коментарі щодо варіації `гілка / дерево` у Thomas 20, Mark 4:32, Matthew 13:32 і Luke 13:19. Після цього вирішити, чи можна переносити коротке ядро логії 20 до українського читацького тексту з маркером.

## 2026-07-17, логія 20: перевірка варіації гілка / дерево

### Що додано

- `project/ide-codex-logion-020-branch-tree-commentary-check-prompt.md` - промпт для точкової перевірки логії 20.
- `reconstruction/earliest-sayings-gospel/notes/logion-020-branch-tree-commentary-check-en.md` - англомовна нотатка щодо варіації `branch / tree`.

### Що оновлено

- `corpus/cards/logion-020.md` оновлено до v0.3.
- `controls/synoptic-parallels/logion-020-mustard-seed.md` доповнено висновком після перевірки.
- `reconstruction/earliest-sayings-gospel/notes/logion-020-evidence-en.md` оновлено до v0.2.
- `corpus/tables/logia-index.md`, `corpus/tables/logia-workflow-matrix.md`, `reconstruction/earliest-sayings-gospel/inclusion-decisions-table.md` і `reconstruction/earliest-sayings-gospel/evidence-dossier-en.md` синхронізовано.

### Методологічне рішення

Логія 20 залишається `UNCERTAIN`. Варіація `велика гілка` у Фоми і `великі гілки` у Марка зміцнює думку, що Фома 20 є важливим свідком мобільної притчевої традиції. Але вона не долає дві головні межі: немає грецького свідка Thomas 20 у завантажених P.Oxy., і напрям залежності від синоптичних форм не доведений.

### Наступна дія

Перейти до логії 22. Вона важлива для кінцевої мети, бо дає інший тип матеріалу: потенційно раннє ядро "малі діти і царство" плюс виразно томине розгортання "двох зробити одним".

## 2026-07-17, поглиблення логії 22: малі діти і царство

### Що додано

- `project/ide-codex-logion-022-children-kingdom-deepening-prompt.md` - промпт для поглиблення логії 22.
- `controls/synoptic-parallels/logion-022-children-kingdom.md` - синоптична evidence table для Thomas 22 / Mark 10 / Matthew 18-19 / Luke 18.
- `reconstruction/earliest-sayings-gospel/notes/logion-022-evidence-en.md` - англомовна evidence note для логії 22.

### Що оновлено

- `corpus/cards/logion-022.md` оновлено до v0.2.
- `corpus/tables/logia-index.md` додано probability assessment для логії 22.
- `corpus/tables/logia-workflow-matrix.md` оновлено статус логії 22.
- `reconstruction/earliest-sayings-gospel/inclusion-decisions-table.md` додано рішення для логії 22.
- `reconstruction/earliest-sayings-gospel/evidence-dossier-en.md` додано summary логії 22.

### Методологічне рішення

Логія 22 переведена з `NOT_DECIDED` у `UNCERTAIN`. Коротке ядро про малих дітей і тих, хто входить у царство, має сильні синоптичні паралелі. Але повна коптська форма містить довге розгортання про єдність протилежностей, яке слід вважати томиним або вторинним інтерпретивним шаром, доки не буде проведена ширша перевірка unity / monachos cluster.

### Наступна дія

Створити кластерну перевірку Thomas unity / monachos для логій 4, 11, 22, 23, 37, 75 і 106. Це потрібно, щоб вирішити, чи будь-які "стати одним" формули можуть входити до реконструкції, чи вони мають лишатися в апараті як томине богословське розгортання.

## 2026-07-17, кластерна перевірка Thomas unity / monachos

### Що додано

- `project/ide-codex-thomas-unity-monachos-cluster-prompt.md` - промпт для перевірки unity / monachos cluster.
- `reconstruction/earliest-sayings-gospel/notes/thomas-unity-monachos-cluster-en.md` - англомовна кластерна evidence note.

### Що оновлено

- `corpus/cards/logion-022.md` доповнено посиланням на кластерну перевірку.
- `corpus/cards/logion-023.md` оновлено до v0.2 і переведено в `UNCERTAIN`.
- `corpus/tables/logia-index.md` додано probability assessment для логії 23.
- `corpus/tables/logia-workflow-matrix.md` синхронізовано для логій 22 і 23.
- `reconstruction/earliest-sayings-gospel/inclusion-decisions-table.md` додано рішення для логії 23.
- `reconstruction/earliest-sayings-gospel/evidence-dossier-en.md` додано cluster summary.

### Методологічне рішення

Повторювана мова `стати одним`, `двох зробити одним`, `стояти як одне`, `monachos / solitary` тепер вважається попереджувальним маркером томиної богословської мови, якщо вона не має незалежної підтримки. Це не автоматичне виключення, але така мова не може сама по собі бути доказом найдавнішого шару.

### Наступна дія

Поглибити логію 16 як тестовий випадок: вона має сильне синоптичне ядро "не мир, а поділ" і фінал `monachos`, який тепер треба оцінювати як можливе томине завершення.

## 2026-07-17, поглиблення логії 16: не мир, а поділ

### Що додано

- `project/ide-codex-logion-016-division-monachos-deepening-prompt.md` - промпт для поглиблення логії 16.
- `controls/synoptic-parallels/logion-016-division-family.md` - синоптична evidence table для Thomas 16 / Matthew 10:34-36 / Luke 12:49-53.
- `reconstruction/earliest-sayings-gospel/notes/logion-016-evidence-en.md` - англомовна evidence note для логії 16.

### Що оновлено

- `corpus/cards/logion-016.md` оновлено до v0.2.
- `corpus/tables/logia-index.md` додано probability assessment для логії 16.
- `corpus/tables/logia-workflow-matrix.md` оновлено статус логії 16.
- `reconstruction/earliest-sayings-gospel/inclusion-decisions-table.md` додано рішення для логії 16.
- `reconstruction/earliest-sayings-gospel/evidence-dossier-en.md` додано summary логії 16.

### Методологічне рішення

Логія 16 переведена з `NOT_DECIDED` у `UNCERTAIN`. Ядро "не мир, а поділ / дім буде розділений" має сильну синоптичну підтримку, особливо через Лк 12:51-53. Але коптська форма Фоми поєднує Лукину структуру, Матвієвий меч, додаткову війну і томиний фінал `monachos`.

### Наступна дія

Поглибити логію 25 як коротку етичну логію: "люби брата як душу; бережи його як зіницю ока". Вона може дати більш придатний матеріал для реконструкції, ніж складні томині unity / monachos тексти.

## 2026-07-17, поглиблення логії 25: любов до брата

### Що додано

- `project/ide-codex-logion-025-love-brother-deepening-prompt.md` - промпт для поглиблення логії 25.
- `controls/synoptic-parallels/logion-025-love-brother.md` - evidence table для Thomas 25 / Lev 19:18 / Mark 12:31 / Matthew 22:39 / Luke 10:27 / біблійного образу зіниці ока.
- `reconstruction/earliest-sayings-gospel/notes/logion-025-evidence-en.md` - англомовна evidence note для логії 25.

### Що оновлено

- `corpus/cards/logion-025.md` оновлено до v0.2.
- `corpus/tables/logia-index.md` додано probability assessment для логії 25.
- `corpus/tables/logia-workflow-matrix.md` оновлено статус логії 25.
- `reconstruction/earliest-sayings-gospel/inclusion-decisions-table.md` додано рішення для логії 25.
- `reconstruction/earliest-sayings-gospel/evidence-dossier-en.md` додано summary логії 25.
- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-uk.md` оновлено до v0.4 і додано логію 25 з маркером.
- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-uk-apparatus.md` оновлено до v0.2.

### Методологічне рішення

Логія 25 переведена з `NOT_DECIDED` у `INCLUDE_WITH_MARKER`. Ядро любові до брата / ближнього має сильну єврейську, синоптичну і ранньохристиянську підтримку. Маркер лишається потрібним, бо Фома має `брат`, а не ширше `ближній`, друга половина про зіницю ока може бути мудрісним розширенням, і немає завантаженого грецького Thomas 25.

### Наступна дія

Після позитивного рішення для логії 25 варто перейти до логії 26, бо вона має грецький P.Oxy. 1 і сильну синоптичну паралель про скалку / колоду в оці брата. Це допоможе повернутися до матеріалу з грецьким свідком.

## 2026-07-17, поглиблення логії 26: скалка і колода

### Що додано

- `project/ide-codex-logion-026-speck-beam-deepening-prompt.md` - промпт для поглиблення логії 26.
- `corpus/cards/logion-026.md` - поглиблена картка логії 26.
- `controls/synoptic-parallels/logion-026-speck-beam.md` - evidence table для Thomas 26 / P.Oxy. 1 / Matthew 7:3-5 / Luke 6:41-42.
- `reconstruction/earliest-sayings-gospel/notes/logion-026-evidence-en.md` - англомовна evidence note для логії 26.

### Що оновлено

- `corpus/tables/logia-index.md` додано логію 26.
- `corpus/tables/logia-workflow-matrix.md` оновлено логію 26.
- `reconstruction/earliest-sayings-gospel/inclusion-decisions-table.md` додано рішення для логії 26.
- `reconstruction/earliest-sayings-gospel/evidence-dossier-en.md` додано summary логії 26.
- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-uk.md` оновлено до v0.5 і додано логію 26 з маркером.
- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-uk-apparatus.md` оновлено до v0.3.

### Методологічне рішення

Логія 26 переведена з `NOT_STARTED` у `INCLUDE_WITH_MARKER`. Вона має сильний доказовий профіль: повний коптський текст, частковий грецький P.Oxy. 1 і близькі паралелі в Матвія та Луки. Маркер потрібен, бо грецький фрагмент зберігає тільки фінал і напрям залежності з синоптичною традицією не вирішений.

### Наступна дія

Продовжити блок P.Oxy. 1: перейти до логії 27, але не для автоматичного включення, а для повної картки fasting/Sabbath із грецьким свідком і зв'язком із уже створеним ritual-ethics cluster.

## 2026-07-17, поглиблення логії 27: піст від світу і субота як субота

### Що додано

- `project/ide-codex-logion-027-fasting-sabbath-poxy1-poxy5575-prompt.md` - промпт для поглиблення логії 27.
- `controls/synoptic-parallels/logion-027-fasting-sabbath.md` - evidence table для Thomas 27 / P.Oxy. 1 / P.Oxy. 5575 / fasting і Sabbath controls.
- `reconstruction/earliest-sayings-gospel/notes/logion-027-evidence-en.md` - англомовна evidence note для логії 27.
- `sources/primary_texts/greek_poxy/gospels-net-poxy5575-snapshot.html` - локальний snapshot Gospels.net для P.Oxy. 5575.
- `sources/primary_texts/notes/nasscal-poxy5575-snapshot.html` - локальний snapshot NASSCAL для P.Oxy. 5575.

### Що оновлено

- `corpus/cards/logion-027.md` оновлено з контрольної картки до поглибленої картки v0.2.
- `corpus/tables/logia-index.md` додано probability assessment для логії 27.
- `corpus/tables/logia-workflow-matrix.md` оновлено статус логії 27.
- `reconstruction/earliest-sayings-gospel/inclusion-decisions-table.md` оновлено рішення для логії 27.
- `reconstruction/earliest-sayings-gospel/evidence-dossier-en.md` додано summary логії 27.
- `reconstruction/earliest-sayings-gospel/notes/ritual-ethics-cluster-006-014-027-104-en.md` оновлено статус логії 27 у кластері.

### Методологічне рішення

Логія 27 переведена з `DEFER` у `UNCERTAIN`. Окреме дослідження виконано: текстово вона дуже важлива, бо має повний коптський текст, сильний грецький P.Oxy. 1 і додатковий ранній контроль P.Oxy. 5575. Але реконструкційно вона не входить до основного українського читача, бо її ключові формули - "постити щодо світу" і "зробити суботу суботою" - мають лише тематичні, а не прямі синоптичні паралелі й добре вписуються в ритуально-символічний томиний шар.

### Наступна дія

Повернутися до найперспективнішого незавершеного раннього ядра в ritual-ethics cluster: протестувати короткий етичний вислів логії 6 "не брешіть і не робіть того, що ненавидите" проти незалежних єврейських, мудрісних і ранньохристиянських паралелей.

## 2026-07-17, поглиблення логії 6: етичне ядро

### Що додано

- `project/ide-codex-logion-006-ethical-core-parallels-prompt.md` - промпт для тесту етичного ядра логії 6.
- `controls/synoptic-parallels/logion-006-ethical-core.md` - evidence table для короткого ядра "не брешіть / не робіть того, що ненавидите".

### Що оновлено

- `corpus/cards/logion-006.md` оновлено до v0.2.
- `reconstruction/earliest-sayings-gospel/notes/logion-006-evidence-en.md` оновлено до v0.2.
- `corpus/tables/logia-index.md` оновлено статус і ймовірності для логії 6.
- `corpus/tables/logia-workflow-matrix.md` оновлено рішення для логії 6.
- `reconstruction/earliest-sayings-gospel/inclusion-decisions-table.md` розділено рішення: етичне ядро `INCLUDE_WITH_MARKER`, повна логія `UNCERTAIN`.
- `reconstruction/earliest-sayings-gospel/evidence-dossier-en.md` оновлено до v0.3.
- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-uk.md` оновлено до v0.6 і додано коротке ядро логії 6.
- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-uk-apparatus.md` оновлено до v0.4.

### Методологічне рішення

Коротке етичне ядро логії 6 переведено в `INCLUDE_WITH_MARKER`:

> Не брешіть і не робіть того, що ненавидите.

Повна логія 6 лишається `UNCERTAIN`: не включено ритуальне питання про піст, молитву, милостиню і їжу; не включено hidden/revealed ending, бо цей мотив уже представлений у логії 5. Маркер потрібен, бо грецький P.Oxy. 654 має ключову частину фрази в реконструйованій лакуні.

### Наступна дія

Після додавання етичного ядра логії 6 варто перейти до логії 8 як ще не вирішеної притчі з можливим синоптичним контролем у Мт 13:47-50. Це дасть баланс між етичними висловами й притчевим матеріалом.

## 2026-07-17, уточнення політики грецької ретроверсії

### Що оновлено

- `project/final-product-specification.md` - додано третю категорію грецького шару: `Greek retroversion, hypothetical`.
- `research/methodology/logion-rating-rubric.md` - додано правило грецької ретроверсії для коптсько-збережених логій без extant Greek witness.
- `reconstruction/earliest-sayings-gospel/evidence-dossier-en.md` - додано `Greek Retroversion Policy`.

### Методологічне рішення

Відсутність збереженого грецького папірусу більше не трактується як причина не реконструювати грецький текст. Якщо коптський текст найімовірніше перекладає або зберігає традицію, що реально існувала грецькою, треба робити обережну грецьку ретроверсію.

Але така ретроверсія не є рукописним свідком. Вона має бути чітко позначена як `Greek retroversion, hypothetical` і мати рівень упевненості: `high`, `medium` або `low`.

## 2026-07-17, corpus completion sprint C: P.Oxy. 1 логії 28-33

### Що додано

- `project/ide-codex-corpus-completion-poxy1-logia-028-033-prompt.md` - промпт для первинного проходу P.Oxy. 1 логій 28-33.
- `corpus/cards/logion-028.md` - первинна картка: світ, сп'яніння, спрага, сліпота серця.
- `corpus/cards/logion-029.md` - первинна картка: плоть/дух/тіло, багатство в убогості.
- `corpus/cards/logion-030.md` - первинна картка: двоє/один, присутність Ісуса, зв'язок із 77b.
- `corpus/cards/logion-031.md` - первинна картка: пророк у батьківщині, лікар.
- `corpus/cards/logion-032.md` - первинна картка: місто на високій горі.
- `corpus/cards/logion-033.md` - первинна картка: почуте на вухо / дахи, лампа.

### Що оновлено

- `corpus/tables/logia-index.md` - додано логії 28-33.
- `corpus/tables/logia-workflow-matrix.md` - логії 28-33 переведено з `NOT_STARTED` у первинний корпусний статус.

### Методологічне рішення

Цей спринт не додає логії 28-33 до українського читача. Він закриває важливий структурний борг: наступний грецько-коптський блок P.Oxy. 1 більше не є порожньою зоною. Найперспективніші кандидати для наступного поглиблення: логії 31, 32 і 33, бо вони мають сильні синоптичні контролі.

### Наступна дія

Поглибити high-candidate підблок 31-33: пророк у батьківщині, місто на горі, лампа/дахи. Це може дати нові марковані одиниці для української реконструкції.

## 2026-07-17, поглиблення логій 31-33: P.Oxy. 1 high candidates

### Що додано

- `project/ide-codex-logia-031-033-high-candidate-deepening-prompt.md` - промпт для поглиблення логій 31-33.
- `controls/synoptic-parallels/logia-031-033-poxy1-synoptic-controls.md` - спільна таблиця P.Oxy. 1 / синоптичних контролів.
- `reconstruction/earliest-sayings-gospel/notes/logion-031-evidence-en.md` - evidence note для логії 31.
- `reconstruction/earliest-sayings-gospel/notes/logion-032-evidence-en.md` - evidence note для логії 32.
- `reconstruction/earliest-sayings-gospel/notes/logion-033-evidence-en.md` - evidence note для логії 33.

### Що оновлено

- `corpus/cards/logion-031.md`, `logion-032.md`, `logion-033.md` оновлено до v0.2.
- `corpus/tables/logia-index.md` і `logia-workflow-matrix.md` синхронізовано.
- `reconstruction/earliest-sayings-gospel/inclusion-decisions-table.md` додано рішення для логій 31-33.
- `reconstruction/earliest-sayings-gospel/evidence-dossier-en.md` оновлено до v0.4.
- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-uk.md` оновлено до v0.7 і додано логії 31-33.
- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-uk-apparatus.md` оновлено до v0.5.

### Методологічне рішення

Логії 31-33 переведено в `INCLUDE_WITH_MARKER`.

- Логія 31: ядро про пророка має сильні синоптичні контролі; фраза про лікаря лишається маркованим парним розгортанням.
- Логія 32: місто на горі має сильний P.Oxy. 1 і Мт 5:14 контроль; повніша форма Фоми лишається маркованою.
- Логія 33: включена як складена одиниця з двома ядрами; P.Oxy. 1 зберігає лише початок, тому ламповий блок потребує `Greek retroversion, hypothetical` у майбутньому грецькому шарі.

### Наступна дія

Після додавання 31-33 треба або поглибити логії 28-30, або продовжити corpus completion до P.Oxy. 655 блоку 36-39. Якщо мета - швидше збільшити надійний український текст, варто спершу поглибити 32/33 у грецькому/англійському паралельному шарі; якщо мета - закрити структурний борг, перейти до 36-39.

## 2026-07-17, corpus completion sprint D: P.Oxy. 655 логії 36-39

### Що додано

- `project/ide-codex-corpus-completion-poxy655-logia-036-039-prompt.md` - промпт для первинного проходу P.Oxy. 655 блоку 36-39.
- `corpus/cards/logion-036.md` - первинна картка: не турбуватися про одяг; ширший комплекс їжа/одяг/лілії.
- `corpus/cards/logion-037.md` - первинна картка: явлення, роздягання без сорому, малі діти, Син Живого.
- `corpus/cards/logion-038.md` - первинна картка: бажання чути слова; майбутнє шукання Ісуса.
- `corpus/cards/logion-039.md` - первинна картка: ключі знання; мудрі як змії і чисті як голуби.

### Що оновлено

- `corpus/tables/logia-index.md` - додано логії 36-39.
- `corpus/tables/logia-workflow-matrix.md` - логії 36-39 переведено з `NOT_STARTED` у первинний корпусний статус.

### Методологічне рішення

Цей спринт не додає логії 36-39 до українського читацького тексту. Він закриває важливий структурний борг: P.Oxy. 655 тепер представлений у корпусі як повноцінний блок.

Попередні висновки:

- Логія 36 перспективна через P.Oxy. 655, P.Oxy. 5575 і сильні синоптичні контролі, але треба відділити коротке коптське ядро від ширшого комплексу.
- Логія 37 має справжній грецький контроль, але її повна коптська форма виглядає сильно фомівською і лишається `UNCERTAIN`.
- Логія 38 має фрагментарний грецький контроль і лишається `UNCERTAIN`.
- Логія 39 перспективна, але майже напевно композитна; треба окремо оцінити "ключі знання" і "змії/голуби".

### Наступна дія

Поглибити Logion 36 і Logion 39 як найперспективніші одиниці P.Oxy. 655: створити evidence notes, синоптичну таблицю й вирішити, чи можна додати одне або два марковані ядра до української реконструкції.

## 2026-07-17, поглиблення логій 36 і 39: P.Oxy. 655 high candidates

### Що додано

- `project/ide-codex-logia-036-039-poxy655-high-candidate-deepening-prompt.md` - промпт для поглиблення P.Oxy. 655 high candidates.
- `controls/synoptic-parallels/logia-036-039-poxy655-synoptic-controls.md` - таблиця Coptic Thomas / P.Oxy. 655 / P.Oxy. 5575 / синоптичних контролів.
- `reconstruction/earliest-sayings-gospel/notes/logion-036-evidence-en.md` - evidence note для логії 36.
- `reconstruction/earliest-sayings-gospel/notes/logion-039-evidence-en.md` - evidence note для логії 39.

### Що оновлено

- `corpus/cards/logion-036.md` і `logion-039.md` оновлено до v0.2.
- `corpus/tables/logia-index.md` і `logia-workflow-matrix.md` синхронізовано.
- `reconstruction/earliest-sayings-gospel/inclusion-decisions-table.md` додано рішення для логій 36 і 39.
- `reconstruction/earliest-sayings-gospel/evidence-dossier-en.md` оновлено до v0.5.
- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-uk.md` оновлено до v0.8.
- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-uk-apparatus.md` оновлено до v0.6.

### Методологічне рішення

Логії 36 і 39 переведено в `INCLUDE_WITH_MARKER`.

- Логія 36: включено коротке ядро про відмову від тривоги щодо одягу. Ширший комплекс їжа/одяг/лілії/Божа турбота лишається в апараті, бо коптська форма коротша, P.Oxy. 655 фрагментарний, а P.Oxy. 5575 є раннім контролем змішаного sayings-середовища, не прямим рукописом Фоми.
- Логія 39: включено як дві марковані одиниці - ключі знання і змії/голуби. Не трактувати як одну немарковану первісну композицію.

### Наступна дія

Після додавання 36 і 39 найкращий наступний крок - пройти логії 34-35 як короткий міст між P.Oxy. 1 і P.Oxy. 655, або перейти до нового великого корпусного спринту 40-60. Якщо мета - швидше розширити український текст, варто спершу поглибити високі кандидати серед уже створених первинних карток 8, 20, 22, 28-30.

## 2026-07-17, bridge sprint: логії 34-35

### Що додано

- `project/ide-codex-logia-034-035-bridge-deepening-prompt.md` - промпт для закриття містка 34-35.
- `corpus/cards/logion-034.md` - поглиблена картка: сліпий веде сліпого.
- `corpus/cards/logion-035.md` - поглиблена картка: дім сильного, зв'язати і пограбувати.
- `controls/synoptic-parallels/logia-034-035-bridge-synoptic-controls.md` - синоптичні контролі для 34-35.
- `reconstruction/earliest-sayings-gospel/notes/logion-034-evidence-en.md` - evidence note для логії 34.
- `reconstruction/earliest-sayings-gospel/notes/logion-035-evidence-en.md` - evidence note для логії 35.

### Що оновлено

- `corpus/tables/logia-index.md` і `logia-workflow-matrix.md` синхронізовано.
- `reconstruction/earliest-sayings-gospel/inclusion-decisions-table.md` додано рішення для логій 34-35.
- `reconstruction/earliest-sayings-gospel/evidence-dossier-en.md` оновлено до v0.6.
- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-uk.md` оновлено до v0.9.
- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-uk-apparatus.md` оновлено до v0.7.

### Методологічне рішення

Логії 34-35 переведено в `INCLUDE_WITH_MARKER`.

Для обох немає extant Greek Thomas witness у завантажених Oxyrhynchus матеріалах, але грецька форма майже напевно реально існувала через сильні синоптичні грецькі контролі. Тому для грецького шару дозволена тільки позначена форма `Greek retroversion, hypothetical`.

### Наступна дія

Після закриття 31-39 без порожніх місць треба або перейти до нового корпусного спринту 40-60, або спершу поглибити найперспективніші вже створені кандидати без читача: 8, 20, 22, 28-30. Найбільш продуктивним для швидкого зростання української реконструкції виглядає поглиблення логій 8, 20 і 22.

## 2026-07-17, high-candidate review: логії 8, 20 і 22

### Що додано

- `project/ide-codex-high-candidate-logia-008-020-022-prompt.md` - промпт для high-candidate review.
- `controls/synoptic-parallels/logia-008-020-022-high-candidate-controls.md` - таблиця контролів для логій 8, 20 і 22.
- `reconstruction/earliest-sayings-gospel/notes/logion-008-evidence-en.md` - evidence note для логії 8.

### Що оновлено

- `corpus/cards/logion-008.md` оновлено до v0.2 і переведено в `UNCERTAIN`.
- `corpus/cards/logion-020.md` оновлено до v0.4 і переведено в `INCLUDE_WITH_MARKER`.
- `corpus/cards/logion-022.md` оновлено до v0.3: дитяче ядро `INCLUDE_WITH_MARKER`, повна логія `UNCERTAIN`.
- `reconstruction/earliest-sayings-gospel/notes/logion-020-evidence-en.md` оновлено до v0.3.
- `reconstruction/earliest-sayings-gospel/notes/logion-022-evidence-en.md` оновлено до v0.2.
- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-uk.md` оновлено до v1.0.
- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-uk-apparatus.md` оновлено до v0.8.
- `reconstruction/earliest-sayings-gospel/evidence-dossier-en.md` оновлено до v0.7.

### Методологічне рішення

- Логія 8 лишається `UNCERTAIN`: близькість до Мт 13:47-48 тематична, але не достатньо структурно пряма.
- Логія 20 включена з маркером як коротка притча про гірчичне зерно.
- Логія 22 включена з маркером тільки як дитяче ядро; unity-of-opposites expansion лишається в апараті.

Для логій 20 і 22 грецький шар має бути тільки `Greek retroversion, hypothetical`, бо extant Greek Thomas witness у завантажених P.Oxy. матеріалах немає.

### Наступна дія

Після додавання 20 і 22 найкращий наступний крок - поглибити логію 16 як test case для відділення сильного синоптичного ядра "не мир, а поділ" від томиного monachos ending, або перейти до корпусного спринту 40-60.

## 2026-07-17, фіналізація ядра логії 16: не мир, а поділ

### Що додано

- `project/ide-codex-logion-016-division-core-finalization-prompt.md` - промпт для фіналізації ядра логії 16.
- `controls/synoptic-parallels/logion-016-division-core-final-controls.md` - таблиця остаточного розділення шарів логії 16.

### Що оновлено

- `corpus/cards/logion-016.md` оновлено до v0.3.
- `reconstruction/earliest-sayings-gospel/notes/logion-016-evidence-en.md` оновлено до v0.2.
- `corpus/tables/logia-index.md` і `logia-workflow-matrix.md` синхронізовано.
- `reconstruction/earliest-sayings-gospel/inclusion-decisions-table.md` оновлено рішення для логії 16.
- `reconstruction/earliest-sayings-gospel/evidence-dossier-en.md` оновлено до v0.8.
- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-uk.md` оновлено до v1.1.
- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-uk-apparatus.md` оновлено до v0.9.

### Методологічне рішення

Коротке ядро логії 16 переведено в `INCLUDE_WITH_MARKER`:

> Я прийшов не принести мир, а поділ; дім буде розділений.

Повна логія 16 лишається `UNCERTAIN`. У головний текст не включено `вогонь / меч / війна` і фінал `monachos`.

Для грецького шару потрібна позначка `Greek retroversion, hypothetical`, бо extant Greek Thomas witness у завантажених P.Oxy. матеріалах немає.

### Наступна дія

Після логії 16 найкраще або перейти до корпусного спринту 40-60, або поглибити ще один уже сильний притчевий кандидат: логію 9, притчу про сіяча без алегоричного тлумачення.
