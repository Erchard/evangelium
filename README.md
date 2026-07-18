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

## Поточний стан

- Clean Ukrainian reader: 37 логій або ядер.
- Англійський, коптський, грецький, арабський літературний і parallel шари синхронізовані для цих 37 одиниць.
- 114 карток логій створені й вирівняні до gold-level status check v0.2: кожна картка має актуальне рішення, reader status, Greek status, evidence/control links або явну прогалину.
- 114 карток мають `Five-source original-language apparatus v0.1`: P.Oxy. 1, P.Oxy. 654, P.Oxy. 655, коптський NHC II і canonical Greek control channel прямо всередині картки; canonical Greek заповнено для 81 картки.
- 114 карток мають окремий розділ `Читацьке тлумачення`: простий сенс, можливі прочитання, значення для реконструкції й застереження; це покриває також відкинуті та appendix-only логії.
- Full 114-logion appendix має всі 114 логій і тепер синхронізований із картковим шаром `Читацьке тлумачення`: кожна логія має базове читацьке пояснення, а раніше розгорнуті секції збережені як сильніші локальні коментарі.
- Перші шість editorial consolidation packages виконано для appendix Logia 1-60: дубльовані card-derived blocks прибрано, Logia 7-8 більше не є skeleton-style entries, а Logia 11-60 отримали цілісні print-safe читацькі пояснення з окремим розділом меж непевності.
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
- Logion 1 frame-status review виконано: логія 1 лишається синхронізованою в поточному source-layer reader, але фінальна модель має трактувати її як рамку/пролог збірки, не як звичайну включену логію.
- Controlled reader-candidate pass 46A/91A виконано: 46A і 91A додано до clean reader як марковані ядра; 90 лишено appendix-only; 104A відкладено до ritual-ethics / bridegroom cluster-control.
- Evidence dossier існує як робочий документ, але ще потребує publication pass.
- Open-task prompt queue створено: `project/open-task-prompt-queue-2026-07-18.md` тепер є актуальною чергою промптів для незакритих задач.

## Найближчий робочий цикл

1. Виконувати наступні задачі через `project/open-task-prompt-queue-2026-07-18.md`; поточний `NEXT` - print-safe full appendix editorial consolidation для Logia 61-70.
2. Перед і після кожного великого проходу запускати `python3 tools/qa_crosscheck.py`, щоб одразу ловити розсинхрони нумерації, clean-reader складу й appendix anchors.
3. Після appendix 61-70 виконати wealth/renunciation cluster-control prompt.
4. Продовжити ritual-ethics / bridegroom follow-up для 104A після wealth/renunciation або dossier pass.
5. Після цього виконати evidence dossier publication pass і clean-reader freeze pass.
