from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages.users import users
from projects.golem_gui.pages import utils


def setup(data):
    actions.store('username', actions.random_str())
    utils.create_user(data.username, '123456')
    common.access_golem(data.env.url, data.env.admin)
    common.navigate_menu('Users')
    users.wait_for_table_to_load()


def test(data):
    users.click_delete_button(data.username)
    common.confirm_confirm_modal()
    common.assert_toast_message_is_displayed('User deleted')
    assert not users.user_in_table(data.username)

