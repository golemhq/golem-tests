from golem import actions

from projects.golem_integration.pages import golem_steps
from projects.golem_integration.utils import expected_exception


description = 'assert_element_attribute_is_not action'

def test(data):
    actions.navigate(data.env.url+'elements/')
    actions.assert_element_attribute_is_not('#button-one', 'id', 'incorrect')
    expected = "Assert element #button-one attribute id value is not incorrect"
    golem_steps.assert_last_step_message(expected)
    msg = "expected element #button-one attribute id value to not be button-one"
    with expected_exception(AssertionError, msg):
        actions.assert_element_attribute_is_not('#button-one', 'id', 'button-one')
