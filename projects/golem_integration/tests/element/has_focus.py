from golem import actions
from golem.browser import element


description = 'Verify webelement.has_focus method'

def test(data):
    actions.navigate(data.env.url+'elements/')
    text_input = element('#input-one')
    text_area = element('#textarea-1')
    assert not text_input.has_focus()
    text_input.focus()
    assert text_input.has_focus()
    assert not text_area.has_focus()
    actions.send_keys(text_area, 'test')
    assert text_area.has_focus()
    assert not text_input.has_focus()
