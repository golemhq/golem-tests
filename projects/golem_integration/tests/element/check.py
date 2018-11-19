from golem import actions

from projects.golem_integration.utils import expected_exception


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
    msg = 'Element #button-one is not checkbox or radiobutton'
    with expected_exception(Exception, msg):
        browser.find('#button-one').check()
