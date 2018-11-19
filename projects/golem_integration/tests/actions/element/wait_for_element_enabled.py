from selenium.common.exceptions import TimeoutException
from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'Verify wait_for_element_enabled action'

def test(data):
    actions.navigate(data.env.url+'dynamic-elements/?delay=3')
    actions.wait_for_element_enabled('#button-three', 10)
    golem_steps.assert_last_step_message('Wait for element #button-three to be enabled')
    actions.verify_element_enabled('#button-three')
    actions.navigate(data.env.url + 'dynamic-elements/?delay=5')
    try:
        actions.wait_for_element_enabled('#button-three', 3)
        assert False, 'Expected Exception'
    except TimeoutException as e:
        assert "Timeout waiting for element #button-three to be enabled" in e.args[0]
