from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'verify_element_has_not_focus action'

def test(data):
    actions.navigate(data.env.url+'elements/')
    actions.verify_element_has_not_focus('#input-one')
    golem_steps.assert_last_step_message('Verify element #input-one does not have focus')
    actions.focus_element('#input-one')
    actions.verify_element_has_not_focus('#input-one')
    golem_steps.assert_last_error('element #input-one has focus')
