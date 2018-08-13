from golem import actions


description = 'Verify wait_for_element_text_is_not action'

def test(data):
    actions.navigate(data.env.url+'dynamic-elements/?delay=3')
    actions.wait_for_element_text_is_not('#button-seven', 'Initial Text', 10)
    actions.navigate(data.env.url + 'dynamic-elements/?delay=5')
    try:
        actions.wait_for_element_text_is_not('#button-seven', 'Initial Text', 3)
        assert False, 'Expected Exception'
    except Exception as e:
        assert "Timeout waiting for element #button-seven text not to be 'Initial Text'" in e.args[0]
