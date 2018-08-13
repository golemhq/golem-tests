from golem import actions


description = 'Verify wait_for_element_has_not_attribute action'

def test(data):
    actions.navigate(data.env.url+'dynamic-elements/?delay=3')
    element = '#button-nine'
    attribute = 'verified'
    actions.verify_element_has_attribute(element, attribute)
    actions.wait_for_element_has_not_attribute(element, attribute, 5)
    actions.verify_element_has_not_attribute(element, attribute)
    actions.navigate(data.env.url + 'dynamic-elements/?delay=5')
    try:
        actions.wait_for_element_has_not_attribute(element, attribute, 3)
        assert False, 'Expected Exception'
    except Exception as e:
        assert "Timeout waiting for element {} to not have attribute {}".format(element, attribute) in e.args[0]
