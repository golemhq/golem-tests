from golem import actions


description = 'Verify webelement.uncheck method'

def test(data):
    actions.navigate(data.env.url + 'elements/')
    browser = actions.get_browser()
    checkbox_checked = browser.find('#selected-checkbox')
    checkbox_not_checked = browser.find('#unselected-checkbox')
    radio_checked = browser.find('#exampleRadios1')
    # checkbox not checked
    actions.verify_element_not_checked(checkbox_not_checked)
    checkbox_not_checked.uncheck()
    actions.verify_element_not_checked(checkbox_not_checked)
    # checkbox already checked
    actions.verify_element_checked(checkbox_checked)
    checkbox_checked.uncheck()
    actions.verify_element_not_checked(checkbox_checked)
    # uncheck a radio button (error)
    actions.verify_element_checked(radio_checked)
    try:
        radio_checked.uncheck()
        assert False, 'Expected Exception'
    except Exception as e:
        assert 'Element #exampleRadios1 is not checkbox' in e.args[0]
    # try to uncheck an element not checkbox
    try:
        actions.get_browser().find('#button-one').uncheck()
        assert False, 'Expected Exception'
    except Exception as e:
        assert 'Element #button-one is not checkbox' in e.args[0]
