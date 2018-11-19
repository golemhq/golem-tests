from golem import actions

from projects.golem_integration.pages import golem_steps
from projects.golem_integration.utils import expected_exception


description = 'Verify switch_to_window_by_title action'

def test(data):
    actions.navigate(data.env.url+'tabs/')
    actions.send_keys('#urlInput', '/elements/')
    actions.click("#goButton")
    actions.wait_for_window_present_by_title('Web Elements - Elements', timeout=3)
    actions.switch_to_window_by_title('Web Playground - Elements')
    golem_steps.assert_last_step_message("Switch to window with title 'Web Playground - Elements'")
    actions.verify_title('Web Playground - Elements')
    msg = "Window with title 'incorrect title' was not found"
    with expected_exception(Exception, msg):
        actions.switch_to_window_by_title('incorrect title')
