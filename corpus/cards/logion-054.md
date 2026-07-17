# Logion 54

Статус: первинна корпусна картка v0.1.

## Текст

### Коптський текст

Джерело: `sources/primary_texts/coptic/linssen-thomas-coptic-unicode-working.txt`.

> ⲡⲉϫⲉ ⲓ̅ⲥ̅ ϫⲉ ϩⲛ̅ⲙⲁⲕⲁⲣⲓⲟⲥ ⲛⲉ ⲛϩⲏⲕⲉ ϫⲉ ⲧⲱⲧⲛ̅ ⲧⲉ ⲧⲙⲛ̅ⲧⲉⲣⲟ ⲛⲙ̅ⲡⲏⲩⲉ`

### Грецький свідок

No loaded Greek Oxyrhynchus witness preserves Thomas 54.

### Буквальний український переклад

Ісус сказав: блаженні бідні, бо ваше є царство небес.

### Робочий український переклад

Блаженні бідні, бо ваше царство небес.

## Попередні паралелі

| Джерело | Місце | Нотатка |
| --- | --- | --- |
| Лука | Лк 6:20 | Дуже сильна паралель: "блаженні бідні, бо ваше царство Боже". |
| Матвій | Мт 5:3 | "Бідні духом" і царство небес. |

## Аналіз

Один із найсильніших кандидатів у спринті: короткий, афористичний, із потужним синоптичним контролем. Потрібне поглиблення перед включенням, особливо через варіант "царство небес" у Фоми.

## Попередній статус

Рішення: `UNCERTAIN`.

Наступна дія: поглибити як high-candidate для можливого `INCLUDE_WITH_MARKER`.

## Еталонне вирівнювання картки v0.1

Еталон: `corpus/cards/logion-002.md`. Для складених або шарових логій додатковий практичний еталон: `corpus/cards/logion-006.md`.

### Поточне рішення

- Рішення: `INCLUDE_WITH_MARKER`.
- Reader text: YES.
- Greek witness status: No loaded P.Oxy. witness.
- Попередній шар: блаженні убогі.
- Поточний робочий статус: Multilingual sync v0.1.

### Ймовірнісний профіль

| Період | Ймовірність | Нотатка |
| --- | ---: | --- |
| До 60 року | 30% | Робоча оцінка з `corpus/tables/logia-index.md`; не є математичним доказом. |
| 60-90 роки | 40% | Робоча оцінка з індексу; переглядати після поглиблення evidence note. |
| 90-130 роки | 25% | Робоча оцінка з індексу; особливо важлива для томиного/редакційного шару. |
| Після 130 року | 5% | Робоча оцінка з індексу; високий показник тут послаблює включення до найдавнішої реконструкції. |

### Доказовий апарат

- Evidence note:
  - `reconstruction/earliest-sayings-gospel/notes/logion-054-evidence-en.md`
- Synoptic/control files:
  - `controls/synoptic-parallels/logion-054-blessed-poor-controls.md`
- Cluster/context notes:
немає окремого файлу; прогалина лишається видимою.

### Шарова модель для реконструкції

- Можливе раннє ядро: є реконструкційний кандидат, але друкувати/оцінювати тільки з маркером непевності.
- Вторинні / томині ризики: головний ризик: напрям залежності й рівень незалежності традиції ще потребують контролю.
- Грецька політика: У завантаженому корпусі немає extant Greek Thomas witness; не створювати грецьке свідчення без маркування.

### Наступна дія

English/Coptic/Greek retroversion/parallel rows added; later refine full dossier.

Примітка якості: цей блок вирівнює картку з еталонним аналітичним стандартом, але не замінює повного поглибленого дослідження. Якщо evidence note або control file відсутні, це означає видиму прогалину, а не мовчазно розв'язану проблему.

## Five-source original-language apparatus v0.1

Цей блок фіксує пʼять джерельних каналів для реконструкції мовою оригіналу. Він не замінює аналіз, але робить видимим, що саме є рукописним свідком, що є перекладом, а що є реконструкційним або канонічним контролем.

### 1. P.Oxy. 1 Greek witness

- Status: no P.Oxy. 1 witness for this logion in the loaded corpus.

> [not preserved in P.Oxy. 1]

- Use: no direct support from this papyrus.

### 2. P.Oxy. 654 Greek witness

- Status: no P.Oxy. 654 witness for this logion; P.Oxy. 654 covers the prologue and Logia 1-7.

> [not preserved in P.Oxy. 654]

- Use: no direct support from this papyrus.

### 3. P.Oxy. 655 Greek witness

- Status: no P.Oxy. 655 witness for this logion in the loaded corpus.

> [not preserved in P.Oxy. 655]

- Use: no direct support from this papyrus.

### 4. Coptic NHC II translation channel

- Status: extant Coptic NHC II,2 witness; this is the complete preserved Coptic line used as the base witness.

> ⲡⲉϫⲉ ⲓ̅ⲥ̅ ϫⲉ ϩⲛ̅ⲙⲁⲕⲁⲣⲓⲟⲥ ⲛⲉ ⲛϩⲏⲕⲉ ϫⲉ ⲧⲱⲧⲛ̅ ⲧⲉ ⲧⲙⲛ̅ⲧⲉⲣⲟ ⲛⲙ̅ⲡⲏⲩⲉ`


