from golem import actions

from projects.golem_integration.pages import golem_steps
from projects.golem_integration.utils import expected_exception


description = 'assert_element_text_not_contains action'

def test(data):
    actions.navigate(data.env.url+'elements/')
    actions.assert_element_text_not_contains('#link1', 'not-contained')
    golem_steps.assert_last_step_message("Assert element #link1 does not contain text 'not-contained'")
    msg = "element #link1 text 'this is a link to index' contains text 'this is a link'"
    with expected_exception(AssertionError, msg):
        actions.assert_element_text_not_contains('#link1', 'this is a link')
