# IDE Codex Prompt: Multilingual Sync for Remaining Current Reader Logia

Статус: збережений робочий промпт для синхронізації решти вже включених українських логій із багатомовними шарами.

## Завдання

Після попереднього sync-pass Logia 41, 54, 72, 73 уже внесені в англійський, коптський, грецький і parallel-edition файли.

Тепер синхронізуй решту логій, які вже присутні в чистому українському reader text, але ще не внесені до багатомовних шарів:

- Logion 6
- Logion 9
- Logion 10
- Logion 16
- Logion 20
- Logion 22
- Logion 25
- Logion 26
- Logion 31
- Logion 32
- Logion 33
- Logion 34
- Logion 35
- Logion 36
- Logion 39

## Мета

Зробити так, щоб поточний чистий український реконструйований текст мав відповідний:

- English reader layer;
- Coptic base witness layer;
- Greek extant / retroversion layer;
- compact parallel-edition row.

Це не фінальна публікаційна колація, а якісний робочий багатомовний sync-pass.

## Перед початком прочитай

- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-uk.md`
- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-en.md`
- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-coptic.md`
- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-greek.md`
- `reconstruction/earliest-sayings-gospel/parallel-edition.md`
- `sources/primary_texts/coptic/linssen-thomas-coptic-unicode-working.txt`
- `sources/primary_texts/greek_poxy/poxy654-transcription-working.md`
- `sources/primary_texts/greek_poxy/dclp-poxy1-62838.xml`
- `sources/primary_texts/greek_poxy/dclp-poxy655-62839.xml`
- relevant evidence notes and synoptic controls for the listed logia.

## Онови англійський reader layer

Файл:

- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-en.md`

Додай англійські робочі переклади для всіх перелічених логій.

Правила:

- переклад має відповідати чистому українському reader text, а не повній коптській логії, якщо в reader увійшло тільки ядро;
- не використовуй сучасні захищені переклади;
- не додавай довгих технічних приміток у reader layer.

## Онови коптський base witness layer

Файл:

- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-coptic.md`

Додай повний коптський NHC II,2 текст для кожної логії з локального Linssen working transcription.

Правила:

- якщо український reader включає тільки ядро, усе одно подай повний коптський base witness;
- коротко поясни в reconstruction note, яка частина була використана в clean reader;
- не приховуй, якщо повна коптська логія ширша або композиційна.

## Онови грецький layer

Файл:

- `reconstruction/earliest-sayings-gospel/reconstructed-gospel-greek.md`

Розрізняй:

- extant Greek P.Oxy. witness;
- partial extant Greek witness;
- reconstructed/lacunose Greek P.Oxy. witness;
- `Greek retroversion, hypothetical`.

Правила:

- Logion 6: P.Oxy. 654 is lacunose/reconstructed for the ethical core.
- Logia 9, 10, 16, 20, 22, 25, 34, 35: no loaded extant Greek Thomas witness; use only clearly marked hypothetical retroversion if useful.
- Logion 26: P.Oxy. 1 preserves the final clause only.
- Logia 31, 32: P.Oxy. 1 is strong.
- Logion 33: P.Oxy. 1 preserves only the opening; lamp unit is hypothetical retroversion.
- Logia 36, 39: P.Oxy. 655 exists but is heavily restored/lacunose.

## Онови parallel edition

Файл:

- `reconstruction/earliest-sayings-gospel/parallel-edition.md`

Додай компактні рядки для всіх перелічених логій.

Правила:

- у Coptic column можна давати стислий excerpt, якщо повний текст є в Coptic base witness file;
- у Greek column обов'язково позначай witness type;
- Ukrainian column має відповідати clean reader;
- English column має відповідати English reader layer.

## Онови контрольні файли

Після синхронізації:

- онови `corpus/tables/logia-workflow-matrix.md`;
- онови `sources/primary_texts/collection-log.md`.

## Перевірка якості

Після змін перевір:

- усі перелічені логії присутні в English layer;
- усі перелічені логії присутні в Coptic layer;
- усі перелічені логії присутні або як extant/partial witness, або як clearly marked hypothetical retroversion у Greek layer;
- усі перелічені логії мають рядки в `parallel-edition.md`;
- clean Ukrainian reader лишився без технічних маркерів.

## Фінальний звіт

Повідом українською:

- який промпт збережено;
- які файли оновлено;
- які логії тепер синхронізовані;
- які грецькі місця лишаються найслабшими або тільки гіпотетичними;
- що є наступним логічним кроком.
