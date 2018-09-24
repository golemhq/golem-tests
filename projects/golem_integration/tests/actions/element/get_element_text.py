from golem import actions


description = 'Verify get_element_text action'

def test(data):
    actions.navigate(data.env.url + 'elements/')
    assert actions.get_element_text('h1') == 'Common Elements'
    assert actions.get_element_text("label[for='selected-checkbox']") == 'Selected Checkbox'
