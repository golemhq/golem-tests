from golem.browser import element


new_password_input = ('id', 'resetPasswordInput', 'New Password input')
confirm_new_password_button = ('id', 'resetPasswordConfirm', 'Confirm Password button')


def send_reset_password_prompt(new_password):
    element(new_password_input).send_keys(new_password)
    element(confirm_new_password_button).click()
