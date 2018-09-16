from selenium.common.exceptions import TimeoutException
from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'Verify wait_for_element_has_attribute action'

def test(data):
    actions.navigate(data.env.url+'dynamic-elements/?delay=3')
    element = '#button-height'
    attribute = 'verified'
    actions.verify_element_has_not_attribute(element, attribute)
    actions.wait_for_element_has_attribute(element, attribute, 5)
    golem_steps.assert_last_step_message('Wait for element #button-height to have verified attribute')
    actions.verify_element_has_attribute(element, attribute)
    actions.navigate(data.env.url + 'dynamic-elements/?delay=5')
    try:
        actions.wait_for_element_has_attribute(element, attribute, 3)
        assert False, 'Expected Exception'
    except TimeoutException as e:
        exp = "Timeout waiting for element {} to have attribute {}".format(element, attribute)
        assert exp in e.args[0]
