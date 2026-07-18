# Структура репозиторію

Статус: актуалізовано 2026-07-18 після technical-debt closure pass.

## Навігаційний принцип

Структура більше не прив'язана до первісної числової схеми. Папки названі за реальною функцією матеріалу, щоб було зрозуміло, куди йти за текстом, джерелами, картками, доказами або робочими планами.

## Активні папки

| Папка | Для чого |
| --- | --- |
| `project/` | Мета, специфікація, дорожня карта, аудит прогалин, робочі промпти Codex. |
| `reconstruction/` | Усі тексти реконструкції: clean reader, apparatus, мовні шари, parallel edition, evidence dossier, full appendix. |
| `corpus/` | 114 карток логій, еталони якості, workflow matrix і таблиці корпусу. |
| `sources/` | Локально збережені першоджерела, snapshots, коптські й грецькі матеріали, source register. |
| `controls/` | Synoptic/control files, кластерні порівняння, паралелі й контрольні аргументи. |
| `research/` | Методологія, історія досліджень, датування, історичні гіпотези. |
| `bibliography/` | Місце для фінальної бібліографії, rights/citation notes і списків літератури. |
| `output/` | Місце для майбутніх експортів: українська паперова книга, англійська паперова книга, digital scholarly companion, статті й публічні редакції. |
| `tools/` | Локальні QA/consistency scripts для перевірки структури, нумерації, reader sync і appendix anchors. |
| `archive/` | Неактивні матеріали, які треба зберегти, але не використовувати як робочий центр. |

## Де шукати головне

| Потреба | Файл або папка |
| --- | --- |
| Чистий український текст | `reconstruction/earliest-sayings-gospel/reconstructed-gospel-uk.md` |
| Український apparatus до clean reader | `reconstruction/earliest-sayings-gospel/reconstructed-gospel-uk-apparatus.md` |
| Повний український додаток до 114 логій | `reconstruction/earliest-sayings-gospel/full-logion-commentary-appendix-uk.md` |
| Англійський текст реконструкції | `reconstruction/earliest-sayings-gospel/reconstructed-gospel-en.md` |
| Коптський шар | `reconstruction/earliest-sayings-gospel/reconstructed-gospel-coptic.md` |
| Грецький шар | `reconstruction/earliest-sayings-gospel/reconstructed-gospel-greek.md` |
| Англомовний доказовий dossier | `reconstruction/earliest-sayings-gospel/evidence-dossier-en.md` |
| Таблиця включення/невключення | `reconstruction/earliest-sayings-gospel/inclusion-decisions-table.md` |
| Картки всіх логій | `corpus/cards/` |
| Операційна матриця 114 логій | `corpus/tables/logia-workflow-matrix.md` |
| Першоджерела | `sources/primary_texts/` |
| Synoptic/control матеріали | `controls/synoptic-parallels/` |
| Structural QA / crosscheck | `tools/qa_crosscheck.py` |
| Головна дорожня карта | `project/project-completion-roadmap.md` |
| Специфікація кінцевого продукту | `project/final-product-specification.md` |
| Print/digital publication architecture | `project/print-and-digital-publication-architecture.md` |
| Головний промпт проєкту | `project/ide-codex-master-project-prompt.md` |

## Поточний стан після реорганізації

- Clean Ukrainian reader містить 37 логій або ядра.
- Мовні шари синхронізовані для 37 одиниць.
- Корпус має 114 карток логій.
- Full 114-logion appendix має 114/114 секцій із читацьким поясненням; Logia 1-114 уже редакційно консолідовані як print-safe книжковий додаток.
- Усі 37 clean-reader одиниці мають точний `Чистий текст реконструкції` anchor у full appendix.
- Structural QA baseline проходить через `python3 tools/qa_crosscheck.py`.
- Print/digital publication architecture v0.1 зафіксована: українська й англійська паперові книги мають бути самодостатніми, а повний evidence apparatus лишається digital scholarly companion.
- Наступний робочий пакет: print / digital render proof preparation.

## Правило для майбутньої роботи

Нові матеріали слід класти за функцією:

- новий промпт або план - у `project/`;
- новий текст реконструкції або коментар - у `reconstruction/earliest-sayings-gospel/`;
- майбутній print/digital export - у `output/print/uk/`, `output/print/en/` або `output/digital/scholarly/`;
- нову картку логії - у `corpus/cards/`;
- нове першоджерело або snapshot - у `sources/primary_texts/`;
- новий контроль паралелей - у `controls/synoptic-parallels/`;
- нове методологічне або історичне дослідження - у `research/`.
- новий QA/consistency script - у `tools/`.
