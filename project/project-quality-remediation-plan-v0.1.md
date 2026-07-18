# Project Quality Remediation Plan v0.1

Статус: план усунення недоліків після `project-quality-audit-v0.1`, актуалізовано 2026-07-18.

## Мета

Довести проект від сильного робочого корпусу до публікаційно переконливої реконструкції найдавнішого досяжного євангелія висловів:

- чистий український reconstructed reader;
- повний український додаток до всіх 114 логій;
- коптський, грецький і англійський шари;
- прозора all-114 decision table;
- англомовний evidence dossier;
- методологія, бібліографія, права і citation policy.

Цей план не замінює дорожню карту завершення. Він є практичним планом закриття саме тих недоліків, які виявив повний аудит якості.

## Принципи Усунення Недоліків

1. **Спершу джерела, потім рішення.** Не фіналізувати all-114 inclusion decisions, доки не закриті видимі source-critical борги.
2. **Clean text лишається чистим.** Коментарі, дужки, статуси, рівні впевненості й пояснення не потрапляють у перший читацький шар.
3. **Відкинуті логії також пояснюються.** Appendix має бути чесним не тільки для включених, а й для excluded/deferred/uncertain логій.
4. **Гіпотетичний грецький текст не є свідком.** Усі Greek retroversions мають бути явно марковані як реконструкційні.
5. **Рішення мають бути відтворюваними.** Кожен крок має лишати audit note або оновлений контрольний файл.
6. **Не всі логії потребують однакової глибини, але всі потребують пояснення.** Low-priority deferred logia можуть мати коротший rationale, але не порожнечу.

## Поточна База

| Актив | Стан |
| --- | --- |
| Картки логій | 114/114 |
| Gold-level status blocks | 114/114 |
| Five-source apparatus blocks | 114/114 |
| Локально виписаний canonical Greek | 81/114 |
| Pending P.Oxy. line extraction | 0 після `poxy-xml-extraction-audit-v0.1.md` |
| Evidence/control inventory | Complete |
| `NEEDS_EVIDENCE_BEFORE_FINAL` | 0 |
| Full appendix headings | 114/114 |
| Remaining unconsolidated card-derived appendix blocks | 31 |
| Remaining working-index skeleton phrases | 20 |
| Clean Ukrainian reader | 37 логій / ядер |

## Phase 0. Stabilize Tracking

**Мета:** зробити сам план виконуваним і контрольованим.

### Tasks

- Додати цей план у `project/project-map.md`.
- Додати запис у `sources/primary_texts/collection-log.md`.
- Зберегти виконуваний prompt у `project/ide-codex-quality-remediation-master-prompt.md`.

### Acceptance Criteria

- План і prompt існують у проекті.
- Project map показує, де їх знайти.
- Collection log має короткий запис, чому план створено.

## Phase 1. P.Oxy. XML Extraction Cleanup

**Пріоритет:** P0. **Статус:** виконано у `corpus/cards/poxy-xml-extraction-audit-v0.1.md`.

**Мета:** закрити прямий папірусний борг перед фінальними рішеннями.

### Scope

Оновити 8 карток:

- P.Oxy. 1: logia 27, 28, 29, 30, 77;
- P.Oxy. 655: logia 24, 37, 38.

### Source Files

- `sources/primary_texts/greek_poxy/dclp-poxy1-62838.xml`
- `sources/primary_texts/greek_poxy/dclp-poxy655-62839.xml`

### Tasks

- Витягнути card-ready Greek lines із TEI/XML.
- Розрізнити extant, lacunose, supplied, uncertain і unusable readings.
- Оновити відповідні `Five-source original-language apparatus v0.1` blocks.
- Не перетворювати conjectural restorations на extant witness.
- Створити audit note, наприклад `corpus/cards/poxy-xml-extraction-audit-v0.1.md`.
- Оновити source register / collection log, якщо потрібно.

### Acceptance Criteria

- У 8 картках більше немає `pending local line extraction`, якщо XML реально дає витяг.
- Якщо XML не дає придатного card-ready text, картка прямо пояснює чому.
- Audit note містить список оновлених логій, джерело XML і межі використання.

## Phase 2. Documentation Sync Pass

**Пріоритет:** P0/P1. **Статус:** виконано базову синхронізацію після P.Oxy. cleanup; глибший evidence/control inventory винесено в Phase 3.

**Мета:** прибрати розсинхрони, які можуть вести наступного виконавця не туди.

### Tasks

- Виправити дубльовану нумерацію у `project/project-completion-roadmap.md`.
- Узгодити nearest action: спершу P.Oxy. extraction, потім all-114 publication decision table.
- Вирішити mismatch `project/publication-gap-audit-v0.1.md` vs title `v0.2`: актуальний файл перейменовано на `project/publication-gap-audit-v0.2.md`, v0.1 лишено як redirect.
- Узгодити evidence-note statistics між roadmap, publication gap audit, quality audit і workflow matrix.
- Оновити `sources/primary_texts/source-register.md`: чітко розвести SBLGNT as working open control і final critical-edition verification target for Matthew/Mark/Luke.
- Зафіксувати, що `/tmp/euagelia-sblgnt` не є стабільним джерелом для довготривалої відтворюваності.

