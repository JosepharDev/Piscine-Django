<div align="center">

# 🗄️ Day 05 — Django ORM & PostgreSQL

### Raw SQL, Django models, migrations, and full CRUD operations on a movie database.

[![Day](https://img.shields.io/badge/Day-05-6366f1?style=for-the-badge)]()
[![Topics](https://img.shields.io/badge/Topics-Django%20ORM%20%7C%20PostgreSQL%20%7C%20CRUD%20%7C%20Migrations-0ea5e9?style=for-the-badge)]()
[![DB](https://img.shields.io/badge/Database-PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white)]()

</div>

---

## 📖 About

Day 05 is the **database day**. Starting with raw `psycopg2` SQL and progressively migrating to the Django ORM, the exercises build a complete Star Wars movie database with full Create, Read, Update, and Delete capabilities.

---

## 🗃️ Database Setup

```bash
# Create the PostgreSQL database and user
psql -U postgres -c "CREATE USER djangouser WITH PASSWORD 'secret';"
psql -U postgres -c "CREATE DATABASE djangotraining OWNER djangouser;"

# Install dependencies and run migrations
pip install -r requierment.txt
python manage.py migrate
python manage.py runserver
```

---

## 🎬 Data Model — `Movies`

All exercises revolve around this core model:

| Field | Type | Constraints |
|-------|------|-------------|
| `episode_nb` | IntegerField | Primary key |
| `title` | CharField(64) | Unique, not null |
| `opening_crawl` | TextField | Nullable |
| `director` | CharField(32) | Not null |
| `producer` | CharField(128) | Not null |
| `release_date` | DateField | Not null |

---

## 📁 Exercises

### ex00 — Raw psycopg2 Table Creation
Creates the `ex00_movies` table using a raw `psycopg2` connection — no ORM.

**Route:** `/ex00/init`

```sql
CREATE TABLE IF NOT EXISTS ex00_movies (
    title VARCHAR(64) UNIQUE NOT NULL,
    episode_nb SERIAL PRIMARY KEY,
    ...
);
```

Demonstrates direct PostgreSQL connection management (connect → cursor → execute → commit → close).

---

### ex01 — Django ORM Model
Defines the `Movies` model using Django's ORM. Running `makemigrations` and `migrate` creates the table automatically.

**Route:** `/ex01/`

- `models.py` defines `Movies` with proper field types
- Uses `IntegerField(primary_key=True)` for `episode_nb`
- `__str__` returns the title

---

### ex02 — ORM Data Display
Fetches all movies from the database and renders them in an HTML table.

**Route:** `/ex02/`

```python
movies = Movies.objects.all()
```

---

### ex03 — Many-to-Many Relationships
Extends the model with character relationships using `ManyToManyField`.

**Route:** `/ex03/`

---

### ex04 — ORM CRUD — Create & Read
A full CRUD interface: a form to insert new movies, and a table displaying all existing records.

**Route:** `/ex04/`

- Django ModelForm or Form for data entry
- `Movies.objects.create(...)` for inserts
- Renders the full list after each insertion

---

### ex05 — Delete Interface
Adds the ability to **delete** movies from the database via a dedicated UI.

**Route:** `/ex05/`

- Lists all movies with a delete button next to each
- Handles POST with movie ID → `Movies.objects.filter(pk=id).delete()`
- Renders updated list after deletion

---

### ex06 — Update / Crawl
Enables **updating** existing movie records (opening crawl text).

**Route:** `/ex06/`

- Pre-fills form with current values from the database
- Handles POST → `Movies.objects.filter(pk=id).update(...)`

---

### ex07 — Advanced ORM Queries
Exercises more complex ORM query operations (filtering, ordering, annotation).

**Route:** `/ex07/`

---

### ex08 — Complex Display
Renders a rich display combining multiple querysets and template logic.

**Route:** `/ex08/`

---

### ex09 — Final Data Pipeline
The final exercise — a complete data ingestion and display pipeline.

**Route:** `/ex09/`

---

## 🗂️ Structure

```
05/
├── ex00/ → ex09/       # One Django app per exercise
│   ├── models.py       # ORM models (ex01+)
│   ├── views.py        # View logic
│   ├── urls.py         # URL routing
│   ├── forms.py        # Forms (ex05+)
│   ├── admin.py
│   └── templates/      # HTML templates
├── manage.py
└── requierment.txt
```

---

## 💡 Key Concepts

| Concept | Covered in |
|---------|------------|
| Raw SQL with `psycopg2` | ex00 |
| Django `models.Model` | ex01+ |
| `makemigrations` / `migrate` | ex01+ |
| `objects.all()`, `filter()`, `get()` | ex02+ |
| `objects.create()` | ex04 |
| `objects.delete()` | ex05 |
| `objects.update()` | ex06 |
| `ManyToManyField` | ex03 |
| Django Admin | All (admin.py) |
