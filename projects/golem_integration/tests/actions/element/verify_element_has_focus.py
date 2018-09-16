from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'verify_element_has_focus action'

def test(data):
    actions.navigate(data.env.url+'elements/')
    actions.focus_element('#input-one')
    actions.verify_element_has_focus('#input-one')
    golem_steps.assert_last_step_message('Verify element #input-one has focus')
    actions.focus_element('#textarea-1')
    actions.verify_element_has_focus('#textarea-1')
    actions.verify_element_has_focus('#input-one')
    golem_steps.assert_last_error('element #input-one does not have focus')
