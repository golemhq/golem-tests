from golem import actions

from projects.golem_integration.pages import golem_steps
from projects.golem_integration.utils import expected_exception


description = 'assert_cookie_present action'

def test(data):
    actions.navigate(data.env.url)
    cookie = {'name': 'foo', 'value': 'bar'}
    actions.add_cookie(cookie)
    actions.assert_cookie_present('foo')
    assert golem_steps.get_last_step_message() == "Assert that cookie 'foo' exists"
    with expected_exception(AssertionError, "cookie 'not_exists' was not found"):
        actions.assert_cookie_present('not_exists')
