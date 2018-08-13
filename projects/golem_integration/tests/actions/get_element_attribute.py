from golem import actions


description = 'Verify get_element_attribute action'

def test(data):
    actions.navigate(data.env.url + 'elements/')
    assert actions.get_element_attribute('#textarea-1', 'name') == 'textarea-name'
    assert actions.get_element_attribute('#selected-checkbox', 'checked') == 'true'
    assert actions.get_element_attribute('#selected-checkbox', 'invalid-attr') is None
