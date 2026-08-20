<div align="center">

# 🧱 Day 02 — Python OOP & Templating

### Object-oriented Python, class inheritance, metaclasses, and HTML generation.

[![Day](https://img.shields.io/badge/Day-02-6366f1?style=for-the-badge)]()
[![Topics](https://img.shields.io/badge/Topics-OOP%20%7C%20Inheritance%20%7C%20Metaclasses%20%7C%20HTML-0ea5e9?style=for-the-badge)]()

</div>

---

## 📖 About

Day 02 goes deeper into Python by exploring **object-oriented programming** — classes, inheritance, operator overloading, metaclasses, and building a mini HTML rendering engine from scratch. The exercises culminate in a self-contained HTML page builder that mirrors how Django templates work internally.

---

## 📁 Exercises

### ex00 — Template Renderer (`render.py`)
A Django-inspired template engine. Takes a `.template` file with `{variable}` placeholders and replaces them with values from `settings.py`.

```bash
python3 render.py myCV.template
# → myCV.html
```

- Reads context from `settings.py` using `vars()`
- Simple string substitution (no `re`, no `jinja`)
- Validates file extension and existence

---

### ex01 — The Intern (`intern.py`)
A class called `intern` whose only purpose is to print `None` no matter what you call on it.

```python
i = intern()
i.whatever()    # → None
i.anything      # → None (attribute access)
```

Uses `__getattr__` and returns a lambda that prints `None`.

---

### ex02 — Hot Beverage Hierarchy (`beverages.py`)
A classic OOP class hierarchy for a café menu:

| Class | Price | Description |
|-------|-------|-------------|
| `HotBeverage` | €0.30 | Base class — just hot water |
| `Coffee` | €0.40 | A coffee, to stay awake |
| `Tea` | €0.30 | Inherits base price |
| `Chocolate` | €0.50 | Sweet chocolate |
| `Cappuccino` | €0.45 | Un po' di Italia |

```bash
python3 beverages.py
```

---

### ex03 — Coffee Machine with Metaclass (`machine.py`)
Extends the beverage classes with a `CoffeeMachine` that uses a **metaclass** to automatically register all beverage types.

```bash
python3 machine.py
```

- Metaclass auto-discovers `HotBeverage` subclasses
- Machine presents a menu and serves the chosen drink
- Demonstrates Python's metaclass machinery

---

### ex04 — HTML Element Builder (`elem.py`)
A Python class `Elem` that can represent any HTML element and render it as valid HTML.

```python
title = Elem('h1', content=Text("Hello!"))
print(title)
# <h1>
#   Hello!
# </h1>
```

Features:
- `double` tags (`<div>...</div>`) and `simple` tags (`<br />`)
- HTML-safe `Text` class (escapes `&`, `<`, `>`, `"`, newlines)
- `add_content()` with type validation
- Custom `ValidationError` exception
- Sorted attribute rendering

---

### ex05 — Extended HTML Elements (`elements.py`)
Adds concrete HTML element classes on top of `elem.py`:

`Html`, `Head`, `Body`, `Title`, `Meta`, `Img`, `Table`, `Th`, `Tr`, `Td`, `Ul`, `Ol`, `Li`, `H1`→`H2`, `P`, `Div`, `Span`, `Hr`, `Br`

```bash
python3 tester.py
```

---

### ex06 — Full Page Generator (`Page.py`)
A `Page` class that wraps a complete HTML document (`<!DOCTYPE html>` + `<html>`) and validates its structure before rendering.

```bash
python3 tester.py
```

- Validates that `<head>` contains only meta-level elements
- Validates that `<body>` contains only body-level elements
- Raises `Page.PageError` for structural violations

---

## 🗂️ Structure

```
02/
├── ex00/
│   ├── render.py          # Template renderer
│   ├── settings.py        # Template context
│   └── myCV.template      # Template file
├── ex01/
│   └── intern.py          # The Intern class
├── ex02/
│   └── beverages.py       # HotBeverage hierarchy
├── ex03/
│   ├── beverages.py       # Extended beverages
│   └── machine.py         # Metaclass coffee machine
├── ex04/
│   ├── elem.py            # HTML Elem + Text builder
│   └── tests.py           # Unit tests
├── ex05/
│   ├── elem.py            # Core Elem
│   ├── elements.py        # Concrete HTML tags
│   └── tester.py
└── ex06/
    ├── elem.py
    ├── elements.py
    ├── Page.py            # Full page generator
    └── tester.py
```

---

## 💡 Key Concepts

| Concept | Covered in |
|---------|------------|
| Django-style templating | ex00 |
| `__getattr__` magic method | ex01 |
| Class inheritance & `__str__` | ex02, ex04 |
| Metaclasses | ex03 |
| HTML escaping | ex04 |
| Type validation with exceptions | ex04, ex06 |
| Recursive HTML tree rendering | ex05, ex06 |
