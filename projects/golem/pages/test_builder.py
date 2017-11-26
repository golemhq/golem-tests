from golem import actions
from golem.browser import element, elements


test_name = ('id', 'testName', 'Test Name')
description = ('id', 'description', 'Description input')
save_button = ('id', 'save', 'Save button')
import_page_imput = ('css', 'input.page-objects-autocomplete', 'Import Page input')
new_page_button = ('id', 'newPageButton', 'New Page button')

def add_action(action_name):
    """adds an action using the autocomplete list"""
    actions.click('#testSteps button.add-step')
    action_inputs = elements("#testSteps .step-first-input")
    last_input = action_inputs[-1]
    actions.send_keys(last_input, action_name)
    actions.press_key(last_input, 'DOWN')
    actions.press_key(last_input, 'ENTER')


def verify_last_action(action_name):
    action_inputs = elements("#testSteps .step-first-input")
    last_input = action_inputs[-1]
    actions.assert_equals(last_input.get_attribute('value'), action_name)


def verify_description(desc):
    assert element(description).get_attribute('value') == desc


def save_test():
    actions.click(save_button)
    actions.wait_for_element_not_exist('#toast-container')


def import_page(page_name):
    actions.send_keys(import_page_imput, page_name)
    actions.press_key(import_page_imput, 'ENTER')
    actions.wait(10)


def verify_page_in_list(page_name):
    actions.step('Verify that page {} is in the list'.format(page_name))
    imported_pages = elements('#pageObjects>div>input.selected-page')
    for page in imported_pages:
        if page.get_attribute('value') == page_name:
            return
    raise Exception('Page {} was not found in the list'.format(page_name))


def add_new_page(page_name):
    actions.click(new_page_button)
    prompt_input = element('#promptModal #promptModalInput')
    actions.send_keys(prompt_input, page_name)
    actions.click('#promptModal #prompSaveButton')
    actions.wait_for_element_not_visible('#promptModal')
