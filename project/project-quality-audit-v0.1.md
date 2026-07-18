# Project Quality Audit v0.2

Статус: актуалізований аудит якості, 2026-07-18.

Примітка: файл збережено під історичною назвою `project-quality-audit-v0.1.md`, щоб не ламати наявні посилання. Поточний зміст відповідає audit v0.2.

## Мета аудиту

Цей документ фіксує актуальні недоліки, які ще відділяють проект EUAGELIA від переконливого публікаційного результату:

- чистого українського reconstructed reader;
- повного українського appendix до всіх 114 логій;
- коптського, грецького, англійського й арабського reader/language layers;
- англомовного evidence dossier;
- прозорої методології, бібліографії, прав і citation policy.

## Executive Assessment

Орієнтовна готовність проекту до кінцевої мети: 88-90%.

Проект уже не перебуває на етапі побудови корпусу. Корпус покрито повністю, clean reader існує, all-114 decision table створено, evidence-blocking gap зведено до нуля, картки мають пʼятиджерельний апарат і читацьке тлумачення, а full appendix синхронізовано з цим читацьким шаром для всіх 114 логій.

Головний актуальний ризик змінився. Раніше слабким місцем була відсутність пояснень і evidence-control покриття. Потім - нерівний appendix, робочий evidence dossier, порожній source-safety layer і 104A як reader-pressure case. Тепер ці шари суттєво підняті: appendix консолідований 114/114, evidence dossier має publication-facing draft v1.4, bibliography/rights/citation/reproducibility має working layer v0.1, а 104A стабілізовано як appendix-only. Найбільше просів тепер Greek publication layer: треба вирівняти extant/lacunose/hypothetical labels і не допустити, щоб ретроверсії виглядали як рукописні свідки.

## Поточні Метрики

| Напрям | Стан |
| --- | ---: |
| Картки логій | 114/114 |
| Картки з `Gold-level status check v0.2` | 114/114 |
| Картки з `Five-source original-language apparatus v0.1` | 114/114 |
| Картки з `Читацьке тлумачення` | 114/114 |
| Картки з реальним локальним canonical Greek text | 81/114 |
| Картки з canonical Greek channel, але без локально виписаного Greek text | 33/114 |
| Картки з pending P.Oxy. line extraction | 0/114 |
| Full appendix logion sections | 114/114 |
| Appendix sections with reader-facing explanation | 114/114 |
| Appendix sections already editorially consolidated | 114/114 |
| Appendix sections still carrying separate card-derived blocks | 0/114 |
| Застаріла фраза `перетворити з каркаса...` | 0 |
| Working-index skeleton phrases still present | 0 |
| All-114 publication decision table | Є, v0.1 |
| `NEEDS_EVIDENCE_BEFORE_FINAL` у all-114 table | 0 |
| Clean Ukrainian reader | 37 логій / ядер |
| Cluster-control passes completed | 7 груп |
| Evidence dossier | Publication-facing draft v1.4 |
| Bibliography / rights / citation / reproducibility | Release verification layer v0.2; open/public-domain controls verified and protected controls limited |

## Що Вже Сильне

1. **Повне корпусне покриття.** 114/114 логій мають картки.
2. **Картки структурно вирівняні.** 114/114 мають gold-level status block.
3. **Джерельний шар видимий у кожній картці.** P.Oxy. 1 / 654 / 655, Coptic NHC II і canonical Greek control channel прямо в картках.
4. **Читацьке тлумачення тепер є всюди.** 114/114 карток і 114/114 appendix-секцій мають окремий reader-facing український шар.
5. **Full appendix більше не є порожнім каркасом.** Він має 114/114 секцій із цілісним print-safe читацьким поясненням для кожної включеної, невключеної, відкладеної й відкинутої логії.
6. **All-114 decision control існує.** `all-114-publication-decision-table-v0.1.md` покриває всі логії й прибрав головний хаос у статусах.
7. **Evidence-blocking gap закрито.** `NEEDS_EVIDENCE_BEFORE_FINAL` зведено до 0 після P1 evidence-rationale packages.
8. **Гіпотетичний грецький шар методологічно відділено від manuscript witness.**
9. **Clean reader лишається чистим.** Коментарі, статуси й дужки не потрапляють у перший читацький шар.

## Закриті Попередні Недоліки

