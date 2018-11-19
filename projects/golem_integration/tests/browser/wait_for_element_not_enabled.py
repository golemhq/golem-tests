from golem import actions

from projects.golem_integration.utils import expected_exception


description = 'Verify webdriver.wait_for_element_not_enabled method'

def test(data):
    actions.navigate(data.env.url+'dynamic-elements/?delay=3')
    actions.wait_for_element_not_enabled('#button-four', timeout=5)
    actions.verify_element_not_enabled('#button-four')
    actions.navigate(data.env.url + 'dynamic-elements/?delay=5')
    msg = 'Timeout waiting for element #button-four to be not enabled'
    with expected_exception(Exception, msg):
        actions.get_browser().wait_for_element_not_enabled('#button-four', timeout=3)
