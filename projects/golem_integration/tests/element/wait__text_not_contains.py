from golem import actions


description = 'Verify webelement.wait_text_not_contains method'

def test(data):
    actions.navigate(data.env.url+'dynamic-elements/?delay=3')
    browser = actions.get_browser()
    element = '#button-seven'
    browser.find(element).wait_text_not_contains('Initial', timeout=5)
    actions.navigate(data.env.url + 'dynamic-elements/?delay=5')
    try:
        browser.find(element).wait_text_not_contains('Initial', timeout=3)
        assert False, 'Expected Exception'
    except Exception as e:
        assert "Timeout waiting for element #button-seven text to not contain 'Initial'" in e.args[0]
