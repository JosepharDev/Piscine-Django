<div align="center">

# 🐍 Day 01 — Python Basics

### Python types, data structures, file I/O, and HTML generation.

[![Day](https://img.shields.io/badge/Day-01-6366f1?style=for-the-badge)]()
[![Topics](https://img.shields.io/badge/Topics-Python%20%7C%20Types%20%7C%20Dicts%20%7C%20Files-0ea5e9?style=for-the-badge)]()

</div>

---

## 📖 About

Day 01 dives into **Python fundamentals** — exploring the language's type system, its powerful data structures (lists, dicts, sets, tuples), file reading, and pure-Python HTML generation. Every exercise builds the muscle memory needed for real Django development.

---

## 📁 Exercises

### ex00 — Variable Display (`var.py`)
Prints a variable's value and type as it changes through multiple Python types.

```bash
python3 var.py
```

Covers: `int`, `str`, `float`, `bool`, `list`, `dict`, `tuple`, `set`

---

### ex01 — Number File Reader (`numbers.py`)
Reads a comma-separated file of numbers and prints each one on its own line.

```bash
python3 numbers.py     # reads numbers.txt in the same directory
```

Demonstrates: file I/O, `split()`, exception handling

---

### ex02 — List to Dictionary (`var_to_dict.py`)
Converts a list of `(name, birth_year)` tuples into a dictionary and prints each entry.

```bash
python3 var_to_dict.py
```

Output format: `{birth_year} : {name}`

---

### ex03 — Capital City Lookup (`capital_city.py`)
Given a US state name, prints its capital city using a two-level dictionary lookup.

```bash
python3 capital_city.py "Oregon"
# Salem
```

Uses a `states → abbreviation → capital` chain.

---

### ex04 — State Reverse Lookup (`state.py`)
Given a capital city name, prints the state it belongs to.

```bash
python3 state.py "Denver"
# Colorado
```

Implements `dict_get_key_from_value()` for reverse dictionary traversal.

---

### ex05 — All-in-One Lookup (`all_in.py`)
Accepts either a state name or a capital city and figures out what it received, then prints the counterpart.

```bash
python3 all_in.py "Salem"
# Salem is the capital of Oregon
python3 all_in.py "Oregon"
# Oregon's capital is Salem
```

Case-insensitive matching. Handles unknown inputs gracefully.

---

### ex06 — Sort by Birth Year (`my_sort.py`)
Takes a dictionary of `{guitarist: birth_year}` and prints names sorted by birth year.

```bash
python3 my_sort.py
```

Uses `sorted()` with a lambda key on values.

---

### ex07 — Periodic Table HTML Generator (`periodic_table.py`)
Reads `periodic_table.txt` and generates a full HTML periodic table page.

```bash
python3 periodic_table.py
# → periodic_table.html
```

- Parses a custom text format (`Name = position: X, number: Y, ...`)
- Generates `<table>` with one `<td>` per element
- Handles empty grid cells for correct positioning

---

## 🗂️ Structure

```
01/
├── ex00/
│   └── var.py               # Python type display
├── ex01/
│   └── numbers.py           # File reader
├── ex02/
│   └── var_to_dict.py       # Tuple list → dict
├── ex03/
│   └── capital_city.py      # State → capital
├── ex04/
│   └── state.py             # Capital → state
├── ex05/
│   └── all_in.py            # Bidirectional lookup
├── ex06/
│   └── my_sort.py           # Sort by birth year
└── ex07/
    ├── periodic_table.py    # HTML generator
    └── utils/
        └── ex07/
            └── periodic_table.txt
```

---

## 💡 Key Concepts

| Concept | Covered in |
|---------|------------|
| Python built-in types | ex00 |
| File I/O & error handling | ex01 |
| List comprehensions | ex02, ex06 |
| Dictionary operations | ex03, ex04, ex05 |
| Sorting with lambdas | ex06 |
| HTML generation from data | ex07 |
