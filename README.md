# EUAGELIA

Робочий проєкт для історико-критичної реконструкції найдавнішого досяжного євангелія висловів, збереженого передусім у традиції Євангелія від Фоми.

## Мета

Побудувати прозору реконструкцію раннього шару висловів: не датувати всю книгу однією датою, а оцінювати кожну логію окремо за джерелами, паралелями, мовними ознаками, історичним контекстом і ймовірністю раннього походження.

Фінальна модель має два читацькі шари:

- чистий реконструйований текст українською, де першими йдуть тільки пронумеровані логії без коментарів і дисклеймерів;
- повний коментований додаток до всіх 114 логій, включно з тими, які не ввійшли до реконструкції.

Публікаційна модель має три виходи з одного контрольованого корпусу: окрема українська паперова книга, окрема англійська паперова книга і повний цифровий науковий апарат. Паперові книги мають бути самодостатніми: замість залежності від клікабельних repo links вони використовують номери логій, позначення свідків, бібліографічні скорочення й друковані індекси. Повний апарат із картками, evidence notes, source paths і audit trail зберігається в digital scholarly companion.

## Структура

- `project/` - службові документи, дорожня карта, специфікація кінцевого продукту, робочі промпти.
- `reconstruction/` - чистий текст, мовні шари, apparatus, evidence dossier і повний коментований додаток.
- `corpus/` - 114 карток логій і робочі таблиці.
- `sources/` - локальні першоджерела, snapshots, коптські й грецькі матеріали.
- `controls/` - синоптичні, міжтекстові й текстові контрольні файли.
- `research/` - методологія, історичні гіпотези, датування й історія досліджень.
- `bibliography/` - майбутня бібліографія і citation/rights material.
- `output/` - майбутні згенеровані виходи: українська паперова книга, англійська паперова книга і digital scholarly companion.
- `archive/` - неактивні, але збережені матеріали.

Докладна навігація: `project/repository-structure.md`.

Правила підготовки друкованих і цифрових виходів: `project/print-and-digital-publication-architecture.md`.

## Commons Policy

EUAGELIA задумано як спільне надбання людства, а не як приватну власність однієї особи чи організації. Оригінальна реконструкція, переклади, коментарі, prompts, таблиці й дослідницька архітектура проекту можуть використовуватися будь-ким, включно з комерційним використанням, за умови, що вони не перетворюються на виключну власність або copyright monopoly.

Див. `LICENSE.md` і `project/commons-dedication-and-use-policy.md`. Сторонні джерела зберігають власний правовий статус.

## Поточний стан

