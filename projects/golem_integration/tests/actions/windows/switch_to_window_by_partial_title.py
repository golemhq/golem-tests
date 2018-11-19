from golem import actions

from projects.golem_integration.pages import golem_steps
from projects.golem_integration.utils import expected_exception


description = 'Verify switch_to_window_by_partial_title action'

def test(data):
    actions.navigate(data.env.url+'tabs/')
    actions.send_keys('#urlInput', '/elements/')
    actions.click("#goButton")
    actions.switch_to_window_by_partial_title('Ele')
    golem_steps.assert_last_step_message("Switch to window with partial title 'Ele'")
    actions.verify_title('Web Playground - Elements')
    msg = "Window with partial title 'incorrect title' was not found"
    with expected_exception(Exception, msg):
        actions.switch_to_window_by_partial_title('incorrect title')
