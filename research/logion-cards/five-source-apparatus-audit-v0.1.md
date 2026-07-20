# Five-Source Apparatus Audit v0.1

Статус: виконаний контрольний прохід, 2026-07-17.

## Мета

Цей аудит фіксує новий шар карток: у кожній картці логії тепер мають бути видимі не тільки рішення й посилання, а й самі джерельні тексти або чесна позначка їхньої відсутності.

Пʼять каналів:

1. `P.Oxy. 1`;
2. `P.Oxy. 654`;
3. `P.Oxy. 655`;
4. коптський NHC II як перекладовий канал;
5. канонічний грецький reconstruction/control channel.

## Що зроблено

| Показник | Стан |
| --- | ---: |
| Карток логій | 114 |
| Карток із `Five-source original-language apparatus v0.1` | 114 |
| Карток із збереженим `Gold-level status check v0.2` | 114 |
| Карток із прямим коптським текстом у новому блоці | 114 |
| Карток із локально виписаним канонічним грецьким текстом | 81 |
| Карток, де canonical Greek ще лишається pending | 33 |
| P.Oxy. 1 card-level Greek extracts pending from XML | 0 after `poxy-xml-extraction-audit-v0.1.md` |
| P.Oxy. 655 card-level Greek extracts pending from XML | 0 after `poxy-xml-extraction-audit-v0.1.md` |

## Методологічне рішення

У кожній картці тепер прямо видно:

- чи зберігся текст у кожному з трьох оксіринхських папірусів;
- чи є тільки XML-покриття без готового card-level витягу;
- повний коптський текст логії;
- чи є грецька ретроверсія з коптського/control layer;
- чи є вже локально виписаний канонічний грецький контроль.

Відсутність свідка не приховується. Для логій без P.Oxy.-свідка картка пише `[not preserved in P.Oxy. X]`. Для логій із покриттям в XML, але без готового витягу, картка пише, що line extraction pending.

## Головна виявлена прогалина

Найбільша прогалина після первинного five-source проходу була canonical Greek control layer.

Після `canonical-greek-extraction-audit-v0.1.md` ситуацію суттєво покращено: 81 картка має canonical Greek прямо в пʼятиджерельному блоці, 33 лишаються pending.

## Наступна дія

Card-level pending extraction для P.Oxy. 1 / P.Oxy. 655 закрито в `corpus/cards/poxy-xml-extraction-audit-v0.1.md`.

Наступна source-critical дія: звірити ці витяги з академічними виданнями й перенести оновлений Greek status у true all-114 publication decision table.
