from golem import actions

from projects.golem_integration.pages import golem_steps
from projects.golem_integration.utils import expected_exception


description = 'assert_title_not_contains action'

def test(data):
    actions.navigate(data.env.url+'elements/')
    actions.assert_title_not_contains('incorrect title')
    golem_steps.assert_last_step_message("Assert page title does not contain 'incorrect title'")
    with expected_exception(AssertionError, "title contains 'Elem'"):
        actions.assert_title_not_contains('Elem')