| Попередній недолік | Поточний стан |
| --- | --- |
| Pending P.Oxy. XML extraction | Закрито в `corpus/cards/poxy-xml-extraction-audit-v0.1.md`. |
| Відсутність true all-114 decision table | Закрито в `reconstruction/earliest-sayings-gospel/all-114-publication-decision-table-v0.1.md`. |
| Evidence-control inventory не виконано | Закрито в `reconstruction/earliest-sayings-gospel/evidence-control-inventory-v0.1.md`. |
| Більшість карток без зрозумілого тлумачення | Закрито на рівні v0.1: `corpus/cards/reader-interpretation-expansion-audit-v0.1.md`. |
| Full appendix мав 70+ старих scaffold-заглушок типу `перетворити з каркаса...` | Закрито: reader-interpretation sync додав пояснення для 114/114 секцій, а editorial consolidation packages 1-114 прибрали card-derived duplication і working-index prose. |
| Невключені логії пояснювалися слабше за включені | Суттєво покращено: усі 114 appendix-секцій мають читацьке пояснення, включно з excluded/deferred/uncertain. |
| Відсутність reusable consistency script | Закрито в `tools/qa_crosscheck.py`; поточний запуск проходить для 114 карток, 114 appendix-секцій, 37 clean-reader одиниць і exact clean-text anchors. |
| Evidence dossier був робочим, не публікаційним | Закрито на рівні publication-facing draft v1.4 у `reconstruction/earliest-sayings-gospel/evidence-dossier-en.md`. |
| Bibliography/rights/citation були тільки принципами | Закрито на рівні working layer v0.1: rights policy, reproducibility note, working bibliography і source-rights register створені. |

## P0 Недоліки: Критичні Для Публікаційної Якості

### 1. Full Appendix Ще Не Є Єдиним Відредагованим Текстом

Попередній найбільший недолік appendix уже закрито: повний додаток тепер має 114/114 редакційно консолідованих секцій. Evidence dossier також піднято до publication-facing draft v1.4. Найбільший актуальний недолік переходить у source/publication safety layer: треба закрити бібліографію, права, citation policy, source snapshots і reproducibility notes.

Фактичний стан:

- 114/114 секцій мають читацьке пояснення;
- 114/114 секцій уже редакційно консолідовані;
- раніше розгорнуті секції збережені;
- окремих card-derived reader blocks більше немає;
- working-index prose більше не лишилося в основному appendix-коментарі.

Ризик тепер інший: appendix і evidence dossier уже читаються як цілісні шари, але без перевіреної бібліографії, прав і print-safe citation keys їх ще не можна безпечно перетворювати на паперові книги.

Потрібно:

- створити або оновити `project/rights-and-citation-policy.md`;
- створити або оновити `bibliography/bibliography-working.md`;
- створити або оновити `bibliography/source-rights-register.md`;
- зафіксувати print-safe citation keys для паперових книг;
- зафіксувати digital source paths і reproducibility notes для scholarly companion;
- після цього виконати generator-ready book production і book-generation proof pass.

### 2. Cluster-Control Notes Ще Не Закриті Для Всіх Deferred-Груп

Виконані cluster-control passes:

- living/dead/world;
- beatitudes;
- seek/find;
- family-renunciation;
- fire/kingdom.
- thief/watchfulness;
- wealth/renunciation.

Найважливіші незакриті або optional-before-freeze групи:

- ritual/practice / bridegroom 104A;
- image/light;
- body/soul;
- authority/community;
- parables with high dependence risk.

Ризик: 46-47 логій усе ще мають логіку `DEFER_TO_CLUSTER` або близький статус. Appendix уже пояснює їх базово, але фінальне рішення має спиратися на cluster-level аргумент, а не тільки на окрему картку.

Потрібно:

- використати Logion 114 publication-level exclusion rationale як готовий secondary-exclusion case у dossier;
- після кожного cluster-control pass оновлювати cards, all-114 table, appendix і dossier;
- не промотувати логії в clean reader без окремого decision pass.

### 3. Evidence Dossier Не Готовий Як Англомовний Публікаційний Захист

Evidence dossier існує і вже корисний, але ще не є документом, який можна дати зовнішньому reviewer без пояснень.

Потрібно:

- methodological introduction;
- source hierarchy;
- explicit uncertainty model;
- logion-by-logion summaries для included units;
- selected summaries для excluded/deferred high-impact logia;
- inclusion/exclusion rationale;
- bibliography;
- rights and citation policy;
- окреме пояснення, чому reconstruction не дорівнює translation of Thomas.

Ризик: clean reader може виглядати переконливо літературно, але без dossier зовнішній читач не побачить повного доказового ланцюга.

### 4. Logion 114 Publication-Level Exclusion Rationale Закрито

Logion 114 має статус `EXCLUDE_AS_SECONDARY`, окремий control file і publication-level rationale. Для фінального видання це вже достатній локальний апарат; тепер його треба інтегрувати в загальний evidence dossier.

Закрито:

- окремий dossier-ready rationale;
- пояснення, чому ця логія не входить до earliest sayings-gospel reconstruction;
- спокійне тлумачення без полеміки;
- пояснення, чому її все одно треба показати в appendix.

Залишковий ризик: читач може сприйняти rationale як ізольовану нотатку, якщо evidence dossier не інтегрує її в загальну методологію inclusion/exclusion.

## P1 Недоліки: Високий Пріоритет

### 5. Canonical Greek Layer Потребує Reproducibility Fix

SBLGNT Greek controls внесені в 81 картку, але довготривала відтворюваність ще слабка.

Потрібно:

