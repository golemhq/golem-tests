from golem.browser import element

preview_button = ('id', 'loadGuiButton', 'Preview button')
save_button = ('id', 'save', 'Save button')


def verify_error_message(expected_error):
    error_container = element(id='error-container')
    assert error_container.text == expected_error