from golem import actions

from projects.golem_integration.pages import golem_steps
from projects.golem_integration.utils import expected_exception


description = 'Verify window_present_by_title action'

def test(data):
    actions.navigate(data.env.url+'tabs/')
    actions.send_keys('#delay', 3)
    actions.send_keys('#title', 'MY TITLE')
    actions.click("#goButtonCustom")
    actions.wait_for_window_present_by_title('MY TITLE', timeout=5)
    golem_steps.assert_last_step_message("Wait for window present by title 'MY TITLE'")
    actions.verify_window_present_by_title('MY TITLE')
    msg = "Timeout waiting for window present by title 'TITLE NOT PRESENT'"
    with expected_exception(Exception, msg):
        actions.wait_for_window_present_by_title('TITLE NOT PRESENT', timeout=2)
