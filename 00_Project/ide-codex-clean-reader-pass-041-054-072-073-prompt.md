# IDE Codex Prompt: Clean Reader Pass for Logia 41, 54, 72, 73

Статус: збережений робочий промпт для контрольованого оновлення чистого українського reader text після `ide-codex-synoptic-control-and-coptic-extraction-prompt.md`.

## Завдання

Додай до чистого українського реконструйованого тексту логії, які після synoptic-control sprint отримали рішення `INCLUDE_WITH_MARKER`:

- Logion 41
- Logion 54
- Logion 72
- Logion 73

## Мета

Мета цього кроку - не розширити реконструкцію механічно, а акуратно перенести до читацького першого шару тільки ті одиниці, для яких уже створено окремий доказовий контроль.

Чистий reader text має залишатися першим шаром для читача: без дисклеймерів, статусів, квадратних дужок, технічних маркерів і пояснень.

Уся непевність має бути перенесена в другий шар:

- `reconstructed-gospel-uk-apparatus.md`
- `reader-commentary-uk.md`
- evidence notes
- synoptic control files
- workflow matrix

## Перед початком прочитай

- `00_Project/clean-reader-text-first-page-principle.md`
- `00_Project/final-product-specification.md`
- `06_Reconstructions/earliest-sayings-gospel/reconstructed-gospel-uk.md`
- `06_Reconstructions/earliest-sayings-gospel/reconstructed-gospel-uk-apparatus.md`
- `06_Reconstructions/earliest-sayings-gospel/reader-commentary-uk.md`
- `06_Reconstructions/earliest-sayings-gospel/inclusion-decisions-table.md`
- `04_Synoptic_Parallels/logion-041-has-given-controls.md`
- `04_Synoptic_Parallels/logion-054-blessed-poor-controls.md`
- `04_Synoptic_Parallels/logion-072-inheritance-dispute-controls.md`
- `04_Synoptic_Parallels/logion-073-harvest-workers-controls.md`

## Онови чистий український reader

Файл:

- `06_Reconstructions/earliest-sayings-gospel/reconstructed-gospel-uk.md`

Додай логії 41, 54, 72, 73 у правильній загальноприйнятій нумерації.

Правила:

- не перенумеровуй логії;
- не додавай жодних статусів;
- не використовуй квадратні дужки;
- не додавай фрази на кшталт "маркований вислів";
- не додавай коментарі в тіло тексту;
- формулюй українською ясно, але ближче до джерельної форми, ніж до вільної літературної адаптації.

## Онови український апарат

Файл:

- `06_Reconstructions/earliest-sayings-gospel/reconstructed-gospel-uk-apparatus.md`

Додай короткі розділи для Logia 41, 54, 72, 73:

- статус;
- текст у головному reader;
- причина включення;
- причина маркера;
- evidence / synoptic control links.

Також уточни вступне правило читання, щоб воно відображало новий склад reader text.

## Онови український читацький коментар

Файл:

- `06_Reconstructions/earliest-sayings-gospel/reader-commentary-uk.md`

Додай коментарні розділи для Logia 41, 54, 72, 73 у стилі наявних розділів:

- реконструйований текст;
- коротко;
- походження і джерела;
- паралелі;
- можливі тлумачення;
- що лишається непевним;
- чому це увійшло до реконструкції.

Коментар має допомогти читачеві відповісти на питання: "що міг хотіти сказати автор або носій цієї традиції?", не перетворюючись на проповідь або догматичне тлумачення.

## Онови контрольні файли

Після reader-pass:

- онови `05_Logia_Corpus/tables/logia-workflow-matrix.md`;
- онови `02_Sources_And_Manuscripts/primary_texts/collection-log.md`;
- за потреби онови статусний рядок в апараті.

## Перевірка якості

Після змін перевір:

- `reconstructed-gospel-uk.md` починається з `## 1`;
- у clean reader немає `[` або `]`;
- у clean reader немає `INCLUDE`, `UNCERTAIN`, `Статус`, `Маркован`;
- логії 41, 54, 72, 73 присутні;
- апарат і commentary мають відповідні розділи;
- таблиця workflow відображає reader-pass.

## Фінальний звіт

Повідом українською:

- який промпт збережено;
- які файли оновлено;
- які логії додано до чистого reader;
- що залишилось наступним логічним кроком.
