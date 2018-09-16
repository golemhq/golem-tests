from golem import actions


description = 'Verify get_element_attribute action'

def test(data):
    actions.navigate(data.env.url + 'elements/')
    class_ = actions.get_element_attribute('#button-one-result', 'class')
    assert class_ == 'span-result'
