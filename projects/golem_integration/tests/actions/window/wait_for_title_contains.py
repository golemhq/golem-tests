from selenium.common.exceptions import TimeoutException
from golem import actions

from projects.golem_integration.pages import golem_steps
from projects.golem_integration.utils import expected_exception


description = 'Verify wait_for_title_contains action'

def test(data):
    actions.navigate(data.env.url+'dynamic-elements/?delay=3')
    actions.verify_title('Dynamic Elements')
    actions.click('#change-title-button')
    actions.wait_for_title_contains('New', 5)
    golem_steps.assert_last_step_message("Wait for title to contain 'New'")
    actions.verify_title_contains('New')
    actions.navigate(data.env.url + 'dynamic-elements/?delay=5')
    with expected_exception(TimeoutException, "Timeout waiting for title to contain 'New'"):
        actions.click('#change-title-button')
        actions.wait_for_title_contains('New', 5)
