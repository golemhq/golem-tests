from golem import actions


description = 'Verify webelement.wait_text_contains method'

def test(data):
    browser = actions.get_browser()
    actions.navigate(data.env.url+'dynamic-elements/?delay=3')
    element = '#button-seven'
    browser.find(element).wait_text_contains('New', timeout=5)
    actions.navigate(data.env.url + 'dynamic-elements/?delay=5')
    try:
        browser.find(element).wait_text_contains('New', timeout=3)
        assert False, 'Expected Exception'
    except Exception as e:
        assert "Timeout waiting for element #button-seven text to contain 'New'" in e.args[0]
