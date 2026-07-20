# IDE Codex Prompt: Normalize Current Parallel Edition

Статус: збережений робочий промпт для нормалізації `parallel-edition.md` після повної багатомовної синхронізації поточного reader.

## Завдання

Приведи `reconstruction/earliest-sayings-gospel/parallel-edition.md` до охайного робочого формату, який відповідає поточному чистому українському reader text і ясно розділяє:

- чистий український текст;
- чистий англійський текст;
- коптський base witness excerpt;
- грецький witness / retroversion status;
- reconstruction decision.

## Мета

Поточний `parallel-edition.md` уже містить 24 включені логії, але таблиця змішує:

- чистий текст;
- старі маркери на кшталт `[Можливе розгортання]`;
- технічні статуси;
- грецькі свідки й ретроверсії в одному полі.

Потрібно зробити цей файл читабельним другим шаром, а не лабораторною чернеткою.

## Перед початком прочитай

- `project/final-product-specification.md`
- `project/clean-reader-text-first-page-principle.md`
- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-uk.md`
- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-en.md`
- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-coptic.md`
- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-greek.md`
- `reconstruction/earliest-sayings-gospel/inclusion-decisions-table.md`

## Онови parallel edition

Файл:

- `reconstruction/earliest-sayings-gospel/parallel-edition.md`

Створи таблицю для всіх 24 логій, які зараз є в `reconstructed-gospel-uk.md`:

- 1, 2, 3, 4, 5, 6, 9, 10, 16, 20, 22, 25, 26, 31, 32, 33, 34, 35, 36, 39, 41, 54, 72, 73.

Колонки:

- `Unit`
- `Coptic Base`
- `Greek Layer`
- `Ukrainian Reader`
- `English Reader`
- `Decision`

## Правила

- Українська колонка має відповідати чистому reader text без квадратних дужок, статусів і ярликів.
- Англійська колонка має відповідати `reconstructed-gospel-en.md` без технічних ярликів.
- У грецькій колонці треба чітко позначати:
  - `Extant Greek`
  - `Partial extant Greek`
  - `Lacunose P.Oxy.`
  - `Greek retroversion, hypothetical`
- Не називай гіпотетичну ретроверсію extant witness.
- Для логій 1-5 прибери старі `[Frame]`, `[Possible expansion]`, `[Можливе розгортання]` з reader columns; вони можуть бути пояснені в апараті, але не тут.
- Coptic column може містити excerpt, бо повний коптський текст уже є в `reconstructed-gospel-coptic.md`.
- Не змінюй `reconstructed-gospel-uk.md`.

## Онови журнал

Після нормалізації онови:

- `sources/primary_texts/collection-log.md`

## Перевірка якості

Після змін перевір:

- `parallel-edition.md` має рівно 24 логійні рядки;
- таблиця має однакову кількість колонок у кожному рядку;
- у `Ukrainian Reader` і `English Reader` для Logia 1-5 немає квадратних дужок;
- у Greek Layer для ретроверсій є фраза `Greek retroversion, hypothetical`;
- чистий український reader не змінено і не містить технічних маркерів.

## Фінальний звіт

Повідом українською:

- який промпт збережено;
- що змінено в `parallel-edition.md`;
- що перевірено;
- який наступний логічний крок.
