<div align="center">

# 📦 Day 03 — External Libraries & APIs

### pip, virtual environments, geohashing, Wikipedia API, web scraping & first Django app.

[![Day](https://img.shields.io/badge/Day-03-6366f1?style=for-the-badge)]()
[![Topics](https://img.shields.io/badge/Topics-pip%20%7C%20APIs%20%7C%20Scraping%20%7C%20Django-0ea5e9?style=for-the-badge)]()

</div>

---

## 📖 About

Day 03 opens the door to the Python ecosystem. You learn to manage **virtual environments**, install third-party packages with `pip`, consume **REST APIs**, scrape web pages, and — most importantly — write your very **first Django application**.

---

## 📁 Exercises

### ex00 — Geohashing (`geohashing.py`)
Computes a geohash coordinate from a latitude, longitude, date, and Dow Jones opening value using the `antigravity` module.

```bash
python3 geohashing.py <latitude> <longitude> <date> <dow_jones>
# Example: python3 geohashing.py 37.421542 -122.085589 2005-05-26 10458.68
```

- Uses the XKCD geohashing algorithm (RFC MD5 hash)
- Validates coordinate ranges (±90 lat, ±180 lon)

---

### ex01 — Local Library Usage (`my_program.py`)
Demonstrates how to use a **locally installed library** (`path.py`) without installing it globally.

```bash
./my_script.sh   # sets up local lib and runs my_program.py
```

- Adds `./local_lib` to `sys.path`
- Uses `Path` objects to create directories and write files

---

### ex02 — Wikipedia API Scraper (`request_wikipedia.py`)
Fetches a Wikipedia article by search term, parses the wikitext, and saves it to a `.wiki` file.

```bash
pip install -r requirement.txt
python3 request_wikipedia.py "Python programming"
# → Python_programming.wiki
```

- Queries the Wikipedia Search API to resolve the correct title
- Fetches raw wikitext via the MediaWiki API
- Uses `dewiki` to clean markup into readable text

---

### ex03 — Roads to Philosophy (`roads_to_philosophy.py`)
Follows the **first link** in each Wikipedia article's body text, walking the chain until it reaches **"Philosophy"** (or detects a loop / dead end).

```bash
pip install -r requirement.txt
python3 roads_to_philosophy.py "Python"
```

Implements the famous Wikipedia → Philosophy phenomenon. Uses:
- `requests.Session` for persistent HTTP connections
- `BeautifulSoup4` for HTML parsing
- Loop detection via a visited pages dictionary
- Proper namespace exclusions (`Wikipedia:`, `File:`, `Help:`, etc.)

---

### ex04 — pip & venv Automation (`my_script.sh`)
A shell script that automates the creation of a Python virtual environment and installs all required packages.

```bash
./my_script.sh
```

---

### ex05 — First Django App (`helloworld/`)
The very first Django project — a minimal "Hello, World!" web application.

```bash
pip install -r requirement.txt
python manage.py runserver
# → http://127.0.0.1:8000/
```

Structure:
- `Django/` — project configuration (settings, URLs, WSGI/ASGI)
- `helloworld/` — app with a single view that returns "Hello, World!"
- SQLite database

---

## 🗂️ Structure

```
03/
├── ex00/
│   └── geohashing.py          # XKCD geohash calculator
├── ex01/
│   ├── my_program.py          # Local library demo
│   └── my_script.sh           # Setup script
├── ex02/
│   ├── request_wikipedia.py   # Wikipedia article downloader
│   └── requirement.txt        # requests, dewiki
├── ex03/
│   ├── roads_to_philosophy.py # Wikipedia link walker
│   └── requirement.txt        # requests, beautifulsoup4
├── ex04/
│   ├── my_script.sh           # venv + pip automator
│   └── requirement.txt
└── ex05/                      # First Django project
    ├── Django/                # Project config
    ├── helloworld/            # App
    ├── manage.py
    └── requirement.txt
```

---

## 💡 Key Concepts

| Concept | Covered in |
|---------|------------|
| `sys.path` manipulation | ex01 |
| REST API consumption | ex02 |
| JSON parsing | ex02 |
| HTML scraping with BeautifulSoup | ex03 |
| Loop / cycle detection | ex03 |
| Virtual environments | ex04 |
| Django project structure | ex05 |
| Django views & URL routing | ex05 |

---

## 🔧 Dependencies

| Package | Used in |
|---------|---------|
| `antigravity` | ex00 |
| `requests` | ex02, ex03 |
| `dewiki` | ex02 |
| `beautifulsoup4` | ex03 |
| `django` | ex05 |
