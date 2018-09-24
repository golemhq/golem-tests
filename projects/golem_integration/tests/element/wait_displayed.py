from selenium.common.exceptions import TimeoutException
from golem import actions

from projects.golem_integration.utils import expected_exception


description = 'Verify webelement.wait_displayed method'

def test(data):
    actions.navigate(data.env.url+'dynamic-elements/?delay=3')
    browser = actions.get_browser()
    button = browser.find('#button-one', wait_displayed=False)
    button.wait_displayed(timeout=5)
    assert button.is_displayed()
    # time out waiting for element to be displayed
    actions.navigate(data.env.url + 'dynamic-elements/?delay=5')
    msg = "Timeout waiting for element #button-one to be displayed"
    with expected_exception(TimeoutException, msg):
        button = browser.find('#button-one', wait_displayed=False)
        button.wait_displayed(timeout=3)
