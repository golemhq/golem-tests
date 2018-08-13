from golem import actions


description = 'Verify webdriver.wait_for_element_not_enabled method'

def test(data):
    actions.navigate(data.env.url+'dynamic-elements/?delay=3')
    actions.wait_for_element_not_enabled('#button-four', timeout=5)
    actions.verify_element_not_enabled('#button-four')
    actions.navigate(data.env.url + 'dynamic-elements/?delay=5')
    try:
        actions.get_browser().wait_for_element_not_enabled('#button-four', timeout=3)
        assert False, 'Expected Exception'
    except Exception as e:
        assert "Timeout waiting for element #button-four to be not enabled" in e.args[0]
