from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'assert_element_has_focus action'

def test(data):
    actions.navigate(data.env.url+'elements/')
    actions.focus_element('#input-one')
    actions.assert_element_has_focus('#input-one')
    golem_steps.assert_last_step_message('Assert element #input-one has focus')
    actions.focus_element('#textarea-1')
    actions.assert_element_has_focus('#textarea-1')
    try:
        actions.assert_element_has_focus('#input-one')
    except AssertionError as e:
        assert 'element #input-one does not have focus' in e.args[0]
