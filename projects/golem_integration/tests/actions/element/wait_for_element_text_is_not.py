from selenium.common.exceptions import TimeoutException
from golem import actions

from projects.golem_integration.pages import golem_steps
from projects.golem_integration.utils import expected_exception


description = 'Verify wait_for_element_text_is_not action'

def test(data):
    actions.navigate(data.env.url+'dynamic-elements/?delay=3')
    actions.wait_for_element_text_is_not('#button-seven', 'Initial Text', 10)
    golem_steps.assert_last_step_message("Wait for element #button-seven text to not be 'Initial Text'")
    actions.navigate(data.env.url + 'dynamic-elements/?delay=5')
    msg = "Timeout waiting for element #button-seven text not to be 'Initial Text'"
    with expected_exception(TimeoutException, msg):
        actions.wait_for_element_text_is_not('#button-seven', 'Initial Text', 3)
