from golem import actions

from projects.golem_integration.utils import expected_exception


description = 'Verify webelement.wait_text_contains method'

def test(data):
    browser = actions.get_browser()
    actions.navigate(data.env.url+'dynamic-elements/?delay=3')
    element = '#button-seven'
    browser.find(element).wait_text_contains('New', timeout=5)
    actions.navigate(data.env.url + 'dynamic-elements/?delay=5')
    msg = "Timeout waiting for element #button-seven text to contain 'New'"
    with expected_exception(Exception, msg):
        browser.find(element).wait_text_contains('New', timeout=3)
