from selenium.common.exceptions import TimeoutException
from golem import actions

from projects.golem_integration.pages import golem_steps
from projects.golem_integration.utils import expected_exception


description = 'Verify wait_for_element_present action'

def test(data):
    actions.navigate(data.env.url+'dynamic-elements/?delay=3')
    actions.wait_for_element_present('#button-five', 10)
    golem_steps.assert_last_step_message('Wait for element #button-five to be present')
    actions.verify_element_present('#button-five')
    actions.navigate(data.env.url + 'dynamic-elements/?delay=5')
    msg = "timeout waiting for element #button-five to be present"
    with expected_exception(TimeoutException, msg):
        actions.wait_for_element_present('#button-five', 3)
