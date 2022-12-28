# Password check

Проверка прочности пароля, на мотив 
"[kaspersky password checker](https://password.kaspersky.com/)

## Установка
```bash
pip install virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```

## Что внутри
[urwid](https://gist.github.com/dvmn-tasks/1519bd2c8f775cb7c38f5fb02d9cb6fb) - библиотека, для перехвата вводимых символов, используется для маскировки ввода.

[logging](https://gist.github.com/dvmn-tasks/1519bd2c8f775cb7c38f5fb02d9cb6fb) - встроенная бибилиотека логирования

## Пример работы
![example](example.gif)
