# Canonical Greek Extraction Audit v0.1

Статус: виконаний контрольний прохід, 2026-07-17.

## Мета

Цей прохід заповнює canonical Greek reconstruction/control channel у картках логій реальним грецьким текстом Матвія, Марка і Луки з локального SBLGNT cache.

Важлива межа: це не рукописний свідок Фоми. Це канонічний контроль для порівняння, реконструкції можливого грецького wording і перевірки напрямку залежності.

## Джерело

Локальний SBLGNT cache:

- `/tmp/euagelia-sblgnt/Matt.txt`
- `/tmp/euagelia-sblgnt/Mark.txt`
- `/tmp/euagelia-sblgnt/Luke.txt`

SBLGNT використано як відкритий робочий грецький контрольний текст. Перед публікаційним фіналом потрібна звірка з академічними виданнями.

## Підсумок

| Показник | Стан |
| --- | ---: |
| Карток логій | 114 |
| Карток із canonical Greek у пʼятиджерельному блоці | 81 |
| Карток, де canonical Greek лишається pending | 33 |
| Витягнутих canonical references | 198 |
| Карток із збереженим `Five-source original-language apparatus v0.1` | 114 |
| Карток із збереженим `Gold-level status check v0.2` | 114 |

## Метод

Було використано тільки явні посилання, уже наявні в картках:

- `Мт`, `Мк`, `Лк`;
- `Матвій`, `Марко`, `Лука`;
- `Matthew`, `Mark`, `Luke`;
- ranges на кшталт `Mark 12:13-17`.

Не додавалися нові паралелі “на здогад”. Якщо картка не мала явного канонічного reference, canonical channel лишився pending.

## Що тепер покращено

Для багатьох ключових логій у картці тепер видно повний пʼятиджерельний набір:

- чи є P.Oxy. witness;
- повний коптський текст;
- якщо грецький Thomas witness відсутній, чи є Greek retroversion;
- канонічні грецькі parallels прямо з SBLGNT.

Це особливо важливо для логій із сильним synoptic control, наприклад 20, 35, 45, 47, 54, 86, 96, 99, 100, 107.

## Обмеження

- SBLGNT використано як working open control text, не як фінальне критичне видання.
- Довші canonical ranges вставлено повністю, бо картка має показувати джерело прямо, а не тільки посилання.
- Не всі логії потребують canonical Greek control; частина pending status означає не дефект, а відсутність явної синоптичної паралелі в поточних картках.
- Для деяких pending логій можливо потрібен не синоптичний, а інший early Christian або Jewish control corpus.

## Наступна дія

Після canonical Greek extraction головним source-critical gap лишається pending P.Oxy. XML extraction:

- P.Oxy. 1: логії 27, 28, 29, 30, 77;
- P.Oxy. 655: логії 24, 37, 38.

Після цього можна якісніше переходити до true all-114 publication decision table.
