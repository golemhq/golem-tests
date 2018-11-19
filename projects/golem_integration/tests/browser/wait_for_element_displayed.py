from selenium.common.exceptions import TimeoutException
from golem import actions

from projects.golem_integration.utils import expected_exception


description = 'Verify webdriver.wait_for_element_displayed method'

def test(data):
    actions.navigate(data.env.url+'dynamic-elements/?delay=3')
    actions.wait_for_element_displayed('#button-one', timeout=5)
    actions.verify_element_displayed('#button-one')
    # time out waiting for element to be displayed
    actions.navigate(data.env.url + 'dynamic-elements/?delay=5')
    msg = "timeout waiting for element #button-one to be displayed"
    with expected_exception(TimeoutException, msg):
        actions.wait_for_element_displayed('#button-one', timeout=3)
