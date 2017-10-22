from golem import actions
from golem.browser import element, elements


test_name = ('id', 'testName')
description = ('id', 'description')
save_button = ('id', 'save')


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