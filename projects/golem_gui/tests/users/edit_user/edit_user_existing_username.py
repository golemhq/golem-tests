from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages.users import users
from projects.golem_gui.pages.users import create_user
from projects.golem_gui.pages import utils


def setup(data):
    data.username1 = actions.random_str()
    data.username2 = actions.random_str()
    utils.create_user(data.username1, '123456')
    utils.create_user(data.username2, '123456')
    common.access_golem(data.env.url, data.env.admin)
    common.navigate_menu('Users')
    users.wait_for_table_to_load()


def test(data):
    users.click_edit_button(data.username1)
    actions.clear_element(create_user.username)
    actions.send_keys(create_user.username, data.username2)
    actions.click(create_user.update_user_button)
    common.assert_toast_message_is_displayed('Username {} already exists'.format(data.username2))
