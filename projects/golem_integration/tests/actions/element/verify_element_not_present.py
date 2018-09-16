from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'verify_element_not_present action'

def test(data):
    actions.navigate(data.env.url+'elements/')
    actions.verify_element_not_present('#does-not-exist')
    golem_steps.assert_last_step_message('Verify element #does-not-exist is not present')
    actions.verify_element_not_present('#button-one')
    golem_steps.assert_last_error('element #button-one is present')
