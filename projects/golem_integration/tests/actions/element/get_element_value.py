from golem import actions


description = 'Verify get_element_value action'

def test(data):
    actions.navigate(data.env.url + 'elements/')
    actions.send_keys('#input-one', 'foo')
    assert actions.get_element_value('#input-one') == 'foo'
