# Django Base Project - Implementation Summary

## Project Overview
This project implements a complete Django web application with four exercises, fully compliant with the training requirements.

## Exercises Implemented

### Exercise 00: Markdown Cheatsheet ✅
**URL:** `/ex00/`

**Implementation:**
- Single static page displaying comprehensive Markdown syntax
- Includes all major Markdown elements: headers, emphasis, lists, links, images, code blocks, tables, etc.
- Clean, professional styling
- Properly formatted HTML structure

**Files:**
- `ex00/views.py` - View function
- `ex00/urls.py` - URL routing
- `ex00/templates/index.html` - Cheatsheet template

---

### Exercise 01: Multiple Pages with Template Inheritance ✅
**URLs:**
- `/ex01/django/` - Django introduction (blue text)
- `/ex01/display/` - Static page display process (blue text)
- `/ex01/templates/` - Template engine documentation (red text)

**Implementation:**
- **Template Inheritance:** All pages extend `base.html`
- **Navigation:** `nav.html` included in all pages
- **Styling:** Two CSS files (`style1.css` and `style2.css`)
  - `style1.css` (blue) used on django and display pages
  - `style2.css` (red) used on templates page
  - Style block override in templates.html
- **DRY Principle:** No code repetition, proper use of blocks

**Key Features:**
- Title block for page-specific titles
- Style block for CSS file selection
- Content block for page content
- Each CSS file used only once in templates

**Files:**
- `ex01/views.py` - Three view functions
- `ex01/urls.py` - URL routing for all three pages
- `ex01/templates/base.html` - Base template with blocks
- `ex01/templates/nav.html` - Navigation bar
- `ex01/templates/django.html` - Django intro page
- `ex01/templates/display.html` - Display process page
- `ex01/templates/templates.html` - Template engine page
- `ex01/static/css/style1.css` - Blue styling
- `ex01/static/css/style2.css` - Red styling

---

### Exercise 02: Form with History ✅
**URL:** `/ex02/`

**Implementation:**
- Django Form class (not hardcoded HTML form)
- Text input field with submit button
- Persistent logging to file with timestamps
- History display on page
- Log file path defined in `settings.py` as `EX02_LOG_FILE`
- Data survives server restarts

**How it Works:**
1. User submits text via form
2. Timestamp is generated
3. Entry saved to `ex02/logs.txt`
4. History reloaded from file and displayed
5. Form resets for new input

**Files:**
- `ex02/views.py` - Form handling and history logic
- `ex02/urls.py` - URL routing
- `ex02/forms.py` - Django Form class definition
- `ex02/templates/index.html` - Form and history template
- `ex02/logs.txt` - Created automatically when first entry is submitted

---

### Exercise 03: Fifty Shades of Bic ✅
**URL:** `/ex03/`

**Implementation:**
- 4 columns × 51 rows table (1 header + 50 color rows)
- Columns: noir (black), rouge (red), bleu (blue), vert (green)
- 50 shades per color generated dynamically in Python
- Cell dimensions: 80px × 40px
- **No hardcoded colors in template**
- Only 4 `<td>` and 4 `<th>` tag pairs in template

**Color Generation:**
- Black: Grayscale from #000000 to #FFFFFF
- Red: Red channel from #000000 to #FF0000
- Blue: Blue channel from #000000 to #0000FF
- Green: Green channel from #000000 to #00FF00

**Technical Implementation:**
- View generates all 50 shades for each color
- Data structured as rows (each row has 4 colors)
- Custom template filter for dictionary access
- Template loops through rows and columns

**Files:**
- `ex03/views.py` - Color generation logic
- `ex03/urls.py` - URL routing
- `ex03/templates/index.html` - Table template
- `ex03/templatetags/ex03_extras.py` - Custom filter
- `ex03/templatetags/__init__.py` - Package marker

---

## Rules Compliance Checklist

### General Rules ✅
- [x] Virtual environment setup supported
- [x] All dependencies in `requirements.txt`
- [x] Development server via `manage.py`
- [x] URLs work with and without trailing slash
- [x] Only requested URLs return pages (404 for others)
- [x] Properly formatted HTML (DOCTYPE, html, head, body)

### Specific Rules ✅
- [x] All paths in respective `urls.py` files
- [x] Forms in `forms.py` (ex02)
- [x] Special character handling
- [x] No strange display issues

### Ex00 Rules ✅
- [x] Static Markdown cheatsheet
- [x] Accessible at `/ex00/`
- [x] Title: "Ex00: Markdown Cheatsheet"
- [x] Template named `index.html`

### Ex01 Rules ✅
- [x] Three pages with proper titles and URLs
- [x] Base template (`base.html`) with content, style, and title blocks
- [x] Navigation template (`nav.html`) included in all pages
- [x] Two CSS files: `style1.css` (blue) and `style2.css` (red)
- [x] `style1.css` used on django and display pages
- [x] `style2.css` used on templates page
- [x] Each stylesheet used only once
- [x] DRY principle respected
- [x] Template inheritance implemented

