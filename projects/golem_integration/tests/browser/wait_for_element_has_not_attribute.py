from golem import actions

from projects.golem_integration.utils import expected_exception


description = 'Verify webdriver.wait_for_element_has_not_attribute method'

def test(data):
    actions.navigate(data.env.url+'dynamic-elements/?delay=3')
    element = '#button-nine'
    attribute = 'verified'
    actions.verify_element_has_attribute(element, attribute)
    actions.get_browser().wait_for_element_has_not_attribute(element, attribute, 5)
    actions.verify_element_has_not_attribute(element, attribute)
    actions.navigate(data.env.url + 'dynamic-elements/?delay=5')
    msg = "Timeout waiting for element {} to not have attribute {}".format(element, attribute)
    with expected_exception(Exception, msg):
        actions.get_browser().wait_for_element_has_not_attribute(element, attribute, 3)
