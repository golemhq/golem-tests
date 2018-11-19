from golem import actions

from projects.golem_integration.utils import expected_exception


description = 'Verify webdriver.wait_for_element_enabled method'

def test(data):
    actions.navigate(data.env.url+'dynamic-elements/?delay=3')
    actions.wait_for_element_enabled('#button-three', 10)
    actions.verify_element_enabled('#button-three')
    actions.navigate(data.env.url + 'dynamic-elements/?delay=5')
    msg = "Timeout waiting for element #button-three to be enabled"
    with expected_exception(Exception, msg):
        actions.get_browser().wait_for_element_enabled('#button-three', timeout=3)
