from golem import actions
from golem.browser import element

from projects.golem_gui.pages import code_editor


save_button = ('id', 'save', 'Save button')
preview_button = ('id', 'loadGuiButton', 'Preview button')


def assert_error_message(expected_error):
    error_container = element(id='error-container')
    assert error_container.text == expected_error


def save_page():
    actions.click(save_button)
    actions.wait_for_element_present('#toast-container', timeout=5)


def set_value(value):
    code_editor.set_value(value)


def assert_value(value):
    code_editor.assert_value(value)