- стабільний source snapshot або reproducibility note;
- URL / commit / license / extraction method;
- оновлення source register;
- чітке розрізнення working open control text і final critical-edition verification target.

### 6. Greek Retroversion Layer Потребує Publication Polish

Проект правильно маркує `Greek retroversion, hypothetical`, але фінальна якість потребує:

- єдиної confidence шкали;
- звірки з коптською граматикою;
- звірки з extant Greek Thomas fragments;
- звірки з canonical Greek formulae;
- пояснення для читача, що retroversion не є рукописним текстом.

### 7. Rights, Bibliography, Citation Policy Ще Не Фінальні

Є source register і working notes, але нема повного фінального апарату.

Потрібно:

- `project/rights-and-citation-policy.md`;
- `project/bibliography.md`;
- список open / public-domain / protected sources;
- правила короткого цитування modern scholarship;
- явне правило: захищені видання використовуються для перевірки, а не як базовий публічний текст.

### 8. Documentation Sync Потребує Ще Одного Проходу Після Нових Змін

README, project map і roadmap вже оновлювалися, але проект рухається швидко.

Потрібно звірити:

- `project/final-product-specification.md`;
- `project/clean-text-plus-commentary-concept.md`;
- `project/repository-structure.md`;
- `project/publication-gap-audit-v0.2.md`;
- `project/project-quality-remediation-plan-v0.1.md`;
- `reconstruction/earliest-sayings-gospel/README.md`;
- поточний audit-файл.

Ризик: частина документів ще може казати, що appendix тільки каркас або що evidence-note coverage старе.

### 9. Prompt Sprawl Повернувся

У `project/` знову багато `ide-codex-...-prompt.md`, включно з уже виконаними промптами.

Потрібно:

- залишити в корені master prompt і актуальний next-step prompt;
- перенести виконані prompts в архів;
- у `project/project-map.md` пояснити, де історія виконаних prompts.

Ризик: наступний executor витратить час на старі prompts або виконає застарілий крок.

## P2 Недоліки: Полірування І Читабельність

### 10. Український Вступ Для Читача Ще Не Написано

Clean reader має починатися без дисклеймерів. Але в другому шарі потрібен читабельний вступ:

- що означає "найдавніше євангеліє";
- чому це reconstruction, а не знайдений рукопис;
- чому за основу взято Фому;
- чому не всі логії включено;
- як користуватися clean reader і appendix.

### 11. Clean Reader Потребує Фінального Літературного Редагування

37 логій/ядер читаються добре, але перед freeze потрібно:

- уніфікувати український стиль;
- перевірити терміни;
- не впустити коментарі в чистий текст;
- зберегти нумерацію за Gospel of Thomas;
- звірити включені split-core units із apparatus.

### 12. Parallel Edition Ще Не Фінальна

Поточний multilingual/parallel layer покриває 34 reader units, але після final freeze треба синхронізувати:

- українську;
- англійську;
- коптську;
- extant Greek або Greek retroversion with confidence;
- арабський literary/Injil layer;
- canonical parallels only as control, not witness.

### 13. Автоматичні Перевірки Майже Відсутні

Проект уже достатньо великий, щоб мати прості consistency checks:

- 114 карток існують;
- кожна має five-source block;
- кожна має gold status block;
- кожна має reader interpretation block;
- appendix має 114 секцій і 114 reader interpretation blocks;
- clean reader logia збігаються зі списком у roadmap;
- workflow matrix не суперечить cards/all-114 table.

### 14. Локальний Робочий Шум

У минулих аудитах було зафіксовано `.DS_Store`. Також у git status є багато untracked audit/prompt/pass files, які треба або заархівувати, або зафіксувати комітом.

Ризик: важче відрізнити активні зміни від завершених робочих пакетів.

## Рекомендована Послідовність Закриття Недоліків

1. **Print/digital rendering preparation.** Підготувати renderer або ручний pipeline для PDF/print proof.
2. **Proof QA.** Перевірити print-safe citations, нумерацію, індекси, права і внутрішні шляхи в паперових виходах.
3. **Final library checks for protected controls.** Закрити page-specific citations тільки там, де вони реально підуть у друк.
6. **Run structural QA before/after major passes.** `python3 tools/qa_crosscheck.py` уже існує; його треба запускати як guardrail, а не створювати заново.
7. **Prompt/archive cleanup and git hygiene.**

## Найважливіший Наступний Крок

Найлогічніше наступне завдання: **print / digital render proof preparation**.

Причина: проект уже має 114/114 карток із тлумаченнями, повністю консолідований appendix, all-114 decision table, основні cluster-control passes, Logion 114 exclusion rationale, publication-facing evidence dossier v1.4, bibliography/rights/citation/reproducibility release layer v0.2, закритий 104A follow-up, Greek retroversion publication polish, final clean-reader freeze і generator-ready source packages. Тепер найбільший видимий недолік - proof/render readiness перед рендерингом і релізом.
