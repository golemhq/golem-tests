from golem import actions


description = 'verify_element_text_not_contains action'

def test(data):
    actions.navigate(data.env.url+'elements/')
    actions.verify_element_text_not_contains('#link1', 'not-contained')
    try:
        actions.verify_element_text_not_contains('#link1', 'this is a link')
        assert False, 'Expected Exception'
    except Exception as e:
        assert "element #link1 contains text 'this is a link'" in e.args[0]
