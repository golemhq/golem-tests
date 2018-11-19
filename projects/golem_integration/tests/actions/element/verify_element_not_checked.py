from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'verify_element_not_checked action'

def test(data):
    actions.navigate(data.env.url+'elements/')
    actions.verify_element_not_checked('#unselected-checkbox')
    golem_steps.assert_last_step_message('Verify element #unselected-checkbox is not checked')
    actions.verify_element_not_checked('#selected-checkbox')
    golem_steps.assert_last_error('element #selected-checkbox is checked')
