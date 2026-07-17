# Карта проєкту

Статус: актуалізовано 2026-07-17.

## Поточний стан у стислому вигляді

- Clean Ukrainian reader: 34 логії/ядра.
- Англійський, коптський, грецький і parallel шари синхронізовані для цих 34 одиниць.
- Greek retroversion confidence audit створено; гіпотетичні ретроверсії не рахуються рукописними свідками.
- Full 114-logion appendix існує для всіх 114 логій як каркас; попередні 31 включені логії/ядра вже розгорнуті до читацьких секцій, а нові 45A/47B/63 мають апаратну підтримку.
- Evidence dossier: робочий v1.3, ще не публікаційний.
- Controlled clean-reader candidate pass виконано; найближчий робочий пакет: true all-114 publication decision table.
- Усі 114 карток логій мають `Gold-level status check v0.2`; актуальним card-quality audit є `corpus/cards/card-quality-audit-v0.2.md`.
- Усі 114 карток логій мають `Five-source original-language apparatus v0.1`; актуальний аудит джерельного шару: `corpus/cards/five-source-apparatus-audit-v0.1.md`.
- Canonical Greek extraction pass виконано: 81 картка має Матвій/Марк/Лука Greek control з локального SBLGNT; аудит: `corpus/cards/canonical-greek-extraction-audit-v0.1.md`.

## Поточні матеріали

