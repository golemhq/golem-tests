from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'verify_element_not_enabled action'

def test(data):
    actions.navigate(data.env.url+'disabled-elements/')
    actions.verify_element_not_enabled('#text')
    golem_steps.assert_last_step_message('Verify element #text is not enabled')
    actions.navigate(data.env.url+'elements/')
    actions.verify_element_not_enabled('#input-one')
    golem_steps.assert_last_error('Element #input-one is enabled')
