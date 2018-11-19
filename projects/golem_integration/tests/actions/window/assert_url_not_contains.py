from golem import actions

from projects.golem_integration.pages import golem_steps
from projects.golem_integration.utils import expected_exception


description = 'assert_url_not_contains action'

def test(data):
    url = data.env.url + 'elements/'
    actions.navigate(url)
    actions.assert_url_not_contains('incorrect')
    golem_steps.assert_last_step_message("Assert page title does not contain 'incorrect'")
    msg = "expected URL '{}' to not contain 'elem'".format(url)
    with expected_exception(AssertionError, msg):
        actions.assert_url_not_contains('elem')
