from golem import actions

from projects.golem_integration.utils import expected_exception


description = 'Verify webdriver.wait_for_element_present method'

def test(data):
    actions.navigate(data.env.url+'dynamic-elements/?delay=3')
    actions.get_browser().wait_for_element_present('#button-five', 5)
    actions.verify_element_present('#button-five')
    actions.navigate(data.env.url + 'dynamic-elements/?delay=5')
    msg = "timeout waiting for element #button-five to be present"
    with expected_exception(Exception, msg):
        actions.get_browser().wait_for_element_present('#button-five', 3)
