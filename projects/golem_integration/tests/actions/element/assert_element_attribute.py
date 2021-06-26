from golem import actions

from projects.golem_integration.pages import golem_steps
from projects.golem_integration.utils import expected_exception


description = 'assert_element_attribute action'


def test_assert_element_attribute(data):
    actions.navigate(data.env.url+'elements/')
    actions.assert_element_attribute('#button-one', 'id', 'button-one')
    expected = "Assert element #button-one attribute id value is 'button-one'"
    golem_steps.assert_last_step_message(expected)
    msg = ("expected element #button-one attribute id "
           "value to be 'not-this-one' was 'button-one'")
    with expected_exception(AssertionError, msg):
        actions.assert_element_attribute('#button-one', 'id', 'not-this-one')
