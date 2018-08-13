from golem import actions


description = 'Verify webelement.wait_enabled method'

def test(data):
    actions.navigate(data.env.url+'dynamic-elements/?delay=3')
    browser = actions.get_browser()
    browser.find('#button-three').wait_enabled(timeout=10)
    actions.verify_element_enabled('#button-three')
    actions.navigate(data.env.url + 'dynamic-elements/?delay=5')
    try:
        browser.find('#button-three').wait_enabled(timeout=3)
        assert False, 'Expected Exception'
    except Exception as e:
        assert "Timeout waiting for element #button-three to be enabled" in e.args[0]
