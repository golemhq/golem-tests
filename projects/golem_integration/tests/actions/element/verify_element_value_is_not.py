from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'verify_element_value_is_not'


def test(data):
    input_one = '#input-one'
    actions.navigate(data.env.url+'elements/')
    actions.send_keys(input_one, 'foo')
    actions.verify_element_value_is_not(input_one, 'bar')
    expected = "Verify element {} value is not 'bar'".format(input_one)
    golem_steps.assert_last_step_message(expected)
    actions.verify_element_value_is_not(input_one, 'foo')
    msg = ("expected element {} value to not be 'foo'".format(input_one))
    golem_steps.assert_last_error(msg)
