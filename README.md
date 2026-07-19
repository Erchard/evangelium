# EUAGELIA

Робочий проєкт для історико-критичної реконструкції найдавнішого досяжного євангелія висловів, збереженого передусім у традиції Євангелія від Фоми.

## Мета

Побудувати прозору реконструкцію раннього шару висловів: не датувати всю книгу однією датою, а оцінювати кожну логію окремо за джерелами, паралелями, мовними ознаками, історичним контекстом і ймовірністю раннього походження.

Фінальна модель має два читацькі шари:

- український читацький розділ **"Логії Ісуса"**, де першими йдуть тільки пронумеровані логії без коментарів і дисклеймерів;
- повний коментований додаток до всіх 114 логій, включно з тими, які не ввійшли до реконструкції.

Назва **"Логії Ісуса"** використовується для головного читацького тексту, щоб не плутати реконструйований корпус із повним **Євангелієм від Фоми**, яке має більше логій і пізніші рамки. Слово "євангеліє" лишається в описі проєкту як сучасний жанровий орієнтир, але не як назва реконструйованого первісного шару.

Публікаційна модель має три виходи з одного контрольованого корпусу: окрема українська паперова книга, окрема англійська паперова книга і повний цифровий науковий апарат. Паперові книги мають бути самодостатніми: замість залежності від клікабельних repo links вони використовують номери логій, позначення свідків, бібліографічні скорочення й друковані індекси. Повний апарат із картками, evidence notes, source paths і audit trail зберігається в digital scholarly companion.

## Структура

- `project/` - службові документи, дорожня карта, специфікація кінцевого продукту, робочі промпти.
- `reconstruction/` - чистий текст, мовні шари, apparatus, evidence dossier і повний коментований додаток.
- `corpus/` - 114 карток логій і робочі таблиці.
- `sources/` - локальні першоджерела, snapshots, коптські й грецькі матеріали.
- `controls/` - синоптичні, міжтекстові й текстові контрольні файли.
- `research/` - методологія, історичні гіпотези, датування й історія досліджень.
- `bibliography/` - майбутня бібліографія і citation/rights material.
- `output/` - згенеровані виходи: українська паперова книга, англійська паперова книга і digital scholarly companion.
- `archive/` - неактивні, але збережені матеріали.

Докладна навігація: `project/repository-structure.md`.

Правила підготовки друкованих і цифрових виходів: `project/print-and-digital-publication-architecture.md`.

## Commons Policy

EUAGELIA задумано як спільне надбання людства, а не як приватну власність однієї особи чи організації. Оригінальна реконструкція, переклади, коментарі, prompts, таблиці й дослідницька архітектура проекту можуть використовуватися будь-ким, включно з комерційним використанням, за умови, що вони не перетворюються на виключну власність або copyright monopoly.

Див. `LICENSE.md` і `project/commons-dedication-and-use-policy.md`. Сторонні джерела зберігають власний правовий статус.

## Поточний стан

Оновлено 2026-07-19 після читацького proof-review української книги.

