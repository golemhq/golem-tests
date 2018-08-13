from golem import actions


description = 'Verify webdriver.wait_for_element_text method'

def test(data):
    actions.navigate(data.env.url+'dynamic-elements/?delay=3')
    actions.get_browser().wait_for_element_text('#button-seven', 'New Text', 10)
    actions.navigate(data.env.url + 'dynamic-elements/?delay=5')
    try:
        actions.get_browser().wait_for_element_text('#button-seven', 'New Text', 3)
        assert False, 'Expected Exception'
    except Exception as e:
        assert "Timeout waiting for element #button-seven text to be 'New Text'" in e.args[0]
