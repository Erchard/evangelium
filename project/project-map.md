# Карта проєкту

Статус: актуалізовано 2026-07-19.

## Поточний стан у стислому вигляді

- Clean Ukrainian reader: 37 логій/ядер.
- Англійський, коптський, грецький, арабський літературний і parallel шари синхронізовані для цих 37 одиниць.
- Greek retroversion confidence audit створено; гіпотетичні ретроверсії не рахуються рукописними свідками.
- Full 114-logion appendix існує для всіх 114 логій: усі секції мають читацьке пояснення; Logia 1-114 уже редакційно консолідовані як print-safe книжковий додаток.
- Print/digital publication architecture v0.1 зафіксовано: українська й англійська паперові книги мають бути окремими самодостатніми виданнями, а повний source/evidence apparatus лишається цифровим companion layer.
- Technical QA baseline закрито: `tools/qa_crosscheck.py` перевіряє структурну цілісність 114 карток, 114 appendix-секцій, clean-reader sync і точні appendix anchors.
- Evidence dossier: publication-facing draft v1.4; bibliography/rights/citation/reproducibility layer оновлено до release verification pass v0.2.
- All-114 publication decision table v0.1 виконано; перший Phase 5 P1 non-reader appendix package і evidence-rationale pass виконано; cluster-control passes для living/dead/world, beatitudes, seek/find, family-renunciation, fire/kingdom, thief/watchfulness, wealth/renunciation і ritual-ethics / bridegroom 104A виконано; Logion 114 publication-level exclusion rationale, evidence dossier publication pass, bibliography/rights/citation/reproducibility pass, Greek retroversion publication polish, final clean-reader freeze, generator-ready book source packages, final bibliography and rights verify, print/digital render proof preparation, render pipeline and first proofs, first proof QA/layout correction, Bible-style book design/index pass, final proof polish/bibliography/TOC, release-candidate proof audit, full book assembly/typesetting pipeline, full Ukrainian proof QA, English full appendix structural generation, English appendix editorial quality pass, full English proof QA, digital companion expansion, browsable companion HTML, final production/copyedit gate, Typst production handoff package, release-candidate audit v1.0-rc1, Logion 1 frame-status review, Review C і controlled reader-candidate pass 46A/91A виконано; найближчий робочий пакет: external production compile and human copyedit signoff.
- Open-task prompt queue створено: `project/open-task-prompt-queue-2026-07-18.md`; актуальний `NEXT` - external production compile and human copyedit signoff.
- Усі 114 карток логій мають `Gold-level status check v0.2`; актуальним card-quality audit є `corpus/cards/card-quality-audit-v0.2.md`.
- Усі 114 карток логій мають `Five-source original-language apparatus v0.1`; актуальний аудит джерельного шару: `corpus/cards/five-source-apparatus-audit-v0.1.md`.
- Усі 114 карток логій мають `Читацьке тлумачення` v0.1 для звичайного читача; актуальний аудит: `corpus/cards/reader-interpretation-expansion-audit-v0.1.md`.
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
| Кінцевий продукт | `project/print-and-digital-publication-architecture.md` | Архітектура фінальних виходів: окрема українська паперова книга, окрема англійська паперова книга і digital scholarly companion; правила print-safe references замість залежності від hyperlinks. |
| Кінцевий продукт | `project/commons-dedication-and-use-policy.md` | Політика commons / anti-ownership: оригінальний внесок EUAGELIA є спільним надбанням людства, дозволений для будь-якого використання включно з комерційним, але без привласнення як виключної власності. |
| Кінцевий продукт | `project/arabic-injil-layer-concept.md` | Концепція арабського Injil-layer: як ідея ісламського первісного Інжилю може бути чесно використана як міжрелігійна рамка для реконструкції. |
| Кінцевий продукт | `project/arabic-injil-layer-editorial-policy.md` | Політика арабського Injil-layer: високий класичний / коранічно-суміжний регістр без претензії на суру, Коран або одкровення. |
| Завершення | `project/project-completion-roadmap.md` | Актуальна дорожня карта: 37-unit reader, синхронізовані мовні шари, Greek audit, пакетне розгортання full appendix і публікаційні прогалини. |
| Завершення | `project/open-task-prompt-queue-2026-07-18.md` | Активна черга високоякісних промптів для незакритих задач; актуальний `NEXT` - external production compile and human copyedit signoff. |
| Завершення | `project/open-task-prompt-factory-execution-v0.1.md` | Audit виконання prompt-factory pass: створено queue і набір поточних executable prompts. |
| Завершення | `project/project-quality-audit-v0.1.md` | Актуалізований аудит якості v0.2: закриті попередні недоліки, нові P0/P1/P2 прогалини, поточні метрики й рекомендований наступний крок. |
| Завершення | `project/project-quality-remediation-plan-v0.1.md` | Практичний план усунення недоліків після quality audit: фази, пріоритети, acceptance criteria і порядок доведення проекту до публікаційної якості. |
| Завершення | `project/probability-vs-reader-decision-audit-2026-07-18.md` | Audit зіставлення probability profiles із clean-reader рішеннями: Logion 1 review, high-early-score non-reader watchlist, duplicate probability profiles і Logion 30 scoring gap. |
| Завершення | `project/technical-debt-closure-2026-07-18.md` | Audit закриття поточних технічних боргів: QA script, appendix clean-text anchors, documented heading formats і Logion 63 status drift. |
| Завершення | `tools/qa_crosscheck.py` | Reusable structural QA script: перевіряє 114 карток, 114 appendix-секцій, clean-reader синхронізацію, workflow/decision alignment і exact clean-text anchors. |
| Завершення | `tools/probability_reader_audit.py` | Reusable audit script для перевірки напруги між probability profiles і clean-reader decisions. |
| Завершення | `project/documentation-refresh-2026-07-18-v0.1.md` | Audit повної актуалізації активної документації після print/digital architecture pass, technical-debt closure, Greek-layer freeze і appendix consolidation Logia 1-114. |
| Завершення | `project/structure-cleanup-2026-07-18-v0.1.md` | Audit структурного cleanup: прибрано `.DS_Store`, порожні старі output folders і порожній `reconstruction/kernel-thomas/`; додано print/digital output README. |
| Завершення | `reconstruction/earliest-sayings-gospel/controlled-clean-reader-candidate-pass-v0.1.md` | Контрольований reader pass після Reviews A/B: включено 45A, 47B і 63; решту кандидатів залишено appendix-only. |
| Завершення | `project/publication-gap-audit-v0.2.md` | Аудит того, що ще відділяє проект від публікаційного рівня. |
| Завершення | `reconstruction/earliest-sayings-gospel/evidence-dossier-publication-pass-v0.1.md` | Audit публікаційного проходу evidence dossier: thesis, method, source hierarchy, cluster logic, uncertainty model і provisional rights/citation note. |
| Завершення | `project/rights-and-citation-policy.md` | Правила прав, attribution, print-safe citations, digital source paths і protected-source controls. |
| Завершення | `project/source-reproducibility-note.md` | Reproducibility layer для Coptic, P.Oxy., SBLGNT і digital/print source mapping. |
| Завершення | `bibliography/bibliography-working.md` | Робоча бібліографія з print keys і конкретними release statuses після final bibliography / rights verify. |
| Завершення | `bibliography/source-rights-register.md` | Rights status table і release rules для основних джерельних сімейств. |
| Завершення | `project/final-bibliography-rights-verify-v0.1.md` | Audit фінальної pre-render bibliography/right verification: відкриті джерела перевірено, protected controls обмежено, snapshots із неясними правами не розповсюджувати. |
| Завершення | `project/print-digital-render-proof-prep-v0.1.md` | Preflight proof-prep report: paper sources print-safe, citation key table, renderer interface і blockers перед першим proof render. |
| Завершення | `project/render-pipeline-first-proofs-v0.1.md` | Audit першого render pass: мінімальний ReportLab renderer, HTML/PDF proofs, checksums, page counts і layout risks. |
| Завершення | `project/bible-style-paper-layout-policy-v0.1.md` | Політика паперового оформлення: чистий текст має наближатися до звичної масової Bible-style верстки. |
| Завершення | `project/first-proof-qa-layout-corrections-v0.1.md` | Audit першого proof-QA/layout correction pass: compact two-column clean text, serif typography, paper-path safety. |
| Завершення | `project/bible-style-book-design-index-pass-v0.1.md` | Audit Bible-style design/index pass: split paper indexes, reader-note page, path-safe paper PDFs і v0.3 proofs. |
| Завершення | `project/final-proof-polish-bibliography-toc-v0.1.md` | Audit final proof polish pass: front matter, proof-stable TOC, print source keys, compressed indexes і v0.4 proofs. |
| Завершення | `project/release-candidate-proof-package-audit-v0.1.md` | Audit release-candidate package: current PDFs are proof skeletons, not final release candidates; full appendix assembly is the blocker. |
| Завершення | `project/full-book-assembly-typesetting-pipeline-v0.1.md` | Audit full-book assembly pass: full-book source pipeline later expanded into 118-page Ukrainian proof, 177-page English proof, 16-page digital companion proof and HTML companion. |
| Завершення | `project/full-ukrainian-book-proof-qa-appendix-typography-v0.1.md` | Audit full Ukrainian proof-QA pass: 118 сторінок переглянуто, status labels локалізовано, QA crosscheck пройдено. |
| Завершення | `project/english-full-114-logion-appendix-generation-v0.1.md` | Audit English appendix generation pass: 114/114 англійських appendix-секцій, 177-сторінковий English full proof, paper-safety checks. |
| Завершення | `project/english-appendix-editorial-quality-pass-v0.1.md` | Audit English appendix editorial pass: системне покращення reader-facing prose, thematic explanations, source-status language і paper sanitizer. |
| Завершення | `project/full-english-book-proof-qa-typography-v0.1.md` | Audit full English proof-QA pass: 177 сторінок перебудовано, текстово й візуально перевірено, no clipping/path leakage. |
| Завершення | `project/digital-scholarly-companion-expansion-v0.1.md` | Audit digital companion expansion pass: deterministic generator, all-114 cross-reference TSV, source inventory, checksums, audit trail і 16-page PDF proof. |
| Завершення | `project/digital-companion-browsable-html-v0.1.md` | Audit browsable HTML companion pass: static HTML workbench, 114 panels, filters/search, source sections, audit trail і valid local links. |
| Завершення | `project/final-production-typesetting-copyedit-gate-v0.1.md` | Audit final production gate: ReportLab proof-only, Typst/professional handoff as final path, copyedit checklist and release-candidate blockers. |
| Завершення | `project/typst-production-pilot-v0.1.md` | Audit Typst production pilot / professional handoff pass: Typst-ready package exists; compilation pending external production environment. |
| Завершення | `project/release-candidate-audit-v1.0-rc1.md` | Release-candidate audit: content/proof package complete, final signoff blocked by external production compile and human copyedit. |
| Завершення | `output/release-candidate-manifest-v1.0-rc1.tsv` | Machine-readable manifest with size and SHA-256 for release-candidate artifacts. |
| Робочий промпт | `project/ide-codex-full-ukrainian-book-proof-qa-appendix-typography-v0.1-prompt.md` | Промпт виконаного проходу: повна page-by-page QA українського full proof і безпечний appendix typography polish. |
| Робочий промпт | `project/ide-codex-english-full-114-logion-appendix-generation-v0.1-prompt.md` | Промпт виконаного проходу: створити повний англійський 114-логійний appendix і mirrored English full proof. |
| Робочий промпт | `project/ide-codex-english-appendix-editorial-quality-pass-v0.1-prompt.md` | Промпт виконаного проходу: підняти English appendix structural draft до публікаційної читацької прози. |
| Робочий промпт | `project/ide-codex-full-english-book-proof-qa-typography-v0.1-prompt.md` | Промпт виконаного проходу: повна page-level QA 177-сторінкового English full proof і безпечні typography fixes. |
| Робочий промпт | `project/ide-codex-digital-scholarly-companion-expansion-v0.1-prompt.md` | Промпт виконаного проходу: розгорнути digital scholarly companion як повний evidence/source/audit/reproducibility layer. |
| Робочий промпт | `project/ide-codex-digital-companion-browsable-html-v0.1-prompt.md` | Промпт виконаного проходу: створити browsable/searchable static HTML companion для all-114 research navigation. |
| Робочий промпт | `project/ide-codex-final-production-typesetting-copyedit-gate-v0.1-prompt.md` | Промпт виконаного проходу: визначити final production path і провести фінальний copyedit/proof gate. |
| Робочий промпт | `project/ide-codex-typst-production-pilot-v0.1-prompt.md` | Промпт виконаного проходу: створити Typst production pilot або professional handoff package. |
| Завершення | `reconstruction/earliest-sayings-gospel/ritual-ethics-bridegroom-104a-followup-v0.1.md` | Follow-up рішення для 104A: appendix-only stable, без зміни clean reader. |
| Завершення | `corpus/cards/card-quality-audit-v0.2.md` | Аудит gold-level нормалізації карток: 114/114 мають поточний v0.2 status block; головна наступна прогалина - publication decision depth. |
| Завершення | `corpus/cards/five-source-apparatus-audit-v0.1.md` | Аудит пʼятиджерельного апарату в картках: усі 114 мають P.Oxy./Coptic/canonical channel, але canonical Greek local extraction ще майже весь попереду. |
| Завершення | `corpus/cards/reader-interpretation-expansion-audit-v0.1.md` | Аудит читацького тлумачення в картках: усі 114 логій мають простий сенс, можливі прочитання, реконструкційне значення й застереження, включно з відкинутими логіями. |
| Завершення | `corpus/cards/canonical-greek-extraction-audit-v0.1.md` | Аудит canonical Greek extraction: 81 картка отримала SBLGNT Greek controls, 33 лишаються pending. |
| Завершення | `corpus/cards/poxy-xml-extraction-audit-v0.1.md` | Аудит P.Oxy. XML extraction cleanup: закрито pending line extraction для логій 24, 27, 28, 29, 30, 37, 38 і 77. |
| Завершення | `corpus/tables/logia-workflow-matrix.md` | Операційна матриця 114 логій: картки, evidence notes, рішення, стан читабельного тексту й наступні дії. |
| Завершення | `reconstruction/earliest-sayings-gospel/full-corpus-classification-v0.1.md` | Перша повна класифікація всіх 114 логій після завершення первинних карток: reader text, high-priority candidates, deferred clusters and secondary material. |
| Завершення | `reconstruction/earliest-sayings-gospel/final-all-114-decision-audit-v0.1.md` | Аудит перед фіналізацією clean reader: що вже стабільне, що потребує split-core review, і які документи застаріли. |
| Завершення | `reconstruction/earliest-sayings-gospel/final-reader-probability-pressure-review-v0.1.md` | Pre-freeze review напруги між probability profiles і clean-reader складом: Logion 1 frame status, high-early non-reader priorities і probability-profile cleanup. |
| Завершення | `reconstruction/earliest-sayings-gospel/logion-001-frame-status-review-v0.1.md` | Pre-freeze рішення для Logion 1: лишити синхронізованою в source-layer reader, але фінально трактувати як рамку/пролог збірки, не як звичайну включену логію. |
| Завершення | `reconstruction/earliest-sayings-gospel/split-core-high-early-pressure-review-c-v0.1.md` | Pre-freeze Review C: 46A і 91A передано в controlled reader-candidate pass; 90 лишено appendix-only; 103A/104A були відкладені до cluster-control; обидва пізніше закриті окремими passes. |
| Завершення | `reconstruction/earliest-sayings-gospel/controlled-reader-candidate-pass-46a-91a-v0.1.md` | Controlled reader pass: 46A і 91A додано до clean reader як марковані ядра; reader set розширено до 36 одиниць. |
| Завершення | `reconstruction/earliest-sayings-gospel/thief-watchfulness-cluster-control-pass-21-103-v0.1.md` | Шостий cluster-control pass: 103A додано до clean reader як марковане ядро; повні Logia 21 і 103 лишаються appendix-only; reader set розширено до 37 одиниць. |
| Завершення | `reconstruction/earliest-sayings-gospel/evidence-control-inventory-v0.1.md` | Інвентаризація фактичних evidence notes і control files для 114 логій перед true all-114 publication decision table. |
| Завершення | `reconstruction/earliest-sayings-gospel/all-114-publication-decision-table-v0.1.md` | Publication-control table для всіх 114 логій: після Package B `NEEDS_EVIDENCE_BEFORE_FINAL` = 0; після living/dead/world pass перший cluster-control документ уже привʼязаний до рішень. |
| Завершення | `reconstruction/earliest-sayings-gospel/full-appendix-p1-non-reader-package-v0.1.md` | Audit виконаного Phase 5 appendix expansion для P1 non-reader логій 23, 24, 28, 29, 30, 37, 38, 75, 77, 104, 106. |
| Завершення | `reconstruction/earliest-sayings-gospel/full-appendix-reader-interpretation-sync-v0.1.md` | Audit синхронізації full appendix із картковим читацьким шаром: на момент sync 114/114 appendix-секцій отримали `Читацьке тлумачення з картки`; після editorial consolidation Logia 1-114 усі секції інтегровано в основний коментар. |
| Завершення | `reconstruction/earliest-sayings-gospel/full-appendix-editorial-consolidation-051-060-v0.1.md` | Audit виконаного print-safe editorial consolidation package для Logia 51-60. |
| Завершення | `reconstruction/earliest-sayings-gospel/full-appendix-editorial-consolidation-061-070-v0.1.md` | Audit виконаного print-safe editorial consolidation package для Logia 61-70. |
| Завершення | `reconstruction/earliest-sayings-gospel/full-appendix-editorial-consolidation-071-080-v0.1.md` | Audit виконаного print-safe editorial consolidation package для Logia 71-80. |
| Завершення | `reconstruction/earliest-sayings-gospel/full-appendix-editorial-consolidation-081-090-v0.1.md` | Audit виконаного print-safe editorial consolidation package для Logia 81-90. |
| Завершення | `reconstruction/earliest-sayings-gospel/full-appendix-editorial-consolidation-091-100-v0.1.md` | Audit виконаного print-safe editorial consolidation package для Logia 91-100; залишок appendix debt зменшено до 13 card-derived blocks і 9 working-index phrases. |
| Завершення | `reconstruction/earliest-sayings-gospel/full-appendix-editorial-consolidation-101-114-v0.1.md` | Audit фінального print-safe editorial consolidation package для Logia 101-114; remaining card-derived blocks і working-index prose зменшено до 0. |
| Завершення | `reconstruction/earliest-sayings-gospel/full-appendix-editorial-consolidation-001-010-v0.1.md` | Перший editorial consolidation package для full appendix: Logia 1-10 перетворено на цілісні читацькі секції без дублювання card-derived blocks. |
| Завершення | `reconstruction/earliest-sayings-gospel/full-appendix-editorial-consolidation-011-020-v0.1.md` | Другий editorial consolidation package для full appendix: Logia 11-20 перетворено на цілісні читацькі секції; глобальний source-heading формат стандартизовано до 114/114. |
| Завершення | `reconstruction/earliest-sayings-gospel/full-appendix-editorial-consolidation-021-030-v0.1.md` | Третій print-safe editorial consolidation package для full appendix: Logia 21-30 перетворено на цілісні читацькі секції без дублювання card-derived blocks. |
| Завершення | `reconstruction/earliest-sayings-gospel/full-appendix-editorial-consolidation-031-040-v0.1.md` | Четвертий print-safe editorial consolidation package для full appendix: Logia 31-40 перетворено на цілісні читацькі секції; особливо уточнено P.Oxy. partial/fragmentary/hypothetical Greek status. |
| Завершення | `reconstruction/earliest-sayings-gospel/p1-non-reader-evidence-rationale-pass-v0.1.md` | Audit попереднього evidence-rationale pass: створено 11 direct evidence notes; цей стан superseded Package A row нижче. |
| Завершення | `reconstruction/earliest-sayings-gospel/p1-remaining-evidence-rationale-package-a-v0.1.md` | Audit Package A evidence-rationale pass: створено 10 direct evidence notes для логій 14, 17, 18, 21, 40, 42, 48, 49, 50, 51; all-114 `NEEDS_EVIDENCE_BEFORE_FINAL` зменшено до 16. |
| Завершення | `reconstruction/earliest-sayings-gospel/p1-remaining-evidence-rationale-package-b-v0.1.md` | Audit Package B evidence-rationale pass: створено 16 direct evidence notes для логій 52, 56, 58, 59, 60, 62, 67, 68, 69, 81, 82, 91, 92, 97, 101, 111; all-114 `NEEDS_EVIDENCE_BEFORE_FINAL` зменшено до 0. |
| Завершення | `reconstruction/earliest-sayings-gospel/living-dead-world-cluster-control-pass-v0.1.md` | Перший cluster-control pass: логії 11, 18, 52, 56, 59, 60, 80, 111 залишено поза clean reader; Logion 80 отримала cluster support без direct evidence note. |
| Завершення | `reconstruction/earliest-sayings-gospel/notes/living-dead-world-cluster-control-en.md` | Англомовна cluster-control note для living/dead/world групи: розрізняє контрольовані підодиниці, внутрішню томину когерентність і appendix-only рішення. |
| Завершення | `reconstruction/earliest-sayings-gospel/beatitudes-cluster-control-pass-v0.1.md` | Другий cluster-control pass: Logion 54 підтверджено для clean reader з маркером; 58, 68, 69 залишено appendix-only. |
| Завершення | `reconstruction/earliest-sayings-gospel/notes/beatitudes-cluster-control-en.md` | Англомовна cluster-control note для beatitudes групи: пояснює різницю між включеною 54 і невключеними 58/68/69. |
| Завершення | `reconstruction/earliest-sayings-gospel/seek-find-cluster-control-pass-v0.1.md` | Третій cluster-control pass: Logion 2 підтверджено як головний seek/find представник clean reader; 92 і 94 залишено appendix-only. |
| Завершення | `reconstruction/earliest-sayings-gospel/notes/seek-find-cluster-control-en.md` | Англомовна cluster-control note для seek/find групи: пояснює вибір Logion 2 над дублетними або розширеними формами 92/94. |
| Завершення | `reconstruction/earliest-sayings-gospel/family-renunciation-cluster-control-pass-v0.1.md` | Четвертий cluster-control pass: Logia 16 і 99 підтверджено як clean-reader ядра з маркером; 55 і 101 залишено appendix-only. |
| Завершення | `reconstruction/earliest-sayings-gospel/notes/family-renunciation-cluster-control-en.md` | Англомовна cluster-control note для family-renunciation групи: розділяє родинний конфлікт, справжню родину, радикальне учнівство, cross-bearing і томину true-mother/life символіку. |
| Завершення | `reconstruction/earliest-sayings-gospel/fire-kingdom-cluster-control-pass-v0.1.md` | П'ятий cluster-control pass: Logion 10 підтверджено як clean-reader fire-casting core; Logion 82 залишено appendix-only. |
| Завершення | `reconstruction/earliest-sayings-gospel/notes/thief-watchfulness-cluster-control-21-103-en.md` | Англомовна cluster-control note для Logia 21/103: 103A як clean-reader representative; Logion 21 як composite support. |
| Завершення | `reconstruction/earliest-sayings-gospel/notes/fire-kingdom-cluster-control-en.md` | Англомовна cluster-control note для fire/kingdom групи: розділяє прямий Luke 12:49 контроль для Logion 10 і тематично-внутрішній контроль для Logion 82. |
| Завершення | `reconstruction/earliest-sayings-gospel/wealth-renunciation-cluster-control-pass-v0.1.md` | Сьомий cluster-control pass: 63, 72, 95 і 100 лишаються clean-reader представниками з маркером; 64, 76, 81, 90, 109 і 110 лишаються appendix-only або deferred. |
| Завершення | `reconstruction/earliest-sayings-gospel/notes/wealth-renunciation-cluster-control-en.md` | Англомовна cluster-control note для wealth/renunciation групи: пояснює representative strategy і залежні/композитні ризики невключених логій. |
| Завершення | `reconstruction/earliest-sayings-gospel/logion-114-publication-exclusion-rationale-v0.1.md` | Publication-facing rationale для виключення логії 114 з clean reader без приховування тексту з appendix. |
| Завершення | `reconstruction/earliest-sayings-gospel/notes/logion-114-exclusion-rationale-en.md` | Англомовний dossier-ready rationale: Mary/Peter/gender-transformation scene як secondary exclusion case. |
| Завершення | `reconstruction/earliest-sayings-gospel/split-core-decision-review-a-v0.1.md` | Перевірка логій 45, 47, 63, 64, 65-66: які ядра промотувати в майбутній reader pass, а що лишити appendix-only. |
| Завершення | `reconstruction/earliest-sayings-gospel/split-core-decision-review-b-v0.1.md` | Перевірка логій 76, 78, 79, 94, 103, 109, 113: які ядра промотувати в майбутній reader pass, а що лишити appendix-only. |
| Робочий промпт | `project/ide-codex-master-project-prompt.md` | Головний промпт проекту для наступних кроків реконструкції, корпусної роботи, коментарів і фінального видання. |
| Робочий промпт | `project/ide-codex-open-task-prompt-factory-v0.1-prompt.md` | Мета-промпт, який створює актуальну чергу високоякісних промптів для незакритих задач і визначає порядок виконання. |
| Робочий промпт | `project/ide-codex-full-appendix-editorial-consolidation-071-080-v0.1-prompt.md` | Промпт виконаного проходу: print-safe editorial consolidation для appendix Logia 71-80. |
| Робочий промпт | `project/ide-codex-full-appendix-editorial-consolidation-081-090-v0.1-prompt.md` | Промпт виконаного проходу: print-safe editorial consolidation для appendix Logia 81-90. |
| Робочий промпт | `project/ide-codex-full-appendix-editorial-consolidation-091-100-v0.1-prompt.md` | Промпт виконаного проходу: print-safe editorial consolidation для appendix Logia 91-100. |
| Робочий промпт | `project/ide-codex-full-appendix-editorial-consolidation-101-114-v0.1-prompt.md` | Промпт виконаного проходу: фінальний print-safe editorial consolidation package для appendix Logia 101-114. |
| Робочий промпт | `project/ide-codex-wealth-renunciation-cluster-control-v0.1-prompt.md` | Промпт виконаного проходу: cluster-control для wealth/renunciation групи. |
| Робочий промпт | `project/ide-codex-logion-114-publication-exclusion-rationale-v0.1-prompt.md` | Промпт виконаного проходу: publication-level exclusion rationale логії 114. |
| Робочий промпт | `project/ide-codex-gold-card-quality-normalization-v0.2-prompt.md` | Промпт виконаного проходу: підняти всі 114 карток до єдиного gold-level status check v0.2 без передчасного промотування нових логій. |
| Робочий промпт | `project/ide-codex-five-source-card-apparatus-v0.1-prompt.md` | Промпт виконаного проходу: внести в кожну картку пʼять джерельних каналів із текстами або явною позначкою відсутності. |
| Робочий промпт | `project/ide-codex-canonical-greek-extraction-pass-v0.1-prompt.md` | Промпт виконаного проходу: витягнути canonical Greek controls із локального SBLGNT у картки. |
| Робочий промпт | `project/ide-codex-quality-remediation-master-prompt.md` | Головний промпт для поетапного усунення недоліків, починаючи з pending P.Oxy. XML extraction cleanup. |
| Робочий промпт | `project/ide-codex-evidence-control-inventory-v0.1-prompt.md` | Промпт виконаного Phase 3 проходу: звірити evidence notes і control files із workflow matrix. |
| Робочий промпт | `project/ide-codex-all-114-publication-decision-table-v0.1-prompt.md` | Промпт виконаного Phase 4 проходу: створити all-114 publication decision table і перевести проект до full appendix expansion. |
| Робочий промпт | `project/ide-codex-full-appendix-p1-non-reader-package-v0.1-prompt.md` | Промпт виконаного Phase 5 проходу: розгорнути appendix для першого P1 non-reader пакета без зміни clean reader. |
| Робочий промпт | `project/ide-codex-p1-non-reader-evidence-rationale-v0.1-prompt.md` | Промпт виконаного Phase 5 evidence-rationale pass: створити direct notes для 23, 24, 28, 29, 30, 37, 38, 75, 77, 104, 106. |
| Робочий промпт | `project/ide-codex-living-dead-world-cluster-control-v0.1-prompt.md` | Промпт виконаного cluster-control проходу для living/dead/world групи. |
| Робочий промпт | `project/ide-codex-beatitudes-cluster-control-v0.1-prompt.md` | Промпт виконаного cluster-control проходу для beatitudes групи. |
| Робочий промпт | `project/ide-codex-seek-find-cluster-control-v0.1-prompt.md` | Промпт виконаного cluster-control проходу для seek/find групи. |
| Робочий промпт | `project/ide-codex-family-renunciation-cluster-control-v0.1-prompt.md` | Промпт виконаного cluster-control проходу для family-renunciation групи. |
| Робочий промпт | `project/ide-codex-fire-kingdom-cluster-control-v0.1-prompt.md` | Промпт виконаного cluster-control проходу для fire/kingdom групи. |
| Робочий промпт | `project/ide-codex-final-reader-probability-pressure-review-v0.1-prompt.md` | Промпт виконаного pre-freeze review: перевірити Logion 1, high-early non-readers і probability-profile cleanup без автоматичної зміни clean reader. |
| Робочий промпт | `project/ide-codex-logion-001-frame-status-review-v0.1-prompt.md` | Промпт виконаного точкового review: зафіксувати Logion 1 як frame/prologue case перед final clean-reader freeze. |
| Робочий промпт | `project/ide-codex-split-core-high-early-pressure-review-c-v0.1-prompt.md` | Промпт виконаного Review C: перевірити high-early non-reader логії 46, 90, 91, 103 і 104 без автоматичного розширення clean reader. |
| Робочий промпт | `project/ide-codex-controlled-reader-candidate-pass-46a-91a-v0.1-prompt.md` | Промпт виконаного controlled reader pass: вирішити 46A/91A і синхронно оновити всі reader-шари. |
| Робочий промпт | `project/ide-codex-reader-interpretation-card-expansion-v0.1-prompt.md` | Промпт виконаного проходу: додати в усі 114 карток розгорнуте читацьке тлумачення, включно з невключеними й відкинутими логіями. |
| Робочий промпт | `project/ide-codex-full-appendix-reader-interpretation-sync-v0.1-prompt.md` | Промпт виконаного проходу: синхронізувати full appendix із читацькими тлумаченнями з усіх 114 карток. |
| Робочий промпт | `project/ide-codex-full-appendix-editorial-consolidation-001-010-v0.1-prompt.md` | Промпт виконаного проходу: редакційно консолідувати перші appendix-секції Logia 1-10. |
| Робочий промпт | `project/ide-codex-full-appendix-editorial-consolidation-011-020-v0.1-prompt.md` | Промпт виконаного проходу: редакційно консолідувати appendix-секції Logia 11-20. |
| Робочий промпт | `project/ide-codex-full-appendix-editorial-consolidation-021-030-v0.1-prompt.md` | Промпт виконаного проходу: print-safe редакційно консолідувати appendix-секції Logia 21-30. |
| Робочий промпт | `project/ide-codex-full-appendix-editorial-consolidation-031-040-v0.1-prompt.md` | Промпт виконаного проходу: print-safe редакційно консолідувати appendix-секції Logia 31-40. |
| Робочий промпт | `project/ide-codex-print-digital-publication-architecture-v0.1-prompt.md` | Промпт виконаного проходу: зафіксувати print/digital publication architecture і правила print-safe references. |
| Робочий промпт | `project/ide-codex-corpus-sprint-081-100-quality-prompt.md` | Якісний промпт для Sprint G: первинні картки логій 81-100 і оновлення контрольних таблиць без передчасного розширення чистого читацького тексту. |
| Робочий промпт | `project/ide-codex-corpus-sprint-101-114-quality-prompt.md` | Якісний промпт для Sprint H: завершити первинне покриття логій 101-114 і підготувати проект до загальної класифікації корпусу. |
| Робочий промпт | `project/ide-codex-full-corpus-classification-prompt.md` | Промпт для першої повної класифікації 114 логій і вибору high-priority evidence-note set. |
| Реконструкція | `reconstruction/earliest-sayings-gospel/README.md` | Карта поточного реконструкційного пакета: clean reader, apparatus, мовні шари, dossier, full appendix і Greek audit. |
| Реконструкція | `reconstruction/earliest-sayings-gospel/reconstructed-gospel-uk.md` | Чистий український текст реконструкції: лише пронумеровані логії, без статусів і коментарів. |
| Реконструкція | `reconstruction/earliest-sayings-gospel/reconstructed-gospel-ar-quranic-register.md` | Арабський літературний reader layer для 37 поточних логій у високому класичному регістрі з явною редакційною межею: не Коран і не сура. |
| Реконструкція | `reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-uk.md` | Повний український додаток до 114 логій: усі логії мають статус, рішення, джерельні блоки й інтегрований print-safe читацький коментар. |
| Реконструкція | `reconstruction/earliest-sayings-gospel/greek-retroversion-confidence-audit-v0.1.md` | Контроль грецького шару: extant, lacunose, partial, mixed і hypothetical retroversion. |

## Принцип роботи

Головна одиниця аналізу - не книга, а логія. Кожна логія має отримати окрему картку, після чого можна буде будувати реконструкції шарів.
