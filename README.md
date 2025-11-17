# 💰 Flask Expense Tracker

Веб-приложение для учета личных расходов с категориями и статистикой.

## 🚀 Быстрый старт

### Запуск через Docker (рекомендуется)

```bash
docker pull yourusername/expense-tracker:latest
docker run -d -p 5000:5000 --name expense-tracker yourusername/expense-tracker:latest
```

Откройте браузер: `http://localhost:5000`

### Запуск с bind mount (для разработки)

```bash
docker run -d -p 5000:5000 \
  -v $(pwd):/app \
  --name expense-tracker-dev \
  yourusername/expense-tracker:latest
```

При изменении кода приложение автоматически перезагрузится.

## 📋 Возможности

- 💰 Учет расходов по категориям
- 📊 Статистика и аналитика
- 📅 Отслеживание трат по датам
- 🎨 Современный UI
- 📱 Адаптивный дизайн

## 🛠️ Сборка образа локально

```bash
# Клонировать репозиторий
git clone https://github.com/yourusername/flask-expense-tracker.git
cd flask-expense-tracker

# Собрать образ
docker build -t expense-tracker:v1.0 .

# Запустить контейнер
docker run -d -p 5000:5000 expense-tracker:v1.0
```

## 🔧 Переменные окружения

| Переменная | Описание | По умолчанию |
|-----------|----------|--------------|
| `FLASK_ENV` | Режим работы | `production` |
| `PORT` | Порт приложения | `5000` |

## 📊 Healthcheck

Образ включает healthcheck:
- Интервал: 30 секунд
- Таймаут: 5 секунд
- Ретраи: 3

```bash
# Проверить статус
docker inspect --format='{{.State.Health.Status}}' expense-tracker
```

## 🐳 Доступные теги

- `latest` - последняя стабильная версия
- `v1.0` - версия 1.0
- `alpine` - легковесная версия

## 📝 API Endpoints

- `GET /` - Главная страница
- `GET /api/expenses` - Получить все расходы
- `POST /api/expenses` - Добавить расход
- `DELETE /api/expenses/<id>` - Удалить расход
- `GET /api/stats` - Получить статистику
- `GET /api/categories` - Получить категории

## 🔍 Пример использования API

```bash
# Добавить расход
curl -X POST http://localhost:5000/api/expenses \
  -H "Content-Type: application/json" \
  -d '{"amount": 1500, "category": "Продукты", "description": "Покупка в магазине"}'

# Получить все расходы
curl http://localhost:5000/api/expenses

# Получить статистику
curl http://localhost:5000/api/stats
```

## 🎯 Технологии

- Python 3.11 Alpine
- Flask 3.0.0
- Flask-CORS
- HTML5/CSS3/JavaScript

## 📦 Размер образа

- Полный образ: ~50MB
- Alpine образ: ~45MB

## 👨‍💻 Разработка

```bash
# Запуск с live reload
docker run -d -p 5000:5000 \
  -v $(pwd):/app \
  -e FLASK_ENV=development \
  expense-tracker:latest

# Просмотр логов
docker logs -f expense-tracker

# Остановка
docker stop expense-tracker

# Удаление
docker rm expense-tracker
```

## 📄 Лицензия

MIT License

## 🤝 Автор

Ваше имя - Лабораторная работа по Docker

## 🔗 Ссылки

- [GitHub Repository](https://github.com/yourusername/flask-expense-tracker)
- [Docker Hub](https://hub.docker.com/r/yourusername/expense-tracker)
