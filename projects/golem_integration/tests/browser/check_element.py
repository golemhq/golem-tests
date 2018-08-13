from golem import actions

description = 'Verify webdriver.check_element method'

def test(data):
    actions.navigate(data.env.url + 'elements/')
    browser = actions.get_browser()
    checkbox_not_checked = '#unselected-checkbox'
    checkbox_checked = '#selected-checkbox'
    radio_not_checked = '#exampleRadios2'
    # checkbox not checked
    actions.verify_element_not_checked(checkbox_not_checked)
    browser.check_element(checkbox_not_checked)
    actions.verify_element_checked(checkbox_not_checked)
    # checkbox already checked
    actions.verify_element_checked(checkbox_checked)
    browser.check_element(checkbox_checked)
    actions.verify_element_checked(checkbox_checked)
    # radio button not checked
    actions.verify_element_not_checked(radio_not_checked)
    browser.check_element(radio_not_checked)
    actions.verify_element_checked(radio_not_checked)
    radio_checked = radio_not_checked
    # radio button already checked
    browser.check_element(radio_checked)
    actions.verify_element_checked(radio_checked)
    # try to check an element not radio or checkbox
    try:
        browser.check_element('#button-one')
        assert False, 'Expected Exception'
    except Exception as e:
        assert 'Element #button-one is not checkbox or radiobutton' in e.args[0]
