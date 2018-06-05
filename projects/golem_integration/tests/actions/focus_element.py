from golem import actions


description = 'Verify focus_element action'

def test(data):
    actions.navigate(data.env.url + 'elements/')
    b = actions.get_browser()
    text_input = b.find(id='input-one')
    text_area = b.find(id='textarea-1')
    actions.focus_element(text_input)
    assert text_input.has_focus()
    actions.focus_element(text_area)
    assert not text_input.has_focus()
    assert text_area.has_focus()
