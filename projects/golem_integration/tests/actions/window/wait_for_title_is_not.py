from selenium.common.exceptions import TimeoutException
from golem import actions

from projects.golem_integration.pages import golem_steps
from projects.golem_integration.utils import expected_exception


description = 'Verify webdriver.wait_for_title_is_not method'

def test(data):
    actions.navigate(data.env.url+'dynamic-elements/?delay=3')
    actions.verify_title('Web Playground - Dynamic Elements')
    actions.click('#change-title-button')
    actions.wait_for_title_is_not('Web Playground - Dynamic Elements', 5)
    golem_steps.assert_last_step_message("Wait for title to not be 'Web Playground - Dynamic Elements'")
    actions.verify_title_is_not('Dynamic Elements')
    actions.navigate(data.env.url + 'elements/')
    with expected_exception(TimeoutException,
                            "Timeout waiting for title to not be 'Web Playground - Elements'"):
        actions.wait_for_title_is_not('Web Playground - Elements', 3)
