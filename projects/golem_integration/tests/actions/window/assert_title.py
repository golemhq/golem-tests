from golem import actions

from projects.golem_integration.pages import golem_steps
from projects.golem_integration.utils import expected_exception


description = 'assert_title action'

def test(data):
    actions.navigate(data.env.url+'elements/')
    actions.assert_title('Web Playground - Elements')
    golem_steps.assert_last_step_message("Assert page title is 'Web Playground - Elements'")
    msg = "expected title to be 'incorrect title' but was 'Web Playground - Elements'"
    with expected_exception(AssertionError, msg):
        actions.assert_title('incorrect title')
