#!/usr/bin/python3

class Text(str):
    """
    A Text class to represent a text you could use with your HTML elements.

    Because directly using str class was too mainstream.
    """

    def __str__(self):
        """
        Do you really need a comment to understand this method?..
        """
        escaped_str = (
            super().__str__()
            .replace('&', '&amp;')
            .replace('<', '&lt;')
            .replace('>', '&gt;')
            .replace('"', '&quot;')
        )
        return escaped_str.replace('\n', '\n<br />\n')

class Elem:
    """
    Elem will permit us to represent our HTML elements.
    """
    class ValidationError(Exception):
        """
        custom exception for validation error related to Elem content.
        """
        def __init__(self, message):
            super().__init__(message)

    def __init__(self, tag='div', attr={}, content=None, tag_type='double'):
        """
        __init__() method.

        Obviously.
        """
        self.tag = tag
        self.attr = attr
        self.tag_type = tag_type
        self.content = []
        if content is not None:
            self.add_content(content)

    def __str__(self):
        """
        The __str__() method will permit us to make a plain HTML representation
        of our elements.
        Make sure it renders everything (tag, attributes, embedded
        elements...).
        """
        str__attr = self.__make_attr()
        if self.tag_type == 'double':
            content_str = self.__make_content()
            result = f"<{self.tag}{str__attr}>{content_str}</{self.tag}>"
        elif self.tag_type == 'simple':
            result = f"<{self.tag}{str__attr} />"
        else:
            raise self.ValidationError(f"Invalid tag_type: {self.tag_type}")
        return result

    def __make_attr(self):
        """
        Here is a function to render our elements attributes.
        """
        result = ''
        for pair in sorted(self.attr.items()):
            escaped_value = str(pair[1]).replace('"', '&quot;')
            result += ' ' + str(pair[0]) + '="' + escaped_value + '"'
        return result

    def __make_content(self):
        """
        Here is a method to render the content, including embedded elements.
        """

        if len(self.content) == 0:
            return ''
        
        needs_indent = any(isinstance(item, Elem) for item in self.content)
        if not needs_indent:
            return "".join(str(elem) for elem in self.content)
        
        result = '\n'
        for elem in self.content:
            elem_str = str(elem)
            indented_str = "  "+ elem_str.replace('\n', '\n  ')
            result += indented_str + '\n'
        return result.rstrip(' ').rstrip('\n')

    def add_content(self, content):
        if not Elem.check_type(content):
            raise Elem.ValidationError
        if self.tag_type == 'simple':
            raise Elem.ValidationError("Cannot add content to a simple (self-closing) tag.")
        
        if type(content) == list:
            self.content += [elem for elem in content if elem != Text('')]
        elif content != Text(''):
            self.content.append(content)

    @staticmethod
    def check_type(content):
        """
        Is this object a HTML-compatible Text instance or a Elem, or even a
        list of both?
        """
        return (isinstance(content, Elem) or type(content) == Text or
                (type(content) == list and all([type(elem) == Text or
                                                isinstance(elem, Elem)
                                                for elem in content])))


if __name__ == '__main__':
    # --- Replication of the required HTML structure ---

    # 1. Title Element
    title_content = Elem(tag='title', content=Text("Oh no, not again!"))

    # 2. Head Element
    head_elem = Elem(tag='head', content=title_content)

    # 3. Header Element (h1)
    h1_content = Elem(tag='h1', content=Text("Oh no, not again!"))

    # 4. Image Element (simple tag)
    img_content = Elem(
        tag='img',
        attr={'src': 'http://i.imgur.com/pfp3x.jpg', 'title': 'The Source'}, # Added title attr for completeness
        tag_type='simple'
    )

    # 5. Body Element
    body_elem = Elem(tag='body', content=[h1_content, img_content])

    # 6. HTML Element
    html_elem = Elem(tag='html', content=[head_elem, body_elem])

    # 7. Final Output (with DOCTYPE)
    doctype = "<!DOCTYPE html>"

    # Combine and display the final HTML
    final_html_output = f"{doctype}\n{html_elem}"
    print(final_html_output)
    
    # --- Example Test ---
    print("\n--- Example Test of Simple/Double Tags ---")
    try:
        simple_img = Elem(tag='img', tag_type='simple')
        simple_img.add_content(Text("Oops"))
    except Elem.ValidationError as e:
        print(f"✅ Successfully caught error for adding content to a simple tag: {e}")