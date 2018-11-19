from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'verify_element_present action'

def test(data):
    actions.navigate(data.env.url+'special-elements/')
    actions.verify_element_present('#double-click-one')
    golem_steps.assert_last_step_message('Verify element #double-click-one is present')
    actions.verify_element_present('#does-not-exist')
    golem_steps.assert_last_error('element #does-not-exist is not present')
