# IDE Codex Prompt: Evidence Sprint High Priority 01

Статус: збережений робочий промпт для першого evidence-note sprint після повної класифікації корпусу.

## Завдання

Створи перший пакет англомовних evidence notes для найперспективніших логій, які після `full-corpus-classification-v0.1.md` отримали статус `HIGH_PRIORITY_DEEPENING`.

Опрацюй:

- Logion 41
- Logion 45
- Logion 47
- Logion 54
- Logion 63
- Logion 64
- Logion 65-66 як один кластер
- Logion 72
- Logion 73

## Мета

Мета цього кроку - не автоматично розширити чистий український текст, а створити доказовий фундамент для наступних рішень.

Після цього спринту має бути зрозуміло:

- які з цих логій можуть перейти до `INCLUDE_WITH_MARKER`;
- які треба розщепити на коротші ядра;
- які лишаються `UNCERTAIN`;
- які синоптичні або біблійні паралелі треба перевірити глибше;
- які evidence notes стануть базою для майбутнього оновлення reader text.

## Перед початком прочитай

- `reconstruction/earliest-sayings-gospel/full-corpus-classification-v0.1.md`
- `corpus/tables/logia-workflow-matrix.md`
- відповідні картки логій у `corpus/cards/`
- `reconstruction/earliest-sayings-gospel/inclusion-decisions-table.md`
- приклад якісної note: `reconstruction/earliest-sayings-gospel/notes/logion-020-evidence-en.md`

## Створи notes

Створи:

- `reconstruction/earliest-sayings-gospel/notes/logion-041-evidence-en.md`
- `reconstruction/earliest-sayings-gospel/notes/logion-045-evidence-en.md`
- `reconstruction/earliest-sayings-gospel/notes/logion-047-evidence-en.md`
- `reconstruction/earliest-sayings-gospel/notes/logion-054-evidence-en.md`
- `reconstruction/earliest-sayings-gospel/notes/logion-063-evidence-en.md`
- `reconstruction/earliest-sayings-gospel/notes/logion-064-evidence-en.md`
- `reconstruction/earliest-sayings-gospel/notes/logion-065-066-evidence-en.md`
- `reconstruction/earliest-sayings-gospel/notes/logion-072-evidence-en.md`
- `reconstruction/earliest-sayings-gospel/notes/logion-073-evidence-en.md`

## Структура кожної note

Кожна note має містити:

- decision;
- confidence;
- textual witnesses;
- Greek witness / retroversion status;
- synoptic or scriptural controls;
- main evidence;
- early-core assessment;
- secondary-layer indicators;
- limits;
- probability assessment;
- reconstruction implication;
- next work.

## Правила

- Не змінюй `reconstructed-gospel-uk.md`.
- Не додавай нові логії в reader text у цьому спринті.
- Якщо evidence note ще не достатня для включення, чесно лишай `UNCERTAIN`.
- Якщо ядро сильне, але немає extant Greek Thomas witness, використовуй `INCLUDE_WITH_MARKER candidate`, а не безумовне `INCLUDE`.
- Якщо логія композиційна, розщепи її на підодиниці.
- Для Logion 65-66 розглянь притчу про орендарів і rejected-stone saying як кластер, але не змішуй їх в одне рішення.

## Онови контрольні файли

Після створення notes:

- онови `corpus/tables/logia-workflow-matrix.md`, позначивши evidence note як `YES`;
- додай рядки до `reconstruction/earliest-sayings-gospel/inclusion-decisions-table.md`;
- онови `sources/primary_texts/collection-log.md`;
- за потреби уточни `full-corpus-classification-v0.1.md`, але не змінюй кошик без сильного аргументу.

## Фінальний звіт

Повідом українською:

- які notes створено;
- які логії стали найсильнішими кандидатами для наступного включення;
- які лишаються композиційними або непевними;
- який наступний evidence sprint варто виконати.
