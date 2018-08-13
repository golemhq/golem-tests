from golem import actions


description = 'Verify get_element_value action'

def test(data):
    actions.navigate(data.env.url + 'elements/')
    assert actions.get_element_value('#input-one') == ''
    actions.send_keys('#input-one', 'some value')
    assert actions.get_element_value('#input-one') == 'some value'

