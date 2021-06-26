from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'verify_cookie_value action'


def test_verify_cookie_value(data):
    actions.navigate(data.env.url)
    actions.add_cookie({'name': 'foo', 'value': 'bar'})
    actions.verify_cookie_value('foo', 'bar')
    golem_steps.assert_last_step_message("Verify that cookie 'foo' value is 'bar'")
    actions.verify_cookie_value('foo', 'baz')
    expected = "Expected cookie 'foo' value to be 'baz' but was 'bar'"
    golem_steps.assert_last_error(expected)
