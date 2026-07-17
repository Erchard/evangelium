# Logion 63

Статус: первинна корпусна картка v0.1.

## Текст

### Коптський текст

Джерело: `sources/primary_texts/coptic/linssen-thomas-coptic-unicode-working.txt`.

> 63 ⲡⲉϫⲉ ⲓ̅ⲥ̅ ϫⲉ ⲛⲉⲩⲛ̅ ⲟⲩⲣⲱⲙⲉ ⲙ̅ⲡⲗⲟⲩⲥⲓⲟⲥ ... ϩⲛ̅ ⲧⲟⲩϣⲏ ⲉⲧⲙ̅ⲙⲁⲩ ⲁϥⲙⲟⲩ ⲡⲉⲧⲉⲩⲙ̅ ⲙⲁϫⲉ ⲙ̅ⲙⲟϥ` ⲙⲁⲣⲉϥ`ⲥⲱⲧⲙ̅

### Грецький свідок

No loaded Greek Oxyrhynchus witness preserves Thomas 63.

### Буквальний український переклад

Був багатий чоловік, який мав багато майна. Він сказав: використаю моє майно, щоб сіяти, жати, садити, наповнити комори плодами, щоб не мати нестачі. Тієї ночі він помер.

### Робочий український переклад

Багатий планував накопичити ще більше, щоб жити без нестачі, але помер тієї ж ночі.

## Попередні паралелі

| Джерело | Місце | Нотатка |
| --- | --- | --- |
| Лука | 12:16-21 | Притча про багатого нерозумного і комори. |
| Фома | 64, 76 | Критика майна / пріоритет запрошення чи перлини. |

## Аналіз

Сильний high-candidate. Форма коротша й простіша за Луку 12:16-21, але збігається в ключовому сюжеті: багатство, комори, плани, смерть уночі.

## Попередній статус

Рішення: `UNCERTAIN`.

Наступна дія: створити synoptic control table з Luke 12:16-21; можливо підняти коротке ядро до `INCLUDE_WITH_MARKER` після поглиблення.

## Еталонне вирівнювання картки v0.1

Еталон: `corpus/cards/logion-002.md`. Для складених або шарових логій додатковий практичний еталон: `corpus/cards/logion-006.md`.

### Поточне рішення

- Рішення: `INCLUDE_WITH_MARKER`; full logion `UNCERTAIN`.
- Reader text: YES, short rich-fool core.
- Greek witness status: Greek retroversion, hypothetical.
- Попередній шар: багатий, комори і смерть уночі.
- Поточний робочий статус: Coptic extraction v0.1.

### Ймовірнісний профіль

| Період | Ймовірність | Нотатка |
| --- | ---: | --- |
| До 60 року | 25% | Робоча оцінка з `corpus/tables/logia-index.md`; не є математичним доказом. |
| 60-90 роки | 40% | Робоча оцінка з індексу; переглядати після поглиблення evidence note. |
| 90-130 роки | 25% | Робоча оцінка з індексу; особливо важлива для томиного/редакційного шару. |
| Після 130 року | 10% | Робоча оцінка з індексу; високий показник тут послаблює включення до найдавнішої реконструкції. |

### Доказовий апарат

- Evidence note:
  - `reconstruction/earliest-sayings-gospel/notes/logion-063-evidence-en.md`
- Synoptic/control files:
  - `controls/synoptic-parallels/logion-063-rich-fool-luke-control.md`
- Cluster/context notes:
  - `reconstruction/earliest-sayings-gospel/controlled-clean-reader-candidate-pass-v0.1.md`

### Шарова модель для реконструкції

- Можливе раннє ядро: short rich-fool core включено в clean reader.
- Вторинні / томині ризики: напрям залежності від Луки лишається відкритим; hearing formula і будь-яка додаткова моралізація не включені.
- Грецька політика: Грецький шар можна використовувати тільки як `Greek retroversion, hypothetical`, не як рукописний свідок.

### Наступна дія

Publication polish: keep Luke-dependence warning visible in apparatus and dossier.

Примітка якості: цей блок вирівнює картку з еталонним аналітичним стандартом, але не замінює повного поглибленого дослідження. Якщо evidence note або control file відсутні, це означає видиму прогалину, а не мовчазно розв'язану проблему.


## Gold-level status check v0.2

Джерело актуального статусу: `corpus/tables/logia-workflow-matrix.md`. Цей блок є поточним синхронізаційним шаром і має пріоритет над старішими робочими позначками картки, якщо вони розходяться.

### Publication Status

- Current decision: `INCLUDE_WITH_MARKER`; full logion `UNCERTAIN`.
- Reader text: YES.
- Greek witness status: Greek retroversion, hypothetical.
- Current work status: Controlled reader pass v0.1.
- Evidence note in matrix: YES.
- Clean-reader implication: Входить до clean Ukrainian reader як поточна реконструкційна одиниця; у чистому тексті друкувати без статусів і коментарів, а всі застереження переносити в apparatus / appendix.

### Evidence Links

Evidence note / dossier files:
- `reconstruction/earliest-sayings-gospel/notes/logion-063-evidence-en.md`

Synoptic/control files:
- `controls/synoptic-parallels/logion-063-rich-fool-luke-control.md`

### Greek/Coptic Policy

- Coptic base: тримати коптський текст як основний збережений witness, доки немає сильнішого первинного контролю.
- Greek layer: Позначати як гіпотетичну ретроверсію, не як рукописне грецьке свідчення.
- Якщо грецький текст не збережений, реконструювати його лише як імовірну ретроверсію й прямо маркувати ступінь гіпотетичності.

### Reader/Appendix Obligation

- Для clean reader: друкувати тільки реконструйоване ядро без коментарів, дужок і дисклеймерів.
- Для full appendix: подати походження, джерельний текст, паралелі, текстологічні ризики, можливі інтерпретації та причину включення або невключення.
- Для відкинутих / відкладених логій: пояснення має бути таким самим серйозним, як для включених логій; читач повинен бачити не лише результат, а й логіку відбору.

### Remaining Work

- Next action: Clean reader prints short rich-fool core with Luke-dependence warning in apparatus.
- Publication pass: звірити цю картку з фінальною all-114 decision table, clean-reader складом і повним читацьким додатком.
