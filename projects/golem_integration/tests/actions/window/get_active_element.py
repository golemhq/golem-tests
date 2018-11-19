from golem import actions


description = 'Verify get_active_element action'

def test(data):
    actions.navigate(data.env.url + 'elements/')
    b = actions.get_browser()
    text_input = b.find(id='input-one')
    actions.focus_element(text_input)
    active_element = actions.get_active_element()
    assert active_element == actions.get_browser().switch_to.active_element
