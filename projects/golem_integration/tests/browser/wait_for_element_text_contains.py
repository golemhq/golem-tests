from golem import actions


description = 'Verify webdriver.wait_for_element_text_contains method'

def test(data):
    actions.navigate(data.env.url+'dynamic-elements/?delay=3')
    actions.get_browser().wait_for_element_text_contains('#button-seven', 'New', 5)
    actions.navigate(data.env.url + 'dynamic-elements/?delay=5')
    try:
        actions.get_browser().wait_for_element_text_contains('#button-seven', 'New', 3)
        assert False, 'Expected Exception'
    except Exception as e:
        assert "Timeout waiting for element #button-seven text to contain 'New'" in e.args[0]
