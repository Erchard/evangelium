# Greek Oxyrhynchus Folder

Статус: робочий Unicode/TEI-корпус зібрано для трьох головних грецьких фрагментів.

У цій папці лежать відкриті робочі матеріали для грецьких фрагментів Євангелія від Фоми: P.Oxy. 1, P.Oxy. 654 і P.Oxy. 655.

## Що вже є

- `gnosis-thomas-poxy-snapshot.html` - сторінка Gnosis Archive з описом Oxyrhynchus fragments і англійськими реконструкціями/паралелями.
- `agraphos-poxy1-snapshot.html` - сторінка Agraphos для P.Oxy. 1.
- `agraphos-poxy654-snapshot.html` - сторінка Agraphos для P.Oxy. 654.
- `agraphos-poxy655-snapshot.html` - сторінка Agraphos для P.Oxy. 655.
- `agraphos_poxy1_images/` - GIF-зображення грецького тексту P.Oxy. 1.
- `agraphos_poxy654_images/` - GIF-зображення грецького тексту P.Oxy. 654.
- `agraphos_poxy655_images/` - GIF-зображення грецького тексту P.Oxy. 655.
- `dclp-poxy1-62838.xml` - DCLP / Papyri.info TEI/EpiDoc XML для P.Oxy. 1, логії 26-30, 77b, 31-33.
- `dclp-poxy654-62840.xml` - DCLP / Papyri.info TEI/EpiDoc XML для P.Oxy. 654, пролог і логії 1-7.
- `dclp-poxy655-62839.xml` - DCLP / Papyri.info TEI/EpiDoc XML для P.Oxy. 655, логії 24(?), 36-39.
- `gospels-net-poxy5575-snapshot.html` - відкритий контрольний snapshot для P.Oxy. 5575, важливий для матеріалу, близького до Thomas 27, але не прямий TEI-свідок тексту Євангелія від Фоми.

## Обмеження

- DCLP XML є відкритим TEI/EpiDoc корпусом під CC BY 3.0; його можна використовувати як робочу Unicode-основу з атрибуцією.
- Agraphos подає грецький текст переважно як зображення, не як чистий Unicode-грецький текст.
- Gnosis Archive подає зручні англійські реконструкції, але не замінює грецький критичний текст.
- Прямий доступ до Papyri.info через браузер був заблокований перевіркою, але raw XML доступний через GitHub `papyri/idp.data`.
- Перед фінальним цитуванням у реконструкції бажано звірити DCLP з Grenfell & Hunt, Fitzmyer, Attridge / Layton.
- P.Oxy. 5575 слід використовувати як контроль для циркуляції Thomas-like матеріалу в змішаному sayings-середовищі, а не як заміну P.Oxy. 1 чи Coptic Thomas.

## Наступна дія

Почати з P.Oxy. 654, бо він покриває пролог і логії 1-7: витягнути з `dclp-poxy654-62840.xml` читабельну таблицю рядків із лакунами й апаратом.
