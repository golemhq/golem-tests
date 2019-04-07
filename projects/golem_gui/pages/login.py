from golem import actions
from golem.browser import element


username_input = ('id', "username", 'username')
password_input = ('id', "password", 'password')
login_button = ('css', "button[type='submit']", 'login_button')
error_list = ('id', 'errorList', 'Error list')


def login(username, password):
    actions.step('Login with user {}'.format(username))
    element(username_input).send_keys(username)
    element(password_input).send_keys(password)
    element(login_button).click()
