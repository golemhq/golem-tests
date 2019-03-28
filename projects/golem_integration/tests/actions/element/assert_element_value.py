from golem import actions

from projects.golem_integration.pages import golem_steps
from projects.golem_integration.utils import expected_exception


description = 'assert_element_value'


def test(data):
    input_one = '#input-one'
    actions.navigate(data.env.url+'elements/')
    actions.assert_element_value(input_one, '')
    expected = "Assert element {} value is ''".format(input_one)
    golem_steps.assert_last_step_message(expected)
    actions.send_keys(input_one, 'foo')
    actions.assert_element_value(input_one, 'foo')
    msg = ("expected element {} value to be 'bar' but was 'foo'".format(input_one))
    with expected_exception(AssertionError, msg):
        actions.assert_element_value(input_one, 'bar')
