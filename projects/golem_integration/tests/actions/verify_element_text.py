from golem import actions


description = 'verify_element_text action'

def test(data):
    actions.navigate(data.env.url+'elements/')
    actions.verify_element_text('#link1', 'this is a link to index')
    try:
        actions.verify_element_text('#link1', 'incorrect text')
        assert False, 'Expected Exception'
    except Exception as e:
        assert "expected element #link1 text to be 'incorrect text' but was 'this is a link to index'" in e.args[0]
