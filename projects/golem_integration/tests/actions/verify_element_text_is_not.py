from golem import actions


description = 'verify_element_text_is_not action'

def test(data):
    actions.navigate(data.env.url+'elements/')
    actions.verify_element_text_is_not('#link1', 'incorrect text')
    try:
        actions.verify_element_text_is_not('#link1', 'this is a link to index')
        assert False, 'Expected Exception'
    except Exception as e:
        assert "expected element #link1 text to not be 'this is a link to index'" in e.args[0]
