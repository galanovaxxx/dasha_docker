# Используем легковесный alpine базовый образ Python
FROM python:3.11-alpine

# Метаданные образа
LABEL maintainer="your-email@example.com"
LABEL description="Flask Expense Tracker Application"
LABEL version="1.0"

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем только requirements.txt сначала (для кэширования слоев)
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь код приложения
COPY . .

# Создаем директорию для templates если её нет
RUN mkdir -p templates

# Открываем порт 5000
EXPOSE 5000

# Healthcheck для проверки работоспособности приложения
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD wget --no-verbose --tries=1 --spider http://localhost:5000/ || exit 1

# Запускаем приложение (JSON формат)
CMD ["python", "app.py"]
