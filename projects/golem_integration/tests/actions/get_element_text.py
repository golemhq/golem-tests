from golem import actions


description = 'Verify get_element_text action'

def test(data):
    actions.navigate(data.env.url + 'elements/')
    assert actions.get_element_text('#link1') == 'this is a link to index'

