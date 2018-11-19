from golem import actions

from projects.golem_integration.utils import expected_exception


description = 'Verify webelement.wait_not_enabled method'

def test(data):
    actions.navigate(data.env.url+'dynamic-elements/?delay=3')
    browser = actions.get_browser()
    button = browser.find('#button-four')
    button.wait_not_enabled(timeout=5)
    assert not button.is_enabled()
    actions.navigate(data.env.url + 'dynamic-elements/?delay=5')
    msg = "Timeout waiting for element #button-four to be not enabled"
    with expected_exception(Exception, msg):
        browser.find('#button-four').wait_not_enabled(timeout=3)
