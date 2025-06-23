# 🎣 Fish Explorer – A Django-Based Fish Information & Preparation Portal

![Fish Explorer Banner](https://raw.githubusercontent.com/yourusername/fish-explorer/main/static/images/banner-fish-explorer.png)

Welcome to **Fish Explorer**, a Django web app offering insights into fish species, fishing methods, fish pods, and preparation styles. Ideal for students, fisheries officers, chefs, and enthusiasts.

![Build](https://img.shields.io/badge/build-passing-brightgreen)
![Python](https://img.shields.io/badge/python-3.10+-blue)
![Django](https://img.shields.io/badge/django-4.2+-green)
![License](https://img.shields.io/badge/license-MIT-yellow)

---

## 📚 Table of Contents

- [✅ Features](#✅-features)
- [💻 Tech Stack](#💻-tech-stack)
- [📦 Models Overview](#📦-models-overview)
- [🛠️ Setup Instructions](#🛠️-setup-instructions)
- [🌐 App Views / Routing](#🌐-app-views--routing)
- [🚀 Deployment on Render](#🚀-deployment-on-render)
- [📸 Screenshots](#📸-screenshots)
- [📄 License](#📄-license)

---

## ✅ Features

- 🐠 Paginated fish species listings
- 🔬 Detailed fish info (biology, habitat, health, etc.)
- 🧩 View fish pods (groupings)
- 🎣 Fishing techniques (traditional & modern)
- 🍽️ Cooking/preparation styles
- 📸 Image support (upload or URL)
- 📱 Responsive UI using Bootstrap + AOS

---

## 💻 Tech Stack

| Component        | Version     |
|------------------|-------------|
| Python           | 3.10+       |
| Django           | 4.2+        |
| Bootstrap        | 5.x         |
| AOS Animation    | 2.3.4       |
| SQLite           | Built-in    |
| Gunicorn         | For deployment |
| Whitenoise       | For static files |

---

## 📦 Models Overview

```python
class Fish(models.Model):
    species_name = models.CharField(max_length=255)
    scientific_name = models.CharField(max_length=255, null=True, blank=True)
    category = models.CharField(max_length=255, null=True, blank=True)
    habitat = models.TextField(null=True, blank=True)
    location = models.TextField(null=True, blank=True)
    biology = models.TextField(null=True, blank=True)
    population = models.TextField(null=True, blank=True)
    fishing_rate = models.TextField(null=True, blank=True)
    health_benefits = models.TextField(null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)
    image_file = models.ImageField(upload_to='fish_images/', null=True, blank=True)
    management = models.TextField(null=True, blank=True)
    availability = models.TextField(null=True, blank=True)
    nutrition = models.TextField(null=True, blank=True)
    texture = models.CharField(max_length=255, null=True, blank=True)
    taste = models.CharField(max_length=255, null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)
```

---

## 🛠️ Setup Instructions

### 📥 Clone the Repository

```bash
git clone https://github.com/yourusername/fish-explorer.git
cd fish-explorer
```

### 🐍 Create Virtual Environment

```bash
python -m venv env
source env/bin/activate         # For Linux/macOS
env\Scripts\activate          # For Windows
```

### 📦 Install Requirements

```bash
pip install -r requirements.txt
```

If not yet created:

```bash
pip install django
pip freeze > requirements.txt
```

### 🔧 Create `.env` File

```env
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

### ⚙️ Migrate and Create Superuser

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### 🚀 Run Development Server

```bash
python manage.py runserver
```

Visit: http://127.0.0.1:8000

---

## 🌐 App Views / Routing

| Path                  | Description                         |
|-----------------------|-------------------------------------|
| `/`                   | Home                                |
| `/fish/`              | List of all fish                    |
| `/fish/<id>/`         | Fish detail view                    |
| `/pods/`              | List of fish pods                   |
| `/techniques/`        | Fishing methods                     |
| `/preparations/`      | Fish preparation/cooking styles     |
| `/admin/`             | Django Admin                        |

---

## 🚀 Deployment on Render

### 1. Required Files

**`requirements.txt`**:

```
Django>=4.2
gunicorn
whitenoise
python-decouple
```

**`build.sh`**:

```bash
#!/bin/bash
python manage.py migrate
python manage.py collectstatic --noinput
```

Make it executable:

```bash
chmod +x build.sh
```

**`render.yaml`**:

```yaml
services:
  - type: web
    name: fish-explorer
    env: python
    buildCommand: "./build.sh"
    startCommand: "gunicorn fish_explorer.wsgi:application"
    envVars:
      - key: DJANGO_SETTINGS_MODULE
        value: fish_explorer.settings
```

### 2. Push to GitHub

```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/abner/fish-explorer.git
git push -u origin master
```

---

## 📸 Screenshots

### 🏠 Home Page
![Home](https://raw.githubusercontent.com/yourusername/fish-explorer/main/static/images/screenshot-home.png)

### 🐟 Fish List View
![List](https://raw.githubusercontent.com/yourusername/fish-explorer/main/static/images/screenshot-list.png)

### 📘 Fish Detail
![Detail](https://raw.githubusercontent.com/yourusername/fish-explorer/main/static/images/screenshot-detail.png)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

> 💬 For contributions, open an issue or submit a PR. Happy fishing!

---

## 🐳 Docker Support

### 1. Create `Dockerfile`

```dockerfile
# Dockerfile
FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "fish_explorer.wsgi:application", "--bind", "0.0.0.0:8000"]
```

### 2. Create `docker-compose.yml`

```yaml
version: "3.9"

services:
  web:
    build: .
    command: gunicorn fish_explorer.wsgi:application --bind 0.0.0.0:8000
    ports:
      - "8000:8000"
    volumes:
      - .:/app
    env_file:
      - .env
```

### 3. Run Docker Container

```bash
docker-compose up --build
```

Visit: [http://localhost:8000](http://localhost:8000)

---

## 📂 Sample Data Fixture

To load sample fish data:

```bash
python manage.py loaddata sample_fish_data.json
```

Create a sample fixture:

```bash
python manage.py dumpdata fish_app.Fish --indent 4 > sample_fish_data.json
```

---

## 🌐 Live Demo

🚀 [**Live Demo on Render**](https://fish-explorer.onrender.com)  
_(Replace with actual link if deployed)_

