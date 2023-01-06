### Web-приложение для определения заполненных форм

Данные (заполненные формы) подаются на /get_form или /get_form/
Формат данных:
* POST-запрос: 'application/x-www-form-urlencoded'
* GET-запрос (отладка в браузере): querystring формата
> /get_form/?email=a@gmail.com&text=abc&phone=%2B7%20000%20000%2000%2000&date=12.02.2000

Ответ:
* имя шаблона формы, если шаблон совпал с формой
* dict {'поле-формы': тип поля} по введенной форме, если она не совпала ни с одним шаблоном

Форматы полей формы:
* date: DD.MM.YYYY или YYYY-MM-DD
* phone: +7 000 000 00 00
* email: abcd@domain.code
* text не имеет установленного формата


Шаблоны хранятся в TinyDB, выводятся на странице с URL "/"

Приложение – Flask app (фреймворк Flask), для тестирования используется pytest и requests;
все используемые модули указаны в requirements.txt, установка:

> env/bin/python -m pip install -r requirements.txt

Запуск:
> $ python main.py

Тестирование (Terminal):
> $ pytest
