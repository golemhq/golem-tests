from golem import actions

from projects.golem_gui.pages import index
from projects.golem_gui.pages import login


description = 'Verify that the user can log in to Golem web module'

tags = ['smoke']


def test(data):
    actions.navigate(data.env.url)
    actions.click(login.login_button)
    actions.send_keys(login.username_input, 'admin')
    actions.send_keys(login.password_input, 'admin')
    actions.click(login.login_button)
    actions.assert_element_text(index.title, 'Select a Project')