Greek retroversion from Coptic/control layer:
> μακάριοι οἱ πτωχοί, ὅτι ὑμετέρα ἐστὶν ἡ βασιλεία τῶν οὐρανῶν.

- Use: primary preserved base for this logion; because it is a translation, it can support a Greek Vorlage only with explicit uncertainty.

### 5. Canonical Greek reconstruction/control channel

- Status: canonical-gospel control/reconstruction channel. This is not a Thomas manuscript witness; it is used to test shared tradition, dependence, and possible Greek wording.

Local Greek canonical/control text currently transcribed:
- Greek canonical text has not yet been transcribed into the local control files for this logion.
- Reconstruction note from current Greek layer: Coptic text plus Luke 6:20 and Matthew 5:3. The retroversion intentionally preserves Thomas's combination of direct "poor" with "kingdom of heaven." It is not an extant Greek witness.
- Use: supports or challenges reconstruction only when direction of dependence and redactional risk are discussed.

## Gold-level status check v0.2
Джерело актуального статусу: `corpus/tables/logia-workflow-matrix.md`. Цей блок є поточним синхронізаційним шаром і має пріоритет над старішими робочими позначками картки, якщо вони розходяться.

### Publication Status

- Current decision: `INCLUDE_WITH_MARKER`.
- Reader text: YES.
- Greek witness status: No loaded P.Oxy. witness.
- Current work status: Multilingual sync v0.1.
- Evidence note in matrix: YES.
- Clean-reader implication: Входить до clean Ukrainian reader як поточна реконструкційна одиниця; у чистому тексті друкувати без статусів і коментарів, а всі застереження переносити в apparatus / appendix.

### Evidence Links

Evidence note / dossier files:
- `reconstruction/earliest-sayings-gospel/notes/logion-054-evidence-en.md`

Synoptic/control files:
- `controls/synoptic-parallels/logion-054-blessed-poor-controls.md`

### Greek/Coptic Policy

- Coptic base: тримати коптський текст як основний збережений witness, доки немає сильнішого первинного контролю.
- Greek layer: Немає завантаженого грецького папірусного свідчення; будь-який грецький шар має бути реконструкційним або відсутнім.
- Якщо грецький текст не збережений, реконструювати його лише як імовірну ретроверсію й прямо маркувати ступінь гіпотетичності.

### Reader/Appendix Obligation

- Для clean reader: друкувати тільки реконструйоване ядро без коментарів, дужок і дисклеймерів.
- Для full appendix: подати походження, джерельний текст, паралелі, текстологічні ризики, можливі інтерпретації та причину включення або невключення.
- Для відкинутих / відкладених логій: пояснення має бути таким самим серйозним, як для включених логій; читач повинен бачити не лише результат, а й логіку відбору.

### Remaining Work

- Next action: English/Coptic/Greek retroversion/parallel rows added; later refine full dossier.
- Publication pass: звірити цю картку з фінальною all-114 decision table, clean-reader складом і повним читацьким додатком.