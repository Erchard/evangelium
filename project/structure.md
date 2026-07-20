# Структура Репозиторію

Статус: оновлено після спрощення структури.

## Принцип

Матеріали розкладено не за історією роботи, а за функцією:

- книга;
- джерела;
- дослідження;
- збірка;
- готові артефакти;
- архів.

## Активні Папки

| Папка | Для чого |
| --- | --- |
| `book/` | Редаговані тексти книги: прологи, основний текст, додатки, мовні шари, бібліографія. |
| `sources/` | Першоджерела, snapshots, коптські й грецькі матеріали. |
| `research/` | Картки логій, рішення, evidence notes, методологія, control files і аудити. |
| `build/` | Скрипти збірки, перевірок і генерації. |
| `dist/` | Згенеровані Markdown/PDF/HTML/TSV артефакти. |
| `project/` | Актуальна специфікація, дорожня карта, структура, карта репозиторію й поточне завдання. |
| `archive/` | Історичні промпти, проміжні звіти, старі аудити й proof-чернетки. |

## Головні Файли Для Редагування

| Потреба | Файл |
| --- | --- |
| Український пролог | `book/front-matter/prologue-uk.md` |
| Англійський пролог | `book/front-matter/prologue-en.md` |
| Український clean reader | `book/text/logia-uk.md` |
| Англійський clean reader | `book/text/logia-en.md` |
| Український 114-логійний додаток | `book/appendix/commentary-uk.md` |
| Англійський 114-логійний додаток | `book/appendix/commentary-en.md` |
| Коптський шар | `book/translations/coptic.md` |
| Грецький шар | `book/translations/greek.md` |
| Parallel edition | `book/translations/parallel-edition.md` |
| Бібліографія | `book/bibliography/bibliography-working.md` |

## Дослідницький Апарат

| Потреба | Файл або папка |
| --- | --- |
| Картки 114 логій | `research/logion-cards/` |
| Таблиці корпусу | `research/tables/` |
| Рішення включення | `research/decisions/` |
| Evidence dossier і notes | `research/evidence/` |
| Методологія | `research/methodology/` |
| Synoptic/control files | `research/controls/primary/` |
| Історія рішень і аудитів | `research/audits/` |

## Збірка

```powershell
python build/scripts/qa_crosscheck.py
python build/scripts/assemble_full_book_sources.py
```

`dist/` не редагується вручну. Якщо треба змінити книжку, редагується джерело в `book/`, після чого запускається збірка.
