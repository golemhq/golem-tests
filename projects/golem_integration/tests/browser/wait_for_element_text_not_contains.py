from golem import actions

from projects.golem_integration.utils import expected_exception


description = 'Verify webdriver.wait_for_element_text_not_contains method'

def test(data):
    actions.navigate(data.env.url+'dynamic-elements/?delay=3')
    actions.get_browser().wait_for_element_text_not_contains('#button-seven', 'Initial', 5)
    actions.navigate(data.env.url + 'dynamic-elements/?delay=5')
    msg = "Timeout waiting for element #button-seven text to not contain 'Initial'"
    with expected_exception(Exception, msg):
        actions.get_browser().wait_for_element_text_not_contains('#button-seven', 'Initial', 3)
