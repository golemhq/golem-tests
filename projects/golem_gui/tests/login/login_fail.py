from golem import actions

from projects.golem_gui.pages import login


def test_login_incorrect_password(data):
    actions.navigate(data.env.url)
    actions.send_keys(login.username_input, 'admin')
    actions.send_keys(login.password_input, 'incorrect password')
    actions.click(login.login_button)
    actions.take_screenshot('Verify the correct error message is shown')
    actions.assert_element_text(login.error_list, 'Username and password do not match')


def test_login_blank_password(data):
    actions.navigate(data.env.url)
    actions.send_keys(login.username_input, 'admin')
    actions.click(login.login_button)
    actions.take_screenshot('Verify the correct error message is shown')
    actions.assert_element_text(login.error_list, 'Password is required')


def test_login_blank_username(data):
    actions.navigate(data.env.url)
    actions.send_keys(login.password_input, 'admin')
    actions.click(login.login_button)
    actions.take_screenshot('Verify the correct error message is shown')
    actions.assert_element_text(login.error_list, 'Username is required')
