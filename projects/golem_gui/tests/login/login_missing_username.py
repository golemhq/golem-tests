from golem import actions

from projects.golem_gui.pages import login


description = 'Verify the user cannot log in if username value is missing'


def test(data):
    actions.navigate(data.env.url)
    actions.send_keys(login.password_input, 'admin')
    actions.click(login.login_button)
    actions.take_screenshot('Verify the correct error message is shown')
    actions.assert_element_text(login.error_list, 'Username is required')
