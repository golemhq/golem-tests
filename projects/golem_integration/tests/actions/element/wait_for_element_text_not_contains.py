from selenium.common.exceptions import TimeoutException
from golem import actions

from projects.golem_integration.pages import golem_steps
from projects.golem_integration.utils import expected_exception


description = 'Verify wait_for_element_text_not_contains action'

def test(data):
    actions.navigate(data.env.url+'dynamic-elements/?delay=3')
    actions.wait_for_element_text_not_contains('#button-seven', 'Initial', 5)
    msg = "Wait for element #button-seven to not contain text 'Initial'"
    golem_steps.assert_last_step_message(msg)
    actions.navigate(data.env.url + 'dynamic-elements/?delay=5')
    msg = "Timeout waiting for element #button-seven text to not contain 'Initial'"
    with expected_exception(TimeoutException, msg):
        actions.wait_for_element_text_not_contains('#button-seven', 'Initial', 3)