| Розділ | Файл | Зміст |
| --- | --- | --- |
| Навігація | `project/repository-structure.md` | Нова функціональна структура репозиторію після відмови від первісних числових папок. |
| Методологія | `research/methodology/bayesian-logion-by-logion-method.md` | Байєсівський підхід, незалежний рейтинг кожної логії, критерії датування. |
| Джерела | `sources/manuscripts-languages-and-working-corpus.md` | Грецькі фрагменти, коптський текст, питання мови оригіналу, робочий корпус. |
| Джерела | `sources/online-resources-and-facsimiles.md` | Gnosis Archive, Наг-Хаммаді, факсиміле, академічні ресурси. |
| Датування | `research/scholarship-and-dating/probability-scale-for-dating-thomas.md` | Сценарії датування та ймовірнісна шкала. |
| Датування | `research/scholarship-and-dating/history-of-dating-and-church-bias.md` | Історія досліджень, конфесійна оптика, зміна консенсусу. |
| Дослідники | `research/scholarship-and-dating/scholarly-reconstructions-deconick-arnal-crossan-patterson.md` | ДеКонік, Арнал, Кроссан, Паттерсон і проблема реконструкції раннього Фоми. |
| Гіпотези | `research/historical-hypotheses/historical-yeshua-and-rise-of-the-church-hypothesis.md` | Робоча реконструкція історичного Єшуа та розвитку ранньої Церкви. |
| Формулювання | `research/historical-hypotheses/precise-formulation-thomas-as-sayings-gospel.md` | Обережне формулювання унікальності Фоми як Євангелія висловів. |
| Кінцевий продукт | `project/final-product-specification.md` | Специфікація реконструйованого найдавнішого євангелія висловів: український, коптський, грецький, англійський шари й англомовний доказовий апарат. |
| Кінцевий продукт | `project/clean-text-plus-commentary-concept.md` | Концепція фінального видання: спочатку чистий реконструйований текст, потім коментар і повний додаток до всіх 114 логій. |
| Кінцевий продукт | `project/clean-reader-text-first-page-principle.md` | Правило першої читацької сторінки: у головному українському тексті тільки пронумеровані логії, без дисклеймерів, статусів, квадратних дужок і коментарів. |
| Завершення | `project/project-completion-roadmap.md` | Актуальна дорожня карта: 34-unit reader, синхронізовані мовні шари, Greek audit, пакетне розгортання full appendix і публікаційні прогалини. |
| Завершення | `project/project-quality-audit-v0.1.md` | Повний аудит якості проекту: сильні сторони, P0/P1/P2 недоліки, метрики, ризики публікації й рекомендована послідовність закриття прогалин. |
| Завершення | `project/project-quality-remediation-plan-v0.1.md` | Практичний план усунення недоліків після quality audit: фази, пріоритети, acceptance criteria і порядок доведення проекту до публікаційної якості. |
| Завершення | `reconstruction/earliest-sayings-gospel/controlled-clean-reader-candidate-pass-v0.1.md` | Контрольований reader pass після Reviews A/B: включено 45A, 47B і 63; решту кандидатів залишено appendix-only. |
| Завершення | `project/publication-gap-audit-v0.2.md` | Аудит того, що ще відділяє проект від публікаційного рівня. |
| Завершення | `corpus/cards/card-quality-audit-v0.2.md` | Аудит gold-level нормалізації карток: 114/114 мають поточний v0.2 status block; головна наступна прогалина - publication decision depth. |
| Завершення | `corpus/cards/five-source-apparatus-audit-v0.1.md` | Аудит пʼятиджерельного апарату в картках: усі 114 мають P.Oxy./Coptic/canonical channel, але canonical Greek local extraction ще майже весь попереду. |
| Завершення | `corpus/cards/canonical-greek-extraction-audit-v0.1.md` | Аудит canonical Greek extraction: 81 картка отримала SBLGNT Greek controls, 33 лишаються pending. |
| Завершення | `corpus/cards/poxy-xml-extraction-audit-v0.1.md` | Аудит P.Oxy. XML extraction cleanup: закрито pending line extraction для логій 24, 27, 28, 29, 30, 37, 38 і 77. |
| Завершення | `corpus/tables/logia-workflow-matrix.md` | Операційна матриця 114 логій: картки, evidence notes, рішення, стан читабельного тексту й наступні дії. |
| Завершення | `reconstruction/earliest-sayings-gospel/full-corpus-classification-v0.1.md` | Перша повна класифікація всіх 114 логій після завершення первинних карток: reader text, high-priority candidates, deferred clusters and secondary material. |
| Завершення | `reconstruction/earliest-sayings-gospel/final-all-114-decision-audit-v0.1.md` | Аудит перед фіналізацією clean reader: що вже стабільне, що потребує split-core review, і які документи застаріли. |
| Завершення | `reconstruction/earliest-sayings-gospel/evidence-control-inventory-v0.1.md` | Інвентаризація фактичних evidence notes і control files для 114 логій перед true all-114 publication decision table. |
| Завершення | `reconstruction/earliest-sayings-gospel/split-core-decision-review-a-v0.1.md` | Перевірка логій 45, 47, 63, 64, 65-66: які ядра промотувати в майбутній reader pass, а що лишити appendix-only. |
| Завершення | `reconstruction/earliest-sayings-gospel/split-core-decision-review-b-v0.1.md` | Перевірка логій 76, 78, 79, 94, 103, 109, 113: які ядра промотувати в майбутній reader pass, а що лишити appendix-only. |
| Робочий промпт | `project/ide-codex-master-project-prompt.md` | Головний промпт проекту для наступних кроків реконструкції, корпусної роботи, коментарів і фінального видання. |
| Робочий промпт | `project/ide-codex-gold-card-quality-normalization-v0.2-prompt.md` | Промпт виконаного проходу: підняти всі 114 карток до єдиного gold-level status check v0.2 без передчасного промотування нових логій. |
| Робочий промпт | `project/ide-codex-five-source-card-apparatus-v0.1-prompt.md` | Промпт виконаного проходу: внести в кожну картку пʼять джерельних каналів із текстами або явною позначкою відсутності. |
| Робочий промпт | `project/ide-codex-canonical-greek-extraction-pass-v0.1-prompt.md` | Промпт виконаного проходу: витягнути canonical Greek controls із локального SBLGNT у картки. |
| Робочий промпт | `project/ide-codex-quality-remediation-master-prompt.md` | Головний промпт для поетапного усунення недоліків, починаючи з pending P.Oxy. XML extraction cleanup. |
| Робочий промпт | `project/ide-codex-evidence-control-inventory-v0.1-prompt.md` | Промпт виконаного Phase 3 проходу: звірити evidence notes і control files із workflow matrix. |
| Робочий промпт | `project/ide-codex-corpus-sprint-081-100-quality-prompt.md` | Якісний промпт для Sprint G: первинні картки логій 81-100 і оновлення контрольних таблиць без передчасного розширення чистого читацького тексту. |
| Робочий промпт | `project/ide-codex-corpus-sprint-101-114-quality-prompt.md` | Якісний промпт для Sprint H: завершити первинне покриття логій 101-114 і підготувати проект до загальної класифікації корпусу. |
| Робочий промпт | `project/ide-codex-full-corpus-classification-prompt.md` | Промпт для першої повної класифікації 114 логій і вибору high-priority evidence-note set. |
| Реконструкція | `reconstruction/earliest-sayings-gospel/README.md` | Карта поточного реконструкційного пакета: clean reader, apparatus, мовні шари, dossier, full appendix і Greek audit. |
| Реконструкція | `reconstruction/earliest-sayings-gospel/reconstructed-gospel-uk.md` | Чистий український текст реконструкції: лише пронумеровані логії, без статусів і коментарів. |
| Реконструкція | `reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-uk.md` | Повний український додаток до 114 логій: усі логії мають каркас; включені логії розгортаються до читацьких секцій. |
| Реконструкція | `reconstruction/earliest-sayings-gospel/greek-retroversion-confidence-audit-v0.1.md` | Контроль грецького шару: extant, lacunose, partial, mixed і hypothetical retroversion. |

## Принцип роботи

Головна одиниця аналізу - не книга, а логія. Кожна логія має отримати окрему картку, після чого можна буде будувати реконструкції шарів.
