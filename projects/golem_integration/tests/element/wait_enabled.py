from golem import actions

from projects.golem_integration.utils import expected_exception


description = 'Verify webelement.wait_enabled method'

def test(data):
    actions.navigate(data.env.url+'dynamic-elements/?delay=3')
    browser = actions.get_browser()
    browser.find('#button-three').wait_enabled(timeout=10)
    actions.verify_element_enabled('#button-three')
    actions.navigate(data.env.url + 'dynamic-elements/?delay=5')
    msg = "Timeout waiting for element #button-three to be enabled"
    with expected_exception(Exception, msg):
        browser.find('#button-three').wait_enabled(timeout=3)
