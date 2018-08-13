from golem import actions


description = 'Verify webdriver.wait_for_element_not_present method'

def test(data):
    browser = actions.get_browser()
    actions.navigate(data.env.url+'dynamic-elements/?delay=3')
    actions.verify_element_present('#button-six')
    browser.wait_for_element_not_present('#button-six', timeout=10)
    actions.verify_element_not_present('#button-six')
    # when element does not exist no exception is thrown
    browser.wait_for_element_not_present('#this-element-does-not-exist', timeout=3)
    # pass a webelement object to the method
    actions.navigate(data.env.url + 'dynamic-elements/?delay=5')
    actions.verify_element_present('#button-six')
    button = browser.find('#button-six', timeout=0)
    browser.wait_for_element_not_present(button, timeout=10)
    # wait times out and element is still present
    actions.navigate(data.env.url + 'elements/')
    try:
        browser.wait_for_element_not_present('#button-one', timeout=3)
        assert False, 'Expected Exception'
    except Exception as e:
        assert "Timeout waiting for element #button-one to not be present" in e.args[0]
