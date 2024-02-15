## О проекте:

Проект API_FINAL_YATUBE представляет собой REST API для взаимодействия с социальной сетью Yatube.

### Описание:

API_FINAL_YATUBE обеспечивает доступ к основной функциональности социальной сети Yatube через HTTP запросы. Он позволяет пользователям выполнять различные действия, такие как создание и редактирование постов, комментариев, подписок.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:AKhlebnov/api_final_yatube.git
```

```
api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Пример запроса:

GET /api/v1/posts/

Response samples
200

Content type
application/json

{
"count": 123,
"next": "http://api.example.org/accounts/?offset=400&limit=100",
"previous": "http://api.example.org/accounts/?offset=200&limit=100",
"results": [
{}
]
}

Полные маршруты API с примерами смотри GET /redoc/
