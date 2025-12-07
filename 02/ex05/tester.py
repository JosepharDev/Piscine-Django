from elem import Text, Elem # Assuming Text and Elem are imported from elem.py
from elements import Html, Head, Body, Title, H1, Img # Assuming your new classes are in a module named 'your_module' or defined in the same script.

# --- Replicating the required HTML structure using the new classes ---

# 1. Title Element
# Note: Text() is used to ensure content is properly HTML-escaped and handles newlines
title_content = Title(content=Text("Oh no, not again!"))

# 2. Head Element
head_elem = Head(content=title_content)

# 3. Header Element (h1)
h1_content = H1(content=Text("Oh no, not again!"))

# 4. Image Element (simple tag)
img_content = Img(
    attr={'src': 'http://i.imgur.com/pfp3x.jpg', 'title': 'The Source'}
)

# 5. Body Element
body_elem = Body(content=[h1_content, img_content])

# 6. HTML Element
html_elem = Html(content=[head_elem, body_elem])

# 7. Final Output (with DOCTYPE)
doctype = "<!DOCTYPE html>"

# Combine and display the final HTML
final_html_output = f"{doctype}\n{html_elem}\n"
print(final_html_output)