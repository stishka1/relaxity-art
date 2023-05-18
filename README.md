
![Alt-текст](https://raw.githubusercontent.com/stishka1/relaxity-art/master/generator/static/generator/images/generator.jpg?v=3&s=460)
# [Relaxity Art](https://relaxity-instruction.fr "Генератор картины из нитей по фото")
### :art: Проект генерирования картины из нитей по фото. В стиле stringart.:art:

В основе проекта - генератор картины из нитей по фото, написанный на языке Javascript. Веб-приложение написано на Python (фреймворк Django). В качестве библиотеки для создания pdf-инструкции выбрана известная fpdf (fpdf2). 

**Акцент** сделан на мобильную версию сайта (**mobile first**). Т.к. во Франции доля пользователей с мобильными устройствами выше всех остальных категорий. Сайт переведен на французский язык.

**В чем суть:**
![Alt-текст](https://raw.githubusercontent.com/stishka1/relaxity-art/master/generator/static/generator/images/photo_2023-03-14_17-54-29.jpg?v=3&s=460)

**Плетение картины по pdf-инструкции**

```
Поэтапно, шаг за шагом (всего 3700 шагов) плетется картинка специальными прочными нитями.
```

1. На главной странице покупатель вводит 8-ти значный код:
![Alt-текст](https://raw.githubusercontent.com/stishka1/relaxity-art/master/generator/static/generator/images/demo0.jpg?v=3&s=460)

2. Выбирает фото, из которого хочет сделать картину и нажимает на кнопку **Lancer** (запустить)
![Alt-текст](https://raw.githubusercontent.com/stishka1/relaxity-art/master/generator/static/generator/images/demo1.jpg?v=3&s=460)

3. По окончании генерации, появляется кнопка скачать мануал (**Telecharger manuel**):
![Alt-текст](https://raw.githubusercontent.com/stishka1/relaxity-art/master/generator/static/generator/images/demo2.jpg?v=3&s=460)

4. Кликнув по кнопке, открывается страница с pdf-инструкцией. Шаги разбиты по секторам (60 в каждом секторе т.е. 240 гвоздей /  60 = 4 сектора A, B, C, D):
![Alt-текст](https://raw.githubusercontent.com/stishka1/relaxity-art/master/generator/static/generator/images/demo3.jpg?v=3&s=460)

____
#### Более подробно про написание приложения можно почитать у меня в блоге: [pro-coders.ru](https://pro-coders.ru/blog/razbiraemsya-v-tonkostyah-biblioteki-fdpf/ "Разбираемся в тонкостях библиотеки fdpf")


![Alt-текст](http://pro-coders.ru/media/blog/images/fpdfban_sbbTaJt.jpg?v=3&s=460)