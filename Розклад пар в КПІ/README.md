# Веб-додаток розкладу пар КПІ 🎓

![Python](https://img.shields.io/badge/python-3.8+-blue)
![Django](https://img.shields.io/badge/django-4.x-green)

Веб-додаток для перегляду академічного розкладу Національного технічного університету України "КПІ".

## 📋 Вимоги
- Python 3.8+
- Django 4.x
- Браузер з підтримкою JavaScript

## 🛠️ Встановлення

```bash
# 1. Клонуйте репозиторій
git clone https://github.com/Ivan65933/iasc-marathon.git
cd iasc-marathon/Розклад пар у КПІ

# 2. Створіть та активуйте віртуальне середовище
python -m venv venv
# Linux/macOS:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# 3. Встановіть залежності
pip install -r requirements.txt

# 4. Запустіть сервер
python manage.py migrate
python manage.py runserver

# 5. Відкрийте у браузері: 

http://localhost:8000/
```

## Структура проекту
Розклад пар у КПІ/
├── core/          # Основні налаштування Django
├── schedule/      # Додаток з розкладом
├── static/        # CSS, JavaScript
└── templates/     # HTML шаблони

## ⚙️ Корисні команди 

```bash
# Збір статичних файлів для продакшену
python manage.py collectstatic

# Створення суперкористувача
python manage.py createsuperuser
```

## Розробник: Іван65933