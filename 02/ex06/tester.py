from Page import * 

def __print_test(target: Page, toBe: bool):
    print("================START===============")
    try:
        print(str(target))
    except Exception as e:
        print(f"Error during __str__ conversion: {type(e).__name__}")
    
    print("===============IS_VALID=============")
    try:
        assert target.is_valid() == toBe
        print("{:^36s}".format(str(target.is_valid())))
    except AssertionError:
        print("ASSERTION FAILED! Expected: {}, Got: {}".format(toBe, target.is_valid()))
        raise 
    except Exception as e:
        print(f"Error during is_valid check: {type(e).__name__}: {e}")
        raise
def __build_valid_complex_tree():
    """Builds a complex, multi-level structure that should pass validation."""
    
    valid_ul = Ul([
        Li(Text("Item 1")), 
        Li(Text("Item 2")),
        Li(Text("Item 3"))
    ])

    valid_table = Table([
        Tr([Th(Text("H1")), Th(Text("H2"))]), # Valid: Only Th
        Tr([Td(Text("D1")), Td(Text("D2"))])  # Valid: Only Td
    ])

    valid_span = Span([
        Text("Inline text."),
        P(Text("Paragraph inside span."))
    ])
    
    valid_div = Div([
        H1(Text("Section Title")), 
        valid_table, 
        valid_ul, 
        valid_span,
        Text("Footer text.")
    ])

    root = Html([
        Head(Title(Text("Complex Valid Page Test"))), # Rule 3
        Body([valid_div, H2(Text("Subtitle"))])     # Rule 2
    ])
    return root

def __test_complex_structure():
    print("\n%{:=^34s}%\n".format("COMPLEX STRUCTURES"))
    
    
    try:
        root_valid = __build_valid_complex_tree()
        target = Page(root_valid)
        
        print("✅ Test A: Complex Tree (Fully Valid)")
        __print_test(target, True)
        
    except AssertionError:
        print("🛑 Test A FAILED (Valid tree failed assertion)")
    except Exception as e:
        print(f"🛑 Test A FAILED UNCAUGHT EXCEPTION: {type(e).__name__}: {e}")
        
    try:
        root_invalid_content = __build_valid_complex_tree()
        
        invalid_tr_mixed = Tr([Th(Text("H")), Td(Text("D"))])
        
        root_invalid_content.content[1].content[0].content[1].content.append(invalid_tr_mixed)
        
        target = Page(root_invalid_content)
        
        print("\n❌ Test B: Deep Invalid Content (Table/Tr Mix Th/Td)")
        __print_test(target, False)
        
    except AssertionError:
        print("🛑 Test B FAILED (Invalid content tree passed assertion)")
    except Exception as e:
        print(f"🛑 Test B FAILED UNCAUGHT EXCEPTION: {type(e).__name__}: {e}")

    try:
        root_invalid_type = __build_valid_complex_tree()

        forbidden_html = Html([Head(Title(Text("Forbidden"))), Body(P(Text("P")))])
        
        root_invalid_type.content[1].content.append(forbidden_html) 
        
        target = Page(root_invalid_type)
        
        print("\n❌ Test C: Deep Invalid Type (Body contains Html)")
        __print_test(target, False) 
        
    except AssertionError:
        print("🛑 Test C FAILED (Invalid type tree passed assertion)")
    except Exception as e:
        print(f"🛑 Test C FAILED UNCAUGHT EXCEPTION: {type(e).__name__}: {e}")
        

def __test():
    __test_complex_structure()

if __name__ == '__main__':
    __test()