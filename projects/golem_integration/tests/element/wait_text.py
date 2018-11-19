from golem import actions

from projects.golem_integration.utils import expected_exception


description = 'Verify webelement.wait_text method'

def test(data):
    browser = actions.get_browser()
    browser.navigate(data.env.url+'dynamic-elements/?delay=3')
    element = '#button-seven'
    browser.find(element).wait_text('New Text', timeout=10)
    actions.navigate(data.env.url + 'dynamic-elements/?delay=5')
    msg = "Timeout waiting for element #button-seven text to be 'New Text'"
    with expected_exception(Exception, msg):
        browser.find(element).wait_text('New Text', 3)
