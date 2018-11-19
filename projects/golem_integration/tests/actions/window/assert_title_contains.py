from golem import actions

from projects.golem_integration.pages import golem_steps
from projects.golem_integration.utils import expected_exception


description = 'verify_title_contains action'

def test(data):
    actions.navigate(data.env.url+'elements/')
    actions.assert_title_contains('Elem')
    golem_steps.assert_last_step_message("Assert page title contains 'Elem'")
    with expected_exception(AssertionError, "expected title to contain 'incorrect'"):
        actions.assert_title_contains('incorrect')
