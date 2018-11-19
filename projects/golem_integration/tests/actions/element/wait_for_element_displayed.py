from selenium.common.exceptions import TimeoutException
from golem.core.exceptions import ElementNotFound
from golem import actions

from projects.golem_integration.pages import golem_steps
from projects.golem_integration.utils import expected_exception


description = 'Verify wait_for_element_displayed action'

def test(data):
    button_selector = '#button-one'
    actions.navigate(data.env.url+'dynamic-elements/?delay=3')
    actions.wait_for_element_displayed(button_selector, timeout=5)
    golem_steps.assert_last_step_message('Wait for element #button-one to be displayed')
    actions.verify_element_displayed(button_selector)
    # time out waiting for element to be displayed
    actions.navigate(data.env.url + 'dynamic-elements/?delay=5')
    msg = "timeout waiting for element #button-one to be displayed"
    with expected_exception(TimeoutException, msg):
        actions.wait_for_element_displayed(button_selector, timeout=3)
    # pass a weblement (the element already exists but
    # is not displayed yet)
    actions.navigate(data.env.url + 'dynamic-elements/?delay=3')
    element = actions.get_browser().find(button_selector)
    actions.wait_for_element_displayed(element, timeout=5)
    actions.verify_element_displayed(button_selector)
    # pass a selector of an element that won't exist
    actions.navigate(data.env.url + 'dynamic-elements/?delay=5')
    with expected_exception(ElementNotFound):
        actions.wait_for_element_displayed('#thisDoesNotExist', timeout=3)
