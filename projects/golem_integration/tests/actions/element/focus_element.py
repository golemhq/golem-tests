from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'Verify focus_element action'

def test(data):
    actions.navigate(data.env.url + 'elements/')
    b = actions.get_browser()
    text_input = b.find(id='input-one')
    text_area = b.find(id='textarea-1')
    actions.focus_element(text_input)
    golem_steps.assert_last_step_message('Focus element input-one')
    assert text_input.has_focus()
    actions.focus_element(text_area)
    assert not text_input.has_focus()
    assert text_area.has_focus()
