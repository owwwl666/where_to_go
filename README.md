# Описание
Проект представляет из себя демо-версию сайта-карты города Москва, на которой точками отмечены главные туристические места города, кликнув по которым, пользователь сможет посмотреть картинки этого места, а также изучить необходимую информацию о нем.

**Демо-версия сайта:** [https://owwwl.pythonanywhere.com/](https://owwwl.pythonanywhere.com/)

**Ссылка на административную панель сайта:** https://owwwl.pythonanywhere.com/admin/    (*логин:www | пароль:123*)

# Алгоритм тестирования

### Скачайте проект с GitHub
[Ссылка](https://github.com/owwwl666/where_to_go/archive/refs/heads/main.zip)


### Установка зависимостей
Используется python v3.10

Введите в терминале команду

```
pip install -r requirements.txt
```

### Переменные окружения
Создайте рядом с файлом `settings.py` файл `.env` и помстите в него следующие переменные окружения:

**SECRET_KEY** - Это большое случайное число, применяемое для защиты от CSRF. Важно, чтобы ключ, используемый в продакшене, не указывался в исходном коде, и/или не запрашивался с другого сервера. Django рекомендует размещать значение ключа либо в переменной окружения, или в файле с доступом только на чтение.

### Наполнение сайта локациями
Сайт принимает на вход JSON файл со всеми необходимыми данными о каждой из локаций, который выглядит следующим образом:

```
{
    "title": "Экскурсионный проект «Крыши24.рф»",
    "imgs": [
        "https://kudago.com/media/images/place/d0/f6/d0f665a80d1d8d110826ba797569df02.jpg",
        "https://kudago.com/media/images/place/66/23/6623e6c8e93727c9b0bb198972d9e9fa.jpg",
        "https://kudago.com/media/images/place/64/82/64827b20010de8430bfc4fb14e786c19.jpg",
    ],
    "description_short": "Хотите увидеть Москву с высоты птичьего полёта?",
    "description_long": "<p>Проект «Крыши24.рф» проводит экскурсии ...</p>",
    "coordinates": {
        "lat": 55.753676,
        "lng": 37.64
    }
}
```

Наполните сайт новыми локациями, выполнив команду:

```
python manage.py load_place http://адрес/файла.json
```

Данные с локацями можно получить [здесь](https://github.com/devmanorg/where-to-go-places/tree/master/places).

### Запуск сайта локально
```
python manage.py runserver
```

# Результат
![image](https://github.com/owwwl666/where_to_go/assets/131767856/ff428108-5063-4768-bf47-2fe8b6a8a3f3)


