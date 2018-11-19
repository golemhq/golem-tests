from golem import actions

from projects.golem_integration.pages import golem_steps
from projects.golem_integration.utils import expected_exception


description = 'assert_element_present action'

def test(data):
    actions.navigate(data.env.url+'elements/')
    actions.assert_element_text('#link1', 'this is a link to index')
    golem_steps.assert_last_step_message("Assert element #link1 text is 'this is a link to index'")
    msg = ("expected element #link1 text to be 'incorrect text' but "
           "was 'this is a link to index'")
    with expected_exception(AssertionError, msg):
        actions.assert_element_text('#link1', 'incorrect text')
