from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages.users import user_profile
from projects.golem_gui.pages import utils
from projects.golem_gui.pages import login
from projects.golem_gui.pages import index


def setup(data):
    actions.store('user', utils.create_random_user())
    common.access_golem(data.env.url, data.user)
    common.navigate_menu('User Profile')


def test(data):
    actions.click(user_profile.reset_password_button)
    new_password = '234567'
    user_profile.send_reset_password_prompt(new_password)
    common.assert_toast_message_is_displayed('Password reset')
    common.logout()
    login.login(data.user['username'], new_password)
    actions.assert_element_text(index.title, 'Select a Project')
