from golem import actions

from projects.golem_integration.pages import golem_steps
from projects.golem_integration.utils import expected_exception


description = 'assert_url_contains action'

def test(data):
    actions.navigate(data.env.url+'elements/')
    actions.assert_url_contains('elements')
    golem_steps.assert_last_step_message("Assert URL contains 'elements'")
    with expected_exception(AssertionError, "expected URL to contain 'incorrect'"):
        actions.assert_url_contains('incorrect')