### Acceptance Criteria

- Документи не суперечать щодо next action.
- Evidence-note numbers або збігаються, або мають explicit "needs verification" note.
- Source register не створює враження, що canonical Greek controls взагалі не знайдені.

## Phase 3. Evidence and Control Inventory

**Пріоритет:** P0. **Статус:** виконано у `reconstruction/earliest-sayings-gospel/evidence-control-inventory-v0.1.md`.

**Мета:** точно знати, які evidence notes і control files реально існують, а не покладатися тільки на стару matrix.

### Tasks

- Просканувати `reconstruction/earliest-sayings-gospel/notes/`.
- Просканувати `controls/` або наявні control-file locations.
- Звірити files із `corpus/tables/logia-workflow-matrix.md`.
- Створити `reconstruction/earliest-sayings-gospel/evidence-control-inventory-v0.1.md`.
- Позначити для кожної логії:
  - evidence note exists / missing;
  - control file exists / cluster file exists / missing;
  - reader status;
  - priority for note creation.

### Acceptance Criteria

- Є точний inventory для 114 логій.
- Workflow matrix має бути оновлена або явно позначена як stale where applicable.
- Список next evidence-note targets сформований за priority, а не інтуїцією.

## Phase 4. True All-114 Publication Decision Table

**Пріоритет:** P0. **Статус:** виконано у `reconstruction/earliest-sayings-gospel/all-114-publication-decision-table-v0.1.md`.

**Мета:** створити головний контрольний документ фінального відбору.

### Target File

- `reconstruction/earliest-sayings-gospel/all-114-publication-decision-table-v0.1.md`

### Result

- 114/114 логій покрито.
- `READER_INCLUDE_MARKED`: 34.
- `APPENDIX_ONLY_STABLE`: 20.
- `APPENDIX_ONLY_UNCERTAIN`: 12 after Package B evidence-rationale pass.
- `DEFER_TO_CLUSTER`: 47 after Package B evidence-rationale pass.
- `NEEDS_EVIDENCE_BEFORE_FINAL`: 0 after Package B evidence-rationale pass.
- `EXCLUDE_AS_SECONDARY`: 1.
- Clean reader не змінено; Phase 5 має розгортати пояснювальний appendix.

### Required Columns

- Logion / subunit;
- current decision;
- clean reader status;
- confidence;
- Greek status;
- Coptic status;
- canonical / extracanonical control;
- evidence note;
- appendix status;
- inclusion/exclusion rationale;
- next action before final freeze.

### Acceptance Criteria

- Покрито всі 114 логій і split-core subunits.
- `INCLUDE_WITH_MARKER`, `KEEP_APPENDIX_ONLY_FOR_NOW`, `DEFER`, `UNCERTAIN`, `EXCLUDE_AS_SECONDARY` використовуються послідовно.
- Немає логії без хоча б короткого rationale.
- Clean reader composition можна вивести з таблиці без ручного здогаду.

## Phase 5. Full Appendix Expansion

**Пріоритет:** P0/P1. **Статус:** розпочато; перший P1 non-reader appendix package і evidence-rationale pass виконано.

**Мета:** перетворити `full-logion-commentary-appendix-uk.md` на реальний читацький довідник до всіх 114 логій.

### Work Method

Робити пакетами по 8-12 логій, починаючи з:

1. excluded/deferred high-impact logia;
2. uncertain logia with strong parallels;
3. included logia that still have shallow commentary;
4. low-priority appendix-only logia.

### Required Section Pattern

Для кожної логії:

- короткий зміст;
- джерела і текстові свідки;
- грецький статус;
- коптська база;
- канонічні / позаканонічні / внутрішньотоміні паралелі;
- можливі тлумачення;
- що лишається непевним;
- чому включено / не включено / відкладено;
- посилання на картку й evidence note або explicit no-note rationale.

### Acceptance Criteria

- Кожен пакет зменшує кількість unconsolidated/card-derived appendix sections і дотримується print-safe reference rules.
- Відкинуті логії отримують таку саму повагу до пояснення, як включені.
- Коментарі не змінюють чистий reader без окремого decision pass.

### Completed Package

- P1 non-reader package: 23, 24, 28, 29, 30, 37, 38, 75, 77, 104, 106.
- Clean reader не змінено.
- Evidence-rationale pass для цього пакета виконано в `reconstruction/earliest-sayings-gospel/p1-non-reader-evidence-rationale-pass-v0.1.md`.
- Наступна дія: продовжити print-safe full appendix editorial consolidation з Logia 81-90; після цього закрити wealth/renunciation cluster-control.

## Phase 6. Evidence Dossier Publication Pass

**Пріоритет:** P1.

**Мета:** зробити англомовний evidence dossier придатним для зовнішньої перевірки.

### Tasks

