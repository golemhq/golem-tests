from golem import actions
from golem.browser import element


save_button = ('id', 'save', 'Save button')
preview_button = ('id', 'loadGuiButton', 'Preview button')


def assert_error_message(expected_error):
    error_container = element(id='error-container')
    assert error_container.text == expected_error


def save_page():
    actions.click(save_button)
    actions.wait_for_element_present('#toast-container', timeout=5)
