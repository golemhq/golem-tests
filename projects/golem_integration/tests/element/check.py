from golem import actions

description = 'Verify webelement.check method'

def test(data):
    actions.navigate(data.env.url + 'elements/')
    browser = actions.get_browser()
    checkbox_not_checked = browser.find('#unselected-checkbox')
    checkbox_checked = browser.find('#selected-checkbox')
    radio_not_checked = browser.find('#exampleRadios2')
    # checkbox not checked
    actions.verify_element_not_checked(checkbox_not_checked)
    checkbox_not_checked.check()
    actions.verify_element_checked(checkbox_not_checked)
    # checkbox already checked
    actions.verify_element_checked(checkbox_checked)
    checkbox_checked.check()
    actions.verify_element_checked(checkbox_checked)
    # radio button not checked
    actions.verify_element_not_checked(radio_not_checked)
    radio_not_checked.check()
    actions.verify_element_checked(radio_not_checked)
    radio_checked = radio_not_checked
    # radio button already checked
    radio_checked.check()
    actions.verify_element_checked(radio_checked)
    # try to check an element not radio or checkbox
    try:
        browser.find('#button-one').check()
        assert False, 'Expected Exception'
    except Exception as e:
        assert 'Element #button-one is not checkbox or radiobutton' in e.args[0]
