from golem import actions

from projects.golem_integration.utils import expected_exception


description = 'Verify webdriver.wait_for_element_text_contains method'

def test(data):
    actions.navigate(data.env.url+'dynamic-elements/?delay=3')
    actions.get_browser().wait_for_element_text_contains('#button-seven', 'New', 5)
    actions.navigate(data.env.url + 'dynamic-elements/?delay=5')
    msg = "Timeout waiting for element #button-seven text to contain 'New'"
    with expected_exception(Exception, msg):
        actions.get_browser().wait_for_element_text_contains('#button-seven', 'New', 3)
