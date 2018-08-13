from golem import actions


description = 'Verify webdriver.wait_for_element_has_attribute method'

def test(data):
    actions.navigate(data.env.url+'dynamic-elements/?delay=3')
    element = '#button-height'
    attribute = 'verified'
    actions.verify_element_has_not_attribute(element, attribute)
    actions.get_browser().wait_for_element_has_attribute(element, attribute, 5)
    actions.verify_element_has_attribute(element, attribute)
    actions.navigate(data.env.url + 'dynamic-elements/?delay=5')
    try:
        actions.get_browser().wait_for_element_has_attribute(element, attribute, 3)
        assert False, 'Expected Exception'
    except Exception as e:
        assert "Timeout waiting for element {} to have attribute {}".format(element, attribute) in e.args[0]
