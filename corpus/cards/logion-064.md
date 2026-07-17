# Logion 64

Статус: первинна корпусна картка v0.1.

## Текст

### Коптський текст

Джерело: `sources/primary_texts/coptic/linssen-thomas-coptic-unicode-working.txt`.

> 64 ⲡⲉϫⲉ ⲓ̅ⲥ̅ ϫⲉ ⲟⲩⲣⲱⲙⲉ ⲛⲉⲩⲛ̅ⲧⲁϥ ϩⲛ̅ϣⲙ̅ⲙⲟ ... ⲛ̅ⲣⲉϥⲧⲟⲟⲩ ⲙⲛ̅ ⲛⲉϣⲟ[ⲧⲉ ⲉⲩⲛⲁⲃⲱⲕ] ⲁⲛ` ⲉϩⲟⲩⲛ` ⲉⲛⲧⲟⲡⲟⲥ ⲙ̅ⲡⲁⲓ̈ⲱⲧ`

### Грецький свідок

No loaded Greek Oxyrhynchus witness preserves Thomas 64.

### Буквальний український переклад

Один чоловік мав гостей. Коли приготував вечерю, послав слугу запросити гостей. Запрошені один за одним відмовилися через торгівлю, дім, весілля, село. Господар наказав покликати тих, кого знайдуть на дорогах, щоб вони вечеряли; купці й торговці не ввійдуть до місця мого Отця.

### Робочий український переклад

Запрошені відмовилися від вечері через справи, майно й соціальні обов'язки; тоді господар відкриває вечерю іншим.

## Попередні паралелі

| Джерело | Місце | Нотатка |
| --- | --- | --- |
| Лука | 14:15-24 | Велика вечеря; відмовки; запрошення інших. |
| Матвій | 22:1-14 | Весільний бенкет; розвиненіша алегорична форма. |

## Аналіз

Сильний притчевий кандидат, але повна форма Фоми довга і має фінальний анти-merchant saying. Потрібно відділити притчу про запрошення від фінального висновку.

## Попередній статус

Рішення: `KEEP_APPENDIX_ONLY_FOR_NOW`.

Наступна дія: publication appendix polish; пояснити, чому banquet core і anti-merchant ending не увійшли в clean reader.

## Еталонне вирівнювання картки v0.1

Еталон: `corpus/cards/logion-002.md`. Для складених або шарових логій додатковий практичний еталон: `corpus/cards/logion-006.md`.

### Поточне рішення

- Рішення: 64A/64B `KEEP_APPENDIX_ONLY_FOR_NOW`.
- Reader text: NO.
- Greek witness status: No loaded P.Oxy. witness.
- Попередній шар: запрошення на вечерю і відмовки.
- Поточний робочий статус: Coptic extraction v0.1.

### Ймовірнісний профіль

| Період | Ймовірність | Нотатка |
| --- | ---: | --- |
| До 60 року | 20% | Робоча оцінка з `corpus/tables/logia-index.md`; не є математичним доказом. |
| 60-90 роки | 40% | Робоча оцінка з індексу; переглядати після поглиблення evidence note. |
| 90-130 роки | 30% | Робоча оцінка з індексу; особливо важлива для томиного/редакційного шару. |
| Після 130 року | 10% | Робоча оцінка з індексу; високий показник тут послаблює включення до найдавнішої реконструкції. |

### Доказовий апарат

- Evidence note:
  - `reconstruction/earliest-sayings-gospel/notes/logion-064-evidence-en.md`
- Synoptic/control files:
  - `controls/synoptic-parallels/logion-064-banquet-invitation-controls.md`
- Cluster/context notes:
  - `reconstruction/earliest-sayings-gospel/controlled-clean-reader-candidate-pass-v0.1.md`

### Шарова модель для реконструкції

- Можливе раннє ядро: banquet invitation core is plausible but kept appendix-only in the controlled reader pass.
- Вторинні / томині ризики: anti-merchant ending and long invitation narrative create dependence/secondary-layer risk.
- Грецька політика: У завантаженому корпусі немає extant Greek Thomas witness; не створювати грецьке свідчення без маркування.

### Наступна дія

Publication polish: refine appendix explanation for banquet core and anti-merchant ending.

Примітка якості: цей блок вирівнює картку з еталонним аналітичним стандартом, але не замінює повного поглибленого дослідження. Якщо evidence note або control file відсутні, це означає видиму прогалину, а не мовчазно розв'язану проблему.


## Gold-level status check v0.2

Джерело актуального статусу: `corpus/tables/logia-workflow-matrix.md`. Цей блок є поточним синхронізаційним шаром і має пріоритет над старішими робочими позначками картки, якщо вони розходяться.

### Publication Status

- Current decision: 64A/64B `KEEP_APPENDIX_ONLY_FOR_NOW`.
- Reader text: NO.
- Greek witness status: No loaded P.Oxy. witness.
- Current work status: Controlled reader pass v0.1.
- Evidence note in matrix: YES.
- Clean-reader implication: Не входить до clean reader на цьому етапі; обовʼязково пояснювати в додатку, чому матеріал лишається appendix-only попри наявність традиційних або синоптичних паралелей.

### Evidence Links

Evidence note / dossier files:
- `reconstruction/earliest-sayings-gospel/notes/logion-064-evidence-en.md`

Synoptic/control files:
- `controls/synoptic-parallels/logion-064-banquet-invitation-controls.md`

### Greek/Coptic Policy

- Coptic base: тримати коптський текст як основний збережений witness, доки немає сильнішого первинного контролю.
- Greek layer: Перевіряти лакуни, реконструкції й частковість папірусного свідчення перед публікаційним висновком.
- Якщо грецький текст не збережений, реконструювати його лише як імовірну ретроверсію й прямо маркувати ступінь гіпотетичності.

### Reader/Appendix Obligation

- Для clean reader: не додавати до чистого тексту без нового контрольованого рішення.
- Для full appendix: подати походження, джерельний текст, паралелі, текстологічні ризики, можливі інтерпретації та причину включення або невключення.
- Для відкинутих / відкладених логій: пояснення має бути таким самим серйозним, як для включених логій; читач повинен бачити не лише результат, а й логіку відбору.

### Remaining Work

- Next action: Banquet core remains too long/dependence-risky for this clean-reader pass.
- Publication pass: звірити цю картку з фінальною all-114 decision table, clean-reader складом і повним читацьким додатком.
