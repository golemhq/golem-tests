from selenium.common.exceptions import TimeoutException
from golem import actions

from projects.golem_integration.pages import golem_steps
from projects.golem_integration.utils import expected_exception


description = 'Verify wait_for_element_not_enabled action'

def test(data):
    actions.navigate(data.env.url+'dynamic-elements/?delay=3')
    actions.wait_for_element_not_enabled('#button-four', timeout=5)
    golem_steps.assert_last_step_message('Wait for element #button-four to be not enabled')
    actions.verify_element_not_enabled('#button-four')
    actions.navigate(data.env.url + 'dynamic-elements/?delay=5')
    msg = "Timeout waiting for element #button-four to be not enabled"
    with expected_exception(TimeoutException, msg):
        actions.wait_for_element_not_enabled('#button-four', timeout=3)
