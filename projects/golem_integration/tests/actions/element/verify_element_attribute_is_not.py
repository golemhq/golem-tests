from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'verify_element_attribute_is_not action'

def test(data):
    actions.navigate(data.env.url+'elements/')
    actions.verify_element_attribute_is_not('#input-one', 'class', 'this-is-not-correct')
    expected = "Verify element #input-one attribute class value is not 'this-is-not-correct'"
    golem_steps.assert_last_step_message(expected)
    actions.verify_element_attribute_is_not('#input-one', 'class', 'form-control')
    expected = "expected element #input-one attribute class to not be 'form-control'"
    golem_steps.assert_last_error(expected)

