from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'verify_element_attribute action'

def test(data):
    actions.navigate(data.env.url+'elements/')
    actions.verify_element_attribute('#input-one', 'class', 'form-control')
    expected = "Verify the element #input-one attribute class value is 'form-control'"
    golem_steps.assert_last_step_message(expected)
    actions.verify_element_attribute('#input-one', 'class', 'incorrect')
    expected = "expected element #input-one attribute class to be 'incorrect' but was 'form-control'"
    golem_steps.assert_last_error(expected)
