from selenium.common.exceptions import TimeoutException
from golem import actions

from projects.golem_integration.pages import golem_steps
from projects.golem_integration.utils import expected_exception


description = 'Verify wait_for_element_has_not_attribute action'

def test(data):
    actions.navigate(data.env.url+'dynamic-elements/?delay=3')
    element = '#button-nine'
    attribute = 'verified'
    actions.verify_element_has_attribute(element, attribute)
    actions.wait_for_element_has_not_attribute(element, attribute, 5)
    golem_steps.assert_last_step_message('Wait for element #button-nine to not have verified attribute')
    actions.verify_element_has_not_attribute(element, attribute)
    actions.navigate(data.env.url + 'dynamic-elements/?delay=5')
    msg = "Timeout waiting for element {} to not have attribute {}".format(element, attribute)
    with expected_exception(TimeoutException, msg):
        actions.wait_for_element_has_not_attribute(element, attribute, 3)
