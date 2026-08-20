<div align="center">

# 🌊 Piscine Django

### A 7-day deep dive into web development with Python & Django

[![Language](https://img.shields.io/badge/Language-Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Framework](https://img.shields.io/badge/Framework-Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://djangoproject.com)
[![School](https://img.shields.io/badge/School-42-000000?style=for-the-badge)](https://42.fr)

</div>

---

## 📖 Overview

The **Piscine Django** is a 42 school intensive training that builds web development skills from the ground up — starting with raw HTML & shell scripting and climbing all the way to full Django authentication systems with PostgreSQL.

Each day (numbered `00` → `06`) is a self-contained module with focused exercises that progressively introduce new concepts.

---

## 🗺️ Learning Journey

```
Day 00 → HTML & Shell basics
Day 01 → Python fundamentals
Day 02 → Python OOP & templating
Day 03 → External libraries & APIs
Day 04 → Django views & templates
Day 05 → Django ORM & PostgreSQL
Day 06 → Django authentication
```

---

## 📅 Days at a Glance

| Day | Theme | Key Topics |
|-----|-------|------------|
| [**00**](./00/) | Web Foundations | Shell scripting, HTML, forms, CSS, JavaScript |
| [**01**](./01/) | Python Basics | Variables, types, data structures, file I/O, HTML generation |
| [**02**](./02/) | Python OOP | Template rendering, inheritance, metaclasses, HTML builder |
| [**03**](./03/) | Libraries & APIs | `pip`, virtual envs, geohashing, Wikipedia API, web scraping |
| [**04**](./04/) | Django Intro | Django apps, views, templates, static files, forms |
| [**05**](./05/) | Django ORM | PostgreSQL, raw SQL, Django models, CRUD operations |
| [**06**](./06/) | Auth & Sessions | Registration, login, logout, session management |

---

## 🏗️ Repository Structure

```
Piscine-Django/
├── 00/          # Day 00 — Web Foundations (HTML, CSS, JS, Shell)
│   ├── ex00/    # curl URL follower script
│   ├── ex01/    # Static HTML CV
│   ├── ex02/    # HTML contact form
│   ├── ex03/    # Styled page clone
│   ├── ex04/    # JavaScript snippets
│   └── ex05/    # Full landing page
│
├── 01/          # Day 01 — Python Basics
│   ├── ex00/    # Python type display
│   ├── ex01/    # File reading
│   ├── ex02/    # List → dict conversion
│   ├── ex03/    # State → capital lookup
│   ├── ex04/    # Capital → state reverse lookup
│   ├── ex05/    # Bidirectional state/capital search
│   ├── ex06/    # Dictionary sorting by birth year
│   └── ex07/    # Periodic table HTML generator
│
├── 02/          # Day 02 — Python OOP & Templating
│   ├── ex00/    # Django-style template renderer
│   ├── ex01/    # The Intern (None printer)
│   ├── ex02/    # HotBeverage class hierarchy
│   ├── ex03/    # Coffee machine with metaclass
│   ├── ex04/    # HTML Elem builder with validation
│   ├── ex05/    # Extended HTML elements
│   └── ex06/    # Full HTML Page generator
│
├── 03/          # Day 03 — External Libraries & APIs
│   ├── ex00/    # Geohashing (antigravity)
│   ├── ex01/    # path.py local library usage
│   ├── ex02/    # Wikipedia API scraper
│   ├── ex03/    # Roads to Philosophy (link walker)
│   ├── ex04/    # pip + venv automation script
│   └── ex05/    # First Django "Hello World" app
│
├── 04/          # Day 04 — Django Views & Templates
│   ├── ex00/    # Markdown cheatsheet view
│   ├── ex01/    # Multi-page nav with static CSS
│   ├── ex02/    # Form with persistent log history
│   └── ex03/    # Color shades table generator
│
├── 05/          # Day 05 — Django ORM & PostgreSQL
│   ├── ex00/    # Raw psycopg2 table creation
│   ├── ex01/    # Django ORM Movies model
│   ├── ex02/    # ORM data display
│   ├── ex03/    # Many-to-many relationships
│   ├── ex04/    # ORM CRUD operations
│   ├── ex05/    # Delete interface
│   ├── ex06/    # Update / crawl operations
│   ├── ex07/    # Advanced ORM queries
│   ├── ex08/    # Complex display views
│   └── ex09/    # Final data pipeline
│
└── 06/          # Day 06 — Authentication & Sessions
    └── ex/      # Register, login, logout, session username
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| **Python 3** | Core language |
| **Django** | Web framework (Days 03–06) |
| **PostgreSQL** | Database (Day 05) |
| **psycopg2** | PostgreSQL driver |
| **requests** | HTTP client (Day 03) |
| **BeautifulSoup4** | HTML scraping (Day 03) |
| **dewiki** | Wikipedia wikitext parser |

---

## 🚀 Quick Start

### Days 00–03 (Pure Python / scripts)
```bash
# No setup needed — run files directly
python3 01/ex00/var.py
python3 02/ex04/elem.py
```

### Days 04–06 (Django apps)
```bash
cd 04/   # or 05/ or 06/
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Day 05 (PostgreSQL setup required)
```bash
psql -U postgres -c "CREATE USER djangouser WITH PASSWORD 'secret';"
psql -U postgres -c "CREATE DATABASE djangotraining OWNER djangouser;"
```

---

<div align="center">

Built during the **42 school** Django Piscine

</div>