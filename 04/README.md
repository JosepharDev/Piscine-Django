# Django Base Project - d05

This is a Django project implementing four exercises as per the training requirements.

## Project Structure

```
d05/
├── manage.py
├── requirements.txt
├── d05/                 # Main project configuration
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── ex00/                # Exercise 00: Markdown Cheatsheet
│   ├── templates/
│   │   └── index.html
│   ├── __init__.py
│   ├── apps.py
│   ├── views.py
│   └── urls.py
├── ex01/                # Exercise 01: Multiple pages with templates
│   ├── templates/
│   │   ├── base.html
│   │   ├── nav.html
│   │   ├── django.html
│   │   ├── display.html
│   │   └── templates.html
│   ├── static/
│   │   └── css/
│   │       ├── style1.css
│   │       └── style2.css
│   ├── __init__.py
│   ├── apps.py
│   ├── views.py
│   └── urls.py
├── ex02/                # Exercise 02: Form with history
│   ├── templates/
│   │   └── index.html
│   ├── __init__.py
│   ├── apps.py
│   ├── forms.py
│   ├── views.py
│   └── urls.py
└── ex03/                # Exercise 03: Color shades table
    ├── templates/
    │   └── index.html
    ├── templatetags/
    │   ├── __init__.py
    │   └── ex03_extras.py
    ├── __init__.py
    ├── apps.py
    ├── views.py
    └── urls.py
```

## Setup Instructions

### 1. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Migrations

```bash
python manage.py migrate
```

### 4. Collect Static Files (for ex01)

```bash
python manage.py collectstatic --noinput
```

### 5. Run Development Server

```bash
python manage.py runserver
```

The server will start at `http://127.0.0.1:8000/`

## Exercise Descriptions

### Exercise 00: Markdown Cheatsheet
- **URL:** `/ex00/` or `/ex00`
- **Description:** A comprehensive static page displaying all Markdown syntax
- **Features:** 
  - Complete Markdown syntax reference
  - Examples and usage
  - Clean, readable layout

### Exercise 01: Django Pages with Template Inheritance
- **URLs:**
  - `/ex01/django/` - Django introduction and history
  - `/ex01/display/` - Display process of static pages
  - `/ex01/templates/` - Template engine documentation
- **Features:**
  - Template inheritance using `base.html`
  - Navigation bar included via `nav.html`
  - Two CSS styles: `style1.css` (blue) for most pages, `style2.css` (red) for templates page
  - DRY principle implementation
  - Proper use of blocks: title, style, and content

### Exercise 02: Form with History
- **URL:** `/ex02/` or `/ex02`
- **Description:** Interactive form with persistent history
- **Features:**
  - Text input form using Django Forms
  - Persistent logging to file
  - Display of submission history with timestamps
  - Log file path configured in `settings.py`
  - Data persists across server restarts

### Exercise 03: Color Shades Table
- **URL:** `/ex03/` or `/ex03`
- **Description:** Dynamic color gradient table
- **Features:**
  - 4 columns × 51 rows table (including header)
  - Colors: noir (black), rouge (red), bleu (blue), vert (green)
  - 50 shades generated dynamically in views
  - Each cell: 80px width × 40px height
  - No hardcoded colors in templates
  - Only 4 `<td></td>` and 4 `<th></th>` tag pairs in template

## Rules Compliance

### General Rules
✅ All paths defined in respective `urls.py` files  
✅ Forms defined in `forms.py` (ex02)  
✅ Proper HTML structure (DOCTYPE, html, head, body)  
✅ URLs work with and without trailing slash  
✅ Only requested URLs return pages (others return 404)

### Exercise-Specific Rules
✅ **Ex00:** Static Markdown cheatsheet page  
✅ **Ex01:** Template inheritance with base.html, nav.html, and CSS files  
✅ **Ex02:** Django Form class used, no hardcoded form fields, persistent logging  
✅ **Ex03:** Dynamic color generation, minimal template tags, no hardcoded colors

## Testing the Application

### Test Ex00
Visit `http://127.0.0.1:8000/ex00/` to see the Markdown cheatsheet.

### Test Ex01
1. Visit each page to verify navigation and styling
2. Verify blue text on Django and Display pages
3. Verify red text on Templates page
4. Check template inheritance and DRY implementation

### Test Ex02
1. Submit text in the form
2. Verify it appears in history with timestamp
3. Restart the server
4. Verify history persists
5. Check `ex02/logs.txt` file

### Test Ex03
1. View the color gradient table
2. Verify 4 columns and 50 color rows
3. Verify smooth gradients from dark to light
4. Inspect page source to confirm minimal template tags

## Configuration

### Settings (d05/settings.py)
- `SECRET_KEY`: Django secret key (change in production)
- `DEBUG`: Set to `False` in production
- `ALLOWED_HOSTS`: Configure for production deployment
- `EX02_LOG_FILE`: Path to ex02 log file

### Static Files
Static files are served from the `staticfiles` directory after running `collectstatic`.

## Development Notes

- The project uses Django's default SQLite database
- Static files must be collected before serving in production
- Log files are created automatically in the ex02 directory
- All apps are properly registered in `INSTALLED_APPS`

## Troubleshooting

### Static files not loading
Run: `python manage.py collectstatic`

### Form not submitting
Ensure CSRF middleware is enabled in settings

### 404 errors
Check URL patterns in urls.py files

### History not persisting
Verify `EX02_LOG_FILE` path in settings.py

## License

This project is created for educational purposes as part of Django training.
