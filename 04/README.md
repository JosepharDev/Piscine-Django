<div align="center">

# ⚙️ Day 04 — Django Views & Templates

### Django apps, URL routing, template inheritance, static files & forms.

[![Day](https://img.shields.io/badge/Day-04-6366f1?style=for-the-badge)]()
[![Topics](https://img.shields.io/badge/Topics-Django%20%7C%20Views%20%7C%20Templates%20%7C%20Static-0ea5e9?style=for-the-badge)]()

</div>

---

## 📖 About

Day 04 is the first **full Django project** day. You build a multi-app Django project (`d05`) where each exercise is a standalone Django app with its own views, URL configuration, and templates. The day covers the MVT (Model-View-Template) pattern, static file serving, template inheritance, and Django Forms.

---

## 🚀 Quick Start

```bash
pip install -r requirements.txt
python manage.py runserver
```

| App | URL |
|-----|-----|
| ex00 — Markdown cheatsheet | `http://127.0.0.1:8000/ex00/` |
| ex01 — Multi-page nav | `http://127.0.0.1:8000/ex01/` |
| ex02 — Form + history | `http://127.0.0.1:8000/ex02/` |
| ex03 — Color shades | `http://127.0.0.1:8000/ex03/` |

---

## 📁 Exercises

### ex00 — Markdown Cheatsheet
A single-page Django view that displays a Markdown syntax cheatsheet.

**Route:** `/ex00/`

- `views.index()` renders `index.html`
- Demonstrates the simplest possible Django view — no model, no form
- Template is a static HTML cheatsheet page

---

### ex01 — Multi-Page Navigation with Static CSS
A multi-page Django app with a persistent navigation bar and two different CSS stylesheets.

**Routes:** `/ex01/`, `/ex01/display/`, `/ex01/django/`, `/ex01/templates/`

- **Template inheritance**: all pages extend `base.html`, include `nav.html`
- **Two static stylesheets** (`style1.css`, `style2.css`) served via `{% static %}`
- Demonstrates Django's static file system (`STATICFILES_DIRS`, `{% load static %}`)

---

### ex02 — Text Input Form with Log History
A Django form that accepts text input, timestamps it, appends it to a log file, and displays the full history below the form.

**Route:** `/ex02/`

```
[Form] → POST → append to logs.txt → re-render with full history
```

Features:
- `TextInputForm` using `django.forms.Form`
- Log file path configured via `settings.EX02_LOG_FILE`
- History parsed from `[YYYY-MM-DD HH:MM:SS] text` format
- Handles GET (display form + history) and POST (save + redirect)

---

### ex03 — Color Shades Table
A dynamic Django view that generates a color gradient table for four colors in French: **noir**, **rouge**, **bleu**, **vert**.

**Route:** `/ex03/`

```python
generate_shades('rouge', 0, 255, 50)
# → ['#000000', '#050000', ..., '#ff0000']
```

- 50 shades per color, computed server-side
- Rendered as an HTML `<table>` via Django template
- Each cell is styled with `background-color: {{ hex }}`

---

## 🗂️ Structure

```
04/
├── d05/                     # Django project config
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py / asgi.py
├── ex00/
│   ├── views.py             # index view
│   ├── urls.py
│   └── templates/index.html
├── ex01/
│   ├── views.py             # multi-page views
│   ├── urls.py
│   ├── static/css/style1.css
│   ├── static/css/style2.css
│   └── templates/           # base, nav, display, django, templates
├── ex02/
│   ├── views.py             # form + log handler
│   ├── forms.py             # TextInputForm
│   ├── urls.py
│   └── templates/indexx.html
├── ex03/
│   ├── views.py             # color shade generator
│   ├── urls.py
│   └── templates/index_03.html
├── manage.py
└── requirements.txt
```

---

## 💡 Key Concepts

| Concept | Covered in |
|---------|------------|
| Django MVT pattern | All |
| `urls.py` routing | All |
| `render()` with context | ex02, ex03 |
| Template inheritance (`{% extends %}`) | ex01 |
| `{% include %}` for partials | ex01 |
| Static files (`{% static %}`) | ex01 |
| Django Forms & validation | ex02 |
| POST handling & redirects | ex02 |
| Dynamic data rendering in templates | ex03 |
