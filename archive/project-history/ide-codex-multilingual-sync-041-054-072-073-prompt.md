# IDE Codex Prompt: Multilingual Sync for Logia 41, 54, 72, 73

Статус: збережений робочий промпт для синхронізації мовних шарів після clean-reader pass.

## Завдання

Синхронізуй нові включення чистого українського reader text з паралельними мовними файлами:

- Logion 41
- Logion 54
- Logion 72
- Logion 73

## Мета

Після попереднього кроку ці логії вже додані до:

- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-uk.md`
- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-uk-apparatus.md`
- `reconstruction/earliest-sayings-gospel/reader-commentary-uk.md`

Тепер треба зробити так, щоб новий український reader-pass не висів окремо від міжнародного й джерельного шару.

## Перед початком прочитай

- `project/final-product-specification.md`
- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-uk.md`
- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-en.md`
- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-coptic.md`
- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-greek.md`
- `reconstruction/earliest-sayings-gospel/parallel-edition.md`
- `controls/synoptic-parallels/logion-041-has-given-controls.md`
- `controls/synoptic-parallels/logion-054-blessed-poor-controls.md`
- `controls/synoptic-parallels/logion-072-inheritance-dispute-controls.md`
- `controls/synoptic-parallels/logion-073-harvest-workers-controls.md`
- `sources/primary_texts/coptic/linssen-thomas-coptic-unicode-working.txt`

## Онови англійський reader layer

Файл:

- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-en.md`

Додай Logia 41, 54, 72, 73 як робочий англійський переклад реконструйованого українського reader text.

Правила:

- не використовуй сучасні захищені переклади;
- перекладай самостійно;
- лишай статуси й технічні позначки мінімальними;
- якщо файл поки неповний, не приховуй це у статусі.

## Онови коптський base witness layer

Файл:

- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-coptic.md`

Додай повний коптський NHC II,2 текст для Logia 41, 54, 72, 73 із локального Linssen working transcription.

Правила:

- не скорочуй коптський текст без позначення;
- збережи дужки, lacunae і нестабільні місця;
- поясни, що коптський текст є базовим збереженим свідком, а не автоматично реконструйованим найдавнішим шаром.

## Онови грецький layer

Файл:

- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-greek.md`

Для Logia 41, 54, 72, 73 немає loaded extant Greek Thomas witness. Тому:

- не подавай грецький текст як рукописний свідок;
- створи окремі секції `Greek retroversion, hypothetical`;
- познач confidence для кожної ретроверсії;
- коротко поясни basis: Coptic wording, Greek loanwords, synoptic controls, formulaic Greek parallels;
- для Logion 72 зазнач підвищений ризик Luke-dependence.

## Онови parallel edition

Файл:

- `reconstruction/earliest-sayings-gospel/parallel-edition.md`

Додай рядки для Logia 41, 54, 72, 73 з п'ятьма шарами:

- Coptic
- Greek
- Ukrainian
- English
- Status

У грецькому стовпці для цих логій має стояти не “Greek witness”, а `Greek retroversion, hypothetical`.

## Онови контрольні файли

Після синхронізації:

- онови `corpus/tables/logia-workflow-matrix.md`;
- онови `sources/primary_texts/collection-log.md`.

## Перевірка якості

Після змін перевір:

- Logia 41, 54, 72, 73 присутні в `reconstructed-gospel-en.md`;
- Logia 41, 54, 72, 73 присутні в `reconstructed-gospel-coptic.md`;
- Greek layer не називає ці ретроверсії extant witnesses;
- `parallel-edition.md` має рядки для Logia 41, 54, 72, 73;
- workflow matrix відображає multilingual sync;
- clean Ukrainian reader не змінено і лишається без технічних маркерів.

## Фінальний звіт

Повідом українською:

- який промпт збережено;
- які мовні файли оновлено;
- які грецькі форми є лише гіпотетичними ретроверсіями;
- що лишається наступним логічним кроком.
