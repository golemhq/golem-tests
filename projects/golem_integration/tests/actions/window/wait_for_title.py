from selenium.common.exceptions import TimeoutException
from golem import actions

from projects.golem_integration.pages import golem_steps
from projects.golem_integration.utils import expected_exception


description = 'Verify wait_for_title action'

def test(data):
    actions.navigate(data.env.url+'dynamic-elements/?delay=3')
    actions.verify_title('Web Playground - Dynamic Elements')
    actions.click('#change-title-button')
    actions.wait_for_title('New Title', 5)
    golem_steps.assert_last_step_message("Wait for title to be 'New Title'")
    actions.verify_title('New Title')
    actions.navigate(data.env.url + 'dynamic-elements/?delay=5')
    with expected_exception(TimeoutException, "Timeout waiting for title to be 'New Title'"):
        actions.click('#change-title-button')
        actions.wait_for_title('New Title', 5)
