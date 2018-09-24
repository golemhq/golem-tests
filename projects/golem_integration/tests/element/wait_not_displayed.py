from golem import actions

from projects.golem_integration.utils import expected_exception


description = 'Verify webelement.wait_not_displayed method'

def test(data):
    actions.navigate(data.env.url+'dynamic-elements/?delay=3')
    browser = actions.get_browser()
    button = '#button-two'
    browser.find(button).wait_not_displayed(timeout=5)
    actions.verify_element_not_displayed(button)
    # time out waiting for element to be not displayed
    actions.navigate(data.env.url + 'dynamic-elements/?delay=5')
    msg = "Timeout waiting for element {} to be not displayed".format(button)
    with expected_exception(Exception, msg):
        browser.find(button).wait_not_displayed(timeout=3)
