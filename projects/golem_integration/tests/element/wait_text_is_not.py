from golem import actions

from projects.golem_integration.utils import expected_exception


description = 'Verify webelement.wait_text_is_not method'

def test(data):
    browser = actions.get_browser()
    actions.navigate(data.env.url+'dynamic-elements/?delay=3')
    element = '#button-seven'
    browser.find(element).wait_text_is_not('Initial Text', timeout=10)
    actions.navigate(data.env.url + 'dynamic-elements/?delay=5')
    msg = "Timeout waiting for element #button-seven text not to be 'Initial Text'"
    with expected_exception(Exception, msg):
        browser.find(element).wait_text_is_not('Initial Text', 3)
