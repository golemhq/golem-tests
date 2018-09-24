from golem import actions

from projects.golem_integration.utils import expected_exception


description = 'Verify webelement.wait_text_not_contains method'

def test(data):
    actions.navigate(data.env.url+'dynamic-elements/?delay=3')
    browser = actions.get_browser()
    element = '#button-seven'
    browser.find(element).wait_text_not_contains('Initial', timeout=5)
    actions.navigate(data.env.url + 'dynamic-elements/?delay=5')
    msg = "Timeout waiting for element #button-seven text to not contain 'Initial'"
    with expected_exception(Exception, msg):
        browser.find(element).wait_text_not_contains('Initial', timeout=3)