### Ex02 Rules ✅
- [x] Form using `django.forms.Form` class
- [x] No hardcoded form fields
- [x] History starts empty
- [x] Entries logged to file with timestamp
- [x] Log file path in `settings.py`
- [x] History displayed on page
- [x] Data persists across server restarts

### Ex03 Rules ✅
- [x] 4 columns × 51 lines (header + 50 shades)
- [x] Accessible at `/ex03/`
- [x] Colors: noir, rouge, bleu, vert
- [x] Cell size: 80px × 40px
- [x] 50 different shades per color
- [x] No hardcoded colors in template
- [x] Colors generated in view
- [x] Only 4 `<td></td>` pairs in template
- [x] Only 4 `<th></th>` pairs in template
- [x] Proper table formatting

---

## Technical Architecture

### Project Structure
```
d05/
├── manage.py                    # Django CLI
├── requirements.txt             # Dependencies
├── d05/                        # Main project
│   ├── settings.py             # Configuration
│   ├── urls.py                 # Root URL routing
│   ├── wsgi.py/asgi.py        # WSGI/ASGI config
├── ex00/                       # Exercise 00 app
├── ex01/                       # Exercise 01 app
├── ex02/                       # Exercise 02 app
└── ex03/                       # Exercise 03 app
```

### Django Features Used
- URL routing with path()
- Template inheritance and blocks
- Template includes
- Static files management
- Forms framework
- File I/O for persistence
- Custom template filters
- Template tags (for, if, extends, include, block, load)

### Design Patterns
- **DRY (Don't Repeat Yourself):** Template inheritance, no code duplication
- **Separation of Concerns:** Views handle logic, templates handle presentation
- **MVC Pattern:** Models (not needed for static sites), Views, Templates
- **Modular Architecture:** Each exercise as separate app

---

## Setup Instructions

1. **Create virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Initialize database:**
   ```bash
   python manage.py migrate
   ```

4. **Collect static files:**
   ```bash
   python manage.py collectstatic --noinput
   ```

5. **Run server:**
   ```bash
   python manage.py runserver
   ```

6. **Access exercises:**
   - Ex00: http://127.0.0.1:8000/ex00/
   - Ex01: http://127.0.0.1:8000/ex01/django/
   - Ex02: http://127.0.0.1:8000/ex02/
   - Ex03: http://127.0.0.1:8000/ex03/

---

## Testing Recommendations

### Ex00 Testing
- Visit `/ex00/` and verify complete Markdown reference
- Check HTML structure in browser inspector
- Verify proper formatting and readability

### Ex01 Testing
- Visit all three pages
- Verify navigation links work
- Confirm blue text on django and display pages
- Confirm red text on templates page
- Check browser inspector for CSS file usage
- Verify template inheritance and DRY implementation

### Ex02 Testing
1. Submit several text entries
2. Verify each appears in history with timestamp
3. Check `ex02/logs.txt` exists and contains entries
4. Restart server with `Ctrl+C` then `python manage.py runserver`
5. Verify history is still present after restart

### Ex03 Testing
1. Visit `/ex03/`
2. Count rows (should be 51: 1 header + 50 shades)
3. Count columns (should be 4)
4. Verify gradients go from dark to light
5. Inspect page source to verify minimal template tags
6. Verify no hardcoded color values in template

---

## Additional Notes

### Static Files
- CSS files in `ex01/static/css/`
- Collected to `staticfiles/` directory
- Served by Django development server

### Logging
- Ex02 logs stored in `ex02/logs.txt`
- Format: `[YYYY-MM-DD HH:MM:SS] text`
- File created automatically on first submission

### Template Filters
- Custom filter `get_item` in `ex03/templatetags/ex03_extras.py`
- Allows dictionary access in templates
- Registered with `@register.filter` decorator

### URL Patterns
- All URLs support trailing slash or no trailing slash
- Achieved by defining both patterns in `urls.py`
- Root project `urls.py` includes app URLs

---

## Potential Enhancements (Beyond Requirements)

While the current implementation fully meets all requirements, possible enhancements could include:

- Admin interface for ex02 history management
- AJAX form submission in ex02
- Interactive color picker in ex03
- Breadcrumb navigation
- Responsive mobile design
- Unit tests for views and forms
- Docker containerization

However, these are not required and the current implementation is complete and compliant.

---

## Conclusion

This Django project successfully implements all four exercises with:
- ✅ Complete functionality
- ✅ Clean, maintainable code
- ✅ Proper Django conventions
- ✅ Full compliance with requirements
- ✅ Professional styling
- ✅ Comprehensive documentation

The project is ready for evaluation and demonstrates solid understanding of:
- Django project structure
- Template system and inheritance
- URL routing and views
- Forms and data handling
- Static files management
- Python integration with templates
