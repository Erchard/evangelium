# Card Quality Audit v0.2

Статус: виконаний контрольний аудит, 2026-07-17.

## Висновок

Найкраща еталонна картка проєкту зараз:

- `corpus/cards/logion-002.md` - формальний gold standard;
- `corpus/cards/logion-006.md` - найкращий практичний приклад для складених логій, де треба розділяти коротке можливе ядро й повну композицію.

Після цього проходу всі 114 карток логій отримали однаковий синхронізаційний блок:

- `## Gold-level status check v0.2`

Цей блок не стверджує, що кожна логія вже має однаково глибоке дослідження. Він фіксує, що кожна картка тепер має однаковий поточний контрольний мінімум: рішення, reader status, Greek status, evidence/control links, clean-reader implication, appendix obligation і next action.

## Перевірені кількісні показники

| Показник | Стан |
| --- | ---: |
| Карток логій | 114 |
| Карток із `Gold-level status check v0.2` | 114 |
| Поточних clean-reader одиниць | 34 |
| Evidence notes у workflow matrix | 55 |
| Карток без окремого evidence note у матриці | 59 |

## Чому це важливо

До цього проходу в багатьох картках могли співіснувати старі верхні статуси, v0.1-вирівнювання і новіші рішення з матриці. Це створювало ризик, що майбутній редактор випадково візьме за актуальну стару позначку.

Тепер кожна картка має поточний v0.2-блок, який прямо каже, що він є синхронізаційним шаром і має пріоритет над старішими робочими позначками, якщо вони розходяться.

## Що саме додано до кожної картки

Кожна картка отримала:

- current decision з `corpus/tables/logia-workflow-matrix.md`;
- reader text status;
- Greek witness status;
- current work status;
- evidence note status;
- посилання на наявні evidence notes;
- посилання на наявні synoptic/control files;
- політику для коптського й грецького шарів;
- наслідок для clean reader;
- обов'язок для full 114-logion appendix;
- next action перед publication pass.

## Межа цього проходу

Це був quality-normalization pass, а не повний академічний rewrite усіх карток.

Він не:

- створював нові evidence notes для 59 логій без окремого note;
- промотував нові логії до clean reader;
- фіналізував all-114 publication decision table;
- завершував full commentary appendix;
- перевіряв усі ретроверсії проти академічних видань.

## Поточний головний висновок

Найслабше місце проєкту після цього проходу вже не базова якість карток. Базова карткова навігація стала контрольованою.

Найслабше місце тепер: публікаційна глибина для всіх 114 рішень, особливо для `UNCERTAIN`, `DEFER`, `KEEP_APPENDIX_ONLY_FOR_NOW` і `EXCLUDE_AS_SECONDARY` матеріалу.

## Рекомендований наступний крок

Створити справжню all-114 publication decision table, де для кожної логії або підодиниці буде:

- decision;
- reader status;
- confidence;
- main reason;
- evidence note / no-note rationale;
- Greek status;
- appendix status;
- publication next action.
