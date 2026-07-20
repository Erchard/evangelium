# IDE Codex Prompt: Synoptic Control and Coptic Extraction Sprint

Статус: збережений робочий промпт для наступного кроку після `ide-codex-evidence-sprint-high-priority-01-prompt.md`.

## Завдання

Створи контрольний доказовий шар для найсильніших кандидатів попереднього evidence sprint:

- Logion 41
- Logion 54
- Logion 72
- Logion 73

Також витягни повний коптський текст для довших і складніших логій:

- Logion 63
- Logion 64
- Logion 65

## Мета

Мета цього кроку - перейти від первинного висновку `INCLUDE_WITH_MARKER candidate` до обережнішого рішення, яке можна буде використати для наступного оновлення чистого українського читацького тексту.

Після виконання має бути зрозуміло:

- чи Logia 41, 54, 72, 73 достатньо сильні для переходу з `UNCERTAIN; candidate` до `INCLUDE_WITH_MARKER`;
- які саме синоптичні формулювання контролюють кожну логію;
- де Thomas може зберігати коротку незалежну форму, а де ймовірне синоптичне скорочення або вторинне переоформлення;
- чи Logia 63-65 мають повний коптський текст у локальному джерелі, достатній для наступного поглибленого аналізу.

## Перед початком прочитай

- `reconstruction/earliest-sayings-gospel/inclusion-decisions-table.md`
- `reconstruction/earliest-sayings-gospel/notes/logion-041-evidence-en.md`
- `reconstruction/earliest-sayings-gospel/notes/logion-054-evidence-en.md`
- `reconstruction/earliest-sayings-gospel/notes/logion-072-evidence-en.md`
- `reconstruction/earliest-sayings-gospel/notes/logion-073-evidence-en.md`
- `controls/synoptic-parallels/logion-020-mustard-seed.md` як модель детальної таблиці
- `controls/synoptic-parallels/logion-010-fire-luke-control.md` як модель коротшого контрольного файлу
- `sources/primary_texts/coptic/linssen-thomas-coptic-unicode-working.txt`
- локальний SBLGNT cache: `/tmp/euagelia-sblgnt/Mark.txt`, `/tmp/euagelia-sblgnt/Matt.txt`, `/tmp/euagelia-sblgnt/Luke.txt`

## Створи synoptic controls

Створи:

- `controls/synoptic-parallels/logion-041-has-given-controls.md`
- `controls/synoptic-parallels/logion-054-blessed-poor-controls.md`
- `controls/synoptic-parallels/logion-072-inheritance-dispute-controls.md`
- `controls/synoptic-parallels/logion-073-harvest-workers-controls.md`

Кожен файл має містити:

- короткий висновок;
- рішення для реконструкції;
- статус грецького свідка Thomas;
- повний або достатньо точний коптський Thomas text з локального джерела;
- основні синоптичні грецькі паралелі з SBLGNT;
- власний стислий український переклад паралелей;
- motif table;
- direction-of-dependence assessment;
- possible early core;
- publication implication.

## Створи коптський extraction file

Створи:

- `sources/primary_texts/coptic/logia-063-065-coptic-extraction.md`

Файл має містити:

- повний коптський текст Logia 63, 64, 65 з `linssen-thomas-coptic-unicode-working.txt`;
- коротку структурну розбивку кожної логії;
- примітку про lacunae / brackets / нестабільні місця;
- перелік наступних перевірок для Logia 63-65.

## Онови контрольні файли

Після створення нових файлів:

- онови `reconstruction/earliest-sayings-gospel/inclusion-decisions-table.md`;
- онови `corpus/tables/logia-workflow-matrix.md`;
- онови `sources/primary_texts/collection-log.md`;
- за потреби уточни відповідні evidence notes, але не переписуй їх повністю без потреби.

## Правила

- Не змінюй `reconstruction/earliest-sayings-gospel/reconstructed-gospel-uk.md` у цьому спринті.
- Не додавай нових логій у чистий reader text, поки не буде окремого рішення.
- Якщо синоптичний контроль сильний, але немає extant Greek Thomas witness, використовуй `INCLUDE_WITH_MARKER`, а не безумовне `INCLUDE`.
- Якщо напрям залежності невирішений, скажи це прямо.
- Не приховуй слабкі місця: відсутність грецького Thomas witness, можливе синоптичне скорочення, коптські lacunae, композиційність.

## Фінальний звіт

Повідом українською:

- який промпт збережено;
- які файли створено;
- які рішення змінилися;
- які логії стали готовими до наступного окремого кроку: оновлення clean reader text;
- що лишається найважливішим ризиком.
