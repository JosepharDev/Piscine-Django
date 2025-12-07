#!/usr/bin/python3

from elements import (
    Html, Head, Body, Title, Meta, Img, Table, Th, Tr, Td, Ul, Ol, Li, H1, H2, P, Div, Span, Hr, Br, Elem, Text
)


class Page:
    """
    A class to manage and validate the structure of an Elem tree against
    HTML rules.
    """
    def __init__(self, elem: Elem) -> None:
        if not isinstance(elem, Elem):
            # The original code uses Elem.ValidationError here, assuming it's defined
            raise Elem.ValidationError("Root element must be an instance of Elem.")
        self.elem = elem

    def __str__(self) -> str:
        result = ""
        if isinstance(self.elem, Html):
            result += "<!DOCTYPE html>\n"
        result += str(self.elem)
        return result

    def write_to_file(self, path: str) -> None:
        """Writes the HTML code to a file."""
        # Use try/except to handle IOError, as required by strict environments
        try:
            with open(path, "w") as f:
                f.write(self.__str__())
        except IOError as e:
            # Re-raising as an exception to be caught in the test block
            raise Exception(f"File writing failed: {e}")

    def is_valid(self) -> bool:
        """Initiates recursive structural validation."""
        return self._recursive_check(self.elem)

    # --- Rule-Checking Helpers ---

    def _check_type_allowed(self, elem: Elem) -> bool:
        """
        Rule 1: Check if the node type is one of the allowed HTML element types or Text.
        """
        return isinstance(elem, (Html, Head, Body, Title, Meta, Img, Table, Th, Tr, Td, Ul, Ol, Li,
                                  H1, H2, P, Div, Span, Hr, Br)) or type(elem) == Text

    def _check_content_single_text(self, elem: Elem) -> bool:
        """
        Rule 5: Title, H1, H2, Li, Th, Td must only contain one Text.
        """
        return isinstance(elem, (Title, H1, H2, Li, Th, Td)) and \
               len(elem.content) == 1 and type(elem.content[0]) == Text

    def _check_content_only_text(self, elem: Elem) -> bool:
        """
        Rule 6: P must only contain Text.
        """
        return isinstance(elem, P) and \
               all(type(el) == Text for el in elem.content)

    def _check_content_body_div(self, elem: Elem) -> bool:
        """
        Rule 4: Body and Div must only contain H1, H2, Div, Table, Ul, Ol, Span, or Text.
        """
        return isinstance(elem, (Body, Div)) and \
               all(isinstance(el, (H1, H2, Div, Table, Ul, Ol, Span)) or
                   type(el) == Text for el in elem.content)

    def _check_content_span(self, elem: Elem) -> bool:
        """
        Rule 7: Span must only contain Text or some P.
        """
        return isinstance(elem, Span) and \
               all(isinstance(el, (Text, P)) for el in elem.content)

    def _check_content_list(self, elem: Elem) -> bool:
        """
        Rule 8: Ul and Ol must contain at least one Li and only some Li.
        """
        return isinstance(elem, (Ul, Ol)) and \
               len(elem.content) > 0 and \
               all(isinstance(el, Li) for el in elem.content)

    def _check_content_tr(self, elem: Elem) -> bool:
        """
        Rule 9: Tr must contain at least one Th or Td and they must be mutually exclusive.
        """
        if not isinstance(elem, Tr) or len(elem.content) == 0:
            return False
            
        content = elem.content
        if not all(isinstance(el, (Th, Td)) for el in content):
            return False
            
        # Check mutual exclusivity (all elements must be of the same type as the first element)
        first_type = type(content[0])
        return all(type(el) == first_type for el in content)

    def _check_content_table(self, elem: Elem) -> bool:
        """
        Rule 10: Table must only contain Tr and only some Tr.
        """
        return isinstance(elem, Table) and \
               all(isinstance(el, Tr) for el in elem.content)

    def _check_structure_html(self, elem: Elem) -> bool:
        """
        Rule 2: Html must strictly contain a Head, then a Body.
        """
        return isinstance(elem, Html) and len(elem.content) == 2 and \
               type(elem.content[0]) == Head and type(elem.content[1]) == Body

    def _check_structure_head(self, elem: Elem) -> bool:
        """
        Rule 3: Head must only contain one Title.
        """
        return isinstance(elem, Head) and \
               [isinstance(el, Title) for el in elem.content].count(True) == 1

    # --- Main Recursive Check ---

    def _recursive_check(self, elem: Elem) -> bool:
        """
        Performs the full validation by chaining rule checks.
        """
        # Rule 1 Check
        if not self._check_type_allowed(elem):
            return False
            
        # Base case for recursion: simple tags or text nodes (which have no children to check)
        if type(elem) == Text or isinstance(elem, Meta) or isinstance(elem, Img) or isinstance(elem, Hr) or isinstance(elem, Br):
            return True

        # --- Rule-Specific Content/Structure Checks ---

        is_node_content_valid = False

        if self._check_structure_html(elem):            # Rule 2
            is_node_content_valid = True
        elif self._check_structure_head(elem):          # Rule 3
            is_node_content_valid = True
        elif self._check_content_body_div(elem):        # Rule 4
            is_node_content_valid = True
        elif self._check_content_single_text(elem):     # Rule 5
            is_node_content_valid = True
        elif self._check_content_only_text(elem):       # Rule 6
            is_node_content_valid = True
        elif self._check_content_span(elem):            # Rule 7
            is_node_content_valid = True
        elif self._check_content_list(elem):            # Rule 8
            is_node_content_valid = True
        elif self._check_content_tr(elem):              # Rule 9
            is_node_content_valid = True
        elif self._check_content_table(elem):           # Rule 10
            is_node_content_valid = True
        elif isinstance(elem, (Meta, Img, Hr, Br)):     # Simple tags already covered in the base case, but explicit for completeness
            is_node_content_valid = True

        if not is_node_content_valid:
            # If the node type does not satisfy its required content rules, it's invalid.
            return False

        # --- Recurse on Children ---
        return all(self._recursive_check(el) for el in elem.content)