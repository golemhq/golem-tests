from golem import actions

from projects.golem_integration.pages import golem_steps
from projects.golem_integration.utils import expected_exception


description = 'assert_page_not_contains_text action'

def test(data):
    actions.navigate(data.env.url+'special-elements/')
    actions.assert_page_not_contains_text('THIS TEXT IS NOT PRESENT')
    golem_steps.assert_last_step_message("Assert 'THIS TEXT IS NOT PRESENT' is not present in the page")
    msg = "text 'Special Elements' was found in the page"
    with expected_exception(AssertionError, msg):
        actions.assert_page_not_contains_text('Special Elements')
