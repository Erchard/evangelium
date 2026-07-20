# EUAGELIA

EUAGELIA - книжковий і дослідницький проєкт реконструкції найдавнішого досяжного шару висловів Ісуса, збереженого передусім у традиції Євангелія від Фоми.

## Головний принцип

Проєкт тепер розділено за функцією:

- `book/` - редаговані тексти книги.
- `sources/` - першоджерела, snapshots, коптські й грецькі матеріали.
- `research/` - картки логій, рішення, докази, методологія, аудити.
- `build/` - скрипти збірки й перевірок.
- `dist/` - згенеровані книжкові та цифрові артефакти.
- `project/` - тільки актуальна карта, специфікація, дорожня карта й поточне завдання.
- `archive/` - стара історія роботи, промпти, аудити й тимчасові proof-матеріали.

## Де редагувати

- Український пролог: `book/front-matter/prologue-uk.md`
- Англійський пролог: `book/front-matter/prologue-en.md`
- Український текст логій: `book/text/logia-uk.md`
- Англійський текст логій: `book/text/logia-en.md`
- Український додаток: `book/appendix/commentary-uk.md`
- Англійський додаток: `book/appendix/commentary-en.md`
- Коптський шар: `book/translations/coptic.md`
- Грецький шар: `book/translations/greek.md`
- Бібліографія: `book/bibliography/bibliography-working.md`

## Як зібрати

```powershell
python build/scripts/qa_crosscheck.py
python build/scripts/assemble_full_book_sources.py
```

Готові Markdown-джерела й proof-артефакти лежать у `dist/`.

## Правило

Редагувати руками треба `book/`, `sources/`, `research/` і актуальні файли в `project/`.

`dist/` не редагується руками: це результат генерації.

Детальна карта для роботи: `PROJECT_GUIDE.md`.