- Clean Ukrainian reader: 36 логій або ядер.
- Англійський, коптський, грецький, арабський літературний і parallel шари синхронізовані для цих 36 одиниць.
- 114 карток логій створені й вирівняні до gold-level status check v0.2: кожна картка має актуальне рішення, reader status, Greek status, evidence/control links або явну прогалину.
- 114 карток мають `Five-source original-language apparatus v0.1`: P.Oxy. 1, P.Oxy. 654, P.Oxy. 655, коптський NHC II і canonical Greek control channel прямо всередині картки; canonical Greek заповнено для 81 картки.
- 114 карток мають окремий розділ `Читацьке тлумачення`: простий сенс, можливі прочитання, значення для реконструкції й застереження; це покриває також відкинуті та appendix-only логії.
- Full 114-logion appendix має всі 114 логій і тепер синхронізований із картковим шаром `Читацьке тлумачення`: кожна логія має базове читацьке пояснення, а раніше розгорнуті секції збережені як сильніші локальні коментарі.
- Усі editorial consolidation packages виконано для appendix Logia 1-114: дубльовані card-derived blocks і working-index prose прибрано, а повний додаток тепер читається як цілісний print-safe книжковий шар.
- Print/digital publication architecture v0.1 зафіксовано: наступні appendix/editorial passes мають писатися print-safe, з окремим digital-only scholarly apparatus.
- Technical QA baseline закрито: `tools/qa_crosscheck.py` перевіряє 114 карток, 114 appendix-секцій, синхронізацію 36 одиниць основного тексту в мовних шарах і наявність українських перекладних anchors для всіх включених логій.
- Перший Phase 5 appendix pass виконано для P1 non-reader логій 23, 24, 28, 29, 30, 37, 38, 75, 77, 104 і 106.
- Package B evidence-rationale pass закрив останні evidence-blocked логії 52, 56, 58, 59, 60, 62, 67, 68, 69, 81, 82, 91, 92, 97, 101 і 111; пряме evidence-note coverage зросло до 91 логії, а `NEEDS_EVIDENCE_BEFORE_FINAL` в all-114 таблиці зменшено до 0.
- Перший cluster-control pass виконано для living/dead/world групи: 11, 18, 52, 56, 59, 60, 80 і 111; clean reader не розширено, але Logion 80 отримала cluster-level support без штучного direct evidence note.
- Другий cluster-control pass виконано для beatitudes групи: 54, 58, 68 і 69; Logion 54 лишається в основному тексті як обережно включене раннє ядро, а 58/68/69 отримали appendix-only пояснення.
- Третій cluster-control pass виконано для seek/find групи: 2, 92 і 94; Logion 2 лишається головним clean-reader представником мотиву, а 92/94 отримали appendix-only пояснення.
- Четвертий cluster-control pass виконано для family-renunciation групи: 16, 55, 99 і 101; 16 і 99 лишаються обережно включеними clean-reader ядрами, 55 і 101 отримали appendix-only пояснення.
- П'ятий cluster-control pass виконано для fire/kingdom групи: 10 і 82; Logion 10 лишається обережно включеним clean-reader ядром, Logion 82 отримала appendix-only пояснення.
- Шостий cluster-control pass виконано для thief/watchfulness групи: повна логія 21 лишається appendix-only як композитний матеріал, а 103A додано до clean reader як обережно відділене ядро; повна логія 103 лишається appendix-only.
- Сьомий cluster-control pass виконано для wealth/renunciation групи: 63, 72, 95 і 100 лишаються обережно включеними clean-reader представниками; 64, 76, 81, 90, 109 і 110 лишаються appendix-only або deferred.
- Logion 114 publication-level exclusion rationale виконано: фінальна Mary/Peter/gender-transformation логія лишається в appendix як прозорий приклад вторинного excluded material, але не входить до clean reader.
- Logion 1 frame-status review виконано: логія 1 перенесена з головного clean reader до додатку як рамка/пролог збірки, не як звичайна включена логія.
- Controlled reader-candidate pass 46A/91A виконано: 46A і 91A додано до clean reader як обережно відділені ядра; 90 лишено appendix-only; 104A після ritual-ethics / bridegroom follow-up стабілізовано як appendix-only.
- Evidence dossier оновлено до publication-facing draft v1.4: він уже має thesis, source hierarchy, method, selection principles, Greek retroversion policy, cluster summaries, uncertainty model і provisional bibliography/rights note.
- Greek retroversion publication polish виконано: грецький шар тепер послідовно розрізняє extant Greek witness, partial extant Greek witness, lacunose extant Greek witness і `Greek retroversion, hypothetical`; для української паперової книги додано окремий маюскульний clean Greek layer без наголосів, придихів, пунктуації й нумерації.
- Final reader freeze після перегляду логії 1 виконано: 36-unit основний текст зафіксовано для цієї редакції; англійський reader очищено від службових приміток і bracketed apparatus labels.
- Generator-ready book source packages створено для української й англійської паперових книг, а також digital scholarly companion manifest.
- Bibliography / rights / citation / reproducibility layer оновлено до release verification pass v0.2: generic `VERIFY` / unresolved source-rights маркери замінено конкретними release statuses, open/public-domain controls перевірено, protected controls обмежено режимом citation/control-only.
- Print / digital render proof preparation v0.1 виконано: paper-book sources перевірені як print-safe, citation-key table створено, renderer interface і blockers перед першими proof artifacts зафіксовано.
- Render pipeline and first proofs v0.1 виконано: перші HTML/PDF proofs були створені, а застарілий first-proof renderer перенесено в `archive/obsolete-output-pipeline/`; активним лишається `tools/render_full_book_proofs.py`.
- First proof QA and layout corrections v0.1 виконано: paper proofs переведено в перший Bible-style напрям із компактним двоколонковим clean text і serif typography.
- Bible-style book design and index pass v0.1 виконано: український і англійський paper proofs мають компактний Bible-style clean reader, окрему reader-note сторінку, print-safe split indexes і не містять внутрішніх repo paths або URLs у паперовому PDF-тексті.
- Final proof polish, bibliography, and TOC v0.1 виконано: paper proofs мають кращий title/front matter, чесний proof-stable contents, компактну друковану bibliography/source-key сторінку, стиснені witness/status індекси й менш щільний non-included index.
- Release-candidate proof package audit v0.1 виконано: поточні PDF визнано придатними як first public proof skeletons, але не як фінальні release candidates, бо в паперових книгах ще немає повного 114-логійного читацького додатка.
- Full book assembly and typesetting pipeline v0.1 виконано: створено повний український paper-book source і full proof із clean text first та повним 114-логійним додатком; пізніші проходи довели англійський proof до повного clean text + 114-logion appendix + dossier формату.
- Full Ukrainian book proof QA and appendix typography v0.1 виконано: український full proof переглянуто через contact-sheet proofing, структурний QA пройдено, а paper-facing appendix labels локалізовано українською без зміни clean reader або рішень.
- English full 114-logion appendix generation v0.1 виконано: створено перший повний англійський structural draft appendix для 114/114 логій, підключено до English full paper book, згенеровано 177-сторінковий English full proof.
- English appendix editorial quality pass v0.1 виконано: англійський appendix отримав системний reader-facing шар `What This Saying Is About`, менш повторювані interpretation options, кращі source-status фрази і paper-sanitizer без draft/status leakage.
- Full English book proof QA and typography v0.1 виконано: English full proof перебудовано, перевірено текстово й візуально через page PNG/contact sheets; усі 114 appendix-секцій, evidence dossier, summary block і bibliography присутні без видимого обрізання або paper-only path leakage.
- Digital scholarly companion expansion v0.1 виконано: створено deterministic generator, all-114 cross-reference index, source-witness inventory, artifact checksums, audit-trail index і digital companion proof.
- Browsable digital companion HTML v0.1 виконано: створено локальний static HTML companion із searchable/filterable all-114 logion index, expandable detail panels, source witness sections, audit trail і 762 валідними локальними file links.
- Final production typesetting and copyedit gate v0.1 виконано: ReportLab залишено proof-only, фінальним production path обрано Typst/professional handoff, створено copyedit/proof checklist і release-candidate blocker list.
- Typst production pilot v0.1 виконано як handoff package: створено Typst-ready template, український і англійський pilot sources, handoff checklist і production manifest; компіляція чекає Typst/professional environment.
- Release-candidate audit v1.0-rc1 виконано: проект content/proof-package complete, але не 100% release candidate до зовнішньої production-компіляції й human copyedit signoff.
- Reader-facing cleanup pass 2026-07-19 виконано: українська паперова книга очищена від службових формул на кшталт `DCLP XML`, `INCLUDE_WITH_MARKER`, `UNCERTAIN`, "квадратні дужки позначають..." і редакторського слова "маркер"; у друкованому шарі лишаються людські пояснення про обережність, джерела й межі реконструкції.
- Поточні proof-артефакти: український full proof - 237 сторінок; англійський full proof - 294 сторінки; digital scholarly companion proof - 29 сторінок.
- Open-task prompt queue створено: `project/open-task-prompt-queue-2026-07-18.md` тепер є актуальною чергою промптів для незакритих задач.

## Найближчий робочий цикл

1. Виконувати наступні задачі через `project/project-completion-plan-2026-07-19.md`; поточний `NEXT` - Logion 1 / title / opening-words decision pass.
2. Перед і після кожного великого проходу запускати `python3 tools/qa_crosscheck.py`, щоб одразу ловити розсинхрони нумерації, clean-reader складу й appendix anchors.
3. У Typst-capable середовищі виконати compile commands із `output/production-typst/README.md`.
4. Провести фінальну людську copyedit/proof signoff-перевірку й після цього заморозити release checksums.
