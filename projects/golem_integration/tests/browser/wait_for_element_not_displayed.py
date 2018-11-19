from golem import actions
from golem.core.exceptions import ElementNotFound

from projects.golem_integration.utils import expected_exception


description = 'Verify webdriver.wait_for_element_not_displayed method'

def test(data):
    actions.navigate(data.env.url+'dynamic-elements/?delay=3')
    button = '#button-two'
    actions.get_browser().wait_for_element_not_displayed(button, timeout=5)
    actions.verify_element_not_displayed(button)
    # time out waiting for element to be not displayed
    actions.navigate(data.env.url + 'dynamic-elements/?delay=5')
    msg = 'Timeout waiting for element {} to be not displayed'.format(button)
    with expected_exception(Exception, msg):
        actions.get_browser().wait_for_element_not_displayed(button, timeout=3)
    # element is not displayed from the beginning
    # wait_for_element_not_displayed is ignored
    button = '#hidden-button'
    actions.navigate(data.env.url + 'special-elements/')
    actions.assert_element_not_displayed(button)
    actions.get_browser().wait_for_element_not_displayed(button, timeout=2)
    # element is not present
    # wait_for_element_not_displayed throws ElementNotFound
    with expected_exception(ElementNotFound):
        actions.get_browser().wait_for_element_not_displayed('#non-existent', timeout=2)

