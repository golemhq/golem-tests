from golem import actions


description = 'Verify webelement.wait_has_attribute method'

def test(data):
    actions.navigate(data.env.url+'dynamic-elements/?delay=3')
    browser = actions.get_browser()
    element = '#button-height'
    attribute = 'verified'
    actions.verify_element_has_not_attribute(element, attribute)
    browser.find(element).wait_has_attribute(attribute, timeout=5)
    actions.verify_element_has_attribute(element, attribute)
    actions.navigate(data.env.url + 'dynamic-elements/?delay=5')
    try:
        browser.find(element).wait_has_attribute(attribute, timeout=3)
        assert False, 'Expected Exception'
    except Exception as e:
        assert "Timeout waiting for element {} to have attribute {}".format(element, attribute) in e.args[0]
