from golem import actions

from projects.golem_integration.pages import golem_steps
from projects.golem_integration.utils import expected_exception


description = 'assert_element_value_is_not'


def test(data):
    input_one = '#input-one'
    actions.navigate(data.env.url+'elements/')
    actions.assert_element_value_is_not(input_one, 'foo')
    expected = "Assert element {} value is not 'foo'".format(input_one)
    golem_steps.assert_last_step_message(expected)
    actions.send_keys(input_one, 'alfa')
    actions.assert_element_value_is_not(input_one, 'bravo')
    msg = ("expected element {} value to not be 'alfa'".format(input_one))
    with expected_exception(AssertionError, msg):
        actions.assert_element_value_is_not(input_one, 'alfa')
