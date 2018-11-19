from golem import actions

from projects.golem_integration.pages import golem_steps
from projects.golem_integration.utils import expected_exception


description = 'assert_page_contains_text action'

def test(data):
    actions.navigate(data.env.url+'special-elements/')
    actions.verify_page_contains_text('Special Elements')
    golem_steps.assert_last_step_message("Verify 'Special Elements' is present in page")
    msg = "text 'THIS TEXT IS NOT PRESENT' not found in page"
    with expected_exception(AssertionError, msg):
        actions.assert_page_contains_text('THIS TEXT IS NOT PRESENT')
