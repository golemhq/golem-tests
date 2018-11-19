from golem import actions


description = 'Verify get_element_attribute action'

def test(data):
    actions.navigate(data.env.url + 'elements/')
    name = actions.get_element_attribute('#textarea-1', 'name')
    assert name == 'textarea-name'
