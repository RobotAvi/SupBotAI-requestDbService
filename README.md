# Requests API

RESTful микросервис для управления пользовательскими заявками с поддержкой CRUD операций. Реализован на FastAPI и упакован в Docker-контейнер.

---

## Описание

Данный сервис позволяет создавать, получать, обновлять и удалять заявки пользователей. Заявка содержит поля:

- `id` - уникальный идентификатор (генерируется автоматически)
- `course` - название курса (обязательное поле)
- `name` - имя пользователя (опционально)
- `email` - email пользователя (опционально)
- `phone` - телефон пользователя (опционально)

---

## Эндпоинты

| Метод | URL                  | Описание                        |
|-------|----------------------|--------------------------------|
| POST  | `/api/requests`      | Создать новую заявку            |
| GET   | `/api/requests`      | Получить список всех заявок     |
| GET   | `/api/requests/{id}` | Получить заявку по ID           |
| PUT   | `/api/requests/{id}` | Обновить заявку по ID           |
| DELETE| `/api/requests/{id}` | Удалить заявку по ID            |

---

## Запуск

### Требования

- Docker
- Docker Compose (опционально)

### Сборка и запуск контейнера

1. Клонируйте репозиторий:

```bash
git clone 
cd 
```

2. Соберите Docker-образ:

```bash
docker build -t requests-api .
```

3. Запустите контейнер:

```bash
docker run -d -p 8000:8000 --name requests-service requests-api
```

4. Проверьте доступность API:

```bash
curl http://localhost:8000/api/requests
```

---

## Пример использования API

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

### Обновление заявки

```bash
curl -X PUT http://localhost:8000/api/requests/1 \
-H "Content-Type: application/json" \
-d '{"name":"Петр Петров"}'
```

### Удаление заявки

```bash
curl -X DELETE http://localhost:8000/api/requests/1
```

---

## Технические детали

- Фреймворк: FastAPI
- Сервер: Uvicorn
- Валидация данных: Pydantic
- Хранилище: in-memory (словарь Python)
- Порт: 8000

---

## Возможные улучшения

- Подключение постоянного хранилища (например, PostgreSQL)
- Добавление аутентификации и авторизации
- Логирование и мониторинг
- Тесты и CI/CD

---

## Контакты

Если у вас есть вопросы или предложения, пожалуйста, создайте issue или свяжитесь со мной напрямую.

---

Спасибо за использование Requests API!

---
Answer from Perplexity: pplx.ai/share
