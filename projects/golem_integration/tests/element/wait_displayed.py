from golem import actions


description = 'Verify webelement.wait_displayed method'

def test(data):
    actions.navigate(data.env.url+'dynamic-elements/?delay=3')
    browser = actions.get_browser()
    button = browser.find('#button-one')
    button.wait_displayed(timeout=5)
    assert button.is_displayed()
    # time out waiting for element to be displayed
    actions.navigate(data.env.url + 'dynamic-elements/?delay=5')
    try:
        browser.find('#button-one').wait_displayed(timeout=3)
        assert False, 'Expected Exception'
    except Exception as e:
        expected = "Timeout waiting for element #button-one to be displayed"
        assert expected in e.args[0]
