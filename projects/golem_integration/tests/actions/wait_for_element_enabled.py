from golem import actions


description = 'Verify wait_for_element_enabled action'

def test(data):
    actions.navigate(data.env.url+'dynamic-elements/?delay=3')
    actions.wait_for_element_enabled('#button-three', 10)
    actions.verify_element_enabled('#button-three')
    actions.navigate(data.env.url + 'dynamic-elements/?delay=5')
    try:
        actions.wait_for_element_enabled('#button-three', 3)
    except Exception as e:
        assert "Timeout waiting for element #button-three to be enabled" in e.args[0]
