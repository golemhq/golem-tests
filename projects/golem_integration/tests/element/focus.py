from golem import actions


description = 'Verify webelement.focus method'

def test(data):
    actions.navigate(data.env.url + 'elements/')
    browser = actions.get_browser()
    text_input = browser.find(id='input-one')
    text_area = browser.find(id='textarea-1')
    text_input.focus()
    assert text_input.has_focus()
    text_area.focus()
    assert not text_input.has_focus()
    assert text_area.has_focus()
