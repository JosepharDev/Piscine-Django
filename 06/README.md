<div align="center">

# 🔐 Day 06 — Authentication & Sessions

### User registration, login, logout, and session-based username assignment.

[![Day](https://img.shields.io/badge/Day-06-6366f1?style=for-the-badge)]()
[![Topics](https://img.shields.io/badge/Topics-Auth%20%7C%20Sessions%20%7C%20Login%20%7C%20Register-0ea5e9?style=for-the-badge)]()
[![DB](https://img.shields.io/badge/Database-SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)]()

</div>

---

## 📖 About

Day 06 introduces **Django's built-in authentication system** and **session management**. The project (`d06`) features a single app (`ex`) that implements the full auth lifecycle: account registration, login, protected home page, logout, and a live session-based username that refreshes periodically.

---

## 🚀 Quick Start

```bash
pip install django
python manage.py migrate
python manage.py runserver
```

| Page | URL | Access |
|------|-----|--------|
| Home | `http://127.0.0.1:8000/` | 🔒 Login required |
| Login | `http://127.0.0.1:8000/login/` | Public |
| Register | `http://127.0.0.1:8000/register/` | Public |
| Logout | `http://127.0.0.1:8000/logout/` | Authenticated |
| Username (JSON) | `http://127.0.0.1:8000/get_name/` | Authenticated |

---

## 🔄 Authentication Flow

```
/register/ ──(POST valid form)──► auto-login ──► /home/
/login/    ──(POST credentials)──► auth OK  ──► /home/
/home/     ──(not logged in)  ──► redirect ──► /login/
/logout/   ──────────────────────────────────► /login/
```

---

## 📁 Features

### 🏠 Home (`/`)
- **Login required** — redirects to `/login/` if not authenticated
- Displays a **session-based username** drawn randomly from a configured list
- Username refreshes every `NAME_VALIDITY_SECONDS` (configurable in `settings.py`)
- Username is fetched live via `/get_name/` (returns JSON)

### 🔑 Login (`/login/`)
- `LoginForm` with `username` and `password` fields
- Calls `django.contrib.auth.authenticate()` and `login()`
- Displays error message on invalid credentials

### 📝 Register (`/register/`)
- `RegisterForm` extends `UserCreationForm` logic
- `user.set_password()` for secure password hashing
- Auto-logs in the user after successful registration

### 🚪 Logout (`/logout/`)
- Calls `django.contrib.auth.logout()`
- Redirects to `/login/`

### 👤 Session Username (`/get_name/`)
- Returns a JSON `{ "username": "..." }`
- Used by the frontend to poll for username updates
- Picks randomly from `settings.USERNAME` list
- Stores name and timestamp in the session; rotates after expiry

---

## 🗂️ Structure

```
06/
├── d06/                        # Django project config
│   ├── settings.py             # Auth settings, USERNAME list, NAME_VALIDITY_SECONDS
│   ├── urls.py
│   └── wsgi.py / asgi.py
├── ex/                         # Authentication app
│   ├── models.py               # (Uses Django's built-in User model)
│   ├── forms.py                # LoginForm, RegisterForm
│   ├── views.py                # index, login_view, register, logout_view, get_name
│   ├── urls.py
│   └── templates/
│       ├── base.html           # Base layout
│       ├── nav.html            # Navigation bar
│       ├── login.html          # Login page
│       └── register.html       # Registration page
├── manage.py
└── db.sqlite3
```

---

## ⚙️ Configuration (`settings.py`)

| Setting | Purpose |
|---------|---------|
| `AUTH_USER_MODEL` | Uses Django's default `auth.User` |
| `USERNAME` | List of random names for session assignment |
| `NAME_VALIDITY_SECONDS` | How long a session username lasts |
| `SESSION_ENGINE` | Django's default DB-backed sessions |

---

## 💡 Key Concepts

| Concept | Implementation |
|---------|---------------|
| `django.contrib.auth` | `authenticate()`, `login()`, `logout()` |
| `request.user.is_authenticated` | Home page guard |
| Session read/write | `request.session['username']` |
| Session expiry & rotation | Timestamp comparison in `get_or_create_username()` |
| Password hashing | `user.set_password()` |
| Django Forms | `LoginForm`, `RegisterForm` |
| JSON responses | `JsonResponse({'username': ...})` |
| Template inheritance | `{% extends "base.html" %}` |