- Clean Ukrainian reader: 37 логій або ядер.
- Англійський, коптський, грецький, арабський літературний і parallel шари синхронізовані для цих 37 одиниць.
- 114 карток логій створені й вирівняні до gold-level status check v0.2: кожна картка має актуальне рішення, reader status, Greek status, evidence/control links або явну прогалину.
- 114 карток мають `Five-source original-language apparatus v0.1`: P.Oxy. 1, P.Oxy. 654, P.Oxy. 655, коптський NHC II і canonical Greek control channel прямо всередині картки; canonical Greek заповнено для 81 картки.
- 114 карток мають окремий розділ `Читацьке тлумачення`: простий сенс, можливі прочитання, значення для реконструкції й застереження; це покриває також відкинуті та appendix-only логії.
- Full 114-logion appendix має всі 114 логій і тепер синхронізований із картковим шаром `Читацьке тлумачення`: кожна логія має базове читацьке пояснення, а раніше розгорнуті секції збережені як сильніші локальні коментарі.
- Усі editorial consolidation packages виконано для appendix Logia 1-114: дубльовані card-derived blocks і working-index prose прибрано, а повний додаток тепер читається як цілісний print-safe книжковий шар.
- Print/digital publication architecture v0.1 зафіксовано: наступні appendix/editorial passes мають писатися print-safe, з окремим digital-only scholarly apparatus.
- Technical QA baseline закрито: `tools/qa_crosscheck.py` перевіряє 114 карток, 114 appendix-секцій, синхронізацію 37 clean-reader одиниць у мовних шарах і наявність точних `Чистий текст реконструкції` anchors для всіх включених логій.
- Перший Phase 5 appendix pass виконано для P1 non-reader логій 23, 24, 28, 29, 30, 37, 38, 75, 77, 104 і 106.
- Package B evidence-rationale pass закрив останні evidence-blocked логії 52, 56, 58, 59, 60, 62, 67, 68, 69, 81, 82, 91, 92, 97, 101 і 111; пряме evidence-note coverage зросло до 91 логії, а `NEEDS_EVIDENCE_BEFORE_FINAL` в all-114 таблиці зменшено до 0.
- Перший cluster-control pass виконано для living/dead/world групи: 11, 18, 52, 56, 59, 60, 80 і 111; clean reader не розширено, але Logion 80 отримала cluster-level support без штучного direct evidence note.
- Другий cluster-control pass виконано для beatitudes групи: 54, 58, 68 і 69; Logion 54 лишається в clean reader з маркером, а 58/68/69 отримали appendix-only пояснення.
- Третій cluster-control pass виконано для seek/find групи: 2, 92 і 94; Logion 2 лишається головним clean-reader представником мотиву, а 92/94 отримали appendix-only пояснення.
- Четвертий cluster-control pass виконано для family-renunciation групи: 16, 55, 99 і 101; 16 і 99 лишаються clean-reader ядрами з маркером, 55 і 101 отримали appendix-only пояснення.
- П'ятий cluster-control pass виконано для fire/kingdom групи: 10 і 82; Logion 10 лишається clean-reader ядром з маркером, Logion 82 отримала appendix-only пояснення.
- Шостий cluster-control pass виконано для thief/watchfulness групи: повна логія 21 лишається appendix-only як композитний матеріал, а 103A додано до clean reader як марковане ядро; повна логія 103 лишається appendix-only.
- Сьомий cluster-control pass виконано для wealth/renunciation групи: 63, 72, 95 і 100 лишаються clean-reader представниками з маркером; 64, 76, 81, 90, 109 і 110 лишаються appendix-only або deferred.
- Logion 114 publication-level exclusion rationale виконано: фінальна Mary/Peter/gender-transformation логія лишається в appendix як прозорий приклад вторинного excluded material, але не входить до clean reader.
- Logion 1 frame-status review виконано: логія 1 лишається синхронізованою в поточному source-layer reader, але фінальна модель має трактувати її як рамку/пролог збірки, не як звичайну включену логію.
- Controlled reader-candidate pass 46A/91A виконано: 46A і 91A додано до clean reader як марковані ядра; 90 лишено appendix-only; 104A після ritual-ethics / bridegroom follow-up стабілізовано як appendix-only.
- Evidence dossier оновлено до publication-facing draft v1.4: він уже має thesis, source hierarchy, method, selection principles, Greek retroversion policy, cluster summaries, uncertainty model і provisional bibliography/rights note.
- Greek retroversion publication polish виконано: грецький шар тепер послідовно розрізняє extant Greek witness, partial extant Greek witness, lacunose extant Greek witness і `Greek retroversion, hypothetical`.
- Final clean-reader freeze виконано: 37-unit clean reader зафіксовано для цієї редакції; англійський clean reader очищено від службових приміток і bracketed apparatus labels.
- Generator-ready book source packages створено для української й англійської паперових книг, а також digital scholarly companion manifest.
- Bibliography / rights / citation / reproducibility layer оновлено до release verification pass v0.2: generic `VERIFY` / unresolved source-rights маркери замінено конкретними release statuses, open/public-domain controls перевірено, protected controls обмежено режимом citation/control-only.
- Print / digital render proof preparation v0.1 виконано: paper-book sources перевірені як print-safe, citation-key table створено, renderer interface і blockers перед першими proof artifacts зафіксовано.
- Render pipeline and first proofs v0.1 виконано: створено `tools/render_first_proofs.py`, згенеровано перші HTML/PDF proofs для української книги, англійської книги й digital companion.
- Open-task prompt queue створено: `project/open-task-prompt-queue-2026-07-18.md` тепер є актуальною чергою промптів для незакритих задач.

## Найближчий робочий цикл

1. Виконувати наступні задачі через `project/open-task-prompt-queue-2026-07-18.md`; поточний `NEXT` - first proof QA and layout corrections.
2. Перед і після кожного великого проходу запускати `python3 tools/qa_crosscheck.py`, щоб одразу ловити розсинхрони нумерації, clean-reader складу й appendix anchors.
3. Виконати first proof QA: PNG preview inspection, table layout correction, front matter, TOC placeholders, paper-path safety.
4. Після цього перейти до фінального PDF/e-book proofing і книжкового дизайну.
