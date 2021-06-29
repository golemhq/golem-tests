from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages.users import users
from projects.golem_gui.pages.users import create_user
from projects.golem_gui.pages import utils


def setup(data):
    data.username = actions.random_str()
    utils.create_user(data.username, '123456')
    common.access_golem(data.env.url, data.env.admin)
    common.navigate_menu('Users')
    users.wait_for_table_to_load()


def test(data):
    users.click_edit_button(data.username)
    actions.click(create_user.reset_password_button)
    new_password = '234567'
    create_user.send_reset_password_prompt(new_password)
    common.assert_toast_message_is_displayed('Password reset')
