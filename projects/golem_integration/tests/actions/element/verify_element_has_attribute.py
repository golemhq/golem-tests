from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'verify_element_has_attribute action'

def test(data):
    actions.navigate(data.env.url+'elements/')
    actions.verify_element_has_attribute('#button-one', 'onclick')
    golem_steps.assert_last_step_message('Verify element #button-one has attribute onclick')
    actions.verify_element_has_attribute('#button-one', 'not-this-one')
    golem_steps.assert_last_error('element #button-one does not have attribute not-this-one')

