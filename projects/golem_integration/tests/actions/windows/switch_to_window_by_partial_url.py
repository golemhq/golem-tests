from golem import actions

from projects.golem_integration.pages import golem_steps
from projects.golem_integration.utils import expected_exception


description = 'Verify switch_to_window_by_partial_url action'

def test(data):
    actions.navigate(data.env.url + 'tabs/')
    actions.send_keys('#urlInput', '/elements/')
    actions.click("#goButton")
    actions.switch_to_window_by_partial_url('elem')
    golem_steps.assert_last_step_message("Switch to window with partial URL 'elem'")
    actions.verify_title('Web Playground - Elements')
    actions.switch_to_window_by_partial_url('tabs/')
    actions.verify_title('Web Playground - Tabs')
    msg = "Window with partial URL 'xyz' was not found"
    with expected_exception(Exception, msg):
        actions.switch_to_window_by_partial_url('xyz')