- Написати methodological introduction.
- Додати source hierarchy.
- Додати uncertainty model.
- Додати logion-by-logion summaries.
- Додати inclusion/exclusion rationale.
- Додати bibliography і rights/citation section.
- Відокремити manuscript evidence, translation evidence, canonical control і modern scholarly models.

### Acceptance Criteria

- Dossier можна дати англомовному читачеві без пояснень у чаті.
- Не створюється враження, що Greek retroversion є extant manuscript.
- Всі ключові inclusion decisions мають evidence trail.

## Phase 7. Rights, Bibliography, and Reproducibility

**Пріоритет:** P1.

**Мета:** зробити проект безпечним для поширення.

### Target Files

- `project/rights-and-citation-policy.md`
- `project/bibliography.md`
- optional: `sources/primary_texts/reproducibility-notes.md`

### Tasks

- Позначити open / public-domain / protected materials.
- Зафіксувати DCLP/Papyri.info license handling.
- Зафіксувати SBLGNT license and source provenance.
- Позначити Brill / Layton / DeConick / other modern editions as verification sources, not fully reproduced sources.
- Дати правила короткого цитування modern scholarship.

### Acceptance Criteria

- Кожен великий source family має rights status.
- Публічний текст не залежить від повного відтворення захищених сучасних перекладів.
- SBLGNT extraction pass can be reproduced.

## Phase 8. Greek Retroversion Publication Polish

**Пріоритет:** P1/P2.

**Мета:** довести Greek layer до методологічної чистоти.

### Tasks

- Перевірити всі Greek retroversions.
- Додати confidence labels where missing.
- Перевірити, що extant Greek, lacunose Greek, supplied Greek і retroversion не змішані.
- Пояснити це в reader-facing або methodological note.

### Acceptance Criteria

- Жодна реконструкція не виглядає як рукописний свідок.
- Кожне місце без збереженого грецького тексту має чесний рівень гіпотетичності.

## Phase 9. Final Reader and Editorial Pass

**Пріоритет:** P2, але фінально обовʼязковий.

**Мета:** зробити видання читабельним, послідовним і готовим до показу.

### Tasks

- Фінальна редакція українського clean reader.
- Англійський reader sync.
- Parallel edition sync.
- Український reader-facing introduction у другому шарі.
- Англомовний methodological introduction.
- Термінологічна перевірка між Ukrainian / English / Coptic / Greek.

### Acceptance Criteria

- Clean reader лишається чистим.
- Appendix пояснює всі рішення.
- Dossier захищає реконструкцію.
- Користувач може читати проект без додаткових пояснень від автора.

## Phase 10. Consistency Checks

**Пріоритет:** P2. Status: baseline completed in `tools/qa_crosscheck.py`.

**Мета:** зменшити технічні розсинхрони.

### Tasks

- Підтримувати й запускати reusable consistency script `tools/qa_crosscheck.py`.
- Перевірити:
  - 114 card files;
  - 114 gold blocks;
  - 114 five-source blocks;
  - 114 appendix sections;
  - clean reader list vs decision table;
  - matrix vs card status;
  - no `pending local line extraction` after Phase 1 unless justified.

### Acceptance Criteria

- Перед фінальним freeze можна одним проходом перевірити structural integrity.
- Виявлені розсинхрони стають явними.

### Current Baseline

`python3 tools/qa_crosscheck.py` already verifies card count and numbering, appendix section coverage, source/control sections, clean-reader synchronization across Ukrainian/English/Greek/Coptic/Arabic/apparatus/parallel layers, workflow/decision alignment, appendix status agreement, and exact clean-text anchors for all current reader units.

## Recommended Execution Order

1. Phase 1: P.Oxy. XML extraction cleanup. Done in `corpus/cards/poxy-xml-extraction-audit-v0.1.md`.
2. Phase 2: Documentation sync pass. Basic sync done after P.Oxy. cleanup.
3. Phase 3: Evidence and control inventory. Done in `reconstruction/earliest-sayings-gospel/evidence-control-inventory-v0.1.md`.
4. Phase 4: True all-114 publication decision table. Done in `reconstruction/earliest-sayings-gospel/all-114-publication-decision-table-v0.1.md`.
5. Phase 5: Full appendix expansion by packages. Started; next recommended package is cluster-control deepening for deferred groups.
6. Phase 6: Evidence dossier publication pass.
7. Phase 7: Rights, bibliography, reproducibility.
8. Phase 8: Greek retroversion polish.
9. Phase 9: Final reader/editorial pass.
10. Phase 10: Consistency checks and final freeze.

## Definition of Done For The Whole Remediation Plan

Проект можна вважати якісно підтягнутим, коли:

- немає unexplained pending source-critical gaps;
- кожна логія має decision і rationale;
- кожна reader logion має evidence trail;
- кожна excluded/deferred logion має appendix explanation;
- Greek/Coptic/English/Ukrainian layers синхронізовані;
- evidence dossier читається як самостійний англомовний захист;
- rights/citation/bibliography не лишаються "потім";
- документація не суперечить сама собі;
- clean reader можна показати першим без пояснень, а appendix дає всю глибину після читання.
