# Quick Start Guide

## Installation & Running

### Step 1: Setup Virtual Environment
```bash
cd d05
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 2: Install Django
```bash
pip install -r requirements.txt
```

### Step 3: Initialize Database
```bash
python manage.py migrate
```

### Step 4: Collect Static Files
```bash
python manage.py collectstatic --noinput
```

### Step 5: Run Server
```bash
python manage.py runserver
```

### Step 6: Access the Application
Open your browser and visit:
- **Ex00:** http://127.0.0.1:8000/ex00/
- **Ex01:** http://127.0.0.1:8000/ex01/django/
- **Ex02:** http://127.0.0.1:8000/ex02/
- **Ex03:** http://127.0.0.1:8000/ex03/

## What Each Exercise Does

### Ex00 - Markdown Cheatsheet
A complete reference guide for Markdown syntax. Visit `/ex00/` to see all Markdown formatting options.

### Ex01 - Django Pages
Three informational pages about Django:
- `/ex01/django/` - Introduction to Django (blue text)
- `/ex01/display/` - How Django displays pages (blue text)
- `/ex01/templates/` - Template engine guide (red text)

Uses template inheritance with a base template and navigation bar.

### Ex02 - Form with History
An interactive form where you can submit text. Every submission:
- Is saved to a log file with timestamp
- Appears in the history on the page
- Persists even after server restart

Visit `/ex02/` to try it out.

### Ex03 - Color Gradients
A beautiful table showing 50 shades of 4 colors:
- Noir (black)
- Rouge (red)
- Bleu (blue)
- Vert (green)

All colors are generated dynamically by Python code, not hardcoded in HTML.

Visit `/ex03/` to see the gradients.

## Troubleshooting

**Problem:** Static files (CSS) not loading  
**Solution:** Run `python manage.py collectstatic`

**Problem:** Port already in use  
**Solution:** Run `python manage.py runserver 8080` to use a different port

**Problem:** Module not found  
**Solution:** Make sure you activated the virtual environment and ran `pip install -r requirements.txt`

## File Structure

```
d05/
├── manage.py           # Django management script
├── requirements.txt    # Python dependencies
├── d05/               # Project configuration
├── ex00/              # Exercise 00 app
├── ex01/              # Exercise 01 app
├── ex02/              # Exercise 02 app
└── ex03/              # Exercise 03 app
```

Each exercise is a separate Django application with its own:
- `views.py` - Logic and data processing
- `urls.py` - URL routing
- `templates/` - HTML templates
- Other files as needed (forms, templatetags, static files)

## Key Features Implemented

✅ Proper Django project structure  
✅ URL routing with and without trailing slashes  
✅ Template inheritance (DRY principle)  
✅ Django Forms for user input  
✅ Persistent file storage  
✅ Dynamic content generation  
✅ Static files management  
✅ Custom template filters  
✅ Navigation between pages  

Enjoy exploring the Django project!
