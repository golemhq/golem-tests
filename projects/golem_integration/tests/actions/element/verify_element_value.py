from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'verify_element_value'


def test(data):
    input_one = '#input-one'
    actions.navigate(data.env.url+'elements/')
    actions.send_keys(input_one, 'foo')
    actions.verify_element_value(input_one, 'foo')
    expected = "Verify element {} value is 'foo'".format(input_one)
    golem_steps.assert_last_step_message(expected)
    actions.verify_element_value(input_one, 'bar')
    msg = ("expected element {} value to be 'bar' but was 'foo'".format(input_one))
    golem_steps.assert_last_error(msg)
