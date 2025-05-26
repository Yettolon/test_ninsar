# Тестовое NINSAT

## Запуск проекта с Docker

1. Склонируйте репозиторий:

```bash
git clone https://github.com/Yettolon/test_ninsar.git
cd test_ninsar
```

2. Постройте и запустите контейнеры Docker:
```bash
docker-compose up --build
```

3. Приложение запустится и будет доступно по адресу::
```bash
http://127.0.0.1:8000/
```

4. Наполнение базы данных
Нужно в контейнере запустить скрипт, который наполнит базу 10000 тестовыми записями
```
python manage.py populate_results
```


5. Получение токена пользователя
```
curl -X POST http://127.0.0.1:8000/api-token-auth/ \
-H "Content-Type: application/json" \
-d '{"username":"admin", "password":"admin"}'
```

6. Отправка запроса
```
curl -X POST "http://127.0.0.1:8000/api/results/results/get-competition-result/?limit=12" \  
-H "Content-Type: application/json" \                               
-H "Authorization: Token <token>" \
-d '{"competition": "SpringCup", "user_name": "Ivan", "scenario": "easy"}'
```

## Примечания

1. При запуске контейнера создается суперюзер с данными admin:admin

2. Есть скрипт для наполнения тестовыми данными

3. В url добавил get параметр limit для фильтрации для поля other_results
