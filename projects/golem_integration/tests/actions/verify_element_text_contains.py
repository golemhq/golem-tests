from golem import actions


description = 'verify_element_text_contains action'

def test(data):
    actions.navigate(data.env.url+'elements/')
    actions.verify_element_text_contains('#link1', 'this is a link')
    try:
        actions.verify_element_text_contains('#link1', 'not-contained')
        assert False, 'Expected Exception'
    except Exception as e:
        assert "expected element #link1 to contain text 'not-contained'" in e.args[0]
