from golem import actions

from projects.golem_integration.utils import expected_exception


description = 'Verify webdriver.wait_for_element_text_is_not method'

def test(data):
    actions.navigate(data.env.url+'dynamic-elements/?delay=3')
    actions.get_browser().wait_for_element_text_is_not('#button-seven', 'Initial Text', 10)
    actions.navigate(data.env.url + 'dynamic-elements/?delay=5')
    msg = "Timeout waiting for element #button-seven text not to be 'Initial Text'"
    with expected_exception(Exception, msg):
        actions.get_browser().wait_for_element_text_is_not('#button-seven', 'Initial Text', 3)
