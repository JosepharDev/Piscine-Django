#!/usr/bin/python3
from elements import (
    Html, Head, Body, Title, Meta, Img, Table, Th, Tr, Td, Ul, Ol, Li, H1, H2, P, Div, Span, Hr, Br, Elem, Text
)

class Page:
    def __init__(self, elem: Elem) -> None:
        if not isinstance(elem, Elem):
            raise Elem.ValidationError("Root must be an Elem instance")
        self.elem = elem

    def __str__(self) -> str:
        result = ""
        if isinstance(self.elem, Html):
            result += "<!DOCTYPE html>\n"
        result += str(self.elem)
        return result

    def write_to_file(self, path: str) -> None:
        try:
            with open(path, "w") as f:
                f.write(self.__str__())
        except IOError as e:
            raise Exception(f"File writing error: {e}")

    def is_valid(self) -> bool:
        return self.__recursive_check(self.elem)

    def __recursive_check(self, elem: Elem) -> bool:
        # Rule 1: Allowed Types
        if not isinstance(elem, (Html, Head, Body, Title, Meta, Img, Table, Th, Tr, Td, Ul, Ol, Li, H1, H2, P, Div, Span, Hr, Br, Text)):
            return False

        # --- Specific Structural Rules ---
        
        # Rule 2: Html -> [Head, Body]
        if isinstance(elem, Html):
            if len(elem.content) != 2:
                return False
            if not isinstance(elem.content[0], Head) or not isinstance(elem.content[1], Body):
                return False
                
        # Rule 3: Head -> [Title]
        elif isinstance(elem, Head):
            if len(elem.content) != 1:
                return False
            if not isinstance(elem.content[0], Title):
                return False
                
        # Rule 4: Body/Div -> [H1, H2, Div, Table, Ul, Ol, Span, Text]
        elif isinstance(elem, (Body, Div)):
            for child in elem.content:
                if not isinstance(child, (H1, H2, Div, Table, Ul, Ol, Span, Text)):
                    return False
                    
        # Rule 5: Title, H1, H2, Li, Th, Td -> [Text]
        elif isinstance(elem, (Title, H1, H2, Li, Th, Td)):
            if len(elem.content) != 1:
                return False
            if not isinstance(elem.content[0], Text):
                return False
                
        # Rule 6: P -> [Text] (Multiple text elements allowed, but ONLY Text)
        elif isinstance(elem, P):
            for child in elem.content:
                if not isinstance(child, Text):
                    return False
                    
        # Rule 7: Span -> [Text, P]
        elif isinstance(elem, Span):
            for child in elem.content:
                if not isinstance(child, (Text, P)):
                    return False
                    
        # Rule 8: Ul/Ol -> [Li] (at least one)
        elif isinstance(elem, (Ul, Ol)):
            if len(elem.content) == 0:
                return False
            for child in elem.content:
                if not isinstance(child, Li):
                    return False
                    
        # Rule 9: Tr -> [Th or Td] (at least one, mutually exclusive)
        elif isinstance(elem, Tr):
            if len(elem.content) == 0:
                return False
            
            # Determine type of first child (Th or Td)
            first_type = type(elem.content[0])
            if first_type not in (Th, Td):
                return False
            
            # Ensure all other children match the first type
            for child in elem.content:
                if not isinstance(child, first_type):
                    return False

        # Rule 10: Table -> [Tr]
        elif isinstance(elem, Table):
            for child in elem.content:
                if not isinstance(child, Tr):
                    return False

        # --- Recursion ---
        # If it's a Text node or a simple tag, it has no children to check.
        if isinstance(elem, (Text, Meta, Img, Hr, Br)):
            return True

        # Check all children recursively
        return all(self.__recursive_check(child) for child in elem.content)

if __name__ == "__main__":
    # Test 1: Invalid Structure (Html has Body then Head) - Should be False
    print("Test 1 (Invalid):")
    head = Page(Html([Body(), Head()]))
    print(head.is_valid()) 

    # Test 2: Invalid Content (H1 contains P) - Should be False
    print("\nTest 2 (Invalid):")
    try:
        head = Page(H1(P(Text("hello"))))
        print(head.is_valid())
    except Exception as e:
        print(f"Caught expected error or invalid result: {e}")

    # Test 3: Valid Structure - Should be True
    print("\nTest 3 (Valid):")
    valid = Page(Html([
        Head(Title(Text("Title"))),
        Body(H1(Text("Hello")))
    ]))
    print(valid.is_valid())