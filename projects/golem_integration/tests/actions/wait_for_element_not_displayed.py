from golem import actions


description = 'Verify wait_for_element_not_displayed action'

def test(data):
    actions.navigate(data.env.url+'dynamic-elements/?delay=3')
    button = '#button-two'
    actions.wait_for_element_not_displayed(button, timeout=5)
    actions.verify_element_not_displayed(button)
    # time out waiting for element to be not displayed
    actions.navigate(data.env.url + 'dynamic-elements/?delay=5')
    try:
        actions.wait_for_element_not_displayed(button, timeout=3)
        assert False, 'Expected Exception'
    except Exception as e:
        expected = ("Timeout waiting for element {} to be not displayed"
                    .format(button))
        assert expected in e.args[0]
