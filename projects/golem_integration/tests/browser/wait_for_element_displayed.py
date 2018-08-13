from golem import actions


description = 'Verify webdriver.wait_for_element_displayed method'

def test(data):
    actions.navigate(data.env.url+'dynamic-elements/?delay=3')
    actions.wait_for_element_displayed('#button-one', timeout=5)
    actions.verify_element_displayed('#button-one')
    # time out waiting for element to be displayed
    actions.navigate(data.env.url + 'dynamic-elements/?delay=5')
    try:
        actions.wait_for_element_displayed('#button-one', timeout=3)
        assert False, 'Expected Exception'
    except Exception as e:
        expected = "Timeout waiting for element #button-one to be displayed"
        assert expected in e.args[0]
