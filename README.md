# Requests API

RESTful микросервис для управления пользовательскими заявками с поддержкой всех CRUD операций. Реализован на FastAPI и упакован в Docker-контейнер.

---

## Описание

Сервис позволяет создавать, получать, обновлять и удалять заявки пользователей. Каждая заявка содержит следующие поля:

- `id` - уникальный идентификатор (генерируется автоматически)
- `course` - название курса (обязательное поле)
- `name` - имя пользователя (опционально)
- `email` - email пользователя (опционально)
- `phone` - телефон пользователя (опционально)

---

## Эндпоинты API

| Метод  | URL                   | Описание                      |
|--------|-----------------------|-------------------------------|
| POST   | `/api/requests`       | Создать новую заявку          |
| GET    | `/api/requests`       | Получить список всех заявок   |
| GET    | `/api/requests/{id}`  | Получить заявку по ID         |
| PUT    | `/api/requests/{id}`  | Обновить заявку по ID (полное обновление) |
| PATCH  | `/api/requests/{id}`  | Частичное обновление заявки   |
| DELETE | `/api/requests/{id}`  | Удалить заявку по ID          |

---

## Запуск

### Требования

- Docker (рекомендуется последняя версия)
- Docker Compose (опционально)

### Сборка и запуск контейнера

1. Клонируйте репозиторий:

```bash
git clone 
cd 
```

2. Соберите Docker-образ:

```bash
docker build -t requests-db .
```

3. Запустите контейнер:

```bash
docker run -d -p 8000:8000 --name requests-db-container requests-db
```

4. Проверьте доступность API:

```bash
curl http://localhost:8000/api/requests
```

---

## Примеры использования API

### Создание заявки

```bash
curl -X POST http://localhost:8000/api/requests \
-H "Content-Type: application/json" \
-d '{"course":"OAIS","name":"Иван Иванов","email":"ivan@mail.ru","phone":"+79991234567"}'
```

### Получение всех заявок

```bash
curl http://localhost:8000/api/requests
```

### Получение заявки по ID

```bash
curl http://localhost:8000/api/requests/1
```

### Полное обновление заявки (PUT)

```bash
curl -X PUT http://localhost:8000/api/requests/1 \
-H "Content-Type: application/json" \
-d '{"course":"OAIS","name":"Петр Петров"}'
```

### Частичное обновление заявки (PATCH)

```bash
curl -X PATCH http://localhost:8000/api/requests/1 \
-H "Content-Type: application/json" \
-d '{"name":"Пётр Петров"}'
```

### Удаление заявки

```bash
curl -X DELETE http://localhost:8000/api/requests/1
```

---

## Технические детали

- Фреймворк: FastAPI
- Сервер: Uvicorn
- Валидация данных: Pydantic (с учётом Pydantic v2)
- Хранилище: in-memory (словарь Python)
- Порт: 8000
- Тесты: реализованы с использованием pytest и FastAPI TestClient

---

## Возможные улучшения

- Подключение постоянного хранилища (PostgreSQL, MongoDB и др.)
- Реализация аутентификации и авторизации (JWT, OAuth2)
- Логирование и мониторинг
- Автоматизация тестирования и CI/CD

---

## Контакты

Если у вас есть вопросы или предложения, пожалуйста, создайте issue в репозитории или свяжитесь со мной напрямую.

---

Спасибо за использование Requests API!

