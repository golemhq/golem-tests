from golem import actions


description = 'Verify wait_for_element_displayed action'

def test(data):
    button_selector = '#button-one'
    actions.navigate(data.env.url+'dynamic-elements/?delay=3')
    actions.wait_for_element_displayed(button_selector, timeout=5)
    actions.verify_element_displayed(button_selector)
    # time out waiting for element to be displayed
    actions.navigate(data.env.url + 'dynamic-elements/?delay=5')
    try:
        actions.wait_for_element_displayed(button_selector, timeout=3)
        assert False, 'Expected Exception'
    except Exception as e:
        expected = "Timeout waiting for element #button-one to be displayed"
        assert expected in e.args[0]

    # pass a weblement (the element already exists but
    # is not displayed yet
    actions.navigate(data.env.url + 'dynamic-elements/?delay=5')
    element = actions.get_browser().find(button_selector)
    actions.wait_for_element_displayed(element, timeout=5)
    actions.verify_element_displayed(button_selector)
    # pass a selector of an element that won't exist
    actions.navigate(data.env.url + 'dynamic-elements/?delay=5')
    try:
        actions.wait_for_element_displayed('#thisDoesNotExist', timeout=3)
        assert False, 'Expected Exception'
    except Exception as e:
        assert e.__class__.__name__ == 'ElementNotFound'

