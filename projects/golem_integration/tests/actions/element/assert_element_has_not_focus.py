from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'assert_element_has_not_focus action'

def test(data):
    actions.navigate(data.env.url+'elements/')
    actions.assert_element_has_not_focus('#input-one')
    golem_steps.assert_last_step_message('Assert element #button-one does not have focus')
    actions.focus_element('#input-one')
    try:
        actions.assert_element_has_not_focus('#input-one')
    except AssertionError as e:
        assert 'element #input-one has focus' in e.args[0]
