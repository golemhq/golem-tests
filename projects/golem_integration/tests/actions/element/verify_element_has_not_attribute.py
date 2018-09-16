from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'verify_verify_element_has_not_attribute action'

def test(data):
    actions.navigate(data.env.url+'elements/')
    actions.verify_element_has_not_attribute('#button-one', 'not-this-one')
    golem_steps.assert_last_step_message('Verify element #button-one has not attribute not-this-one')
    actions.verify_element_has_not_attribute('#button-one', 'onclick')
    golem_steps.assert_last_error('element #button-one has attribute onclick')
