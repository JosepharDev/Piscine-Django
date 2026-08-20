<div align="center">

# 🌐 Day 00 — Web Foundations

### HTML, CSS, JavaScript & Shell scripting — no frameworks, just fundamentals.

[![Day](https://img.shields.io/badge/Day-00-6366f1?style=for-the-badge)]()
[![Topics](https://img.shields.io/badge/Topics-HTML%20%7C%20CSS%20%7C%20JS%20%7C%20Shell-0ea5e9?style=for-the-badge)]()

</div>

---

## 📖 About

Day 00 is all about the **raw building blocks** of the web. No libraries, no frameworks — just a browser, a terminal, and your own hands. You learn to write valid HTML, style it with CSS, sprinkle interactivity with JavaScript, and automate with shell scripts.

---

## 📁 Exercises

### ex00 — URL Follower (`myawesomescript.sh`)
A shell script that follows HTTP redirects and prints the final effective URL.

```bash
./myawesomescript.sh <url>
```

- Uses `curl -L` to follow redirects silently
- Prints the final resolved URL via `%{url_effective}`
- Handles missing or extra arguments gracefully

---

### ex01 — Static CV (`cv.html`)
A hand-crafted HTML résumé page.

- Semantic HTML structure (`<table>`, `<section>`, `<article>`)
- Inline CSS for clean table styling
- No external dependencies — pure HTML

---

### ex02 — Contact Form (`form.html`)
An HTML contact form with client-side validation.

- Fields: first name, last name, email, phone, message
- Uses native HTML5 `required`, `type="email"`, `autocomplete`
- No JavaScript needed — relies on browser-native validation

---

### ex03 — Styled Page Clone (`copy.html`)
A styled HTML page that replicates a given design using CSS.

- External stylesheet (`utils/ex03/style.css`)
- Image embedding
- CSS layout with custom fonts and colors

---

### ex04 — JavaScript Snippets (`snippets.html`)
An HTML page that loads and runs multiple JavaScript files.

- Integrates `file1.js` through `file4.js`
- Demonstrates DOM manipulation and script loading order

---

### ex05 — Full Landing Page (`index.html`)
A complete styled landing page with audio, fonts, and imagery.

- Custom web fonts (Bebas Neue, Droid Serif)
- Audio player integration
- Normalized CSS (`normalize.css`)
- Responsive layout with background image

---

## 🗂️ Structure

```
00/
├── ex00/
│   └── myawesomescript.sh    # curl URL follower
├── ex01/
│   └── cv.html               # Static résumé
├── ex02/
│   └── form.html             # Contact form
├── ex03/
│   └── copy.html             # Styled page clone
├── ex04/
│   └── snippets.html         # JS integration
├── ex05/
│   └── index.html            # Full landing page
└── utils/                    # Shared assets (CSS, JS, fonts, images, audio)
```

---

## 💡 Key Concepts

| Concept | Covered in |
|---------|------------|
| `curl` & HTTP redirects | ex00 |
| Semantic HTML | ex01, ex02 |
| HTML5 form validation | ex02 |
| CSS layouts & selectors | ex03, ex05 |
| JavaScript file loading | ex04 |
| Web fonts & audio | ex05 |
